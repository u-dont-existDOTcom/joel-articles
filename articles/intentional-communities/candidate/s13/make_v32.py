"""Section 13 draft v32 (2026-10-17), from Joel's message of 2026-10-16 23:38 UTC:

- "yes i want "if the community uses them" back in section 13": his exact words, in the cash reserves question. Batch 312g
  read v31 with them as a whole, and the section stays 100% Human (0.11, two Human windows, both high). The AI windows of
  v30 (310g) came from my paraphrase ", if you have any?" with "gets exhausted", never from his words, which I hadn't tested.
- "no ai tells you see, and it has human tells? isn't that part of the rules?": his rule that every paragraph passes alone.
  312g checked each v31 paragraph alone for the first time: all read Human but the short visit, which read AI over its 45 words
  with the paragraph before it. Its punchline is the "Congratulations: you have established that ..." joke, a format AI has
  taken over (his ruling of 2026-10-02 on quips: keep the point, let the format go). The point stays: a short visit shows
  little more than that someone can be charming for two weeks.
- "no we should not lean on Christian's book order if it contradicts my own order ... so fix that": H3-P5 now points to the
  book for the nuts and bolts, not for the order. The article's order is his, in "Practice Comes Before Property" (practice,
  a real conflict, values, membership, ownership and exit, then land).
- "also dedup other sections you're asking about": the repeats round r19 found (review-r19/REPEATS.md), cut where the other
  instance carries the point better:
  item 3, the failing well: section 12's "The water well doesn't care how beautiful the new member's heart is." (his) carries
  it; H1-P4 keeps the exhausted person.
  item 1, scarcity without money: section 4's "Even in a moneyless community, someone can control what's scarce." (his)
  carries it; H3-P3 keeps the bottlenecks in its list of what people need to see.
  item 6, a right to leave needs resources: H3-P3 and H3-P4 said it side by side; the exit resources move into H3-P4 next to
  "That's coercive", and H3-P3's "specified ahead of time" sentence goes (H3-P4's "Write up the exit terms when it's only
  theoretical" says it).
  item 4, growing faster than the group can carry: H4-P1's "It's no good for anyone to join a group that can't deliver what it
  promised." restated section 12's capacity point and section 5's warning about promising too much; The Farm stays.
  item 15, time gives evidence, not certainty: H4-P4 and H4-P6 both said it; H4-P6's "there's still no "good person"
  detector" stays.
  item 14, the order of steps: gone with the book line.
  The others are kept, each with its reason (DISPOSITIONS-r21.md); item 5 is his own sentence and is asked on the questions
  page.

Writes v32.md and v32-fixes.json. Run from this folder: python3 make_v32.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v31.md').read_text(encoding='utf-8')
BOOK = ('[*Creating a Life Together*](https://library.uniteddiversity.coop/Ecovillages_and_Low_Impact_Development/'
        'Creating_a_Life_Together-Practical_Tools_to_Grow_Ecovillages_and_Intentional_Communities.pdf)')
EXIT = ('Whether or not you use money, you\'ll need to have a way of providing people with resources when they leave (cash, if '
        'you use it, but also tools, transportation, temporary housing, stored up goods, the right to keep using something, or '
        'whatever). Otherwise your "right" to leave is only on paper -- it can\'t be exercised unless the community has spare '
        'money!')
FIX = [
    ('H1-P4', 'How long will your cash reserves last?', 'How long will your cash reserves last, if the community uses them?',
     'Joel, 2026-10-16 23:38 UTC: "yes i want "if the community uses them" back"; his published words, read Human in v31 (312g)'),
    ('H1-P4', 'dead in the water if your well fails, or if the one person', 'dead in the water if the one person',
     'repeats r19 item 3: section 12\'s well (his) carries it'),
    ('H3-P3', 'Even if you\'re a money-free community, you\'ll still have scarce resources and bottlenecks. Sorry! ',
     'There will be bottlenecks, sorry! ',
     'repeats r19 item 1: section 4\'s "Even in a moneyless community, someone can control what\'s scarce." (his) carries the '
     'scarcity; the bottlenecks and the "Sorry!" (the paragraph\'s break; march r21 read b found none without it) stay'),
    ('H3-P3', ' It will be important to have it specified ahead of time what people\'s rights are to the common resources when '
              'they leave the community. ' + EXIT, '',
     'repeats r19 item 6: the exit resources move into H3-P4; "specified ahead of time" is H3-P4\'s "Write up the exit terms '
     'when it\'s only theoretical"'),
    ('H3-P4', 'You don\'t want to make them leave everything they\'ve put in when they leave! That\'s coercive',
     'You don\'t want to make them leave everything they\'ve put in! ' + EXIT.replace('your "right"', 'their "right"') +
     ' That\'s coercive',
     'repeats r19 item 6: the two halves of the point (a paper right, staying becomes coercive) said once, side by side, as '
     'published'),
    ('H3-P5', 'For the full sequence -- vision, then members, then pooling major resources, then land -- see Diana Leafe '
              'Christian\'s ' + BOOK + ' (on the reading list at the end). Honestly, it\'s where I\'d start for getting that '
              'order right!',
     'Honestly? For the nuts and bolts of all this (members, resources, land, agreements, etc.), I\'d go to Diana Leafe '
     'Christian\'s ' + BOOK + ' (on the reading list at the end).',
     'Joel, 23:38: "no we should not lean on Christian\'s book order if it contradicts my own order"; his order is in "Practice '
     'Comes Before Property", and his reading list recommends the book for membership, money, land and agreements'),
    ('H4-P1', ' It’s no good for anyone to join a group that can’t deliver what it promised.', '',
     'repeats r19 item 4: section 12\'s capacity point and section 5\'s "recruit too quickly and promise too much" carry it'),
    ('H4-P3', 'charming for two weeks. So if that\'s all they do, congratulations! You\'ve established that they can be charming '
              'for two weeks. 😅', 'charming for two weeks. Not exactly a ' +
     'high bar! 😅 So that\'s about all you\'ll find out.',
     'batch 312g: with H4-P2 it read AI over exactly these 45 words; the "Congratulations: you have established" format is '
     'AI\'s now (his 2026-10-02 ruling on quips: keep the point)'),
    ('H4-P4', 'may be able to pull off an act for months, so time gets you more evidence, not certainty.',
     'may be able to pull off an act for months!',
     'repeats r19 item 15: H4-P6\'s "Six months will give you more data, but there\'s still no "good person" detector." '
     'carries it'),
    # the phrases two or more cold reads paused at across rounds (pause_tally.py over review-r11 to review-r21; the rule of
    # Joel's 2026-10-16 18:22 answer: each gets a fix or a reason before Pangram); these had none
    ('H1-P3', 'before you need a surveyor', 'before you need a land surveyor',
     'pause tally: "before you need a surveyor" (r19 b, r21 a); "land" says what the surveyor is for (published "before hiring '
     'a surveyor")'),
    ('H3-P4', 'You don\'t want to make them leave everything they\'ve put in!', 'You don\'t want them to lose everything they\'ve '
     'put in!', 'pause tally: "make them leave everything they\'ve put in" (r17 a, r19 a); the published "forfeiting everything '
     'contributed"'),
    ('H3-P4', 'it can\'t be exercised unless the community has spare money!', 'it only works when the community happens to have '
     'spare money!', 'pause tally: "unless the community has spare money" (r16 a, r19 b); the published "a paper right that works '
     'only when the community has spare money"'),
    ('H4-P6', 'It’s also easy to take people doing what everyone else is doing as a sign of safety.',
     'It’s also easy to think someone’s safe just because they’re going along with everyone else.',
     'pause tally: "doing what everyone else is doing as a sign of safety" (r19 b, r21 a); the published "mistaking conformity '
     'for safety"'),
    ('H4-P6', 'Six months will give you more data', 'Six months with someone will give you more data',
     'pause tally: "Six months" (r19 a, r21 a): six months of what; the published "Six months gives you a larger sample"'),
    ('H4-P8', 'before anybody sells a house.', 'before anybody sells their house to move in.',
     'pause tally: "before anybody sells a house" (r17 b, r19 b); whose house and why'),
    ('H5-P4', 'Also decide on a mediator or ombud in advance.', 'Also decide on a mediator or ombudsperson in advance.',
     'pause tally: "ombud" (six reports, r16 to r21); the plainer word for the published "ombud"'),
    # round r21's trace T1 (review-r21/trace-T1.md) on the merged H3-P4
    ('H3-P4', 'You don\'t want them to lose everything they\'ve put in! Whether or not you use money, you\'ll need to have a way '
              'of providing people with resources when they leave (cash, if you use it, but also tools, transportation, '
              'temporary housing, stored up goods, the right to keep using something, or whatever). Otherwise their "right" to '
              'leave is only on paper -- it only works when the community happens to have spare money! That\'s coercive -- they '
              'HAVE to stay if they can\'t afford to go.',
     'You don\'t want them to lose everything they\'ve put in! That\'s coercive -- they HAVE to stay if they can\'t afford to '
     'go. Whether or not you use money, you\'ll need to have a way of providing people with resources when they leave (cash, '
     'if you use it, but also tools, transportation, temporary housing, stored up goods, the right to keep using something, or '
     'whatever). Otherwise their "right" to leave is only on paper -- it only works when the community happens to have spare '
     'money!',
     'trace r21 T1-1 (SHIFT): after the move, "That\'s coercive" read as the paper right; the published ties coercion to '
     'forfeiting everything contributed, so it follows "lose everything" again, and the exit resources come after it'),
    ('H3-P4', 'Much easier than doing it once everybody\'s furious.', 'Much easier than doing it once anybody\'s furious.',
     'trace r21 T1-2 (SHIFT): "everybody" made the window last until all are angry; the published "before anybody is furious"'),
]
log = []
for pid, old, new, why in FIX:
    assert t.count(old) == 1, (pid, old[:80])
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old.strip(), 'new': new, 'why': why})
(HERE / 'v32.md').write_text(t, encoding='utf-8')
(HERE / 'v32-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v32.md:', len(t.split()), 'words (v31:', len((HERE / 'v31.md').read_text(encoding='utf-8').split()), ')')
