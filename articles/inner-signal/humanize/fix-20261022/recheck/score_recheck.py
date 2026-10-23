"""Batches 470g's and 471g's forecasts (batch/FORECAST.json, written before the recheck) scored against the recheck of
2026-10-22 (part A; part B when its result is in).

Each forecast is one changed paragraph, its text the batch's drafts.json (the version installed, which this checks in
HUMANIZED-SO-FAR.md first). Its text is found in the checked text of the recheck's part A or part B (RESULT-A.json,
RESULT-B.json) and given the reading of the windows it overlaps: red (any AI-Generated window), light (Human, Medium or
Low) or dark (Human, High). A "Human" call is right when the reading is light or dark, an "AI" call when it is red.
As fix-20261021/b469/score_b469.py did 469g's.

  python3 articles/inner-signal/humanize/fix-20261022/recheck/score_recheck.py   (from the repo root)
      -> b470/batch/SCORE.md, b471/batch/SCORE.md
"""
import json, pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent
F = R.parent
H = F.parents[0]
sys.path.insert(0, str(H / 'fix-20261021' / 'b469'))
from score_b469 import norm_map, plain, reading  # noqa: E402

LINKS = {'part A': 'https://www.pangram.com/feed/47610d4b-fb69-4966-896f-317b029fc1af'}   # part B: its result's own link


def locate(probe, res):
    q, _ = norm_map(probe)
    q = q[:160]
    for name, r in res:
        nt, idx = norm_map(r['text'])
        i = nt.find(q)
        if i >= 0:
            a = idx[i]
            tail, _ = norm_map(probe[-120:])
            j = nt.find(tail, i)
            b = idx[j + len(tail) - 1] + 1 if j >= 0 else a + len(probe)
            return name, r, a, b
    return None


def main():
    # part A of this round was checked here (Joel's result of 2026-10-23 01:10 UTC); part B is pasted from the next
    # round's folder (fix-20261023/recheck/, with Joel's Appendix C), so its result is read from there
    where = {'part A': [R / 'RESULT-A.json'], 'part B': [R / 'RESULT-B.json', H / 'fix-20261023' / 'recheck' / 'RESULT-B.json']}
    res = [(n, json.loads(next(f for f in fs if f.exists()).read_text(encoding='utf-8'))) for n, fs in where.items()
           if any(f.exists() for f in fs)]
    hsf, _ = norm_map(plain((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')))
    out, fcs = [], {b: json.loads((F / b / 'batch' / 'FORECAST.json').read_text(encoding='utf-8')) for b in ('b470', 'b471')}
    for batch in ('b470', 'b471'):
        B = F / batch
        fc = json.loads((B / 'batch' / 'FORECAST.json').read_text(encoding='utf-8'))
        drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
        rows, right = [], 0
        for key, f in fc.items():
            text = plain(drafts[key])
            if norm_map(text)[0][:160] not in hsf:
                later = [k for b, fc2 in fcs.items() if b > batch for k, g in fc2.items() if g['lineage'] == f['lineage']]
                rows.append((key, f['call'], f['chance'], 'replaced since by %s' % ', '.join(later) if later else
                             'not in the working copy as drafted', '', 'unscored'))
                continue
            found = locate(text, res)
            if not found:
                rows.append((key, f['call'], f['chance'], 'not in part A (part B is still to check)', '', 'pending'))
                continue
            name, r, a, b = found
            shade, hit = reading(r['windows'], a, b)
            ok = (f['call'] == 'Human') == (shade != 'red')
            right += ok
            rows.append((key, f['call'], f['chance'], '%s, %s' % (name, shade),
                         '; '.join('%s %s' % (w['label'], w['confidence']) for w in hit), 'right' if ok else 'MISS'))
        scored = sum(1 for r in rows if r[5] in ('right', 'MISS'))
        lines = ['# Batch %sg: its forecasts against the recheck of 2026-10-22' % batch[1:], '',
                 'Written by `fix-20261022/recheck/score_recheck.py` from `batch/FORECAST.json` (written before the '
                 'recheck) and the recheck\'s results: ' + ', '.join('[%s](%s)' % (n, LINKS.get(n, r.get('link')))
                                                                      for n, r in res) + '.', '',
                 '**%d of %d right**%s.' % (right, scored, '' if scored == len(rows) else
                                             ' (%d still to score)' % (len(rows) - scored)), '',
                 '| Paragraph | Call | Chance | Reading | Windows | |', '|---|---|---|---|---|---|']
        lines += ['| %s | %s | %s | %s | %s | %s |' % r for r in rows]
        (B / 'batch' / 'SCORE.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
        out.append('%s: %d of %d right, %d pending' % (batch, right, scored, len(rows) - scored))
        print('\n'.join(lines))
    print('\n'.join(out))


if __name__ == '__main__':
    main()
