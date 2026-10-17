"""Section 15 draft v1 (2026-10-17): from Emulate round a (emu-a/out/s01-emuA.txt and s01-emuB.txt, byte for byte from the laptop,
sha256 ac0dcdfc... and a941cbb9...), the published meaning put back inside Emulate's sentences (the 2026-10-16 21:05 lesson),
paragraph by paragraph from whichever call kept more of it. Two paragraphs stay as published: H2-P5 (the moringa pods) and
H2-P6 (the sheep), which read Human together in the baseline (321g, 0.02). The headings, images, captions and the page's embed
lines stay as published. Emulate's slips are not carried over: "with my family here" (he stays with a friend's family),
"ground zero", "I used to cringe at this", "as you say", the law's wording in quotation marks that the published section
doesn't quote, "I recommended", "a similar position to a westerner". Joel's rule on "and ... and ... and" chains (section 7,
2026-10-07: commas for Emulate's "and") and his list rulings apply. Writes v1.md and v1-fixes.json.
Run from this folder: python3 make_v1.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
v0 = (HERE / 'v0.md').read_text(encoding='utf-8')
bl = [b.strip() for b in re.split(r'\n\s*\n', v0) if b.strip()]
LAW = '[Law No. 2026-08](https://www.humandignitytrust.org/resources/law-no-2026-08-of-march-27-2026-amending-article-319-of-law-no-65-60-of-july-21-1965/)'
assert LAW in v0
NEW = {
 'H1-P1': ("I live in Sénégal, where \"intentional community\" often sounds like a strange Western phrase. Don't human beings "
           "already do that?", 'B', 'B\'s reaction as the locals\' own question, kept to the published point: something people '
           'assume humans already do (B\'s "are you people not doing that in the West already??" turned it around)'),
 'H1-P2': ("Sénégal is unlike anywhere else I've lived. Five times a day the prayers pour out into the streets, and I find them so "
           "soothing. And Sufism doesn't stay inside designated \"spiritual\" places here. It's in the music, in the pictures "
           "everywhere, in the murals, in the names, in the conversations.", 'A',
           'A\'s run-on list; "People are devout in a way I\'ve never seen before" and "praying ... out in the streets" were A\'s '
           '(the published prayers pour into the streets)'),
 'H1-P3': ("And the humor! People are outside laughing for hours at a time. It's the most joking culture I've ever been in, and I "
           "keep wondering if I'll ever understand the really complicated jokes in Wolof. Basic conversation is one thing. But "
           "knowing why twelve people are suddenly crying with laughter? That's graduate school.", 'A',
           'A\'s "And the humor!"; the published "understand" the jokes (A had "make jokes") and its "twelve people" (A: "a bunch")'),
 'H1-P4': ("In the villages and families I've spent time around, a lot of what we're trying to \"re-invent\" with intentional "
           "community is just done. Land, childcare, housing, food, obligations, etc. all go through the extended family and local "
           "memory, alongside the formal systems. Nobody has to announce a workshop called \"Rebuilding Intergenerational "
           "Belonging.\" An aunt has already given three people a task.", 'A',
           'A\'s "re-invent ... just done"; "with my family here" was A\'s slip (he stays with a friend\'s family); the published '
           'local memory, formal systems, workshop and aunt back'),
 'H1-P5': ("Even in Dakar, I see things like this spray painted on walls: \"Tolerance! Openness! Union! Happiness! Love!\" And "
           "elsewhere there are murals of Sufi leaders. Spiritual graffiti still surprises me! Where I grew up, a city wall was "
           "either selling you a product or showing off somebody's inability to draw a penis.", 'A',
           'A\'s "spray painted"; the published "elsewhere" and the product-or-penis expectation (B\'s "f**k the police" left out)'),
 'H2-P1': ("Not that Sénégal is some communal paradise that survived! The warmth has hard limits, and "
           "for LGBTQ+ people who cross them, it can be brutal.", 'A', 'A\'s "it can be a brutal place"; the published stance and limits'),
 'H2-P2': ("In March 2026, Sénégal passed " + LAW + ", which raised the penalty for consensual same-sex intimacy to five to ten "
           "years in prison. It also makes public \"apology\" for homosexuality a crime, and certain financing or support meant to "
           "promote it. And that's on top of the arrests, rejection by family, harassment, assault and mob violence that were "
           "already happening. Some people say that once homosexuals are arrested they're actually protected in jail, because the "
           "mob can't get at them. I'm not going to praise communal belonging while ignoring the people who survive it by hiding who "
           "they are, or by leaving.", 'A',
           'A\'s jail sentence; the law\'s wording A put in quotation marks is out (the published section doesn\'t quote it), as are '
           'A\'s "constant" and "endemic"; the published closing stance back'),
 'H2-P3': ("So yes, a society can be spiritually alive, generous, funny and super communal. It can also be cruel to people who break "
           "its categories. Community isn't automatically freeing, then. It depends on who gets to belong without having to "
           "pretend.", 'A+B', 'A\'s and B\'s "So"; the published criterion (who may belong without pretending) for their "it depends '
           'on the community"'),
 'H2-P4': ("The forgiving social culture has its shadows too. People avoid confrontation so much that everybody knows who stole the "
           "sheep, and nobody wants to make a stink by saying it out loud.", 'A', 'A\'s "make a stink"; the published sheep, kept '
           'apart from the moringa pods, which A had folded in'),
 'H2-P7': ("But the old communal ways are changing too. The young people are heading for the cities, for jobs, phones, imported "
           "food, the wider world (and some of the men take the dangerous sea route to Europe). Families that used to share nearly "
           "everything end up depending more on cash, and on individual opportunity.", 'A',
           'A\'s parenthesis for the men; commas for A\'s "and ... and" chain (Joel\'s rule); "another world" stays in H2-P6, as published'),
 'H3-P1': ("One strange leftover of the old communal system is what people call the \"Black Tax.\" If you make any money at all, "
           "you're expected to support your parents, your siblings, school fees, medical bills, funerals, whoever else the family's "
           "carrying. I understand the instinct, though. In the ancestral way of doing things, nobody made it alone. The people who "
           "fed you, raised you, housed you and protected you had a real claim on whatever you made of yourself later. So sharing "
           "was how the whole organism survived. Nobody thought of it as charity.", 'B',
           'B\'s "if you make any money at all"; A\'s "ground zero" and "I used to cringe at this" out; the published list of who '
           'is carried, the claim and the organism back; "cousins" goes under his list rule'),
 'H3-P2': ("Today it can be soul destroying, because the obligation is still there but most of the communal life that held it up is "
           "gone. People don't share the land, the work, the childcare, the food and the daily belonging the way they did, but whoever "
           "earns the cash can still be expected to carry everybody. They can hardly build any independence or long-term stability. "
           "And the relatives who get the money stay dependent, because the payments don't give them any real alternative. The "
           "ancestral ethic is still alive, just inside an individualistic cash economy now. It keeps people alive, and it eats "
           "away at both sides while it does.", 'B',
           'B\'s order; the published survival of the obligation, the viable alternative and both sides back; "quietly" out'),
 'H3-P3': ("It's also the boundary problem any money-free commune runs into. Life inside can go without cash, but taxes, hospitals, "
           "visas, school fees, family obligations, imported tools, etc. all still come with a price in money. And no, that doesn't "
           "mean bringing individual wages back inside! It means somebody has to handle all that, and the group has to decide how "
           "much shared cash to keep for it. And how do you stop access to outside money from turning into a new status "
           "hierarchy?", 'B', 'B\'s question for the hierarchy; A\'s "as you say" out; the published boundary and wages back'),
 'H3-P4': ("Outside work complicates that boundary too, and it starts before there's a common purse. Cash is only part of what it brings "
           "in. There's another schedule, another status system and social world, other loyalties, and often new habits of "
           "consumption. In the first stage, whoever works outside gives the commune an agreed share, but the money can't buy them "
           "out of doing their share of the communal work, or buy extra political authority. And the group has to watch for outside jobs draining "
           "the people and skills it needs to build shared livelihoods. Otherwise the commune stays a dormitory for the cash "
           "economy, and the common purse never happens.", 'B',
           'B\'s "whoever is working outside" and "buy their way out of work"; A\'s "into the common purse" out (the first stage '
           'comes before it); the published dormitory back'),
 'H3-P5': ("Zapatista communities ran into a version of this with migration. Some of them used to try to stop their young people "
           "from leaving, and now they negotiate with them instead: migrants can work elsewhere as long as they keep defined obligations "
           "to the community. The pull between leaving and belonging didn't go away. But now it's something the community can name "
           "and negotiate.", 'A', 'A\'s "used to try to stop ... now ... negotiate"; A\'s "I\'ve heard" and "given up trying" out'),
 'H3-P6': ("Westerners often start out isolated and try to rebuild a tribe. A lot of Africans start out with a communal life they "
           "inherited, and watch parts of it fall apart. And urban Africans who get interested in intentional community might come "
           "to it feeling alienated from both the city and the tradition they left.", 'A',
           'A\'s "a lot of africans ... opposite direction" in the published shape; A\'s "trying to hold on to it" and "a similar '
           'position to a westerner" out'),
 'H3-P7': ("So this is a global conversation. It's way bigger than some Western lifestyle niche. There's knowledge in the living villages that no "
           "book can give you. But they're people, not exhibits! If you go, be respectful, and be ready to contribute and learn the "
           "language. Just don't show up expecting a spiritual service package.", 'B',
           'B\'s "be respectful ... learn the language" and "Don\'t go there expecting"; A\'s "I recommended" out'),
 'H3-P8': ("Oh, and a practical note: getting my residency here was pretty cheap and straightforward. French and Wolof matter a lot "
           "more than English. And the country's famous ideal of Teranga (hospitality) is real in my life. I'm staying in a friend's "
           "family's house, and they won't let me pay rent! Of course that generosity lives right alongside watchfulness, social "
           "conservatism, bureaucracy and all the usual complications of a real country.", 'B',
           'B\'s "it was pretty cheap and easy to get residency here" (his own process, as published; A generalized it) and "they '
           'won\'t let me pay rent"; the published watchfulness back'),
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
        log.append({'id': pid, 'old': OLD[pid], 'new': new, 'source': 'Emulate round a call ' + src, 'why': why})
    else:
        out.append(b)
        log.append({'id': pid, 'old': OLD[pid], 'new': b, 'source': 'published', 'why': 'read Human in the baseline (321g, S15-F, 0.02)'})
(HERE / 'v1.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v1-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v1.md', len(out), 'blocks')
