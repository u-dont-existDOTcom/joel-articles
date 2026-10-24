#!/usr/bin/env python3
"""Turn 106: Joel's answers of 2026-10-24 22:55 UTC (experiments/t106-answers/JOEL-20261024-2255.md) into the article.

- His own versions of five places, word for word (HIS-SECTIONS.json, taken from his message by its own markers): When to
  Change the Strategy (all five paragraphs; 98.7's point is now his P3's texting example), You Don't Need an Inner
  Monologue, the crisis stretch in If You Want to Kill Yourself, First Social Connections, Done Right, and Speak Toward What
  You Are Building (its last paragraph out: "yes i removed the final para on that one, it seemed extra"). The only change
  to his characters is the Forbes link's markdown: his "[so research could be dangerous] (https://...)" has a space that
  would show the brackets and the address instead of a link.
- 102.2 A: d3 for his 98.2 (experiments/t105-tries/drafts/98_2-d3.txt).
- His picks on the ideas page (experiments/t105-readers-edit/IDEAS.md), checked against his new versions first: the
  headings E2 to E33 he took (E22's move is moot, since his H26 answer cuts that paragraph), the cuts E10 and E13, the
  paragraph break E34, and the hedge items H2, H3, H7, H12, H14, H17, H18, H22 (with "These are just"), H23 (his merged
  sentence), H26 (with the line before it), H31, H32, H38 (with the Jeffrey Young parenthetical) and H39. H35's sentence
  is in his new Speak Toward, which he wrote and checked, so it stays as he has it. E5 (a paragraph break in his new
  Inner Monologue) is tried through the API before it goes in, as he said ("you can try").
Every replacement asserts that it finds its text exactly once.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
OLD = json.loads((HERE / 'OLD-SECTIONS.json').read_text(encoding='utf-8'))
NEW = json.loads((HERE / 'HIS-SECTIONS.json').read_text(encoding='utf-8'))
D3 = (HERE.parent / 't105-tries' / 'drafts' / '98_2-d3.txt').read_text(encoding='utf-8').strip()
NOTE = '<!-- Turn 106 (his answers of 2026-10-24 22:55 UTC, experiments/t106-answers/JOEL-20261024-2255.md): %s -->\n\n'

s = ART.read_text(encoding='utf-8')


def once(old, new):
    global s
    n = s.count(old)
    assert n == 1, (n, old[:90])
    s = s.replace(old, new)


def line_of(start):
    """The one paragraph line that starts with START."""
    hits = [l for l in s.split('\n') if l.startswith(start)]
    assert len(hits) == 1, (len(hits), start)
    return hits[0]


# 1. His five places, paragraph for paragraph
FORBES_BAD = '[so research could be dangerous] (https://'
FORBES_OK = '[so research could be dangerous](https://'
for key, label in (('change', 'his When to Change the Strategy, word for word ("i fixed the whole section and now it\'s 100% high conf human"); 98.7\'s point is his P3\'s texting example'),
                   ('monologue', 'his You Don\'t Need an Inner Monologue, word for word ("now it\'s fully dark green")'),
                   ('crisis', 'his crisis stretch, word for word ("crisis stretch is now fully human"); the Forbes link\'s markdown has no space before its address, so it shows as a link'),
                   ('social', 'his First Social Connections, Done Right, word for word ("first social connections is fully green")'),
                   ('speak', 'his Speak Toward What You Are Building, word for word ("now speak toward is all green"); its last paragraph is out ("it seemed extra")')):
    olds, news = OLD[key], [p.replace(FORBES_BAD, FORBES_OK) for p in NEW[key]]
    for k, old in enumerate(olds):
        if k < len(news):
            once(old, (NOTE % label if k == 0 else '') + news[k])
        else:
            once('\n' + old + '\n', '\n')

# 2. 102.2 A: d3
once(line_of('After the day, look at what actually happened. If you did the Protector action(s)'),
     NOTE % '102.2 A, d3 for his 98.2 (Human alone and in its h2, experiments/t105-api/API-CHECKS.md)' + D3)

# 3. Headings from the ideas page (level: one below the section it splits)
HEADS = [
    ('For now, I think of the whole path in five fairly predictable stages.', '## Five Stages of Reparenting', 'E2'),
    ("Some gurus really do demand surrender, and they're the opposite of the Guide", '### Signs of Manipulation', 'E3'),
    ('Some somatic work can feel pleasant, and some can feel like a raging storm got unleashed.', '### When Somatic Work Brings Things Up', 'E4'),
    ("In one of the Buddha's own accounts of how he woke up, ill will shows up in his mind", '### Ill Will and Loving-Kindness', 'E6'),
    ("If the only time the Nurturer shows up is when something's wrong", "### Show Up When Nothing's Wrong", 'E7'),
    ('Once you start to feel that lovely softness of the heart, invite your little one in with you', '##### Invite Your Little One In', 'E8'),
    ("Intentional, meaning you pick one of those acts and decide when you'll do it", '### Make It Intentional', 'E9'),
    ("Don't be afraid to ask your therapist/yourself", "### How Would You Know It's Helping?", 'E11'),
    ("Here's where I want to clearly depart from the new-age wizdumb", '### What to Make of a Passing Feeling', 'E12'),
    ('A good routine, like yoga in the morning and a proper bedtime, still feels like lockdown', '### Answering the Strict Disciplinarian', 'E14'),
    ('Say you learned somewhere along the way that if you need someone, they end up leaving you.', '#### The Belief Behind the Guards', 'E16'),
    ('So why not just blast right past that part, with intensive meditation or psychedelics?', '#### Intensive Meditation and Psychedelics', 'E18'),
    ('Now, the beautiful stuff.', '## What to Do With a Peak', 'E19'),
    ('Gentle meditation or self-hypnosis is a different story.', '### Gentle Meditation and Mantra', 'E21'),
    ("I try not to proselytize about spirituality, because I've made that mistake before", '## The Spiritual Side of the Question', 'E23'),
    ('Some families run on a bargain like "If I\'m happy while someone I love is suffering', '### When Being Happy Feels Like Abandoning Someone', 'E24'),
    ('Differentiation can happen right inside a family, religion, community or relationship.', '#### Differentiation', 'E25'),
    ('Maybe you’d rather that your support person were a lover, as well.', '## Dating While You Heal', 'E27'),
    ('Then there’s the stuff that’s hardest to tell anyone', '#### Before You Tell the Hardest Stuff', 'E28'),
    ('Before giving anyone advice, your little one included, it can help to find out what kind of company they want', '### Ask What Kind of Company They Want', 'E30'),
    ('Community can come before the big opening or after it, too.', '### The Love Has to Move', 'E31'),
    ('Forgiving yourself works the same way.', '## Forgiving Yourself', 'E32'),
    ('When you miss someone, let the ache be a cue for love.', '## Missing Someone', 'E33'),
]
for start, head, tag in HEADS:
    p = line_of(start)
    once('\n' + p + '\n', '\n' + head + '\n\n' + NOTE % ('%s from the ideas page, the heading only (his "%s a")' % (tag, tag.lower())) + p + '\n')

# E15: the section's first two paragraphs get their own heading, and Start With Whatever Showed Up moves down to its how-to
once('\n## Start With Whatever Showed Up\n', '\n## Play Is Part of the Work\n')
p = line_of('You might go looking for your little one and get mad instead')
once('\n' + p + '\n', '\n## Start With Whatever Showed Up\n\n' + NOTE % 'E15, the section\'s own heading moved down to its how-to, its first two paragraphs under "Play Is Part of the Work" (his "e15 a")' + p + '\n')

# 4. Cuts and the paragraph break from the reader's edit
once(' Hindsight being 20/20 doesn\'t change that.', '')                                  # E10
once(' If you made a mistake, you can see how to repair that.', '')                       # E13
once(' more foolish indifference. You can see both sides of this see-saw',                 # E34
     ' more foolish indifference.\n\nYou can see both sides of this see-saw')

# 5. The hedge read
once(' You can always slow down and look closer when it helps.', '')                      # H2
once(" I did it too. It doesn't mean you're stupid or crazy.", ' I did it too.')         # H3
once("It's scaffolding, and it isn't a test of whether you were loved enough.", "It's scaffolding.")  # H7
once(' Some of them are only one step anyway.', '')                                       # H12
once(' Maybe forget the parts detective work for a minute. You can figure that out later.',
     ' Maybe forget the parts detective work for a minute.')                               # H14
once('Or just nothing comes up, which is also completely OK.', 'Or just nothing comes up.')  # H17
once('easily influenced by guided imagery and suggestions, so we gotta be careful about that.',
     'easily influenced by guided imagery and suggestions.')                               # H18
once(" I can't tell you exactly what to do about it, and nobody can tell you for sure what's best for you. There are just caution signs,",
     ' These are just caution signs,')                                                     # H22, with his "These are just"
once("I also learned that mixing acacia confusa with mimosa hostilis is very dangerous. I'd never recommend anyone risk it, since it's highly destabilizing and challenging.",
     'I also learned that mixing acacia confusa with mimosa hostilis is very destabilizing and challenging, but excellent if you want to know how it feels to be painfully autistic + schizo!')  # H23, his merge
once('\nBeing ready to do anything to end the pain isn’t a suicide plan, so I wouldn’t present it as one to get relief. But if you’re scared you’ll actually hurt yourself, or can’t tell whether you’re safe, get someone with you right away.\n',
     '\n')                                                                                 # H26, with the line before it
once(' can get a lot less desperate. Not all at once, though. Your little one', ' can get a lot less desperate. Your little one')  # H31
once('Timing is different for everyone, but most of us need enough Nurturer and Protector first.',
     'Most of us need enough Nurturer and Protector first.')                               # H32
once(" since it grew out of cognitive therapy ([Jeffrey Young](https://en.wikipedia.org/wiki/Jeffrey_Young_(psychologist)), who developed it, did his postdoctoral work with Aaron Beck).",
     ' since it grew out of cognitive therapy.')                                           # his H38 extra cut
once('back in Your Loan is PRE-APPROVED! (no belief in God required).', 'back in Your Loan is PRE-APPROVED!')  # H38
once(" (more on that in the next section). Past that, a lot depends on who you're seeing.", ' (more on that in the next section).')  # H39

ART.write_text(s, encoding='utf-8')
print('installed: 5 sections of his, d3, %d headings plus E15, E10, E13, E34 and 14 hedge items' % len(HEADS))
