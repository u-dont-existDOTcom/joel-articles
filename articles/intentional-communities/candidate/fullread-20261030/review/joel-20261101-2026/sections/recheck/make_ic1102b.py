"""Batch ic1102b: a tested suggestion for the one window batch ic1102 found (gate E306), with its prediction written
before the run.

Communes Are Hot Again read Human Written by itself on 2 November (RESULTS.md here), with one window Human (Low): his
new sentence of W-5, "In a large society, the shared norms and close ties that held those groups together fall apart,
and nobody knows anybody well enough or for long enough to tell who can be trusted—even your next-door neighbor is often
a total stranger." The section has used its two checks (IC1101-02), so the suggestion is checked as its paragraph, in a
lineage of its own: his words, the one long sentence said as three (two full stops and two commas, nothing else).

  python3 articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/sections/recheck/make_ic1102b.py [--ledger]
Writes p3/TEXTS.json and p3/PREDICTIONS.json; with --ledger, adds the prediction to candidate/pangram-ledger.jsonl.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parents[5]
ROOT = A.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = A / 'candidate' / 'pangram-ledger.jsonl'
OUT = HERE / 'p3'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
OLD = ('In a large society, the shared norms and close ties that held those groups together fall apart, and nobody knows '
       'anybody well enough or for long enough to tell who can be trusted—even your next-door neighbor is often a total '
       'stranger.')
NEW = ('In a large society, the shared norms and close ties that held those groups together fall apart. Nobody knows '
       'anybody well enough, or for long enough, to tell who can be trusted. Even your next-door neighbor is often a total '
       'stranger.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    bl = sr.blocks((A / 'master.md').read_text(encoding='utf-8'))
    [p] = [b['text'] for b in bl if OLD in b['text']]
    assert p.startswith('What’s starving them is anomie.')
    text = p.replace(OLD, NEW)
    key = 'ic1102b-W5'
    OUT.mkdir(exist_ok=True)
    (OUT / 'TEXTS.json').write_text(json.dumps({key: text}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    row = {'key': key, 'lineage': 'IC1102-02-P3', 'scope': 'paragraph', 'name': 'Communes Are Hot Again, P3 (W-5 split)',
           'words': len(text.split()), 'call': 'Human', 'chance': 0.75, 'card': 'W-5', 'old': OLD, 'new': NEW,
           'why': 'his words, the long sentence that read Human (Low) said as three; the rest of the paragraph read Human',
           'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()}
    (OUT / 'PREDICTIONS.json').write_text(json.dumps([row], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(key, row['words'], 'words')
    if a.ledger:
        f = OUT / (key + '.txt')
        f.write_text(text, encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', row['lineage'], '--scope', 'paragraph', '--text', str(f), '--call', 'Human',
               '--chance', str(row['chance']), '--key', key, '--batch', 'ic1102b', '--detector', DETECTOR,
               '--tells', 'batch ic1102: the sentence read Human (Low) in its section',
               '--human-tells', 'his own words; only the punctuation changes', '--diagnosis', row['why'],
               '--decides', 'whether the suggestion reads Human before it goes on his cards page (E306, E315)']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit(p.stdout + p.stderr)
        print('ledger: prediction added')


if __name__ == '__main__':
    main()
