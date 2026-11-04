#!/usr/bin/env python3
"""Turn 122: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t122.py PR [--test NOTE]   writes the update with the turn's pull request number; with --test, applies it to
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
PAGE = 'https://claude.ai/artifact/MuvzCwPHsRtrwNVCfQQBfM'
UDA = 'https://github.com/u-dont-existDOTcom/universal-dev-architecture/pull/467'
H = 'https://www.pangram.com/history/'
e = re.escape

turn122 = '\n'.join([
    '- TURN 122 (2026-11-04, his marking-page answers of 13:44 UTC; by %s), the latest; its next step wins over everything below. Branch %s, from main (pull request #288, turns 120 and 121, merged by him at 12:37 UTC); %s.' % (S, BR, PRS),
    '  - His answers (experiments/t122-answers/ANSWERS-20261104-1344.json, his export of the marking page %s): 18 versions of his and 3 kept as they are (M-A15, M-B11, M-B15). HW-1: "i rewrote teh whole section, so remove and replace the whole hearthwork section. it tests human and sounds better"; HW-2 and HW-3: "delete"; M-B13: "this is better, and also edited the prior para, and i want you to delete P5"; M-A11 and M-B5 came with his own checks of the old paragraphs alone, both AI (%s27a73b1c-f15e-4aa9-bf76-3c6d8743cb70, %s3fd8fe60-c398-4650-9472-29ea5b175391), and "my version ... passes".' % (PAGE, H, H),
    '  - Put in word for word (experiments/t122-apply/: apply_t122.py, CHANGES.json): the Hearthwork section is now his heading, "Hearthwork: Taking Turns Lending & Borrowing Adulthood", and his four paragraphs; the links went back on their words (Hearthwork, the Serenity Prayer, the romance guide; 79 links before and after); the Serenity Prayer\'s lines are hard breaks. OWNER-EDITS.json: 16 joel-122-* entries; joel-121-aside superseded, emoji-pass-20261001 and joel-92-20261022 updated where his versions took their strings (supersede_t122.py); 115 pass, 0 failed.',
    '  - His Hearthwork section alone through the API (experiments/t122-check/): Human Written, 0%% AI, one window, Human (High) (%s271b89ee-5c56-40eb-8eed-d910a238b3d5); prediction #379 right.' % H,
    '  - Asked him: three typos in his new text, "Nurterer" (Nurturer) and "the way they keeping" (keep) in the Hearthwork section, "it has become to carry" (has come to carry) in Dating While You Heal; my recommendation, fix all three.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. His answer on the three typos (each fix he approves gets an OWNER-EDITS.json entry). 2. Round 10, the free way: the whole guide '
         'in the two temporary drafts (experiments/t119-substack/make_payloads.py\'s method, the quote marks curled), each draft\'s text checked '
         'on its secret preview link, both opened in his Brave for his extension; then his two result links, each window recorded with its '
         'confidence (E278). 3. Before the post, the word-for-sense read (SKILL.md, tools/humanization/sense_read.py, E331). 4. The publish '
         'draft: his pictures uploaded where the notes say, the post\'s own pictures and videos kept, the Rumi quote as a pull quote, its '
         'quote marks curled the right way before pasting. 5. After he publishes: the Hearthwork article (his paste of 2026-11-04 12:02 UTC, '
         'experiments/t121-answers/), humanized in a lane of its own (its article folder registered, a branch from main), its reparenting '
         'passages brought in line with the reorganized guide. Every turn ends with the whole article sent and passed to the chat check as '
         '--sent (E271 (Inner Child)), rendered with --images for his pictures.')
upd = {
    'turn': '122',
    'replace': [
        [e('TURN 121 (2026-11-04, his message of 12:02 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 121 (2026-11-04, his message of 12:02 UTC; by %s), FINISHED.' % S, 1],
        [r'this version is from turn 121 \(his message of 2026-11-04 12:02 UTC; pull request #\d+ \(https://github\.com/u-dont-existDOTcom/joel-articles/pull/\d+\), open for him to merge \(turns 120 and 121\)\)\.',
         'this version is from turn 122 (his marking-page answers of 2026-11-04 13:44 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 121 by %s' % S), 'turns 59 to 76 and 100 to 122 by %s' % S, 1],
        [e('  - experiments/t121-answers/ (his message and the Hearthwork article\'s HTML), t121-check/ (Hearthwork: Taking Turns checked alone) and t121-review/ (the marking page) (the latest turn), '),
         '  - experiments/t122-answers/ (his marking-page answers), t122-apply/ (his versions put in) and t122-check/ (his Hearthwork section checked) (the latest turn), t121-answers/ (his message and the Hearthwork article\'s HTML), t121-check/ (Hearthwork: Taking Turns checked alone), t121-review/ (the marking page), ', 1],
        [r"^1\. His answers on the marking page \(https://claude\.ai/artifact/MuvzCwPHsRtrwNVCfQQBfM.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 121 (2026-11-04', turn122],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His answer on the three typos in his new text (Nurterer, they keeping, has become to carry); I\'d fix all three.',
            '2. The map lane\'s reset: his merge of UDA pull request #467 (%s), or the map lane\'s resume line with the request (given to him in turn 121), then his merge of that lane\'s pull request that empties the queue.' % UDA,
            '3. His merge of pull request #%s (turn 122).' % PRN,
            '4. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)": round 10 reuses them; deleting them is his.',
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
