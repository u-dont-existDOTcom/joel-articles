#!/usr/bin/env python3
"""build_batch.py BATCH PREFIX ITEMS_JSON PARTS_JSON... -> vNNN.json and gui/bNNN-first.js

ITEMS_JSON: [[name, [part keys]], ...]. Parts are looked up in the PARTS_JSON files in order
(later files win). Texts are the parts joined by a blank line; each item's sha-256[:12] is
checked in the browser before anything is submitted. The first JS call installs the parts
and submits slice(0,3) and sets window.__B<batch>ok; gui/b<batch>-rest.js submits the rest only when that flag is set
(2026-10-10: the flag and the three-per-call limit were in the section 10 batch files but not in this builder)."""
import json, sys, hashlib, pathlib
batch, prefix, items_path, *parts_paths = sys.argv[1:]
parts = {}
for pp in parts_paths:
    parts.update(json.load(open(pp)))
items = json.load(open(items_path))
texts, H = {}, {}
for name, keys in items:
    t = '\n\n'.join(parts[k] for k in keys)
    texts[name] = t
    H[name] = hashlib.sha256(t.encode()).hexdigest()[:12]
used = sorted({k for _, ks in items for k in ks})
here = pathlib.Path(__file__).resolve().parent
# Headings guard (Joel 2026-09-29: never pick a heading by its Pangram result; candidate headings get a grounding
# review before any Pangram check). My slip in batch 190g tried two unreviewed headings. A heading part that isn't
# published goes in only if headings-grounded.json lists its exact text.
pub = json.load(open(here / 'pub-parts.json'))
pub_heads = {v for k, v in pub.items() if k.startswith('H')}
gpath = here / 'headings-grounded.json'
grounded = set(json.load(open(gpath))) if gpath.exists() else set()
bad_heads = [k for k in used if k.startswith('H') and parts[k] not in pub_heads | grounded]
if bad_heads:
    sys.exit('refused: heading(s) without a grounding record: ' + ', '.join(f'{k} = {parts[k]!r}' for k in bad_heads))
# Lint guard (2026-10-12, section 12): the gate says "Lint every candidate before Pangram, and treat a FAIL as blocking",
# and I still sent four batches (240g to 244g) built on Emulate's "jealousy or God or death or ..." P1, which the linter
# fails (O14, Joel's ban on Emulate's "and ... and" lists); the gate's linter run caught it after the fact. Every part that
# isn't published text or a heading is linted alone here, and a FAIL refuses the batch. The linter is main's
# tools/humanization/tells_lint.py: TELLS_LINT names it, or it's found at the repo root or in the /home/claude/ja-tells worktree.
import os, subprocess, tempfile
def _find_lint():
    cands = [os.environ.get('TELLS_LINT', '')]
    for parent in here.parents:
        cands.append(str(parent / 'tools' / 'humanization' / 'tells_lint.py'))
    cands.append('/home/claude/ja-tells/tools/humanization/tells_lint.py')
    for c in cands:
        if c and pathlib.Path(c).is_file():
            return c
    sys.exit('refused: no linter found; set TELLS_LINT to main\'s tools/humanization/tells_lint.py')
pub_texts = set(pub.values())
lint_path, lint_fails = None, []
for k in used:
    if k.startswith('H') or parts[k] in pub_texts:
        continue
    lint_path = lint_path or _find_lint()
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(parts[k] + '\n')
    r = subprocess.run([sys.executable, lint_path, f.name], capture_output=True, text=True,
                       env={**os.environ, 'TELLS_LINT_PARSE': '0'})
    os.unlink(f.name)
    if 'verdict: FAIL' in r.stdout:
        why = [l.strip() for l in r.stdout.splitlines() if 'HARD:' in l or "flag('FAIL'" in l or 'owner ban' in l][:3]
        lint_fails.append(f'{k}: ' + ' / '.join(why))
if lint_fails:
    sys.exit('refused: the linter fails these parts (fix them or leave them out):\n  ' + '\n  '.join(lint_fails))
json.dump({'batch': batch, 'items': items, 'texts': texts}, open(here / f'v{batch[:-1]}.json', 'w'), ensure_ascii=False, indent=0)
P = {prefix + k: parts[k] for k in used}
js = ("Object.assign(window.__PARTS, " + json.dumps(P, ensure_ascii=False) + "); "
      "const H=" + json.dumps(H) + "; const S=" + json.dumps([[n, [prefix + k for k in ks]] for n, ks in items]) + "; "
      "const bad=[]; window.__B" + batch[:-1] + "=__mk(S); "
      "for(const it of window.__B" + batch[:-1] + "){ if((await __h(it.text))!==H[it.name]) bad.push(it.name);} "
      "window.__B" + batch[:-1] + "ok=!bad.length; "
      "let r=['not sent']; if(!bad.length){ r=await __pgSubmit(window.__B" + batch[:-1] + ".slice(0,3)); } "
      "'bad '+bad.join(',')+' | '+r.join(' | ')+' | '+new Date().toISOString()")
(here / 'gui').mkdir(exist_ok=True)
open(here / 'gui' / f'b{batch[:-1]}-first.js', 'w').write(js)
if len(items) > 3:
    # 2026-10-10 (section 11): the rest goes in calls of five at most, each its own file (rest1, rest2, ...), since a
    # browser-pane script must finish in about 45 seconds (s7 lesson) and a submit takes four to five seconds.
    n = batch[:-1]
    for j, lo in enumerate(range(3, len(items), 5), start=1):
        hi = min(lo + 5, len(items))
        rest = (f"let r=['not sent: first call missing or its hash check failed']; if(window.__B{n}ok && window.__B{n}){{ r=await __pgSubmit(window.__B{n}.slice({lo},{hi})); }} "
                "r.join(' | ')+' | '+new Date().toISOString()")
        open(here / 'gui' / f'b{n}-rest{j}.js', 'w').write(rest)
for n, _ in items:
    print(f'{n}\t{len(texts[n].split())}\t{H[n]}')
