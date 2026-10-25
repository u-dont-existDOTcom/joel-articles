#!/usr/bin/env python3
"""Turn 111: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t111.py [--test NOTE]   writes the update; with --test, applies it to a copy of NOTE"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parents[1] / 'HANDOFF-UPDATE.json'
S = 'https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq'
BR = 'handoff/claude-dangerous-adult-20260924-1631'
PRS = 'the lane\'s open pull request (https://github.com/u-dont-existDOTcom/joel-articles/pulls?q=is%3Apr+is%3Aopen+head%3Ahandoff%2Fclaude-dangerous-adult-20260924-1631)'
OLDPR = 'pull request #246 (https://github.com/u-dont-existDOTcom/joel-articles/pull/246)'
e = re.escape

turn111 = '\n'.join([
    '- TURN 111 (2026-10-25, his answers of 2026-10-25 20:08 UTC and his question of 20:14 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s for him to merge.' % (S, BR, PRS),
    '  - Objective anchor (UDA): main objective, the guide humanized, every paragraph and section reading Human with the meaning kept and reading engagingly, like a good public self-help book; this turn\'s contribution, his decisions from the review sheet put in word for word and checked, his question about the reshape answered, and two lines he called out traced; scope, no new claims, no life facts he didn\'t give, his words changed only with his OK.',
    '  - His message: experiments/t111-answers/JOEL-20261025-2014.md ("you gave up on reshaping everything for easier reading with exercise first and then caveats after? was that because gpt disagreed?"; answered in chat: no, GPT agreed with the shape and objected only to two lines the reshape had separated from what they belong to; the next five sections come as proposals first) and his answers, experiments/t111-answers/ANSWERS-20261025-2008.json.',
    '  - Installed (experiments/t111-installs/apply_t111.py; owner_edits_t111.py, OWNER-EDITS joel-111-20261025, 186 of 186 pass): S1 Hear the Guard First in the agreed order; S3 in his version ("So I\'d ask this person"); cuts C3 to C9, C11, C12; C10 kept, with his added sentence ("If it\'s more distributed ...") and his cut of "Say they\'re the one who always remembers your appointments."; P2 and P5; Just Like Me P2 his sentence (the tonglen link kept) and his cut of "Some of them make it worse ... 😅" in P1; Q1 his "Once a truce is made, we can begin to let down our defenses."; Q2 and Q3 answered with their basis ("people i know"; Re-evaluation Counseling and common therapy advice), no text change.',
    '  - Traced (experiments/t111-answers/TRACES.md): the stray line was my turn-65 narration of his guide\'s said-aloud wish with a fragment and an emoji; "I\'d leave out forgiving them" was the guide\'s "This is not a demand to forgive an abuser ..." turned into "leave it out" by turn 93\'s tell fix (E268 (Inner Child)).',
    '  - API checks (experiments/t111-api/API-CHECKS.md, batches t111-api-1 and -2, ledger #310 to #325, 16 checks, 14 right): 12 of the 14 changed paragraphs of 50 words or more Human alone. Borrow Love P3 read 100% AI alone after its approved cut and Human with the line (question 108.1, my pick: put it back). Untangling the Belonging Bargains P1 reads AI alone with and without its cut (Human in context in round 6), so it is queued for its own fix. Hear the Guard First is the text checked as t110_sec_guard_b; the sections come in round 7.',
    '  - Lessons: E268 (Inner Child), a tell fix keeps what the sentence claims; E269 (Inner Child), a line of what someone is worth to the reader can be his point, and a repeat can sit across a paragraph break (the point-of-view brief updated); E270 (Inner Child), an approved cut is checked alone, and when it turns the paragraph AI the line goes back to him with both checks. The next lesson in either lane is E271.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. His answers to question 108 on OWNER-QUESTIONS.md (108.1, Borrow Love\'s life\'s-journey line, my pick A: put it back, '
         'from experiments/t111-answers/ANSWERS-20261025-2008.json\'s C4 "before"; 108.2, Just Like Me P2, my pick A: keep his '
         'sentence alone). Then round 7, the whole-article check, in the two temporary drafts (paste with '
         'experiments/t88-substack/paste_payload_lane.js; he sends the result links; read them as experiments/t108-results/record_round6.py '
         'does): it is the section check for every section turns 110 and 111 changed. Then Untangling the Belonging Bargains P1\'s own fix '
         '(a diagnosed draft through tools/humanization/owner_delivery_gate.py, then to him on a suggestion_review.py page), and the next '
         'reshape batch as proposals on a page before anything moves (How to Forgive Without Forgetting, How Much Happiness Do You Know Is '
         'Possible?, Borrow One Competency at a Time, Differentiation; The Parent You Inherited only with his OK). An open question names '
         'what it\'s about (E257), and every file named in what he reads is a link to a page, never a folder (repo_links.py).')
upd = {
    'turn': '111',
    'replace': [
        [e('TURN 110 (2026-10-25, his message of 2026-10-25 17:26 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s for him to merge, which turn 110 pushed to as well.' % (S, BR, OLDPR)),
         'TURN 110 (2026-10-25, his message of 2026-10-25 17:26 UTC; by %s), FINISHED. Branch %s; %s, merged.' % (S, BR, OLDPR), 1],
        [e('this version is from turn 110 (his message of 2026-10-25 17:26 UTC; pull request #246 for him to merge).'),
         'this version is from turn 111 (his answers of 2026-10-25 20:08 UTC; the turn-111 pull request for him to merge).', 1],
        [e('turns 59 to 76 and 100 to 110 by %s' % S), 'turns 59 to 76 and 100 to 111 by %s' % S, 1],
        [e('  - experiments/t110-answers/ (his message and GPT\'s review), t110-review/ (the agreement, the cold read and his review sheet), t110-installs/ and t110-api/ (the latest turn), '),
         '  - experiments/t111-answers/ (his message, his answers and the traces), t111-installs/ and t111-api/ (the latest turn), t110-answers/ (his message and GPT\'s review), t110-review/ (the agreement, the cold read and his review sheet), t110-gate/ (the owner-delivery gate), t110-installs/ and t110-api/ (turn 110), ', 1],
        [r"^1\. His answers from the review sheet \(question 107 on OWNER-QUESTIONS\.md;.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 110 (2026-10-25', turn111],
        ['- A link goes to a page he can read, never to a folder',
         '- A tell fix says the same claim with the same force ("not required" never becomes "leave it out"), checked against the guide\'s own sentence (E268 (Inner Child), turn 111).\n'
         '- The omission test reads across the paragraph break, and a line of what someone is worth to the reader can be his point (E269 (Inner Child), turn 111).\n'
         '- An approved cut is checked alone like any change; when it turns the paragraph AI, the line goes back to him with both checks (E270 (Inner Child), turn 111).'],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His answers to question 108 on OWNER-QUESTIONS.md: Borrow Love\'s line (my pick: put it back) and Just Like Me\'s second paragraph (my pick: his sentence alone).',
            '2. His merge of the turn-111 pull request.',
            '3. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)", stay for round 7; his delete comes after its results.',
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
