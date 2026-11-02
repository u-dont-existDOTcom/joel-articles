"""The whole hypnosis guide, checked in two halves through the API with public links, after Joel's answers of
2026-11-02 18:16 UTC were in (gate E307: the whole-guide check comes last), with my predictions written before the run.

Each half is under the 99,999 characters a check of a Substack post reads, cut at the chapter heading nearest the middle
("The 15-minute daily practice"), so the halves compare with the parts A and B of earlier whole-guide checks. My chance
of a 100% Human result for each: every section read Human by itself in its last check except the ones listed in the
handoff (Human (Low) windows in his words and in Pattern 10, kept), and a whole half reads each section in the light of
the ones around it, which can go either way (E307, E319).

  python3 articles/inner-signal/humanize/fix-20261102/whole/make_whole.py [--ledger]
Writes TEXTS.json and PREDICTIONS.json here; with --ledger, adds the two predictions to the ledger.
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
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
CUT = 'The 15-minute daily practice'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    [k] = [b['i'] for b in bl if b['level'] == 1 and b['text'] == CUT]
    halves = {'w1102-A': [b['text'] for b in bl[:k]], 'w1102-B': [b['text'] for b in bl[k:]]}
    texts = {key: '\n\n'.join(v) for key, v in halves.items()}
    assert all(len(t) < 99999 for t in texts.values())
    rows = []
    for key, t in texts.items():
        rows.append({'key': key, 'lineage': 'HG1102-whole-' + key[-1], 'scope': 'stretch', 'chars': len(t),
                     'words': len(t.split()), 'call': 'Human', 'chance': 0.55,
                     'why': 'every section of this half read Human by itself in its last check, but for the Human (Low) '
                            'windows kept; a half reads them in context',
                     'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest(),
                     'guide_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest()})
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print([(r['key'], r['chars'], r['words']) for r in rows])
    if not a.ledger:
        return
    td = HERE / 'texts'
    td.mkdir(exist_ok=True)
    for r in rows:
        f = td / (r['key'] + '.txt')
        f.write_text(texts[r['key']], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', 'stretch', '--text', str(f), '--call', 'Human',
               '--chance', str(r['chance']), '--key', r['key'], '--batch', 'w1102', '--detector', DETECTOR,
               '--tells', 'the Human (Low) windows kept in sections 15, 27 and 69',
               '--human-tells', 'every section read Human by itself in its last check',
               '--diagnosis', r['why'],
               '--decides', 'whether the finished guide reads Human as a whole before it goes into his post (E307)']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (r['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
