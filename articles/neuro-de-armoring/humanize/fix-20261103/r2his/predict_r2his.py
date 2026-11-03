"""The predictions for round 2's checks (his way, E335), written into the lane's ledger before the texts go to Pangram
(gate E307). PREDICTIONS-IN.json here: {key: {"chance": my chance of a 100% Human result, "why": the tells I still see,
"diagnosis": what the round changed, "decides": what the result decides}}. Each key is a stretch in TEXTS.json
(assemble_r2his.py), its lineage ND1103-<key without "r2-"> with "R2" in front, so a later try continues it.

  python3 articles/neuro-de-armoring/humanize/fix-20261103/r2his/predict_r2his.py --batch r1103c --dir c
Copies TEXTS.json into the batch folder (--dir, under this one) and writes there the PREDICTIONS.json list that
record_r1102.py reads; a key the ledger already has a prediction for in this batch, at the same text, is not predicted again.
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
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218, E325: at most six paragraphs and 1,200 words)'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch', required=True)
    ap.add_argument('--dir', required=True)
    a = ap.parse_args()
    D = HERE / a.dir
    (D / 'texts').mkdir(parents=True, exist_ok=True)
    texts = json.loads((HERE / 'TEXTS.json').read_text(encoding='utf-8'))
    preds = json.loads((HERE / 'PREDICTIONS-IN.json').read_text(encoding='utf-8'))
    (D / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    done = set()
    for line in LEDGER.read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        if r.get('batch') == a.batch and r.get('type', 'prediction') != 'result' and r.get('key'):
            done.add((r['key'], r.get('sha256')))
    rows = []
    for key, t in texts.items():
        p = preds[key]
        f = D / 'texts' / (key + '.txt')
        f.write_text(t, encoding='utf-8')
        call = 'Human' if p['chance'] >= 0.5 else 'AI'
        sha = hashlib.sha256(t.encode('utf-8')).hexdigest()
        lineage = 'ND1103-R2' + key.split('-', 1)[1]
        rows.append({'key': key, 'name': p['name'], 'lineage': lineage, 'scope': 'stretch', 'words': len(t.split()),
                     'call': call, 'chance': p['chance'], 'why': p['why'], 'sha256': sha})
        if (key, sha) in done:
            print(key, 'already predicted in', a.batch)
            continue
        subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                        '--lineage', lineage, '--scope', 'stretch', '--text', str(f), '--call', call,
                        '--chance', str(p['chance']), '--key', key, '--batch', a.batch, '--detector', DETECTOR,
                        '--tells', p['why'], '--diagnosis', p['diagnosis'], '--decides', p['decides']], check=True)
    (D / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
