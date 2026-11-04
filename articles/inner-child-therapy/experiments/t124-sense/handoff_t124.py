#!/usr/bin/env python3
"""Turn 124: articles/inner-child-therapy/HANDOFF-UPDATE.json, the update tools/humanization/handoff_note.py applies to
~/claude-acceptance-transfer/handoffs/inner-child-article.md on Joel's laptop.
  handoff_t124.py PR [--test NOTE [OUT]]   writes the update with the turn's pull request number; with --test, applies it
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
FA = 'https://www.pangram.com/feed/26ca9a6d-2636-43b6-a68f-5478fe8e388d'
FB = 'https://www.pangram.com/feed/fd028698-3e86-44a3-ba40-17c95dcbcb08'
e = re.escape
SENSE = json.loads((HERE / 'SENSE-SUMMARY.json').read_text(encoding='utf-8'))   # written once the read is scored and traced

turn124 = '\n'.join([
    '- TURN 124 (2026-11-04, his message of 15:00 UTC; by %s), the latest; its next step wins over everything below. Branch %s, from main (pull request #294, turn 123, merged by him at 14:58 UTC); %s.' % (S, BR, PRS),
    '  - His message (experiments/t124-answers/JOEL-20261104-1500.md): his two round-10 result links, draft A %s and draft B %s.' % (FA, FB),
    '  - Round 10 read (experiments/t124-results/: record_round10.py, RESULT-A/B.json, ROUND10-RESULTS.json, SPOTS.json): each feed page read in the built-in browser with tools/humanization/pangram_feed_read.js in compact mode, the windows checked against the pages\' SHA-256s and the checked texts against CHECK-A.txt (the one no-break space as Substack shows it) and CHECK-B.txt. A: Human Written, 0.00% AI, 11 windows, 10 Human (High), 1 Human (Medium); B: Human Written, 0.00% AI, 10 windows, 8 Human (High), 2 Human (Medium). The three Medium windows are 1 to 5 of his own words where Pangram\'s sentence cut fell: "How do you check that?" (Don\'t Sell Your Inner Adult To Buy An Outer Adult), "Debs." after "Eugene V." (When Being Happy Feels Like Abandoning Someone), "Just because Mr." before "Boopaloopa" (Before You Tell the Hardest Stuff). My recommendation to him: leave all three. Predictions t123s-A#380 and t123s-B#381 right; scorecards rebuilt. Round 9 had one AI window (Low); round 10 has none and no Low window.',
    '  - The word-for-sense read (E331; experiments/t124-sense/: tools/humanization/sense_read.py make, seed 124, STYLE.md his guide\'s own "what is not wrong here"): ' + SENSE['record'],
    '  - NEXT: Next step 1.',
])
next1 = SENSE['next1'] + (
    ' Then the publish draft: his live post (https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided, post '
    '189761959, last updated 2026-11-03 22:29 UTC) checked against what we last had of it before anything replaces it (E332), his '
    'pictures uploaded where the notes say, the post\'s own pictures and videos kept, the Rumi quote as a pull quote, its quote marks '
    'curled the right way before pasting; he updates the post himself. After he publishes: the Hearthwork article (his paste of '
    '2026-11-04 12:02 UTC, experiments/t121-answers/), humanized in a lane of its own (its article folder registered, a branch from '
    'main), its reparenting passages brought in line with the reorganized guide. Every turn ends with the whole article sent and '
    'passed to the chat check as --sent (E271 (Inner Child)), rendered with --images for his pictures.')
upd = {
    'turn': '124',
    'replace': [
        [e('TURN 123 (2026-11-04, his message of 14:27 UTC; by %s), the latest; its next step wins over everything below.' % S),
         'TURN 123 (2026-11-04, his message of 14:27 UTC; by %s), FINISHED.' % S, 1],
        [r'this version is from turn 123 \(his message of 2026-11-04 14:27 UTC; pull request #\d+ \(https://github\.com/u-dont-existDOTcom/joel-articles/pull/\d+\), open for him to merge\)\.',
         'this version is from turn 124 (his message of 2026-11-04 15:00 UTC; %s).' % PRS, 1],
        [e('turns 59 to 76 and 100 to 123 by %s' % S), 'turns 59 to 76 and 100 to 124 by %s' % S, 1],
        [e('  - experiments/t123-answers/ (his message) and t123-substack/ (round 10: the payloads and the paste) (the latest turn), '),
         '  - experiments/t124-answers/ (his message), t124-results/ (round 10 read), t124-sense/ (the word-for-sense read and its marking page) and t124-live/ (his live post as it was on 2026-11-04, against our copy and his guide) (the latest turn), t123-answers/ (his message), t123-substack/ (round 10: the payloads and the paste), ', 1],
        [r"^1\. His two round-10 result links \(pangram\.com/feed/\.\.\.\): each window recorded with its confidence.*$", next1, 1],
    ],
    'insert_before': [
        ['- TURN 123 (2026-11-04', turn124],
    ],
    'sections': {
        '## Waiting on Joel': '\n'.join(SENSE['waiting'] + [
            '%d. The map lane\'s reset: his merge of UDA pull request #467 (%s), or the map lane\'s resume line with the request (given to him in turn 121), then his merge of that lane\'s pull request that empties the queue.' % (len(SENSE['waiting']) + 1, UDA),
            '%d. His merge of pull request #%s (turn 124).' % (len(SENSE['waiting']) + 2, PRN),
            '%d. The two temporary Substack drafts, "Inner Child, draft A (temp, delete after)" and "Inner Child, draft B (temp, delete after)": round 10 is in them and read; deleting them is his.' % (len(SENSE['waiting']) + 3),
            '%d. Never in the article: amounts (the 1g, the 7g) and any recipe for what to take instead, including his "ultimate psychedelic recipe" line and its link.' % (len(SENSE['waiting']) + 4),
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
