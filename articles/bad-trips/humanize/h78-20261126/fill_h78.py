#!/usr/bin/env python3
"""fill_h78.py - the making-sense receipts of turn 70's texts of mine, all from his round-59 answers (GUT-SIGNS 2.1 and 2.2;
review/r59/ANSWERS-R59-20261126-1555.json); the method and the fields are fill_h77.py's:

- a4-b141-signs, a5-b141-do: the gut-driven paragraph of My Acute Rescue Remedies (B141), now two paragraphs: the signs
  with what his two terms mean (2.1), then what to do, with his "address the gut first" (2.2) and his kept last line;
- a4-gutintro: the opening of Gut-Toxin & Die-Off Tools: B151 with "the come-up" explained and "more mysterious" given an
  example, and a new paragraph from his 2.2 answer (nausea and diarrhea are common; diarrhea can be a flushing out;
  severe diarrhea dries them out; binding the toxins and a lower dose).

  python3 fill_h78.py a4-b141-signs a5-b141-do a4-gutintro
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
HIS59 = 'his round-59 answer (review/r59/ANSWERS-R59-20261126-1555.json, GUT-SIGNS)'
READER = ('somebody sitting with a friend on a psychedelic who has diarrhea and nausea and says their mind is going crazy, '
          'deciding whether to talk them through it or to treat it')
READS_B141 = ('two rounds of fresh reads: on my first draft (reads/*-a1-rescue-sec.txt, panel-b141/PANEL.md) and on the third '
              '(reads/*-a3-rescue-sec.txt). Changed from their marks: the summing-up tag "basically everything related to '
              'controlling the body" is out; "themselves" has "someone"; each of his two terms is explained in the sentence that '
              'first uses it, with S10\'s run of signs split in two so the point still comes early; the examples of neurological '
              'disorganization that any strong trip brings (confusion, shaking, light and sound) are out, and the brain checks, '
              'which are the guide\'s own way to tell, are linked; what to do about loss of control names it and gives the list '
              'first; "If the gut is fine, obviously it\'s not related to the gut" is out (both reads: it tells the reader nothing, '
              'and a fine gut does not rule out the brain); "address the gut first" names the gut tools. Kept: his last line word '
              'for word (keep-as-is K2), "Those trips are what the remedies below are for ..." as it read Human High on '
              '2026-11-25 (8f7d99cd), and his "you don\'t need to try to tell which is from what", after the act it follows from (the linter\'s O65: the advice first)')
READS_GUT = ('two rounds of fresh reads: on my first draft (reads/*-a1-gut-sec.txt, panel-gut/PANEL.md) and on the second '
             '(reads/*-a2-gut-sec.txt). Changed from their marks: "These" is "The gut tools"; "the come-up" is explained where it '
             'is first used; "something more mysterious" has an example from two paragraphs up (a spiritual sign); "anyway" is '
             '"After all", tied to the reason before it; "Diarrhea is actually not as bad necessarily" is said as what is so, "Diarrhea can be a flushing out of toxins" (the linter\'s X1, his rule on "X does not Y"); the dehydration '
             'sentence names the act (the call-medics list, which says what badly dried out looks like) and has no "they"; '
             '"if you do things right" says what right is (the toxins get bound, a lower dose), in one sentence with the payoff first. '
             'Kept: his "a flushing out of toxins" and "once everything starts coming out in the toilet", which are two things '
             '(what it does, how it feels); "possible toxins", his frame for the whole section')
CFG = {
    'a4-b141-signs': dict(
        section='My Acute Rescue Remedies', reader=READER,
        place='the sixth paragraph of the opening of My Acute Rescue Remedies (B141), after R27-HIER, before the paragraph on what to do',
        why='it tells the reader which signs point to the gut or the brain, what his two terms mean, and that losing control of the body is a reason to call medics',
        same=('none new: read the section from its heading to the next. The call-medics list (B94) and the brain checks (R38-BRAIN-LIST) hold the same '
              'signs as tests; this paragraph points to both and does not repeat them'),
        readkey='a3-rescue-sec', note=READS_B141),
    'a5-b141-do': dict(
        section='My Acute Rescue Remedies', reader=READER,
        place='the last paragraph of the opening of My Acute Rescue Remedies (new block R59-GUT-DO, after B141), before Remedies Needing Caution',
        why='it tells the reader which part of the guide to use, and that with mental hell and gut hell together the gut comes first',
        same=('B151 says the gut tools are the first things he would use; this says the reader need not tell which hell is causing which, and links those tools. '
              'One point said from the reader\'s side here and from his practice there'),
        readkey='a3-rescue-sec', note=READS_B141),
    'a4-gutintro': dict(
        section='Gut-Toxin & Die-Off Tools',
        reader=('somebody about to take a psychedelic, or to sit with a friend who has, deciding whether to have a gut remedy ready '
                'and what to do when the nausea or diarrhea comes'),
        place='the opening of Gut-Toxin & Die-Off Tools: B151, then a new paragraph (R59-GUT-COMMON), before ZeoCharge & Ferment',
        why='it tells the reader why the gut tools come first, and what to make of nausea and diarrhea on a psychedelic',
        same=('B126 (Swallowed Too Much?) says vomiting and diarrhea help undo an overdose, up to a point; this is about an ordinary trip, and adds the relief, '
              'the drying out and the two ways to have less of it. B94 holds "Being badly dried out" with its signs; this links it'),
        readkey='a2-gut-sec', note=READS_GUT),
}
PAY = {
    'If a trip comes with diarrhea': ('they know which signs point to the gut or the brain as what is making the mind feel crazy', 'the body reasons the paragraphs before it give', None),
    'The same goes for loss of bodily control': ('they know what loss of bodily control looks like, and that neurological disorganization is his word for that and more', 'the signs just listed', 'The same goes for'),
    'Losing control of the body like that': ('they know to call medics when someone loses control of their body, and where the other brain signs are listed', 'the loss of control just described', 'Losing control of the body'),
    'Those trips are what the remedies': ('they know which part of the guide to use: the remedies below for those trips, the shadow work further down for a mainly emotional crisis', 'the trips with the signs in the paragraph before', None),
    "If you're in mental hell and gut hell": ('they know what to do when both are there: treat the gut first, with the gut tools', 'the two kinds of crisis just named', 'mental hell'),
    "You don't need to try to tell": ('they stop trying to work out which hell is causing which', 'treating the gut first, just said', "You don't need to"),
    'A gut-driven mental hell is often': ('they know the two get mixed up, which is why the gut comes first', 'addressing the gut first, just said', 'A gut-driven mental hell'),
    'The gut tools are the first things': ('they know to reach for the gut tools first, even before trouble, and why: rule out toxins before reading the distress as something mysterious', "the section's heading", None),
    'After all, nausea and diarrhea': ('they know gut trouble is common on psychedelics and drags the mind down, so the distress may be the gut', 'the reason just given for using the tools first', 'After all'),
    "Diarrhea can be a flushing out": ('they know diarrhea can be the body clearing itself and usually brings relief, so they need not fight it', 'the diarrhea just named', 'Diarrhea'),
    'But severe diarrhea can flush': ('they know the limit: severe diarrhea dries a person out, and badly dried out means calling medics', 'diarrhea not being bad, just said', 'But severe diarrhea'),
    "Still, you shouldn't have a lot": ('they know how to have less of it: bind the toxins in the gut with the tools below, and take a lower dose', 'gut trouble being common, just said', 'Still'),
}
SRC = {
    'a4-b141-signs': [
        {'point': 'the signs that point to the gut or the brain: diarrhea or nausea, a toxic heaviness or a dirty body-feeling, jaw tension, loss of bodily control, neurological disorganization',
         'found': 'his post as of 2026-11-03 and the paragraph as it read Human High on 2026-11-25 (8f7d99cd); every sign stays, in the same words and order, in two sentences',
         'still_needed': 'yes: they recognize the case by them', 'fate': 'kept'},
        {'point': 'loss of bodily control: wetting or soiling themselves, not being able to sit up, stand, walk or talk',
         'found': HIS59 + ' 2.1: "loss of bodily control includes urination, defecation, inability to sit up, stand, walk, talk, basically everything related to controlling the body"; "wetting or soiling themselves" is the guide\'s wording for it (B94, R38-BRAIN-LIST)',
         'still_needed': 'yes: they look for each of these in their friend', 'fate': 'changed'},
        {'point': 'neurological disorganization is a catch-all for that plus a whole lot more',
         'found': HIS59 + ' 2.1: "neurological disorganization is basically that plus a whole lot more it\'s a catch all term"; the list he pasted is a model\'s (GPT), and most of it is what any strong trip brings, so none of its items is in; the guide\'s own brain checks are linked for what to look for',
         'still_needed': 'yes: they stop looking for a separate test for the term and use the brain checks', 'fate': 'changed'},
        {'point': 'wetting or soiling themselves, not being able to walk normally and losing the ability to speak are on the call-medics list; the brain checks say what else to look for',
         'found': 'the guide, B94 (Call Medics For:) and R38-BRAIN-LIST with B104 and B106 ("if any of the checks above fail, call medics right away"), read 2026-11-26; his own lists, linked, nothing new claimed',
         'still_needed': 'yes: they call medics for someone who cannot talk or walk, and start the remedies meanwhile', 'fate': 'changed'},
    ],
    'a5-b141-do': [
        {'point': 'those trips are what the remedies below are for; the shadow work further down is for a mainly emotional crisis',
         'found': 'the paragraph as it read Human High on 2026-11-25 (8f7d99cd); unchanged', 'still_needed': 'yes: they choose between treating the body and working with the feeling', 'fate': 'kept'},
        {'point': 'in mental hell and gut hell at the same time, no need to tell which is from what: address the gut first',
         'found': HIS59 + ' 2.2: "if you\'re in mental hell and gut hell at the same time you don\'t need to try to tell which is from what, you address the gut first i think i mentioned that"; B151 says the gut tools are the first things he would use, so they are linked as the act',
         'still_needed': 'yes: they treat the gut first without working out which crisis it is', 'fate': 'changed'},
        {'point': 'if the gut is fine, obviously it is not related to the gut',
         'found': HIS59 + ' 2.2; left out: the needed read and the read against his fixes both found it tells the reader nothing, and a fine gut does not rule out the brain, which the paragraph before names',
         'still_needed': 'no', 'fate': 'cut'},
        {'point': 'a gut-driven mental hell is often mistaken as shadow work',
         'found': 'his own line, keep-as-is K2 (round 1, card RP-4); word for word, the last sentence', 'still_needed': 'yes: they check the gut before treating a mental hell as shadow work', 'fate': 'kept'},
    ],
    'a4-gutintro': [
        {'point': 'these are the first things he would use, even preventively on the come-up, to address possible toxins before assigning the distress to something more mysterious',
         'found': 'his post as of 2026-11-03 (B151 as it stood); "These" is "The gut tools", "the come-up" is explained once, "assigning the distress to" is "put the distress down to", and "something more mysterious" has an example from B86 two paragraphs up (a spiritual sign)',
         'still_needed': 'yes: they reach for the gut tools first, before trouble too', 'fate': 'changed'},
        {'point': 'nausea and diarrhea are common on psychedelics, and people generally do not feel good mentally during the nausea and gut pain parts of the come-up',
         'found': HIS59 + ' 2.2, his words', 'still_needed': 'yes: they suspect the gut when the mind feels bad on the come-up', 'fate': 'changed'},
        {'point': 'diarrhea is not necessarily bad: it can be a flushing out of toxins, and there is usually a lot of relief once everything starts coming out in the toilet; severe diarrhea can flush out too much fluid and cause dehydration',
         'found': HIS59 + ' 2.2, his words; "being badly dried out" and what it looks like are the call-medics list\'s (B94), linked',
         'still_needed': 'yes: they let ordinary diarrhea run and call medics when it dries the person out', 'fate': 'changed'},
        {'point': 'they should not have a lot of gut discomfort if they do things right: ideally bind the toxins in the gut to avoid too much nausea or diarrhea; dosing lower on the psychedelic can help too',
         'found': HIS59 + ' 2.2, his words; "do things right" is said as the two things he names', 'still_needed': 'yes: they bind the toxins with the tools below, and take less next time', 'fate': 'changed'},
    ],
}


def first(s):
    for k in PAY:
        if s.startswith(k):
            return k
    return None


def fill(key):
    c = CFG[key]
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
                        '--section', c['section'], '--reader', c['reader']], capture_output=True, text=True)
    if r.returncode:
        print(key, 'make:', (r.stdout + r.stderr)[-600:]); return 1
    d = json.loads(out.read_text(encoding='utf-8'))
    for s in d['sentences']:
        k = first(s['s'])
        if not k:
            print(key, 'no PAY for:', s['s'][:80]); return 1
        pay, fol, link = PAY[k]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link
    d['checked'] = SRC[key]
    d['placement'] = c['place']
    d['opens']['why_reading'] = c['why']
    d['same_point'] = c['same']
    who = 'a fresh agent (Sonnet) given tools/humanization/%s (reads/%s-' + c['readkey'] + '.txt and the round before it); the checked text answers its marks'
    d['needed'] = {'reader': who % ('needed_read_brief.md', 'need'), 'unneeded': [], 'kept': {}}
    d['his_fixes'] = {'reader': who % ('his_fixes_brief.md', 'his'), 'marked': [], 'kept': {}}
    d['fit'] = {'reader': who % ('fit_read_brief.md', 'fit'), 'marked': [], 'kept': {}}
    q = 'PASS: ' + c['note']
    d['questions'] = {k: q for k in d['questions']}
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1500:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode




# ---- the zeolite paragraphs (ZeoCharge & Ferment), added after the answers were in: first tries from the reads of the
# section as it stands (reads/*-asis-zeo-sec.txt) and the three panels
ZREADER = ('somebody about to take a psychedelic, or to sit with a friend who has, who wants a gut remedy ready and is deciding '
           'what to buy or make and how to give it when the nausea comes')
ZPOST = 'his post as of 2026-11-03 (original.md), the paragraph as it stands in the guide'
ZNOTE = ('the three fresh reads of the section as it stands (reads/*-asis-zeo-sec.txt) and the panels (panel-b153, panel-zeo-take, '
         'panel-zeo-ozone). ')
CFG.update({
    'a1-b153-b154': dict(
        section='ZeoCharge & Ferment', reader=ZREADER,
        place='the first two paragraphs of ZeoCharge & Ferment (B153, then B154 as it stands, which read Human High by itself: c293133e)',
        why='it tells the reader when he reaches for zeolite and the ferment',
        same=('B141 lists the same gut signs for the whole remedies section; here they say when these two remedies are his first thought, '
              'in one clause, and parasite die-off is named only here'),
        readkey='asis-zeo-sec',
        note=ZNOTE + ('B153 read AI High together with B151 (fc82fa68); the read against his fixes and both panel readers marked its run of '
                      'seven category phrases. Changed: the two remedies come first, the signs are one picture (a sick stomach, with nausea '
                      'or diarrhea and the toxic, dirty feeling) and one more (mental hell driven by gut hell), and parasite die-off has its '
                      'own short sentence. Every sign stays. B154 is unchanged')),
    'a1-b158-b155': dict(
        section='ZeoCharge & Ferment', reader=ZREADER,
        place='the third and fourth paragraphs of ZeoCharge & Ferment (B158, B155)',
        why='it tells the reader how he takes zeolite, and that which zeolite it is matters',
        same='none: read the section from its heading to the next; the amounts and the kind of zeolite are said only here',
        readkey='asis-zeo-sec',
        note=ZNOTE + ('As they stand the two read Human in every window but none High (Low 9, Low 15, Low 30, Medium 18, Low 21; 25652097), '
                      'so only two small things change in this try (lesson bad-trips-2026-11-19b; the ledger refused a first version that '
                      'changed four): the two short sentences about sober people are joined with "but", and "it" is "the zeolite". What the '
                      'reads asked that the section does not hold (how much water, wet or dry on the body, how to tell a good zeolite, what '
                      '"cleaned" means) is his to give: round 60, ZEO-FACTS')),
    'a1-b156-b157': dict(
        section='ZeoCharge & Ferment', reader=ZREADER,
        place='the last two paragraphs of ZeoCharge & Ferment (B156, B157)',
        why='it tells the reader how he ozonates his zeolite and why he keeps it in glass',
        same='none: read the section from its heading to the next for the ozonating and the metal; glass is named for the ozone (plastic) in B156 and for the metal in B157, two reasons',
        readkey='asis-zeo-sec',
        note=ZNOTE + ('As they stand: Human Medium 32, then AI Low 19, AI Medium 24, AI High 30, AI Medium 9 (859d5bdf). A try with a Human '
                      'window is fixed in small steps, so this one changes only the last paragraph, where the AI High window is: the do '
                      '(glass) is joined to the don\'t it follows from, "adsorbs" is explained, and "before ingestion" is "before I swallow '
                      'it". B156 is unchanged in this try; its two AI windows are the next check')),
})
PAY.update({
    'Zeolite and the [ZHoly3O]': ('they know when to reach for zeolite and the ferment: a sick stomach on a trip, or a mental hell that the gut is driving', "the section's heading, which names the two", None),
    "I'd think of them for parasite": ('they know he uses the same two for parasite die-off', 'the two remedies, just named', "I'd think of them"),
    'Many ferments help to different': ('they know other ferments will do if they lack his', 'the ferment, just named', 'Many ferments'),
    'I prefer fermented beet juice': ('they know which ferment he makes', 'the ferments just listed', 'I prefer fermented'),
    'Smelling the ferment helps': ('they know the easiest way to use it', 'the ferment he prefers', 'Smelling the ferment'),
    'Drinking a spoonful can also': ('they know a spoonful by mouth helps too, and what to do if it makes someone itch', 'smelling it, just said', 'Drinking a spoonful'),
    "Most sober people don't feel": ('they know not to judge zeolite by trying it sober: it shows during a trip with gut trouble', 'the ferment paragraph before it, the other of the two remedies', None),
    'I put a spoonful into water': ('they know how he takes it, and that the amount differs by person', 'the zeolite, just named', 'I put a spoonful'),
    'Rubbing the zeolite on the body': ('they know two more ways he uses it', 'taking it in water, just said', 'Rubbing the zeolite'),
    'In my experiments, zeolite has': ('they know the kind of zeolite and how it is prepared matter', 'the zeolite he takes, just described', 'In my experiments, zeolite'),
    'I use powdered zeolite rather': ('they know to buy powder, not the nano-liquid kind', 'preparing it correctly, just said', 'I use powdered zeolite'),
    'Many products did nothing': ('they know a zeolite off the shelf may do nothing', 'the kind he uses, just said', 'Many products'),
    'Most zeolites have clogged': ('they know why many do nothing, which is what his preparation is for', 'the products that did nothing', 'Most zeolites'),
    'For my ozonated zeolite, I mix': ('they know how he prepares it: powder in water, an ozone-water purifier, glass', 'the section on zeolite before it', None),
    'I mean ozonating water': ('they know never to breathe the ozone', 'the ozone purifier, just named', 'I mean ozonating'),
    'With a machine producing': ('they know how long he runs it', 'the ozonating, just described', 'With a machine'),
    'Less time did not work': ('they know ten minutes is the time to use', 'the ten minutes, just said', 'Less time'),
    'I also keep zeolite away from metal': ('they know to keep it off metal, and to use glass for ozonating and storing it', 'the glass vessel of the paragraph before', 'I also keep zeolite'),
    'Zeolite adsorbs metals': ('they know why: metals stick to zeolite, so it should not sit against metal before it is swallowed', 'keeping it from metal, just said', 'Zeolite adsorbs metals'),
})
SRC.update({
    'a1-b153-b154': [
        {'point': 'zeolite and the ZHoly3O ferment are often his first thoughts when the trip feels like sick stomach, nausea, diarrhea, toxic heaviness, a dirty body-feeling, parasite die-off, or mental hell driven by gut hell',
         'found': ZPOST + '; every sign stays; the remedies come first and the run of seven is one picture, a second, and a short sentence for parasite die-off',
         'still_needed': 'yes: they reach for these two when the trip feels like that', 'fate': 'changed'},
        {'point': 'other ferments help; he prefers fermented beet juice with apple vinegar and salt; smelling it helps, a spoonful too, with itching and charcoal for someone who breaks down histamine poorly',
         'found': ZPOST + ' (B154); unchanged, Human High 56 by itself (c293133e)', 'still_needed': 'yes: they know which ferment to use and how', 'fate': 'kept'},
    ],
    'a1-b158-b155': [
        {'point': 'most sober people do not feel much from zeolite; its effect is more obvious when a trip has a toxic or gut-driven component; a spoonful in water, sipped slowly, a teaspoon for some and a tablespoon for others; rubbing it on the body or holding the jar also helps him',
         'found': ZPOST + ' (B158); every fact stays, two sentences joined and "it" named', 'still_needed': 'yes: they take it this way and do not write it off after trying it sober', 'fate': 'changed'},
        {'point': 'zeolite has to be prepared correctly; he uses powdered zeolite, not nano-liquid; many products did nothing for him and quality mattered enormously; most zeolites have clogged pores because they have not been cleaned',
         'found': ZPOST + ' (B155); unchanged in this try', 'still_needed': 'yes: they buy powder and expect to prepare it', 'fate': 'kept'},
    ],
    'a1-b156-b157': [
        {'point': 'he mixes the powder into water and uses an ozone-water purifier in a glass vessel because ozone destroys plastic; ozonating water, never inhaling ozone gas; about two grams of ozone per hour for ten minutes; less time worked less well and more did not noticeably improve it',
         'found': ZPOST + ' (B156); unchanged in this try', 'still_needed': 'yes: they ozonate the powder in water, in glass, for ten minutes, and never breathe the gas', 'fate': 'kept'},
        {'point': 'he keeps zeolite away from metal during preparation; zeolite adsorbs metals, part of why it is used for heavy-metal removal; no metal vessel or utensil before ingestion; glass for ozonation and storage whenever possible',
         'found': ZPOST + ' (B157); every fact stays; glass is joined to the metal it answers, "adsorbs" is explained, "before ingestion" is "before I swallow it"',
         'still_needed': 'yes: they keep it in glass and off metal', 'fate': 'changed'},
    ],
})
UNNEEDED = {
    'a1-b158-b155': {
        'Its effect becomes more obvious when a trip has a toxic or gut-driven component.': 'now the second half of the sentence about sober people: they expect to feel it during a trip with gut trouble, and do not write it off after trying it sober',
        'In my experiments, zeolite has to be prepared correctly.': 'they read what follows as what makes a zeolite work, not as fuss; it turns the paragraph from taking zeolite to preparing it',
        "Most zeolites have clogged pores because they haven't been cleaned.": 'they understand why a product off the shelf may do nothing, and that his preparation is what cleans it (what "cleaned" means is his to say: round 60, ZEO-FACTS)',
    },
}
_fill0 = fill


def fill(key):  # the same, with the needed read's list where a sentence it could lose is kept with what the reader does with it
    rc = _fill0(key)
    if key in UNNEEDED:
        out = HERE / ('TEST-%s.receipt.json' % key)
        d = json.loads(out.read_text(encoding='utf-8'))
        d['needed']['unneeded'] = list(UNNEEDED[key]); d['needed']['kept'] = UNNEEDED[key]
        out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check',
                            str(HERE / ('TEST-%s.txt' % key)), str(out)], capture_output=True, text=True)
        res = (r.stdout + r.stderr).strip()
        print(key, 'receipt check with the kept sentences:', res[-900:] if r.returncode else res.splitlines()[-1][:120])
        rc = r.returncode
    return rc


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in sys.argv[1:]))
