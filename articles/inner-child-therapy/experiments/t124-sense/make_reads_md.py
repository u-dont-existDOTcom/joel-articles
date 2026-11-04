#!/usr/bin/env python3
"""Turn 124: READS.md, the record of the word-for-sense read (E331; SKILL.md step 5: "Record each finding's fate and the
recall with the article"): the scores of both passes, the non-word net, and every finding with whose words it is and its
fate (a card on the marking page, a line of his keep-as-is list, or not a real finding, with why).
  python3 articles/inner-child-therapy/experiments/t124-sense/make_reads_md.py"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
P1 = json.loads((HERE / 'pass1' / 'SCORE.json').read_text(encoding='utf-8'))
P2 = json.loads((HERE / 'SCORE.json').read_text(encoding='utf-8'))
CAN = json.loads((HERE / 'CANARIES.json').read_text(encoding='utf-8'))
CARDS = {c['cid']: c for c in json.loads((HERE / 'CARDS.json').read_text(encoding='utf-8'))}
META = json.loads((HERE / 'META.json').read_text(encoding='utf-8'))
PAGE = 'https://claude.ai/artifact/RKJUWjR4MRCyRkpTqfDoZA'
NOT_CARDS = [   # (block, readers, whose, the words, fate, why)
    (8, 'part 1', 'his guide', 'like another ex of mine (X)', 'kept: KEEP-AS-IS.json K4',
     'his turn-116 card A1: two exes are X on purpose, so nobody takes the unnamed one for Key'),
    (105, 'part 1', 'his guide', '"What\'s a \'boundary\'?", I might be asking.', 'kept: KEEP-AS-IS.json K2',
     'his turn-116 card A3: "I", not "you": he is learning this too'),
    (506, 'part 3 (both readers)', 'his guide', "Below are the differences between Lucia's approach and my guide's approach:",
     'not real', 'the list is his picture right after it ("How This Reparenting Guide Differs From: Lucia Capacchione"), which the parts leave out'),
    (518, 'part 3 (both readers)', 'his guide', 'Anthony de Mello) is an excellent example', 'not real: a tool bug, fixed',
     'the link\'s address holds brackets (Anthony_de_Mello_(Jesuit_priest)), and suggestion_review.py cut it at the first one, so the parts showed a stray bracket; the post never had it (CHECK-B.txt). Fixed this turn (LINK; tests/test_suggestion_review.py), with a link inside emphasis, which showed its markup'),
    (19, 'part 1 (notes)', 'his guide', 'the five stages list', 'not real', 'the list\'s first item is "1." in the article; the part file shows list items without their numbers'),
    (377, 'part 3 (notes)', 'his guide', 'Yep. Exactly like that.', 'not real', 'it answers the drawing just above it (an IMAGE note the parts leave out)'),
    (405, 'part 3, second reader (notes)', 'his guide', 'a double space before "It can help"', 'left', 'a double space doesn\'t show in the post'),
    (157, 'part 1 (notes)', 'his guide', 'tuberculosis from a cave', 'kept', 'his own history'),
]


def score_rows(sc, label):
    out = []
    for r in sc['parts']:
        miss = '; missed: ' + ', '.join('"%s" for "%s" (block %d)' % (m['planted'], m['original'], m['block']) for m in r['missed']) if r['missed'] else ''
        out.append('| %s | %d | %d-%d | %d of %d | %d of %d%s | %d |' % (label, r['part'], r['blocks'][0], r['blocks'][1], r['read'],
                                                                         r['expected'], r['found'], r['planted'], miss, r['findings']))
    return out


md = ['# The word-for-sense read of the guide (turn 124)', '',
      'Gate E331 (SKILL.md, "Word-for-sense read before publication"), on HUMANIZED-ARTICLE-SO-FAR.md %s (%d blocks, %d words): '
      'tools/humanization/sense_read.py make, %d parts, %d planted errors in each (seed %d), the brief with this guide\'s own '
      'style notes (STYLE.md). One fresh reader per part, given only its task line; the planted list (CANARIES.json) was out of '
      'the folder while they read. Part 3\'s first reader missed one planted error, so a second fresh reader read it again '
      '(pass1/ keeps the first reader\'s read and scores).' % (META['master_sha256'][:12], META['blocks'], META['words'],
                                                               META['parts'], META['plant_per_part'], META['seed']), '',
      '| Pass | Part | Blocks | Read | Planted errors found | Findings |', '|---|---|---|---|---|---|']
md += score_rows(P1, 'first')
md += [r for r in score_rows(P2, 'second') if r.startswith('| second | 3 |')]
md += ['', 'Recall: 8 of 9. Both readers of part 3 missed the same one, "wealth" where "warmth" belonged, in a list of what to '
       'picture ("wealth, protection, steadiness, rest"), where the planted word fits the sentence; so in part 3 the readers\' '
       'silence counts for a little less. The planted errors:', '']
md += ['- part %d, block %d: "%s" for "%s"' % (c['part'], c['block'], c['planted'], c['original']) for c in CAN]
md += ['', 'Under the read, the non-word net (sense_read.py nonwords, NONWORDS.json): 96 tokens a dictionary doesn\'t know; 95 '
       'are names, terms, or his own words and spellings, every one in his guide, and one is a link address. Nothing to fix.', '',
       '## Every finding, and its fate', '',
       'The cards are on the marking page (%s; REVIEW.json, REVIEW.html, built by build_sense_page.py from CARDS.json). Every '
       'finding is in his own words (his reorganized guide of 2026-11-03), so none is changed without him.' % PAGE, '',
       '| Card | Kind | Found by | The words | Suggested | Why |', '|---|---|---|---|---|---|']
for cid in sorted(CARDS, key=lambda k: int(''.join(ch for ch in k.split('-')[1] if ch.isdigit()))):
    c = CARDS[cid]
    if c['kind'] == 'fix':
        sug = '"%s"' % c['new'] + (''.join('; "%s"' % x[1] for x in c.get('extra', [])))
        words = '"%s"' % c['old'] + (''.join('; "%s"' % x[0] for x in c.get('extra', [])))
        kind = c['typ']
    elif c['kind'] == 'leave':
        sug, words, kind = 'leave it (the reader: "%s")' % c['reader_new'], '"%s"' % c['quote'], 'leave'
    else:
        sug, words, kind = c['question'], '"%s"' % c['quote'], 'ask'
    md.append('| %s | %s | %s | %s | %s | %s |' % (cid, kind, ', '.join('reader %d' % r for r in c['readers']), words.replace('|', '/'),
                                                 sug.replace('|', '/'), c.get('why', c.get('reader_said', '')).replace('|', '/')))
md += ['', '(Readers: 1 and 2 read parts 1 and 2; 3 and 4 are the first and second readers of part 3.)', '',
       '## Findings that aren\'t cards', '', '| Block | Found by | Whose words | The words | Fate | Why |', '|---|---|---|---|---|---|']
md += ['| %d | %s | %s | %s | %s | %s |' % row for row in NOT_CARDS]
(HERE / 'READS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print('READS.md', len(CARDS), 'cards,', len(NOT_CARDS), 'other findings')
