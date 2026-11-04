#!/usr/bin/env python3
"""Turn 119: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
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

turn119 = '\n'.join([
    '- TURN 119 (2026-11-04, his messages of 00:51 and 00:56 UTC; by %s), the latest; its next step wins over everything below. Branch %s, from main (pull request #284, turn 118, merged by him at 00:51 UTC); %s.' % (S, BR, PRS),
    '  - His messages: "go ahead" (00:51, round 9), and at 00:56 "make sure you check the lane bc you were sent some things to put into the guide, but i think i already put them in if they were important points".',
    '  - Round 9: experiments/t119-substack/ (make_payloads.py, PAYLOAD-A/B.html, TEXT-A/B.txt, PASTED.json). The guide whole in the two temporary drafts, A (Understanding Reparenting to Discovering and Healing Old Patterns, 16,668 words) and B (When the Practice Gets Difficult to the appendix, 11,799); the payloads carry their quote marks curled the right way, because Substack curls straight ones on paste and three wrongly after an opening bracket (the first paste of A showed them; docs/HUMANIZATION-GATE.md now says so beside the standard swap). Each draft\'s text checked on its secret preview link (A: one no-break space shown as a space; B exact). Both links opened in his Brave through Claude in Chrome, his extension labeled each "Human" and the full analysis was started; those result pages open outside the session\'s tabs, so their links come from him. Predictions t119s-A#373 and t119s-B#374 (both AI, 0.30 and 0.35).',
    '  - The queue: the InnerSignal map\'s authoring/PENDING-PUBLIC-GUIDE-CHANGES.md (innerSignalGraph, read-only from here), PGQ-018 to PGQ-055, read against his guide (experiments/t119-queue/QUEUE-COVERAGE.md): 15 in, 18 with their core point in his words, 2 not in (PGQ-054 drawing or scribbling anger, which I\'d add as a line or two under Journal With Each Hand; PGQ-036 hypnosis during grief, which I\'d leave out). GUIDE-UPDATE-QUEUE-20261006.md points to it.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. Round 9\'s results: his two result links (pangram.com/feed/...) from the full analyses his extension opened; record each window with '
         'its confidence (E278) against TEXT-A.txt and TEXT-B.txt (substack_check_text.py result), and the windows that read AI or below '
         'High go to him on a marking page, his words first, with KEEP-AS-IS.json read before any card. His answer on PGQ-054 and PGQ-036. '
         'Then the publish draft: his pictures uploaded where the notes say, the post\'s own pictures and videos kept, the Rumi quote as a '
         'pull quote, its quote marks curled the right way before pasting. Every turn ends with the whole article sent and passed to the '
         'chat check as --sent (E271 (Inner Child)), rendered with --images for his pictures.')
upd = {
    'turn': '119',
    'replace': [
        [e('TURN 118 (2026-11-04, his message of 2026-11-04 00:43 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 118 (2026-11-04, his message of 2026-11-04 00:43 UTC; by %s), FINISHED.' % S, 1],
        [r'this version is from turn 118 \(his message of 2026-11-04 00:43 UTC; pull request #\d+ \(https://github\.com/u-dont-existDOTcom/joel-articles/pull/\d+\), open for him to merge\)\.',
         'this version is from turn 119 (his messages of 2026-11-04 00:51 and 00:56 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 118 by %s' % S), 'turns 59 to 76 and 100 to 119 by %s' % S, 1],
        [e('  - experiments/t118-answers/ (his message) and t118-apply/ (the four pairs back) (the latest turn), '),
         '  - experiments/t119-substack/ (round 9) and t119-queue/ (the map\'s queue checked) (the latest turn), t118-answers/ (his message), t118-apply/ (the four pairs back), ', 1],
        [r"^1\. Round 9: the whole guide as it is now.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 118 (2026-11-04', turn119],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His two round-9 result links (pangram.com/feed/...), from the full analyses his extension opened in his Brave.',
            '2. His answer on the two queue items not in his guide: PGQ-054 (drawing or scribbling anger; I\'d add a line or two of his under Journal With Each Hand) and PGQ-036 (hypnosis during grief; I\'d leave it out).',
            '3. %s' % ('His merge of pull request #%s (turn 119).' % PRN if PRN != 'none' else 'The push of turn 119, then his merge of its pull request.'),
            '4. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)", hold round 9; his delete comes after round 9 is read.',
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
