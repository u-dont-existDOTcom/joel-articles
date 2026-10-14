"""Build apiNN.json from a parts file and a spec: python3 build.py parts.json spec.json out.json
spec = {"entry name": ["part key", "part key", ...], ...}; each entry is its parts joined by a blank line.
Parts files are merged in order if several are given as parts1.json,parts2.json. Prints the sha256 of the written JSON
(json.dumps of the loaded file, ensure_ascii=False), the total words and the entry count.
(Copy of the laptop's pangram-runs/community-s5/build.py, 2026-10-06; used for API batch 72, which the exhausted key refused.)"""
import json, hashlib, sys
P = {}
for f in sys.argv[1].split(','):
    P.update(json.load(open(f, encoding='utf-8')))
S = json.load(open(sys.argv[2], encoding='utf-8'))
d = {k: '\n\n'.join(P[x] for x in v) for k, v in S.items()}
open(sys.argv[3], 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
print(hashlib.sha256(json.dumps(json.load(open(sys.argv[3], encoding='utf-8')), ensure_ascii=False).encode()).hexdigest(), sum(len(v.split()) for v in d.values()), len(d))
