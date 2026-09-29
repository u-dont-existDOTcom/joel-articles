"""One authorized Emulate request, exact response capture and budget reservation."""
import argparse,hashlib,json,os,subprocess,time,urllib.request,urllib.error
from pathlib import Path
from datetime import datetime,timezone
p=Path(__file__).resolve().parent
repo=p.parents[3]
a=argparse.ArgumentParser();a.add_argument('run_id');a.add_argument('input_file');a.add_argument('--allocation',choices=['learning','article_first','second'],required=True);args=a.parse_args()
assert subprocess.check_output(['git','branch','--show-current'],cwd=repo,text=True).strip()=='gpt/emulate-overnight-20260929'
rel=Path(args.input_file);assert not rel.is_absolute() and '..' not in rel.parts
assert 'E_holdout' not in rel.parts and 'REFERENCE_ONLY' not in str(rel)
assert (str(rel).startswith('inputs/learning/') and rel.suffix=='.txt') or (str(rel).startswith('runs/') and rel.suffix in ['.md','.txt'])
text=(p/rel).read_bytes().decode('utf-8');words=len(text.split());assert 40<=words<=3000
out=p/'runs/emulate'/f'{args.run_id}.txt';assert not out.exists(), 'existing run: recover, never repeat'
rows=[json.loads(l) for l in (p/'runs/emulate.jsonl').read_text().splitlines()]
limits={'learning':5000,'article_first':38600,'second':12000}
used=sum(r.get('words_charged',0) for r in rows if r.get('allocation','learning' if r.get('run_id','').startswith('gpt_charge_') else 'historical')==args.allocation)
assert used+words<=limits[args.allocation],f'allocation boundary {used}+{words}>{limits[args.allocation]}'
key=os.environ.get('EMULATE_API_KEY') or Path('/home/joel/ai-work/claude-dangerous-lane/secrets/emulate.key').read_text().strip()
def request(path,body=None):
 data=None if body is None else json.dumps(body,ensure_ascii=False).encode()
 req=urllib.request.Request('https://www.tryemulate.ai'+path,data=data,headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=60) as r:return json.loads(r.read())
me=request('/v1/me');assert me['words_left']-words>=2000, 'reserve boundary'
reservation={'run_id':args.run_id,'input_file':str(rel),'input_words':words,'input_sha256':hashlib.sha256(text.encode()).hexdigest(),'allocation':args.allocation,'started_utc':datetime.now(timezone.utc).isoformat(),'status':'reserved_before_POST','balance_before':me['words_left']}
reserve=p/'runs/emulate'/f'{args.run_id}.reservation.json';assert not reserve.exists(),'reserved run: recover before repeat'
reserve.write_text(json.dumps(reservation,indent=2)+'\n')
response=None
for attempt in range(2):
 try:response=request('/v1/humanize',{'text':text});break
 except urllib.error.HTTPError as e:
  error={'status':e.code,'body':e.read().decode('utf8',errors='replace'),'attempt':attempt+1}
  (p/'runs/emulate'/f'{args.run_id}.error{attempt+1}.json').write_text(json.dumps(error,indent=2)+'\n')
  if e.code==503 and attempt==0:time.sleep(30);continue
  if e.code==502 and attempt==0:continue
  reservation['status']='error_no_automatic_resubmit';reserve.write_text(json.dumps(reservation,indent=2)+'\n');raise SystemExit(f'HTTP {e.code}; saved error, not repeated')
assert isinstance(response,dict) and isinstance(response.get('text'),str)
out.write_bytes(response['text'].encode('utf8'))
charged=response['words']['charged'];reservation.update(status='completed',provider_id=response['id'],words_charged=charged);reserve.write_text(json.dumps(reservation,indent=2)+'\n')
row={**reservation,'style':{'transport':'API','requested':'Auto','resolved_style':'not exposed by API'},'output_file':str(out.relative_to(p)),'output_words':len(response['text'].split()),'output_sha256':hashlib.sha256(response['text'].encode()).hexdigest(),'response':response,'notes':'Authorized lossless API fallback; exact provider text, no editing.'}
with (p/'runs/emulate.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
lint=subprocess.run(['python3',str(repo/'articles/inner-child-therapy/tools/tells_lint.py'),str(out)],capture_output=True,text=True);out.with_suffix('.lint.txt').write_text(lint.stdout+lint.stderr)
subprocess.run(['python3',str(p/'mechanical.py'),str(p/rel),str(out),str(p/'runs/align'/f'{args.run_id}.json')],check=True)
print(json.dumps({'run_id':args.run_id,'charged':charged,'output_words':row['output_words'],'reads_human_provider_claim':response.get('reads_human'),'allocation_used':used+charged}))
