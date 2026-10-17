"""Section 13 draft v27 (2026-10-16, Joel's 34 a at 21:05 UTC: "34a and learn from how emulate fixes it"): v26 with the two
stretches that read AI inside the whole section (304g stage 2) taken from Emulate round j (emu-j/out/, byte for byte from the
laptop, sha256 checked), each stretch sent whole.

How the meaning goes back this time (the lesson of round i, docs/HUMANIZATION-GATE.md, "What Emulate's rewrites change"): the
land subsection read Human after round i because its final wording kept Emulate's loose, spoken shape (run-on lists, a clause
out of place, short reactions, repeated words, "etc.") and put back only the meaning, in that shape. Where a fix here needs
the published meaning, it goes into Emulate's sentence, not back into the published one.
- H1-P3, H1-P4, H2-P2, H2-P3, H2-P3b: Emulate's call A, with the meaning it lost or shifted put back (each fix below).
- H2-P4: call B, which keeps the four questions call A dropped.
- H2-P1 stays v26's (the vacation-rental monologue, Emulate's earlier round, Human alone and in the section).
- H5-P1 to H5-P4: call A, with the published meaning back where A shifted it (the conditional ejection, "especially if", the
  Zapatista sentence), Joel's two sentences as he wrote them ("So work out the process before it's about anyone in
  particular." and the linked "My research initially leaned too far that way.").
Writes v27.md, v27b.md (way B keeps v26b's H5-P2 out: one way only from here, since Emulate rewrote H5-P2 whole) and
v27-fixes.json. Run from this folder: python3 make_v27.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'emu-j' / 'out'
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
blocks = lambda md: [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]
V26 = blocks((HERE / 'v26.md').read_text(encoding='utf-8'))
assert len(V26) == len(IDS)
EMU = {k: blocks((OUT / (k + '.txt')).read_text(encoding='utf-8')) for k in ('j01-emuA', 'j01-emuB', 'j02-emuA', 'j02-emuB')}
J01 = ['H1-P3', 'H1-P4', 'heading', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4']
J02 = ['heading', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
src = {}
for k, units in (('j01-emuA', J01), ('j01-emuB', J01), ('j02-emuA', J02), ('j02-emuB', J02)):
    assert len(EMU[k]) == len(units), (k, len(EMU[k]))
    for u, b in zip(units, EMU[k]):
        src[(k, u)] = b
JOEL_H5P2 = "So work out the process before it's about anyone in particular."
JOEL_H5P3 = ('[My research](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) initially leaned too far '
             'that way.')
NEW = {
 'H1-P3': ('j01-emuA',
   "Until that’s happened, the group’s still a circle of promising strangers, and I wouldn’t ask that circle to take out a "
   "mortgage yet. That’s okay! There’s lots you can do! You can all meet in a rented or borrowed space, or at each other’s "
   "houses, and find out how much conflict the group can handle before you need a surveyor.",
   ['"Until then" -> "Until that’s happened" (H1-P2 ends on "Until then, what’s it worth?")',
    '"it’s still just a group" -> "the group’s still a circle of promising strangers" (his published words, keys U7)',
    '"maybe you don’t want to take out a mortgage yet" -> "I wouldn’t ask that circle to take out a mortgage yet" (the '
    'published "I would not ask that circle": his advice, not the reader\'s mood)',
    '"each others" -> "each other’s" (a typo, which isn\'t his kind of rough edge to copy, O27)',
    '"get to the point of dealing with conflict" -> "find out how much conflict the group can handle" (the published '
    '"Discover the group’s conflict capacity")']),
 'H1-P4': ('j01-emuA',
   "You’ll also want a budget of what the group can provide. This is the boring stuff! But you need to know what "
   "the group can offer in the way of water, housing, food stores, health care, tools, seasonal labor, transportation, access "
   "to markets, schooling, etc. Do you have outside debts to pay? How long will your cash reserves last? Which few skills "
   "would stop everything if nobody had them? A group that’s great on an emotional level can still be dead in the water if the "
   "well fails, or if the one person who knows where everything is and how it works is too exhausted to go on.",
   ['"a good idea of what you have in the way of resources" -> "a budget of what the group can provide" (the published '
    '"capacity budget", keys U11; v25\'s words, which readers didn\'t pause at)',
    '"What critical skills will you need?" -> "Which few skills would stop everything if nobody had them?" (the published '
    '"the few skills whose absence can stop everything")',
    '"great feelings for each other will not stop you from being dead in the water" -> "a group that’s great on an emotional '
    'level can still be dead in the water" (the published "extraordinary emotional skill and still die", keys U12)',
    '"collapses from exhaustion" -> "is too exhausted to go on" (the published "one exhausted person is the only one who '
    'knows")',
    'march r19 a read no break in it: "This is the boring stuff, but you need to know" -> "This is the boring stuff! But you '
    'need to know" (a reaction, the kind of break that held in every reading, "What section 13\'s Emulate rounds taught"), and '
    '"It’s boring, but a group" -> "A group" (one "boring", the published word: "Do the boring capacity budget too"; the '
    'linter\'s O12 and his rule keep one that says something)']),
 'H2-P2': ('j01-emuA',
   "Whenever you go to visit a community, have a list ready of what you really believe about children, money, property "
   "ownership, romance, medicine, food, spiritual practice, technology, privacy, how to deal with conflict, and leaving the "
   "community. Long list, huh? Put some question marks next to the things you’re not sure about yet.",
   ['"what you believe should be the community’s stance on" -> "what you really believe about" (the published "what you '
    'actually believe": the reader\'s beliefs, not the community\'s stance)',
    '", etc." out (the published list is closed)',
    '"It’s a long list, I know." -> "Long list, huh?" (v26\'s break, which both march readings and its trace passed; the '
    'section has two "I know"s already)',
    '"you aren’t sure about" -> "you’re not sure about" (keys U16)']),
 'H2-P3': ('j01-emuA',
   "You better put sexuality and gender on that list too. Can LGBTQ+ people live openly in the community? Can they date or be "
   "in relationships? Will the community keep them fully protected? Should children be taught to question their sexual "
   "identities at an early age? What will the community do if one of its children turns out to be gay or transgender? Until a "
   "group has answered those questions, its values on freedom and on raising children aren’t complete. Both of them!",
   ['"Will you protect them?" -> "Will the community keep them fully protected?" (the published "remain fully protected by '
    'the community", keys U18)',
    '"Is it okay to question a child’s sexuality at an early age?" -> "Should children be taught to question their sexual '
    'identities at an early age?" (Emulate made it adults questioning a child; the published is children taught to question '
    'their own identities)',
    '"What will you do if one of the community’s children" -> "What will the community do if one of its children"',
    '"Until you’ve answered those questions, your stance on freedom and children is incomplete." -> "Until a group has '
    'answered those questions, its values on freedom and on raising children aren’t complete. Both of them!" (the published '
    'is about the group; "Both of them!" is v26\'s break)',
    '"LGBTQ" -> "LGBTQ+" (the published term)']),
 'H2-P3b': ('j01-emuA',
   "Are you willing to experiment? That’s a real value too! Make sure your list declares whether or not you are. The people "
   "next to you may feel that all experimenting ended in 1978, and that whatever came out of it is doctrine now.",
   ['"That’s a real value too!" back (the published "“Willing to experiment” is a real value"; v26\'s break)',
    '"includes whether or not you are willing to experiment" -> "declares whether or not you are" (the published "It has to '
    'be declared", keys U20)',
    '"and everything since has been doctrine" -> "and that whatever came out of it is doctrine now" (the published "the '
    'results are now doctrine")']),
 'H2-P4': ('j01-emuB',
   "When you have this list well in hand, compare it to how the group you’re joining actually functions, not just its public "
   "face. How was a recent conflict handled? Who can block group decisions? How did leaving go for the last person who left? "
   "Who owns the land? It will be uncomfortable to talk about these things, but the view isn’t going anywhere.",
   ['call B, which keeps the four questions (call A dropped them; keys U22)',
    '"compare it to the actual functioning of the group you’re joining, not the group’s public face" -> "compare it to how '
    'the group you’re joining actually functions, not just its public face" (plain; the published "not only its public '
    'language")',
    '"How was recent conflict handled?" -> "How was a recent conflict handled?" (the published "a recent conflict")']),
 'H5-P1': ('j02-emuA',
   "A safe community can’t promise to keep everyone. There’s going to be times when someone has to go. Yeah, it’s tough. It’s "
   "also true. If someone is a serious or generalized danger to others, or keeps violating essential boundaries, or for "
   "whatever reason just makes living together impossible for everyone else, it can be the right call to eject them. If "
   "restorative work can help in a reasonable amount of time, all the better. But it’s not the community’s job to be a "
   "treatment program for someone who’s endangering everyone else.",
   ['the published first sentence back ("A safe community cannot promise to keep everyone")',
    '"dangerous (seriously or in a generalized sense)" -> "a serious or generalized danger to others" (the published words)',
    '"repeatedly breaks essential community rules" -> "keeps violating essential boundaries" (keys U55 "boundaries")',
    '"just can’t make it work with the rest of y’all" -> "just makes living together impossible for everyone else" (the '
    'published "makes ordinary shared life impossible", keys U55; "y’all" isn\'t his)',
    '"it’s appropriate to eject them ..., assuming restorative approaches either can’t be used or can’t work in a reasonable '
    'time" -> "it can be the right call to eject them. If restorative work can help in a reasonable amount of time, all the '
    'better." (the published "ejection can be the right answer" and "Restorative work is useful when it can work on a '
    'reasonable timescale", with no condition on ejection)',
    '"It’s not necessary or desirable for the entire community to act as that one person’s treatment program, especially if '
    'they’re endangering everyone." -> "But it’s not the community’s job to be a treatment program for someone who’s '
    'endangering everyone else." (call B\'s sentence: the published duty is about a person who endangers everyone else, not '
    '"especially if")']),
 'H5-P2': ('j02-emuA',
   "This power to remove people is so easily abused, though. " + JOEL_H5P2 + " What counts as cause for immediate protective "
   "action? Who decides to put temporary restrictions on someone? Who will make sure all the evidence is preserved? Who will "
   "recuse themselves? How will the person be able to reply to the concerns, and have the decision reviewed or appealed, "
   "without anyone being put in danger? What protections will there be for the person’s interests (housing, records, family "
   "contact, access to common resources, outside funds if any) while the separation is being worked out? When is it time to "
   "bring in outside help? (More on that next.)",
   ['"Because this power is so easily abused, though, it’s critical to discuss and decide in advance of any particular issue: '
    'what the process will be." -> "This power to remove people is so easily abused, though." and Joel\'s own sentence, as he '
    'wrote it (keys U57 "power to remove"; "This", not "The": a third paragraph opening on "The" fails B13)',
    '"Who will recuse themselves from a decision?" -> "Who will recuse themselves?"',
    '"reply to concerns and appeal a decision, without creating dangerous situations" -> "reply to the concerns, and have the '
    'decision reviewed or appealed, without anyone being put in danger" (the published "what review or appeal is possible '
    'without endangering others")',
    '"(housing, records, family contact, common resources, outside funds, etc.)" -> "(housing, records, family contact, access '
    'to common resources, outside funds if any)" (the published closed list and its "if any")',
    '"When is it appropriate to bring in outside help?" -> "When is it time to bring in outside help?"']),
 'H5-P3': ('j02-emuA',
   "‘Outside’ doesn’t always mean the nation-state. " + JOEL_H5P3 + " The basic need here is a competent layer of authority "
   "that isn’t reviewing its own conduct. That could be another community, a federation, a professional, an autonomous "
   "regional institution, a court, a regulator, an emergency service, etc. Just not whoever’s being reviewed! The "
   "Zapatistas are an important correction here: autonomous institutions can review local power without becoming the state, "
   "and when power crept up in their own system, they pushed it back down again. And no, autonomy still doesn’t let anyone "
   "erase non-waivable individual rights, or make outside jurisdiction disappear.",
   ['the first sentence is v26\'s, his published one; his linked sentence as he wrote it (OWNER-EDITS s13-joel-20261015-1828-32b) '
    'for Emulate\'s "though at first, when doing this research, that’s where it seemed to have to go"',
    '"a competent level of authority that is not reviewing its own actions" -> "a competent layer of authority that isn’t '
    'reviewing its own conduct" (his published "competent layer", which readers paused at, with Emulate\'s "authority" saying '
    'what it is)',
    '"federation of communities, professionals, ... emergency services, etc." -> the published singulars, Emulate\'s "etc." '
    '(the published "sometimes" makes the list examples)',
    '"The key is that it’s not the same people!" -> v26\'s "Just not whoever’s being reviewed!" (march r19: no break in '
    'reading b; v26\'s was a break in both of its readings)',
    'the Zapatista sentences: Emulate\'s ("it’s ok for that authority to be in a regional institution as long as it’s '
    'autonomous ... But when it tried to push power upwards") lost the published point; v26\'s sentence back, with Emulate\'s '
    '"again"',
    '"And no, it still can’t decide that individual people don’t have certain non-waivable rights." -> "And no, autonomy still '
    'doesn’t let anyone erase non-waivable individual rights, or make outside jurisdiction disappear." (the published two '
    'limits)']),
 'H5-P4': ('j02-emuA',
   "Also decide on a mediator or ombud in advance. Why bother? People often won’t trust someone they haven’t already met, who "
   "shows up in a crisis as a ‘neutral stranger’. Mediation is there to repair things between people. It doesn’t remove the "
   "need for evidence, safeguarding or a ruling, or for a final separation when people can’t or won’t consent to living "
   "together anymore.",
   ['"mediator/ombud person" -> "mediator or ombud" (the published words)',
    '"Why bother?" back (v26\'s break)',
    '"People won’t trust" -> "People often won’t trust" (the published "often do not trust")',
    '"who comes in as a "neutral stranger."" -> "who shows up in a crisis as a ‘neutral stranger’" (the published "until the '
    'day of the explosion")',
    'Emulate\'s order of the last three sentences changed back to the published one (what mediation is for, then what it '
    'doesn\'t replace), one sentence each']),
}
log, text = [], dict(zip(IDS, V26))
for pid, (k, new, fixes) in NEW.items():
    assert (k, pid) in src, (k, pid)
    log.append({'id': pid, 'emulate': 'emu-j/out/%s.txt' % k, 'emulate_text': src[(k, pid)], 'v26': text[pid], 'new': new,
                'fixes': fixes})
    text[pid] = new
assert JOEL_H5P2 in text['H5-P2'] and JOEL_H5P3 in text['H5-P3']
out = [V26[i] if pid is None else text[pid] for i, pid in enumerate(IDS)]
(HERE / 'v27.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v27-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for pid in NEW:
    print('%-7s %3d words (v26 %3d)' % (pid, len(text[pid].split()), len(dict(zip(IDS, V26))[pid].split())))
