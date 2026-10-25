#!/usr/bin/env python3
"""Turn 109: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t109.py PR [--test NOTE]   writes the update for pull request PR; with --test, applies it to a copy of NOTE"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE.parents[1] / 'HANDOFF-UPDATE.json'
S = 'https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq'
BR = 'handoff/claude-dangerous-adult-20260924-1631'
SHEET = 'https://claude.ai/artifact/LTEDB18wTYzuUkgobzbUrn'
pr = sys.argv[1]
assert pr.isdigit()
PR = 'pull request #%s (https://github.com/u-dont-existDOTcom/joel-articles/pull/%s)' % (pr, pr)
e = re.escape

turn109 = '\n'.join([
    '- TURN 109 (2026-10-25, his answers of 2026-10-25 14:20 UTC; by %s), the latest; its next step wins over everything below. Branch %s; %s for him to merge.' % (S, BR, PR),
    '  - Objective anchor (UDA): main objective, the guide humanized, every paragraph and section reading Human with the meaning kept and reading engagingly, like a good public self-help book; this turn\'s contribution, his two rewrites in and checked, three sections in the plain-path-first shape he approved (104 A), round 6\'s windows below Human-High saved, and the point-of-view read under the new rule; scope, no new claims, no life facts he didn\'t give, his words changed only with his OK.',
    '  - His message: experiments/t109-answers/JOEL-20261025-1420.md: "104 a yes this makes it much more of a readable guide, good."; 105.1 his Pink paragraph for How This Relates to IFS\'s end; 105.2 his photos opener ("this is the part that reads ai and it\'s actually redundant also"); "make sure you save all the sections that pangram marked as less than human high confidence"; "make sure you use the new rule in the repo about marking wherever it looks like there\'s a lack of a real POV".',
    '  - Installs (experiments/t109-installs/): apply_t109.py (his IFS and photos texts, Hear the Guard First reshaped); reshape_t109.py (Start With Whatever Showed Up, Before You Tell the Hardest Stuff); reshape_t109b.py to reshape_t109e.py (the later tries); owner_edits_t109*.py (OWNER-EDITS.json, 184/184 pass); questions_t109.py (question 106).',
    '  - API checks (experiments/t109-api/API-CHECKS.md, batches t109-api-1 to -5, ledger #281 to #299, 19 checks, 14 right): his IFS paragraph Human alone and How This Relates to IFS Human; photos P2 Human and the section Human; Before You Tell the Hardest Stuff P1, P3 and the section Human. Hear the Guard First took four tries: his line "It puts you into the role of the Nurturer, which alleviates the instinct to argue back." carried whichever paragraph held it to Human and the other read 28% to 99.8% AI (E264 (Inner Child)); the second try is installed, my pick on the sheet. Start With Whatever Showed Up\'s first try P1 read 99.8% AI; its second try keeps his P1 whole. Both sections\' checks wait on his point-of-view decisions (5.1 and 4.8 in experiments/t109-pov/CHECKED.json).',
    '  - Saved: round 6\'s 111 windows below Human-High, by section, with whose words and whether still in the article (experiments/t109-windows/WINDOWS.md and WINDOWS.json, windows_list.py).',
    '  - The point-of-view read (project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md "Actual POV required", omission test first; tools/humanization/clarity_read.py make --kind pov, new, with tools/humanization/pov_examples.json; docs/CLARITY-READ.md part 5): eight Sonnet readers, 61 flags; my check (experiments/t109-pov/my_check.py, CHECKED.json, POV-READ.md): 13 cuts, 10 fixes from his own words, 3 for his words only, 35 left with why.',
    '  - His review sheet: %s (an artifact of this account; the master is experiments/t109-review/REVIEW.html, built by make_review.py with tools/humanization/decision_page.py, new, browser-tested by decision_page_browser_test.py: 28 checks pass in light and dark). He pastes its Copy JSON into the chat; save it as experiments/t110-answers/ and put in what he approves.' % SHEET,
    '  - NEXT: Next step 1.',
])
next1 = ('1. His decisions from the review sheet (question 106 on OWNER-QUESTIONS.md; he pastes the JSON from either account; the '
         'sheet\'s master is experiments/t109-review/REVIEW.html, its ids S1 to S4, Y1, C1 to C13, P1 to P10, Q1 to Q3, L1, mapped to '
         'the readers\' keys in experiments/t109-review/SPEC.json). Put in what he approves word for word, with notes; then the two '
         'held section checks (Hear the Guard First, Start With Whatever Showed Up) and the next reshape batch, densest first, each '
         'new paragraph of 50 words or more checked alone before the next section (E264 (Inner Child)). Then round 7, the next '
         'whole-article check, in the two temporary drafts (paste with experiments/t88-substack/paste_payload_lane.js; he sends the '
         'result links; read them as experiments/t108-results/record_round6.py does). A list of more than a few items goes to him '
         'on a decision page (tools/humanization/decision_page.py), an open question names what it\'s about (E257), and every '
         'file named in what he reads is a link to a page, never a folder (repo_links.py).')
upd = {
    'turn': '109',
    'replace': [
        [e('TURN 108 (2026-10-25, his message of 2026-10-25 12:39 UTC; by %s), the latest; its next step wins over everything below. Branch %s; pull request #241 (https://github.com/u-dont-existDOTcom/joel-articles/pull/241) for him to merge.' % (S, BR)),
         'TURN 108 (2026-10-25, his message of 2026-10-25 12:39 UTC; by %s), FINISHED. Branch %s; pull request #241 (https://github.com/u-dont-existDOTcom/joel-articles/pull/241), merged.' % (S, BR), 1],
        [e('this version is from turn 108 (his message of 2026-10-25 12:39 UTC; pull request #241 for him to merge).'),
         'this version is from turn 109 (his answers of 2026-10-25 14:20 UTC; pull request #%s for him to merge).' % pr, 1],
        [e('turns 59 to 76 and 100 to 108 by %s' % S), 'turns 59 to 76 and 100 to 109 by %s' % S, 1],
        [e('  - experiments/t108-answers/, t108-results/ (round 6), t108-shape/ (the density page and the worked example), t108-panel/, t108-tries/ and t108-installs/ (the latest turn), '),
         '  - experiments/t109-answers/, t109-installs/, t109-api/, t109-windows/ (round 6\'s saved windows), t109-pov/ (the point-of-view read) and t109-review/ (his review sheet) (the latest turn), t108-answers/, t108-results/ (round 6), t108-shape/ (the density page and the worked example), t108-panel/, t108-tries/ and t108-installs/ (turn 108), ', 1],
        [r"^1\. His answers to question 104 \(OWNER-QUESTIONS\.md; my pick: the plain path first.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 108 (2026-10-25', turn109],
        ['- A link goes to a page he can read, never to a folder',
         '- A reshape moves a reply only with what it answers, and a paragraph of instructions keeps a line of his reason or voice; each new paragraph of 50 words or more is checked alone before the next section is reshaped (E264 (Inner Child), turn 109).'],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His decisions on the review sheet (question 106 on OWNER-QUESTIONS.md): the three sections in the new shape, whether to name his friend Pink, and the point-of-view read\'s 26 items.',
            '2. His merge of pull request #%s (turn 109).' % pr,
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
