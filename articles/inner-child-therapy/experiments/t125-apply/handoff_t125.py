#!/usr/bin/env python3
"""Turn 125: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t125.py PR [--test NOTE [OUT]]   writes the update with the turn's pull request number; with --test, applies it
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
PAGE = 'https://claude.ai/artifact/RKJUWjR4MRCyRkpTqfDoZA'
e = re.escape

turn125 = '\n'.join([
    '- TURN 125 (2026-11-04, his sense-read answers of 16:11 UTC; by %s), the latest; its next step wins over everything below. Branch %s, from main (pull request #295, turn 124, merged by him at 16:03 UTC); %s.' % (S, BR, PRS),
    '  - His answers (experiments/t125-answers/ANSWERS-20261104-1611.json, his export of the sense-read marking page %s; README.md there quotes his comments): 15 cards approved, his own version of SR-516 ("in very powerful meditations and altered states."), SR-11 and SR-69 rejected, SR-373 answered, SR-212b and SR-384 (my "leave") left undecided. SR-11, the two double hyphens: "no everything should be the 2 dashes not em-dash, em-dash is ai". SR-69: "debatable makes no sense you can\' tdebate an experience... different is what i meant". SR-373: "it came first and after, but after it was less dangerous as i wasn\'t hanging out as far".' % PAGE,
    '  - Put in (experiments/t125-apply/: apply_t125.py, APPLIED.json): 16 changes, each card\'s words as the card had them, his version word for word; OWNER-EDITS.json 16 joel-125-* entries, joel-116-117-guide updated where SR-514 changed its words (supersede_t125.py); 132 pass, 0 failed. KEEP-AS-IS.json K19 to K22: his two double hyphens, "Even if every case is different", and the bars-and-windows sentence, with his words.',
    '  - Asked him (my recommendation in brackets): the guide has 9 dashes " – " (7 were em dashes in his ODT, changed by the standard swap; 2 he typed, "bigger – perhaps much bigger –"), which he may be seeing as em dashes. Should all 9 be his two hyphens with no spaces, like "handling--we" [yes]? And should the standard swap (tools/humanization/typography_swap.py, gate E337 (gut), AGENTS.md) make "--" in all his articles [yes, with round 11 showing whether Pangram minds]? A change to the swap is a shared-rule change: record his words in AGENTS.md and the gate doc, and check other lanes\' open pull requests for overlap first.',
    '  - NEXT: Next step 1.',
])
next1 = ('1. His answer on the dashes: put it in (and, if he says so, the standard swap changed for every article: typography_swap.py, its '
         'tests, AGENTS.md, a lesson in docs/HUMANIZATION-GATE.md); then round 11, the free way, on the guide as it will be published '
         '(experiments/t119-substack/make_payloads.py\'s method in a new t126-substack/, the two temporary drafts, their secret preview '
         'links, his extension; each window recorded with its confidence, E278). Then the publish draft: his live post '
         '(https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided, post 189761959) checked against what we last had of '
         'it before anything replaces it (E332; experiments/t124-live/LIVE-COMPARE.md: 18 paragraphs from his post of 2026-10-03 to '
         'check against the article first), his pictures uploaded where the notes say, the post\'s own pictures and videos kept, the '
         'Rumi quote as a pull quote, its quote marks curled the right way before pasting, the post\'s updated date set; he updates the '
         'post himself. After he publishes: the Hearthwork article (his paste of 2026-11-04 12:02 UTC, experiments/t121-answers/), '
         'humanized in a lane of its own (its article folder registered, a branch from main), its reparenting passages brought in line '
         'with the reorganized guide. Every turn ends with the whole article sent and passed to the chat check as --sent (E271 (Inner '
         'Child)), rendered with --images for his pictures.')
upd = {
    'turn': '125',
    'replace': [
        [e('TURN 124 (2026-11-04, his message of 15:00 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 124 (2026-11-04, his message of 15:00 UTC; by %s), FINISHED.' % S, 1],
        [r'this version is from turn 124 \(his message of 2026-11-04 15:00 UTC; pull request #\d+ \(https://github\.com/u-dont-existDOTcom/joel-articles/pull/\d+\), open for him to merge\)\.',
         'this version is from turn 125 (his sense-read answers of 2026-11-04 16:11 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 124 by %s' % S), 'turns 59 to 76 and 100 to 125 by %s' % S, 1],
        [e('  - experiments/t124-answers/ (his message), t124-results/ (round 10 read), t124-sense/ (the word-for-sense read and its marking page) and t124-live/ (his live post as it was on 2026-11-04, against our copy and his guide) (the latest turn), '),
         '  - experiments/t125-answers/ (his sense-read answers) and t125-apply/ (put in) (the latest turn), t124-answers/ (his message), t124-results/ (round 10 read), t124-sense/ (the word-for-sense read and its marking page), t124-live/ (his live post as it was on 2026-11-04, against our copy and his guide), ', 1],
        [r"^1\. His answers on the sense-read marking page \(https://claude\.ai/artifact/RKJUWjR4MRCyRkpTqfDoZA; its db's decisions collection.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 124 (2026-11-04', turn125],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join([
            '1. His answer on the dashes: all 9 " – " of the guide as his two hyphens with no spaces (my recommendation: yes), and the standard swap with them for every article (yes, with round 11 showing whether Pangram minds).',
            '2. The map lane\'s reset: his merge of UDA pull request #467 (%s), or the map lane\'s resume line with the request (given to him in turn 121), then his merge of that lane\'s pull request that empties the queue.' % UDA,
            '3. His merge of pull request #%s (turn 125).' % PRN,
            '4. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)": round 11 reuses them; deleting them is his.',
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
