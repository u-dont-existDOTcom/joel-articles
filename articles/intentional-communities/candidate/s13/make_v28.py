"""Section 13 draft v28 (2026-10-16): v27 with the sentences I had rebuilt from the published wording taken back to Emulate
round j's call A, and only the meaning they lost put in (b307/PREDICTIONS.md: H5-P3 with H5-P4, which carried the most
published wording, read 0.99 AI, and the section's AI windows ended on H1-P3's rebuilt first sentence and on H5-P4's last
three sentences, put back in the published order). Joel, 21:05 UTC: "34a and learn from how emulate fixes it". Each change
from Emulate's sentence is listed with its reason; a change that v27 made and v28 keeps says so.
Writes v28.md and v28-fixes.json. Run from this folder: python3 make_v28.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'emu-j' / 'out'
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
blocks = lambda md: [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]
V27 = blocks((HERE / 'v27.md').read_text(encoding='utf-8'))
assert len(V27) == len(IDS)
A1 = blocks((OUT / 'j01-emuA.txt').read_text(encoding='utf-8'))
A2 = blocks((OUT / 'j02-emuA.txt').read_text(encoding='utf-8'))
EMU = dict(zip(['H1-P3', 'H1-P4', 'heading', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'], A1))
EMU.update(dict(zip(['heading5', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4'], A2)))
JOEL_H5P3 = ('[My research](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) initially leaned too far '
             'that way.')
NEW = {
 'H1-P3': ("Until that’s happened, it’s still just a circle of promising strangers, and you don’t want to take out a mortgage "
           "with them yet. That’s okay! There’s lots you can do! You can all meet in a rented or borrowed space, or at each "
           "other’s houses, and find out how much conflict the group can handle before you need a surveyor.",
   ['"Until then" -> "Until that’s happened" (kept from v27: H1-P2 ends on "Until then, what’s it worth?")',
    '"just a group" -> "just a circle of promising strangers" (the published words, keys U7)',
    '"maybe you don’t want to take out a mortgage yet" -> "you don’t want to take out a mortgage with them yet" (the published '
    '"I would not ask that circle to take on a mortgage yet" is advice; "you don’t want to" says it in Emulate\'s voice. v27\'s '
    '"I wouldn’t ask that circle" rebuilt the published sentence, where the section\'s first AI window ended)',
    '"each others" -> "each other’s" (a typing slip, O27)',
    '"get to the point of dealing with conflict" -> "find out how much conflict the group can handle" (kept from v27: the '
    'published "Discover the group’s conflict capacity")']),
 'H1-P4': ("You will also want a budget of what you have in the way of resources. This is the boring stuff! But you will need "
           "to know what the group can offer in the way of water, housing, food stores, health care, tools, seasonal labor, "
           "transportation, access to markets, schooling, etc. Do you have outside debts to pay? How long will your cash "
           "reserves last? What critical skills will you need? Being great at the emotional stuff won’t stop you from being "
           "dead in the water if your well fails, or if the one person who knows where everything is and how it works gets "
           "too exhausted to keep going.",
   ['"a good idea of what you have" -> "a budget of what you have" (the published "capacity budget", keys U11)',
    '"This is the boring stuff, but you will need" -> "This is the boring stuff! But you will need" (kept from v27: the march '
    'found no break in Emulate\'s paragraph)',
    '"It’s boring, but great feelings for each other will not stop you" -> "Being great at the emotional stuff won’t stop you" '
    '(the published "extraordinary emotional skill": a skill, not affection, keys U12; one "boring", O12)',
    '"collapses from exhaustion" -> "gets too exhausted to keep going" (the published "one exhausted person", keys U12)',
    'Emulate\'s "What critical skills will you need?" back for v27\'s "Which few skills would stop everything if nobody had '
    'them?", which rebuilt the published "the few skills whose absence can stop everything" (the section\'s second AI '
    'window starts at these questions)']),
 'H2-P2': ("Whenever you go to visit a community, have a list ready of what you really believe about children, money, property "
           "ownership, romance, medicine, food, spiritual practice, technology, privacy, how to deal with conflict, leaving "
           "the community, etc. Long list, huh? Put some question marks next to the things you’re not sure about yet.",
   ['"what you believe should be the community’s stance on" -> "what you really believe about" (the published "what you '
    'actually believe": the reader\'s own beliefs)',
    '"It’s a long list, I know." -> "Long list, huh?" (kept from v27: v26\'s break; the section already has "I know, it’s the '
    'fun part.")',
    '"you aren’t sure" -> "you’re not sure" (keys U16)',
    'Emulate\'s ", etc." back (v27 had closed the list as published)']),
 'H2-P3': ("You better also include sexuality and gender on that list. Can LGBTQ+ people live openly in the community? Can they "
           "date or be in relationships? Will they be fully protected? Is it okay for children to be taught to question their "
           "sexuality at an early age? What will you do if one of the community’s children turns out to be gay or transgender? "
           "Until a group has answered those questions, its stance on freedom and raising children is incomplete. Both of them!",
   ['"LGBTQ" -> "LGBTQ+" (the published term)',
    '"Will you protect them?" -> "Will they be fully protected?" (the published "remain fully protected by the community": '
    'the community protects them, not the reader; keys U18)',
    '"Is it okay to question a child’s sexuality at an early age?" -> "Is it okay for children to be taught to question their '
    'sexuality at an early age?" (the published question is whether children are taught to question their own identities; '
    'Emulate\'s made it adults questioning a child\'s; keys U18)',
    '"Until you’ve answered those questions, your stance on freedom and children" -> "Until a group has answered those '
    'questions, its stance on freedom and raising children" (the published "A group that has not answered these has not '
    'completed its values on freedom or children"; keys U19 "raising children")',
    '"Both of them!" (v26\'s break, the march\'s only break in this paragraph)',
    'Emulate\'s own sentences back where v27 had rebuilt the published ones ("You better put ... too", "Will the community keep '
    'them fully protected?", "Should children be taught to question their sexual identities", "What will the community do", '
    '"its values on freedom and on raising children aren’t complete")']),
 'H2-P3b': ("Are you willing to experiment? That’s a real value too! Make sure your list of values declares whether or not you "
            "are willing to experiment. The people next to you may feel that all experimenting ended in 1978, and everything "
            "that came out of it has been doctrine ever since.",
   ['"That’s a real value too!" (the published "“Willing to experiment” is a real value"; v26\'s break)',
    '"includes whether or not" -> "declares whether or not" (the published "It has to be declared", keys U20)',
    '"and everything since has been doctrine" -> "and everything that came out of it has been doctrine ever since" (the '
    'published "the results are now doctrine": what came out of the experimenting, not everything after 1978)']),
 'H5-P3': ("Note that \"outside\" doesn't have to mean the nation-state. " + JOEL_H5P3 + " The basic need here is for a competent "
           "level of authority that is not reviewing its own conduct. That could mean another community, a federation of "
           "communities, professionals, autonomous regional institutions, courts, regulatory agencies, emergency services, etc. "
           "The key is that it's not the same people! An important correction that came from the Zapatistas: that authority "
           "can be an autonomous regional institution, without it turning into the state. But when power started creeping "
           "upward in their own system, they pushed it back down again. And no, autonomy still doesn't mean anyone gets to "
           "decide that individual people don't have certain non-waivable rights, or that outside jurisdiction just goes away.",
   ['Joel\'s sentence as he wrote it, link on "My research" (OWNER-EDITS s13-joel-20261015-1828-32b), for Emulate\'s "though at '
    'first, when doing this research, that\'s where it seemed to have to go"',
    '"nation state" -> "nation-state" (the published spelling)',
    '"its own actions" -> "its own conduct" (keys U61)',
    '"it\'s ok for that authority to be in a regional institution as long as it\'s autonomous, and doesn\'t combine its powers '
    'with the other institutions" -> "that authority can be an autonomous regional institution, without it turning into the '
    'state" (the published "autonomous institutions can review local power without becoming the state"; combining powers '
    'isn\'t in it; keys U62)',
    '"when it tried to push power upwards" -> "when power started creeping upward in their own system" (the published "when '
    'power drifted upward in their own system")',
    '"it still can\'t decide that individual people don\'t have certain non-waivable rights" -> "autonomy still doesn\'t mean '
    'anyone gets to decide that individual people don\'t have certain non-waivable rights, or that outside jurisdiction just '
    'goes away" (the published: autonomy lets no one erase those rights or make outside jurisdiction disappear)',
    'Emulate\'s own sentences back where v27 had the published ones ("‘Outside’ doesn’t always mean", "a competent layer of '
    'authority", the published singular list, "Just not whoever’s being reviewed!", v26\'s Zapatista sentence): the pair read '
    '0.99 AI in 307g']),
 'H5-P4': ("Also decide on a mediator or ombud in advance. Why bother? People often won't trust someone they haven't already "
           "met, who comes in during a crisis as a \"neutral stranger.\" This does not obviate the need for evidence, "
           "safeguarding, rulings, etc. Mediation is an attempt to restore good relations between people. When people can't or "
           "won't consent to being in community any more, it's time for a separation.",
   ['"mediator/ombud person" -> "mediator or ombud" (the published words, keys U64)',
    '"Why bother?" (v26\'s break, the march\'s only break in this paragraph)',
    '"People won\'t trust" -> "People often won\'t trust" (the published "often")',
    '"who comes in as" -> "who comes in during a crisis as" (the published "met on the day of the explosion")',
    '"Note that this does not obviate" -> "This does not obviate" (the paragraph before opens "Note that")',
    '"restore good human relations" -> "restore good relations between people" (keys U65)',
    '"they need to be separated" -> "it\'s time for a separation" (keys U65 "separation")',
    'Emulate\'s order of the last three sentences back: v27 had put them in the published order, and they were the section\'s '
    'last AI window (307g)']),
}
log, text = [], dict(zip(IDS, V27))
for pid, (new, fixes) in NEW.items():
    log.append({'id': pid, 'emulate': EMU[pid], 'v27': text[pid], 'new': new, 'fixes': fixes})
    text[pid] = new
assert JOEL_H5P3 in text['H5-P3'] and "So work out the process before it's about anyone in particular." in text['H5-P2']
out = [V27[i] if pid is None else text[pid] for i, pid in enumerate(IDS)]
(HERE / 'v28.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v28-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for pid in NEW:
    print('%-7s %3d words (v27 %3d)' % (pid, len(text[pid].split()), len(dict(zip(IDS, V27))[pid].split())))
