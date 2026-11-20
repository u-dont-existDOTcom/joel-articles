"""Put his answers of 2026-11-20 17:05 UTC that change only words of his into HUMANIZED-SO-FAR.md (his message:
../joel-20261120-1705-message.txt; the questions: ../../OWNER-QUESTIONS.md, 15 to 23).

- 15a: the DMSO item's clause on children says it means uses other than IV: "when it's not given by IV", the words
  question 15 showed him.
- 19a: Weeks 1-2's agmatine line: "increase PS" becomes "start PS", as question 19 showed.
- 20: the mackerel line says its PS is above the dose that worked, with his caveat in his words ("you can say it's
  above, although when not isolated, it's harder to compare").
- 21b: Weeks 3-5's first PS line says "Reduce or stop", as its other PS line does.
- 22a: the agmatine section's cycle rule gets the exception Weeks 3-5 gives, in that line's own words.

16a and 17 (a new line of mine at the top of Weeks 3-5) go in only after their checks; 18 and 23 go to him as cards.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1120a/apply_x1120a.py [--write]

Each change goes in once: a change already in the article is skipped.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
CHANGES = [
    ('15a', "although so far there's no proof it's harming children, and many people use it",
     "although so far there's no proof it's harming children when it's not given by IV, and many people use it",
     'his clause, with the words question 15 showed him'),
    ('19a', 'Do not add agmatine on the same day you increase PS,', 'Do not add agmatine on the same day you start PS,',
     'his line, with the word question 19 showed him'),
    ('20', 'A 200g mackerel fillet ≈ 960 mg PS--above clinical doses.',
     "A 200g mackerel fillet ≈ 960 mg PS--above the 400 mg that worked, although when it's not isolated, it's harder "
     'to compare.', 'his line, "above" the dose his PS section says worked, and his caveat in his words'),
    ('21b', 'Protocol:Taper off Phosphatidylserine here.', 'Protocol:Reduce or stop phosphatidylserine here.',
     'his line, in the words of his other Weeks 3-5 PS line, as question 21 offered'),
    ('22a', '7–14 day anxiety-phase experiment, not a forever baseline. Stop if',
     '7–14 day anxiety-phase experiment, not a forever baseline, unless it is unmistakably helping acute glutamate '
     'storms without worsening flatness. Stop if', "his line, with Weeks 3-5's exception in that line's own words"),
]


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(md.encode('utf-8')).hexdigest()
    lines = md.split('\n')
    applied = []
    for answer, old, new, whose in CHANGES:
        if any(new in l for l in lines):
            continue
        (i,) = [k for k, l in enumerate(lines) if old in l]
        assert lines[i].count(old) == 1
        applied.append({'answer': answer, 'line': i + 1, 'old': lines[i], 'new': lines[i].replace(old, new),
                        'whose': whose})
        lines[i] = lines[i].replace(old, new)
    out = '\n'.join(lines)
    rec = {'about': 'his answers of 2026-11-20 17:05 UTC that change only words of his: 15a, 19a, 20, 21b, 22a',
           'message': '../joel-20261120-1705-message.txt', 'applied': applied,
           'held': ['16a and 17: a new line of mine at the top of Weeks 3-5, after its checks',
                    '18 and 23: his new points, checked against sources, go to him as cards'],
           'before_sha256': before, 'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], [x['answer'] for x in applied])
    if write and applied:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1120A.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
