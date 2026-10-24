#!/usr/bin/env python3
"""Turn 106: OWNER-EDITS.json for Joel's answers of 2026-10-24 22:55 UTC. Entries whose strings his new versions or his
cuts replaced are superseded (or carry his current strings), each with a history note, and three new entries record
what went in: his five places, d3, and his picks on the ideas page."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / 'OWNER-EDITS.json'
NEW = json.loads((HERE / 'HIS-SECTIONS.json').read_text(encoding='utf-8'))
D3 = (HERE.parent / 't105-tries' / 'drafts' / '98_2-d3.txt').read_text(encoding='utf-8').strip()
WHEN = 'Turn 106 (his answers of 2026-10-24 22:55 UTC, experiments/t106-answers/JOEL-20261024-2255.md)'
data = json.loads(P.read_text(encoding='utf-8'))
by = {e['id']: e for e in data['entries']}


def history(e, note):
    e.setdefault('history', []).append(WHEN + ': ' + note)


def supersede(eid, note):
    e = by[eid]
    e['status'] = 'superseded'
    history(e, note)


def cut_from(eid, field, old, new, note):
    e = by[eid]
    vals = e[field]
    hits = [k for k, v in enumerate(vals) if old in v]
    assert len(hits) == 1, (eid, field, old[:40], hits)
    vals[hits[0]] = vals[hits[0]].replace(old, new)
    history(e, note)


for eid in ('wcs-h3', 'wcs-p1-what-is-blocking', 'wcs-p4-joel-ending', 'pgq-005-duration', 'pgq-013-transfer',
            'five-percent-question', 'wcs-p1-getting-ready', 'wcs-p2-joel'):
    supersede(eid, 'his own When to Change the Strategy, word for word, replaced the section (entry joel-106-20261024-sections). '
              'Of the guide points here, his P3 keeps that relief isn\'t proof of a deeper fix and that the benefit should carry into '
              'regular life (the texting example); "not a reason to go deeper" and "one small act teaches more than more meditations" '
              'went with 98.7 as its own paragraph.')
supersede('mpv-p5-joel', '102.2 A put d3 in for this paragraph (entry joel-106-20261024-982).')
supersede('speak-toward-joel-20261017-2259', 'his own Speak Toward What You Are Building, word for word, replaced P1 and P2 (entry joel-106-20261024-sections).')
cut_from('ldw-p11-joel', 'must_contain', " Hindsight being 20/20 doesn't change that.", '', 'his E10 A cut the last sentence.')
cut_from('guide-p14-joel-20261017', 'must_contain_exact', 'Timing is different for everyone, but most of us', 'Most of us', 'his H32 A cut "Timing is different for everyone, but".')
cut_from('photos-h2-joel-20261017', 'must_contain_exact', 'Or just nothing comes up, which is also completely OK.', 'Or just nothing comes up.', 'his H17 A.')
cut_from('photos-h2-joel-20261017', 'must_contain_exact', 'guided imagery and suggestions, so we gotta be careful about that.', 'guided imagery and suggestions.', 'his H18 A.')
cut_from('joel-88-20261022', 'must_contain_exact', ' You can always slow down and look closer when it helps.', '', 'his H2 A ("that was from GPT, i humanized it but didn\'t notice how jarring that last stupid sentence was").')
cut_from('joel-104-20261023', 'must_contain_exact', ' Not all at once, though.', '', 'his H31 A.')
cut_from('plork-paragraph', 'must_contain', '## Start With Whatever Showed Up\n\nYour little one wants to play', '## Play Is Part of the Work\n\nYour little one wants to play',
         'his E15 A: the pl/ork paragraph now opens "Play Is Part of the Work", and "Start With Whatever Showed Up" heads the how-to after it.')
cut_from('acacia-mimosa-20261011b', 'must_contain', 'mixing acacia confusa with mimosa hostilis is very dangerous', 'mixing acacia confusa with mimosa hostilis is very destabilizing and challenging',
         'his H23 merge put the warning in one sentence of his.')
e = by['q8c-acacia-why-20261011c']
e['must_contain'] = [s for s in e['must_contain'] if s != 'highly destabilizing and challenging'] + ['very destabilizing and challenging, but excellent if you want to know how it feels to be painfully autistic + schizo!']
history(e, 'his H23 merge: "I also learned that mixing acacia confusa with mimosa hostilis is very destabilizing and challenging, but excellent if you want to know how it feels to be painfully autistic + schizo!" in place of the two sentences.')
e = by['published-first-person-20261017']
old = [s for s in e['must_contain_exact'] if s.startswith('My father used to tell suicidal people')]
assert len(old) == 1
e['must_contain_exact'] = [s for s in e['must_contain_exact'] if s not in old] + ['My father used to tell suicidal people, “Oh, you want to kill yourself? That’s wonderful! Now you can change what you’ve always been too afraid to change in your life, and then see if you still want to end it!”']
history(e, 'his own crisis stretch, word for word, has his father\'s line as he wrote it now, without "His point wasn\'t that dying is wonderful."')
e = by['dedup-cuts-20261021']
for f in ('must_contain', 'must_contain_exact'):
    if f in e:
        e[f] = [s for s in e[f] if 'Look at that life you' not in s]
history(e, 'his own crisis stretch ends the father paragraph differently, so its old last line is no longer required.')

HEADS = ['## Five Stages of Reparenting', '### Signs of Manipulation', '### When Somatic Work Brings Things Up', '### Ill Will and Loving-Kindness',
         "### Show Up When Nothing's Wrong", '##### Invite Your Little One In', '### Make It Intentional', "### How Would You Know It's Helping?",
         '### What to Make of a Passing Feeling', '### Answering the Strict Disciplinarian', '## Play Is Part of the Work', '## Start With Whatever Showed Up',
         '#### The Belief Behind the Guards', '#### Intensive Meditation and Psychedelics', '## What to Do With a Peak', '### Gentle Meditation and Mantra',
         '## The Spiritual Side of the Question', '### When Being Happy Feels Like Abandoning Someone', '#### Differentiation', '## Dating While You Heal',
         '#### Before You Tell the Hardest Stuff', '### Ask What Kind of Company They Want', '### The Love Has to Move', '## Forgiving Yourself', '## Missing Someone']
data['entries'] += [
    {'id': 'joel-106-20261024-sections', 'status': 'applied',
     'what': "Joel's own versions of five places, word for word, each checked by him: When to Change the Strategy (all five paragraphs; 98.7's own paragraph is gone, its point his P3's texting example), You Don't Need an Inner Monologue, the crisis stretch of If You Want to Kill Yourself, First Social Connections, Done Right, and Speak Toward What You Are Building without its last paragraph. The Forbes link's markdown has no space before its address. Installed by experiments/t106-installs/apply_t106.py.",
     'joel': '2026-10-24 22:55 UTC: "i fixed the whole section and now it\'s 100% high conf human, learn some lessons"; "now it\'s fully dark green"; "crisis stretch is now fully human"; "first social connections is fully green"; "now speak toward is all green ... yes i removed the final para on that one, it seemed extra"',
     'where': 'When to Change the Strategy; You Don\'t Need an Inner Monologue; If You Want to Kill Yourself; First Social Connections, Done Right; Speak Toward What You Are Building',
     'must_contain_exact': [p.replace('[so research could be dangerous] (https://', '[so research could be dangerous](https://') for k in ('change', 'monologue', 'crisis', 'social', 'speak') for p in NEW[k]],
     'must_not_contain': ['Sometimes the session itself goes really well.', 'What they tell you is worth remembering, too']},
    {'id': 'joel-106-20261024-982', 'status': 'applied',
     'what': "102.2 A: d3 in place of his Not Every Hero Wears A Cape P5 (Human alone and in its h2 through the API, experiments/t105-api/API-CHECKS.md).",
     'joel': '2026-10-24 22:55 UTC: "102.2 98.2a"', 'where': 'Not Every Hero Wears A Cape',
     'must_contain_exact': [D3], 'must_not_contain': ['information to learn from', 'Healing is nonlinear', "Hey, we've all been there."]},
    {'id': 'joel-106-20261024-ideas', 'status': 'applied',
     'what': "His picks on the ideas page (experiments/t105-readers-edit/IDEAS.md): 25 heading lines (E2 to E33 and E15's two), the cuts E10 and E13, E34's paragraph break, and the hedge cuts H2, H3, H7, H12, H14, H17, H18, H22 (with his \"These are just\"), H23 (his merged sentence), H26 (with the line before it), H31, H32, H38 (with the Jeffrey Young parenthetical) and H39.",
     'joel': '2026-10-24 22:55 UTC: his answers e1 to e35 and h1 to h41 (experiments/t106-answers/JOEL-20261024-2255.md)',
     'where': 'the whole article',
     'must_have_line': HEADS,
     'must_contain': ['These are just caution signs', 'Most of us need enough Nurturer and Protector first.', "It's scaffolding.",
                      'more foolish indifference. You can see both sides of this see-saw'],
     'must_not_contain': [" I can't tell you exactly what to do about it", 'You can always slow down and look closer when it helps.',
                          "It doesn't mean you're stupid or crazy.", "it isn't a test of whether you were loved enough", 'Some of them are only one step anyway.',
                          'You can figure that out later.', 'which is also completely OK', 'so we gotta be careful about that',
                          "I'd never recommend anyone risk it", 'Being ready to do anything to end the pain', 'Not all at once, though.',
                          'Timing is different for everyone', '(no belief in God required)', "Past that, a lot depends on who you're seeing.",
                          'did his postdoctoral work with Aaron Beck', "Hindsight being 20/20 doesn't change that.",
                          'If you made a mistake, you can see how to repair that.']},
]
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits updated:', len(data['entries']), 'entries')
