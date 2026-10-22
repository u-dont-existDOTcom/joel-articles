"""Batch 469g's forecasts (batch/FORECAST.json, written before the recheck) scored against the recheck (2026-10-22).

Each forecast is one changed paragraph (or one edit's sentences) of 469g. Its text is found in the checked text of the
recheck's part A or part B (fix-20261020/substack41r/RESULT-41r3-a.json, RESULT-41r2-b.json) and given the reading of the
windows it overlaps: red (any AI-Generated window), light (Human, Medium or Low) or dark (Human, High). A "Human" call
is right when the reading is light or dark, an "AI" call when it is red.

  python3 articles/inner-signal/humanize/fix-20261021/b469/score_b469.py   (from the repo root) -> batch/SCORE.md
"""
import json, pathlib, re

B = pathlib.Path(__file__).resolve().parent
X = B.parents[1] / 'fix-20261020' / 'substack41r'
RESULTS = [('part A', X / 'RESULT-41r3-a.json'), ('part B', X / 'RESULT-41r2-b.json')]


def norm_map(t):
    tr = {'’': "'", '‘': "'", '“': '"', '”': '"', '—': '-', '–': '-', ' ': ' '}
    out, idx, sp = [], [], False
    for i, ch in enumerate(t):
        ch = tr.get(ch, ch)
        if ch.isspace():
            if sp:
                continue
            ch, sp = ' ', True
        else:
            sp = False
        out.append(ch)
        idx.append(i)
    return ''.join(out), idx


def plain(md):
    md = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md)
    md = re.sub(r'^\s*(?:[-*+]|\d+[.)])\s+', '', md, flags=re.M)
    return md.replace('**', '').replace('*', '').strip()


def reading(ws, a, b):
    hit = [w for w in ws if w['start_index'] < b and w['end_index'] > a]
    if any(w['label'] != 'Human' for w in hit):
        return 'red', hit
    return ('light' if any(w['confidence'] != 'High' for w in hit) else 'dark'), hit


def main():
    fc = json.loads((B / 'batch' / 'FORECAST.json').read_text(encoding='utf-8'))
    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    edits = {e['key']: e for e in meta['edits']}
    res = [(n, json.loads(p.read_text(encoding='utf-8'))) for n, p in RESULTS]
    rows, right = [], 0
    for key, f in fc.items():
        base = re.sub(r'-p\d+$', '', key)
        e = edits[base]
        if key != base:
            n = int(key.rsplit('-p', 1)[1])
            text = [p for p in e['new'].split('\n\n') if p.strip()][n - 1]
        else:
            text = e['new']
        probe = plain(text)
        found = None
        for name, r in res:
            nt, idx = norm_map(r['text'])
            q, _ = norm_map(probe)
            q = q[:160] if len(q) > 160 else q
            i = nt.find(q)
            if i >= 0:
                a = idx[i]
                tail, _ = norm_map(probe[-120:])
                j = nt.find(tail, i)
                b = idx[j + len(tail) - 1] + 1 if j >= 0 else a + len(probe)
                found = (name, r, a, b)
                break
        if not found:
            rows.append((key, f['call'], f['chance'], 'not found', '', 'unscored'))
            continue
        name, r, a, b = found
        shade, hit = reading(r['windows'], a, b)
        ok = (f['call'] == 'Human') == (shade != 'red')
        right += ok
        rows.append((key, f['call'], f['chance'], '%s, %s' % (name, shade),
                     '; '.join('%s %s' % (w['label'], w['confidence']) for w in hit), 'right' if ok else 'MISS'))
    lines = ['# Batch 469g: its forecasts against the recheck (2026-10-22)', '',
             'Written by `score_b469.py` from `batch/FORECAST.json` (written before the recheck) and the recheck\'s results: '
             '[part A](https://www.pangram.com/feed/c8001eb5-84a6-41dc-a2c0-0f4733dc3fc7), '
             '[part B](https://www.pangram.com/feed/558d14f6-625d-46aa-8495-adf9141cb3a4).', '',
             '**%d of %d right.**' % (right, sum(1 for r in rows if r[5] != 'unscored')), '',
             '| Paragraph | Call | Chance of Human | Reading | Windows | |', '|---|---|---|---|---|---|']
    for r in rows:
        lines.append('| %s | %s | %s | %s | %s | %s |' % r)
    (B / 'batch' / 'SCORE.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
