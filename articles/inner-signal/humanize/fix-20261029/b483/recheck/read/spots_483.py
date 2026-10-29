"""Batch 483's candidates (its own 11, and batch 482's 11 that read Human) read in place: for each, the windows of the candidate recheck (RESULT-A.json, RESULT-B.json)
that overlap its new words, its worst reading, and how the stretch read before (the recheck that sent it: batch 482's for batch 483's own, the 2026-10-29 18:18 check for batch 482's).

Batch 483 is the test of the writers fed with the shape rules from Emulate's fixes (E293). It also lists the windows that
turned red on words nobody changed in this batch, since those count against a rewrite too (E276: red moves).

  python3 articles/inner-signal/humanize/fix-20261029/b483/recheck/read/spots_483.py  -> SPOTS.json, SPOTS.md
"""
import json
import pathlib

R = pathlib.Path(__file__).resolve().parent
B = R.parents[1]
LAST = B.parent / 'b482' / 'recheck' / 'read'
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
        out.append({'id': s['id'], 'batch': s.get('batch'), 'where': s['where'], 'whose': s['whose'], 'part': p,
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
    own = [o for o in out if o.get('batch') == 483]
    lines = ['# Batch 483\'s candidates read in place', '',
             'Made by `spots_483.py`: each candidate\'s worst window in batch 483\'s recheck '
             '([part A](https://www.pangram.com/feed/d7900092-2691-46bd-b76a-d2043526509c), '
             '[part B](https://www.pangram.com/feed/845b60a9-9b58-4824-bc34-29cb1e395efa)). Batch 483\'s own: %d of %d read '
             'Human (%d at High); batch 482\'s that read Human last time: %d of %d still do.' % (
                 sum(1 for o in own if o.get('human')), len(own), sum(1 for o in own if o.get('high')),
                 sum(1 for o in out if o.get('batch') == 482 and o.get('human')), sum(1 for o in out if o.get('batch') == 482)), '',
             '| spot | batch | where | whose | before | now | windows |', '| --- | --- | --- | --- | --- | --- | --- |']
    for o in out:
        lines.append('| %s | %s | %s | %s | %s | **%s** | %s |' % (o['id'], o.get('batch'), o['where'], o.get('whose', ''),
                                                                  '; '.join(o.get('before', [])), o.get('now', o.get('reading')),
                                                                  '; '.join(o.get('windows', []))))
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
