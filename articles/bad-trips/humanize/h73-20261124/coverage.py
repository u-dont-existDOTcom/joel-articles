#!/usr/bin/env python3
"""coverage.py - which of the guide's blocks, as they stand now, have a Pangram check of their exact words, and what it
read (turn 65, 2026-11-24): a block counts as checked when its words (links, bold and spacing aside) sit inside a text
the ledger recorded a result for; the latest such result is the block's reading. Blocks with no check, or whose latest
check has a window below Human High, are the work left, worst first.

  python3 coverage.py [--md OUT.md]
"""
import argparse, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]


def norm(s):
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s or '')
    s = s.replace('**', '').replace('’', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'^\s*(?:\d+\.|[-*])\s+', '', s, flags=re.M)
    return re.sub(r'\s+', ' ', s).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md', default='')
    a = ap.parse_args()
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    recs = [json.loads(l) for l in (ART / 'humanize' / 'pangram-ledger.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
    preds = {r['id']: r for r in recs if r.get('type') == 'prediction'}
    voided = {r.get('prediction') for r in recs if r.get('type') == 'void'}
    checked = []   # (at, normalized text, result, prediction)
    for r in recs:
        if r.get('type') == 'result' and r.get('prediction') in preds and r.get('prediction') not in voided:
            p = preds[r['prediction']]
            if p.get('text'):
                # (turn 67) older results carry a time of day only ('21:07:12'), which sorted after every dated one, so a
                # section check of 2026-11-11 counted as later than a by-itself check of 2026-11-24 (lesson
                # bad-trips-2026-11-24y): a result's time counts only when it has its date, else the prediction's does
                at = r.get('at') or ''
                if not re.match(r'\d{4}-\d{2}-\d{2}', at):
                    at = p.get('at') or ''
                checked.append((at, norm(p['text']), r, p))
    checked.sort(key=lambda x: x[0])
    heading, rows = '', []
    for b in blocks:
        if b['kind'].startswith('h'):
            heading = norm(b['md']).lstrip('# ').strip()
            continue
        t = norm(b['md'])
        if len(t.split()) < 8:
            continue
        hit = None
        for at, ct, r, p in checked:
            if t in ct:
                hit = (at, ct, r, p)
        if not hit:
            rows.append((0, b['id'], heading, len(t.split()), 'never checked as it stands', '', ''))
            continue
        at, ct, r, p = hit
        ws = [w for w in (r.get('windows') or []) if isinstance(w, dict)]
        bad = [w for w in ws if not (str(w.get('label', '')).startswith('Human') and w.get('confidence') == 'High')]
        if ws and not bad:
            continue
        worst = 3 if any(str(w.get('label', '')).startswith('AI') for w in bad) else 2 if any(w.get('confidence') == 'Low' for w in bad) else 1
        shown = '; '.join('%s %s %s' % (w.get('label'), w.get('confidence'), w.get('words', '')) for w in ws) or r.get('verdict', '')
        rows.append((worst, b['id'], heading, len(t.split()), shown, p.get('lineage', ''), (r.get('link') or '')))
    rows.sort(key=lambda x: (-x[0], x[1]))
    kinds = {3: 'AI window', 2: 'Low window', 1: 'Medium window', 0: 'no check of these words'}
    out = ['# What is left (as of the ledger\'s last result): the guide\'s blocks below Human High or with no check of their words', '',
           '%d blocks of 8 words or more; %d left.' % (sum(1 for b in blocks if not b['kind'].startswith('h') and len(norm(b['md']).split()) >= 8), len(rows)), '',
           '| Block | Section | Words | Why | Latest reading | Lineage |', '|---|---|---|---|---|---|']
    for w, bid, h, n, shown, lin, link in rows:
        out.append('| %s | %s | %d | %s | %s | %s |' % (bid, h[:40], n, kinds[w], shown[:80], lin[:60]))
    text = '\n'.join(out) + '\n'
    if a.md:
        pathlib.Path(a.md).write_text(text, encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main()
