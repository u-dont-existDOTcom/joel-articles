#!/usr/bin/env python3
"""Turn 115: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t115.py PR [--test NOTE]   writes the update with the turn's pull request number (or "none"); with --test,
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
PRS = ('pull request #%s (https://github.com/u-dont-existDOTcom/joel-articles/pull/%s), for him to merge' % (PRN, PRN)
       if PRN != 'none' else 'no pull request yet: the laptop dropped off the link before the push, so the commits wait to be pushed')
e = re.escape

turn115 = '\n'.join([
    '- TURN 115 (2026-10-26, his message of 2026-10-26 12:24 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s. He merged pull request #252 (turns 113 and 114).' % (S, BR, PRS),
    '  - Objective anchor (UDA): main objective, the guide humanized, every paragraph and section reading Human with the meaning kept and reading engagingly, like a good public self-help book; this turn\'s contribution, round 8 read, his question about below-High windows answered with lesson E276 (Inner Child), and the one pass he asked for in a docx he can work in; scope, no new claims, no life facts he didn\'t give, his words changed only with his OK.',
    '  - His message: experiments/t115-answers/JOEL-20261026-1224.md (round 8\'s two links; "let\'s start prioritizing working now on spots that are not high confidence human"; "have you been saving those parts?"; "try to get it all high conf human with one more pass, then whatever remains you can just give me as highlighted in a docx").',
    '  - Round 8: experiments/t115-results/ (record_round8.py, ROUND8.md, WINDOWS.md and windows_list.py): both halves Human Written, high (0.37% and 0.21% AI), 4 AI windows (all Low) and 89 more below Human, high; ledger #347 to #359, 12 of 13 right. All four AI windows were on words round 6 read below High, unchanged since. Lesson E276 (Inner Child) in docs/HUMANIZATION-GATE.md; the next lesson in either lane is E277.',
    '  - The pass: experiments/t115-pass/ (fixes.py, CANDIDATE-ARTICLE.md, PASS.md): 12 tell fixes in my paragraphs, 7 cuts and 5 plain rewordings, taking in all 4 AI windows and 7 of the 8 Low ones (the eighth is in his crisis P2); one cut is only a suggestion (C2, which he approved as it is). experiments/t115-gate/: three fresh reviewers passed all 12, the owner-delivery gate admitted the 5 rewordings (GATE-OUTCOMES.json). Nothing installed: the article is as turn 114 left it (sha 3f3d938d6583441d).',
    '  - The docx: experiments/t115-docx/inner-child-spots-round8.docx (build_spec.py, build_docx.js, whose.py): the whole guide as round 8 read it, the pass as tracked changes (one he leaves as it is counts as accepted), every remaining window below High shaded by kind with a comment (its reading, round 6\'s, whose words), Track Changes on.',
    '  - The checks: each changed block through the API, predictions first (experiments/t115-api/, API-CHECKS.md; ledger #360 to #370; laptop results in pangram-api/t115). No checked paragraph reads Low or AI; F01, F02, F05 and F11 read High throughout. F03 needed a second try (its permission clause cut too, reviewed again). F09\'s block timed out ambiguously (pangram-api/t115/cache has its .ambiguous.json): check the account\'s History before resending. The second check of Love Doesn\'t Have to Wait put an AI, Low window on P10\'s "Be careful not to take the accusation ..." (unchanged; High in round 8), marked in the docx for round 9.',
    '  - Main took pull request #254 (the community lane) and the hypnosis guide lane\'s batch 480 while this turn ran; both are merged into the lane. The hypnosis guide lane wrote its own E276 at the same time, so this lane cites "E276 (Inner Child)", and the next lesson in either lane is E277 (docs/HUMANIZATION-GATE.md).',
    '  - NEXT: Next step 1.',
])
next1 = ('1. When his docx '
         'comes back: read its tracked changes and his edits, put in what he accepted (a change he left as it is counts as accepted) '
         'and what he wrote (his words as he wrote them; any new words of mine through tools/humanization/owner_delivery_gate.py), '
         'then round 9, the whole guide, in the two temporary drafts. Every turn ends with the whole article sent and passed to the '
         'chat check as --sent (E271 (Inner Child)); an open question names what it\'s about (E257), and every file named in what '
         'he reads is a link to a page, never a folder (repo_links.py).')
upd = {
    'turn': '115',
    'replace': [
        [e('TURN 114 (2026-10-26, his message of 2026-10-26 00:53 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 114 (2026-10-26, his message of 2026-10-26 00:53 UTC; by %s), FINISHED.' % S, 1],
        [e('this version is from turn 114 (his message of 2026-10-26 00:53 UTC; pull request #252, turns 113 and 114, for him to merge).'),
         'this version is from turn 115 (his message of 2026-10-26 12:24 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 114 by %s' % S), 'turns 59 to 76 and 100 to 115 by %s' % S, 1],
        [e('  - experiments/t114-answers/ (his message and answers), t114-installs/ (the install) and t114-substack/ (round 8) (the latest turn), '),
         '  - experiments/t115-answers/ (his message), t115-results/ (round 8 read), t115-pass/ (the pass), t115-gate/ (its reviews and gate), t115-docx/ (the docx) and t115-api/ (its checks) (the latest turn), t114-answers/ (his message and answers), t114-installs/ (the install) and t114-substack/ (round 8), ', 1],
        [r"^1\. Round 8's two result links when he sends them:.*$", next1, 1],
        [e('The next lesson in either lane is E276 (the community lane\'s turn took E272 to E274 while this one ran, and the hypnosis guide lane its own E275, so this one is cited as "E275 (Inner Child)").'),
         'The next lesson in either lane is E277 (the community lane\'s turn took E272 to E274 while this one ran, the hypnosis guide lane its own E275, so this one is cited as "E275 (Inner Child)", and both lanes took E276 at the same time in turn 115, this one cited as "E276 (Inner Child)").', 1],
    ],
    'insert_before': [
        ['- TURN 114 (2026-10-26', turn115],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His docx back (experiments/t115-docx/inner-child-spots-round8.docx): the pass decided, his shaded spots worked on.',
            '2. %s' % ('His merge of pull request #%s (turn 115).' % PRN if PRN != 'none' else 'The push of turn 115, then his merge of its pull request.'),
            '3. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)", still hold round 8; round 9 goes into them after his docx, and his delete comes after round 9 is read.',
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
