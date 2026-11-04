"""One batch of paragraph checks for the neuro de-armoring lane (2026-11-04): each text checked by itself, its prediction
written into the lane's ledger first (gate E307), one paragraph per text (Joel, 2026-11-04 10:01 UTC: "just work on one
paragraph at a time so you can see whether your strat is working").

DIR/IN.json: {key: {"lineage", "name", "text", "chance" (my chance of a 100% Human result), "why", "diagnosis",
"decides", and "panel" (the PANEL.md, after two AI reads: E346)}}. Writes DIR/TEXTS.json, DIR/PREDICTIONS.json (the list record_r1102.py reads) and DIR/texts/KEY.txt; a key
already predicted in the batch at the same text is not predicted again.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/checks/predict_batch.py DIR --batch BATCH [--detector WHO]

--detector names who runs the checks when it isn't the API: from batch x1104k Joel checks each paragraph in Pangram's web
app with his account's credits (his message of 2026-11-04 14:59 UTC: "i'm not topping up the api unless you think it's
really important because we have tons of gui credits still").
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
LEDGER = H / 'pangram-ledger.jsonl'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218, E325: one paragraph per text, 2026-11-04)'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dir')
    ap.add_argument('--batch', required=True)
    ap.add_argument('--detector', default=DETECTOR, help='who runs the checks, and where (the API by default)')
    a = ap.parse_args()
    D = pathlib.Path(a.dir).resolve()
    items = json.loads((D / 'IN.json').read_text(encoding='utf-8'))
    done = set()
    for line in LEDGER.read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        if r.get('batch') == a.batch and r.get('type', 'prediction') != 'result':
            done.add((r.get('key'), r.get('sha256')))
    (D / 'texts').mkdir(exist_ok=True)
    texts, rows = {}, []
    for key, p in items.items():
        t = p['text']
        paras = [x for x in t.split('\n\n') if len(x.split()) >= 8]
        assert len(paras) <= 2, (key, 'one paragraph per text (a heading of eight words or more counts as one)')
        texts[key] = t
        sha = hashlib.sha256(t.encode('utf-8')).hexdigest()
        call = 'Human' if p['chance'] >= 0.5 else 'AI'
        rows.append({'key': key, 'name': p['name'], 'lineage': p['lineage'], 'scope': 'paragraph',
                     'words': len(t.split()), 'call': call, 'chance': p['chance'], 'why': p['why'], 'sha256': sha})
        f = D / 'texts' / (key + '.txt')
        f.write_text(t, encoding='utf-8')
        if (key, sha) in done:
            print(key, 'already predicted in', a.batch)
            continue
        subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                        '--lineage', p['lineage'], '--scope', 'paragraph', '--text', str(f), '--call', call,
                        '--chance', str(p['chance']), '--key', key, '--batch', a.batch, '--detector', a.detector,
                        '--tells', p['why'], '--diagnosis', p['diagnosis'], '--decides', p['decides']]
                       + (['--panel', p['panel']] if p.get('panel') else []), check=True)
    (D / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (D / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
