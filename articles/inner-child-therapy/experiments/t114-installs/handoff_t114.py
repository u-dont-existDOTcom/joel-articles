#!/usr/bin/env python3
"""Turn 114: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t114.py [--test NOTE]   writes the update; with --test, applies it to a copy of NOTE"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parents[1] / 'HANDOFF-UPDATE.json'
S = 'https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq'
BR = 'handoff/claude-dangerous-adult-20260924-1631'
PRS = 'pull request #252 (https://github.com/u-dont-existDOTcom/joel-articles/pull/252)'
e = re.escape

turn114 = '\n'.join([
    '- TURN 114 (2026-10-26, his message of 2026-10-26 00:53 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s, which now holds turns 113 and 114, for him to merge.' % (S, BR, PRS),
    '  - Objective anchor (UDA): main objective, the guide humanized, every paragraph and section reading Human with the meaning kept and reading engagingly, like a good public self-help book; this turn\'s contribution, his approved review sheet installed word for word and the installed guide in the two drafts for the whole-guide check (round 8); scope, no new claims, no life facts he didn\'t give, his words changed only with his OK.',
    '  - His message: experiments/t114-answers/JOEL-20261026-0053.md ("oh yeah i didn\'t need gpt that was easy, it\'s way easier to read now"), with his answers, experiments/t114-answers/ANSWERS-20261026-0052.json: all eleven cards approved, Q-me answered "you". GPT\'s review: not needed, as he said.',
    '  - The install: experiments/t114-installs/apply_t114.py replaces each old paragraph in place by what it became (every turn note stays above its paragraph, one turn-114 note above each section\'s first changed paragraph); its check is that the article without its notes is experiments/t113-shape/PROPOSAL-ARTICLE.md with his "you". OWNER-EDITS.json: entry joel-114-20261026 (the 36 heading lines with their levels, the paragraphs the splits start, the moved sentence, 109 A, "you"), and the fifteen older entries whose strings his cards changed now hold the current strings, each with a history line; 188 of 188 pass.',
    '  - Round 8: experiments/t114-substack/ (make_payloads.py, make_items.py; ITEMS.json; predictions #347 to #359, batch t114-substack, written before the paste), pasted into both drafts at commit 93be1ee7 (PASTED.json: A 14,987 words, matching; B 12,644, the note embed\'s 100 words over TEXT-B.txt, as in rounds 3 to 7).',
    '  - Main took two more pull requests while turns 113 and 114 ran (#251 and #253, the community and hypnosis guide lanes); both are merged into the lane. The hypnosis guide lane wrote its own E275 at the same time as this lane\'s, so this lane cites "E275 (Inner Child)", and the next lesson in either lane is E276 (docs/HUMANIZATION-GATE.md).',
    '  - NEXT: Next step 1.',
])
next1 = ('1. Round 8\'s two result links when he sends them: read each feed page\'s windows as experiments/t108-results/record_round6.py '
         'does (items in experiments/t114-substack/ITEMS.json), record and score them, and fix what a window shows (a diagnosed '
         'draft through tools/humanization/owner_delivery_gate.py, up to six diagnosed tries per paragraph lineage). Then '
         'Untangling the Belonging Bargains P1\'s own fix. Every turn ends with the whole article sent and passed to the chat '
         'check as --sent (E271 (Inner Child)); an open question names what it\'s about (E257), and every file named in what he '
         'reads is a link to a page, never a folder (repo_links.py).')
upd = {
    'turn': '114',
    'replace': [
        [e('TURN 113 (2026-10-25, his message of 2026-10-25 22:38 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s for him to merge.' % (S, BR, PRS)),
         'TURN 113 (2026-10-25, his message of 2026-10-25 22:38 UTC; by %s), FINISHED. Branch %s; %s (turns 113 and 114).' % (S, BR, PRS), 1],
        [e('this version is from turn 113 (his message of 2026-10-25 22:38 UTC; pull request #252 for him to merge).'),
         'this version is from turn 114 (his message of 2026-10-26 00:53 UTC; pull request #252, turns 113 and 114, for him to merge).', 1],
        [e('turns 59 to 76 and 100 to 113 by %s' % S), 'turns 59 to 76 and 100 to 114 by %s' % S, 1],
        [e('  - experiments/t113-answers/ (his message), t113-shape/ (the proposals and the cold read), '),
         '  - experiments/t114-answers/ (his message and answers), t114-installs/ (the install) and t114-substack/ (round 8) (the latest turn), t113-answers/ (his message), t113-shape/ (the proposals and the cold read), ', 1],
        [r"^1\. GPT's review of the turn-113 sheet, when he pastes it.*$", next1, 1],
        [e('The next lesson in either lane is E276 (the community lane\'s turn took E272 to E274 while this one ran).'),
         'The next lesson in either lane is E276 (the community lane\'s turn took E272 to E274 while this one ran, and the hypnosis guide lane its own E275, so this one is cited as "E275 (Inner Child)").', 1],
    ],
    'insert_before': [
        ['- TURN 113 (2026-10-25', turn114],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. Round 8\'s two result links: draft A\'s and draft B\'s Pangram feed pages (question page to-do, turn 114).',
            '2. His merge of pull request #252 (turns 113 and 114).',
            '3. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)", hold round 8, the guide as installed; his delete comes after round 8 is read.',
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
