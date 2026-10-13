"""Write a web-app batch script: install parts into window.__PARTS (hash-checked), build the items from part keys
(joined with a blank line, as __mk does) and submit them. Usage: mkbatch.py spec.json out.js
spec.json: {"batch": "127g", "parts": {key: text}, "items": [[name, [key, ...]], ...]}
Prints each item's word count and sha, so the predictions table can be written before the call."""
import hashlib, json, sys
spec = json.load(open(sys.argv[1], encoding='utf-8'))
parts, items, b = spec['parts'], spec['items'], spec['batch']
h = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()[:12]
js = ('Object.assign(window.__PARTS,%s); const H=%s; const bad=[]; for(const k in H){ if((await __h(window.__PARTS[k]))!==H[k]) bad.push(k);} '
      'window.__B%s=__mk(%s); const r=await __pgSubmit(window.__B%s); "bad "+bad.join(",")+" | "+r.join(" | ")+" | "+new Date().toISOString()') % (
    json.dumps(parts, ensure_ascii=False), json.dumps({k: h(v) for k, v in parts.items()}), b.replace('g', ''),
    json.dumps(items, ensure_ascii=False), b.replace('g', ''))
open(sys.argv[2], 'w', encoding='utf-8').write(js)
known = {}
for k, v in parts.items(): known[k] = v
for name, keys in items:
    missing = [k for k in keys if k not in known]
    t = '\n\n'.join(known[k] for k in keys if k in known)
    print('%-28s %4d words  sha %s%s' % (name, len(t.split()), h(t), ('  (keys installed earlier: %s)' % missing) if missing else ''))
print('script', len(js), 'chars')
