"""Batch ic1101: each section of the community post that the 19 changes of 2026-11-01 touched, checked in Pangram by
itself (gates E306, E307), with predictions written before the run.

A section is the changed paragraph's heading and the paragraphs under it, to the next heading of any level; one under
MIN words takes in the next heading's paragraphs too. The text is what a reader sees (each block's plain text, one blank
line between blocks), from master.md, which is the live post (../LIVE-CHECK-20261101.json).

The evidence for each prediction is how its words read in the last whole-article check (2026-10-25 00:27 UTC,
https://www.pangram.com/feed/954042b6-e624-4c7f-87d7-db15c547d5c8; candidate/joel-20261025/recheck-r1/RESULT.json), the
version before question 66 and the 19 changes: every window with two runs of eight of its words still in the section,
and how much of the section those runs cover. My chance of a 100% Human result: every window Human (High) 0.8, any
Human (Medium) 0.65, any Human (Low) 0.45, any AI 0.3, less than half covered at most 0.55; less 0.05, since a section
alone loses the context around it (E307).

  python3 articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/sections/make_ic1101.py [--ledger]
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parents[4]
ROOT = A.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MASTER = A / 'master.md'
EDITS = HERE.parents[1] / 'SUBSTACK-EDITS.md'
RESULT = A / 'candidate' / 'joel-20261025' / 'recheck-r1' / 'RESULT.json'
LEDGER = A / 'candidate' / 'pangram-ledger.jsonl'
TEXTS = pathlib.Path('/tmp/claude-0/-home-claude/c925a45d-77a0-5b11-a8c3-3ce570004d0e/scratchpad/ic1101-texts')
BATCH = 'ic1101'
MIN = 120
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' ', '—': '-', '–': '-'})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(FLAT)).strip()


def words(bl, a, z):
    return sum(len(bl[j]['text'].split()) for j in range(a, z))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    args = ap.parse_args()
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    pairs = re.findall(r'\*\*Find:\*\*\n\n> (.*?)\n\n\*\*Replace with:\*\*\n\n> (.*?)\n', EDITS.read_text(encoding='utf-8'))
    spans = {}
    for k, (o, n) in enumerate(pairs, 1):
        hit = [b['i'] for b in bl if n in b['text']]
        assert len(hit) == 1, (k, len(hit))
        i = hit[0]
        a = i
        while a > 0 and not bl[a]['level']:
            a -= 1
        z = i + 1
        while z < len(bl) and not bl[z]['level']:
            z += 1
        while words(bl, a, z) < MIN and z < len(bl):
            z += 1
            while z < len(bl) and not bl[z]['level']:
                z += 1
        spans.setdefault((a, z), []).append(k)
    r = json.loads(RESULT.read_text(encoding='utf-8'))
    ws = [{'n': k, 'label': w['label'], 'conf': w['confidence'], 'words': w['word_count'],
           'text': norm(r['text'][w['start_index']:w['end_index']])} for k, w in enumerate(r['windows'], 1)]
    secs, rows = [], []
    for k, ((a, z), changes) in enumerate(sorted(spans.items()), 1):
        text = '\n\n'.join(bl[j]['text'] for j in range(a, z))
        key = '%s-%02d' % (BATCH, k)
        s = {'key': key, 'name': bl[a]['text'], 'blocks': list(range(a, z)), 'changes': ['C-%d' % c for c in changes],
             'words': len(text.split()), 'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'text': text}
        secs.append(s)
        st = norm(text)
        hit, covered = [], 0
        for w in ws:
            wd = w['text'].split()
            ps = [' '.join(wd[i:i + 8]) for i in range(0, max(1, len(wd) - 7), 8)]
            m = sum(1 for p in ps if p in st)
            if m >= 2 or (ps and m == len(ps)):
                hit.append(w)
                covered += m * 8
        cover = min(1.0, covered / max(1, s['words']))
        labels = [(w['label'], w['conf']) for w in hit]
        chance = (0.3 if any(l != 'Human' for l, c in labels) else 0.45 if ('Human', 'Low') in labels else
                  0.65 if ('Human', 'Medium') in labels else 0.8 if labels else 0.55)
        if cover < 0.5:
            chance = min(chance, 0.55)
        chance = round(chance - 0.05, 2)
        tells, human = [], []
        for l, c in sorted(set(labels)):
            n = labels.count((l, c))
            (human if l == 'Human' and c == 'High' else tells).append(
                '%d window%s %s (%s) on 25 October' % (n, '' if n == 1 else 's', 'AI' if l != 'Human' else 'Human', c))
        tells.append('changed on 1 November: %s' % ', '.join(s['changes']))
        if not human:
            human.append('his own words, read beside his published version (full read of 30 October)')
        rows.append({'key': key, 'lineage': 'IC1101-%02d' % k, 'name': s['name'], 'words': s['words'],
                     'call': 'Human' if chance >= 0.5 else 'AI', 'chance': chance, 'tells': tells, 'human_tells': human,
                     'cover': round(cover, 2)})
    (HERE / 'SECTIONS.json').write_text(json.dumps({'master_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
                                                    'sections': secs}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / ('%s-items.json' % BATCH)).write_text(json.dumps([[s['key'], s['text'], s['sha256']] for s in secs],
                                                            ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = ['# Batch ic1101: the community post\'s sections with the 19 changes, each by itself (predictions, written '
           'before the run)', '', 'Chance = my chance of a 100% Human result (make_ic1101.py says how it is set). The '
           'Pangram column is filled after the run.', '', '| text | mine | chance | why | Pangram |', '|---|---|---|---|---|']
    for x in rows:
        out.append('| %s: %s (%d words) | %s | %.2f | %s | |' % (x['key'], x['name'], x['words'], x['call'], x['chance'],
                                                              '; '.join(x['tells'] + x['human_tells'])))
    (HERE / 'PREDICTIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(secs), 'sections,', sum(s['words'] for s in secs), 'words')
    for x in rows:
        print(x['key'], x['words'], x['call'], x['chance'], x['cover'], x['name'][:60])
    if not args.ledger:
        return
    TEXTS.mkdir(parents=True, exist_ok=True)
    for s, x in zip(secs, rows):
        f = TEXTS / (s['key'] + '.txt')
        f.write_text(s['text'], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', x['lineage'], '--scope', 'section', '--text', str(f), '--call', x['call'],
               '--chance', str(x['chance']), '--key', s['key'], '--batch', BATCH,
               '--decides', 'whether this section of the live post reads Human by itself after the 19 changes (E307), and '
                            'which of its windows need a fix (E306)']
        for t in x['tells']:
            cmd += ['--tells', t]
        for t in x['human_tells']:
            cmd += ['--human-tells', t]
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (s['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
