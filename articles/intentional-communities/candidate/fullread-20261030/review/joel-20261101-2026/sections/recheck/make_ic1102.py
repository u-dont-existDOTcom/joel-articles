"""Batch ic1102: the two sections of the community post that his answers of 2026-11-02 changed, each checked again by
itself, their second and last section check (lineages IC1101-01 and IC1101-02, gate E307), with predictions written
before the run.

Each section is cut at the same blocks as the first check (../SECTIONS.json), from master.md as promoted on 2 November
(../review/promote_20261102.py), which is his live post (../review/LIVE-CHECK-20261102.json). Every window that read AI
or Human (Low) in the first check (../RESULTS.md) was on his cards page, and his answers changed every one of them: the
Escuelita sentence and the refuge line (W-1, his W-2), the visitor's kid (W-3, W-4), and the anomie sentence (his W-5,
with W-6). The rest of each section read Human (High) or (Medium).

  python3 articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/sections/recheck/make_ic1102.py [--ledger]
Writes TEXTS.json (name -> text, for pangram_api.py), SECTIONS-IC1102.json and PREDICTIONS.md / .json; with --ledger,
adds each prediction to candidate/pangram-ledger.jsonl.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
S = HERE.parent
A = HERE.parents[5]
ROOT = A.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = A / 'candidate' / 'pangram-ledger.jsonl'
BATCH = 'ic1102'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
CHANCE = {
    'ic1101-01': (0.6, 'Mostly Human Written (0.04) on 1 November; its four windows that read AI or Human (Low) are now '
                       'his own versions or the cards he approved (W-1 to W-4), not checked in Pangram by him'),
    'ic1101-02': (0.65, 'Mostly Human Written (0.01); its one window that read Human (Low) is now his own version (W-5, '
                        'with W-6), not checked in Pangram by him'),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    args = ap.parse_args()
    md = (A / 'master.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    first = {s['key']: s for s in json.loads((S / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']}
    res = json.loads((S / 'RESULTS.json').read_text(encoding='utf-8'))
    texts, secs, rows = {}, [], []
    for k, (chance, why) in CHANCE.items():
        f = first[k]
        text = '\n\n'.join(bl[j]['text'] for j in f['blocks'])
        assert bl[f['blocks'][0]]['text'] == f['name'], (k, bl[f['blocks'][0]]['text'])
        key = '%s-%s' % (BATCH, k.split('-')[1])
        texts[key] = text
        secs.append({'key': key, 'first': k, 'name': f['name'], 'blocks': f['blocks'], 'words': len(text.split()),
                     'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'text': text})
        r1 = res[k]
        rows.append({'key': key, 'first': k, 'lineage': 'IC1101-%s' % k.split('-')[1], 'name': f['name'],
                     'words': len(text.split()), 'call': 'Human' if chance >= 0.5 else 'AI', 'chance': chance,
                     'why': why, 'first_result': '%s (%.3f), %s' % (r1['headline'], r1['likelihood'], r1['link'])})
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'SECTIONS-IC1102.json').write_text(json.dumps({'master_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
                                                           'sections': secs}, ensure_ascii=False, indent=1) + '\n',
                                               encoding='utf-8')
    out = ['# Batch ic1102: the two changed sections of the community post, each by itself, second and last check '
           '(predictions, before the run)', '', 'Chance = my chance of a 100% Human result. The Pangram column is filled '
           'after the run.', '', '| text | mine | chance | why | first check | Pangram |', '|---|---|---|---|---|---|']
    for r in rows:
        out.append('| %s: %s (%d words) | %s | %.2f | %s | %s | |' % (r['key'], r['name'], r['words'], r['call'],
                                                                     r['chance'], r['why'], r['first_result']))
    (HERE / 'PREDICTIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rows), 'sections:', [(r['key'], r['words'], r['chance']) for r in rows])
    if not args.ledger:
        return
    td = HERE / 'texts'
    td.mkdir(exist_ok=True)
    for s, r in zip(secs, rows):
        f = td / (s['key'] + '.txt')
        f.write_text(s['text'], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', 'section', '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', s['key'], '--batch', BATCH, '--detector', DETECTOR,
               '--tells', 'first check: ' + r['first_result'].split(',')[0],
               '--human-tells', 'his own words and the cards he approved',
               '--diagnosis', r['why'],
               '--decides', 'whether this section of the live post reads Human by itself after his answers of 2 November '
                            '(E307): try 2 of 2']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (s['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
