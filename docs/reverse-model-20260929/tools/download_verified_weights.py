"""Segmented/resumable public downloads, installed only after pinned LFS verification.
Never imports Unsloth: its downloader watchdog is deliberately bypassed.
"""
import argparse
import concurrent.futures
import fnmatch
import hashlib
import json
import os
import shutil
import subprocess
import threading
import time
from pathlib import Path
os.environ.setdefault('HF_HOME','/workspace/.hf_home')
os.environ.setdefault('HF_HUB_DISABLE_XET','1')
from huggingface_hub import HfApi, hf_hub_download
MODELS={
 'instruct':('Qwen/Qwen3-30B-A3B-Instruct-2507','0d7cf23991f47feeb3a57ecb4c9cee8ea4a17bfe'),
 'base':('Qwen/Qwen3-30B-A3B-Base','1b75feb79f60b8dc6c5bc769a898c206a1c6a4f9')}
PATTERNS=['*.json','*.safetensors','*.txt','*.model','LICENSE','README.md']

def digest_file(path):
    digest=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024),b''):
            digest.update(block)
    return digest.hexdigest()

def run(args):
    assert shutil.which('aria2c'), 'Install distribution-package aria2; do not change the Python stack'
    model_id,revision=MODELS[args.condition]
    info=HfApi().model_info(model_id,revision=revision,files_metadata=True,token=False)
    assert info.sha==revision
    files=[f for f in info.siblings if any(fnmatch.fnmatch(f.rfilename,p) for p in PATTERNS)]
    assert all('/' not in f.rfilename for f in files)
    weights=[f for f in files if f.rfilename.endswith('.safetensors')]
    assert len(weights)==16
    root=args.root;root.mkdir(parents=True,exist_ok=True)
    hub=Path(os.environ['HF_HOME'])/'hub'/('models--'+model_id.replace('/','--'))
    blobs=hub/'blobs';blobs.mkdir(parents=True,exist_ok=True)
    snapshot=hub/'snapshots'/revision;snapshot.mkdir(parents=True,exist_ok=True)
    temporary=root/('download-pieces-'+args.condition);temporary.mkdir(parents=True,exist_ok=True)
    private_logs=root/'aria2-private';private_logs.mkdir(parents=True,exist_ok=True);private_logs.chmod(0o700)
    evidence=args.evidence;evidence.mkdir(parents=True,exist_ok=True)
    manifest={'model':model_id,'revision':revision,'source':'Hugging Face original pinned repository',
              'tool':subprocess.check_output(['aria2c','--version'],text=True).splitlines()[0],
              'connections_per_file':8,'concurrent_files':4,'max_tries_per_piece':30,
              'verification':'aria2 SHA-256 against Hugging Face LFS oid; Git blob oid for metadata',
              'started_unix':time.time(),'files':[],'status':'RUNNING'}
    lock=threading.Lock()
    def save():
        path=evidence/('download-manifest-'+args.condition+'.json')
        with lock:
            temp=path.with_suffix('.tmp');temp.write_text(json.dumps(manifest,indent=2)+'\n');temp.replace(path)
    save()
    for item in files:
        if item in weights:
            continue
        path=Path(hf_hub_download(model_id,item.rfilename,revision=revision,token=False))
        raw=path.read_bytes();oid=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert oid==item.blob_id, f'Metadata bytes do not match pinned Git oid: {item.rfilename}'
        manifest['files'].append({'filename':item.rfilename,'bytes':len(raw),'git_blob_oid':oid,'verified':True})
        save()
    missing=sum(item.size for item in weights if not (snapshot/item.rfilename).exists())
    assert shutil.disk_usage(root).free>missing+10*1024**3, 'Insufficient disk for missing weights plus working margin'
    def download(item):
        expected=item.lfs.sha256 if hasattr(item.lfs,'sha256') else item.lfs['sha256']
        blob=blobs/expected;destination=snapshot/item.rfilename
        cached=blob.exists() and blob.stat().st_size==item.size and digest_file(blob)==expected
        begin=time.time()
        if not cached:
            target=temporary/item.rfilename
            command=['aria2c','--continue=true','--auto-file-renaming=false','--allow-overwrite=false',
                '--file-allocation=none','--split=8','--max-connection-per-server=8',
                '--min-split-size=16M','--max-tries=30','--retry-wait=3','--timeout=60',
                '--connect-timeout=30','--summary-interval=30','--show-console-readout=false',
                '--console-log-level=warn','--check-integrity=true','--checksum=sha-256='+expected,
                '--dir='+str(temporary),'--out='+item.rfilename,
                'https://huggingface.co/'+model_id+'/resolve/'+revision+'/'+item.rfilename]
            logfile=private_logs/(args.condition+'-'+item.rfilename+'.log')
            with logfile.open('a') as log:
                process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
                for line in process.stdout:
                    log.write(line);log.flush()
                    if line.startswith('[#'):
                        print(json.dumps({'file':item.rfilename,'aria_progress':line.strip()}),flush=True)
                code=process.wait()
            assert code==0, f'aria2 failed for {item.rfilename}; partial pieces retained; inspect private log locally'
            assert target.stat().st_size==item.size
            # aria2's checksum validation is the direct completion gate.
            os.replace(target,blob)
        if destination.is_symlink() and destination.resolve()!=blob.resolve():
            raise RuntimeError('Unexpected pinned snapshot link; preserve and diagnose')
        if not destination.exists():
            destination.symlink_to(Path('../../blobs')/expected)
        record={'filename':item.rfilename,'bytes':item.size,'sha256':expected,
                'verified':True,'verification':'cached SHA-256' if cached else 'aria2 SHA-256',
                'reused_complete_cache':cached,'seconds':time.time()-begin}
        with lock:
            manifest['files'].append(record)
        save();print(json.dumps(record),flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures=[pool.submit(download,item) for item in weights]
        for future in concurrent.futures.as_completed(futures):
            future.result()
    assert len(manifest['files'])==len(files)
    manifest.update(status='COMPLETE',ended_unix=time.time(),total_weight_bytes=sum(item.size for item in weights))
    save();print(json.dumps({'status':'COMPLETE','condition':args.condition,
                           'verified_weight_files':len(weights),'weight_bytes':manifest['total_weight_bytes']}),flush=True)
    if args.start_fit:
        assert args.condition=='instruct'
        subprocess.run(['supervisorctl','start','reverse-pilot-fit'],check=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--condition',choices=list(MODELS),required=True)
    p.add_argument('--root',type=Path,default=Path('/workspace/reverse-pilot-20260929'))
    p.add_argument('--evidence',type=Path,required=True);p.add_argument('--start-fit',action='store_true')
    run(p.parse_args())
