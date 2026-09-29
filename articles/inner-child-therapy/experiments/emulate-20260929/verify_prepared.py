"""Verify saved artifact identity and exact splice endpoints; never read holdout."""
import json,sys
from pathlib import Path
p=Path(__file__).resolve().parent
sys.path.insert(0,str(p))
from mechanical import digest,splice

def read(rel):
 assert 'E_holdout' not in str(rel)
 return (p/rel).read_bytes().decode('utf8')
def load(rel):return json.loads(read(rel))
rows=[json.loads(l) for l in read('runs/emulate.jsonl').splitlines()]
for r in rows:
 output=read(r['output_file']);source=read(r['input_file'])
 if 'output_sha256' in r:assert digest(output)==r['output_sha256'],r['run_id']
 if 'response' in r:assert output==r['response']['text'],r['run_id']
 assert (p/r['output_file']).with_suffix('.lint.txt').exists(),r['run_id']
 alignment=load('runs/align/'+r['run_id']+'.json')
 assert ''.join(u['source_text'] for u in alignment['units'])==source
 assert ''.join(u['output_text'] for u in alignment['units'])==output
for r in load('runs/part3-check-queue.json')+load('runs/part4-check-queue.json'):
 text=read(r['text_file']);assert digest(text)==r['text_sha256'],r['check_id']
 assert r['status'] in ['blocked_browser_policy','excluded_gui_minimum','completed_from_exact_saved_result']
 if r['variant']=='output_paragraph':
  base=read(next(v['output_file'] for v in rows if v['run_id']==r['run_id']))
  assert text==base[r['output_start']:r['output_end']]
 if r['variant']=='context':
  base=read(next(v['output_file'] for v in rows if v['run_id']==r['run_id']))
  assert text==read(r['context_file'])+'\n\n'+base
 kind=r.get('experiment_kind')
 if kind in ['forward','backward','cumulative']:
  alignment=load(f"runs/align/{r['pair_run_id']}_{r['unit_kind']}.json")
  assert text==splice(alignment,r['selected_units'],backward=kind=='backward')
 if kind=='edit':
  base=read('runs/emulate/'+r['base_run_id']+'.txt')
  assert r['own_words'] and r['author']=='Codex model'
  if r['edit_type']=='one_word':
   a,b=r['range'];assert base[a:b]==r['old'];assert text==base[:a]+r['new']+base[b:]
   assert len(base.split())==len(text.split())
  elif r['edit_type']=='model_sentence_rewrite':assert text==base.replace(r['old'],r['new'],1)
  else:assert text==base+' '+r['new']
 if kind=='context_swap':
  alignment=load('runs/align/B01_context_fail_to_pass.json')
  assert text==read('inputs/learning/CONTEXT_section_so_far.txt')+'\n\n'+splice(alignment,r['selected_units'])
for r in load('runs/part4-qualified-seed-pairs.json')['pairs']:
 source=read(r['input_file']);output=read(r['output_file'])
 for kind in ['sentence','paragraph']:
  rel=f"runs/align/{r['run_id']}_{kind}.json"
  if not (p/rel).exists():continue
  a=load(rel);all_units=range(len(a['units']))
  assert splice(a,[])==source and splice(a,all_units)==output
  assert splice(a,[],True)==output and splice(a,all_units,True)==source
print('PASS: exact provider bytes, alignment reconstruction, paragraph/context identity, splice endpoints and 12 labelled edit operations; no holdout read')
