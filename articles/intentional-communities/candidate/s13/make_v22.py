"""Section 13 draft v22 (2026-10-15, after batch 299g): the land subsection (H3-P1 to H3-P5) and the run H4-P9, H5-P1, H5-P2
rebuilt from Emulate round i (emu-i/out, byte for byte from the laptop), which rewrote each stretch whole after both read AI as
wholes in every context checked (299g: https://www.pangram.com/history/0b7c2345-0629-47ef-b66a-75f5f9be2e22 and
https://www.pangram.com/history/edf0cb54-e5f7-428f-8e37-253d2954eea1). The base is call A of each stretch (l01-emuA, l02-emuA),
which kept more of the published meaning than call B; H5-P2 goes two ways, A (v22.md) and B from l02-emuB (v22b.md). Each fix is
an exact old -> new pair on one Emulate paragraph: the preservation keys, Joel's own words, and what Emulate changed in the
meaning. Everything else is Emulate's. Writes v22.md, v22b.md and v22-fixes.json. Run from this folder: python3 make_v22.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'emu-i' / 'out'
BOOK = ('https://library.uniteddiversity.coop/Ecovillages_and_Low_Impact_Development/'
        'Creating_a_Life_Together-Practical_Tools_to_Grow_Ecovillages_and_Intentional_Communities.pdf')


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v21 = blocks((HERE / 'v21.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v21) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v21))
text = {i: b for i, b in zip(IDS, v21) if i}

l01 = blocks((OUT / 'l01-emuA.txt').read_text(encoding='utf-8'))
l02 = blocks((OUT / 'l02-emuA.txt').read_text(encoding='utf-8'))
l02b = blocks((OUT / 'l02-emuB.txt').read_text(encoding='utf-8'))
assert l01[0] == 'Resources, Land, and Exit Terms' and len(l01) == 6
assert l02[1] == 'When Somebody Has to Go' and len(l02) == 4 and len(l02b) == 4
EMU = {'H3-P1': l01[1], 'H3-P2': l01[2], 'H3-P3': l01[3], 'H3-P4': l01[4], 'H3-P5': l01[5],
       'H4-P9': l02[0], 'H5-P1': l02[2], 'H5-P2': l02[3], 'H5-P2b': l02b[3]}
SRC = {k: ('emu-i/out/l01-emuA.txt' if k.startswith('H3') else 'emu-i/out/l02-emuB.txt' if k == 'H5-P2b' else 'emu-i/out/l02-emuA.txt')
       for k in EMU}

JOEL_PROCESS = "So work out the process before it's about anyone in particular."  # his own sentence, 2026-10-11
FIX = {
 'H3-P1': [
  ('INTERESTED Parties -- Who will have title', 'Who will have title',
   "Emulate's opening, a mailing-list salutation, not text"),
  ('If it\'s in the name of the "founder", then he or she is really your landlord, with a philosophy.',
   'If the deed is in the name of the founder, then he or she is really a landlord with a philosophy.',
   'key U25 "deed"; his phrase "a landlord with a philosophy" whole (kept since round r11); the quotes on "founder" '
   'doubted that he founded it, which the published does not say'),
  ('in the names of 3 out of 12 members, then despite what your literature says, there are',
   'in the names of three out of twelve members, then despite what your literature says about everyone being equal, there are',
   'key U26 "three", "twelve", "equal" (the published "whether or not the welcome packet uses the word “equal”")')],
 'H3-P2': [
  ('2. WHAT kind of legal entity (co-op, trust, association, company, etc.) will hold the land?',
   'What kind of legal entity (cooperative, trust, association, company, whatever fits your jurisdiction) will hold the land?',
   'the number is Emulate\'s list artifact; key U27 "cooperative", "jurisdiction" (the published "or whatever fits the jurisdiction")'),
  ("This needs to be decided before it's bought, so that you can decide who has what voting rights, who has what access to and use of common resources,",
   "This needs to be decided before it's bought. Then you'll need to decide who has what voting rights, who has what access and use rights to common resources,",
   '"so that" made the legal form the reason for the decisions after it, which the published lists side by side; key U28 "use rights"'),
  ('can an owner borrow money outside the community and what happens if they do, what happens when someone wants to leave',
   'what about outside debt (can an owner borrow money outside the community, and what happens if they do?), how improvements get handled, what happens when someone wants to leave',
   'key U28 "outside debt", "improvements": both in the published list; Emulate narrowed the debt to one case and dropped improvements')],
 'H3-P3': [
  ("3. How will you handle VISIBILITY of this issue? Even if you don't use money, you'll still have",
   "How will you handle VISIBILITY of what you have? Even if you're a money-free community, you'll still have",
   'the number is Emulate\'s; "this issue" named nothing; key U29 "money-free"'),
  ("know what you have, what you've set aside, what you owe, who has authority to distribute the major resources,",
   "know what's owned or held in common, what you've set aside, what obligations you have to outsiders, who has authority to hand out the major resources,",
   'key U30 "owned", "common", "obligations", "hand out" (the published: owns or holds in common, obligations outside the '
   'community, who can allocate)'),
  ("(whether it's cash or tools or transportation or temporary housing or stored up goods or whatever)",
   "(whether it's cash, if you use it, or tools, transportation, temporary housing, stored up goods, the right to keep using something, or whatever)",
   'linter O14, his ban on Emulate\'s "or ... or" chains; key U32 "keep using" (the published "continued use rights"); '
   '"if you use it", the published "cash if the community uses it"'),
  ("it can't be exercised without money!", "it can't be exercised unless the community has spare money!",
   'the published "a paper right that works only when the community has spare money": "without money" made it the leaver\'s money')],
 'H3-P4': [
  ('4. Good people', 'Good people', "the number is Emulate's"),
  ("That's a subtle way of saying they HAVE to stay if they can't afford to.",
   "That's coercive -- they HAVE to stay if they can't afford to go.",
   'key U34 "coercive" (the published "staying becomes coercive"); "subtle" was added'),
  ("Write it up when it's only theoretical", "Write up the exit terms when it's only theoretical",
   'key U35 "exit terms"; "it" named nothing'),
  ('Much easier that way.', "Much easier than doing it once everybody's furious.",
   'key U36 "furious" (the published "much easier before anybody is furious")')],
 'H3-P5': [
  ("For a fuller sequence, see Diana Leafe Christian's Creating a Life Together (on the reading list at the end) -- vision, then people,",
   "For the full sequence, see Diana Leafe Christian's [*Creating a Life Together*](%s) (on the reading list at the end) -- vision, then members," % BOOK,
   'the published "full" (trace T1 of r13 caught it lost before); key U37 "members"; the link on the title as published')],
 'H4-P9': [
  ('People who visit, work, rent and intern at the commune (yes, even interns!)',
   'Visitors, volunteers, workers, renters and interns at the commune (yes, even interns!)',
   'key U51: the published list; Emulate\'s verbs dropped the volunteers'),
  ('They should have the chance to know the terms of their association, to be heard, and to have such decisions reviewed.',
   'They should have clear terms, and the chance to be heard and to have such decisions reviewed.',
   'key U52 "clear terms" (the published "clear terms, a way to be heard, and review")'),
  ('All people are created equal, even the servants. (Wait, when did there become a class of people moving from commune to commune to be servants?)',
   'Equality is for everybody, not just members, or communes can end up recreating a servant class that moves from commune to commune.',
   'the published "Egalitarianism that stops at the membership boundary can recreate a servant class between communes": Emulate\'s '
   'two sentences said the servants are already there and asked when the class began; key U53 "equality", "servant class"')],
 'H5-P1': [
  ('It may not be possible to make the community safe for everyone.', "A community that wants to be safe can't promise to keep everyone.",
   'both Emulate calls read the published "A safe community cannot promise to keep everyone" as a community that cannot be safe '
   'for everyone; key U54 "keep everyone"'),
  ('It can be the right thing to do when someone is generally or in some way a serious danger to others, repeatedly violates essential community boundaries, or is just generally intolerable to live with.',
   "It can be the right thing to eject someone when they're a serious danger to others (or to everyone in general), repeatedly violate essential community boundaries, or are just impossible to live with.",
   'key U55 "eject", "impossible"; "generally or in some way a serious danger" garbled the published "a serious or generalized danger"'),
  ('do the necessary work with the person', 'do restorative work with the person', 'key U56 "restorative"')],
 'H5-P2': [
  ("The power to remove people is also susceptible to abuse. It's important to know in advance how it will be used.",
   'But the power to remove people is also one of the easiest to abuse. ' + JOEL_PROCESS,
   '"susceptible" lost the published "one of the easiest powers to abuse"; his own sentence of 2026-10-11 back in place of Emulate\'s; '
   '"But": the linter\'s B13 failed a third paragraph opening "The" (with "The short visit" and "The long visit")'),
  ('immediate action to protect the community?', 'immediate action to protect people?',
   'the published "immediate protective action": people, not the community as such'),
  ('family and access to common resources and outside funds (if any) be ensured during the separation?',
   'family contact, access to common resources and outside funds (if any) be protected during the separation?',
   'linter O14 ("and ... and"); the published "family contact" and "are protected"'),
  ('When will help be sought from outside?', 'When will outside help be sought?', 'key U59 "outside help"')],
 'H5-P2b': [
  ("Since this power can easily be abused, though, it's a good idea to prepare ahead for dealing with it.",
   'This power to remove people is also one of the easiest to abuse, though. ' + JOEL_PROCESS,
   '"this power" pointed to call B\'s own first paragraph, which isn\'t used, so it names the power; the published "one of the '
   'easiest powers to abuse"; his own sentence of 2026-10-11'),
  ('What might cause the community to have to act immediately to protect people from somebody?',
   'What might call for immediate action to protect people from somebody?', 'key U59 "action to protect"'),
  ('Who should stay out of these decisions?', 'Who should step aside from these decisions?',
   'key U59 "step aside" (the published "who is recused")'),
  ('housing, records, family, access to common stuff, outside money, etc., during the separation?',
   'housing, records, family contact, access to common stuff, outside money (if any), etc., during the separation?',
   'the published "family contact" and "outside funds if any"'),
  ('When will the community seek outside help, to be discussed next?', 'When will the community seek outside help? (More on that next.)',
   '"to be discussed next" read as the help being discussed; the signpost as in v21, a break in every reading')],
}
log, new = [], {}
for pid, fixes in FIX.items():
    t = EMU[pid]
    for old, new_s, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new_s)
        log.append({'id': pid, 'source': SRC[pid], 'old': old, 'new': new_s, 'why': why})
    new[pid] = t
for name, p2 in (('v22.md', 'H5-P2'), ('v22b.md', 'H5-P2b')):
    t = dict(text)
    for pid in ('H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', 'H4-P9', 'H5-P1'):
        t[pid] = new[pid]
    t['H5-P2'] = new[p2]
    out = [b if i is None else t[i] for i, b in zip(IDS, v21)]
    (HERE / name).write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v22-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for pid in ('H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', 'H4-P9', 'H5-P1', 'H5-P2', 'H5-P2b'):
    print('%-7s %3d words | %s' % (pid, len(new[pid].split()), new[pid]))
    print()
print(len(log), 'fixes')
