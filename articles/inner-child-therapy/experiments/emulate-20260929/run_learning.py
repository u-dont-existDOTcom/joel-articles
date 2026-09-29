"""Sequential approved learning runs, with published checkpoints between calls."""
import argparse,json,subprocess,sys
from pathlib import Path
p=Path(__file__).resolve().parent;repo=p.parents[3]
parser=argparse.ArgumentParser();parser.add_argument('group',choices=['A','B','C']);args=parser.parse_args()
items=json.loads((p/'runs/input-inventory.json').read_text())['learning']
for item in items:
 if not item['id'].startswith(args.group):continue
 run_id='gpt_'+item['id'].split('_')[0]+'_api_r1'
 rows=[json.loads(l) for l in (p/'runs/emulate.jsonl').read_text().splitlines()]
 if args.group=='B' and item['id']=='B01_m34':
  print('B01 already materialized in website charge test; reuse, no extra first run',flush=True);continue
 if any(r['run_id']==run_id for r in rows):
  print(run_id+' already saved; reuse',flush=True);continue
 if item['words']<40:
  event={'input_file':item['file'],'status':'skipped_below_API_minimum','words':item['words'],'reason':'No authorized grouping rule for learning inputs'}
  with (p/'runs/learning-skips.jsonl').open('a') as f:f.write(json.dumps(event)+'\n')
  subprocess.run([sys.executable,str(p/'checkpoint_experiment.py'),'Record below-minimum learning input'],cwd=repo,check=True)
  print(item['id']+' below40: not submitted',flush=True);continue
 result=subprocess.run([sys.executable,str(p/'emulate_client.py'),run_id,item['file'],'--allocation','learning'],cwd=repo)
 if result.returncode:
  print(run_id+' halted: recover saved reservation before another call',flush=True);sys.exit(result.returncode)
 subprocess.run([sys.executable,str(p/'checkpoint_experiment.py'),'Save exact '+run_id+' output and charge'],cwd=repo,check=True)
print(args.group+' learning group complete',flush=True)
