"""Prepare exact, unsubmitted detector texts. No browser or paid API calls."""
import json,re,subprocess,sys
from pathlib import Path
p=Path(sys.argv[1]).resolve();sys.path.insert(0,str(p))
from mechanical import align,splice,digest,paragraph_spans
repo=p.parents[3]
def read(rel):
 assert 'E_holdout' not in str(rel)
 return (p/rel).read_bytes().decode('utf8')
def write(rel,text):
 target=p/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(text.encode('utf8'))
def jwrite(rel,data): write(rel,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
rows=[json.loads(l) for l in read('runs/emulate.jsonl').splitlines()]
scores=[json.loads(l) for l in read('runs/pangram.jsonl').splitlines()]
cache={digest(read(r['text_file'])):r['check_id'] for r in scores}
jobs=[]
def job(check_id,rel,variant,**details):
 text=read(rel);words=len(text.split());sha=digest(text)
 status=('completed_from_exact_saved_result' if sha in cache else 'excluded_gui_minimum' if words<50 else 'blocked_browser_policy')
 record={'check_id':check_id,'text_file':rel,'text_sha256':sha,'variant':variant,'words':words,'status':status,**details}
 if sha in cache:record['cached_check_id']=cache[sha]
 jobs.append(record)
 return record
context=read('inputs/learning/CONTEXT_section_so_far.txt')
for r in rows:
 rid=r['run_id'];out=r['output_file'];text=read(out)
 if 'DOM_DIAGNOSTIC_ONLY' in out:
  report=(p/out).with_suffix('.lint.txt')
  result=subprocess.run(['python3',str(repo/'articles/inner-child-therapy/tools/tells_lint.py'),str(p/out)],capture_output=True,text=True)
  report.write_text(result.stdout+result.stderr)
  diagnostic=align(read(r['input_file']),text)
  diagnostic['provenance']='DOM DIAGNOSTIC ONLY; exact Copy requirement unmet; excluded from paid check queue'
  jwrite(f'runs/align/{rid}.json',diagnostic)
  continue
 if not (p/'runs/align'/f'{rid}.json').exists():jwrite(f'runs/align/{rid}.json',align(read(r['input_file']),text))
 job('part3_'+rid,out,'output',run_id=rid)
 parts=paragraph_spans(text)
 if len(parts)>1:
  for n,part in enumerate(parts,1):
   rel=f'runs/prepared/paragraphs/{rid}_p{n:02}.txt';write(rel,part['text'])
   job(f'part3_{rid}_p{n:02}',rel,'output_paragraph',run_id=rid,output_start=part['start'],output_end=part['end'])
 if 'B01' in rid or 'B05' in rid:
  rel=f'runs/prepared/context/{rid}.txt';write(rel,context+'\n\n'+text)
  job('part3_context_'+rid,rel,'context',run_id=rid,context_file='inputs/learning/CONTEXT_section_so_far.txt',join='exact context bytes + two LF + exact output bytes')
 # Ensure every exact provider output has a lint artifact (no provider modification).
 report=p/out;report=report.with_suffix('.lint.txt')
 if not report.exists():
  result=subprocess.run(['python3',str(repo/'articles/inner-child-therapy/tools/tells_lint.py'),str(p/out)],capture_output=True,text=True)
  report.write_text(result.stdout+result.stderr)
jwrite('runs/part3-check-queue.json',jobs)
p4=[];pairs=[]
def p4job(check_id,text,kind,**meta):
 rel=f'runs/prepared/part4/{check_id}.txt';write(rel,text)
 r=job(check_id,rel,'splice' if kind!='edit' else 'edit',experiment_kind=kind,**meta);p4.append(r)
seed=[r for r in rows if r['run_id'].startswith('claude_test_')]
for r in seed:
 rid=r['run_id'];source=read(r['input_file']);output=read(r['output_file'])
 before=next((s for s in scores if s['variant']=='baseline' and s['text_file']==r['input_file'] and s['percent'].get('AI',0)>=80),None)
 after=next((s for s in scores if s['variant']=='output' and s['text_file']==r['output_file'] and s['label']=='Human Written' and not s['flagged_spans']),None)
 if not before or not after:continue
 pairs.append({'run_id':rid,'input_file':r['input_file'],'output_file':r['output_file'],'baseline_check_id':before['check_id'],'output_check_id':after['check_id'],'multi_paragraph':len(paragraph_spans(source))>1,'provenance':'historical Claude output result; fresh worker source recheck; heuristic alignment unreviewed'})
 for mode in ['sentence','paragraph']:
  if mode=='paragraph' and len(paragraph_spans(source))<2:continue
  alignment=align(source,output,unit_kind=mode)
  jwrite(f'runs/align/{rid}_{mode}.json',alignment)
  n=len(alignment['units'])
  assert splice(alignment,[])==source and splice(alignment,range(n))==output
  assert splice(alignment,[],backward=True)==output and splice(alignment,range(n),backward=True)==source
  for i in range(n):
   for backward,name in [(False,'forward'),(True,'backward')]:
    p4job(f'part4_{rid}_{mode}_{name}_{i+1:02}',splice(alignment,[i],backward),name,pair_run_id=rid,unit_kind=mode,selected_units=[i],own_words=False)
  if mode=='sentence':
   for i in range(n):
    p4job(f'part4_{rid}_cumulative_{i+1:02}',splice(alignment,range(i+1)),'cumulative',pair_run_id=rid,unit_kind=mode,selected_units=list(range(i+1)),stop_after_first_Human=True,own_words=False)
# These are only labelled Part 4.3 experiments; they are never editorial corrections.
edits={
 'claude_test_B01_m34_opt1':('midnight','bedtime','The warm fuzzy feelings can come later.','You may begin to feel warmth toward your little one later.','You can choose a different act next time.'),
 'claude_test_B01_m34_opt2':('meal','breakfast','It’s okay for the Protector to go first.','It’s all right for the Protector to start.','You can review the result before choosing another act.'),
 'claude_test_B02_after_a_opt1':('friend','helper',"On the other hand, if you didn't do the thing you had planned to, don't jump to conclusions.","If you didn't do what you planned, wait before deciding why.",'You can think about what happened before making another plan.'),
 'claude_test_B02_after_a_opt2':('friend','helper','Then reflect on whether you did it or not.','Then check whether you did what you said you would do.','You can consider the reason before making another plan.')}
for rid,(old,new,sent,rewrite,added) in edits.items():
 output=read(f'runs/emulate/{rid}.txt')
 match=re.search(r'\b'+re.escape(old)+r'\b',output);assert match
 text=output[:match.start()]+new+output[match.end():]
 p4job(f'part4_{rid}_edit_a',text,'edit',base_run_id=rid,edit_type='one_word',old=old,new=new,range=[match.start(),match.end()],author='Codex model',own_words=True,label='ONLY Part4.3; ungraded; never article prose')
 assert output.count(sent)==1
 p4job(f'part4_{rid}_edit_b',output.replace(sent,rewrite,1),'edit',base_run_id=rid,edit_type='model_sentence_rewrite',old=sent,new=rewrite,author='Codex model',own_words=True,label='ONLY Part4.3; semantic equivalence unreviewed by Pro')
 p4job(f'part4_{rid}_edit_c',output+' '+added,'edit',base_run_id=rid,edit_type='model_sentence_addition',new=added,author='Codex model',own_words=True,label='ONLY Part4.3; ungraded; never article prose')
# Owner named the B01 contextual swap as an existing case. No synthetic words.
failing=read('runs/emulate/claude_test_B01_m34_opt2.txt');passing=read('runs/emulate/claude_test_B01_m34_opt1.txt')
alignment=align(failing,passing);jwrite('runs/align/B01_context_fail_to_pass.json',alignment)
flag=next(s for s in scores if s['check_id']=='claude_test_ctx_B01_opt2')['flagged_spans'][0]
assert failing.startswith(flag)
flagunits=[i for i,u in enumerate(alignment['units']) if u['source_start']<len(flag) and u['source_end']>0]
for i in flagunits:
 p4job(f'part4_B01_context_swap_{i+1:02}',context+'\n\n'+splice(alignment,[i]),'context_swap',failing_run_id='claude_test_B01_m34_opt2',passing_run_id='claude_test_B01_m34_opt1',selected_units=[i],own_words=False,semantic_coverage='UNREVIEWED_BY_PRO; heuristic alignment, no same-point/order certification')
# P4 materializations enter the same explicit gate; no submissions here.
jwrite('runs/part4-check-queue.json',p4)
jwrite('runs/part4-qualified-seed-pairs.json',{'required_pairs':12,'required_multi_paragraph':4,'available_version_pairs':len(pairs),'distinct_inputs':len({r['input_file'] for r in pairs}),'available_multi_paragraph':sum(r['multi_paragraph'] for r in pairs),'pairs':pairs,'qualification':'Four historical versions, not twelve completed pairs; newly generated outputs await Pangram'})
summary={'provider_outputs':len(rows),'diagnostic_only_outputs':sum('DOM_DIAGNOSTIC_ONLY' in r['output_file'] for r in rows),'part3_jobs':len(jobs)-len(p4),'part4_jobs':len(p4),'part4_edited_texts':12,'browser_submissions_executed':0,'new_detector_results_inferred':0,'E_holdout_read':False}
jwrite('runs/preparation-summary.json',summary)
print(json.dumps(summary))
