"""Section 3 ("Why Communities Keep Dying in the Same Two Ways") v1, 2026-10-01.

Every published paragraph failed Pangram (base/pangram-s3.jsonl, 8 of 8 at 100% AI), so every paragraph is rewritten.
Each paragraph is an Emulate version (emu/outputs.json) with small logged fixes (EMULATE-FALLBACK section 4, step 4):
facts, inventions, strength and referents only, and never the published sentence put back (the section 2 lesson).
Where two fixes are both defensible, both versions are built and Pangram decides between them; Joel sees the choice.
"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
O = json.load(open(HERE / 'original-blocks.json', encoding='utf-8'))
E = json.load(open(HERE / 'emu/outputs.json', encoding='utf-8'))
def emu(k, i):
    return [p.strip() for p in E[k].split('\n\n')][i]
U_FEC = 'https://www.egalitariancommunities.org/'
U_FARM = 'https://thefarmcommunity.com/'
FIX = {}
def fixed(name, text, swaps, why):
    for a, b in swaps:
        assert text.count(a) == 1, (name, a)
        text = text.replace(a, b)
    FIX[name] = why
    return text
P = {}
P['P1'] = fixed('P1', emu('e1-emuA', 0), [('in one of two ways:', 'in one of two ways.')],
    'Emulate e1-emuA, P1. Fix: the colon became a full stop, since a heading follows, not a list. Kept as wording: "of my acquaintance" for "I knew", "failed from the inside" for "tended to fail inwardly", "Most" for "tended to".')
P['P2'] = fixed('P2', emu('e1-emuA', 1), [('a brilliant solution', 'a solution'), ('a common, well-honed method', 'a common method')],
    'Emulate e1-emuA, P2. Fixes: "brilliant" cut (hype: the published text only says they distributed ownership and labor); "well-honed" cut (it implied they had some method, just not a honed one; the published text says they had no shared way). Kept as wording: "deep waters", the past tense (these are the communes he knew), and "They just became agenda items." for "Those things don\'t disappear. They acquire agenda items."')
P['P3'] = fixed('P3', emu('e2-emuA', 0),
    [('won’t make two people who hate each other like one another', 'won’t make two people who hate each other stop'), ('whether they need a second', 'whether the motion needs a second')],
    'Emulate e2-emuA, P3. Fixes: "won\'t make two people who hate each other like one another" to "... stop" (liking each other is a higher bar than not hating; the published claim is that procedure can\'t even stop the hating); "whether they need a second" to "whether the motion needs a second" (without "motion", "a second" reads as a second person or a second of time, and the joke about seconding a motion is lost). Link kept on "Federation of Egalitarian Communities".')
P['P3'] = P['P3'].replace('The Federation of Egalitarian Communities', '[The Federation of Egalitarian Communities](%s)' % U_FEC, 1)
P['P4b'] = fixed('P4b', emu('e2-emuB', 1), [],
    'Emulate e2-emuB, P2, unchanged. It keeps "carrying emotional material that people can\'t name" and all five things people fight about ("some policy or other"); "when people are together long enough" glosses "Eventually"; "but it won\'t be about that" carries "while the real subject sits nearby with its arms crossed" (the point: the fight isn\'t about what it\'s about).')
P['P4a'] = fixed('P4a', emu('e2-emuA', 1), [('politics will deal with emotional material.', 'politics will carry emotional material that nobody names.')],
    'Emulate e2-emuA, P2. Fix: "politics will deal with emotional material" reversed the point (politics doesn\'t deal with it, it carries it in disguise), and dropped that nobody can name it: now "politics will carry emotional material that nobody names". "or whatever" stands for "policy".')
P['P5'] = fixed('P5', emu('e3-emuA', 0), [('This often comes about', 'This comes about')],
    'Emulate e3-emuA, P1. Fix: "often" cut (the published sentence defines the failure; "often" made it a frequency). Kept as wording: "realizes the importance of embracing a transformation from within", "funneled through a particular person", "usually", "some other special knower of how things really are".')
P['P6a'] = fixed('P6a', emu('e3-emuA', 1), [('The Farm , in Tennessee', 'The Farm, in Tennessee'), ('about 1500 people', 'about 1,500 people'),
    ('But, especially in the early days,', 'But in the early days,'), ('the “doctrine” ran very deep into the lives of community members', 'the doctrine ran deep into members’ intimate decisions'),
    ('to not be able to escape the consciousness of one person’s opinions', 'to barely be able to escape one man’s opinions')],
    'Emulate e3-emuA, P2. Fixes: the stray space and "1500" (noise); "especially" cut (the published text limits it to the early days); the scare quotes on "doctrine" cut (they add a sneer the published text doesn\'t have); "very" cut; "the lives of community members" to "members\' intimate decisions" (the published claim is about intimate decisions); "to not be able to escape the consciousness of one person\'s opinions" to "to barely be able to escape one man\'s opinions" (the published text says "unusually difficult to escape", not impossible; "the consciousness of" was garbled; Gaskin is a man). Link kept on "The Farm". Kept as wording: "It\'s one thing to talk about a universal consciousness. It\'s another ..." for "A group can talk about universal consciousness while ...".')
P['P6a'] = P['P6a'].replace('The Farm', '[The Farm](%s)' % U_FARM, 1)
P['P6b'] = fixed('P6b', emu('e3-emuA', 1), [('The Farm , in Tennessee', 'The Farm, in Tennessee'), ('about 1500 people', 'about 1,500 people'),
    ('But, especially in the early days,', 'But in the early days,'), ('the “doctrine” ran very deep', 'the doctrine ran deep'),
    ('to not be able to escape the consciousness of one person’s opinions', 'to barely be able to escape one man’s opinions')],
    'As P6a, but keeping Emulate\'s "the lives of community members" for "intimate decisions" (one fix fewer, to see whether the fixes cost the pass).')
P['P6b'] = P['P6b'].replace('The Farm', '[The Farm](%s)' % U_FARM, 1)
P['P7'] = fixed('P7', emu('e4-emuB', 0), [('It seems to be that both approaches fail', 'Both approaches fail')],
    'Emulate e4-emuB, P1. Fix: "It seems to be that" cut (the published "The two failures mirror each other" isn\'t hedged). Kept as wording: "fail for symmetric reasons" for "mirror each other"; "fail to address the inner life" for "leave the inner life largely private"; "(while doing a good job at distributing power)"; "fail to distribute power" for "concentrate power around whoever defines the path" (who ends up with the power is said in the next paragraph).')
P['P8a'] = fixed('P8a', emu('e5-emuB', 0), [('It seems like a related problem to me is cult leaders: someone', 'The deeper problem is that someone'), ('The guru who is a good teacher', 'The founder who is a good teacher'),
    ('farmer/business manager', 'farmer or business manager'), ('control all the information', 'control the information')],
    'Emulate e5-emuB, P1. Fixes: "It seems like a related problem to me is cult leaders:" to "The deeper problem is that" (the published text calls it the deeper failure, under both; "cult leaders" was Emulate\'s label, and the hedge was its own); "guru" to "founder" (the published example is a founder who may be a gifted teacher; "guru" comes later, in Joel\'s wish); the slash; "all" cut. Kept as wording: "has authority in multiple domains at once" for "authority earned in one role can be spent in every other role", and the three examples as one fragment.')
P['P8b'] = fixed('P8b', emu('e4-emuB', 1), [('(ie, a community leader/faith-healer, a therapist', '(a community leader, a therapist')],
    'Emulate e4-emuB, P2. Fix: "ie," and the invented "faith-healer" cut. It keeps "earned power in one role ... translate that power to the other roles" (the published mechanism) and the four powers as (a) to (d), but drops that the founder, therapist and farmer may be genuinely good at their role.')
P['P9a'] = fixed('P9a', emu('e5-emuA', 1), [(', that also has peer practice and a playful aspect.', ', that also has peer practice and enough play that it doesn’t become a permanent repair shop.')],
    'Emulate e5-emuA, P2. Fix: "and a playful aspect" to "and enough play that it doesn\'t become a permanent repair shop": the repair-shop line carries a point the article needs (play, so the community isn\'t all healing work), and Joel\'s rule keeps a quip that carries a point. Kept as wording: "a way to work in depth that doesn\'t involve gurus" for "depth without a guru owning it", "where people don\'t come in pre-healed" for "without pretending that people arrive emotionally finished", "peer practice" for "practice between peers".')
P['P9b'] = fixed('P9b', emu('e5-emuA', 1), [(', that also has peer practice and a playful aspect.', '. That needs peer practice, and enough play that the community doesn’t turn into a permanent repair shop.')],
    'As P9a, with the requirement as its own sentence ("That needs ..."), closer to the published "That requires practice between peers, plus enough play ...".')
P['P3e'] = P['P3'].replace('whether the motion needs a second.', 'whether the motion needs a second 🙄')
FIX['P3e'] = 'Proposal only: P3 with 🙄 (on Joel\'s list) after the Robert\'s Rules joke, to mark it as a joke.'
import re
for k in list(P):  # Emulate's straight apostrophes to the article's curly ones (noise; e5 used straight ones)
    P[k] = re.sub(r"(?<=\w)'(?=\w)", "’", P[k])
H1, H2a, H2b = O['H1'], O['H2a'], O['H2b']
plain = lambda md: mdplain.plain(md).strip()
OUT = HERE / 'r1'; OUT.mkdir(exist_ok=True)
words = {}
def put(name, *parts):
    t = plain('\n\n'.join(parts)); (OUT / (name + '.txt')).write_text(t + '\n', encoding='utf-8'); words[name] = len(t.split())
put('H1P1H2P2', H1, P['P1'], H2a, P['P2']); put('P2', P['P2'])
put('P3', P['P3']); put('P3e', P['P3e']); put('P3P4a', P['P3'], P['P4a']); put('P3P4b', P['P3'], P['P4b'])
put('H2P5P6a', H2b, P['P5'], P['P6a']); put('P6a', P['P6a']); put('P6b', P['P6b'])
put('P7P8a', P['P7'], P['P8a']); put('P7P8b', P['P7'], P['P8b']); put('P8a', P['P8a']); put('P8b', P['P8b'])
put('P8aP9a', P['P8a'], P['P9a']); put('P8aP9b', P['P8a'], P['P9b']); put('P8bP9a', P['P8b'], P['P9a'])
json.dump(dict(texts=P, fixes=FIX), open(HERE / 'fixlog-s3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(words)

# ---- v2 (2026-10-01): fixes for the blind trace (TRACE-v1-A.md, TRACE-v1-B.md), the cold read (SENSE-v1.md) and the
# grounding review (GROUNDING-v1.md) on v1's picks. Each is the smallest change that restores the published meaning.
V2 = {}
def v2(name, base, swaps, why):
    t = P[base]
    for a, b in swaps:
        assert t.count(a) == 1, (name, a)
        t = t.replace(a, b)
    V2[name] = t; FIX[name] = why
v2('P1', 'P1', [('failed from the inside', 'went wrong from the inside')],
   'v1 + "failed" to "went wrong" (grounding [1]: under "Keep Dying", "failed" read as most of them collapsing, which the article never says; the published text is about how they went wrong inside).')
v2('P2', 'P2', [('They may have had a solution', 'The secular ones had a solution'), ('They just became agenda items.', 'The feelings just became agenda items.')],
   'v1 + two referent fixes: "They may have had" to "The secular ones had" (cold read [2]: "They" opened the subsection and read as all the communes; the trace: "may have had" hedged what the published text states flatly), and "They just became" to "The feelings just became" (cold read [3]: "They" switched from the communes to the feelings).')
v2('P3', 'P3', [('income-sharing communities', 'income-sharing groups'), ('who hate each other stop.', 'who hate each other stop hating.')],
   'v1 + "communities" to "groups" (grounding [4]: the Federation links communities, it isn\'t one) and "stop" to "stop hating" (cold read [5]: "stop" with no object read as a missing word).')
V2['P3e'] = V2['P3'].replace('whether the motion needs a second.', 'whether the motion needs a second 🙄'); FIX['P3e'] = 'Proposal only: v2 P3 with 🙄.'
v2('P4', 'P4b', [('that people can’t name', 'that nobody can name'), ('It will be a fight about', 'It will be an argument about')],
   'v1 + "people can\'t name" to "nobody can name" and "a fight" to "an argument" (the trace: the published "nobody knows how to name" is universal, and "argue" is milder than "fight").')
v2('P5', 'P5', [('from within. This gets funneled through', 'from within, and then funnels it through')],
   'v1 + the two sentences joined: "... from within, and then funnels it through a particular person ..." (grounding [9] and cold read [9]-[10]: alone, the first sentence made valuing inner change the cause; the failure is routing it through one person, and the community is the one doing the routing; the second "This" had switched referent).')
v2('P6', 'P6a', [('revolved around Stephen Gaskin', 'was deeply shaped by Stephen Gaskin'), ('the doctrine ran deep', 'the community’s doctrine ran deep'), ('to barely be able to escape', 'to struggle to escape')],
   'v1 + "revolved around" to "was deeply shaped by" (grounding [12] and the trace: a stronger claim about a real person than the published one); "the doctrine" to "the community\'s doctrine" (cold read [13]: no doctrine had been named); "barely be able to escape" to "struggle to escape" (the trace: stronger than "unusually difficult to escape").')
v2('P7', 'P7', [('(while doing a good job at distributing power)', '(while distributing power)'), ('but fail to distribute power.', 'but concentrate power.')],
   'v1 + "doing a good job at" cut (grounding [17]: it graded the secular groups a success, against East Wind and the freeloader passage) and "fail to distribute power" to "concentrate power" (the trace: the published text says spiritual groups concentrate power).')
v2('P8', 'P8a', [('or rather, has authority in multiple domains at once.', 'or rather, carries authority earned in one domain into the others.'),
                  ('that actually has a lot of the economy in their hands.', 'that actually carries a lot of the economy.'),
                  ('The problem happens when that person has', 'The danger starts when one person has')],
   'v1 + the deeper failure\'s mechanism back: "has authority in multiple domains at once" to "carries authority earned in one domain into the others" (grounding [18] and the trace: the published point is authority earned in one role and spent in the others; without it the one-role examples didn\'t illustrate anything); "has a lot of the economy in their hands" to "carries a lot of the economy" (the trace: controls vs carries); "The problem happens when that person" to "The danger starts when one person" (cold read [20] and grounding [20]: "problem" in two senses, and "that person" after three people).')
v2('P9', 'P9b', [('that doesn’t involve gurus', 'that no guru owns'), ('where people don’t come in pre-healed', 'where nobody has to come in pre-healed')],
   'v1 + "doesn\'t involve gurus" to "no guru owns" (the trace: the published "without a guru owning it" doesn\'t rule out gurus) and "people don\'t come in" to "nobody has to come in" (the trace and cold read [21]: the published text refuses a pretense, it doesn\'t describe the members).')
OUT2 = HERE / 'r2'; OUT2.mkdir(exist_ok=True)
w2 = {}
def put2(name, *parts):
    t = plain('\n\n'.join(parts)); (OUT2 / (name + '.txt')).write_text(t + '\n', encoding='utf-8'); w2[name] = len(t.split())
S2 = lambda p3: [H1, V2['P1'], H2a, V2['P2'], V2[p3], V2['P4'], H2b, V2['P5'], V2['P6'], V2['P7'], V2['P8'], V2['P9']]
put2('H1P1H2P2', H1, V2['P1'], H2a, V2['P2']); put2('P3', V2['P3']); put2('P3e', V2['P3e']); put2('P3P4', V2['P3'], V2['P4'])
put2('H2P5P6', H2b, V2['P5'], V2['P6']); put2('P6', V2['P6']); put2('P7P8', V2['P7'], V2['P8']); put2('P8', V2['P8']); put2('P8P9', V2['P8'], V2['P9'])
put2('section-v2', *S2('P3')); put2('section-v2e', *S2('P3e'))
(HERE / 'section-v2.md').write_text('\n\n'.join(S2('P3')) + '\n', encoding='utf-8')
json.dump(dict(texts=P, v2=V2, fixes=FIX), open(HERE / 'fixlog-s3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(w2)

# ---- v3 (2026-10-01): v2's section check came back 34% AI, flagging P3 (with P4's first sentence) and P6, and P8+P9 failed
# as a pair. v2's fixes in P3 and P6 were the published wording put back ("groups", "stop hating", "was deeply shaped by").
# So: P4 back to v1 (its v2 fixes were small wording shifts, under Joel's "wording can flex"), with one referent fix;
# P6's strength fix in Emulate's own words (e3-emuB/0301-B: "heavily influenced by"); P3 tested with and without
# "stop hating"; P9 with only the "no guru owns" fix (Emulate's "people don't come in pre-healed" back).
V3 = dict(V2)
def v3(name, base, swaps, why):
    t = base
    for a, b in swaps:
        assert t.count(a) == 1, (name, a)
        t = t.replace(a, b)
    V3[name] = t; FIX['v3-' + name] = why
v3('P2', V2['P2'], [('The secular ones had', 'The secular communes had')],
   'v2 + "ones" to "communes" (the v2 trace: "ones" pointed back to "ways", the nearest plural).')
v3('P3x2', P['P3'], [('income-sharing communities', 'income-sharing groups')],
   'v1 + "communities" to "groups" only (the fact fix: the Federation isn\'t a community); keeps v1\'s "stop".')
V3['P3x1'] = V2['P3']; FIX['v3-P3x1'] = 'v2 as it was ("groups" and "stop hating").'
v3('P4', P['P4b'], [('It will be a fight about', 'There will be a fight about')],
   'v1 (Emulate\'s P4 unchanged) + "It will be a fight" to "There will be a fight" (the v2 trace: "It" could be politics or the emotional material). v2\'s "nobody can name" and "an argument" are dropped: small wording shifts, and they were in the flagged span.')
v3('P6', V2['P6'], [('was deeply shaped by Stephen Gaskin', 'was heavily influenced by Stephen Gaskin')],
   'v2 with "was deeply shaped by" (the published phrase, inside the flagged span) changed to "was heavily influenced by", Emulate\'s own wording in its other version (0301-B), the same strength.')
v3('P9B', P['P9b'], [('that doesn’t involve gurus', 'that no guru owns')],
   'v1 + "doesn\'t involve gurus" to "no guru owns" only (the exact relation: the published text is "without a guru owning it"); Emulate\'s "where people don\'t come in pre-healed" back, since the v2 trace flagged "nobody has to come in" too.')
V3['P9v1'] = P['P9b']
prop = ' There’s no shared way to talk about the hurt itself, but the meeting agenda is the one place the group lets you push for something and win, so the anger goes there, trying to get some justice.'
V3['P4prop'] = V3['P4'] + prop
FIX['v3-P4prop'] = 'Proposal only: P4 with the grounding review\'s good-to-great idea (why the hurt comes out as a fight about the schedule), written by a fresh writer (proposal/P4/w1.txt), its sentence added to v3\'s P4.'
OUT3 = HERE / 'r3'; OUT3.mkdir(exist_ok=True)
w3 = {}
def put3(name, *parts):
    t = plain('\n\n'.join(parts)); (OUT3 / (name + '.txt')).write_text(t + '\n', encoding='utf-8'); w3[name] = len(t.split())
def sec3(p3, p9, p4='P4'):
    return [H1, V2['P1'], H2a, V3['P2'], V3[p3], V3[p4], H2b, V2['P5'], V3['P6'], V2['P7'], V2['P8'], V3[p9]]
put3('H1P1H2P2', H1, V2['P1'], H2a, V3['P2']); put3('P3x2', V3['P3x2']); put3('P3x2P4', V3['P3x2'], V3['P4'])
put3('P6', V3['P6']); put3('H2P5P6', H2b, V2['P5'], V3['P6'])
put3('P8P9v1', V2['P8'], V3['P9v1']); put3('P8P9B', V2['P8'], V3['P9B'])
put3('P4prop', V3['P4prop']); put3('P3x2P4prop', V3['P3x2'], V3['P4prop'])
put3('section-a', *sec3('P3x2', 'P9B')); put3('section-b', *sec3('P3x1', 'P9B'))
json.dump(dict(texts=P, v2=V2, v3=V3, fixes=FIX), open(HERE / 'fixlog-s3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(w3)

# ---- v4 (2026-10-01): section-a (v3) flagged P3's last two sentences with P4's first (12% AI), text identical to section
# v1's, which passed; P9 with "no guru owns" failed in its pair (34% AI). So: P4 as Emulate's other version (P4a, v1's
# fix: "carry emotional material that nobody names"; it keeps "People will argue"), and two other wordings for the
# guru relation.
V4 = dict(V3)
V4['P4a'] = P['P4a']
def v4(name, base, swaps, why):
    t = base
    for a, b in swaps:
        assert t.count(a) == 1, (name, a)
        t = t.replace(a, b)
    V4[name] = t; FIX['v4-' + name] = why
v4('P9C', V3['P9v1'], [('that doesn’t involve gurus', 'that isn’t run by a guru')],
   'v1 + "doesn\'t involve gurus" to "isn\'t run by a guru" (the relation: a guru running it, not gurus being involved; "no guru owns" failed in its pair).')
v4('P9E', V3['P9v1'], [('that doesn’t involve gurus', 'that no guru controls')],
   'v1 + "doesn\'t involve gurus" to "no guru controls".')
OUT4 = HERE / 'r4'; OUT4.mkdir(exist_ok=True)
w4 = {}
def put4(name, *parts):
    t = plain('\n\n'.join(parts)); (OUT4 / (name + '.txt')).write_text(t + '\n', encoding='utf-8'); w4[name] = len(t.split())
def sec4(p9):
    return [H1, V2['P1'], H2a, V3['P2'], V3['P3x2'], V4['P4a'], H2b, V2['P5'], V3['P6'], V2['P7'], V2['P8'], V4[p9]]
put4('P3x2P4a', V3['P3x2'], V4['P4a']); put4('P8P9C', V2['P8'], V4['P9C']); put4('P8P9E', V2['P8'], V4['P9E'])
put4('section-c', *sec4('P9v1')); put4('section-d', *sec4('P9C'))
json.dump(dict(texts=P, v2=V2, v3=V3, v4=V4, fixes=FIX), open(HERE / 'fixlog-s3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(w4)

# ---- v5 (2026-10-01): section-c and section-d (v4) still flag from P3's second sentence ("But the best meeting procedure
# in the world won't make ...") into P4. The gate: start the repair where the flagged span starts. P3 becomes Emulate's
# other version (e2-emuB, P1), which says the same thing in its own build: "It can't make it so that two people don't
# hate each other" (the published strength), seconding spelled out, and the Federation's communities as members.
V5 = dict(V4)
t = emu('e2-emuB', 0)
t = t.replace('a community of the Federation of Egalitarian Communities', 'a community of the [Federation of Egalitarian Communities](%s)' % U_FEC, 1)
V5['P3B'] = t
FIX['v5-P3B'] = 'Emulate e2-emuB, P1, unchanged but for the link (on "Federation of Egalitarian Communities"). It keeps the published strength ("It can\'t make it so that two people don\'t hate each other"), makes the Federation\'s communities its members (the grounding\'s point), and spells out the seconding joke as "one of them has to find somebody who agrees with him or her before they get to talk about it". "isn\'t going to solve every problem, no matter how sophisticated the system ... may be" carries "developed sophisticated systems" as a concession.'
OUT5 = HERE / 'r5'; OUT5.mkdir(exist_ok=True)
w5 = {}
def put5(name, *parts):
    t = plain('\n\n'.join(parts)); (OUT5 / (name + '.txt')).write_text(t + '\n', encoding='utf-8'); w5[name] = len(t.split())
SEC5 = [H1, V2['P1'], H2a, V3['P2'], V5['P3B'], V4['P4a'], H2b, V2['P5'], V3['P6'], V2['P7'], V2['P8'], V4['P9C']]
put5('P3B', V5['P3B']); put5('P3BP4a', V5['P3B'], V4['P4a']); put5('section-g', *SEC5)
(HERE / 'section-v5.md').write_text('\n\n'.join(SEC5) + '\n', encoding='utf-8')
json.dump(dict(texts=P, v2=V2, v3=V3, v4=V4, v5=V5, fixes=FIX), open(HERE / 'fixlog-s3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(w5)

# ---- v6 (2026-10-01): section-g (v5) is 7% AI, now only on P4a ("Sooner or later ..."), whose first sentence carries my v1 fix.
# P4 back to v3's (Emulate's e2-emuB P4 with "There will be a fight"), now after P3B.
SEC6 = [H1, V2['P1'], H2a, V3['P2'], V5['P3B'], V3['P4'], H2b, V2['P5'], V3['P6'], V2['P7'], V2['P8'], V4['P9C']]
OUT6 = HERE / 'r6'; OUT6.mkdir(exist_ok=True)
for name, parts in (('P3BP4', [V5['P3B'], V3['P4']]), ('section-h', SEC6)):
    (OUT6 / (name + '.txt')).write_text(plain('\n\n'.join(parts)) + '\n', encoding='utf-8')
(HERE / 'section-v6.md').write_text('\n\n'.join(SEC6) + '\n', encoding='utf-8')

# ---- v7 (2026-10-01): the final cold read (SENSE-v6.md) and trace (TRACE-v6.md) on v6, which passed whole (100% Human).
# P3: "or other income-sharing community" needed "any" (cold read [4]); "one of them has to find" left the reader asking
# which one (cold read [6]): the one who raises it, as with a motion and its second. P8: "someone has too much authority,
# or rather," is Emulate's added claim (traces v2 and v6), and it made "the deeper problem" read as the spiritual side
# only (cold reads v1, v2 and v6, [17]); without it the sentence is the published point, for both kinds of community.
V7 = dict(V5)
def v7(name, base, swaps, why):
    t = base
    for a, b in swaps:
        assert t.count(a) == 1, (name, a)
        t = t.replace(a, b)
    V7[name] = t; FIX['v7-' + name] = why
v7('P3', V5['P3B'], [('or other income-sharing community', 'or any other income-sharing community'), ('and that one of them has to find', 'and that whoever raises it has to find')],
   'P3B + "any" (cold read [4]) and "one of them" to "whoever raises it" (cold read [6]: which of the two needs backing; it\'s the seconding rule, so the one who raises it).')
v7('P8', V2['P8'], [('someone has too much authority, or rather, carries authority', 'someone carries authority')],
   'v2 + Emulate\'s "has too much authority, or rather," cut (traces v2 and v6: an added claim; cold reads [17]: it made the deeper problem the spiritual side\'s only).')
SEC7 = [H1, V2['P1'], H2a, V3['P2'], V7['P3'], V3['P4'], H2b, V2['P5'], V3['P6'], V2['P7'], V7['P8'], V4['P9C']]
OUT7 = HERE / 'r7'; OUT7.mkdir(exist_ok=True)
for name, parts in (('P3', [V7['P3']]), ('P3P4', [V7['P3'], V3['P4']]), ('P8', [V7['P8']]), ('P7P8', [V2['P7'], V7['P8']]), ('P8P9', [V7['P8'], V4['P9C']]), ('section-v7', SEC7)):
    (OUT7 / (name + '.txt')).write_text(plain('\n\n'.join(parts)) + '\n', encoding='utf-8')
(HERE / 'section-v7.md').write_text('\n\n'.join(SEC7) + '\n', encoding='utf-8')
json.dump(dict(texts=P, v2=V2, v3=V3, v4=V4, v5=V5, v7=V7, fixes=FIX), open(HERE / 'fixlog-s3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

# ---- v8 (2026-10-01): v7 passed whole (100% Human) and in every check but one: P8 (v7) + P9 ("isn't run by a guru")
# came back 37% AI, on P9. P9's second sentence ("That needs peer practice, and enough play ...") is close to the
# published one. Two other P9s with the v7 P8: "no guru controls" (passed with v2's P8), and Emulate's own one-sentence
# build (P9a, v1's pass with P8a) with the guru relation fixed.
V8 = dict(V7)
V8['P9E'] = V4['P9E']
V8['P9aC'] = P['P9a'].replace('that doesn’t involve gurus', 'that isn’t run by a guru')
assert V8['P9aC'] != P['P9a']
FIX['v8-P9aC'] = 'Emulate e5-emuA P2 (v1\'s P9a: one sentence, the repair-shop clause kept) with the guru relation fixed: "isn\'t run by a guru".'
OUT8 = HERE / 'r8'; OUT8.mkdir(exist_ok=True)
for name, parts in (('P8P9E', [V7['P8'], V8['P9E']]), ('P8P9aC', [V7['P8'], V8['P9aC']])):
    (OUT8 / (name + '.txt')).write_text(plain('\n\n'.join(parts)) + '\n', encoding='utf-8')
json.dump(dict(texts=P, v2=V2, v3=V3, v4=V4, v5=V5, v7=V7, v8=V8, fixes=FIX), open(HERE / 'fixlog-s3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

# ---- final (v8): v7 with P9aC, the one P9 that passed with v7's P8.
SEC8 = [H1, V2['P1'], H2a, V3['P2'], V7['P3'], V3['P4'], H2b, V2['P5'], V3['P6'], V2['P7'], V7['P8'], V8['P9aC']]
(OUT8 / 'section-v8.txt').write_text(plain('\n\n'.join(SEC8)) + '\n', encoding='utf-8')
(HERE / 'section-v8.md').write_text('\n\n'.join(SEC8) + '\n', encoding='utf-8')
FINAL = dict(zip(['H1', 'P1', 'H2a', 'P2', 'P3', 'P4', 'H2b', 'P5', 'P6', 'P7', 'P8', 'P9'], SEC8))
json.dump(FINAL, open(HERE / 'final-v8.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
