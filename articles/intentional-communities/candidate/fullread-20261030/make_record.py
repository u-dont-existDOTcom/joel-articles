"""DISPOSITIONS.json and READ.md for the community article's full read by the lead model (30 October 2026).

Every finding of FINDINGS.json (READER-1..10.md, my read of master.md beside original.md, part by part) gets a fate:
- "his": on his marking page (review/REVIEW-FULLREAD.*), as the card named; the post is live, so even a fix to my words
  waits on him;
- "not": no card, and why: a point he cut himself stays out (gates E298, E301), a snag in words he chose that a reader
  still gets stays as it is, or my reading was wrong.
How a point left was traced through every version (the trace is in READ.md): his published post (original.md), my version
of 18 October (MY-FINAL-20261018.md, which master.md still was on 21 October), his edits of 20 October (his and GPT's,
community-final-substack-20261020.html), the restructure of 23 October, his answers to 64, 65 and 66, and the live post;
and against his rulings in OWNER-EDITS.json (JOEL-CHANGES.md).

  python3 articles/intentional-communities/candidate/fullread-20261030/make_record.py
  python3 tools/humanization/compare_read.py record articles/intentional-communities/candidate/fullread-20261030
"""
import collections
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
DIR = 'articles/intentional-communities/candidate/fullread-20261030/'
E20 = 'his edits of 20 October (his and GPT\'s) took this out'

CARDS = {'F1.2': 'C-1', 'F1.3': 'C-2', 'F1.7': 'C-3', 'F1.9': 'C-4', 'F2.3': 'C-5', 'F2.5': 'C-6', 'F3.1': 'C-7',
         'F3.2': 'C-8', 'F3.3': 'C-9', 'F3.7': 'C-10', 'F4.3': 'C-11', 'F5.6': 'C-12', 'F6.6': 'C-13', 'F7.3': 'C-14',
         'F7.5': 'C-15', 'F8.5': 'C-16', 'F8.6': 'C-17', 'F8.8': 'C-18', 'F8.10': 'C-19'}
CUT = {
    'F1.5': E20 + ' (the group-chat joke was in my version of 18 October).',
    'F1.6': 'His ruling of 30 September (section 1): "labor credit" went.',
    'F1.10': E20 + ': he rewrote the AI paragraph ("Apart from the Covid lockdowns just prior ...").',
    'F2.2': 'His answer 59 a (23 October) put the new sentence in place of his own of 1 October, which had the '
            'relationships point.',
    'F2.4': E20 + ': it was his own rewrite of 1 October ("People want to go back to the old way of living, but they '
            'have no idea why earlier communes failed ...").',
    'F2.8': 'His ruling of section 4 (P7): "longer meetings and fewer robes" went (every wording he tried was flagged).',
    'F3.5': 'My version moved it to "Six months with someone will give you more data, but there\'s still no \'good '
            'person\' detector."; ' + E20 + '.',
    'F4.1': E20 + ' ("nobody told me", "my impression" were in my version of 18 October).',
    'F4.4': E20 + '.',
    'F5.4': E20 + '.',
    'F5.8': 'His own rewrite of the four parts (13 October) and ' + E20 + '.',
    'F5.9': E20 + '.',
    'F6.1': E20 + ' (my version said "that community should definitely get actual local legal advice").',
    'F6.2': E20 + ' (my version: "Are you mature enough as a community to tell the good from the bad?").',
    'F6.3': 'His ruling "s5-p10-age": he changed 26 to 25 himself.',
    'F6.4': 'His answer 64.5 (24 October) cut "I\'m not saying paid help can\'t be good sometimes, but".',
    'F7.2': 'His answer 64.15 (24 October) cut "Their answers are not a set of commandments ..."; the colleagues joke '
            'left in his edits of 20 October.',
    'F7.4': E20 + ' (my version: "at least one trusted adult, advocate or reporting route they can reach without going '
            'through the community\'s leadership").',
    'F7.6': 'His ruling of 7 October (section 8) cut "that the home community does not control".',
    'F8.1': E20 + ' ("a landlord with a philosophy" was in my version).',
    'F8.2': E20 + '.',
    'F8.3': E20 + '.',
    'F8.4': E20 + ' (my version: "Remember, it\'s not an override unless it can actually work on the person in '
            'question ...").',
    'F8.7': 'His own rewrite of the section (11 October), kept in his edits of 20 October.',
    'F8.9': 'His ruling of 11 October (section 11) cut "The boundary is simple".',
    'F8.11': 'His own rewrite of section 11 (11 October): the floor as it stands is his.',
    'F10.1': E20 + ' (my version had Orlov\'s four things and "From a distance, cohesion ...").',
}
WRONG = {'F2.6': 'My reading was wrong: his ruling of 2 October (section 3, P9) is that he does want people to come in '
                 'largely healed, without pretending they\'re finished.'}
LIGHT = {
    'F1.1': 'his edit of 20 October', 'F1.4': 'his edit of 20 October', 'F1.8': 'his opening of 18 October, which he '
    'checked in Pangram himself', 'F1.11': 'his edit of 20 October', 'F2.1': 'his edit of 20 October',
    'F2.7': 'his edit of 20 October', 'F3.4': 'his own words', 'F3.6': 'his own words', 'F4.2': 'his ruling of 9 '
    'October (section 9)', 'F4.5': 'his edit of 20 October; I can\'t tell his joke\'s point without guessing',
    'F5.1': 'his own words', 'F5.2': 'his edit of 20 October', 'F5.3': 'his own words (13 October)',
    'F5.5': 'his own sentence, written twice (10 and 15 October)', 'F5.7': 'his own words (17 October)',
    'F6.5': 'his own words', 'F6.7': 'his own idiom (6 October)', 'F7.1': 'his own words', 'F9.1': 'his edit of 20 '
    'October'}


def main():
    d = json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))
    disp = {}
    for f in d['findings']:
        i = f['id']
        if i in CARDS:
            disp[i] = ['his', 'On his marking page as %s (review/REVIEW-FULLREAD.md); the post is live, so it changes '
                              'only with his answer.' % CARDS[i]]
        elif i in CUT:
            disp[i] = ['not', 'His cut stays out (E298, E301): ' + CUT[i]]
        elif i in WRONG:
            disp[i] = ['not', WRONG[i]]
        elif i in LIGHT:
            disp[i] = ['not', 'A snag in words he chose (%s) that a reader still gets: it stays as it is.' % LIGHT[i]]
    missing = [f['id'] for f in d['findings'] if f['id'] not in disp]
    assert not missing, missing
    (HERE / 'DISPOSITIONS.json').write_text(json.dumps(disp, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = collections.Counter(v[0] for v in disp.values())
    by = {f['id']: f for f in d['findings']}
    rv = json.loads((HERE / 'review' / 'REVIEW-FULLREAD.json').read_text(encoding='utf-8'))
    lines = [
        '# The community article\'s full read by the lead model (30 October 2026)', '',
        'Joel, 2026-10-30 20:15 UTC, after the hypnosis guide\'s own full read: "i guess we need to go back and re-read '
        'the community article as well after this then". [The plan](%sPLAN.md).' % (BLOB + DIR), '',
        '**What was read.** The live post (`master.md`, "Updated: Oct 25 2026") beside his published version '
        '(`original.md`), in ten parts, sentence by sentence, by me (Claude Opus 5.5, the lead session), never Sonnet '
        '(gate E294): READER-1.md to READER-10.md. `compare_read.py collect` put the %d findings into FINDINGS.json (%s).'
        % (d['summary']['findings'], ', '.join('%d at severity %s' % (v, k) for k, v in sorted(
            d['summary']['by_severity'].items()))), '',
        '**How each was checked.** Before anything went to him, every finding was checked against how its words got '
        'there and, for a lost point, how the point left (gates E298, E301): through my version of 18 October '
        '(`joel-20261025/emulate-check/MY-FINAL-20261018.md`, which `master.md` still was on 21 October), his edits of 20 '
        'October (his and GPT\'s: `joel-20261020/community-final-substack-20261020.html`), the restructure of 23 October '
        '(`joel-20261023/restructure/RECORD.json`), his answers to 64, 65 and 66, and his rulings in `OWNER-EDITS.json` '
        '(as text: `fix-20261017b/faithful/JOEL-CHANGES.md`).', '',
        '**What came of it.** %d findings are cards on [his marking page](https://claude.ai/artifact/QzrX2ZWqtWZdW3WR6ZNq5X) '
        '([its cards as text](%sreview/REVIEW-FULLREAD.md)): the four sentences that a cut of 24 October (64.4, 64.23, '
        '64.24 and 64.25, cuts I advised) left hanging, which is lesson E305; commas and slips; suggestions for his own '
        'words; one fix to my words; and two questions where a sentence of his can be read two ways. %d have no card: '
        '%d are points he cut himself (most of them in his edits of 20 October), which stay out; %d are snags in words '
        'he chose that a reader still gets; and one was my misreading.' % (
            c['his'], BLOB + DIR, c['not'], len(CUT), len(LIGHT)), '',
        '## The points his edits took out (no card; they stay out unless he wants them back)', '',
        'Each was in his published post and in my version of 18 October, and is gone from the live post. If he wants '
        'any back, it goes on a page of its own.', '']
    for i in sorted(CUT, key=lambda x: (int(x[1:].split('.')[0]), int(x.split('.')[1]))):
        f = by[i]
        lines.append('- **%s** (%s): "%s" %s' % (i, f['where'][0] if f['where'] else '', f['published'][:220].strip()
                                                 + ('...' if len(f['published']) > 220 else ''), CUT[i]))
    lines += ['', '## Every finding and its fate', '',
              '| finding | where | kind | severity | fate | why |', '|---|---|---|---|---|---|']
    for f in d['findings']:
        lines.append('| %s | %s | %s | %d | %s | %s |' % (f['id'], (f['where'][0] if f['where'] else '').replace(
            '|', '/'), f['kind'], f['severity'], disp[f['id']][0], disp[f['id']][1].replace('|', '/')))
    lines += ['', '## The cards', '']
    for s in rv['suggestions']:
        lines.append('- %s (%s, %s): %s' % (s['id'], s['spot'], rv['types'][s['type']]['label'],
                                            s.get('what') or s.get('question')))
    lines += ['', 'Made by `make_record.py`; the page by `review/build_page.py` (browser test: `review/BROWSER-TEST.json`, '
              '80 of 82; the two misses are the test\'s "Next undecided" check, which fails the same way on the hypnosis '
              'guide\'s published page: the button scrolls to the next card\'s words, and a long paragraph puts its card '
              'more than 400 px down).']
    (HERE / 'READ.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(dict(c), 'cut', len(CUT), 'light', len(LIGHT), 'wrong', len(WRONG))


if __name__ == '__main__':
    main()
