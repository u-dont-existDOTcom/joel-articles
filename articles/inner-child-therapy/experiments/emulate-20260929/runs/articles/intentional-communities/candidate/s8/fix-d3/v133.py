"""Batch 133g: the d4 gate's findings (TRACE-d4-*, LOGIC-d4-*, SENSE-d4, STANCE-d4) fixed word by word on cand-v21, each with
its reason. Writes v133-parts.json and the batch spec v133.json."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
B = json.load(open(HERE.parent / 'cand-v21.json', encoding='utf-8'))
V0 = {}
for f in ('v127-parts.json', 'v128-parts.json', 'v129-parts.json', 'v130-parts.json', 'v131-parts.json'):
    V0.update(json.load(open(HERE / f, encoding='utf-8')))
V = {}
# P2 (logic A/B CHANGED): "only saying that" made the agreement a disclaimer; the published semicolon lets it be the reason the
# village isn't for everyone. Two sentences keep both readings. "among the parents" out: the agreement is the community's.
V['g-P2n'] = ("I mention vaccination specifically because it's one of the values I would absolutely need to share with people in a "
              "community, if I was going to raise children there. I'm not trying to design a village for everyone. Communities need some "
              "common ground on children's health, enough that parents can actually trust one another.")
# P7 (logic A, trace A): "should" can read as a duty laid on mothers; the published states the arrangement.
V['g-P7n'] = B['P7'].replace('moms should raise their own kids', 'moms raise their own kids')
# P8 (trace A): "She talks about how" made Liedloff the stated source of every item; the published gives the list as the picture.
V['g-P8n2'] = ("One of the biggest reasons I think community matters for kids is Jean Liedloff's The Continuum Concept. It's one outsider's "
               "interpretation of the Ye'kuana, and she may have idealized what she saw, but it's still a powerful picture: the babies are "
               "carried along in ordinary adult life, the kids are surrounded by people of several ages and learn by taking part, and it "
               "doesn't fall on one exhausted parent to be a child's whole social world. While a nuclear household can imitate some of this, "
               "a real village can make it normal.")
# P10 (trace A): "People should study" casts people at large as the caricaturists; P10c keeps "deserves direct study" (it passed
# beside P9a in 127g). g: the system as the agent again ("without making the bond…").
V['g-P10g'] = ("What's going on at Tamera's Children's Place deserves direct study instead of caricature. My own bias is still toward a "
               "system where kids interact with more people, without making the parent-child bond ideologically inconvenient.")
# P13 (trace B): "lord it over" is lighter than "dominate"; "pass for" can read as a fact, not a rule. One fix each.
V['g-P13f'] = V0['f-P13d'].replace('quietly lord it over the younger ones', 'quietly dominate the younger ones')
V['g-P13g'] = V0['f-P13d'].replace("secrecy can't pass for independence", "secrecy can't be treated as independence")
# P14 (trace B, logic A): "don't buy" is weaker than "reject"; "any" after it can read as ruling out justified suspicion.
V['g-P14c'] = ("I also reject the suburban panic that treats every warm relationship between a child and an unrelated adult as suspicious. "
               "It's good for kids to have a whole bunch of grownups who know them and enjoy them, who would notice when something changes, "
               "and who would act when something's wrong. Fear like that can destroy that gift and still not prevent abuse.")
# P16 (logic B, the most serious): "When kids say no" could govern the next clause, so adults lose their claims only after a refusal.
V['g-P16h'] = ("Give children real agency. When kids say no, it counts. No grownup has a right to their affection, physical contact, "
               "obedience outside of legitimate safety needs, or private access to them.")
# P17 (trace B, logic A minor): the added definition; the published plural "Surprises".
V['g-P17l'] = V0['f-P17j'].replace("A surprise isn't a secret, because at the end of a certain date it has to be told.", "Surprises have an end date.")
# P18 (trace B, logic A): the goal back ("Make sure the kids understand"), one fix at a time; "badly" is stronger than "imperfectly".
V['g-P18l'] = V0['f-P18j'].replace('Talk with the kids about', 'Make sure the kids understand')
V['g-P18m'] = V0['f-P18j'].replace('may tell it badly and still need protection.', 'may get mixed up telling it and still need protection.')
# P19 (trace B, logic B CHANGED): "they accuse" casts the child as the accuser; "everyone" includes the accused.
V['g-P19c'] = ("Hear the child even when the accused is someone people love. Communities fail here, because the adult may be charismatic, "
               "useful, rich, spiritually important, or everybody's friend. Decide on the response process ahead of time, before anyone's "
               "face is attached to it. Keep whoever's at risk safe first, right away, then make sure the accusation is investigated "
               "competently and fairly. Nobody's status buys silence.")
# P21 (trace C, logic A/B): "couldn't find any where the whole sequence was on record" suggests partial cases turned up; the
# search target now holds both conditions ("a good, complete record"), then "I couldn't find one."
V['g-P21g'] = ("I also looked through the research corpus for a good, complete record of an actual case, a child in an intentional "
               "community who remained seriously dangerous to other people: the conduct, the assessment, the intervention, the review, and "
               "what happened later. I couldn't find one. It's possible that records are private, or that cases were referred elsewhere. "
               "Whatever the reason, I can't claim communities already know how to handle the hardest cases on their own. In those cases, "
               "the child, the family, and the people at risk all need access to competent help and review, outside the control of the home community.")
# P22 (trace C): "their teenage Rumspringa" states that every Amish youth has one; the caricature is the published claim.
V['g-P22d'] = ("Amish young people decide as adults whether to join the church, and roughly 85 percent or more of them end up joining. Pop "
               "culture makes Rumspringa seem like a wilder, more universal teenage free-for-all than it is, but it still matters that they're "
               "baptized as adults, because then belonging is a commitment instead of a fact imposed at birth.")
V['g-P22e'] = ("Amish young people decide as adults whether to join the church, and roughly 85 percent or more of them end up joining. The "
               "pop-culture picture of Rumspringa as a universal teenage free-for-all is exaggerated, but it still matters that they're "
               "baptized as adults, because then belonging is a commitment instead of a fact imposed at birth.")
# P23 (logic A): "without treating them as traitors" can mean the founders; the published passive back.
V['g-P23n'] = ("If a community's kids never leave, it has no way of knowing whether they'd come back freely. So let them study, travel and "
               "make friends, encounter other ways of living, and disagree with the founders without being treated as traitors.")
# P25a (logic A, sense [75]): "It's just not making it…" (the standard as merely a negative duty; a reread).
V['g-P25a2'] = V0['f-P25a'].replace("It's just not making it artificially impossible for people to leave.", "It's that leaving shouldn't be made artificially impossible.")
# P25b (stance, trace C): "travel expenses" and "a little money" turn the help into cash; the published "travel help" and "a small
# transition reserve".
V['g-P25b10'] = V0['f-P25b9'].replace('like temporary housing, travel expenses, tools or a little money,', 'like temporary housing, help with travel, tools or a small reserve,')
# P26 (trace C, logic A/B): "others will start" outside "It's possible"; "and that" keeps both under it.
V['g-P26n'] = V0['f-P26'].replace('and others will start their own communities', 'and that others will start their own communities')
for k, v in V.items():
    assert '  ' not in v and v == v.strip(), k
for k, base in (('g-P7n', B['P7']), ('g-P13f', V0['f-P13d']), ('g-P13g', V0['f-P13d']), ('g-P17l', V0['f-P17j']), ('g-P18l', V0['f-P18j']),
                ('g-P18m', V0['f-P18j']), ('g-P25a2', V0['f-P25a']), ('g-P25b10', V0['f-P25b9']), ('g-P26n', V0['f-P26'])):
    assert V[k] != base, k
parts = dict(V)
for k in ('f-P9a', 'f-P10a', 'f-P13d', 'f-P14a', 'f-P17j', 'f-P27a', 'f-P28a'): parts[k] = V0[k]
parts['c-P3'] = B['P3']; parts['c-P15'] = B['P15']; parts['f-P3e'] = V0['f-P3e']
items = [['133g-P2n', ['g-P2n']], ['133g-P2nP3c4', ['g-P2n', 'c-P3']], ['133g-P2nP3e', ['g-P2n', 'f-P3e']], ['133g-P7n', ['g-P7n']],
         ['133g-P8n2', ['g-P8n2']], ['133g-P9aP10g', ['f-P9a', 'g-P10g']],
         ['133g-P13fP14c', ['g-P13f', 'g-P14c']], ['133g-P13gP14c', ['g-P13g', 'g-P14c']], ['133g-P13dP14c', ['f-P13d', 'g-P14c']],
         ['133g-P13fP14a', ['g-P13f', 'f-P14a']], ['133g-P14c', ['g-P14c']],
         ['133g-P15P16hP17j', ['c-P15', 'g-P16h', 'f-P17j']], ['133g-P15P16hP17l', ['c-P15', 'g-P16h', 'g-P17l']],
         ['133g-P18l', ['g-P18l']], ['133g-P18m', ['g-P18m']], ['133g-P19c', ['g-P19c']], ['133g-P21g', ['g-P21g']],
         ['133g-P22dP23n', ['g-P22d', 'g-P23n']], ['133g-P22eP23n', ['g-P22e', 'g-P23n']], ['133g-P22d', ['g-P22d']],
         ['133g-P25a2', ['g-P25a2']], ['133g-P25b10', ['g-P25b10']], ['133g-P25b10P26n', ['g-P25b10', 'g-P26n']]]
json.dump({'batch': '133g', 'parts': parts, 'items': items}, open(HERE / 'v133.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(V, open(HERE / 'v133-parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(V), 'variants;', len(items), 'items')
