"""CHANGED-A.json and CHANGED-B.json for batch 483's recheck (part_forecast.py make), written before the paste.

The last check is batch 482's recheck (../../b482/recheck/read/RESULT-A.json and RESULT-B.json). Since then only batch
483's candidates changed: new versions of the 10 stretches whose batch 482 version still read AI, and a suggestion for
his HG-S15 sentence (J5); batch 482's 11 versions that read Human stay word for word. My chances, from one stated rule
measured on batch 482 (its writers' versions read AI in 5 of 12 stretches that had read AI Low only, and in 5 of 9 that
had read AI Medium or High, against my 0.2 and 0.35): a stretch whose last try read AI High, red 0.5; any other, red 0.4;
High 0.2 for each. What read AI last time and is unchanged now: the audit, red 0.95; a window that turned red last time
next to a rewrite that changes again, red 0.4 (the red came with the rewrite); one that turned red with nothing changing
near it, red 0.55 (the window moved, and nothing has changed there since); one red in both of the last two checks, red
0.6. part_forecast.py adds the neighbours and the windows that read Human at Low or Medium last time.

  python3 articles/inner-signal/humanize/fix-20261029/b483/recheck/make_changed.py
"""
import json
import pathlib
import re

X = pathlib.Path(__file__).resolve().parent
B = X.parent
LAST = B.parent / 'b482' / 'recheck' / 'read'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
AUDIT_FIRST, AUDIT_LAST = 'Before accepting a recording or live suggestion, ask:', 'change the method, or leave.'


def locate(text, s):
    ft, fs = text.translate(FLAT), s.translate(FLAT)
    k = ft.find(fs)
    return text[k:k + len(s)] if k >= 0 and ft.count(fs) == 1 else None


def main():
    spots = [s for s in json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']
             if s.get('pick') != 'none' and s.get('batch') == 483]
    targets = {t['id']: t for t in json.loads((B / 'TARGETS.json').read_text(encoding='utf-8'))['items']}
    lastspots = json.loads((LAST / 'SPOTS.json').read_text(encoding='utf-8'))
    for part in ('A', 'B'):
        text = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        out = []
        for s in spots:
            got = locate(text, s['new'])
            if got is None:
                continue
            lt = targets[s['id']]['last_try']
            high_last = bool(lt) and lt['read_in_place'] == 'AI (High)'
            red = 0.5 if high_last else 0.4
            out.append({'name': '%s (%s)' % (s['id'], s['where']), 'text': got, 'chance_red': red, 'chance_high': 0.2,
                        'why': ('a suggestion for his own words' if s['id'].startswith('J') else 'a writer\'s version') +
                               '; last try %s' % (lt['read_in_place'] if lt else 'none (his sentence read AI Low twice)'),
                        'kind': 'changed'})
        taken = [(text.find(c['text']), text.find(c['text']) + len(c['text'])) for c in out]
        spots_here = list(out)
        for r in lastspots['red_elsewhere']:
            if r['part'] != part or AUDIT_FIRST in r['text']:
                continue
            seg = r['text'].strip()
            if text.count(seg) != 1:
                continue
            i = text.find(seg)
            if any(a < i + len(seg) and b > i for a, b in taken):
                continue
            # near a rewrite: within two lines (paragraphs) of the checked text of a changed candidate
            line = text.count('\n', 0, i)
            near = any(abs(text.count('\n', 0, a) - line) <= 2 for a, _b in taken[:len(spots_here)])
            taken.append((i, i + len(seg)))
            if r['red_last_time']:
                red, why = 0.6, 'and the check before'
            elif near:
                red, why = 0.4, 'next to a rewrite that changes again (the red came with the rewrite)'
            else:
                red, why = 0.55, 'with nothing near it changing (a window that moved)'
            out.append({'name': 'kept: ' + seg[:48].rstrip() + '...', 'text': seg, 'chance_red': red, 'chance_high': 0.1,
                        'why': 'unchanged; read %s last time, %s' % (r['reading'], why), 'kind': 'changed'})
        if part == 'B':
            a = text.find(AUDIT_FIRST)
            b = text.find(AUDIT_LAST, a) + len(AUDIT_LAST)
            out.append({'name': 'the hypnosis audit (kept, 2c)', 'text': text[a:b], 'chance_red': 0.95, 'chance_high': 0.0,
                        'why': 'his list, kept by his answer 2c, unchanged: read AI (High) in every check since recheck B2',
                        'kind': 'changed'})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(part, len(out), 'parts')


if __name__ == '__main__':
    main()
