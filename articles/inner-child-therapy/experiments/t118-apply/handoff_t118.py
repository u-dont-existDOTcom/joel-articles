#!/usr/bin/env python3
"""Turn 118: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t118.py PR [--test NOTE]   writes the update with the turn's pull request number (or "none"); with --test,
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
PRS = ('pull request #%s (https://github.com/u-dont-existDOTcom/joel-articles/pull/%s), open for him to merge' % (PRN, PRN)
       if PRN != 'none' else 'no push yet: the commits wait on the laptop link')
e = re.escape

turn118 = '\n'.join([
    '- TURN 118 (2026-11-04, his message of 2026-11-04 00:43 UTC; by %s), the latest; its next step wins over everything below. Branch %s, from main (pull request #283, turn 117, merged by him at 00:39 UTC); %s.' % (S, BR, PRS),
    '  - His message: experiments/t118-answers/JOEL-20261104-0043.md ("all good, and i guess you should restore the four pairs i dleeted then i didn\'t realize they wer eimportant for that part"). "all good" answers the rest of turn 117, the calls I listed included.',
    '  - Done: the four pairs back under Four Pairs That Commonly Hook the Child, in his words from the last guide (experiments/t118-apply/apply_t118.py); KEEP-AS-IS.json lost the meant cut X2 and gained K18 (no pass cuts them as a repeat again); OWNER-EDITS.json gained joel-118-four-pairs (98 pass, 0 failed). apply_t117.py no longer installs over a later article, and verify_t117.py accepts the pairs\' return.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. Round 9: the whole guide as it is now in the two temporary Substack drafts ("Inner Child, draft A (temp, delete after)" '
         'and "Inner Child, draft B (temp, delete after)", split at an h1), each sent as its secret preview link in the paid '
         'subscriber view for his Pangram extension (gate E277), every window recorded with its confidence (E278); the AI '
         'windows and the ones below High go to him on a marking page, his words first, with KEEP-AS-IS.json read before any '
         'card. Then the publish draft: his pictures uploaded where the notes say, the post\'s own pictures and videos kept, the '
         'Rumi quote as a pull quote. Every turn ends with the whole article sent and passed to the chat check as --sent '
         '(E271 (Inner Child)), rendered with --images for his pictures.')
upd = {
    'turn': '118',
    'replace': [
        [e('TURN 117 (2026-11-03, his answers exported from the turn-116 marking page at 23:32 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 117 (2026-11-03, his answers exported from the turn-116 marking page at 23:32 UTC; by %s), FINISHED.' % S, 1],
        [r'this version is from turn 117 \(his answers of 2026-11-03 23:32 UTC; pull request #\d+ \(https://github\.com/u-dont-existDOTcom/joel-articles/pull/\d+\), open for him to merge\)\.',
         'this version is from turn 118 (his message of 2026-11-04 00:43 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 117 by %s' % S), 'turns 59 to 76 and 100 to 118 by %s' % S, 1],
        [e('  - experiments/t117-answers/ (his answers) and t117-apply/ (the build, the checks, DECISIONS.md) (the latest turn), '),
         '  - experiments/t118-answers/ (his message) and t118-apply/ (the four pairs back) (the latest turn), t117-answers/ (his answers), t117-apply/ (the build, the checks, DECISIONS.md), ', 1],
        [r"^1\. Round 9: the whole guide as it is now.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 117 (2026-11-03', turn118],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. %s' % ('His merge of pull request #%s (turn 118).' % PRN if PRN != 'none' else 'The push of turn 118, then his merge of its pull request.'),
            '2. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)", still hold round 8; round 9 goes into them next, and his delete comes after round 9 is read.',
            '3. Never in the article: amounts (the 1g, the 7g) and any recipe for what to take instead, including his "ultimate psychedelic recipe" line and its link.',
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
