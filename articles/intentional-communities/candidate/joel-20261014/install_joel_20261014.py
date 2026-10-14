"""Install Joel's answers of 2026-10-14 03:04 UTC (joel-20261014-attachment.txt, his Rule Scoring Sheet answers)
into HUMANIZED-SO-FAR.md, and record them in OWNER-EDITS.json. Run from candidate/.

What goes in:
- F4 (section 2, "Fix it"): his sentence, as written.
- F6 (section 2, "Fix it"): his clause, as written ("... a baby is born or jealousy rears its head.").
- F10 (section 8, "Fix it (revert to yours)"): my sentence from before his 2026-10-07 text ("A scared or confused kid
  may get mixed up telling it and still need protection.", v22), with his own "what happened" for its "it": his
  answers on the I set say an "it" is unclear when what it stands for isn't named nearby.
- I1 (section 4, "Unclear"): his "And it's built on somatic regulation first." names what's built: "And inner pl/ork is
  built on ...", the subsection's subject (reparenting, the other candidate, pulled against section 5 in the stance check).
- W1 (section 12): his preferred P2 and P3 ("i prefer this version"), as written; the ")" after P3 closes his note.
  His P2 replaces mine; his P3 replaces his earlier P3.
His characters are kept (straight quotes and apostrophes, "&").
"""
import json, pathlib

C = pathlib.Path(__file__).resolve().parents[1]
J = C / 'joel-20261014'
art_path = C / 'HUMANIZED-SO-FAR.md'
art = art_path.read_text(encoding='utf-8')
att = (J / 'joel-20261014-attachment.txt').read_text(encoding='utf-8').split('\n')


def rep(t, a, b):
    assert t.count(a) == 1, (a[:60], t.count(a))
    return t.replace(a, b)


# his texts, taken from the attachment's lines
F4 = att[4].split('(replace with "', 1)[1].rsplit('")', 1)[0]
assert F4 == 'No, taking away the idea of a boss does not make everyone less passive, selfish, thieving, nor suddenly unlearning learned helplessness.'
F6 = att[8].strip()
assert F6.startswith('they have no idea why earlier communes failed') and F6.endswith('jealousy rears its head.)')
F6 = F6[:-1]  # the ")" closes his note
P2 = att[41].strip()
P3 = att[43].strip()
assert P2.startswith("This doesn't surprise me") and P3.startswith('So then a lot of people') and P3.endswith('caretaker operation.)')
P3 = P3[:-1]  # the ")" closes his W1 note

# section 2
OLD4 = 'No, taking away the idea of a boss does not make everyone less passive, selfish, steal less, or stop trying to act helpless.'
art = rep(art, OLD4, F4)
OLD6 = 'they have no idea why earlier communes failed or what to do when someone wants to own land, the group runs out of money, a baby is born or someone thinks they own something.'
art = rep(art, OLD6, F6)

# section 4
art = rep(art, "And it's built on [somatic regulation]", 'And inner pl/ork is built on [somatic regulation]')

# section 8
F10_OLD = "A scared or confused kid may get mixed up telling what happened, and that's to be expected."
F10_NEW = 'A scared or confused kid may get mixed up telling what happened and still need protection.'
art = rep(art, F10_OLD, F10_NEW)

# section 12
OLD_P2 = ('This does not surprise me, since we are taught to put on a show of competence in modern society. We have a lot of '
          'incentives to hide ourselves in our lives and disappear behind our screens the second things get uncomfortable. '
          'We have been encouraged by our institutions to be narrow in our skills, and then they act surprised when nobody '
          'can sit through a conflict without appointing a subcommittee or blocking somebody.')
OLD_P3 = ('So the question isn’t whether a person is “good enough” for community. Rather, whether the fit is right. Consider '
          'how much attention they currently have available for other people, how willing they are to examine their own '
          'reactions. And on the other hand, look at whether the group has enough free resource/capacity to support them '
          'without becoming a full-time caretaker operation.')
art = rep(art, OLD_P2, P2)
art = rep(art, OLD_P3, P3)

# candidate notes
art = rep(art, '<!-- CANDIDATE: section 2 v3.1 (2026-10-01,',
          '<!-- CANDIDATE: section 2 v3.2 (2026-10-14): v3.1 with Joel\'s F4 sentence and F6 clause from his Rule Scoring '
          'Sheet answers of 2026-10-14 03:04 UTC (joel-20261014/), as written. Pangram results for v3.2 are in '
          'fix-20261014/RESULTS.md. Before that: section 2 v3.1 (2026-10-01,')
art = rep(art, '<!-- CANDIDATE: section 4 v11 (2026-10-13):',
          '<!-- CANDIDATE: section 4 v11.1 (2026-10-14): v11 with "And reparenting is built on" for "And it\'s built on" '
          '(Joel\'s I1 answer, 2026-10-14: the "it" is unclear); Pangram results in fix-20261014/RESULTS.md. v11 '
          '(2026-10-13):')
art = rep(art, '<!-- CANDIDATE: section 8 v28 (2026-10-07;',
          '<!-- CANDIDATE: section 8 v29 (2026-10-14): v28 with P18\'s last sentence back to mine of v22 with his "what '
          'happened" (Joel\'s F10 answer, 2026-10-14: "Fix it (revert to yours)"); Pangram results in '
          'fix-20261014/RESULTS.md. v28 (2026-10-07;')
art = rep(art, '<!-- CANDIDATE: section 12 v12 (2026-10-13):',
          '<!-- CANDIDATE: section 12 v13 (2026-10-14): v12 with Joel\'s P2 and P3 from his W1 answer of 2026-10-14 03:04 UTC '
          '("i prefer this version"), as written; Pangram results in fix-20261014/RESULTS.md. v12 (2026-10-13):')
art_path.write_text(art, encoding='utf-8')

# ledger
L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id']: e for e in L['entries']}
Q = '2026-10-14 03:04 UTC, Rule Scoring Sheet answers (joel-20261014/joel-20261014-attachment.txt)'
have['s2-c10-fix']['status'] = 'superseded'
have['s2-c10-fix']['superseded_by'] = 's2-joel-20261014-f4'
have['s2-c11b']['status'] = 'superseded'
have['s2-c11b']['superseded_by'] = 's2-joel-20261014-f6'
e = have['s4-p12']
e['must_contain_exact'] = [x for x in e['must_contain_exact'] if x != "And it's built on"]
e['what'] += (' (2026-10-14: Joel\'s I1 answer says the "it" of "And it\'s built on" is unclear, so it names reparenting now; '
              'entry s4-joel-20261014-i1 checks it.)')
e = have['s12-joel-20261013-2100']
e['must_contain'] = [x for x in e['must_contain'] if not x.startswith('So the question isn’t whether')]
e['what'] += ' (2026-10-14: his P3 of his W1 answer replaces this P3; entry s12-joel-20261014-w1 checks it.)'
e = have['s12-joel-20261012-0533']
e['must_contain'] = [x for x in e['must_contain'] if x != 'So the question isn’t whether a person is “good enough” for community.']
e['must_contain'].append('"good enough" for community')
e['what'] += (' (2026-10-14: his W1 P3 keeps "for community" in his own characters: "aren\'t "good enough" for community".)')
new = [
 {'id': 's2-joel-20261014-f4', 'status': 'applied',
  'what': 'Section 2, The Freeloader Problem: F4 "Fix it", his sentence as written.',
  'joel': att[4].strip(), 'when': Q,
  'must_contain': [F4], 'must_not_contain': ['or stop trying to act helpless', 'steal less']},
 {'id': 's2-joel-20261014-f6', 'status': 'applied',
  'what': 'Section 2, the next paragraph: F6 "Fix it", his clause as written ("jealousy rears its head" for "someone thinks they own something").',
  'joel': ' / '.join(x.strip() for x in att[6:9]), 'when': Q,
  'must_contain': ['People want to go back to the old way of living, but ' + F6, 'They just know they are tired and alone and want to change it.'],
  'must_not_contain': ['someone thinks they own something']},
 {'id': 's4-joel-20261014-i1', 'status': 'applied',
  'what': 'Section 4, Inner pl/ork: I1 "Unclear" for his "And it\'s built on somatic regulation first." The sentence names reparenting now.',
  'joel': att[17].strip(), 'when': Q,
  'must_contain': ['And inner pl/ork is built on'], 'must_not_contain': ["And it's built on"]},
 {'id': 's8-joel-20261014-f10', 'status': 'applied',
  'what': 'Section 8, Children Need Freedom Inside Real Protection, P18\'s last sentence: F10 "Fix it (revert to yours)": my v22 sentence back, with his "what happened" for its "it".',
  'joel': att[12].strip(), 'when': Q,
  'must_contain': [F10_NEW], 'must_not_contain': ["and that's to be expected"]},
 {'id': 's12-joel-20261014-w1', 'status': 'applied',
  'what': 'Section 12, P2 and P3: his W1 versions ("i prefer this version"), as written.',
  'joel': 'the last part of the 1st para is that cute, wry and tidy ai quip ... so now looking at that, yeah, 2nd para doesn\'t follow the first, so pangram is right to flag it ... i prefer this version:',
  'when': Q,
  'must_contain': [P2, P3],
  'must_not_contain': ['appointing a subcommittee', 'We have been encouraged by our institutions', 'Rather, whether the fit is right.']},
]
for n in new:
    assert n['id'] not in have
    L['entries'].append(n)
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('installed; ledger entries', len(L['entries']))

# added after the first run: s2-c10 also held the old F4 sentence's start
L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
for e in L['entries']:
    if e['id'] == 's2-c10':
        old = 'No, taking away the idea of a boss does not make everyone less passive, selfish, steal less,'
        if old in e['must_contain']:
            e['must_contain'] = [x for x in e['must_contain'] if x != old]
            e['what'] += ' (2026-10-14: his F4 sentence replaces its last sentence; entry s2-joel-20261014-f4 checks it.)'
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
