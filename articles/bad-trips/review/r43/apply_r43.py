#!/usr/bin/env python3
"""apply_r43.py - his round-43 answers (ANSWERS-R43-20261120-0001.json, exported 2026-11-20 00:01:40 UTC) into the guide.

- TEACH-DMSO-WATER revised: his version of the DMSO section's third paragraph (B201), whole, from his check 9dfa6b6d
  (Human High 63).
- TEACH-OPPOSITES revised: his rewrite of Dealing With Shadow Thoughts up to the paragraph after the card's (his check
  4f316acd, Human High 253, the heading and his six paragraphs): B412 keeps its first two sentences; the Hermetic
  paragraph (B414) comes third with his last sentence; two new paragraphs of his (R43-SHADOW-LIGHT, R43-SHADOW-PRESSURE)
  say the two reasons the opposite shows up; "So relax ..." (B413) follows them. His check stops before "During a trip,
  don't identify ..." (B415), the paragraph he left to fix ("you can try to fix p5"), so it stays as it stands.
  The page showed plain text, so the guide's bold stays on the words of his it was on ("does **not** feel").

  python3 articles/bad-trips/review/r43/apply_r43.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
ANS = json.loads((HERE / 'ANSWERS-R43-20261120-0001.json').read_text(encoding='utf-8'))
A = {i['id']: i for i in ANS['items']}

DMSO_HIS = A['TEACH-DMSO-WATER']['your_version'].strip()
PARAS = [p.strip() for p in A['TEACH-OPPOSITES']['your_version'].split('\n\n')]
HEAD, P1 = PARAS[0].split('\n', 1)
assert HEAD == 'Dealing With Shadow Thoughts', HEAD
P2, P3, P4, P5, P6, P7 = PARAS[1:]
BOLD = ('A hated baby does not feel love, and a loved baby does not feel hate.',
        'A hated baby does **not** feel love, and a loved baby does **not** feel hate.')

NEW = [  # the section in his order, as (id, kind, md)
    ('B410', 'h2', '## Dealing With Shadow Thoughts'),
    ('B411', 'p', P1),
    ('B412', 'p', P2),
    ('B414', 'p', P3.replace(*BOLD)),
    ('R43-SHADOW-LIGHT', 'p', P4),
    ('R43-SHADOW-PRESSURE', 'p', P5),
    ('B413', 'p', P6),
]
B415_PLAIN = P7  # "During a trip ..." as the page showed it, unchanged by him


def plain(md):
    return md.replace('**', '')


def main():
    assert A['TEACH-DMSO-WATER']['status'] == 'revise' == A['TEACH-OPPOSITES']['status']
    assert BOLD[0] in P3 and P3.count(' not ') >= 2
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = [b['id'] for b in B]
    blk = lambda i: B[ids.index(i)]

    b201 = blk('B201')
    assert b201['md'] in (A['TEACH-DMSO-WATER']['before'], DMSO_HIS), b201['md'][:80]
    b201['md'] = DMSO_HIS

    assert plain(blk('B415')['md']) == B415_PLAIN, 'B415 changed since the page'
    start = ids.index('B410')
    old_ids = ids[start:ids.index('B415')]
    if old_ids != [i for i, _, _ in NEW]:
        assert old_ids == ['B410', 'B411', 'B412', 'B413', 'B414'], old_ids
        assert blk('B411')['md'] == P1, 'B411 differs from his first paragraph'
        assert blk('B412')['md'].startswith(P2), blk('B412')['md'][:80]
        assert plain(blk('B414')['md']).startswith(P3.split(' A hated')[0]), blk('B414')['md'][:80]
        assert blk('B413')['md'] == 'R' + P6[len('So r'):], blk('B413')['md'][:80]
        fresh = []
        for i, kind, md in NEW:
            b = dict(blk(i)) if i in ids else {'id': i, 'kind': kind, 'md': md, 'text': None}
            b['md'] = md
            fresh.append(b)
        B[start:start + len(old_ids)] = fresh
    else:
        for b, (i, kind, md) in zip(B[start:start + len(NEW)], NEW):
            assert b['id'] == i
            b['md'] = md

    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    have = {e['id'] for e in oe['entries']}
    by = 'review/r43/ANSWERS-R43-20261120-0001.json (exported 2026-11-20 00:01:40 UTC), put in by review/r43/apply_r43.py'
    new = [
     {'id': 'r43-dmso-water-his', 'status': 'applied',
      'what': "DMSO's third paragraph, beside the charcoal water, his version whole (round 43, TEACH-DMSO-WATER; his check 9dfa6b6d, Human High 63)",
      'joel': 'card TEACH-DMSO-WATER revised, 2026-11-19 23:40 UTC, his check linked in his comment',
      'applied_by': by,
      'must_contain_exact': [DMSO_HIS],
      'must_not_contain': ['In my experience there is generally no harm in taking both or mixing them']},
     {'id': 'r43-shadow-his', 'status': 'applied',
      'what': ("Dealing With Shadow Thoughts up to \"So relax ...\", his rewrite whole (round 43, TEACH-OPPOSITES; his check "
               "4f316acd, Human High 253): the Hermetic paragraph third, two new paragraphs of his on why the opposite shows up"),
      'joel': ('2026-11-20 00:01 UTC: "i had to rewrite everything in this section up to this part, it was not written very '
               'well. now it\'s good and human high conf ... you can try to fix p5"'),
      'applied_by': by,
      'must_contain_exact': [P2, NEW[3][2], P4, P5, P6],
      'must_not_contain': ['I also notice them after excessive focus.',
                           'In the subconscious world of concepts, however, two sides are often considered together.']},
    ]
    oe['entries'] += [e for e in new if e['id'] not in have]
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied |', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    main()
