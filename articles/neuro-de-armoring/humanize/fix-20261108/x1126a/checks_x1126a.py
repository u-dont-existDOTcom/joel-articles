"""One batch of web-app checks for x1126a (the desktop app's browser pane, signed in to his account this turn): write each text's prediction into the lane's ledger first, then (after the
checks ran in his browser and RESULTS-GUI.json holds what his history returned, read by SHA-256) record the results.

  python3 .../x1125a/checks_x1125a.py predict DIR      DIR/IN.json -> texts/, TEXTS.json, PREDICTIONS.json, ITEMS.js
  python3 .../x1125a/checks_x1125a.py record DIR --title "..."

DIR/IN.json: {key: {"lineage", "scope", "name", "text", "chance", "tells", "human_tells", "diagnosis", "decides",
"receipt" (a path) or "unchanged" ("what and where"), "humanized", "first_fix", "panel", "big_change"}}.
ITEMS.js is the [[key, text, sha256], ...] list window.__run and window.__readFull take.
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
LEDGER = H / 'pangram-ledger.jsonl'
DETECTOR = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"
OPT = {'tells': '--tells', 'human_tells': '--human-tells', 'diagnosis': '--diagnosis', 'decides': '--decides',
       'receipt': '--receipt', 'unchanged': '--unchanged', 'humanized': '--humanized', 'first_fix': '--first-fix',
       'panel': '--panel', 'big_change': '--big-change', 'narrowed': '--narrowed'}


def predict(D, batch):
    items = json.loads((D / 'IN.json').read_text(encoding='utf-8'))
    done = set()
    for line in LEDGER.read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        if r.get('batch') == batch and r.get('type', 'prediction') != 'result':
            done.add((r.get('key'), r.get('sha256')))
    (D / 'texts').mkdir(exist_ok=True)
    texts, rows, js = {}, [], []
    for key, p in items.items():
        t = p['text']
        sha = hashlib.sha256(t.encode('utf-8')).hexdigest()
        call = 'Human' if p['chance'] >= 0.5 else 'AI'
        f = D / 'texts' / (key + '.txt')
        f.write_text(t, encoding='utf-8')
        texts[key] = t
        rows.append({'key': key, 'name': p['name'], 'lineage': p['lineage'], 'scope': p.get('scope', 'paragraph'),
                     'words': len(t.split()), 'call': call, 'chance': p['chance'], 'why': 'see the ledger record',
                     'sha256': sha})
        js.append([key, t, sha])
        if (key, sha) in done:
            print(key, 'already predicted in', batch)
            continue
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', p['lineage'], '--scope', p.get('scope', 'paragraph'), '--text', str(f), '--call', call,
               '--chance', str(p['chance']), '--key', key, '--batch', batch, '--detector', DETECTOR]
        for k, o in OPT.items():
            if p.get(k):
                cmd += [o, p[k]]
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(key, (r.stdout + r.stderr).strip()[-900:])
        if r.returncode:        # refused: it stays out of this batch, and the others go on
            rows.pop(); js.pop(); texts.pop(key); f.unlink()
            print(key, 'NOT IN THE BATCH')
    (D / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (D / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (D / 'ITEMS.js').write_text(json.dumps(js, ensure_ascii=False), encoding='utf-8')


def record(D, title):
    subprocess.run([sys.executable, str(H / 'fix-20261104' / 'checks' / 'record_gui.py'), str(D), '--title', title],
                   check=True)


if __name__ == '__main__':
    what, D = sys.argv[1], pathlib.Path(sys.argv[2]).resolve()
    if what == 'predict':
        predict(D, sys.argv[sys.argv.index('--batch') + 1])
    else:
        record(D, sys.argv[sys.argv.index('--title') + 1])
