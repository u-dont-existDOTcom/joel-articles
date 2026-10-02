import json, re, sys, subprocess, hashlib

# usage: append_rec.py D FILE < page_result.json
# stdin: the exact JSON object that pg_read.js returned from the page.
D, FILE = sys.argv[1], sys.argv[2]
page = json.loads(sys.stdin.read())
block = page["block"]

text = open(D + "/" + FILE, encoding="utf-8").read().strip()
words_local = len(text.split())
sha12 = hashlib.sha256((text + "\n").encode()).hexdigest()[:12]

m = re.search(r"\n([^\n]+)\n(\d[\d\s,.]*?)\s*words scanned", block)
label = m.group(1).strip() if m else None
words_page = int(re.sub(r"\D", "", m.group(2))) if m else None

pm = re.search(r"\n(\d+(?:\.\d+)?)\n%\nof this text is ([^\n]+)", block)
percent = float(pm.group(1)) if pm else None
if percent is not None and percent == int(percent):
    percent = int(percent)
percent_of = pm.group(2).strip() if pm else None

bm = re.search(r"\nAI\n(\d+(?:\.\d+)?)%\nHuman\n(\d+(?:\.\d+)?)%", block)
breakdown = None
if bm:
    breakdown = {"ai_percent": float(bm.group(1)), "human_percent": float(bm.group(2))}
    for k in breakdown:
        if breakdown[k] == int(breakdown[k]):
            breakdown[k] = int(breakdown[k])

utc = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"]).decode().strip()

rec = {
    "file": FILE,
    "words": words_page,
    "label": label,
    "percent": percent,
    "spans": page["spans"],
    "credits_before": page["before"],
    "credits_after": page["after"],
    "utc": utc,
    "percent_of": percent_of,
    "words_local": words_local,
    "sha12": sha12,
    "ok": page["ok"],
    "block": block,
}
if breakdown:
    rec.update(breakdown)
if len(sys.argv) > 3:
    rec.update(json.loads(sys.argv[3]))
line = json.dumps(rec, ensure_ascii=False)
with open(D + "/pangram-s3.jsonl", "a", encoding="utf-8") as f:
    f.write(line + "\n")
print(line)
