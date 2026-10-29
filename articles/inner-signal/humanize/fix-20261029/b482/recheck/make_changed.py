"""CHANGED-A.json and CHANGED-B.json for the recheck with batch 482's candidates in (part_forecast.py make), written before
the paste.

The last check is the recheck of 2026-10-29 (../../recheck/read/RESULT-A.json and RESULT-B.json). Since then only batch
482's candidates changed: each picked version of a stretch that read AI there (T items, ours) and each suggestion for his
own words that read AI (J items). Each candidate is one part, its new words as the check will read them, with my chances
from one stated rule, by how the stretch read last time: where every window over it was AI at Low confidence, red 0.2 and
High 0.35 (a Low window is close to the line, and in the last recheck 129 of our 140 changes in place read Human); where
any was AI at Medium or High, red 0.35 and High 0.25 (the new words still sit among the same neighbours, and the
writers' versions are new words, not Emulate's). The audit, unchanged and kept (2c), red 0.95. And what read AI last time
and is still there word for word: a whole window unchanged (his HG-S15 list, the three-jobs line), red 0.55 at Low and
0.65 at Medium (a window can move when the text before it changes length, but the words that read AI are the same); a
sentence left unchanged in a window whose other words changed (his Quick start line beside T1, the Nimja link line
beside T7), red 0.3. part_forecast.py adds the neighbours and the windows that read Human at Low or Medium last time.

  python3 articles/inner-signal/humanize/fix-20261029/b482/recheck/make_changed.py
"""
import json
import pathlib

import re

X = pathlib.Path(__file__).resolve().parent
B = X.parent
LAST = B.parent / 'recheck' / 'read'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
AUDIT_FIRST, AUDIT_LAST = 'Before accepting a recording or live suggestion, ask:', 'change the method, or leave.'


def locate(text, s):
    ft, fs = text.translate(FLAT), s.translate(FLAT)
    k = ft.find(fs)
    return text[k:k + len(s)] if k >= 0 and ft.count(fs) == 1 else None


def main():
    spots = [s for s in json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots'] if s['pick'] != 'none']
    for part in ('A', 'B'):
        text = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        out = []
        for s in spots:
            # the new words, as one line of the checked text holds them (a version can be several sentences)
            got = locate(text, s['new'])
            if got is None:
                continue
            low_only = all(r.startswith('AI (Low)') for r in s['readings'])
            red, high = (0.2, 0.35) if low_only else (0.35, 0.25)
            out.append({'name': '%s (%s)' % (s['id'], s['where']), 'text': got, 'chance_red': red, 'chance_high': high,
                        'why': ('a suggestion for his own words' if s['id'].startswith('J') else 'a writer\'s version') +
                               ' of a stretch that read AI on 2026-10-29 (%s)' % '; '.join(s['readings']) +
                               ('' if low_only else '; red stays likelier where it read Medium or High'),
                        'kind': 'changed'})
        # what read AI last time and is still here word for word
        last = json.loads((LAST / ('RESULT-%s.json' % part)).read_text(encoding='utf-8'))
        taken = [(text.find(c['text']), text.find(c['text']) + len(c['text'])) for c in out]
        for w in last['windows']:
            if not str(w.get('label', '')).startswith('AI'):
                continue
            seg = last['text'][w['start_index']:w['end_index']].strip()
            if AUDIT_FIRST in seg:
                continue   # the audit is its own part below
            if text.count(seg) == 1:
                pieces = [(seg, {'Low': 0.55, 'Medium': 0.65}.get(w['confidence'], 0.9),
                           'unchanged; read AI (%s, %d words) last time' % (w['confidence'], w['word_count']))]
            else:
                pieces = [(x, 0.3, 'unchanged, in a window that read AI (%s) last time whose other words changed' % w['confidence'])
                          for x in (y.strip() for y in re.split(r'(?<=[.!?”"])\s+|\n', seg)) if len(x.split()) >= 3 and text.count(x) == 1]
            for x, red, why in pieces:
                i = text.find(x)
                if any(a < i + len(x) and b > i for a, b in taken):
                    continue
                taken.append((i, i + len(x)))
                out.append({'name': 'kept: ' + x[:48].rstrip() + '...', 'text': x, 'chance_red': red, 'chance_high': 0.1,
                            'why': why, 'kind': 'changed'})
        if part == 'B':
            a = text.find(AUDIT_FIRST)
            b = text.find(AUDIT_LAST, a) + len(AUDIT_LAST)
            out.append({'name': 'the hypnosis audit (kept, 2c)', 'text': text[a:b], 'chance_red': 0.95, 'chance_high': 0.0,
                        'why': 'his list, kept by his answer 2c, unchanged: read AI (High) in the last three checks',
                        'kind': 'changed'})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(part, len(out), 'parts')


if __name__ == '__main__':
    main()
