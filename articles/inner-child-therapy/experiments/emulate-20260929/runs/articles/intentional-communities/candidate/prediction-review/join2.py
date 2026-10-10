import json, re, glob, os, collections
C = "/home/claude/joel-articles/articles/inner-child-therapy/experiments/emulate-20260929/runs/articles/intentional-communities/candidate"
texts = json.load(open("texts.json"))
rows = json.load(open("rows2.json"))
for sec in ("s7", "s8"):
    parts = {}; items = {}
    files = sorted(glob.glob(f"{C}/{sec}/**/*.json", recursive=True) + glob.glob(f"{C}/{sec}/**/*.js", recursive=True), key=os.path.getmtime)
    for f in files:
        s = open(f, encoding="utf-8", errors="replace").read()
        objs = []
        if f.endswith(".json"):
            try: objs.append(json.loads(s))
            except Exception: pass
        else:
            for m in re.finditer(r"Object\.assign\(window\.__PARTS,\s*(\{.*?\})\);", s, re.S):
                try: objs.append(json.loads(m.group(1)))
                except Exception: pass
            for m in re.finditer(r"window\.__B\w*\s*=\s*(\[.*?\]);", s, re.S):
                try: objs.append(json.loads(m.group(1)))
                except Exception: pass
            for m in re.finditer(r"(\[\[\".*?\]\]\])", s, re.S):
                try: objs.append(json.loads(m.group(1)))
                except Exception: pass
        for o in objs:
            if isinstance(o, dict):
                for k, v in o.items():
                    if isinstance(v, str) and len(v) > 40: parts[k] = v
                    if isinstance(v, dict):
                        for k2, v2 in v.items():
                            if isinstance(v2, str) and len(v2) > 40: parts.setdefault(k2, v2)
            elif isinstance(o, list):
                for it in o:
                    if isinstance(it, list) and len(it) == 2 and isinstance(it[0], str):
                        if isinstance(it[1], list) and all(isinstance(x, str) for x in it[1]): items[it[0]] = it[1]
                        elif isinstance(it[1], str) and len(it[1]) > 40: parts[it[0]] = it[1]
    n = 0
    for r in rows:
        if r["sec"] != sec or r.get("body"): continue
        i = r["id"]
        if i in parts: r["body"] = parts[i]; n += 1
        elif i in items and all(p in parts for p in items[i]):
            r["body"] = "\n\n".join(parts[p] for p in items[i]); n += 1
    left = [r["id"] for r in rows if r["sec"] == sec and not r.get("body") and r["res"] in ("Human","AI","Mixed","MostlyHuman")]
    print(sec, "parts", len(parts), "items", len(items), "joined", n, "left", len(left), left[:25])
json.dump(rows, open("rows3.json", "w"))
