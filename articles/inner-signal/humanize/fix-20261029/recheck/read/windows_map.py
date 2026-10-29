"""Where the recheck of 2026-10-29 read below High, and how each change of 28 and 29 October read in place.

  python3 articles/inner-signal/humanize/fix-20261029/recheck/read/windows_map.py   -> WINDOWS-MAP.md, SPOTS.json, SPOTS.md

WINDOWS-MAP.md: every window that isn't High-confidence Human (CONFIDENCE.json, window_confidence.py), each line of the
checked text it touches, and what that line is: changed since the last check (a fix he approved on 29 October, my advised
wording on a card in his own words, his own version of 28 October, or a batch 481 spot back to batch 480's words), or
unchanged, with how the last check (batch 481's recheck) read it.

SPOTS: every fix of 28 October (fix-20261028/comprehension/fix/KEPT.json) and the four advised wordings, with the reading of
the windows its new words sit in (the worst one: AI before Human, Low before High), so the next tries go where a change
of ours reads AI or below High, and Joel's rule for 25 holds: the clear version stays, and a try has to be both (E291).
"""
import json
import pathlib
import re

X = pathlib.Path(__file__).resolve().parent
R = X.parent
H = R.parents[1]
LAST = H / 'fix-20261026' / 'b481' / 'recheck' / 'read'
C28 = H / 'fix-20261028' / 'comprehension'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '–': '-', '—': '-', ' ': ' '})
RANK = {('AI', 'High'): 0, ('AI', 'Medium'): 1, ('AI', 'Low'): 2, ('Human', 'Low'): 3, ('Human', 'Medium'): 4,
        ('Human', 'High'): 5}


def flat(s):
    return re.sub(r'\s+', ' ', s.translate(FLAT)).strip()


def label(w):
    return ('AI' if str(w.get('label', '')).startswith('AI') else 'Human', w['confidence'])


def lines_of(text):
    out, i = [], 0
    for ln in text.split('\n'):
        out.append((i, i + len(ln), ln))
        i += len(ln) + 1
    return out


def windows_over(res, a, b):
    return [w for w in res['windows'] if w['start_index'] < b and w['end_index'] > a]


def worst(ws):
    return min((label(w) for w in ws), key=lambda x: RANK[x]) if ws else None


def main():
    kept = json.loads((C28 / 'fix' / 'KEPT.json').read_text(encoding='utf-8'))['fixes']
    review = json.loads((C28 / 'REVIEW-28.json').read_text(encoding='utf-8'))
    card_of = {}
    for s in review['suggestions']:
        for f in s.get('findings', []):
            card_of[f] = s['id']
    dec = json.loads((H / 'fix-20261029' / 'DECISIONS-20261029.json').read_text(encoding='utf-8'))
    advised = []
    for x in dec['items']:
        if x['status'] == 'revise':
            advised.append(x)
    his28 = [x['your_version'] for x in json.loads((H / 'fix-20261028' / 'ANSWERS-20261028-1519.json')
                                                   .read_text(encoding='utf-8'))['items'] if x.get('your_version', '').strip()]
    conf = json.loads((X / 'CONFIDENCE.json').read_text(encoding='utf-8'))
    out = ['# Where the recheck of 2026-10-29 read below High', '',
           'Made by `windows_map.py`. Each window that isn\'t High-confidence Human, and each line of the checked text it '
           'touches: what the line is, and how the last check (batch 481\'s recheck) read it if it is unchanged.', '']
    spots = []
    for part in ('A', 'B'):
        res = json.loads((X / ('RESULT-%s.json' % part)).read_text(encoding='utf-8'))
        last = json.loads((LAST / ('RESULT-%s.json' % part)).read_text(encoding='utf-8'))
        last_other = json.loads((LAST / ('RESULT-%s.json' % ('B' if part == 'A' else 'A'))).read_text(encoding='utf-8'))
        changed = {flat(c['text']): c for c in json.loads((R / ('CHANGED-%s.json' % part)).read_text(encoding='utf-8'))}
        text = res['text']
        rows = conf['RESULT-%s.json' % part]['rows']
        out += ['## Part %s (%s, %s)' % (part, res.get('headline'), res.get('link')), '']

        def what(ln):
            f = flat(ln)
            tags = []
            for fx in kept:
                if flat(fx['with']) and flat(fx['with']) in f:
                    tags.append('fix %s (card %s)' % (fx['id'], ', '.join(sorted({card_of.get(g, '?') for g in fx['findings']}))))
            for x in advised:
                if flat(x['your_version'])[:60] in f or f[:60] in flat(x['your_version']):
                    tags.append('my advised wording (card %s)' % x['id'])
            if any(f[:60] in flat(h) for h in his28) and f:
                tags.append('his own version of 28 October')
            c = changed.get(f)
            if c and not tags:
                tags.append(c['why'])
            if not c and not tags:
                for src, nm in ((last, 'last check'), (last_other, 'last check, other part')):
                    k = src['text'].translate(FLAT).find(ln.translate(FLAT)) if len(ln) > 12 else -1
                    if k >= 0:
                        lw = worst(windows_over(src, k, k + len(ln)))
                        tags.append('unchanged; %s read it %s' % (nm, '%s (%s)' % lw if lw else '?'))
                        break
                else:
                    tags.append('unchanged')
            return '; '.join(tags)

        for w in rows:
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            ws = [x for x in res['windows'] if x['start_index'] <= text.find(w['text'][:40]) < x['end_index']]
            a = text.find(w['text'][:40])
            b = a + len(w['text'])
            touched = [(s, e, ln) for s, e, ln in lines_of(text) if s < b and e > a and ln.strip()]
            out.append('- **#%d %s (%s)**, %d words, %s: "%s"' % (w['window'], w['label'], w['confidence'], w['words'],
                                                                 w['where'], w['text'][:160].replace('\n', ' / ')))
            for s, e, ln in touched:
                out.append('  - "%s": %s' % (ln[:90], what(ln)))
        out.append('')
        # each of our changes in place
        flat_text = text.translate(FLAT)
        for fx in kept:
            w_ = fx['with'].translate(FLAT)
            k = flat_text.find(w_) if len(w_) >= 8 else -1
            if k < 0:
                continue
            lw = worst(windows_over(res, k, k + len(w_)))
            spots.append({'part': part, 'id': fx['id'], 'card': ', '.join(sorted({card_of.get(g, '?') for g in fx['findings']})),
                          'where': fx['where'], 'with': fx['with'], 'reading': '%s (%s)' % lw if lw else None})
        for x in advised:
            for old, new in [(None, None)]:
                pass
            seg = None
            for frag in re.split(r'(?<=[.!?])\s+', x['your_version']):
                if any(t in frag for t in ('become more your own person', 'push past that no', 'your inner child',
                                           'inner adult’s Protector')):
                    seg = frag
            if seg:
                k = flat_text.find(seg.translate(FLAT))
                if k >= 0:
                    lw = worst(windows_over(res, k, k + len(seg)))
                    spots.append({'part': part, 'id': 'advice ' + x['id'], 'card': x['id'], 'where': '', 'with': seg,
                                  'reading': '%s (%s)' % lw if lw else None})
    (X / 'WINDOWS-MAP.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (X / 'SPOTS.json').write_text(json.dumps(spots, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    from collections import Counter
    n = Counter(s['reading'] for s in spots)
    md = ['# Our changes of 28 and 29 October, read in place', '',
          'Made by `windows_map.py`: each fix he approved on 29 October (fix-20261028/comprehension/fix/KEPT.json) and each '
          'advised wording, with the worst reading of the windows its new words sit in. %d found in the checked text: %s.'
          % (len(spots), ', '.join('%s %d' % (k, v) for k, v in sorted(n.items(), key=lambda kv: RANK.get(tuple(
              kv[0].replace(')', '').split(' (')), 9) if kv[0] else 9))), '',
          '| fix | card | reading | where | new words |', '|---|---|---|---|---|']
    for s in sorted(spots, key=lambda s: RANK.get(tuple(s['reading'].replace(')', '').split(' (')), 9) if s['reading'] else 9):
        md.append('| %s | %s | %s | %s | %s |' % (s['id'], s['card'], s['reading'], s['where'], s['with'][:110].replace('|', '/')))
    (X / 'SPOTS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(len(spots), 'changes found in place:', dict(n))


if __name__ == '__main__':
    main()
