import re, json, sys, glob, os
C = "/home/claude/joel-articles/articles/inner-child-therapy/experiments/emulate-20260929/runs/articles/intentional-communities/candidate"
rows = []
def norm_pred(s):
    t = re.sub(r"[*_`]", "", s).strip().lower()
    if t.startswith("ai"): return "AI"
    if t.startswith("human"): return "Human"
    if t.startswith("mixed"): return "Mixed"
    return "other"
def norm_res(s):
    t = re.sub(r"[*_`]", "", s).strip()
    tl = t.lower()
    if not t or tl.startswith("not run") or tl.startswith("not sent") or tl.startswith("—") or tl.startswith("-") or "discard" in tl[:40]:
        return "none", None
    m = re.search(r"(\d+(?:\.\d+)?)\s*%\s*ai", tl)
    pct = float(m.group(1)) if m else None
    if tl.startswith("human"):
        if "mostly human" in tl: return "MostlyHuman", pct
        return "Human", pct if pct is not None else 0.0
    if tl.startswith("ai"):
        return "AI", pct if pct is not None else 100.0
    if tl.startswith("mostly human"): return "MostlyHuman", pct
    if tl.startswith("mixed"):
        return "Mixed", pct
    m2 = re.match(r"(\d+(?:\.\d+)?)\s*%\s*ai", tl)
    if m2:
        p = float(m2.group(1))
        return ("Human" if p == 0 else "AI" if p >= 99.5 else "Mixed"), p
    return "unparsed", None
for f in sorted(glob.glob(C + "/s*/PREDICTIONS-*.md")):
    sec = os.path.basename(os.path.dirname(f))
    lines = open(f).read().split("\n")
    hdr = None; batchline = None
    for i, ln in enumerate(lines):
        if not ln.startswith("|"):
            if ln.strip(): batchline = ln[:200] if ln.startswith("Batch") else batchline
            hdr = None if not ln.strip()=="" else hdr
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells if c): continue
        low = [c.lower() for c in cells]
        if "mine" in low and any(c.startswith("pangram") for c in low):
            hdr = {"text": 0, "mine": low.index("mine"), "why": next((k for k,c in enumerate(low) if c.startswith("why")), None), "res": next(k for k,c in enumerate(low) if c.startswith("pangram"))}
            continue
        if not hdr: continue
        if len(cells) <= hdr["res"]:
            # tolerate '||' merges
            continue
        resc = cells[hdr["res"]]
        if not resc.strip():
            tail = [c for c in cells[hdr["res"]+1:] if c.strip()]
            resc = tail[-1] if tail else ""
        r = {"sec": sec, "line": i+1, "text": cells[0], "mine_raw": cells[hdr["mine"]], "why": cells[hdr["why"]] if hdr["why"] is not None else "", "res_raw": resc, "batch": batchline}
        r["mine"] = norm_pred(r["mine_raw"]); r["res"], r["pct"] = norm_res(r["res_raw"])
        m = re.match(r"\**(\d+g?)-", r["text"]); r["bid"] = m.group(1) if m else None
        rows.append(r)
json.dump(rows, open("rows.json","w"), indent=0)
from collections import Counter
print(len(rows))
print(Counter((r["sec"]) for r in rows))
print(Counter(r["res"] for r in rows))
print(Counter(r["mine"] for r in rows))
for r in rows:
    if r["res"] in ("unparsed",) : print("UNPARSED", r["sec"], r["line"], r["res_raw"][:100])
