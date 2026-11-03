"""The predictions for round 1's checks, written into the lane's ledger before the texts go to Pangram (gate E307).

PREDICTIONS.json here: {key: {"chance": my chance of a 100% Human result, "why": the tells I still see or the reason,
"decides": what the result decides}}. Each key is a stretch in TEXTS.json (assemble_r1.py), and its lineage is
ND1103-<key without "r1-">, so a later try of the same stretch continues it.

  python3 articles/neuro-de-armoring/humanize/fix-20261103/r1/predict_r1.py --batch r1103b --dir b
Copies TEXTS.json into the batch folder (--dir, under this one) and writes there the PREDICTIONS.json list that
record_r1102.py reads; a key the ledger already has an open prediction for in this batch is not predicted again.
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
    D.mkdir(exist_ok=True)
    texts = json.loads((HERE / 'TEXTS.json').read_text(encoding='utf-8'))
    preds = json.loads((HERE / 'PREDICTIONS.json').read_text(encoding='utf-8'))
    (D / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    done = set()
    for line in LEDGER.read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        if r.get('batch') == a.batch and r.get('type', 'prediction') != 'result' and r.get('key'):
            done.add((r['key'], r.get('sha256')))
    rows = []
    td = D / 'texts'
    td.mkdir(exist_ok=True)
    n = 0
    for key, t in texts.items():
        p = preds[key]
        f = td / (key + '.txt')
        f.write_text(t, encoding='utf-8')
        call = 'Human' if p['chance'] >= 0.5 else 'AI'
        sha = hashlib.sha256(t.encode('utf-8')).hexdigest()
        rows.append({'key': key, 'name': p['why'], 'lineage': 'ND1103-' + key.split('-', 1)[1], 'scope': 'stretch',
                     'words': len(t.split()), 'call': call, 'chance': p['chance'], 'why': p['why'], 'sha256': sha})
        if (key, sha) in done:
            print(key, 'already predicted in', a.batch)
            continue
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', 'ND1103-' + key.split('-', 1)[1], '--scope', 'stretch', '--text', str(f), '--call', call,
               '--chance', str(p['chance']), '--key', key, '--batch', a.batch, '--detector', DETECTOR,
               '--tells', p['why'], '--diagnosis', p.get('diagnosis', 'round 1: the section rewritten freely in his voice '
                                                     '(his answer to question 1), every claim and number kept'),
               '--decides', p.get('decides', 'whether the free rewrite reads Human, or what still reads AI')]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            sys.exit('%s: %s%s' % (key, r.stdout, r.stderr))
        n += 1
        print(key, call, p['chance'], len(t.split()), 'words')
    (D / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('ledger: %d predictions added' % n)


if __name__ == '__main__':
    main()
