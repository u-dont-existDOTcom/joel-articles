#!/usr/bin/env python3
"""Turn 139: how to change the guide so its readers know where to look (RECOMMENDATIONS.md).

Joel, 2026-11-21 13:07 UTC: "in that approach you should recommend how to improve the guide so the real readers will
also know where they would look for the sections". Two kinds, both proposals for him: a line or two under each part
and role the guide gives no text of its own (a reader, like a model, can only guess what it holds; lesson
inner-child-2026-11-20r), drafted from his own words; and a pointer, with a link, where most of five card-sort
readings would look for a section under another part or role than the one it sits in (READERS-LOOK.json, made by
where_readers_look.py). Nothing here is in the post or checked with Pangram yet.

  python3 recommend.py      # RECOMMENDATIONS.md"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
POST = 'https://ibogaqueen.substack.com/i/189761959/'
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-child-therapy/experiments/'

INTROS = [
    ('Building Your Inner Adult', 'h1', 'Your Inner Adult has three jobs: protection blocks, love accepts, and the guide directs. '
     'Until each one grows in you, you can borrow it from someone who has it.',
     'his answer to question 114 ("love accepts. protection blocks. guide directs."); the opening ("a loving Nurturer, a safe '
     'Adult Protector [...] and a wise Guide"); Five Stages ("Begin to borrow adulthood")'),
    ('The Nurturer', 'h2', 'Love accepts. The Nurturer is who you\'d go to with shame, or when you need forgiveness: someone '
     'who takes care of you, holds you, stays with you and listens. Divine love goes beyond that, and the Guide can take you there.',
     'his answers to questions 114 ("when you have shame or you need forgiveness, it is someone who feeling like a nurturer '
     'that you go to") and 115 ("divine love is beyond taking care of someone, or hugging them, or being with them or '
     'listening to them"); his line "This is what the Inner Guide can bring you to"'),
    ('Safety and Readiness', 'h1', 'Before you go deep, make sure there\'s enough safety around you to continue: in your body, '
     'with the people in your life, and with yourself.',
     'Five Stages ("make sure there\'s enough safety around you to continue with reparenting"); what the part holds'),
    ('Practice With Your Little One', 'h1', 'These are ways to sit down with your little one, and any of the three roles can '
     'use them: how to start, how to listen, and how to close the session.',
     'Five Stages ("saying the right thing when you sit down with your little one helps"); his answer to question 114 (a '
     'practice "could be done by any of the roles")'),
    ('When Practice Gets Hard', 'h1', 'At first it\'s deliberate, and it might feel difficult: fake, empty, shallow, or like '
     'something to escape. Here\'s what helps, and how to tell whether it\'s working.',
     'the opening ("At first, it\'s deliberate and might feel difficult"); what the part holds'),
    ('Altered States', 'h1', 'Psychedelics and intensive meditation can deepen this work or turn it into escapism. Here\'s '
     'how to prepare, what to do with a peak, and what to do if a trip leaves reality behind.',
     'Therapy or Escapism? ("intensive meditation or psychedelics [...] can get you past the guards before there\'s a '
     'grown-up big enough to hold whatever comes through"); what the part holds'),
    ('Play and Your Preferences', 'h2', 'Your little one wants to play too, and to find out what they really like.',
     'Play Is Part of the Work ("Your little one wants to play, too")'),
    ('Keeping Your Own Ground', 'h2', 'You can belong without trading away your own inner knowing.',
     'Belonging Bargains ("pull you away from your own inner-knowing in return for belonging")'),
]

POINTERS = {
    'N078': ('the end of When It Feels Fake (after "So, it\'s worth meditating first on why it feels fake.")',
             'And for some people, it first feels real in an altered state: see [Altered Can Make It Real](%saltered-can-make-it-real).' % POST),
    'N039': ('the end of If Love Isn\'t Coming Yet, under the Nurturer (after "That takes warmth, and if there isn\'t any yet, borrow some.")',
             'Once you have a little warmth, [A Heart to Child Loop](%sa-heart-to-child-loop) sends it down to your little one.' % POST),
    'N075': ('the end of Discipline Done Right?, which moves to the Guide with Re-do Trauma Memories',
             'If the strict voice from back then still runs your routines, see [Answer the Disciplinarian](%sanswer-the-disciplinarian), under the Protector.' % POST),
    'N070': ('the end of Re-do Trauma Memories',
             'Another way to settle a hard memory is to finish it like a story: [“And So That’s the Way It Happened!”](%sand-so-thats-the-way-it-happened), under the Nurturer.' % POST),
    'N041': ('Earning trust, day to day, under the Protector, after "like keeping a promise to yourself nobody else knew about"',
             'A vow to your little one is one of those promises ([Make a Simple Vow](%smake-a-simple-vow)).' % POST),
    'N126': ('the opening of Speaking Up in Conflict',
             'Speaking up for yourself with doctors is in [Physical Pain?](%sphysical-pain).' % POST),
}
SERVED = {'N035': 'already pointed to from the Nurturer: Divine Love: Bigger Door links to Toward Divine Love'}


def cross(r):
    """Another part, or another role inside Building Your Inner Adult (a sibling inside the same part shows beside it
    in the sidebar, so it needs no pointer)."""
    a, b = r['sits_in'], r['readers_look']
    return a['part'] != b['part'] or (a['part'] == 'Building Your Inner Adult' and a['under'] != b['under'])


def main():
    look = json.load(open(HERE / 'READERS-LOOK.json'))
    rows = look['sections_readers_look_elsewhere']
    far = [r for r in rows if cross(r) and r['readers_look']['readings'] >= 3]
    near = [r for r in rows if not cross(r)]
    weak = [r for r in rows if cross(r) and r['readers_look']['readings'] < 3]
    L = ['# How to help readers know where to look (turn 139)', '',
         'Joel, 2026-11-21 13:07 UTC: "in that approach you should recommend how to improve the guide so the real readers '
         'will also know where they would look for the sections". Made by [recommend.py](%st139-readers/recommend.py) '
         'from [where_readers_look.py](%st139-readers/where_readers_look.py). These are proposals: none is in the post, '
         'and none has been checked with Pangram yet. The section names are his of 20 November, with the moves of '
         'question 117 (A).' % (GH, GH), '',
         '## 1. A line or two under each part and role with no text of its own', '',
         'A reader who opens the contents sees only a part\'s name. Where the guide says nothing under it, they guess what '
         'it holds, as the models did. Each line below is drafted from his own words, given beside it.', '']
    for name, lvl, text, src in INTROS:
        L += ['- **%s** (%s, before its first section): "%s"' % (name, lvl, text), '  - From: %s.' % src]
    L += ['', 'Conclusion and Appendix and Appendix need none. Instead of separate lines, one "how this guide is laid out" '
          'paragraph near the top could do the same job for a first-time reader.', '',
          '## 2. A pointer where readers would look somewhere else', '',
          'Five blind card sorts (runs 3 to 6 in the contents test, each with a different frame) filed every section where '
          'a reader thought it belongs. Where at least 3 of the 5 would look under another part, or another role, than '
          'the one it sits in now, a real reader may look there too. A pointer with a link goes in that place:', '']
    def place(a, sec):
        if a['under'] and a['under'] != sec:
            return '%s (under %s)' % (a['part'], a['under'])
        return a['part']
    for r in far:
        u = r['id']
        where = place(r['readers_look'], None)
        sits = place(r['sits_in'], r['section'])
        sec = r['section'] if not r['merged_into'] else '%s (merged into %s)' % (r['section'], r['merged_into'])
        head = '- **%s**: %d of 5 readings would look in %s; it is in %s' % (sec, r['readers_look']['readings'], where, sits)
        if u in SERVED:
            L.append(head + '. %s.' % (SERVED[u][0].upper() + SERVED[u][1:]))
            continue
        at, text = POINTERS[u]
        L += [head + '.', '  - At %s: "%s"' % (at, text)]
    L += ['', '%d more sections were filed under a neighbouring heading inside the same part (%s). They show next to each '
          'other in the sidebar, so they need no pointer. %s' % (
              len(near), ', '.join(r['section'] for r in near),
              ('Too few readings agreed on another place for %s.' % ', '.join(r['section'] for r in weak)) if weak else ''), '',
          '**Answer the Disciplinarian**, going to the Protector (question 117, A): 2 of the 5 readings put it there, '
          'beside The Parent You Inherited, and 3 beside Discipline Done Right?, which goes to the Guide. The pointer '
          'above serves the 3. '
          'Re-do Trauma Memories: one reading (run 6, high confidence) put it under Borrow Hindsight, where it now goes.', '',
          '## 3. Then test it with readers', '',
          'Once he has picked what goes in, the contents test from 16 and 17 November (fresh readers, the sidebar\'s '
          'headings, real situations, "where would you look first?") runs again on the new contents. It shows whether the '
          'lines and pointers changed where readers look.', '']
    (HERE / 'RECOMMENDATIONS.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
