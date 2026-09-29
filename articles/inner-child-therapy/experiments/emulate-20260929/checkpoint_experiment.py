"""Publish this writer's exact experimental evidence; never read holdout content."""
import hashlib,json,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[4]
branch='gpt/emulate-overnight-20260929'
def git(*args): return subprocess.check_output(['git',*args],cwd=root,text=True).strip()
assert git('branch','--show-current')==branch
head=git('rev-parse','HEAD')
remote=git('ls-remote','origin','refs/heads/'+branch).split()[0]
assert head==remote, 'remote movement requires reconciliation'
prefix='articles/inner-child-therapy/experiments/emulate-20260929/'
exp=root/prefix
pangram=[json.loads(l) for l in (exp/'runs/pangram.jsonl').read_text().splitlines()]
own=[r for r in pangram if r['check_id'].startswith('gpt_')]
emulate=[json.loads(l) for l in (exp/'runs/emulate.jsonl').read_text().splitlines()]
charged=sum(r.get('words_charged',0) for r in emulate if r['run_id'].startswith('gpt_'))
latest=own[-1] if own else {}
queue_file=exp/'runs/active-baseline-queue.json'
queue=json.loads(queue_file.read_text());done={r['check_id'] for r in own}
for entry in queue:
 if entry['check_id'] in done: entry['status']='completed'
queue_file.write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
from datetime import datetime,timezone
now=datetime.now(timezone.utc).isoformat()
me=json.loads((exp/'runs/me-latest.json').read_text())
gate=json.loads((exp/'RUNTIME-GATES.json').read_text())
next_action=('Controlling owner correction: use ChatGPT Work cloud browser per GPT-RESUME-CLOUD-BROWSER.md. This local Codex chat exposes no cloud browser. The ready startup prompt is CLOUD-WORK-START.md. Owner signs in in the cloud; then saved output checks come first. Commit/push every10 results; no PDFs, new registers, reservations or verification layers. Article work and Pro remain pending.' if gate['browser'].get('required_surface')=='ChatGPT Work cloud browser' else 'Pangram browser policy verification is blocked; resume only through an authorized available surface. Article rewriting awaits measured flagged paragraphs; Pro remains pending.')
(exp/'CURRENT-STATE.md').write_text(f'''# Overnight run checkpoint

{now}. Owner outcome OPEN. External submissions approved; PDF downloads disabled after disruptive native Save As dialogs. Detector evidence is exact text snapshots and highlighted spans.

Worker scans saved: {len(own)}; latest Pangram balance {latest.get('credits_after','unread')}; logged worker credit charges {sum(r.get('credits_cost',0) for r in own)}. Five historical rechecks matched earlier labels. Baselines left: {sum(r['status']=='reserved_not_submitted' for r in queue)}; GUI minimum exclusions: {sum('minimum' in r['status'] for r in queue)}.

Worker Emulate charges: {charged}; latest measured balance {me['words_left']} at {me['observed_utc']}. Charge test established two website options cost180 together. A exact Copy capture; B DOM diagnostic only. Website pricing default; API fallback for lossless capture. No article rewrites submitted; E_holdout excluded.

{next_action}

Own branch only; no published article changes or authority promotion. Outcome remains incomplete at the recorded external access boundary.
''')
# Reconcile the entire writer-owned delta, including earlier manual checkpoints.
# Checking only the latest working-tree delta can leave prior artifacts unregistered.
writer_base='c20fb7d8516e162f988ef24c2f0b31a14538eca8'
files=set(git('diff','--name-only',writer_base).splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
index_path=root/'articles/INDEX.json'
index=json.loads(index_path.read_text())
article=next(a for a in index['articles'] if a['id']=='inner-child-therapy')
entries={e['path']:e for e in article['additional_artifacts']}
for rel in sorted(files):
 if not rel.startswith(prefix) or '/E_holdout/' in rel or '__pycache__' in rel: continue
 path=root/rel
 if not path.is_file(): continue
 entries[rel]={'path':rel,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'role':'owner_authorized_emulate_experiment_support','status':'experimental_not_article_authority'}
article['additional_artifacts']=list(entries.values())
index_path.write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
subprocess.run(['git','add','articles/INDEX.json',prefix],cwd=root,check=True)
if not git('diff','--cached','--name-only'): sys.exit(0)
subprocess.run(['git','commit','-q','-m',sys.argv[1]],cwd=root,check=True)
subprocess.run(['git','push','origin',branch],cwd=root,check=True)
