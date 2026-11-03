#!/usr/bin/env python3
"""Turn 116: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t116.py PR [--test NOTE]   writes the update with the turn's pull request number (or "none"); with --test,
                                     applies it to a copy of NOTE"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parents[1] / 'HANDOFF-UPDATE.json'
S = 'https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq'
BR = 'handoff/claude-dangerous-adult-20260924-1631'
PRN = sys.argv[1]
PRS = ('pull request #%s (https://github.com/u-dont-existDOTcom/joel-articles/pull/%s), still open for him to merge, now with turns 115 and 116' % (PRN, PRN)
       if PRN != 'none' else 'no push yet: the commits wait on the laptop link')
e = re.escape

turn116 = '\n'.join([
    '- TURN 116 (2026-11-03, his message of 2026-11-03 21:00 UTC with his reorganized guide; by %s), the latest; its next step wins over everything below. Branch %s; %s.' % (S, BR, PRS),
    '  - Objective anchor (UDA): main objective, the guide humanized and published, every paragraph and section reading Human with the meaning kept and reading engagingly; this turn\'s contribution, his reorganized guide read whole for flow, late terms, broken pointers and repeats, the suggestions on a marking page, and what his edits teach written up as rules; scope, his words changed only with his OK, no life facts he didn\'t give.',
    '  - His messages: experiments/t116-answers/JOEL-20261103-2100.md ("i think it\'s basically ready to publish unless you have suggestions"; "learn as much as possible from my edits and reorgs"; the shame link\'s new address at 21:25; "yes the links were gone when you sent me the file" at 21:45). His ODT is not in Git (SHA-256 998baaa9...; its pictures include a meme); its text is experiments/t116-joel/JOEL-GUIDE-20261103.md.',
    '  - The comparison: experiments/t116-joel/ (compare.py, EDITS.md: 1,525 sentences of his, 1,031 kept, 219 edited, 275 new; 98 of 378 paragraphs moved), LINKS.md (55 of 67 links gone as bare words, 6 real links left, the rest typed as [words](address)), INDEPENDENT-READ.md (a fresh reader\'s read), LESSONS.md (what his edits teach, each with a rule), URLS-CHECKED.txt (93 addresses opened from the laptop).',
    '  - The cause of the lost links: the turn-115 docx I sent him had no links and no pictures (built from plain text); he did the reorganization in it. Lesson E337 (Inner Child): tools/humanization/file_links_check.py before any file goes to him. Lesson E338 (Inner Child): his edit patterns in docs/FIXING-AN-ARTICLE.md, and tools/humanization/section_refs.py after any reorganization. Tests: tests/test_file_links_and_section_refs.py. The next lesson in either lane is E339.',
    '  - The marking page: experiments/t116-review/ (REVIEW.json, REVIEW.html, build_review.py on GUIDE-PAGE.md, his text with only bold marks and list breaks changed for the page; relink.py and RELINK.md for the links): 44 cards (3 links and pictures, 11 pointers, 4 repeats, 2 second looks, 6 formatting, 9 typo cards with 62 typos, 9 questions). Six cards put a few words of mine into his sentences; experiments/t116-gate/ admitted all six (three fresh readers each, GATE-OUTCOMES.json). The page is published as an artifact with the db capability; his answers save there.',
    '  - Not yet: the master. HUMANIZED-ARTICLE-SO-FAR.md is still the guide as of turn 114; his ODT becomes the new master only with his decisions on the page (AGENTS.md: competing masters need his word). Nothing checked in Pangram this turn.',
    '  - Main had moved on by 93 commits (the hypnosis guide, Nibbana, community lanes, E277 to E336); merged into the lane this turn (docs/HUMANIZATION-GATE.md and state/PANGRAM-SCORECARD.md resolved, the scorecards rebuilt).',
    '  - NEXT: Next step 1.',
])
next1 = ('1. When his answers on the turn-116 marking page come in (the artifact\'s store, or his paste): apply each approved card and '
         'his revisions to his text (experiments/t116-joel/JOEL-GUIDE-20261103.md), put the links back (relink.py\'s plan) and the '
         'seven live-post pictures and videos, fix the French quote marks if he says yes, and make that the new '
         'HUMANIZED-ARTICLE-SO-FAR.md with his OK to make his version the master. Then round 9, the whole guide, in the two '
         'temporary drafts, with file_links_check.py on every file that goes to him. Every turn ends with the whole article '
         'sent and passed to the chat check as --sent (E271 (Inner Child)).')
upd = {
    'turn': '116',
    'replace': [
        [e('TURN 115 (2026-10-26, his message of 2026-10-26 12:24 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 115 (2026-10-26, his message of 2026-10-26 12:24 UTC; by %s), FINISHED.' % S, 1],
        [e('this version is from turn 115 (his message of 2026-10-26 12:24 UTC; pull request #255 (https://github.com/u-dont-existDOTcom/joel-articles/pull/255), for him to merge).'),
         'this version is from turn 116 (his message of 2026-11-03 21:00 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 115 by %s' % S), 'turns 59 to 76 and 100 to 116 by %s' % S, 1],
        [e('  - experiments/t115-answers/ (his message), t115-results/ (round 8 read), t115-pass/ (the pass), t115-gate/ (its reviews and gate), t115-docx/ (the docx) and t115-api/ (its checks) (the latest turn), '),
         '  - experiments/t116-answers/ (his messages), t116-joel/ (his guide, the comparison, the links, the lessons), t116-review/ (the marking page) and t116-gate/ (its six gated cards) (the latest turn), t115-answers/ (his message), t115-results/ (round 8 read), t115-pass/ (the pass), t115-gate/ (its reviews and gate), t115-docx/ (the docx; it had no links) and t115-api/ (its checks), ', 1],
        [r"^1\. When his docx comes back:.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 115 (2026-10-26', turn116],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His answers on the turn-116 marking page (44 cards on his reorganized guide), and his OK to make his version the master.',
            '2. %s' % ('His merge of pull request #%s (turns 115 and 116).' % PRN if PRN != 'none' else 'The push of turn 116, then his merge of its pull request.'),
            '3. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)", still hold round 8; round 9 goes into them after his answers, and his delete comes after round 9 is read.',
            '4. Never in the article: amounts (the 1g, the 7g) and any recipe for what to take instead, including his "ultimate psychedelic recipe" line and its link.',
        ]),
    },
}
OUT.write_text(json.dumps(upd, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('wrote', OUT)
if '--test' in sys.argv:
    sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
    from handoff_note import apply
    note = pathlib.Path(sys.argv[sys.argv.index('--test') + 1]).read_text(encoding='utf-8')
    new, done = apply(note, upd)
    print('\n'.join(done))
    print(len(note), '->', len(new), 'characters')
