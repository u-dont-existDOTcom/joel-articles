#!/usr/bin/env python3
"""Turn 107: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t107.py [--test NOTE]   writes the update; with --test, applies it to a copy of NOTE and prints what changed"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parents[1] / 'HANDOFF-UPDATE.json'
S = 'https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq'
BR = 'handoff/claude-dangerous-adult-20260924-1631'
PR = 'pull request #239 (https://github.com/u-dont-existDOTcom/joel-articles/pull/239)'
e = re.escape

turn107 = '\n'.join([
    '- TURN 107 (2026-10-25, his answers of 2026-10-25 00:24 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s for him to merge.' % (S, BR, PR),
    '  - Objective anchor (UDA): main objective, the guide humanized, every paragraph and section reading Human with the meaning kept and reading engagingly, like a good public self-help book; this turn\'s contribution, his own My Journey and Not Every Hero Wears A Cape P1 to P3, question 103 decided, lesson E261 (Inner Child), the repo_links.py check, and round 6 pasted; scope, no new claims, no life facts he didn\'t give, his words changed only with his OK.',
    '  - His answers: experiments/t107-answers/JOEL-20261025-0024.md: "103a oh i had not read that whole section, it looks still a little ai, and you put in some of my things too verbatim. here\'s the fixed, fully green section"; "103.2 i fixed the section, it\'s all dark green now"; "103.3 a" (his acacia sentence stays: "people can read it how they want"); "103.4 a"; "i have no idea where the 3 files are that i\'m supposed to read".',
    '  - In (experiments/t107-installs/apply_t107.py and owner_edits_t107.py; entries joel-107-20261025-sections and -103; owner edits 183 of 183): his My Journey (bypassing paragraph second), his Not Every Hero P1 to P3 (Make It Intentional stays), "if progress" for "if it progress". His paste was plain text, so the links and the two italic words went back on the same words, and each of his lines is its own paragraph.',
    '  - Lessons: E261 (Inner Child): three of the lines he rewrote were his chat answers I had put in close to as typed (turns 43, 45, 79); an answer that explains something goes in as article sentences, shown beside his words (docs/HUMANIZATION-GATE.md, docs/FIXING-AN-ARTICLE.md section 2; the community lane wrote its own E261 at the same time, so cite this one as "E261 (Inner Child)"). experiments/t107-answers/LESSONS.md has what his rewrites do and a search of his saved messages for other answers put in as typed (chat_runs.py). tools/humanization/repo_links.py: a document or message for him links every file it names; pangram_links_check.py --chat and questions_page.py refuse a repository path, and ENGAGING.md, turn 106\'s LESSONS.md and OWNER-QUESTIONS.md link theirs.',
    '  - Round 6 (experiments/t107-substack/): round 5\'s drafts were gone from his drafts list, so two new ones with the same titles, "Inner Child, draft A (temp, delete after)" (https://ibogaqueen.substack.com/publish/post/221982879) and "Inner Child, draft B (temp, delete after)" (https://ibogaqueen.substack.com/publish/post/221983135), pasted in his Brave through Claude in Chrome (A 15,026 words, matching; B 12,604, its note link shown as the note, as before; PASTED.json). 19 predictions, ledger #262 to #280 (ITEMS.json). Both labels read Human; the extension\'s panel opens beside the page, so he sends the result links.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. Round 6\'s results (OWNER-QUESTIONS.md asks him for the two result links): read each pangram.com/feed page with '
         'tools/humanization/pangram_feed_read.js in his Brave (Claude in Chrome), save experiments/t107-results/RESULT-A.json and '
         'RESULT-B.json, record the two halves and the 17 items against ledger #262 to #280 (experiments/t107-substack/ITEMS.json; '
         'experiments/t99-results/ROUND5-RESULTS.json is the model), rebuild the scorecard (articles/inner-child-therapy/tools/build_scorecard.py), '
         'and bring each window to him with its link: his own text is his to fix, mine goes through the tell panel first (E253). Then the '
         'two drafts are his to delete. A list of more than a few items goes to him as an interactive review page (UDA '
         'patterns/owner-questions-page.md), an open question names what it\'s about, never an old question\'s number (E257), and every '
         'file named in what he reads is a link (repo_links.py).')
upd = {
    'turn': '107',
    'replace': [
        [e('TURN 106 (2026-10-24, his answers of 2026-10-24 22:55 UTC; by %s), the latest; its next step wins over everything below. Branch %s; pull request #233 (https://github.com/u-dont-existDOTcom/joel-articles/pull/233) for him to merge.' % (S, BR)),
         'TURN 106 (2026-10-24, his answers of 2026-10-24 22:55 UTC; by %s), FINISHED. Branch %s; pull request #233 (https://github.com/u-dont-existDOTcom/joel-articles/pull/233), merged 2026-10-24 23:45 UTC.' % (S, BR), 1],
        [e('this version is from turn 106 (his answers of 2026-10-24 22:55 UTC; pull request #233 for him to merge).'),
         'this version is from turn 107 (his answers of 2026-10-25 00:24 UTC; pull request #239 for him to merge).', 1],
        [e('turns 59 to 76 and 100 to 106 by %s' % S), 'turns 59 to 76 and 100 to 107 by %s' % S, 1],
        [e('  - experiments/t106-answers/ (with LESSONS.md), t106-api/, t106-installs/, t106-tries/, t106-panel/ and t106-review/ (the latest turn), '),
         '  - experiments/t107-answers/ (with LESSONS.md and chat_runs.py), t107-installs/, t107-review/ and t107-substack/ (the round 6 drafts; the latest turn), t106-answers/ (with LESSONS.md), t106-api/, t106-installs/, t106-tries/, t106-panel/ and t106-review/ (turn 106), ', 1],
        [r'^1\. His answers to question 103 \(OWNER-QUESTIONS\.md\):.*$', next1, 1],
    ],
    'insert_before': [
        ['- TURN 106 (2026-10-24', turn107],
        ['- A flag on one of the guide\'s instructions is about its wording',
         '- An answer of his that explains something goes in as article sentences, not as he typed it, and is shown beside his words; only the line itself goes in as typed (E261, Inner Child; his 2026-10-25 "you put in some of my things too verbatim").\n'
         '- Every file named in a document or message for him is a link he can click, never a path in the repository (tools/humanization/repo_links.py; his 2026-10-25 "i have no idea where the 3 files are").'],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His merge of pull request #239 (turn 107).',
            '2. Round 6\'s two result links: on each draft\'s paid preview, the Pangram label next to the author\'s name, then View Full Analysis (OWNER-QUESTIONS.md).',
            '3. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)" (new in turn 107), stay until round 6 is read; his delete comes after.',
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
