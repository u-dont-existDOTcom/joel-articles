"""Batch 482's 21 candidates read in place: for each, the windows of the candidate recheck (RESULT-A.json, RESULT-B.json)
that overlap its new words, its worst reading, and how the stretch read before (the recheck of 2026-10-29 that sent it).

This is the test of the fresh writers without Emulate (Joel's question 26 of 2026-10-29). It also lists the windows that
turned red on words nobody changed in this batch, since those count against a rewrite too (E276: red moves).

  python3 articles/inner-signal/humanize/fix-20261029/b482/recheck/read/spots_482.py  -> SPOTS.json, SPOTS.md
"""
import json
import pathlib

R = pathlib.Path(__file__).resolve().parent
B = R.parents[1]
LAST = B.parent / 'recheck' / 'read'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
ORDER = [('Human', 'High'), ('Human', 'Medium'), ('Human', 'Low'), ('AI', 'Low'), ('AI', 'Medium'), ('AI', 'High')]


def lab(w):
    return ('AI' if w['label'].startswith('AI') else 'Human', w['confidence'])


def over(res, a, b):
    return [w for w in res['windows'] if w['start_index'] < b and w['end_index'] > a]


def main():
    spots = [s for s in json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots'] if s['pick'] != 'none']
    res = {p: json.loads((R / ('RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
    last = {p: json.loads((LAST / ('RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
    out, taken = [], {'A': [], 'B': []}
    for s in spots:
        got = None
        for p in 'AB':
            t = res[p]['text'].translate(FLAT)
            k = t.find(s['new'].translate(FLAT))
            if k >= 0:
                got = (p, k, k + len(s['new']))
                break
        if not got:
            out.append({'id': s['id'], 'where': s['where'], 'reading': 'not found'})
            continue
        p, a, b = got
        taken[p].append((a, b))
        ws = over(res[p], a, b)
        worst = max((lab(w) for w in ws), key=ORDER.index)
        out.append({'id': s['id'], 'where': s['where'], 'whose': s['whose'], 'part': p,
                    'before': s['readings'], 'now': '%s (%s)' % worst,
                    'windows': ['%s %s %d words' % (lab(w) + (w['word_count'],)) for w in ws],
                    'human': worst[0] == 'Human', 'high': worst == ('Human', 'High'), 'new': s['new']})
    # red on words this batch didn't change, and whether it was red last time
    newred = []
    for p in 'AB':
        t = res[p]['text']
        lt = last[p]['text']
        old_red = [lt[w['start_index']:w['end_index']].strip() for w in last[p]['windows'] if w['label'].startswith('AI')]
        for w in res[p]['windows']:
            if not w['label'].startswith('AI'):
                continue
            a, b = w['start_index'], w['end_index']
            if any(x < b and y > a for x, y in taken[p]):
                continue
            seg = t[a:b].strip()
            newred.append({'part': p, 'reading': '%s (%s)' % lab(w), 'words': w['word_count'], 'text': seg,
                           'red_last_time': any(seg in o or o in seg for o in old_red if o)})
    (R / 'SPOTS.json').write_text(json.dumps({'spots': out, 'red_elsewhere': newred}, ensure_ascii=False, indent=1) + '\n',
                                  encoding='utf-8')
    hum = sum(1 for o in out if o.get('human'))
    lines = ['# Batch 482\'s candidates read in place', '',
             'Made by `spots_482.py`: each candidate\'s worst window in the candidate recheck '
             '([part A](https://www.pangram.com/feed/19fba559-fe64-46a3-92a1-ab87f728b4ba), '
             '[part B](https://www.pangram.com/feed/82470746-1d28-4ddc-ac19-276ca31c19f2)), beside how its stretch read in '
             'the recheck that sent it ([part A](https://www.pangram.com/feed/d1e283a5-efcf-4fc4-ad6f-d535e12951b2), '
             '[part B](https://www.pangram.com/feed/f9b45a7b-402c-412c-af68-a5f9ca44f6e6)). %d of %d read Human '
             '(%d at High).' % (hum, len(out), sum(1 for o in out if o.get('high'))), '',
             '| spot | where | whose | before | now | windows |', '| --- | --- | --- | --- | --- | --- |']
    for o in out:
        lines.append('| %s | %s | %s | %s | **%s** | %s |' % (o['id'], o['where'], o.get('whose', ''), '; '.join(o.get('before', [])),
                                                             o.get('now', o.get('reading')), '; '.join(o.get('windows', []))))
    lines += ['', '## Red on words this batch didn\'t change', '', '| part | reading | words | red last time | text |',
              '| --- | --- | --- | --- | --- |']
    for r in newred:
        lines.append('| %s | %s | %d | %s | %s |' % (r['part'], r['reading'], r['words'], 'yes' if r['red_last_time'] else 'no',
                                                      r['text'].replace('\n', ' / ')[:160]))
    (R / 'SPOTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('%d of %d Human (%d High); red elsewhere: %d windows (%d new)' % (
        hum, len(out), sum(1 for o in out if o.get('high')), len(newred), sum(1 for r in newred if not r['red_last_time'])))


if __name__ == '__main__':
    main()
