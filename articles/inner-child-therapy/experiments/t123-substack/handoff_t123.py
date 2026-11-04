#!/usr/bin/env python3
"""Turn 123: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t123.py PR [--test NOTE]   writes the update with the turn's pull request number; with --test, applies it to
                                     a copy of NOTE"""
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
PRS = 'pull request #%s (https://github.com/u-dont-existDOTcom/joel-articles/pull/%s), open for him to merge' % (PRN, PRN)
UDA = 'https://github.com/u-dont-existDOTcom/universal-dev-architecture/pull/467'
e = re.escape

turn123 = '\n'.join([
    '- TURN 123 (2026-11-04, his message of 14:27 UTC; by %s), the latest; its next step wins over everything below. Branch %s, from main (pull request #292, turn 122, merged by him at 14:27 UTC); %s.' % (S, BR, PRS),
    '  - His message (experiments/t123-answers/JOEL-20261104-1427.md), answering turn 122\'s question on the three typos in his new text: "yes fix the typos".',
    '  - Fixed: "Nurterer" to "Nurturer" and "the way they keeping" to "the way they keep" in his Hearthwork section, "has become to carry" to "has come to carry" in Dating While You Heal (OWNER-EDITS.json joel-123-typos; 116 pass, 0 failed).',
    '  - Round 10, the free way (experiments/t123-substack/: make_payloads.py, turn 119\'s method with the quote marks curled; PAYLOADS.json; PASTED.json): A, Understanding Reparenting to Discovering and Healing Old Patterns, 16,708 words; B, When the Practice Gets Difficult to the appendix, 11,889; predictions t123s-A#380 and t123s-B#381 before the paste. Pasted into the two temporary drafts (saved 14:31 and 14:32 UTC), each word count the payload\'s before and after a reload; on the secret preview links, A\'s 226 lines all as CHECK-A.txt but line 78 (the no-break space of "Breadcrumbing is" shown as a plain space, as in round 9), B\'s 163 lines exactly CHECK-B.txt. Both links opened in his Brave through Claude in Chrome: his extension labeled each "Human" (its label, not the result) and its full analysis was clicked; those open outside the session\'s tab group, so the result links (pangram.com/feed/...) are his to send. The secret links went to him in chat only, never into Git.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. His two round-10 result links (pangram.com/feed/...): each window recorded with its confidence (E278), predictions #380 '
         'and #381 scored (tools/humanization/pangram_ledger.py result; 81% AI counts as Mixed), the scorecards rebuilt. A window that '
         'reads AI is narrowed to its paragraphs through the API first (E343; a paragraph that has read AI twice goes to the tell panel, '
         'E346); then the windows go on a marking page for him, the Low ones first (his turn-121 answer: "i do want to work on the low '
         'windows especially, medium ones i can look at altho i might not bother changing"). 2. Before the post, the word-for-sense read '
         '(SKILL.md, tools/humanization/sense_read.py, E331). 3. The publish draft: his pictures uploaded where the notes say, the '
         'post\'s own pictures and videos kept, the Rumi quote as a pull quote, its quote marks curled the right way before pasting. '
         '4. After he publishes: the Hearthwork article (his paste of 2026-11-04 12:02 UTC, experiments/t121-answers/), humanized in a '
         'lane of its own (its article folder registered, a branch from main), its reparenting passages brought in line with the '
         'reorganized guide. Every turn ends with the whole article sent and passed to the chat check as --sent (E271 (Inner Child)), '
         'rendered with --images for his pictures.')
upd = {
    'turn': '123',
    'replace': [
        [e('TURN 122 (2026-11-04, his marking-page answers of 13:44 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 122 (2026-11-04, his marking-page answers of 13:44 UTC; by %s), FINISHED.' % S, 1],
        [r'this version is from turn 122 \(his marking-page answers of 2026-11-04 13:44 UTC; pull request #\d+ \(https://github\.com/u-dont-existDOTcom/joel-articles/pull/\d+\), open for him to merge\)\.',
         'this version is from turn 123 (his message of 2026-11-04 14:27 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 122 by %s' % S), 'turns 59 to 76 and 100 to 123 by %s' % S, 1],
        [e('  - experiments/t122-answers/ (his marking-page answers), t122-apply/ (his versions put in) and t122-check/ (his Hearthwork section checked) (the latest turn), '),
         '  - experiments/t123-answers/ (his message) and t123-substack/ (round 10: the payloads and the paste) (the latest turn), t122-answers/ (his marking-page answers), t122-apply/ (his versions put in), t122-check/ (his Hearthwork section checked), ', 1],
        [r"^1\. His answer on the three typos \(each fix he approves gets an OWNER-EDITS\.json entry\)\. 2\. Round 10, the free way.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 122 (2026-11-04', turn123],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His two round-10 result links (pangram.com/feed/...), from the full-analysis tabs his extension opened in Brave (the two secret preview links went to him in chat in turn 123, in case those tabs are gone).',
            '2. The map lane\'s reset: his merge of UDA pull request #467 (%s), or the map lane\'s resume line with the request (given to him in turn 121), then his merge of that lane\'s pull request that empties the queue.' % UDA,
            '3. His merge of pull request #%s (turn 123).' % PRN,
            '4. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)": round 10 is in them; deleting them is his.',
            '5. Never in the article: amounts (the 1g, the 7g) and any recipe for what to take instead, including his "ultimate psychedelic recipe" line and its link.',
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
    out = sys.argv[sys.argv.index('--test') + 2] if len(sys.argv) > sys.argv.index('--test') + 2 else None
    if out:
        pathlib.Path(out).write_text(new, encoding='utf-8')
