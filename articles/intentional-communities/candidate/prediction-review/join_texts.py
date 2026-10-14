import json, re, glob, os
C = "/home/claude/joel-articles/articles/inner-child-therapy/experiments/emulate-20260929/runs/articles/intentional-communities/candidate"
texts = {}
# 1) vNNN.json texts (s9, s10)
for f in glob.glob(C + "/s*/v*.json"):
    try: d = json.load(open(f))
    except Exception: continue
    if isinstance(d, dict) and isinstance(d.get("texts"), dict):
        for k, v in d["texts"].items():
            if isinstance(v, str): texts.setdefault(k, v)
# 2) generic: any json/js file with "id": "text" pairs or [id, text] pairs
pat = re.compile(r'"((?:\d+g?|z|s\d+pub|pub)-[A-Za-z0-9_.\-]+)"\s*[:,]\s*"((?:[^"\\]|\\.){120,})"')
for f in glob.glob(C + "/s*/**/*.js", recursive=True) + glob.glob(C + "/s*/**/*.json", recursive=True):
    try: s = open(f, encoding="utf-8", errors="replace").read()
    except Exception: continue
    for m in pat.finditer(s):
        k = m.group(1)
        try: v = json.loads('"' + m.group(2) + '"')
        except Exception: continue
        texts.setdefault(k, v)
json.dump(texts, open("texts.json", "w"))
rows = json.load(open("rows.json"))
def rid(r):
    t = re.sub(r"[*`]", "", r["text"]).strip()
    m = re.match(r"([^\s(:,]+)", t)
    return m.group(1) if m else t
hit = 0; miss = []
for r in rows:
    r["id"] = rid(r)
    r["body"] = texts.get(r["id"])
    if r["body"]: hit += 1
    elif r["res"] in ("Human","AI","Mixed","MostlyHuman"): miss.append((r["sec"], r["id"]))
json.dump(rows, open("rows2.json", "w"))
import collections
print("texts", len(texts), "rows with text", hit, "of", len(rows))
print(collections.Counter(s for s, _ in miss))
print([i for s, i in miss if s in ("s9", "s10")][:40])
print([i for s, i in miss if s in ("s8",)][:40])
print([i for s, i in miss if s in ("s7",)][:40])
