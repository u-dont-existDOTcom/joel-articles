#!/usr/bin/env python3
"""The proposed contents (the pick) for the Self-Hypnosis guide: Fable's names (PROPOSAL-FABLE.json) with my changes,
and the structure Joel chose in his answers to Fable's 15 notes (2026-11-24 01:04 UTC, answers/JOEL-20261124-0104.md).

  python3 make_pick.py

Writes PROPOSAL-PICK.json (the new order, without the headings that go; for readers and score_reads.py),
PICK-FOR-PAGE.json (every heading of CONTENTS-NOW.json, in the post's order, for contents_picks_page.py),
TOC-PICK-SIDEBAR.md and LINES-PICK.json (what fresh readers see), EXPECTED-PICK.json (the answer key with the merged and
dropped sections mapped to where their text goes) and STRUCTURE.json (every move, level change and dropped heading, with
the answer it comes from).
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

# My changes to Fable's names, each with its reason (read against tools/humanization/headings_brief.md)
MINE = {
    'S013': ("What It's For, and Not For", 'Fable\'s "What Self-Hypnosis Is For" dropped your "and What Not To"; this keeps both '
             'halves and fits.'),
    'S017': ('Start From the Whole', 'Your words ("start from the sacred whole"); Fable\'s "Fragmented? Start Whole" read three ways to a reader of the first pick.'),
    'S030': ('When to Stop Scanning', 'Your words ("knows when to stop scanning"); readers of the first pick read Fable\'s "Protect, Then Stand Down" as a repeat of "The Protector".'),
    'S032': ("Don't Rush the Repair", 'Your words, which fit; Fable made them positive, and readers asked "repair of what?" of both.'),
    'S034': ('Write With Your Other Hand', 'Says it is writing; a reader of the first pick: "Other-Hand Dialogue only makes sense once you know it is writing".'),
    'S037': ('Wake Up Inside the Influence', 'Your words, which fit once "De-hypnosis:" goes; a reader of the first pick read "De-Hypnosis: Wake Up" as leaving a trance.'),
    'S122': ('Buteyko & Systema', 'Names both practices, now that the section adds Systema\'s continuous breathing (your message of 2026-11-24 21:05 UTC); its neighbours are method names too (EFT Tapping, Somatic Experiencing, Gendlin Focusing). "Buteyko & Systema Breathing" is cut off.'),
    'S118': ('The Whole NLP Sequence', 'Your words ("Running the whole NLP sequence"); "The Whole Sequence" left readers asking "of what?".'),
    'S023': ('Inner Child Practices', 'With the three jobs and the guards moved out (your answer 4), what stays under it is the '
             'practices: the two-hand practice, reparenting in hypnosis, the slow repair, play and rest, the other-hand '
             'dialogue. Readers said yours repeated the section above it.'),
    'S029': ('Your Inherited Parent Script', 'Your words fit as they are.'),
    'S091': ('A: Asking the Subconscious', 'Your answer 12: a letter instead of "Appendix" leaves room for what it is about; '
             'the text still says "Appendix A".'),
    'S093': ('B: NLP Without the Sales Pitch', 'Your answer 12; keeps your sales-seminar joke in a form that fits.'),
    'S119': ('C: The De-Hypnosis Checklist', 'Your answer 12; your words without "extended".'),
    'S121': ('D: Anxiety, Body First', 'Your answer 12; your words.'),
    'S129': ('E: Is Daydreaming Helping?', 'Your answer 12; your question, shortened to fit.'),
    'S130': ('F: Self-Trust and Guidance', 'Your answer 12. After the moves it holds finding a hypnotist (with the audit '
             'questions merged in), the oracle and the council.'),
    'S136': ('G: Altered States', 'Your answer 12.'),
    'S138': ('H: Demons, Jinn & Presences', 'Your answer 12; keeps the words a reader with that fear would look for.'),
    'S148': ('I: An Induction Library', 'Your answer 8 drops the sleep appendix, so this becomes I; your words.'),
    'S158': ('J: Sources & Further Reading', 'Was K; your words.'),
}

# His answers to Fable's notes, as operations
DROPPED = {   # heading that goes: where its text goes
    'S002': ('S001', 'answer 1: its two sentences end "How to Use This Huge Guide"'),
    'S090': (None, 'answer 2: the heading and its note go; "How to Use This Huge Guide" already says the appendices are extra tools'),
    'S120': ('S131', 'answer 10: merged into "Find a Hypnotist Who Fits" in Appendix F'),
    'S144': ('S143', 'answer 7: cut to one sentence at the end of "Could It Be Psychosis?", linking to "Daily Life Is the Feedback"'),
    'S147': ('S047', 'answer 8: the sleep appendix goes; "Sleep Induction" already gives the same Nimja playlist'),
}
LEVEL = {'S009': (2, 'answer 5: S009 only; it now sits under S008'),
         'S028': (1, 'answer 4: the guards get an h1 of their own, with the parent script under it'),
         'S064': (2, 'answer 6: moved up and made an h2')}
MOVES = [  # (ids, after id, answer)
    (['S025', 'S026', 'S027', 'S030'], 'S018', 'answer 4: the three jobs and the Protector drill go under "The Inner Adult’s Three Jobs", right after its own text'),
    (['S134', 'S135'], 'S022', 'answer 9: forgiveness goes next to "Love First, Trust Later" and "Instead of Blame"'),
    (['S028', 'S029'], 'S135', 'answer 4: the guards and the parent script, as their own h1, after the three jobs'),
    (['S064'], 'S055', 'answer 6: right after the own text of "Let the Response Guide You", before "Finding Your Own Words"'),
]


def main(name='PICK'):
    now = json.load(open(os.path.join(HERE, 'CONTENTS-NOW.json'), encoding='utf-8'))
    fable = {e['id']: e for e in json.load(open(os.path.join(HERE, 'PROPOSAL-FABLE.json'), encoding='utf-8'))}
    pick = {}
    for e in now:
        f = fable[e['id']]
        h, why = (MINE[e['id']] if e['id'] in MINE else (f['heading'], f.get('why', '')))
        lvl = LEVEL.get(e['id'], (e['level'], ''))[0]
        assert ts.shown(h, lvl)[0], (e['id'], h)
        kind = 'kept' if h == e['heading'] else 'renamed'
        pick[e['id']] = {'id': e['id'], 'level': lvl, 'heading': h, 'was': e['heading'], 'kind': kind,
                         'why': why, 'by': 'mine' if e['id'] in MINE else 'Fable'}
    order = [e['id'] for e in now if e['id'] not in DROPPED]
    for ids, after, _ in MOVES:
        for i in ids:
            order.remove(i)
        at = order.index(after) + 1
        order[at:at] = ids
    entries = [pick[i] for i in order]
    json.dump(entries, open(os.path.join(HERE, 'PROPOSAL-%s.json' % name), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    page = []
    for e in now:
        p = dict(pick[e['id']])
        if e['id'] in DROPPED:
            p.update(heading=e['heading'], level=e['level'], kind='dropped', why=DROPPED[e['id']][1])
        page.append(p)
    json.dump(page, open(os.path.join(HERE, '%s-FOR-PAGE.json' % name), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    words = {e['id']: e['words'] for e in now}
    lines, nums = ['# Contents as the sidebar shows it', '', 'Line, level and heading, then the words under it.', ''], []
    for n, e in enumerate(entries, 1):
        lines.append('%02d.  %s%s %s  (%d words)' % (n, '    ' * (e['level'] - 1), '#' * e['level'],
                                                    ts.shown(e['heading'], e['level'])[1], words[e['id']]))
        nums.append({'n': n, 'id': e['id']})
    open(os.path.join(HERE, 'TOC-%s-SIDEBAR.md' % name), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    json.dump(nums, open(os.path.join(HERE, 'LINES-%s.json' % name), 'w'), indent=0)
    key = json.load(open(os.path.join(HERE, 'EXPECTED-REVIEWED.json'), encoding='utf-8'))
    to = {k: v[0] for k, v in DROPPED.items()}
    for n, v in key['situations'].items():
        for part in ('right', 'also'):
            v[part] = list(dict.fromkeys(to.get(i, i) for i in v.get(part, []) if to.get(i, i)))
    key['about'] += ' Remapped for the pick: a dropped or merged heading\'s section counts as the section its text goes to.'
    json.dump(key, open(os.path.join(HERE, 'EXPECTED-PICK.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({'dropped': DROPPED, 'level': LEVEL, 'moves': MOVES}, open(os.path.join(HERE, 'STRUCTURE.json'), 'w',
              encoding='utf-8'), ensure_ascii=False, indent=1)
    ren = sum(1 for e in entries if e['kind'] == 'renamed')
    print('pick: %d headings (%d dropped), %d renamed, %d mine, none cut off' % (len(entries), len(DROPPED), ren, len(MINE)))


if __name__ == '__main__':
    main(*sys.argv[1:])
