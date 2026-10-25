"""CHANGED.json for the whole guide's recheck of 2026-10-25 (parts A and B, after make_recheck.py): every paragraph of each
part's checked text that isn't word for word in the text Pangram last read for that part (part A: recheck A4 of
2026-10-23, ../../fix-20261023/recheck-a4/RESULT-A.json; part B: recheck B2, ../../fix-20261023/recheck-b2/RESULT-B.json),
with my chance that it reads red, by how much of it changed against the closest paragraph of the last text:
- 95% or more the same (a mark, a typo, a quote mark off, one word such as "guard" for "protector"): CHANCES[0]
- 80% to 95% (a clause, his own words back): CHANCES[1]
- 50% to 80%: CHANCES[2]
- less, or new: CHANCES[3]
The changes are his answers of 19:42 UTC (../review/APPLIED.json), the strict Emulate check's fixes, his answers to
question 20 (../emulate-check/APPLIED-20.json) and the guard sweep (../emulate-check/GUARD-SWEEP.json). Most new
sentences are his own or ones he approved, and the gate's reviewers passed mine; Emulate's sentences that stayed were in
the last checks. part_forecast.py adds each changed paragraph's neighbours itself (gate E249).

  python3 articles/inner-signal/humanize/fix-20261025/recheck/make_changed.py
"""
import difflib
import json
import pathlib
import re

X = pathlib.Path(__file__).resolve().parent
LAST = {'A': X.parents[1] / 'fix-20261023' / 'recheck-a4' / 'RESULT-A.json',
        'B': X.parents[1] / 'fix-20261023' / 'recheck-b2' / 'RESULT-B.json'}
CHANCES = (0.01, 0.04, 0.10, 0.15)


def words(s):
    return re.findall(r'\w+', s.lower())


def main():
    for part in ('A', 'B'):
        new = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        last = json.loads(LAST[part].read_text(encoding='utf-8'))['text']
        old_paras = [p for p in last.split('\n') if p.strip()]
        old_set = set(old_paras)
        old_words = [words(p) for p in old_paras]
        out = []
        for p in new.split('\n'):
            if not p.strip() or p in old_set or len(p) < 40 or new.count(p) != 1:
                continue
            w = words(p)
            best = max((difflib.SequenceMatcher(None, w, o, autojunk=False).ratio() for o in old_words if o), default=0)
            k = 0 if best >= 0.95 else 1 if best >= 0.8 else 2 if best >= 0.5 else 3
            out.append({'name': '%s-p%d' % (part, len(out) + 1), 'text': p, 'chance_red': CHANCES[k],
                        'why': 'changed since the last check: %d%% of its words as in the closest paragraph then' % round(100 * best)})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        by = [sum(1 for x in out if x['chance_red'] == c) for c in CHANCES]
        print(part, len(out), 'changed paragraphs; by size of change:', dict(zip(CHANCES, by)))


if __name__ == '__main__':
    main()
