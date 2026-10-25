"""Gather the community readers' findings (READ-<part>.json) into READS-ALL.json and mark the ones that are his.

  python3 articles/intentional-communities/candidate/joel-20261025/emulate-check/explain_findings.py

A finding is his when its new words are in his own words (OWNER-RULINGS.txt, the must_contain strings of his rulings in
../../OWNER-EDITS.json; JOEL-TEXTS.txt; JOEL-EDITS-20261020.md), or came in with his Substack paste of 2026-10-20
(in that paste and not in my version of 2026-10-18); a loss is his when my version of 2026-10-18 still had the words
(MY-FINAL-20261018.md), so they went in his edits or his answers 57 to 65. Each finding's words are looked up in each
version (word for word, else the closest sentence at 80% of its words).
"""
import glob
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import emulate_artifacts as ea  # noqa: E402

CAND = HERE.parents[1]


def main():
    oe = json.loads((CAND / 'OWNER-EDITS.json').read_text(encoding='utf-8'))
    strings = [s for e in oe['entries'] for s in e.get('must_contain', []) if isinstance(s, str)]
    (HERE / 'OWNER-RULINGS.txt').write_text('\n\n'.join(strings) + '\n', encoding='utf-8')
    blocks = {b['i']: b for b in ea.load(CAND / 'joel-20261024' / 'answer65' / 'WORKING.html')}
    mine = ea.Corpus([HERE / 'MY-FINAL-20261018.md'])
    paste = ea.Corpus([CAND / 'joel-20261020' / 'community-final-substack-20261020.html'])
    his = ea.Corpus([HERE / 'OWNER-RULINGS.txt', HERE / 'JOEL-TEXTS.txt', HERE / 'JOEL-EDITS-20261020.md'])

    def present(c, t):
        if not t:
            return 0
        if c.has(t):
            return 1.0
        b = c.best(t)
        return b[0][0] if b else 0

    out = []
    for f in sorted(glob.glob(str(HERE / 'READ-*.json'))):
        part = re.findall(r'READ-(\w+)\.json', f)[0]
        for k, x in enumerate(json.loads(pathlib.Path(f).read_text(encoding='utf-8'))):
            x['id'] = '%s.%d' % (part, k)
            b = blocks.get(x.get('block'))
            x['new_found'] = (not x.get('new')) or (b is not None and ea.norm(x['new']) in ea.norm(b['text']))
            x['explained'] = None
            t = x.get('his') if x['kind'] == 'lost' else x.get('new')
            if x['kind'] == 'lost':
                if present(mine, t) >= 0.8:
                    x['explained'] = 'removed after my 2026-10-18 version (his edits or answers)'
            elif t and (his.has(t) or any(ea.low(t) in ea.low(s) or ea.low(s) in ea.low(t) for s in strings if len(s) > 12)):
                x['explained'] = 'his own words (his rulings, messages or Substack edits)'
            elif t and present(mine, t) < 0.8 and present(paste, t) >= 0.8:
                x['explained'] = 'his Substack edit of 2026-10-20'
            out.append(x)
    (HERE / 'READS-ALL.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(out), 'findings;', sum(1 for x in out if x['explained']), 'his')


if __name__ == '__main__':
    main()
