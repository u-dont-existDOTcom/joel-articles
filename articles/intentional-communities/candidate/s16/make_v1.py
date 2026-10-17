"""Section 16 draft v1 (2026-10-17): from Emulate round a (emu-a/out/s01-emuA.txt and s01-emuB.txt, byte for byte from the
laptop, sha256 69a43e1c... and a6a0f803...), the published meaning put back inside Emulate's sentences (the 2026-10-16 21:05
lesson), paragraph by paragraph from whichever call kept more of it. H2-P5 (what remote readers can build) stays as
published: it read Human in the baseline (324g, S16-E, 0.46). The headings, images and the caption stay as published.
H3-P1, the ten-word lead-in ("Here is the first month without the heroic land purchase:"), goes into H3-P2's first sentence.
The dedup (Joel 2026-10-16 23:38 UTC: "also dedeup other sections"; 2026-10-17 02:07: "you can only cut if it isn't losing
important meaning or there's no good way to merge") follows the repeats check of sections 15, 16 and the appendix
(review-r1/REPEATS.md); each cut says where the point is said. Emulate's slips are not carried over: "Call it a practice
group, or a commune, whatever." (the published says rather than a commune), "he's helping to publish the movie" (Joel
publishes it), "a two-bedroom studio apartment", "a forested mountain", "find a friend who just came back from a long retreat
and has been reborn", "wherever people take it seriously" and "they will end up building a community" (the published:
community tends to gather wherever people experience care, play, usefulness and room to become more honest). Joel's rule on
"and ... and" chains (2026-10-07) and his list rulings apply. Writes v1.md and v1-fixes.json.
Run from this folder: python3 make_v1.py"""
import hashlib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'emu-a' / 'out'
for k, h in {'s01-emuA': '69a43e1c', 's01-emuB': 'a6a0f801'}.items():
    assert hashlib.sha256((OUT / (k + '.txt')).read_bytes()).hexdigest().startswith(h), k
v0 = (HERE / 'v0.md').read_text(encoding='utf-8')
bl = [b.strip() for b in re.split(r'\n\s*\n', v0) if b.strip()]
L = {k: re.search(r'\[%s\]\(([^)]+)\)' % re.escape(k), v0).group(1) for k in
     ('Peer counseling', 'cuddle puddle', 'reparenting guide', 'Hearthwork manual', 'Twin Oaks', 'East Wind', 'Acorn',
      'intentional communities', 'ecovillages')}
NEW = {
 'H1-P1': (("One of the main problems I see with how people go about building community is that they do the steps in the wrong "
            "order. They get the land first, put the vision in a document, let ownership pile up with whoever had the money, and "
            "put off the emotional preparation until everyone has more time."), 'B',
           'B\'s opening sentence; the published list of the wrong steps (both calls dropped it) as one run-on sentence'),
 'H1-P2': (("The better order is less cinematic, more like this: practice together, process a real conflict, clarify your "
            "values, test membership, decide ownership and exit, and only then think about land."), 'B',
           'B\'s "It\'s more like this:" and its one run-on list; Joel\'s order (2026-10-16 23:38) step by step, every step his '
           '(B had "figure out who you want in" for testing membership, and no real conflict), and the published "less '
           'cinematic"'),
 'H1-P3': (("Likewise, the economic side has to go in stages. You're probably not going to be able to fly straight to the "
            "economic destination! Start with a cluster of households where nobody has to buy the basics of life inside the "
            "cluster anymore, and anyone making money on the outside contributes a set share. Only after you've proven that "
            "you can reliably provide for everybody, and fairly decide who gets what from the common, should you move to a "
            "common purse. Cutting back on outside money, or getting rid of it, comes from what you've shown you can do. "
            "(\"Money is impure!\" is a weird thing to say while somebody else is quietly paying the tax bill.)"), 'A',
           'A\'s sentences and its aside; the published staging "the same way", the common purse only after the group can '
           'provision members reliably and allocate the common fairly, and outside money reduced from demonstrated ability (A '
           'ran the two together)'),
 'H2-P1': (("I realize that for most people reading this there are a lot of reasons why they can't just head off and go build "
            "community on some land. Jobs, kids, pets, debt, a mortgage, a sick parent, or several of these arranged in a "
            "circle... That's fine! The most important pl/ork doesn't need land anyway."), 'A and B',
           'A\'s opening and its list, B\'s "go build community on some land"; the published circle joke, "Fine." and the '
           'most important pl/ork that needs no land (both calls dropped them)'),
 'H2-P2': (("People sometimes buy forty acres and then bring all their unprocessed baggage with them to a more scenic location. "
            "Sure, the view's better! But now the conflict has goats."), 'A and B',
           'A\'s baggage, B\'s goats; the published unprocessed material, the scenic location and the view'),
 'H2-P3': (("But there's no reason you can't start the inner pl/ork where you live. [Peer counseling](" + L['Peer counseling'] +
            ") only needs two people and enough privacy to talk. And reparenting, somatic work, jealousy, conflict repair, etc. "
            "don't have to wait for a deed!"), 'B',
           'B\'s sentences; the published two people and privacy, and the deed nothing has to wait for'),
 'H2-P4': (("A group that practices together weekly for two years already has a real piece of community, even if it never owns "
            "land, and it can make a difference in how people get through divorce, illness, grief, parenting and plain old "
            "loneliness."), 'A and B',
           'A\'s "make a difference in how people deal with divorce, illness, grief", B\'s "weekly for two years"; the '
           'published real piece of community and "may never own land" (A: "never buy land")'),
 'H2-P6': (("If three households can commit to showing up for each other like this for six months, you'll learn more than you "
            "would from another year of daydreaming about the ideal village."), 'A',
           'A\'s sentence; the published six months (A: "half a year"), another year and the ideal village'),
 'H3-P2': (("Here's your first month, no heroic land purchase required. Start working on the inner pl/ork, whether it's "
            "following the free [reparenting guide](" + L['reparenting guide'] + ") and [Hearthwork manual](" +
            L['Hearthwork manual'] + ") or another serious practice you already trust. And practice before you have an "
            "audience!"), 'B',
           'the published lead-in (H3-P1) as the first sentence; B\'s "whether it\'s following ... or something else"; the '
           'published serious practice you already trust and the audience'),
 'H3-P3': (("Find two or three people to form a practice group with (call it that, not a commune). Meet regularly, and learn to "
            "listen, switch roles, handle one disagreement and keep your commitments before you start talking about a shared "
            "future."), 'B',
           'B\'s first sentence; the published "rather than a commune" (A had "or a commune, whatever") and what to learn '
           'before discussing a shared future'),
 'H3-P4': (("Where do you find them? You can try unprogrammed Quaker meetings, restorative practice groups, open-hearted "
            "congregations, mature recovery groups, meditation groups, or people who came back from a long retreat kinder "
            "rather than more impressed with themselves."), 'B',
           'B\'s "You can try going to" and its list; the published congregations, and the retreat people who came back kinder '
           'rather than more impressed with themselves (B: "come back humble"); the question is the break'),
 'H3-P5': (("Then go visit actual communities, like [Twin Oaks](" + L['Twin Oaks'] + "), [East Wind](" + L['East Wind'] +
            "), [Acorn](" + L['Acorn'] + ") or other [intentional communities](" + L['intentional communities'] + ") (a lot of "
            "[ecovillages](" + L['ecovillages'] + ") take visitors too). Just check their current visitor requirements "
            "first."), 'B',
           'B\'s list with its parenthesis; the published "Read their current visitor requirements first"'),
 'H3-P6': (("You'll learn things no manifesto can teach you: how much togetherness you actually enjoy, what kind of privacy you "
            "need, which labor system drives you nuts, and whether communal showers feel liberating or send you off pricing "
            "studio apartments."), 'A and B',
           'A\'s "how much you like being together" and its showers, B\'s "what you want and don\'t want"; the published '
           'manifesto, the labor system that irritates you and the studio apartments (A: "a two-bedroom studio apartment")'),
 'H3-P7': (("So do those three things first, before you spend serious time or money looking for land."), 'B',
           'B\'s "Don\'t go looking for land until you\'ve done the above" with the published three things and the time or '
           'money'),
 'H3-P8': (("I'm not trying to sell you a retreat or get you to fill out an application or anything, the manuals are free. I'm "
            "in Sénégal and I expect to buy land, but it's not like I'm announcing a commune. I've just noticed that community "
            "tends to gather wherever people find real care, play, usefulness and room to become more honest."), 'B',
           'B\'s run-on first sentence and "it\'s not like I\'m starting a commune or anything"; the published last sentence '
           '(both calls changed it: "wherever people take it seriously", "they will end up building a community")'),
 'H3-P9': (("Decades after the Bruderhof shaped my father, I'm publishing the film he made, and writing this."), 'published',
           'DEDUP: the published "He made a film, founded a research organization, and carried me through communal '
           'experiments" is section 14\'s last paragraph ("It shaped the foundation he started and the film he made. It '
           'shaped the places he took me, too"); what is this paragraph\'s own, decades later he publishes the film and writes '
           'this, stays'),
 'H3-P10': (("Maybe some of you will help build something good from this. Maybe you'll teach someone else, who'll build "
             "another. Passing it on doesn't need one institution, one founder or one official version."), 'A',
            'A\'s two "Maybe" sentences; the published transmission that needs no one institution, founder or official '
            'version (both calls dropped it)'),
 'H3-P11': (("If you build something real, maybe we'll hear about each other. And if you teach other people to build, hearing "
             "about it matters less."), 'A',
            'A\'s pair; the published "hear about each other" and "matters less" (A: "it won\'t matter")'),
}
SKIP = re.compile(r'^(#|\[image \d+\]|\[caption\])')
IDS = ['H1-P%d' % i for i in range(1, 4)] + ['H2-P%d' % i for i in range(1, 7)] + ['H3-P%d' % i for i in range(1, 12)]
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
    if pid == 'H3-P1':
        log.append({'id': pid, 'old': OLD[pid], 'new': '', 'source': 'merged', 'why': 'into H3-P2\'s first sentence'})
        continue
    if pid in NEW:
        new, src, why = NEW[pid]
        out.append(new)
        log.append({'id': pid, 'old': OLD[pid], 'new': new, 'source': 'Emulate round a call ' + src, 'why': why})
    else:
        out.append(b)
        log.append({'id': pid, 'old': OLD[pid], 'new': b, 'source': 'published', 'why': 'read Human in the baseline (324g, S16-E, 0.46)'})
(HERE / 'v1.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v1-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v1.md', len(out), 'blocks')
