#!/usr/bin/env python3
"""Joel's answers of 2026-11-23 17:24 UTC (answers/JOEL-20261123-1724.json) as the edit to his post: every heading's
final text and level, the headings that go, the section that moves, and the lines his answers add. Writes PLAN.json and
the guide before and after as Markdown (BEFORE.md, AFTER.md) for section_refs.py and the Pangram checks.

His answers, word for word, and what each does here:
- Spiritual Bypass Warning: "remove ###realization isn't enough, so its body can sit under ##spiritual bypass warning.###
  friends heading can be under ##spirirtual byapss warning still" -> S023's heading goes; its text follows S022's heading.
- Loving-kindness: "yes make it ##. yes open the section with that blessing on its own" -> S008 h3 -> h2; the blessing
  (the old heading, emoji and all) opens the section as a line of its own.
- Enlightened Fingers: "yes" -> S018 h3 -> h2, with S019 (h3) after it, now under it; the old heading's sentence opens
  the section.
- Rebirth sections: "no leave it i fixed the title so it makes sense i think they should be under it" -> no move; his
  S048 "Stream Entry Ends Rebirth".
- Appendix: "yeah last suggestion sounds good" (move the section into the manual after "What Remains Afterward") ->
  the h1 "Appendix" goes and S060 follows S056, keeping its level (h2).
- Your own phrases: "it's ok to drop all that. i have her vid there anyway." -> nothing added for them.
Headings: his "headings" record, with one capital: "The pithy Bāhiya Sutta" -> "The Pithy Bāhiya Sutta" (title case).
Rule 9 (a first line that leaned on the old heading): S015's "both of us" leaned on "For Me & Bāhiya", which his pick
"Desperation Did the Trick" drops, as the page's note for S015 said -> "both Bāhiya and I".
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, 'answers', 'JOEL-20261123-1724.json'), encoding='utf-8'))
SEC = json.load(open(os.path.join(HERE, 'SECTIONS.json'), encoding='utf-8'))
S = {s['id']: s for s in SEC}

HEAD = dict(A['headings'])
FIXES = {'S013': ('The pithy Bāhiya Sutta', 'The Pithy Bāhiya Sutta', 'title case: a capital for "Pithy"')}
for i, (was, now, why) in FIXES.items():
    assert HEAD[i] == was
    HEAD[i] = now
LEVEL = {'S008': 2, 'S018': 2}
# His picks for these two read below High in Pangram in their sections (gate: nothing goes in below High; Joel, 2026-11-21:
# "make sure you don't add anything that hasn't passed pangram with high conf"), so they keep their headings until he picks
# again: NB-toc-S055#36 (the heading alone, Human Low; his heading read Medium) and NB-toc-S060#37 (Human Low, 45 words;
# his heading read High).
HOLD = {'S055': 'his pick "Did It Work or Go Wrong?" read Human Low by itself in its section (NB-toc-S055#36)',
        'S060': 'his pick "Is It Safe When \"I\" Vanish?" read Human Low with its first sentences (NB-toc-S060#37)'}
DROP_HEADING = {'S023': 'his answer: its text sits under "Spiritual Bypass Warning"',
                'S059': 'his answer: "Appendix" goes and its one section moves into the manual'}
MOVE = {'S060': 'S056'}  # move S060 to right after S056
OPEN_LINE = {'S008': '🫶🏿 May All Beings Be Loving, Peaceful & Free 🫶🏿',
             'S018': 'Your fingers are already enlightened, but your hand is deluded.'}
TEXT_EDIT = {'S015': ('Interestingly, both of us were really desperate', 'Interestingly, both Bāhiya and I were really desperate',
                      'rule 9: "both of us" leaned on the old heading "Desperation Did The Trick For Me & Bāhiya"')}


# Section links (gate inner-child-2026-11-20c; Joel, 2026-11-23 17:24 UTC: "make sure you're linking to the section anchors
# whenever they are mentioned"): (section the words sit in, a string that finds them once, the words to link, target).
LINKS = [
    ('S001', 'The Enlightenment Manual then', 'The Enlightenment Manual', 'S021'),
    ('S011', 'what I’ll explain later as partial untying', 'partial untying', 'S030'),
    ('S016', 'the fingers event I’ll tell you about below', 'the fingers event', 'S018'),
    ('S019', 'the room itself unweaving', 'the room itself unweaving', 'S016'),
    ('S019', 'those terms more carefully below', 'those terms more carefully below', 'S048'),
    ('S025', 'that evidence later on', 'that evidence later on', 'S051'),
    ('S029', 'the guided meditation later in this article', 'the guided meditation later in this article', 'S054'),
    ('S034', 'Amaro translation of the Bāhiya Sutta', 'the Bāhiya Sutta', 'S013'),
    ('S039', 'the Bāhiya Sutta, repeats', 'the Bāhiya Sutta', 'S013'),
    ('S039', 'passage I quoted earlier', 'I quoted earlier', 'S033'),
    ('S052', 'the lucid dreaming analogy I made earlier', 'the lucid dreaming analogy I made earlier', 'S020'),
    ('S057', 'the lovely Bāhiya Sutta', 'the lovely Bāhiya Sutta', 'S013'),
    ('S058', 'as I said earlier in the essay', 'as I said earlier in the essay', 'S035'),
]
UNLINKED = [  # mentions left without a link on purpose, with the reason (for CURRENT-STATE.md)
    ('S004', 'the weight of the world', 'the heading takes its words from this line, its own first line'),
    ('S017', 'before the room event', 'the room event is this subsection\'s own parent, the line above it in the contents'),
    ('S019', 'I call the fingers event body-limited nibbāna and the room event', 'the fingers event is this subsection\'s parent; the room event is linked once already in this section'),
    ('S019', 'which I analyze further down', 'no single section: the analysis runs through the manual'),
    ('S025', 'In the video below', 'a video in the same section'),
    ('S037', 'the capacity for suffering', 'the section\'s own words'),
    ('S039', 'nibbāna as light flows', 'its own parent\'s heading, the line above in the contents'),
    ('S040', 'go into the light', 'the section\'s own words'),
    ('S057', 'because I told you a sound heard itself', 'the section links the Bāhiya Sutta section once already, in its first line'),
    ('S058', 'come and see for yourself', 'the section\'s own words'),
]


def order():
    ids = [s['id'] for s in SEC if s['id'] != 'S000']
    for m, after in MOVE.items():
        ids.remove(m)
        ids.insert(ids.index(after) + 1, m)
    return ids


def main():
    for i, l in OPEN_LINE.items():
        assert S[i]['heading'] == l or i == 'S018' and S[i]['heading'] == l, (i, S[i]['heading'])
    for i, (a, b, _) in TEXT_EDIT.items():
        assert S[i]['text'].count(a) == 1, i
    plan = []
    for i in order():
        s = S[i]
        e = {'id': i, 'was': s['heading'], 'was_level': s['level'], 'level': LEVEL.get(i, s['level']),
             'heading': None if i in DROP_HEADING else (s['heading'] if i in HOLD else HEAD[i])}
        if i in HOLD:
            e['held'] = {'his_pick': HEAD[i], 'why': HOLD[i]}
        if i in DROP_HEADING:
            e['drop_heading'] = DROP_HEADING[i]
        if i in MOVE:
            e['moved_after'] = MOVE[i]
        if i in OPEN_LINE:
            e['open_line'] = OPEN_LINE[i]
        if i in TEXT_EDIT:
            e['text_edit'] = {'from': TEXT_EDIT[i][0], 'to': TEXT_EDIT[i][1], 'why': TEXT_EDIT[i][2]}
        if i in FIXES:
            e['heading_fix'] = {'his': FIXES[i][0], 'why': FIXES[i][2]}
        plan.append(e)
    import sys
    sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
    import section_links as sl
    final = {e['id']: e['heading'] for e in plan if e['heading']}
    links = []
    for where, find, words, target in LINKS:
        assert S[where]['text'].count(find) == 1 and words in find, (where, find)
        links.append({'in': where, 'find': find, 'words': words, 'target': target, 'heading': final[target],
                      'href': sl.url('https://ibogaqueen.substack.com', 209400477, final[target]),
                      'unchecked': sl.unchecked(final[target]) or ''})
    unlinked = [{'in': w, 'words': t, 'why': y} for w, t, y in UNLINKED]
    json.dump({'answers': 'answers/JOEL-20261123-1724.json', 'sections': plan, 'links': links, 'unlinked': unlinked}, open(os.path.join(HERE, 'PLAN.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    def md(entries, after):
        out = []
        for e in entries:
            s = S[e['id']]
            text = s['text']
            if after:
                if 'text_edit' in e:
                    text = text.replace(e['text_edit']['from'], e['text_edit']['to'])
                if 'open_line' in e:
                    text = e['open_line'] + '\n\n' + text
                if e['heading']:
                    out.append('#' * e['level'] + ' ' + e['heading'])
            else:
                out.append('#' * s['level'] + ' ' + s['heading'])
            if text.strip():
                out.append(text.strip())
        return '\n\n'.join(out) + '\n'
    before = [{'id': s['id']} for s in SEC if s['id'] != 'S000']
    ops = {'rename': [], 'drop': [], 'move': [], 'insert': [], 'edit': [], 'links': [], 'expected_headings': []}
    after_head = {e['id']: e['heading'] for e in plan}
    for e in plan:
        if e['heading'] is None:
            ops['drop'].append({'id': e['id'], 'text': e['was'], 'level': e['was_level']})
            continue
        ops['expected_headings'].append([e['level'], e['heading']])
        if e['heading'] != e['was'] or e['level'] != e['was_level']:
            ops['rename'].append({'id': e['id'], 'from': e['was'], 'from_level': e['was_level'], 'to': e['heading'], 'to_level': e['level']})
        if 'moved_after' in e:
            nxt = plan[plan.index(e) + 1]['id']
            ops['move'].append({'id': e['id'], 'heading': e['heading'], 'before': after_head[nxt]})
        if 'open_line' in e:
            ops['insert'].append({'id': e['id'], 'heading': e['heading'], 'text': e['open_line']})
        if 'text_edit' in e:
            ops['edit'].append({'id': e['id'], 'from': e['text_edit']['from'], 'to': e['text_edit']['to']})
    ops['links'] = [{'find': l['find'], 'words': l['words'], 'href': l['href']} for l in links]
    json.dump(ops, open(os.path.join(HERE, 'EDITOR-OPS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(os.path.join(HERE, 'BEFORE.md'), 'w', encoding='utf-8').write(md(before, False))
    open(os.path.join(HERE, 'AFTER.md'), 'w', encoding='utf-8').write(md(plan, True))
    n = sum(1 for e in plan if e['heading'] and e['heading'] != e['was'])
    print('PLAN.json, BEFORE.md, AFTER.md written:', len(plan), 'sections,', n, 'headings renamed,',
          len(DROP_HEADING), 'headings removed,', len(LEVEL), 'levels changed,', len(MOVE), 'moved,', len(OPEN_LINE), 'lines added,', len(TEXT_EDIT), 'sentence fixed')


if __name__ == '__main__':
    main()
