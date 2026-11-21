#!/usr/bin/env python3
"""Run 6's frame (PLAN.md, "Run 6"): run 4's model descriptions where the guide describes a part or role in its own
words, and Joel's own words where it doesn't (a model describes those by what sits under them: lesson
inner-child-2026-11-20r), with his framework answers to questions 114, 115 and 116.

  python3 make_frame6.py      # out/FRAME-6.json"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
NOV4 = {'N%03d' % int(s['n']): s for s in json.load(open(HERE.parent / 't132-toc-links' / 'order' / 'NOV4-SECTIONS.json'))[1:]}
OPENING, STAGES = NOV4['N001']['body'], NOV4['N003']['body']


def quote(text, words):
    """His words, checked to be in the 4 November text."""
    assert words in text, words[:40]
    return words


HIS = {
    'N005': ['Five Stages: "' + quote(STAGES, "make sure there's enough safety around you to continue with reparenting") + '"',
             'his rule (2026-11-20 23:22 UTC): "A problem goes where the reader meets it."'],
    'N015': ['the opening: "' + quote(OPENING, 'Reparenting means consciously evolving and molding a better Inner Adult inside you, '
                                       'comprising a loving Nurturer, a safe Adult Protector (hereafter just the Protector) and a wise Guide.') + '"',
             'Five Stages: "' + quote(STAGES, 'Begin to borrow adulthood') + '"'],
    'N052': ['Five Stages: "' + quote(STAGES, 'Practice being the adult--do at least one part of caring for yourself while support is still there from the previous step.') + '"',
             'Five Stages: "' + quote(STAGES, 'saying the right thing when you sit down with your little one helps') + '"'],
    'N067': ['his answer to question 116 (2026-11-21 01:47 UTC): "yes all 3 roles are for healing old patterns, that\'s true. this '
             'section is basically where we have decided to put techniques that don\'t seem to fit cleanly into just one role"',
             'his answer to question 114: "healing old patterns is just a catch all category which is not important enough to deal '
             'with such a primary obstacle"'],
    'N076': ['the opening: "' + quote(OPENING, "At first, it's deliberate and might feel difficult. Many struggle to get past the silly, awkward feeling of it.") + '"'],
    'N090': ['its first section, Altered States Can Deepen Therapy or Escapism: "' + quote(NOV4['N091']['body'],
             "Why not just blast right past that guard part, with [intensive meditation](https://goenka.u-dont-exist.com) or psychedelics? "
             "Sometimes that can help tremendously, but both can get you past the guards before there's a grown-up big enough to hold "
             "whatever comes through, so I'd hold off until there's enough Nurturer and Protector around.") + '"'],
    'N141': [],
    'N028': ['the opening: "' + quote(OPENING, 'a loving Nurturer') + '"',
             'his answer to question 114: "when you have shame or you need forgiveness, it is someone who feeling like a nurturer that '
             'you go to for that [...] love accepts. protection blocks. guide directs. shame and forgiveness need acceptance."',
             'his answer to question 115: "the nurturer doesn\'t give divine love, they give the love of the nurturer [...] divine love '
             'is beyond taking care of someone, or hugging them, or being with them or listening to them. it\'s infinite, it\'s '
             'unspeakable..."',
             'his line on divine love in his guide: "This is what the Inner Guide can bring you to"'],
}


def main():
    f2 = json.load(open(HERE / 'out' / 'FRAME-2.json'))
    f5b = json.load(open(HERE / 'out' / 'FRAME-5B.json'))
    parts, roles = [], []
    for p in f2['parts']:
        if p['id'] in HIS:
            parts.append({'id': p['id'], 'heading': p['heading'], 'his_words': HIS[p['id']]})
        else:
            parts.append({'id': p['id'], 'heading': p['heading'], 'job': p['job']})
    for r in f2['roles']:
        if r['id'] in HIS:
            roles.append({'id': r['id'], 'name': r['name'], 'his_words': HIS[r['id']]})
        else:
            roles.append({'id': r['id'], 'name': r['name'], 'work': r['work']})
    frame = {
        'about': 'What each part and role of the guide is for. Where the guide describes a part or role in its own words, '
                 '"job" or "work" is a reader\'s summary of it. Where it doesn\'t, "his_words" are the author\'s own words '
                 'about it (empty: only its name). "joel_view" is how the author sorts things.',
        'parts': parts, 'roles': roles, 'joel_view': f5b['joel_view'],
    }
    (HERE / 'out' / 'FRAME-6.json').write_text(json.dumps(frame, indent=1, ensure_ascii=False) + '\n')
    print('model descriptions kept: %s; his words: %s' % (
        ', '.join(x.get('heading') or x.get('name') for x in parts + roles if 'his_words' not in x),
        ', '.join(x.get('heading') or x.get('name') for x in parts + roles if 'his_words' in x)))


if __name__ == '__main__':
    main()
