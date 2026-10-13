"""Batch 129g: after 127g/128g. P2 with P3 (P2b and P2g, which keep round f's "only …" turn, beside the P3 fixes), P13 with the
passing P14s, P15-P17 diagnostics and P16f/g, P18 one fix at a time on c6-P18, P21f, P25b with only the first sentence's
fixes (b3) and with "help with travel" (b4), and P27 with P28's second sentence under H4 (the cut, a proposal)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
C = json.load(open(HERE.parent / 'cand-current.json', encoding='utf-8'))
V0 = json.load(open(HERE / 'v127-parts.json', encoding='utf-8')); V0.update(json.load(open(HERE / 'v128-parts.json', encoding='utf-8')))
V = {}
V['f-P2g'] = ("I mention vaccination specifically because it's one of the values I would absolutely need to share with people in a community, "
              "if I was going to raise children there. I'm not trying to design a village for everyone, only saying that there needs to be some "
              "common ground among the parents on children's health, enough that they can actually trust one another.")
V['f-P13c'] = ("The safeguards need to be explicit, because this could be badly misunderstood otherwise. The adults still have to pay attention "
               "to what goes on in a children's territory. Older kids can't be allowed to quietly lord it over the younger ones there, and "
               "secrecy can't pass for independence.")
V['f-P13d'] = ("This could be badly misunderstood, so the safeguards need to be explicit. The adults still have to pay attention to what goes "
               "on in a children's territory. Older kids can't be allowed to quietly lord it over the younger ones there, and secrecy can't "
               "pass for independence.")
V['f-P13e'] = C['P13'].replace("I'm making the safeguards explicit, because this could be badly misunderstood otherwise.",
                               "The safeguards need to be explicit, because this could be badly misunderstood otherwise.")
assert V['f-P13e'] != C['P13']
V['f-P16f'] = ("Give children real agency. Kids are allowed to say no, and it counts. No grownup has a right to their affection, physical "
               "contact, obedience outside of legitimate safety needs, or private access to them.")
V['f-P16g'] = ("Give children real agency. A kid's no counts, and no grownup has a right to their affection, physical contact, obedience "
               "outside of legitimate safety needs, or private access to them.")
c6P18 = C['P18']
S3old = "Don't interrogate them, don't punish them if they're not sure, and don't brush off what they report."
S3new = "Don't let the teaching turn into interrogation, punishment when they're not sure, or a reason to brush off what they report."
assert S3old in c6P18
V['f-P18c'] = c6P18.replace(S3old, S3new)
V['f-P18h'] = V['f-P18c'].replace("and how what they say will be taken seriously.", "and how adults will take what they say seriously.")
V['f-P18i'] = V['f-P18c'].replace("may tell it wrong and still need protection.", "may not tell the story perfectly and still need protection.")
assert V['f-P18h'] != V['f-P18c'] and V['f-P18i'] != V['f-P18c']
V['f-P21f'] = ("I also looked through the research corpus for good documentation of an actual case, a child in an intentional community who "
               "remained seriously dangerous to other people, with the whole sequence on record: the conduct, the assessment, the intervention, "
               "the review, and what happened later. I couldn't find any. It's possible that records are private, or that cases were referred "
               "elsewhere. Whatever the reason, I can't claim communities already know how to handle the hardest cases on their own. In those "
               "cases, the child, the family, and the people at risk all need access to competent help and review, outside the control of the "
               "home community.")
v12 = C['P25b']
first_old = v12.split(' It would be great')[0]
first_new = V0['f-P25b1'].split(' It would be great')[0]
V['f-P25b3'] = v12.replace(first_old, first_new)
V['f-P25b4'] = V['f-P25b3'].replace('travel expenses', 'help with travel')
assert V['f-P25b3'] != v12 and V['f-P25b4'] != V['f-P25b3']
V['f-P28a-s2'] = V0['f-P28a'].split("goodwill doesn't answer those questions. ")[1]
H4 = 'Discuss Child-Rearing Values Before Children Are Caught Between Them'
parts = dict(V)
for k in ['f-P2b', 'f-P3e', 'f-P3g', 'f-P3f', 'f-P14a', 'f-P14b', 'f-P17', 'f-P27a', 'f-P27b', 'f-P26']: parts[k] = V0[k]
parts.update({'c-P3': C['P3'], 'c-P15': C['P15'], 'c8-P16': C['P16'], 'c6-P17': 'Create a no-secrets rule. No grownup has a right to ask a kid to keep a secret from their mom or another trusted adult, whether it\'s about a gift, a game, a touch, a conversation or a relationship. A surprise isn\'t a secret, because at the end of a certain date it has to be told. But isolating a kid with secrets isn\'t allowed.', 'c-H4': H4})
assert parts['c6-P17'] == C['P17']
items = [['129g-P2bP3e', ['f-P2b', 'f-P3e']], ['129g-P2bP3g', ['f-P2b', 'f-P3g']], ['129g-P2bP3f', ['f-P2b', 'f-P3f']],
         ['129g-P2bP3c4', ['f-P2b', 'c-P3']], ['129g-P2g', ['f-P2g']], ['129g-P2gP3e', ['f-P2g', 'f-P3e']],
         ['129g-P13cP14b', ['f-P13c', 'f-P14b']], ['129g-P13dP14b', ['f-P13d', 'f-P14b']], ['129g-P13eP14b', ['f-P13e', 'f-P14b']], ['129g-P13dP14a', ['f-P13d', 'f-P14a']],
         ['129g-P15P16c8P17f', ['c-P15', 'c8-P16', 'f-P17']], ['129g-P15P16bP17c6', ['c-P15', 'f-P16b', 'c6-P17']],
         ['129g-P15P16fP17', ['c-P15', 'f-P16f', 'f-P17']], ['129g-P15P16gP17', ['c-P15', 'f-P16g', 'f-P17']],
         ['129g-P18c', ['f-P18c']], ['129g-P18h', ['f-P18h']], ['129g-P18i', ['f-P18i']], ['129g-P21f', ['f-P21f']],
         ['129g-P25b3', ['f-P25b3']], ['129g-P25b4', ['f-P25b4']], ['129g-P25b3P26', ['f-P25b3', 'f-P26']],
         ['129g-H4P27aP28s2', ['c-H4', 'f-P27a', 'f-P28a-s2']], ['129g-H4P27bP28s2', ['c-H4', 'f-P27b', 'f-P28a-s2']]]
json.dump({'batch': '129g', 'parts': parts, 'items': items}, open(HERE / 'v129.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(V, open(HERE / 'v129-parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k in ['f-P13e', 'f-P18c', 'f-P18h', 'f-P18i', 'f-P25b3', 'f-P25b4', 'f-P28a-s2']: print(k, '|', V[k])
