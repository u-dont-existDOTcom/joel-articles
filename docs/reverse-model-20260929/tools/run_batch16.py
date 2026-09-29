import json,subprocess,time,shutil
from pathlib import Path
root=Path('/workspace/reverse-pilot-20260929')
repo=root/'repo'; data=repo/'docs/reverse-model-20260929/data'; tools=repo/'docs/reverse-model-20260929/tools'
out=data/'generated'; history=out/'run-history';history.mkdir(exist_ok=True)
for name in ['generation-manifest.json','generation-status.json']:
    if (out/name).exists(): shutil.copy2(out/name,history/('initial12-'+name))
receipt={'started_unix':time.time(),'repo_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip(),'batch_size':16,'new_passage_limit':16,'deadline_seconds':3600}
(root/'batch16-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
r=subprocess.run(['/venv/main/bin/python','-u',str(tools/'generate_pairs.py'),'--input',str(data/'human-passages.jsonl'),'--output',str(out),'--batch-size','16','--limit','16','--deadline-unix',str(time.time()+3600)])
receipt.update(ended_unix=time.time(),returncode=r.returncode)
(root/'batch16-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
raise SystemExit(r.returncode)
