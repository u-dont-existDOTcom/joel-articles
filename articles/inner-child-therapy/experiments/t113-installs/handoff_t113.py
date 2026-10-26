#!/usr/bin/env python3
"""Turn 113: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t113.py [--pr N] [--test NOTE]   writes the update; with --test, applies it to a copy of NOTE"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parents[1] / 'HANDOFF-UPDATE.json'
S = 'https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq'
BR = 'handoff/claude-dangerous-adult-20260924-1631'
N = sys.argv[sys.argv.index('--pr') + 1] if '--pr' in sys.argv else None
PRS = ('pull request #%s (https://github.com/u-dont-existDOTcom/joel-articles/pull/%s)' % (N, N)) if N else 'the turn-113 pull request'
PRN = ('pull request #%s' % N) if N else 'the turn-113 pull request'
OLDPR = 'pull request #250 (https://github.com/u-dont-existDOTcom/joel-articles/pull/250)'
e = re.escape

turn113 = '\n'.join([
    '- TURN 113 (2026-10-25, his message of 2026-10-25 22:38 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s for him to merge.' % (S, BR, PRS),
    '  - Objective anchor (UDA): main objective, the guide humanized, every paragraph and section reading Human with the meaning kept and reading engagingly, like a good public self-help book; this turn\'s contribution, every edit he asked for proposed on one review sheet for him and GPT (case headings, long paragraphs split, his 109 A wording), nothing installed; scope, no new claims, no life facts he didn\'t give, his words changed only with his OK.',
    '  - His message: experiments/t113-answers/JOEL-20261025-2238.md ("109a"; "no point checking the drafts at this point, we are about to make major edits. so do the major edits as you suggested and then i can see what GPT thinks of all the changes (not just the headings idea but fixing the way the sections read as you did with Hear the Guard)"). Round 7 of the guide as it is: skipped, as he said.',
    '  - The proposals (experiments/t113-shape/proposals.py, which checks every operation; SECTIONS.json; PROPOSAL-ARTICLE.md, the guide with all of them in): case headings in eight sections (Hear the Guard First, Start With Whatever Showed Up, When to Change the Strategy, When Escape Leaves Reality Behind, When the Adult Voice Feels Fake, Finding a Therapist to Borrow Adulthood, Other Folks Also Have Hooks, Borrow One Competency at a Time), every one a #### (the guide\'s small-heading size, so a section\'s own subsections keep their size; cold read A1\'s catch), a lifted heading where the paragraph\'s first words named its case (the paragraph then drops them), new words otherwise; splits in How Would You Know It\'s Helping? (in four), How to Forgive Without Forgetting P3, and inside the headed sections (one each in Start With, When to Change and Other Folks, two in When Escape); one sentence moved up three sentences in Start With ("How you picture all that is up to you ..."), to stay with what it is about; his 109 A ("the blind spot behind it even has a name"). Left as they are, with why on the sheet: How to Forgive (order), The Parent You Inherited, How Much Happiness, Differentiation, Make a Simple Vow, Signs of Manipulation, Before You Try to Go Deep, and the story and argument sections.',
    '  - Gate (experiments/t113-gate/GATE.md): three rounds; every item with new words (the new headings and the Solomon sentence) through tools/humanization/owner_delivery_gate.py, three fresh Sonnet reviewers per role; a round-3 FAIL fell back to the paragraph\'s own words, never redrafted (GATE.md); the sheet shows only delivered bytes (t113-review/build_review.py refuses otherwise). Four cold reads of every proposed section, and what I did with each note: experiments/t113-shape/COLD-READ.md.',
    '  - The sheet: experiments/t113-review/ (CARDS.json, build_review.py, REVIEW.json, REVIEW.html), published to https://claude.ai/artifact/LTEDB18wTYzuUkgobzbUrn (this account only can republish). tools/humanization/suggestion_review.py 1.2 shows a new heading inside a whole passage with its Markdown #s.',
    '  - Pangram: not run this turn (his "no point checking the drafts at this point, we are about to make major edits"); the two temporary drafts still hold round 7\'s text, and the next check puts in what he approves from the sheet (experiments/t113-substack/ holds the tools, unrun).',
    '  - NEXT: Next step 1.',
])
next1 = ('1. GPT\'s review of the turn-113 sheet, when he pastes it (into experiments/t114-answers/ first, E174). Take GPT\'s advice card '
         'by card as in turn 110 (experiments/t110-review/AGREED.md), and give him a sheet of only what both recommend '
         '(suggestion_review.py); any new or changed heading or sentence goes through tools/humanization/owner_delivery_gate.py first. '
         'What he approves goes in word for word; then the two temporary drafts get the guide as installed for the free check, '
         'predictions first (experiments/t113-substack/ has the tools). Then Untangling the Belonging Bargains P1\'s own fix. Every turn ends with the whole article sent and passed to the chat check as --sent (E271 (Inner Child)); an open '
         'question names what it\'s about (E257), and every file named in what he reads is a link to a page, never a folder (repo_links.py).')
upd = {
    'turn': '113',
    'replace': [
        [e('TURN 112 (2026-10-25, his message of 2026-10-25 21:40 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s for him to merge.' % (S, BR, OLDPR)),
         'TURN 112 (2026-10-25, his message of 2026-10-25 21:40 UTC; by %s), FINISHED. Branch %s; %s, merged.' % (S, BR, OLDPR), 1],
        [e('this version is from turn 112 (his message of 2026-10-25 21:40 UTC; pull request #250 for him to merge).'),
         'this version is from turn 113 (his message of 2026-10-25 22:38 UTC; %s for him to merge).' % PRN, 1],
        [e('turns 59 to 76 and 100 to 112 by %s' % S), 'turns 59 to 76 and 100 to 113 by %s' % S, 1],
        [e('  - experiments/t112-answers/ (his message), t112-installs/ and t112-substack/ (round 7) (the latest turn), '),
         '  - experiments/t113-answers/ (his message), t113-shape/ (the proposals and the cold read), t113-gate/ (the owner-delivery gate), t113-review/ (the sheet), t113-substack/ (the proposals\' check) and t113-installs/ (the latest turn), t112-answers/, t112-installs/ and t112-substack/ (turn 112), ', 1],
        [r"^1\. Round 7's two result links when he sends them: read each feed page's windows.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 112 (2026-10-25', turn113],
        ['- A link goes to a page he can read, never to a folder',
         '- A case heading goes only where a paragraph is its own case a reader may skip to, as a #### (the guide\'s small-heading size, so a section\'s own subsections keep their size), worded the way a reader would name their own situation; where the paragraph\'s first words already name it, they become the heading and the paragraph starts after them, so nothing is said twice (his 2026-10-25 21:40 idea and "the first sentence of the para will often not connect anymore or be redundant"; turn 113).'],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. GPT\'s review of the turn-113 review sheet (question 110).',
            '2. His merge of %s (turn 113).' % PRN,
            '3. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)", still hold round 7\'s text; the next check puts in what he approves, and his delete comes after it is read.',
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
