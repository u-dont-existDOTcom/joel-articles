"""Section 8, the d3 gate's findings fixed word by word on the current candidate (cand-current.json, the v3 drafts).
Each variant changes only what a finding names; the reason is in the comment above it. Writes v127.json (the
batch spec for gui/mkbatch.py) and v127-parts.json (the variants by key)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
C = json.load(open(HERE.parent / 'cand-current.json', encoding='utf-8'))
V = {}
# P2: stance and logic. "agree with me" -> one of the values he'd need to share; "not even considering" and "only that
# there would need to be" -> the published "not trying to design a village for everyone" and its general claim.
V['f-P2a'] = ("I mention vaccination specifically because it's one of the values I would absolutely need to share with people in a "
              "community, if I was going to raise children there. I'm not trying to design a village for everyone, but communities do "
              "need some common ground among the parents on children's health, enough that they can actually trust one another.")
V['f-P2b'] = ("I mention vaccination specifically because it's one of the values I would absolutely need to share with people in a "
              "community, if I was going to raise children there. I'm not trying to design a village for everyone, only saying that "
              "communities need some common ground among the parents on children's health, enough that they can actually trust one another.")
# P3: "go on about" -> "talk about"; "who lived through" back; "All of this" anchored (d) or kept (a).
V['f-P3a'] = ("All of this will ultimately be reviewed by the kids, once they're grown, and their review weighs more heavily than founders "
              "usually want it to. Adults can talk about their intentions forever, but the kids who lived through it might have something else to say.")
V['f-P3d'] = ("How a community raises its kids will ultimately be reviewed by those kids, once they're grown, and their review weighs more "
              "heavily than founders usually want it to. Adults can talk about their intentions forever, but the kids who lived through it "
              "might have something else to say.")
# P5: both reasons under "because" (no comma); "had no say in" -> "never chose".
V['f-P5'] = ("A friend who reviewed this draft grew up in a Christian commune in Colorado where her father was a pastor. She calls her "
             "childhood \"a treasure and a burden.\" A treasure because she belonged and everybody cared for everybody. A burden because of "
             "the strict religious life she never chose.")
# P7: no comma before "inside", so the shared care is half of the one position.
V['f-P7'] = C['P7'].replace('raise their own kids, inside', 'raise their own kids inside')
# P8: "carried with them and brought into adult life" -> "carried along in ordinary adult life"; "tired" -> "exhausted";
# "their" -> "a child's"; "may be idealizing" -> "may have idealized" (tense with "saw"). b: "one of the biggest reasons".
V['f-P8a'] = ("A big part of why I think community matters for kids is Jean Liedloff's The Continuum Concept. It's one outsider's "
              "interpretation of the Ye'kuana, and she may have idealized what she saw, but it's still a powerful picture. She talks about "
              "how the babies are carried along in ordinary adult life, how the kids are surrounded by people of several ages and learn by "
              "taking part, and how it doesn't fall on one exhausted parent to be a child's whole social world. While a nuclear household "
              "can imitate some of this, a real village can make it normal.")
V['f-P8b'] = V['f-P8a'].replace('A big part of why I think', 'One of the biggest reasons I think')
# P9: "don't sleep and live with" -> "sleep and live apart from"; "need" -> "deserve"; agentless "eventually ended";
# "many" -> "multiple".
V['f-P9a'] = ("Experiments where kids sleep and live apart from their parents deserve special caution. Research on Israeli kibbutzim "
              "found that the practice of kids sleeping communally eventually ended for a mix of reasons: developmental findings, parents' "
              "preferences and social change. Kids can benefit from high-quality group care and multiple loving adults in their lives, but "
              "replacing a secure attachment to their parents is a different matter.")
# P10: "I'd suggest taking a direct look" -> "should study ... directly"; "To be honest" out; "expands a kid's circle".
V['f-P10a'] = ("People should study what's going on at Tamera's Children's Place directly, instead of caricaturing it. My own bias is "
               "still toward a system that expands a kid's circle, without the parent-child bond being made ideologically inconvenient.")
V['f-P10c'] = ("What's going on at Tamera's Children's Place deserves direct study instead of caricature. My own bias is still toward a "
               "system where kids interact with more people, without the parent-child bond being made ideologically inconvenient.")
# P11: "a space to create their own society in, invent" -> "places where they can create their own society, invent".
V['f-P11'] = ("Kids also need their own territory, places where they can create their own society, invent games and work out ordinary "
              "disputes, without always being under the management of adults.")
# P12: "idea" -> "intuition"; "The adults ... the kids" -> generic "Adults ... kids".
V['f-P12'] = ("I got a taste of that at a Unitarian youth camp, and it's still one of the freest memories I have. ZEGG's Kinderhaus "
              "works from a similar intuition. Adults take care of safety on the outside, but kids still get a world of their own.")
# P13: the requirement back ("need to be explicit"); duty on adults ("can't be allowed to"); "dominate"; "treated as".
V['f-P13a'] = ("This can be badly misunderstood, so the safeguards need to be explicit. The adults still have to pay attention to what "
               "goes on in a children's territory. Older kids can't be allowed to quietly dominate the younger ones there, and secrecy "
               "can't be treated as independence.")
V['f-P13b'] = ("The safeguards need to be explicit, because this could be badly misunderstood otherwise. The adults still have to pay "
               "attention to what goes on in a children's territory. Older kids can't be allowed to quietly dominate the younger ones "
               "there, and secrecy can't be treated as independence.")
# P14: rejecting the panic (not "so many suburban folks"); "can" over both halves of the last sentence.
V['f-P14a'] = ("I also don't buy the suburban panic that treats any warm relationship between a child and an unrelated adult as "
               "suspicious. It's good for kids to have a whole bunch of grownups who know them and enjoy them, who would notice when "
               "something changes, and who would act when something's wrong. Fear like that can destroy that gift and still not prevent abuse.")
V['f-P14b'] = ("I also reject the suburban panic that treats any warm relationship between a child and an unrelated adult as "
               "suspicious. It's good for kids to have a whole bunch of grownups who know them and enjoy them, who would notice when "
               "something changes, and who would act when something's wrong. Fear like that can destroy that gift without actually preventing abuse.")
# P16: "Kids are allowed to say no" -> their no carries weight.
V['f-P16a'] = ("Give children real agency. Their \"no\" matters, and no grownup has a right to their affection, physical contact, "
               "obedience outside of legitimate safety needs, or private access to them.")
V['f-P16b'] = ("Give children real agency. When kids say no, it counts, and no grownup has a right to their affection, physical "
               "contact, obedience outside of legitimate safety needs, or private access to them.")
# P17: the added definition out ("A surprise has an end date"); secrets defined by their purpose ("meant to isolate").
V['f-P17'] = ("Create a no-secrets rule. No grownup has a right to ask a kid to keep a secret from their mom or another trusted adult, "
              "whether it's about a gift, a game, a touch, a conversation or a relationship. A surprise has an end date. But secrets "
              "meant to isolate a kid aren't allowed.")
# P18: the added topic out; adults as the listeners; the limits on the teaching back; "tell it wrong" -> "not tell the story perfectly".
V['f-P18a'] = ("Teach truthfulness before there's a crisis. Talk with the kids about the power of their words, and how adults will take "
               "what they say seriously. Don't let the teaching turn into interrogation, punishment when they're not sure, or a reason "
               "to brush off what they report. A scared or confused kid may not tell the story perfectly and still need protection.")
V['f-P18b'] = ("Teach truthfulness before there's a crisis. Make sure the kids understand the power of their words, and that adults "
               "will take what they say seriously. Don't let the teaching turn into interrogation, punishment when they're not sure, or "
               "a reason to brush off what they report. A scared or confused kid may not tell the story perfectly and still need protection.")
# P19: "point a finger at" -> "accuse"; "Be clear about the process" -> "Decide on the response process"; safety first without
# an open licence; the no-silence rule on its own.
V['f-P19b'] = ("Hear the child even when they accuse someone people love. Communities fail here, because the adult may be charismatic, "
               "useful, rich, spiritually important, or everybody's friend. Decide on the response process ahead of time, before anyone's "
               "face is attached to it. Keep everyone safe first, right away, then make sure the accusation is investigated competently "
               "and fairly. Nobody's status buys silence.")
# P20: "perspective on their life" -> "perspective"; "someone to talk to" -> "somewhere to speak"; the court returns them;
# "Counting on" out; "enclosing them" -> "enclosing kids". b keeps the first two as they were.
V['f-P20a'] = ("Make sure kids have relationships and a reporting route outside the community. Grandparents, cousins, local friends, "
               "teachers and other trusted adults give them perspective, and somewhere to speak. Make sure there's at least one trusted "
               "adult, advocate or reporting route they can reach without going through the community's leadership. In 1984, Vermont "
               "authorities seized 112 kids in the Island Pond raid, but a court rejected the state's blanket request and returned them. "
               "State intervention can fail spectacularly, and enclosing kids completely in a community can fail too. Kids need more than one world.")
V['f-P20b'] = V['f-P20a'].replace('give them perspective, and somewhere to speak.', 'give them perspective on their life, and someone to talk to.')
# P21: "my" -> "the"; both search conditions before "I couldn't find one"; the two reasons as possibilities, past, without
# "good documentation"; "Either way" -> "Whatever the reason"; "potential victims" -> "people at risk".
V['f-P21c'] = ("I also looked through the research corpus for good documentation of an actual case, a child in an intentional "
               "community who remained seriously dangerous to other people, where the record covered the whole sequence: the conduct, "
               "the assessment, the intervention, the review, and what happened later. I couldn't find one. It's possible that records "
               "are private, or that cases were referred elsewhere. Whatever the reason, I can't claim communities already know how to "
               "handle the hardest cases on their own. In those cases, the child, the family, and the people at risk all need access to "
               "competent help and review, outside the control of the home community.")
V['f-P21b'] = ("I also looked through the research corpus for good documentation of an actual case, a child in an intentional "
               "community who remained seriously dangerous to other people, but I couldn't find any where the whole sequence was on "
               "record: the conduct, the assessment, the intervention, the review, and what happened later. It's possible that records "
               "are private, or that cases were referred elsewhere. Whatever the reason, I can't claim communities already know how to "
               "handle the hardest cases on their own. In those cases, the child, the family, and the people at risk all need access to "
               "competent help and review, outside the control of the home community.")
# P22: the youth decide (no "let", no "on their own"); "whether to join"; "teenage" back; "far" out; "a big deal" -> "matters".
V['f-P22a'] = ("Amish young people decide as adults whether to join the church, and roughly 85 percent or more of them end up joining. "
               "Pop culture makes their teenage Rumspringa seem wilder and more universal than it is, but it still matters that they're "
               "baptized as adults, because then belonging is a commitment instead of a fact imposed at birth.")
V['f-P22c'] = ("The Amish let their young people decide whether to join the church when they're adults, and roughly 85 percent or more "
               "of them end up joining. Pop culture makes their teenage Rumspringa seem wilder and more universal than it is, but it still "
               "matters that they're baptized as adults, because then belonging is a commitment instead of a fact imposed at birth.")
# P23: any community, not "the kids" (the Amish); "see" -> "encounter"; "for it" out.
V['f-P23'] = ("If a community's kids never leave, it has no way of knowing whether they'd come back freely. So let them study, travel "
              "and make friends, encounter other ways of living, and disagree with the founders, without treating them as traitors.")
# P25a: "ever" out; "a decent education" -> enough not to be helpless; "outside" back.
V['f-P25a'] = ("The realistic standard isn't unlimited freedom. It's just not making it artificially impossible for people to leave. "
               "Kids who grow up without using money especially need to learn enough about how the money world outside operates that "
               "they aren't helpless in it: jobs, rent, contracts, banks, scams, ID, getting around, and how to ask for help.")
# P25b: "They also need" -> "Kids also need" (every kid, not only the money-free ones); "good" x2 out; no "outside the
# community" on the next step, and its "or"; "travel expenses" -> "help with travel"; "avoid punishing"; "needs"; "provides".
V['f-P25b1'] = ("Kids also need transferable skills and education, relationships with people outside the community, access to their "
                "own records and documents, and at least one plausible next step (school, an apprenticeship, work, family, or another "
                "community). It would be great if the community could also provide resources to smooth the transition, like temporary "
                "housing, help with travel, tools or a little money, but even if it can't, it can at least avoid punishing people for "
                "leaving, or holding back the knowledge and records a young adult needs to function outside the community. No upbringing "
                "provides perfect freedom, and the point isn't to erase path dependence. It's to not turn belonging into a trap.")
V['f-P25b2'] = V['f-P25b1'].replace("It would be great if the community could also provide resources to smooth the transition, like "
                                    "temporary housing, help with travel, tools or a little money, but even if it can't, it can",
                                    "If the community can also provide resources to smooth the transition, like temporary housing, help "
                                    "with travel, tools or a little money, great. But even if it can't, it can")
# P26: two groups again; "rather than" on the second only (no comma).
V['f-P26'] = ("It's possible that some of them will leave permanently, and others will start their own communities with different "
              "values rather than wait decades to inherit the original one. And parents may experience that as a loss, even when it's "
              "the movement evolving.")
# P27: "end up with very different opinions about" -> "disagree about" (a) or "split over" (b).
V['f-P27a'] = ("Couples who live together, share the same culture and even the same bed still disagree about screens, vaccinations, "
               "schooling, religion, food, discipline and medical care. And that's just two people. Now think of twenty adults, all with "
               "different childhoods.")
V['f-P27b'] = V['f-P27a'].replace('still disagree about', 'still split over')
# P28: "to hang together" -> coherence offered; "enough room ... to remain parents"; "and still" -> "and".
V['f-P28a'] = ("Once a kid is already living inside the disagreement, goodwill doesn't answer those questions. The community has to "
               "share enough principles about raising kids to offer them coherence, and leave parents enough room to remain parents.")
V['f-P28c'] = ("Once a kid is already living inside the disagreement, goodwill doesn't answer those questions. The community has to "
               "share enough principles about raising kids to be consistent with them, and leave parents enough room to remain parents.")
for k, v in V.items():
    assert '  ' not in v and v == v.strip(), k
keep = {'c-P6': C['P6'], 'c-P15': C['P15'], 'c-P24': C['P24']}
parts = dict(V); parts.update(keep)
items = [
    ['127g-P2a', ['f-P2a']], ['127g-P2aP3a', ['f-P2a', 'f-P3a']], ['127g-P2aP3d', ['f-P2a', 'f-P3d']], ['127g-P2b', ['f-P2b']],
    ['127g-P5P6', ['f-P5', 'c-P6']], ['127g-P5', ['f-P5']], ['127g-P7', ['f-P7']],
    ['127g-P8a', ['f-P8a']], ['127g-P8b', ['f-P8b']],
    ['127g-P9a', ['f-P9a']], ['127g-P9aP10a', ['f-P9a', 'f-P10a']], ['127g-P9aP10c', ['f-P9a', 'f-P10c']],
    ['127g-P11P12', ['f-P11', 'f-P12']],
    ['127g-P13aP14a', ['f-P13a', 'f-P14a']], ['127g-P13bP14b', ['f-P13b', 'f-P14b']], ['127g-P14a', ['f-P14a']], ['127g-P14b', ['f-P14b']],
    ['127g-P15P16aP17', ['c-P15', 'f-P16a', 'f-P17']], ['127g-P15P16bP17', ['c-P15', 'f-P16b', 'f-P17']], ['127g-P17', ['f-P17']],
    ['127g-P18a', ['f-P18a']], ['127g-P18b', ['f-P18b']], ['127g-P19b', ['f-P19b']],
    ['127g-P20a', ['f-P20a']], ['127g-P20b', ['f-P20b']], ['127g-P21c', ['f-P21c']], ['127g-P21b', ['f-P21b']],
    ['127g-P22a', ['f-P22a']], ['127g-P22aP23', ['f-P22a', 'f-P23']], ['127g-P22cP23', ['f-P22c', 'f-P23']],
    ['127g-P25a', ['f-P25a']], ['127g-P25b1', ['f-P25b1']], ['127g-P25b2', ['f-P25b2']], ['127g-P25b1P26', ['f-P25b1', 'f-P26']],
    ['127g-P27aP28a', ['f-P27a', 'f-P28a']], ['127g-P27bP28a', ['f-P27b', 'f-P28a']], ['127g-P27aP28c', ['f-P27a', 'f-P28c']],
    ['127g-P24P27a', ['c-P24', 'f-P27a']], ['127g-P24P28a', ['c-P24', 'f-P28a']],
]
json.dump({'batch': '127g', 'parts': parts, 'items': items}, open(HERE / 'v127.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(V, open(HERE / 'v127-parts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(V), 'variants;', len(items), 'items')
