#!/usr/bin/env python3
"""fill_h79.py - the making-sense receipts of turn 71's texts of mine. The machinery and the field rules are fill_h78.py's
(imported, with HERE pointed at this folder); the entries below are this turn's:

- a3-b158-b155, a3-b156-b157: try 3 of the two zeolite pairs, each a small change from try 2 (the best near miss of its
  lineage, lesson bad-trips-2026-11-19b), with facts from his ZeoCharge post, which the section's heading links
  (https://ibogaqueen.substack.com/p/here-is-why-everyone-should-use-zeocharge, read 2026-11-26 23:35 UTC): "mix a spoon or
  2 of the zeolite into a (non-metal) cup of water of water or juice"; ZeoCharge "is billed as 'cleaned and remineralized'"
  and "likely all zeolites except ZeoCharge, since I don't see others that are cleaned"; "Zeolite binds metals, so don't
  put it into a metal thing or use a metal spoon."
- a1-b154 (with B153 before it in the reads): the ferments paragraph with his round-60 answer 2.1.

  python3 fill_h79.py a3-b158-b155 a3-b156-b157 a4-b158-b155 a4-b156-b157 a2-b154 a1-charcoal
"""
import importlib.util, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fill_h78', HERE.parent / 'h78-20261126' / 'fill_h78.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
M.HERE = HERE
POST = ('his ZeoCharge post (https://ibogaqueen.substack.com/p/here-is-why-everyone-should-use-zeocharge, linked on the '
        'section\'s heading; read 2026-11-26 23:35 UTC)')
READS_Z = ('the three fresh reads of the section as it stood (../h78-20261126/reads/*-asis-zeo-sec.txt) and the panels '
           '(../h78-20261126/panel-zeo-take, panel-zeo-ozone); his round-60 answer left 2.2 to 2.6 of ZEO-FACTS unanswered, '
           'and his ZeoCharge post answers two of them in a few words. ')

M.CFG.update({
    'a3-b158-b155': dict(M.CFG['a1-b158-b155'], readkey='asis-zeo-sec', note=READS_Z + (
        'Try 2 (86a0478d), the best near miss, read Human in every window but Low and Medium, so try 3 changes two things a '
        'reader could take two ways, 18 percent of its words by the ledger\'s count: "a spoonful" (the paragraph before gives the '
        'ferment by the spoonful, and no water is named) is "a spoonful of zeolite into a cup of water or juice", the cup and '
        'the juice from his post, with the dash aside after the act in brackets; and "haven\'t been cleaned" (a reader cannot '
        'tell which product to buy, and sober people feel little) has "but ZeoCharge is sold as cleaned", his post\'s fact, '
        'which the heading\'s link already points to. Everything else is try 2 word for word')),
    'a3-b156-b157': dict(M.CFG['a1-b156-b157'], readkey='asis-zeo-sec', note=READS_Z + (
        'Try 2 (07cec6fa), the best near miss, read AI High on the whole metal paragraph (55 words), so try 3 changes that '
        'paragraph only, 12 percent of its words: its second sentence takes his post\'s plain words ("Zeolite binds metals, so '
        'don\'t put it into a metal thing or use a metal spoon"), in place of "adsorbs metals (they stick to it)" and "sitting '
        'against a metal vessel or utensil before I swallow it", keeping "heavy-metal removal", a fidelity key (W047); and '
        '"for ozonation and storage" is "for ozonating and storing it". B156 is try 2 word for word')),
})
M.PAY.update({
    'I put a spoonful of zeolite': ('they know how he takes it: a spoonful in a cup of water or juice, sipped slowly, more or less by person', 'the zeolite, just named', 'I put a spoonful'),
    'Most zeolites have clogged': ('they know why many do nothing, and which one is sold already cleaned', 'the products that did nothing', 'Most zeolites'),
    'Zeolite binds metals': ('they know why: zeolite binds metals, so it goes in no metal thing and gets no metal spoon', 'keeping it from metal, just said', 'Zeolite binds metals'),
})
M.SRC['a3-b158-b155'] = [
    {'point': 'a spoonful of zeolite into a cup of water or juice, sipped slowly; a teaspoon for some and a tablespoon for others; rubbing it on the body or holding the jar',
     'found': 'his post as of 2026-11-03 (B158) and ' + POST + ': "mix a spoon or 2 of the zeolite into a (non-metal) cup of water of water or juice"',
     'still_needed': 'yes: they take it this way and do not mistake the zeolite for the ferment', 'fate': 'changed'},
    {'point': 'most zeolites have clogged pores because they have not been cleaned; ZeoCharge is sold as cleaned',
     'found': 'his post as of 2026-11-03 (B155) and ' + POST + ': ZeoCharge "is billed as \'cleaned and remineralized\'"; "likely all zeolites except ZeoCharge, since I don\'t see others that are cleaned"',
     'still_needed': 'yes: they buy ZeoCharge, or expect to prepare another zeolite', 'fate': 'changed'},
    M.SRC['a1-b158-b155'][1],
]
M.SRC['a3-b156-b157'] = [
    M.SRC['a1-b156-b157'][0],
    {'point': 'he keeps zeolite away from metal during preparation and uses glass for ozonating and storing it; zeolite binds metals, part of why it is used for heavy-metal removal, so no metal thing and no metal spoon',
     'found': 'his post as of 2026-11-03 (B157) and ' + POST + ': "Zeolite binds metals, so don\'t put it into a metal thing or use a metal spoon."',
     'still_needed': 'yes: they keep it in glass and off metal', 'fate': 'changed'},
]
M.UNNEEDED['a3-b158-b155'] = M.UNNEEDED['a1-b158-b155']



# ---- the second batch: try 4 of both zeolite pairs, the ferments paragraph with his answer 2.1, Activated Charcoal try 1
CREADER = ('somebody sitting with a friend whose trip has turned sick and toxic, with charcoal and zeolite on hand, deciding which '
           'to give')
FREADER = ('somebody about to take a psychedelic, or to sit with a friend who has, who wants a ferment ready for when the nausea '
           'comes and is deciding what to buy or make')
M.CFG.update({
    'a4-b158-b155': dict(M.CFG['a3-b158-b155'], note=READS_Z + (
        'Try 3 (361aa0fa) read Human in every window, Low 25, Low 38, Medium 18, Low 10, Medium 17, with a lower AI '
        'likelihood than try 2. Try 4 changes two Low windows, 17 percent of the words: "a toxic or gut-driven component" '
        '(the read against his fixes: vague) is "the trip is toxic or the gut is driving it"; and "Many products did nothing '
        'for me, and quality mattered enormously." (a label with nothing in it, its own Low window) joins the next sentence '
        'as its cause, "I think because most zeolites have clogged pores that haven\'t been cleaned", his post\'s hedge '
        '("likely all zeolites except ZeoCharge, since I don\'t see others that are cleaned")')),
    'a4-b156-b157': dict(M.CFG['a3-b156-b157'], note=READS_Z + (
        'Try 3 (9fafe36c) read Human: High 32 on B156\'s first two sentences, Low on the rest. Try 4 makes two small changes, '
        'measured by the ledger: the ten-minutes sentence gets his post\'s "this works regardless of how much zeolite I am '
        'ozonating" as "however much zeolite was in the water" (the fit read: the ten minutes seemed to depend on amounts '
        'not given); and the metal paragraph gives its reason first and ends on what he does, so the lead line "I also keep '
        'zeolite away from metal during preparation, so" goes (the read against his fixes: a don\'t before its reason, said '
        'again by the next sentence) and "whenever possible" is "whenever I can"')),
    'a2-b154': dict(
        section='ZeoCharge & Ferment', reader=FREADER,
        place='the second paragraph of ZeoCharge & Ferment (B154), after the paragraph that names zeolite and the ZHoly3O ferment',
        why='it tells the reader which ferment to use if they have no ZHoly3O ferment, which work and which don\'t, and how to use it',
        same='none: read the section from its heading to the next; which ferments work is said only here',
        readkey='a1-ferment-sec', note=(
            'his round-60 answer 2.1 (review/r60/ANSWERS-R60-20261126-2229.json), nearly word for word, in place of the '
            'post\'s "Many ferments help to different degrees, including kombucha, kimchi, and apple vinegar. I prefer fermented '
            'beet juice made with apple vinegar and salt."; the last two sentences are B154 as it read Human High (c293133e). '
            'Three fresh reads on the first draft (reads/*-a1-ferment-sec.txt). Changed from their marks: "various" is out '
            '(the next sentence names the ferments), "but kimchi and kombucha also helped" is "though", the weaker ones are '
            'one sentence with yogurts first, and "fermented beet" is his word, so "beet juice" is said twice, not three times '
            '(the linter\'s O30). Not changed: what else the ZHoly3O ferment holds (both readers asked; he did not say, so it '
            'is not said); "even" is his word; the last two sentences stay as they read High')),
    'a1-charcoal': dict(
        section='Activated Charcoal', reader=CREADER,
        place='the three paragraphs of Activated Charcoal (B160, B161, B162), after ZeoCharge & Ferment',
        why='it tells the reader what charcoal does that zeolite doesn\'t, when to give charcoal and when zeolite, and the caution about medicines',
        same=('his charcoal paragraph in Swallowed Too Much? (B127) says it can adsorb medication they need and links here; this '
              'section says what to do about it here (think twice, tell the medics) and how charcoal differs from zeolite'),
        readkey='asis-charcoal-sec', note=(
            'the three fresh reads and the panel on the section as it stood (reads/*-asis-charcoal-sec.txt, '
            'panel-charcoal/PANEL.md; both panel readers marked all seven sentences), and its check, AI High 91 in one window '
            '(73098017). Changed from their marks: "Sometimes that is exactly the point." is out (the needed read: S4 says '
            'it with the case); "adsorbs drugs" is "drugs bind to it too", his word in B127 ("what binds to it"); the trip '
            'effect and the choice are one sentence with "that\'s why"; "may be relevant" says which to give; the mirrored '
            '"When ..., ..." pair is two different shapes, the zeolite one with the act first (the linter\'s O65); "use it '
            'cautiously" is "think twice before giving it", his way with a hedged don\'t (lesson bad-trips-2026-11-07j); '
            '"tell the medics" says when ("if medics come"). Every fact stays')),
})
M.PAY.update({
    'Many products did nothing for me, I think': ('they know why many zeolites do nothing, and which one is sold already cleaned', 'the kind of zeolite he uses, just said', 'Many products'),
    'With a machine producing': ('they know how long he runs it, with what machine, and that the amount of zeolite does not change it', 'the ozonating, just described', 'With a machine'),
    'Zeolite binds metals': ('they know zeolite binds metals, so it goes in no metal thing and gets no metal spoon', 'the glass vessel of the paragraph before', 'Zeolite binds metals'),
    'I use glass for ozonating': ('they know to use glass for ozonating and storing it', 'no metal, just said', 'I use glass'),
    'The ZHoly3O ferment contains': ('they know they can make their own beet ferment or use another ferment if they have no ZHoly3O ferment', 'the ZHoly3O ferment, named in the paragraph before', 'The ZHoly3O ferment'),
    'I found fermented beet': ('they know which ferment worked best for him, and that kimchi and kombucha help too', 'other ferments, just said', 'I found fermented beet'),
    "Most yogurts weren't": ('they know not to count on yogurt, and that apple vinegar alone helps only a little', 'the ferments that helped, just named', 'Most yogurts'),
    'Activated charcoal helps with toxins': ('they know charcoal takes up the drug as well as gut toxins, so it can weaken the trip, and why it is not a swap for zeolite', "the section's heading", None),
    'That makes charcoal the one': ('they know when to give charcoal: to stop more of the drug being absorbed, or when the gut itself is toxic', 'drugs binding to charcoal, just said', 'That makes charcoal'),
    'I use [zeolite]': ('they know to give zeolite instead when the trip should go on and only the gut needs help', 'when to give charcoal, just said', 'instead'),
    'Medicines bind to charcoal too': ('they know charcoal can take up a medicine someone depends on, to think twice before giving it then, and to tell medics it was taken', 'drugs binding to charcoal, said at the start', 'Medicines bind to charcoal'),
})
M.SRC['a4-b158-b155'] = [
    M.SRC['a3-b158-b155'][0],
    {'point': 'most sober people don\'t feel much from zeolite; its effect is more obvious when a trip is toxic or gut-driven',
     'found': 'his post as of 2026-11-03 (B158); "a toxic or gut-driven component" said as what it is', 'still_needed': 'yes: they do not write zeolite off after trying it sober', 'fate': 'changed'},
    {'point': 'many products did nothing for him, he thinks because most zeolites have clogged pores that have not been cleaned; ZeoCharge is sold as cleaned',
     'found': 'his post as of 2026-11-03 (B155) and ' + POST + ': ZeoCharge "is billed as \'cleaned and remineralized\'"; "likely all zeolites except ZeoCharge, since I don\'t see others that are cleaned"; "quality mattered enormously" goes into the cause it stood for',
     'still_needed': 'yes: they buy ZeoCharge, or expect to prepare another zeolite', 'fate': 'changed'},
    M.SRC['a1-b158-b155'][1],
]
M.SRC['a4-b156-b157'] = [
    {'point': 'powder into water, an ozone-water purifier, a glass vessel because ozone destroys plastic; ozonating water, never inhaling ozone gas; about two grams of ozone per hour for ten minutes, however much zeolite is in the water; less time worked less well and more did not noticeably improve it',
     'found': 'his post as of 2026-11-03 (B156) and ' + POST + ': "put it in water and ozonate it for 20 minutes at 1000mg/hr (this works regardless of how much zeolite I am ozonating btw)", the same amount of ozone as ten minutes at two grams an hour',
     'still_needed': 'yes: they ozonate the powder in water, in glass, for ten minutes, whatever the amount, and never breathe the gas', 'fate': 'changed'},
    M.SRC['a3-b156-b157'][1],
]
M.SRC['a2-b154'] = [
    {'point': 'the ZHoly3O ferment contains more than just fermented beet juice; they can ferment their own beet juice or use other ferments; fermented beet was best so far, kimchi and kombucha also helped; most yogurts were not fermented enough to work; apple vinegar helped a little',
     'found': 'his round-60 answer 2.1 (review/r60/ANSWERS-R60-20261126-2229.json): "yes, although the Zholy3O ferment contains more than just the fermented beet juice. but they can ferment their own beet juice or even use various other ferments. i found fermented beet was best so far, but kimchi and kombucha also helped. most yogurts weren\'t fermented enough to work, and ACV helped a little."',
     'still_needed': 'yes: they make or buy a ferment that works and skip yogurt', 'fate': 'changed'},
    {'point': 'his fermented beet is made with apple vinegar and salt',
     'found': 'his post as of 2026-11-03 (B154: "I prefer fermented beet juice made with apple vinegar and salt")', 'still_needed': 'yes: they know what it is made with', 'fate': 'kept'},
    {'point': 'smelling the ferment helps a lot; a spoonful can help too, but may cause itching in someone who breaks down histamine poorly, which then needs activated charcoal',
     'found': 'his post as of 2026-11-03 (B154), as it read Human High (c293133e); unchanged', 'still_needed': 'yes: they smell it first and know what to do if a spoonful makes someone itch', 'fate': 'kept'},
]
M.SRC['a1-charcoal'] = [
    {'point': 'charcoal can help gut toxicity but adsorbs drugs; it can flatten or reduce a trip, so he does not treat charcoal and zeolite as interchangeable',
     'found': 'his post as of 2026-11-03 (B160); "adsorbs" said with his word in B127, "binds"', 'still_needed': 'yes: they do not give charcoal when the trip should go on', 'fate': 'changed'},
    {'point': 'charcoal when the goal is to reduce drug absorption or stop a toxic gut situation; zeolite to keep the trip while improving the gut feeling',
     'found': 'his post as of 2026-11-03 (B161)', 'still_needed': 'yes: they choose which of the two to give, and when', 'fate': 'changed'},
    {'point': 'charcoal can adsorb medications somebody depends on; use it cautiously around necessary medicines and tell the medics if charcoal was taken',
     'found': 'his post as of 2026-11-03 (B162); his own B127 says the same of medication', 'still_needed': 'yes: they hold back with someone on a needed medicine and tell the medics', 'fate': 'changed'},
]
M.UNNEEDED['a4-b158-b155'] = {k: v for k, v in M.UNNEEDED['a1-b158-b155'].items() if not k.startswith('Most zeolites')}
M.UNNEEDED['a1-charcoal'] = {}


# ---- the third batch: try 5 of both zeolite pairs, Activated Charcoal try 3
M.CFG.update({
    'a5-b158-b155': dict(M.CFG['a4-b158-b155'], note=READS_Z + (
        'Try 4 (bcff53e3) read Human Low 26 (the first sentence), High 24 (the dose sentence, High for the first time), Low 14 '
        '(the rubbing sentence) and Medium 43 (the second paragraph). Try 5 changes the two Low windows, 9 percent of the '
        'words: "its effect becomes more obvious when" ("more obvious" than what, the read against his fixes asked) is '
        '"when the trip is toxic or the gut is driving it, the effect is easy to feel", the case first and then what the '
        'reader notices; and "simply holding the jar" ("simply" is filler, and the read asked which jar) is "just holding '
        'its jar". The second paragraph waits for the next check')),
    'a5-b156-b157': dict(M.CFG['a4-b156-b157'], note=READS_Z + (
        'Try 4 (1ba42201) read Human High 58 and High 41, with one Medium window, 15 words: "Less time did not work as well, '
        'and more time did not noticeably improve it." Try 5 changes that sentence only, 4 percent of the words: "it" (the '
        'read against his fixes: the zeolite or the result?) is "the zeolite", and "did not" is "didn\'t" twice, as he '
        'writes it')),
    'a2-charcoal': dict(M.CFG['a1-charcoal'], note=(
        'Try 2 (de52656f), my first rewrite, read AI in every window: Medium 35, High 44 (the paragraph that says when to give '
        'which), Low 31. The panel and the reads on the section as it stood (reads/*-asis-charcoal-sec.txt, '
        'panel-charcoal/PANEL.md) marked a comparison built as a rule; try 2 kept that build in other words ("the one to give '
        'when the goal is to ..."). Try 3 says what he does first and gives cases a friend would recognize: "I don\'t treat '
        'charcoal and zeolite as interchangeable, because ..." (his practice first, the linter\'s O65); "if someone took too '
        'much, or the gut itself is toxic, I give charcoal" (the case, for "reduce drug absorption or stop a toxic gut '
        'situation"); "If the trip is going fine and only the gut feels bad, I give zeolite, which leaves the trip alone" (for '
        '"preserve the trip while improving the gut feeling"); the medics line said as his B127 says its cautions, to the '
        'reader. Every fact stays')),
})
M.PAY.update({
    "Most sober people don't feel much from zeolite, but when": ('they know not to judge zeolite sober: on a toxic or gut-driven trip the effect is easy to feel', 'the ferment paragraph before it, the other of the two remedies', None),
    'Rubbing the zeolite on the body or just': ('they know two more ways he uses it', 'taking it in water, just said', 'Rubbing the zeolite'),
    "Less time didn't work": ('they know ten minutes is the time to use', 'the ten minutes, just said', 'Less time'),
    "I don't treat charcoal and zeolite": ('they know charcoal and zeolite are not a swap: drugs bind to charcoal too, so it can flatten or reduce a trip', "the section's heading", None),
    'So if someone took too much': ('they know when to give charcoal: someone took too much, or the gut itself is toxic', 'charcoal flattening a trip, just said', 'So if someone took too much'),
    'If the trip is going fine': ('they know to give zeolite instead when the trip is fine and only the gut feels bad', 'when to give charcoal, just said', 'If the trip is going fine'),
    'Medicines bind to charcoal too, so': ('they know to think twice before giving charcoal to someone who depends on a medicine', 'drugs binding to charcoal, said at the start', 'Medicines bind to charcoal'),
    'If medics come': ('they know to tell medics charcoal was taken', 'charcoal and medicines, just said', 'If medics come'),
})
M.SRC['a5-b158-b155'] = M.SRC['a4-b158-b155']
M.SRC['a5-b156-b157'] = M.SRC['a4-b156-b157']
M.SRC['a2-charcoal'] = M.SRC['a1-charcoal']
M.UNNEEDED['a5-b158-b155'] = M.UNNEEDED['a4-b158-b155']
M.UNNEEDED['a2-charcoal'] = {}


# ---- the fourth batch: each zeolite paragraph by itself (B155 with B156 after it, as it is under 50 words), charcoal try 4
M.CFG.update({
    'a1-b158': dict(M.CFG['a5-b158-b155'],
        place='the third paragraph of ZeoCharge & Ferment (B158), checked by itself (64 words)',
        why='it tells the reader how he takes zeolite and not to judge it sober',
        note=READS_Z + (
        'B158 was checked with B155 because B155 was under 50 words; five tries of the pair took this paragraph from Low to '
        'Low and Medium, with its dose sentence reaching High in try 4. Each paragraph is the unit the guide is held to, so '
        'B158 (64 words, as in try 5 of the pair, b72967ee) is checked by itself, and B155 with B156, the paragraph its last '
        'sentence leads into')),
    'a1-b155-b156': dict(M.CFG['a5-b158-b155'],
        place='the fourth and fifth paragraphs of ZeoCharge & Ferment (B155, B156): which zeolite and how he ozonates it',
        why='it tells the reader which zeolite to buy, why many do nothing, and how he ozonates the others',
        note=READS_Z + (
        'B155 as in try 5 of B158 with B155, less its lead line "In my experiments, zeolite has to be prepared correctly." '
        '(the needed read: only a lead-in, which the next lines show; in try 5 it sat in a Low window with the rubbing '
        'sentence), and "rather than nano-liquid zeolite" is "not the nano-liquid kind" (the read against his fixes: a '
        '"Y rather than Z" contrast where he says what he uses). B156 is as it read Human High in try 5 of B156 with B157 '
        '(c6363909)')),
    'a3-charcoal': dict(M.CFG['a2-charcoal'], note=(
        'Try 3 (a4614eee) read Human High 82 with one Medium window of 8 words, the last sentence, "If medics come, tell them '
        'charcoal was taken." Try 4 joins it to the sentence before, 13 percent of the words, the way he joins a short '
        'sentence that carries one thought (his fixes, way 8): "..., and I\'d tell any medics who come that charcoal was '
        'taken." Everything else is try 3 word for word')),
})
M.PAY.update({
    'For my ozonated zeolite, I mix': ('they know how he prepares a zeolite that is not sold cleaned: powder in water, an ozone-water purifier, glass', 'the zeolites that have not been cleaned, just said', 'For my ozonated zeolite'),
    'I use powdered zeolite, not': ('they know to buy powder, not the nano-liquid kind', 'the paragraph before, how he takes zeolite', None),
    "Medicines bind to charcoal too, so I'd think twice before giving it to someone who depends on one, and": ('they know to think twice before giving charcoal to someone who depends on a medicine, and to tell medics it was taken', 'drugs binding to charcoal, said at the start', 'Medicines bind to charcoal'),
})
M.SRC['a1-b158'] = [M.SRC['a4-b158-b155'][0], M.SRC['a4-b158-b155'][1]]
M.SRC['a1-b155-b156'] = [M.SRC['a4-b158-b155'][2], M.SRC['a4-b158-b155'][3], M.SRC['a4-b156-b157'][0]]
M.SRC['a3-charcoal'] = M.SRC['a1-charcoal']
M.UNNEEDED['a1-b158'] = {k: v for k, v in M.UNNEEDED['a4-b158-b155'].items() if k.startswith('Its effect')}
M.UNNEEDED['a1-b155-b156'] = {}
M.UNNEEDED['a3-charcoal'] = {}


# ---- the fifth batch: B158 by itself (try 2), the pair's last try, B156 by itself
M.CFG.update({
    'a2-b158': dict(M.CFG['a1-b158'], note=READS_Z + (
        'Try 1 of B158 by itself (1e17485d) read Human High 51 with one Medium window, 14 words, the rubbing sentence. Try 2 '
        'changes that sentence only, 10 percent of the words: "on the body" is "on my body", "holding its jar" is "holding '
        'its jar in my hand" (his ZeoCharge post: "HOLD the zeolite in your hand"), and "also helps me" is "helps me too"')),
    'a6-b158-b155': dict(M.CFG['a5-b158-b155'], note=READS_Z + (
        'The pair\'s last try (6 of 6), from try 4 (bcff53e3), the best near miss, at 16 percent of its words: B158 as in try 2 '
        'of B158 by itself, and B155 less its lead line "In my experiments, zeolite has to be prepared correctly." (the needed '
        'read: only a lead-in; it sat in a Low window in try 5). B155 is under 50 words, so it is read with B158; its check '
        'with B156 after it read B156 Medium (7d31b545), where B156 with B157 had read High (c6363909)')),
    'a1-b156': dict(M.CFG['a5-b156-b157'],
        place='the fifth paragraph of ZeoCharge & Ferment (B156), checked by itself (66 words)',
        why='it tells the reader how he ozonates his zeolite, never breathing the gas, and for how long',
        note=READS_Z + (
        'B156 read Human High inside one 115-word window with B157 (c6363909) and Medium 74 with B155 before it (7d31b545). '
        'It is 66 words, so it is checked by itself, as in try 5 of B156 with B157, to see which reading holds')),
})
M.PAY.update({
    'Rubbing the zeolite on my body': ('they know two more ways he uses it', 'taking it in water, just said', 'Rubbing the zeolite'),
    "Many products did nothing for me, I think because most zeolites have clogged pores that": ('they know why many zeolites do nothing, and which one is sold already cleaned', 'the kind of zeolite he uses, just said', 'Many products'),
})
M.SRC['a2-b158'] = M.SRC['a1-b158']
M.SRC['a6-b158-b155'] = M.SRC['a4-b158-b155']
M.SRC['a1-b156'] = [M.SRC['a4-b156-b157'][0]]
M.UNNEEDED['a2-b158'] = M.UNNEEDED['a1-b158']
M.UNNEEDED['a6-b158-b155'] = {k: v for k, v in M.UNNEEDED['a4-b158-b155'].items() if not k.startswith('In my experiments')}


# ---- the sixth batch: B155 with B156, try 2
M.CFG['a2-b155-b156'] = dict(M.CFG['a1-b155-b156'], note=READS_Z + (
    'Try 1 (7d31b545) read Medium 9 on "I use powdered zeolite, not the nano-liquid kind.", High 25 on the next sentence and '
    'Medium 74 on B156, which reads High by itself (e36188fb). In the pair with B158, the post\'s words, "I use powdered '
    'zeolite rather than nano-liquid zeolite.", read High 9 (38bb7235). Try 2 puts those words back, 2 words, and changes '
    'nothing else'))
M.PAY['I use powdered zeolite rather than nano-liquid zeolite.'] = ('they know to buy powder, not the nano-liquid kind', 'the paragraph before, how he takes zeolite', None)
M.SRC['a2-b155-b156'] = M.SRC['a1-b155-b156']
M.UNNEEDED['a2-b155-b156'] = {}


# ---- the eighth batch: the section's short Medium sentences (b9d02255), joined where the ledger's limit allows
SEC = ('The section as it stands after this turn\'s paragraphs read Human in every window (b9d02255), High but for four short '
       'sentences that read Medium on their own: "Smelling the ferment helps a lot." (6), "I mean ozonating water, never '
       'inhaling ozone gas." (8), "Less time didn\'t work as well, and more time didn\'t noticeably improve the zeolite." (16) '
       'and "I use glass for ozonating and storing it whenever I can." (11). The read against his fixes had marked each: a '
       'short line he would join to its neighbour, or a mirrored pair. ')
M.CFG['a3-b154'] = dict(M.CFG['a2-b154'], note=SEC + 'Here the first joins the sentence after it, 9 percent of the words: '
    '"Smelling the ferment helps a lot, and drinking a spoonful can also help, although ..."')
M.CFG['a2-b156'] = dict(M.CFG['a1-b156'], note=SEC + 'Here, 19 percent of the words: the safety line joins the sentence before '
    'it, "..., and I mean ozonating water, never inhaling ozone gas" (fidelity key W046 kept), and the mirrored "more time" is '
    '"going past ten minutes". The glass line in B157 waits: its join measured 21 percent of the pair\'s words, over the '
    'ledger\'s limit after a near miss')
M.CFG['a6-b156-b157'] = dict(M.CFG['a5-b156-b157'], note=SEC + 'Here B156 as in try 2 of B156 by itself; B157 unchanged '
    '(12 percent of the pair\'s words)')
M.PAY['Smelling the ferment helps'] = ('they know to smell the ferment first, and that a spoonful helps too unless it makes someone itch, which then calls for activated charcoal', 'the ferments just ranked', 'Smelling the ferment')
M.PAY['For my ozonated zeolite, I mix'] = ('they know how he prepares it: powder in water, an ozone-water purifier, glass, and never breathing the gas', 'the zeolites that have not been cleaned, just said', 'For my ozonated zeolite')
M.SRC['a3-b154'] = M.SRC['a2-b154']
M.SRC['a2-b156'] = M.SRC['a1-b156']
M.SRC['a6-b156-b157'] = M.SRC['a5-b156-b157']


# ---- B155 with B156, try 3: B156 as in its try 2 by itself (99253002)
M.CFG['a3-b155-b156'] = dict(M.CFG['a2-b155-b156'], note=READS_Z + (
    'Try 2 (bf5f7b19) read High 58 on B155 and the first sentence of B156, Medium 8 on B156\'s short safety line, and High 42. '
    'B156\'s try 2 by itself (99253002, Human High 77) joins that line to the sentence before ("..., and I mean ozonating '
    'water, never inhaling ozone gas") and says "going past ten minutes" for the mirrored "more time"; try 3 is B155 as in '
    'try 2 with that B156'))
M.SRC['a3-b155-b156'] = M.SRC['a2-b155-b156']
M.UNNEEDED['a3-b155-b156'] = {}


if __name__ == '__main__':
    sys.exit(max(M.fill(k) for k in sys.argv[1:]))
