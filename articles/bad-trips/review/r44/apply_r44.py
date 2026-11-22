#!/usr/bin/env python3
"""apply_r44.py - his round-44 answers (ANSWERS-R44-20261120-1353.json, exported 2026-11-20 13:53:52 UTC) into the guide.
All five cards revised; each version goes in whole, from his last check (../../humanize/h59-20261120/HIS-CHECKS-R44.json):

- TEACH-TRIP-SHADOW (ab6720fc, Human High 370, the whole section): his own paragraph for B415 ("Shadow thoughts also serve
  to show us ..."), moved before "So relax ..." ("i felt that the last para needed more work and was in thew rong place
  also"). His italics kept (*identifying*, *any*). One obvious correction: "we re-identifying as the gold-panners" read as
  "we re-identify as the gold-panners" (checked in place before it went in; the turn's report names it).
- EDIT-AFTERMATH (1e3928a2, Human: Medium 6 on the heading, High 63): B425, "usually" and the children analogy.
- EDIT-SS-LEAD (fe532a4d, Human: Medium 18 on the heading and first sentence, High 95): B132, the payoff first.
- EDIT-CONFRONT (e04e1552, Human High 107): B236, the confrontation folded into "keep them from ...".
- EDIT-REDEFINING (a03b5901, Human High 155): B330c and B357, his two paragraphs.
Two spaces after a comma or full stop in his text are one (typing, not wording).

  python3 articles/bad-trips/review/r44/apply_r44.py      (from the repo root)
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
ANS = json.loads((HERE / 'ANSWERS-R44-20261120-1353.json').read_text(encoding='utf-8'))
A = {i['id']: i for i in ANS['items']}
TYPO = ('we re-identifying as the gold-panners', 'we re-identify as the gold-panners')


def tidy(t):
    return re.sub(r'([,.]) {2,}', r'\1 ', t.strip())


def plain(md):
    return re.sub(r'(?<!\*)\*(?!\*)', '', md.replace('**', ''))


SHADOW = [p.strip() for p in A['TEACH-TRIP-SHADOW']['your_version'].split('\n\n')]
HEAD, S1 = SHADOW[0].split('\n', 1)
S2, S3, S4, S5, S_NEW, S6 = SHADOW[1:]
assert HEAD == 'Dealing With Shadow Thoughts' and S_NEW.startswith('Shadow thoughts also serve') and S6.startswith('So relax')
NEW_B415 = tidy(S_NEW).replace(*TYPO)
B425_HIS = tidy(A['EDIT-AFTERMATH']['your_version'])
SS = A['EDIT-SS-LEAD']['your_version'].split('\n\n')
assert SS[0] == 'Recognizing serotonin toxicity', SS[0]
B132_HIS = tidy(SS[1])
B236_HIS = tidy(A['EDIT-CONFRONT']['your_version'])
RE1, RE2 = [tidy(p) for p in A['EDIT-REDEFINING']['your_version'].split('\n\n')]


def main():
    assert all(A[k]['status'] == 'revise' for k in A), [(k, A[k]['status']) for k in A]
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = [b['id'] for b in B]
    blk = lambda i: B[ids.index(i)]

    # the shadow section: his first five paragraphs are the guide's already (round 43), so only B415 changes and moves
    for i, his in (('B411', S1), ('B412', S2), ('B414', S3), ('R43-SHADOW-LIGHT', S4), ('R43-SHADOW-PRESSURE', S5),
                   ('B413', S6)):
        assert plain(blk(i)['md']) == tidy(his), (i, blk(i)['md'][:80])
    blk('B415')['md'] = NEW_B415
    order = ids[ids.index('B410'):ids.index('B416')]
    want = ['B410', 'B411', 'B412', 'B414', 'R43-SHADOW-LIGHT', 'R43-SHADOW-PRESSURE', 'B415', 'B413']
    if order != want:
        assert order == ['B410', 'B411', 'B412', 'B414', 'R43-SHADOW-LIGHT', 'R43-SHADOW-PRESSURE', 'B413', 'B415'], order
        s = ids.index('B410')
        by = {b['id']: b for b in B[s:s + len(order)]}
        B[s:s + len(order)] = [by[i] for i in want]
        ids = [b['id'] for b in B]

    assert plain(blk('B132')['md']) in (A['EDIT-SS-LEAD']['before'], B132_HIS), blk('B132')['md'][:80]
    blk('B132')['md'] = B132_HIS
    for i, his, before in (('B425', B425_HIS, A['EDIT-AFTERMATH']['before']), ('B236', B236_HIS, A['EDIT-CONFRONT']['before'])):
        assert plain(blk(i)['md']) in (before, his), (i, blk(i)['md'][:80])
        blk(i)['md'] = his
    old_re = A['EDIT-REDEFINING']['before'].split('\n\n')
    assert plain(blk('B330c')['md']) in (old_re[0], RE1) and plain(blk('B357')['md']) in (old_re[1], RE2)
    blk('B330c')['md'], blk('B357')['md'] = RE1, RE2

    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    have = {e['id'] for e in oe['entries']}
    by = 'review/r44/ANSWERS-R44-20261120-1353.json (exported 2026-11-20 13:53:52 UTC), put in by review/r44/apply_r44.py'
    new = [
     {'id': 'r44-shadow-p7-his', 'status': 'applied',
      'what': ("Dealing With Shadow Thoughts' paragraph on identifying with the mind's contents, his own (round 44, "
               "TEACH-TRIP-SHADOW; his check ab6720fc, Human High 370), before \"So relax ...\"; \"we re-identifying\" read as "
               "\"we re-identify\""),
      'joel': ('2026-11-20 13:25 UTC: "all human high conf, i felt that the last para needed more work and was in thew rong '
               'place also"'),
      'applied_by': by, 'must_contain_exact': [NEW_B415],
      'must_not_contain': ["During a trip, don't identify with every shadow thought"]},
     {'id': 'r44-aftermath-his', 'status': 'applied',
      'what': 'What Kind of Aftermath Is This?, his first paragraph (round 44, EDIT-AFTERMATH; his check 1e3928a2)',
      'joel': ('2026-11-20 13:53 UTC: "first i thought "may" sounds so ai, and what i meant was "usually" ... i changed solves '
               'nothing to an analogy about children and it flipped it all high conf human"'),
      'applied_by': by, 'must_contain_exact': [B425_HIS]},
     {'id': 'r44-ss-lead-his', 'status': 'applied',
      'what': 'Recognizing serotonin toxicity, his lead-in with the payoff first (round 44, EDIT-SS-LEAD; his check fe532a4d)',
      'joel': ('2026-11-20 12:35 UTC: "can\'t believe you still don\'t understand what i\'m talking about when i say payoff '
               'first. look, i moved the payoff first and now it\'s almost all human"'),
      'applied_by': by, 'must_contain_exact': [B132_HIS]},
     {'id': 'r44-confront-his', 'status': 'applied',
      'what': ('The First Five Minutes, his dangers paragraph with confrontations folded into "keep them from ..." (round 44, '
               'EDIT-CONFRONT; his check e04e1552, Human High 107)'),
      'joel': 'card EDIT-CONFRONT revised, 2026-11-20 12:37 UTC, his check linked',
      'applied_by': by, 'must_contain_exact': [B236_HIS],
      'must_not_contain': ['If they want to go confront somebody, that can wait.']},
     {'id': 'r44-redefining-his', 'status': 'applied',
      'what': '(Re)defining "Bad Trip", his two paragraphs (round 44, EDIT-REDEFINING; his check a03b5901, Human High 155)',
      'joel': ('2026-11-20 13:46 UTC: "removed the ai tell word "ordinary" (it\'s on your linter right?) and now it\'s all high '
               'conf human"'),
      'applied_by': by, 'must_contain_exact': [RE1, RE2],
      'must_not_contain': ['Samsara, the cycle of ordinary existence']},
    ]
    oe['entries'] += [e for e in new if e['id'] not in have]
    # his room-first decision (round 5, Q-5 a) held B415's old last line word for word; his round-44 paragraph replaces
    # that line, so the record keeps the Grounding Menu's order, which is where the decision still applies
    for e in oe['entries']:
        if e['id'] == 'q5-room-first' and 'Then return to room, body, human, time, and love.' in e.get('must_contain', []):
            e['must_contain'] = [x for x in e['must_contain'] if x != 'Then return to room, body, human, time, and love.']
            e['what'] += (' | 2026-11-20: B415\'s line "Then return to room, body, human, time, and love." went with his '
                          'round-44 paragraph (r44-shadow-p7-his); room before body still holds in the Grounding Menu')
    # three older records held his earlier wording of the lines his round-44 versions changed: they follow his new words,
    # each with a note (his later version supersedes his earlier one)
    FOLLOW = {
        'r06-move-his-version': ("or pools of water for that matter. Letting them move around is fine, and pacing can help, but keep "
                                 "them from taking more of any substance. If they want to go confront somebody, that can wait. "
                                 "And if they want to leave, have someone go with them. Put any weapons away",
                                 "or pools of water for that matter. Letting them move around is fine, and pacing can help, but keep "
                                 "them from taking more of any substance or getting into confrontations. And if they want to "
                                 "leave, have someone go with them. Put any weapons away", 'r44-confront-his'),
        'r27-his-versions': ("When symptoms linger, people too often put everything into the \"I'm broken\" bucket, which solves "
                             "nothing.",
                             "When symptoms linger after a trip, people too often put everything into the \"I'm broken\" "
                             "bucket, the way children sometimes give up at the slightest difficulty.", 'r44-aftermath-his'),
        'r36-teach-ss': ("We can use the same Hunter criteria that clinicians use to diagnose serotonin syndrome.",
                         "To diagnose serotonin syndrome, we can use the Hunter criteria, the same checklist clinicians use.",
                         'r44-ss-lead-his'),
    }
    for e in oe['entries']:
        if e['id'] in FOLLOW:
            old, new, by_id = FOLLOW[e['id']]
            m = e.get('must_contain_exact') or []
            if old in m:
                e['must_contain_exact'] = [new if x == old else x for x in m]
                e['what'] += ' | 2026-11-20: his round-44 version (%s) says this line his new way; the check follows it' % by_id
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    KA = ART / 'KEEP-AS-IS.json'
    ka = json.loads(KA.read_text(encoding='utf-8'))
    for e in ka['keep']:
        if e.get('id') == 'K16' and e['quote'] == ('Letting them move around is fine, and pacing can help, but keep them from taking '
                                                  'more of any substance.'):
            e['quote'] = ('Letting them move around is fine, and pacing can help, but keep them from taking more of any '
                          'substance or getting into confrontations.')
            e['reworded'] = ('2026-11-20 13:53 UTC, his round-44 version (EDIT-CONFRONT, e04e1552, Human High 107): "or getting '
                             'into confrontations" folded into this line, his confront line\'s own sentence gone; the movement '
                             'lines still sit inside his dangers paragraph, where his round-6 fix put them')
    KA.write_text(json.dumps(ka, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied |', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    main()
