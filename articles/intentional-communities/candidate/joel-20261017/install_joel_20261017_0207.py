"""Install Joel's message of 2026-10-17 02:07 UTC (joel-20261017-0207-message.txt). Run from candidate/:
python3 joel-20261017/install_joel_20261017_0207.py

- 35 b: section 13 keeps both, his removal sentence and section 8's ("i don't see how we could cut one of those without
  losing the intended meaning"); nothing changes; a ledger entry checks his sentence stays.
- 36 a: section 10 v5 (make_s10_v5.py): "(with private details protected)" in his last paragraph. 320g: the paragraph Human
  alone (0.10) and the section 100% Human (0.06).
- 37 a: section 14's four short breaks stay; a ledger entry checks them.
- 38 b: section 14 v9 (s14/make_v9.py): his P2 as written. 319g: Human alone (0.01) and the section 100% Human (0.15).
- "accept 13 and 14.": sections 13 (v34) and 14 (v9) are accepted. Their notes become ACCEPTED notes, which the article page
  doesn't show (only CANDIDATE notes show), and EDITORIAL-STATUS.json records it.
"""
import json, pathlib, re

C = pathlib.Path(__file__).resolve().parents[1]
HERE = C / 'joel-20261017'
ART = C / 'HUMANIZED-SO-FAR.md'
art = ART.read_text(encoding='utf-8')
MSG = 'joel-20261017/joel-20261017-0207-message.txt'


def rep(t, a, b):
    assert t.count(a) == 1, (a[:70], t.count(a))
    return t.replace(a, b)


# 36 a
v4 = (HERE / 's10-v4-installed.md').read_text(encoding='utf-8').strip()
v5 = (HERE / 's10-v5.md').read_text(encoding='utf-8').strip()
art = rep(art, v4, v5)
art = rep(art, '<!-- CANDIDATE: section 10 v4 (2026-10-15 09:33):',
          '<!-- CANDIDATE: section 10 v5 (2026-10-17 02:07): v4 with "(with private details protected)" after "store the full '
          'case history" in the last paragraph (Joel\'s 36 a; joel-20261017/). Pangram 320g: the paragraph Human alone (0.10), '
          'the section 100% Human, high (0.06, https://www.pangram.com/history/a20d6f1a-66a7-41c6-9468-1524d6578d72). Before: '
          'section 10 v4 (2026-10-15 09:33):')
# 38 b and the acceptance of 13 and 14
v8 = (C / 's14' / 'v8.md').read_text(encoding='utf-8').strip()
v9 = (C / 's14' / 'v9.md').read_text(encoding='utf-8').strip()
art = rep(art, v8, v9)
i = art.index('<!-- CANDIDATE: section 14 v8')
j = art.index('-->', i) + 3
art = art[:i] + ('<!-- ACCEPTED: section 14 v9 (2026-10-17): accepted by Joel at 02:07 UTC ("accept 13 and 14."), with his P2 of the '
                 'same message (38 b: the repeated bridging question cut; s14/make_v9.py). Pangram 319g: his P2 Human alone (0.01), '
                 'the section 100% Human, high (0.15, https://www.pangram.com/history/ecdae74f-2cb1-47fe-97b4-86f5aff0a620). '
                 'Before: section 14 v8 (2026-10-17): v5 deduplicated at his word; every paragraph Human alone (305g-x, 315g). '
                 'Records: s14/review-r1 to review-r6, batches b300 to b306, b313, b315, b319, and s13/b316. -->') + art[j:]
i = art.index('<!-- CANDIDATE: section 13 v34')
j = art.index('-->', i) + 3
note = art[i:j]
assert 'Not accepted until Joel says so.' in note
art = art[:i] + note.replace('<!-- CANDIDATE: section 13 v34 (2026-10-17):',
                             '<!-- ACCEPTED: section 13 v34 (2026-10-17): accepted by Joel at 02:07 UTC ("accept 13 and 14."), keeping '
                             'both his removal sentence and section 8\'s (35 b). Before acceptance:').replace(
                             ' Not accepted until Joel says so.', '') + art[j:]
ART.write_text(art, encoding='utf-8')

L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id']: e for e in L['entries']}
e = have['s10-joel-20261014-2119']
old = [s for s in e['must_contain_exact'] if 'store the full case history so it can be' in s]
assert len(old) == 1
e['must_contain_exact'] = [s.replace('store the full case history so it can be',
                                     'store the full case history (with private details protected) so it can be') if s == old[0] else s
                           for s in e['must_contain_exact']]
e['what'] += ' (2026-10-17 02:07: "(with private details protected)" after "store the full case history", his 36 a; entry s10-joel-20261017-0207-36a.)'
new = [
    {'id': 's13-joel-20261017-0207-35b', 'status': 'applied', 'words': 'his',
     'what': 'Section 13, "When Somebody Has to Go": his sentence about deciding the removal process early stays, and so does section 8\'s about a child\'s report (question 35 b). Nothing cut.',
     'joel': '35b because i don\'t see how we could cut one of those without losing the intended meaning (that should be a standing dedup pass rule, you can only cut if it isn\'t losing important meaning or there\'s no good way to merge)',
     'when': '2026-10-17 02:07 UTC (%s)' % MSG,
     'must_contain': ["So work out the process before it's about anyone in particular.",
                      "Decide on the response process ahead of time, before anyone's face is attached to it."]},
    {'id': 's10-joel-20261017-0207-36a', 'status': 'applied', 'words': 'proposed',
     'what': 'Section 10, the last paragraph: "(with private details protected)" after "store the full case history" (question 36 a, my wording, his pick).',
     'joel': '36a', 'when': '2026-10-17 02:07 UTC (%s)' % MSG,
     'must_contain': ['store the full case history (with private details protected) so it can be re-evaluated in future']},
    {'id': 's14-joel-20261017-0207-37a', 'status': 'applied', 'words': 'proposed',
     'what': 'Section 14: the four short breaks stay, "Who would?", "That\'s a lot of loose ends!", "Who wants that?" and "(as you may have noticed!)" (question 37 a).',
     'joel': '37a', 'when': '2026-10-17 02:07 UTC (%s)' % MSG,
     'must_contain': ['Who would?', "That's a lot of loose ends!", 'Who wants that?', '(as you may have noticed!)']},
    {'id': 's14-joel-20261017-0207-38b', 'status': 'applied', 'words': 'his',
     'what': 'Section 14, P2: his paragraph as written (question 38 b): the repeated question about bridging people\'s food, housing and care, and any outside cash or benefits, is cut.',
     'joel': '38b simple i just deleted the 2nd one and it\'s still human on pangram: ...', 'when': '2026-10-17 02:07 UTC (%s)' % MSG,
     'must_contain_exact': [(C / 's14' / 'v9.md').read_text(encoding='utf-8').split('\n\n')[[k for k, b in enumerate((C / 's14' / 'v9.md').read_text(encoding='utf-8').split('\n\n')) if b.startswith('If the community dissolves')][0]].strip()],
     'must_not_contain': ['Who takes responsibility for bridging']},
]
for n in new:
    assert n['id'] not in have
    L['entries'].append(n)
(C / 'OWNER-EDITS.json').write_text(json.dumps(L, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

E = C.parent / 'EDITORIAL-STATUS.json'
ed = json.load(open(E, encoding='utf-8'))
ed.setdefault('accepted', [])
for sec, ver in ((13, 'v34'), (14, 'v9')):
    ed['accepted'].append({'section': sec, 'version': ver, 'by': 'Joel', 'when': '2026-10-17 02:07 UTC', 'words': 'accept 13 and 14.',
                           'record': MSG})
ed['note'] = ed['note'].rstrip() + ' Accepted sections are listed under "accepted", with Joel\'s words; their notes in candidate/HUMANIZED-SO-FAR.md start "ACCEPTED:" instead of "CANDIDATE:".'
open(E, 'w', encoding='utf-8').write(json.dumps(ed, ensure_ascii=False) + '\n')
print('installed Joel\'s 02:07 answers')
