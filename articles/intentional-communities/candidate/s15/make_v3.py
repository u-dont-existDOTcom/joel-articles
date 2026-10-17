"""Section 15 draft v3 (2026-10-17): v2 with the stretches that read AI in batch 322g rewritten from Emulate round b
(emu-b/out/, byte for byte from the laptop, sha256 checked: t01 H1-P4, t02 the paradise subsection, t03 the Black Tax
subsection, each sent whole, calls A and B), the published meaning put back inside Emulate's sentences (the 2026-10-16 21:05
lesson), paragraph by paragraph from whichever call kept more of it. The paragraphs that read Human alone in 322g and sit
outside an AI window stay as v2 has them: H1-P1 to H1-P3, H1-P5, H2-P5 (the moringa pods, published), H3-P6 and H3-P8.
Emulate's slips are not carried over: its reply framing ("You remind me of", "You're absolutely right", "Hi again",
"commies"), "our sheep" (the published sheep thief is anybody's), "occasional mob actions" (the published mob violence is
part of the existing reality, not occasional), "consensual" in quotation marks, "I have no idea who" (everybody knows),
the misspelt "it's" for "its". Joel's rule on "and ... and" chains (2026-10-07) and his list rulings apply; the linter's
landings (B7/B13) and two lists of three (E125) are checked by make_batch. Writes v3.md and v3-fixes.json.
Run from this folder: python3 make_v3.py"""
import hashlib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'emu-b' / 'out'
SHA = {'t01-emuA': '138881e3', 't01-emuB': 'f7a66ec4', 't02-emuA': '7a398e17', 't02-emuB': '2bd6a184', 't03-emuA': 'a27f5ac6',
       't03-emuB': 'e43d8b60'}
for k, h in SHA.items():
    assert hashlib.sha256((OUT / (k + '.txt')).read_bytes()).hexdigest().startswith(h), k
v2 = (HERE / 'v2.md').read_text(encoding='utf-8')
bl = [b.strip() for b in re.split(r'\n\s*\n', v2) if b.strip()]
LAW = '[Law No. 2026-08](https://www.humandignitytrust.org/resources/law-no-2026-08-of-march-27-2026-amending-article-319-of-law-no-65-60-of-july-21-1965/)'
assert LAW in v2
NEW = {
 'H1-P4': ("In the villages and families I've spent time around, a lot of the things we think we have to \"re-invent\" to form "
           "intentional communities are simply the way things are done. Nobody's holding a workshop called \"Rebuilding "
           "Intergenerational Belonging,\" because some aunt already gave three people a task. Land, childcare, housing, food, "
           "obligations, etc. etc. all get taken care of by the extended family and local memory, in addition to whatever formal "
           "systems there might be.", 'b t01 B',
           'B\'s "the things we think we have to "re-invent" ... are simply the way things are done" and its run-on list with "etc. '
           'etc."; the published "villages and families I\'ve spent time around" (B: "most villages and most families", a claim '
           'about the country), "childcare" (B: "kids") and "local memory" (B: "the people who are there in memory"); the '
           'workshop and the aunt, which both calls dropped, go back in the middle so the paragraph doesn\'t land on a short line'),
 'H2-P1': ("But does this mean I think Sénégal is some magical place that's kept its communal paradise? No! The warmth has hard "
           "limits, and for LGBTQ+ people who cross them, it can be brutal.", 'b t02 B',
           'B\'s question and its "No!"; the warmth\'s hard limits and the brutality for LGBTQ+ people who cross them go back '
           '(both calls dropped them)'),
 'H2-P2': (("Sénégal passed a law in March 2026 (" + LAW + ") that increased the penalty for consensual same-sex intimacy to 5 to "
           "10 years in prison, and it also made public \"apology\" for homosexuality a crime, along with certain financing or "
           "support meant to promote it. Homosexuals were already facing arrests, family rejection, harassment, assault and mob "
           "violence, but some say they're actually protected once they're arrested, because then at least the mob can't get at "
           "them. I can't just praise the virtues of community and ignore the people who have to hide who they are to survive "
           "in it, or leave."), 'b t02 B',
          'B\'s two long sentences; the published "public" apology, "meant to promote it" (B: "for promoting homosexuality"), the '
          'list of what was already happening with its "harassment" and "family rejection", "protected" (B: "safer"), "praise" '
          '(B: "extol the virtues"; "I don\'t want to" opening a stance is the linter\'s O20) and "leave" (B: "flee from them")'),
 'H2-P3': (("So which is it? Well, in a way, it's both. It's possible for a society to be incredibly spiritually alive, "
           "generous, funny and super communal, while at the same time being extremely cruel to those who break its social categories. It's interesting to "
           "see that being in community isn't necessarily liberating for everyone, it depends on whether you're allowed to "
           "belong without pretending."),
          'b t02 A and B', 'A\'s "So, in a way, it\'s both." and its "It\'s interesting to see that being in community is not '
          'necessarily a way of liberation for everyone", B\'s middle sentence; the published point that it depends on who may '
          'belong without pretending goes inside A\'s last sentence; the break is a question before A\'s "it\'s both" (march r3: reading a found none) (B\'s "may or may not" and "you can" are the linter\'s coach phrases, E41; the published "permitted" is "allowed")'),
 'H2-P4': (("One other shadow side of the forgiving social culture here is that people will go to pretty funny lengths to avoid "
           "confrontation. Who stole the sheep? We all know, but nobody wants to cause a stink by bringing it up."), 'b t02 A',
          'A\'s sentences; the sheep thief is anybody\'s (A: "our sheep"), and A\'s "relatively" forgiving culture is the '
          'published "forgiving" one'),
 'H2-P6': (("Everybody here has sheep (even me!), and they are super cute! It can feel like you're living in another world, with "
           "the music, the animals, the joking, the praying, and just being around people all the time."), 'b t02 B',
          'B\'s sentences with the published "another world" (B: "a different world") and "Everybody" (B: "Almost everyone"); '
          'inside the subsection v2\'s second sentence began the 75-word AI window'),
 'H2-P7': (("Of course, the old ways here are changing. Young people want to move to the city, get a job, get a phone, eat imported "
           "food, be part of the wider world, etc. (some young men even make the dangerous journey by sea to Europe). And can "
           "you blame them? Families that used to share almost everything are now more reliant on cash and individual "
           "opportunities."), 'b t02 A',
          'A\'s sentences, with B\'s "dangerous journey by sea" (A: "risk their lives by trying to sail") and the published '
          'families that once shared nearly everything (A: "as families become less reliant on each other")'),
 'H3-P1': (("Then there's the so-called \"Black Tax,\" a legacy of the old communal system: if you've got any money at all, you're "
           "expected to share it with your parents, your siblings, to pay school fees, medical bills, funerals, etc. I understand "
           "the instinct. In the ancestral way of doing things nobody made it alone, and the people who fed and raised you had a "
           "real claim on whatever you made of yourself later. So why not share in return? It was the most natural thing to do, "
           "and that's how the whole organism survived (nobody thought of it as charity)."), 'b t03 A and B',
          'A\'s first sentence and its run-on list (without "You remind me of"), B\'s "Why not share in return" and its comma '
          'splice; the published instinct, "nobody succeeded alone", the real claim, and "not charity"; of the four who fed, '
          'raised, housed and protected you two stay, so the paragraph has one list of three (E125)'),
 'H3-P2': (("The problem is that it can be very soul destroying in today's world. The obligation is still there, but most people "
           "no longer live close enough to share land, work, childcare, food etc. and feel part of a larger whole, while whoever "
           "earns the cash can still be expected to carry everybody. So it's hard for them to become independent or build any "
           "long-term stability. How are they supposed to get ahead? And yet the relatives stay dependent, because the payments "
           "don't give them a real alternative. So the ancestral ethic carries on inside the individualistic cash economy, "
           "keeping people alive but gnawing at both sides."), 'b t03 A',
          'A\'s sentences; the published obligation that survived the communal life holding it up, the earner expected to carry '
          'everybody, "dependent" (A: "a position of continued dependency"), the payments that don\'t create an alternative, and '
          '"both sides" (A: "gnawing at them")'),
 'H3-P3': (("It's also one of the thorny boundary issues of living without money inside a money-based society. Life inside the "
           "commune can go without cash, but you'll still need money for taxes, hospital bills, visas, school fees, family "
           "obligations, buying in tools etc. That doesn't mean going back to individuals working for wages and bringing them "
           "into the commune, but it does mean someone has to handle it! Who's that going to be? And the commune has to work "
           "out how much shared cash it "
           "keeps for these things, and how to stop access to outside money from creating a new status hierarchy."), 'b t03 A',
          'A\'s sentences; the published cashless inside, "family obligations" (A: "\'Black Tax\'"), who handles it (A: "someone '
          'has to do it!"), the shared cash and the status hierarchy that outside money can create; the break is the question "Who\'s that going to be?" (march r3: no break in either reading)'),
 'H3-P4': (("Another aspect of outside work is that it's not just money you're bringing into the commune. You're also bringing in a "
           "different schedule, a different status system, a different social world, different loyalties, different consumption "
           "habits etc. etc. And you can't exactly leave all that at the door, can you? In the first stage, where some people "
           "work outside and contribute an agreed share, it's really important that they can't use the money to buy their way "
           "out of communal work, or to buy a greater say in the political system. It's also important that outside jobs don't "
           "drain the energy and skills out of the people who could be building the communal livelihoods. Otherwise the commune "
           "will never develop a common purse, and it will stay a dormitory for the money economy."), 'b t03 A',
          'A\'s sentences; "schedule" (A: "a different way of organizing your time"), "a different status system" (A: "different '
          'status differences"), "agreed share", "drain"; the break is a tag question that claims nothing new (A had none)'),
 'H3-P5': (("Some Zapatista communities used to try to stop their young people from emigrating, which is a version of the same "
           "problem. Now they talk it through with them instead: it's OK to go and work elsewhere, as long as the migrants keep "
           "certain defined obligations to the community. That doesn't make the pull between leaving and belonging go away, but "
           "at least now it's something they can name and negotiate. I like that."), 'b t03 A',
          'A\'s sentences and its "I like that."; the published version of the same problem, the defined obligations, and the '
          'conflict that stays but can be named and negotiated (A dropped it)'),
 'H3-P7': (("So this is a global issue, far from some Western lifestyle niche. There's knowledge in the living villages that no "
           "book can give you. And by the way, if you visit, remember they're people, not museums. Would you like people coming "
           "to your house to stare at you and your family? So be respectful, go wanting to contribute, learn some of the "
           "language, and don't expect anyone to hand you a spiritual service package!"), 'b t03 B',
          'B\'s sentences; the published niche, the knowledge no book reproduces, "the living villages" and the "spiritual service '
          'package"; B\'s "they are living and working there, they are not there to entertain you" goes (the linter\'s O9, a '
          '"not Y" tail), as does "as you can see" (E41) and the second "and" in B\'s question (O14)'),
}
SKIP = re.compile(r'^(#|\[image \d+\]|\[caption\]|\[Professor Baby Sheep|Double click to interact with video)')
IDS = ['H1-P%d' % i for i in range(1, 6)] + ['H2-P%d' % i for i in range(1, 8)] + ['H3-P%d' % i for i in range(1, 9)]
prose = [b for b in bl if not SKIP.match(b)]
assert len(prose) == len(IDS)
OLD = dict(zip(IDS, prose))
out, log = [], []
it = iter(IDS)
for b in bl:
    if SKIP.match(b):
        out.append(b)
        continue
    pid = next(it)
    if pid in NEW:
        new, src, why = NEW[pid]
        out.append(new)
        log.append({'id': pid, 'old': OLD[pid], 'new': new, 'source': 'Emulate round ' + src, 'why': why})
    else:
        out.append(b)
        log.append({'id': pid, 'old': OLD[pid], 'new': b, 'source': 'v2', 'why': 'read Human alone in 322g'})
(HERE / 'v3.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v3-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v3.md', len(out), 'blocks')
