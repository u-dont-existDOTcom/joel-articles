#!/usr/bin/env python3
"""build_batch.py BATCH PREFIX ITEMS_JSON PARTS_JSON... -> vNNN.json and gui/bNNN-first.js

ITEMS_JSON: [[name, [part keys]], ...]. Parts are looked up in the PARTS_JSON files in order
(later files win). Texts are the parts joined by a blank line; each item's sha-256[:12] is
checked in the browser before anything is submitted. The first JS call installs the parts
and submits slice(0,5); later calls submit window.__B<batch>.slice(n, n+5)."""
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
json.dump({'batch': batch, 'items': items, 'texts': texts}, open(here / f'v{batch[:-1]}.json', 'w'), ensure_ascii=False, indent=0)
P = {prefix + k: parts[k] for k in used}
js = ("Object.assign(window.__PARTS, " + json.dumps(P, ensure_ascii=False) + "); "
      "const H=" + json.dumps(H) + "; const S=" + json.dumps([[n, [prefix + k for k in ks]] for n, ks in items]) + "; "
      "const bad=[]; window.__B" + batch[:-1] + "=__mk(S); "
      "for(const it of window.__B" + batch[:-1] + "){ if((await __h(it.text))!==H[it.name]) bad.push(it.name);} "
      "let r=['not sent']; if(!bad.length){ r=await __pgSubmit(window.__B" + batch[:-1] + ".slice(0,5)); } "
      "'bad '+bad.join(',')+' | '+r.join(' | ')+' | '+new Date().toISOString()")
(here / 'gui').mkdir(exist_ok=True)
open(here / 'gui' / f'b{batch[:-1]}-first.js', 'w').write(js)
for n, _ in items:
    print(f'{n}\t{len(texts[n].split())}\t{H[n]}')
