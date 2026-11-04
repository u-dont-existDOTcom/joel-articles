#!/usr/bin/env python3
"""Turn 126: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t126.py PR [--test NOTE [OUT]]   writes the update with the turn's pull request number; with --test, applies it
                                           to a copy of NOTE (and writes the result to OUT)"""
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

turn126 = '\n'.join([
    '- TURN 126 (2026-11-04, his message of 16:30 UTC; by %s), the latest; its next step wins over everything below. Branch %s, from main (pull request #297, turn 125, merged by him at 16:29 UTC); %s.' % (S, BR, PRS),
    '  - His message (experiments/t126-answers/JOEL-20261104-1630.md): "1 yes to both, we\'ve already established before that pangram prefers the 2 dashes, but it won\'t matter anyway in high conf human sections. it could flip low conf ones ai" (all nine dashes his two hyphens with no spaces, and the standard swap with them for every article).',
    '  - The standard swap changed for every article (gate E353 (Inner Child) in docs/HUMANIZATION-GATE.md, after E341, and the swap\'s sentence under "Keep his exact characters"): tools/humanization/typography_swap.py makes every em dash, and every en dash with a space beside it, "--" with no spaces (a range stays a range, "10–20", "1.8g – 2.4g"; a dash at a line\'s edge keeps a space toward its words); fidelity_keys.py matches a dash whatever its length; tells_lint.py\'s O63 names his two hyphens; tells_registry.json W115; tests. Pushed with --overlap-ok for #293 (its E353 to E355 are in the gut lane\'s section) and #280 (no line of those files changed).',
    '  - The guide\'s nine dashes are his two hyphens (experiments/t126-dashes/: record_dashes.py, DASHES.json; OWNER-EDITS.json joel-126-dashes; 133 pass).',
    '  - Round 11, the free way (experiments/t126-substack/: make_payloads.py, PAYLOADS.json, CHECK-A/B.txt, PASTED.json): A 16,694 words, B 11,892; predictions t126s-A#382 and t126s-B#383 first. Pasted into the two temporary drafts (saved 16:43 and 16:44 UTC), each word count the payload\'s before and after a reload; on the secret preview links, A\'s 226 lines all as CHECK-A.txt but line 79 (the no-break space of "Breadcrumbing is"), B\'s 163 lines exactly CHECK-B.txt. Both secret links opened in his own Brave from his laptop\'s shell (brave-browser-stable, "Opening in existing browser session"), as the gut lane found (E353 of pull request 293): Claude in Chrome\'s browser is not his.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. His two round-11 result links (pangram.com/feed/...): each window recorded with its confidence (E278; experiments/'
         't124-results/record_round10.py\'s way, the pages read in the built-in browser with pangram_feed_read.js in compact mode), '
         'predictions #382 and #383 scored, the scorecards rebuilt; a window that reads AI is narrowed to its paragraphs through the API '
         'first (E343), a Low one fixed in its own sentence only (E350). Then the publish draft: his live post '
         '(https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided, post 189761959) checked against what we last had of '
         'it before anything replaces it (E332; experiments/t124-live/LIVE-COMPARE.md: 18 paragraphs from his post of 2026-10-03 to '
         'check against the article first), his pictures uploaded where the notes say, the post\'s own pictures and videos kept, the '
         'Rumi quote as a pull quote, its quote marks curled the right way before pasting, the post\'s updated date set; he updates the '
         'post himself. After he publishes: the Hearthwork article (his paste of 2026-11-04 12:02 UTC, experiments/t121-answers/), '
         'humanized in a lane of its own (its article folder registered, a branch from main), its reparenting passages brought in line '
         'with the reorganized guide. Every turn ends with the whole article sent and passed to the chat check as --sent (E271 (Inner '
         'Child)), rendered with --images for his pictures.')
upd = {
    'turn': '126',
    'replace': [
        [e('TURN 125 (2026-11-04, his sense-read answers of 16:11 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 125 (2026-11-04, his sense-read answers of 16:11 UTC; by %s), FINISHED.' % S, 1],
        [r'this version is from turn 125 \(his sense-read answers of 2026-11-04 16:11 UTC; pull request #\d+ \(https://github\.com/u-dont-existDOTcom/joel-articles/pull/\d+\), open for him to merge\)\.',
         'this version is from turn 126 (his message of 2026-11-04 16:30 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 125 by %s' % S), 'turns 59 to 76 and 100 to 126 by %s' % S, 1],
        [e('  - experiments/t125-answers/ (his sense-read answers) and t125-apply/ (put in) (the latest turn), '),
         '  - experiments/t126-answers/ (his message), t126-dashes/ (his two hyphens) and t126-substack/ (round 11) (the latest turn), t125-answers/ (his sense-read answers), t125-apply/ (put in), ', 1],
        [r"^1\. His answer on the dashes: put it in \(and, if he says so, the standard swap changed for every article.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 125 (2026-11-04', turn126],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His two round-11 result links (pangram.com/feed/...), from his extension on the two secret preview links opened in his Brave (the links also went to him in chat in turn 126).',
            '2. The map lane\'s reset: his merge of UDA pull request #467 (%s), or the map lane\'s resume line with the request (given to him in turn 121), then his merge of that lane\'s pull request that empties the queue.' % UDA,
            '3. His merge of pull request #%s (turn 126).' % PRN,
            '4. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)": round 11 is in them; deleting them is his.',
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
    if len(sys.argv) > sys.argv.index('--test') + 2:
        pathlib.Path(sys.argv[sys.argv.index('--test') + 2]).write_text(new, encoding='utf-8')
