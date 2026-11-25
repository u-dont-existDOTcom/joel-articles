#!/usr/bin/env python3
"""The final contents of the Self-Hypnosis guide: Joel's record of 2026-11-25 01:08 UTC (answers/JOEL-20261125-0108.json,
every heading as he left it on his picks page) with the structure his answers there add to STRUCTURE.json
(answers/JOEL-20261125-0108.md says how each answer is read).

  python3 make_final.py

Writes PROPOSAL-FINAL.json (the order after the moves, without the headings that go), STRUCTURE-FINAL.json,
TOC-FINAL-SIDEBAR.md and LINES-FINAL.json (what fresh readers see), EXPECTED-FINAL.json (the answer key, remapped) and
FINAL-CONTENTS.md (the page he can read: every heading, what it was, and whose words it is).
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/'
J = lambda f: json.load(open(os.path.join(HERE, f), encoding='utf-8'))

# Changes to the headings in his record, each with its reason
ADJUST = {
    'S015': ("You're Better Than the Pros", 'his words; "the" in AP title case (headings brief, rule 7), as recorded on 2026-11-24 14:18'),
    'S093': ('B: Ethical NLP', 'his pick of Fable\'s "Appendix B: Ethical NLP", with the letter only, as his answer 12 '
             'gives every appendix ("A: ...", "C: ...")'),
    'S157': ('No-Trance Inner Contact', 'his answer of 2026-11-25: it leaves the induction library, so it loses its number'),
    'S018': ('Become a Trustworthy Adult', 'his answer of 2026-11-25 ("rethink the heading at least"): the section now '
             'holds ten sections, three of them the jobs, and all ten are about being the adult the inner child can trust; '
             'his words ("becoming reliable" in its first paragraph, "become a trustworthy adult" in the Closing). The '
             'three jobs show right under it: The Nurturer, The Protector, The Guide'),
}
# His answer of 2026-11-25 01:08 UTC to "What the readers of the proposal still found", as operations added to STRUCTURE.json
LEVEL_ADD = {
    'S086': (1, '2026-11-25: "daily life should not be when to get outside help": an h1 of its own, where it stands, '
             'between the outside-help sections and the Closing'),
    'S157': (1, '2026-11-25: out of the induction library, an h1 of its own above the inductions'),
}
MOVES_ADD = [
    (['S131'], 'S085', '2026-11-25: "wouldn\'t find a hypnotist go under when to get outside help?": after "Do These With '
     'a Clinician", with the audit merged in (answer 10)'),
    (['S157'], 'S039', '2026-11-25: "no trance inner contact shouldn\'t be in the induction library i guess, and i\'d put '
     'that above the inductions, makes sense to do that preliminarily": right before "Induction: Gather and Soften"'),
]


def build():
    rec = J('answers/JOEL-20261125-0108.json')
    now = J('CONTENTS-NOW.json')
    st = J('STRUCTURE.json')
    proposed = {e['id']: e for e in J('PICK3-PAGE-OPTION.json')}
    fable = {e['id']: e for e in J('PROPOSAL-FABLE.json')}
    dropped = dict(st['dropped'])
    level = {k: tuple(v) for k, v in st['level'].items()}
    level.update(LEVEL_ADD)
    moves = [tuple(m) for m in st['moves']] + MOVES_ADD
    final = {}
    for e in now:
        i = e['id']
        if i in dropped:
            continue
        h = rec['headings'][i]
        assert h != '(goes)', i
        whose = ('his words' if rec['picks'].get(i) == 'own' else 'Fable\'s first version, his pick' if rec['picks'].get(i) == 'fable'
                 else 'his heading, kept' if h == e['heading'] else 'his heading, title case' if h.lower() == e['heading'].lower()
                 else 'the proposal, left as it was')
        why = ''
        if i in ADJUST:
            h, why = ADJUST[i]
            if i == 'S018':
                whose = 'mine, 2026-11-25, for him to change'
        lvl = level.get(i, (e['level'], ''))[0]
        ok, shown = ts.shown(h, lvl)[:2]
        assert ok, (i, h, lvl)
        final[i] = {'id': i, 'level': lvl, 'heading': h, 'was': e['heading'], 'was_level': e['level'], 'whose': whose,
                    'why': why, 'kind': 'kept' if h == e['heading'] else 'renamed'}
    order = [e['id'] for e in now if e['id'] not in dropped]
    for ids, after, _ in moves:
        for i in ids:
            order.remove(i)
        at = order.index(after) + 1
        order[at:at] = ids
    return rec, now, dropped, level, moves, [final[i] for i in order]


def main():
    rec, now, dropped, level, moves, entries = build()
    json.dump(entries, open(os.path.join(HERE, 'PROPOSAL-FINAL.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({'dropped': dropped, 'level': level, 'moves': moves}, open(os.path.join(HERE, 'STRUCTURE-FINAL.json'), 'w',
              encoding='utf-8'), ensure_ascii=False, indent=1)
    words = {e['id']: e['words'] for e in now}
    lines, nums = ['# Contents as the sidebar shows it', '', 'Line, level and heading, then the words under it.', ''], []
    for n, e in enumerate(entries, 1):
        lines.append('%02d.  %s%s %s  (%d words)' % (n, '    ' * (e['level'] - 1), '#' * e['level'],
                                                    ts.shown(e['heading'], e['level'])[1], words[e['id']]))
        nums.append({'n': n, 'id': e['id']})
    open(os.path.join(HERE, 'TOC-FINAL-SIDEBAR.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    json.dump(nums, open(os.path.join(HERE, 'LINES-FINAL.json'), 'w'), indent=0)
    key = J('EXPECTED-REVIEWED.json')
    to = {k: v[0] for k, v in dropped.items()}
    for n, v in key['situations'].items():
        for part in ('right', 'also'):
            v[part] = list(dict.fromkeys(to.get(i, i) for i in v.get(part, []) if to.get(i, i)))
    key['about'] += ' Remapped for the final contents: a dropped or merged heading\'s section counts as the section its text goes to.'
    json.dump(key, open(os.path.join(HERE, 'EXPECTED-FINAL.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    moved = {i: (after, why) for ids, after, why in moves for i in ids}
    head = {e['id']: e['heading'] for e in entries}
    md = ['# Self-Hypnosis guide: the contents that goes in', '',
          'Your record of 2026-11-25 01:08 UTC ([as you sent it](%sanswers/JOEL-20261125-0108.md)), with the structure your '
          'answers set. %d headings (5 go), %d renamed, none cut off in the sidebar. Nothing on the post has changed yet.'
          % (GH, len(entries), sum(1 for e in entries if e['kind'] == 'renamed')), '',
          '| # | Heading | Whose | Was | Change of place or level |', '|---|---|---|---|---|']
    for n, e in enumerate(entries, 1):
        note = []
        if e['id'] in moved:
            note.append('moves after “%s”' % head[moved[e['id']][0]])
        if e['level'] != e['was_level']:
            note.append('h%d, was h%d' % (e['level'], e['was_level']))
        md.append('| %d | %s%s | %s | %s | %s |' % (n, '&nbsp;&nbsp;&nbsp;&nbsp;' * (e['level'] - 1), e['heading'], e['whose'],
                                                '' if e['kind'] == 'kept' else e['was'], '; '.join(note)))
    md += ['', '## The headings that go', '']
    was = {e['id']: e['heading'] for e in now}
    for i, (to_, why) in dropped.items():
        md.append('- “%s”: %s' % (was[i], why))
    md += ['', '## Changed from your record, and why', '']
    for i, (h, why) in ADJUST.items():
        md.append('- “%s” (you had “%s”): %s.' % (h, rec['headings'][i], why))
    open(os.path.join(HERE, 'FINAL-CONTENTS.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print('final: %d headings, %d renamed, %d moves, none cut off' % (len(entries), sum(1 for e in entries if e['kind'] == 'renamed'), len(moves)))


if __name__ == '__main__':
    main()
