#!/usr/bin/env python3
"""Turn 120: the item for the InnerSignal map's lane in universal-dev-architecture (suggested-fixes/innerSignalGraph/), asking
that lane to clear the humanization queue, as Joel asked (2026-11-04 10:02 UTC). UDA's suggested-fix rule: an agent with a
change for a project it isn't working on files it in that project's lane; the project's own agent makes the change. The
counts come from QUEUE-CLEARED.json. Writes UDA-ITEM.md, the exact file that goes into UDA (the repository is public: an
extract, his words quoted only where they are the request)."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
C = json.loads((HERE / 'QUEUE-CLEARED.json').read_text(encoding='utf-8'))
K = C['counts']
assert not K['undecided'], K['undecided']
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/'
REC = BLOB + 'experiments/t120-queue/QUEUE-CLEARED.md'
left = [r for r in C['entries'] if r['fate'] == 'left out']
SHORT = {'PGQ-036': 'hypnosis during grief or an altered state: the guide never raises whether hypnosis suits someone grieving, so I recommended leaving it out, and the owner raised no objection'}
assert all(r['id'] in SHORT for r in left), [r['id'] for r in left]

text = '\n'.join([
    '# Clear the humanization queue: every entry is in the humanized Inner Child guide or deliberately left out',
    '',
    '- For: `u-dont-existDOTcom/innerSignalGraph`',
    '- Filed: 2026-11-04, by the Claude session working on the humanized Inner Child guide (`u-dont-existDOTcom/joel-articles`)',
    '- From: `u-dont-existDOTcom/joel-articles`, branch `handoff/claude-dangerous-adult-20260924-1631`: [every entry\'s fate](%s) '
    '(`articles/inner-child-therapy/experiments/t120-queue/QUEUE-CLEARED.md`, with the script that built it and checked its quotes)' % REC,
    '- Owner request: yes. The owner\'s words, 2026-11-04 10:02 UTC: "make sure you clear the humanization queue". Earlier, at 00:56 UTC, '
    'about this queue: "i think i already put them in if they were important points".',
    '- Existing pull request: none',
    '- Supersedes: none',
    '',
    '## What to do',
    '',
    'Consume every entry of `authoring/PENDING-PUBLIC-GUIDE-CHANGES.md` (queue version 2026-10-31-r20, the file as of cb2008ce6: %d entries, '
    'PGQ-001 to PGQ-055, with no PGQ-044 to PGQ-046), reset the file to its EMPTY sentinel and update `authoring/public-guide-sync.json` '
    'for the inner-child guide, in one reviewed change, as the file\'s consumption contract says.' % K['entries'],
    '',
    'Each entry\'s fate, read against the owner\'s current humanized guide, is in [the record](%s): %d in, %d with the core point in his own '
    'words (what an entry adds beyond that went with his own cuts and edits of the guide, or was left out as his call), and %d left out '
    '(%s). The record quotes, for each entry, the guide\'s words that carry it and the heading they sit under, and says what each '
    'partly covered entry adds that the guide doesn\'t. For two of them, PGQ-009 and PGQ-016, that extra went in an edit of his inside a '
    'paragraph that he hasn\'t confirmed as meant; he has been asked, and whatever he wants back goes into the guide from that record, so '
    'neither needs to hold the reset.'
    % (REC, K['in'], K['core'], K['out'], '; '.join('%s, %s' % (r['id'], SHORT[r['id']]) for r in left)),
    '',
    '## Why',
    '',
    'The owner reorganized and edited the humanized guide himself on 2026-11-03 and asked, on 2026-11-04, that the queue be cleared. Until it '
    'is, every entry still reads as waiting for the guide, and the humanized guide\'s lane keeps reading them again. That lane doesn\'t edit '
    'this repository, so the reset is yours.',
    '',
    '## Check first',
    '',
    '- Read the record against your queue. If an entry\'s fate looks wrong to you, consume the others and leave that one queued, as the '
    'contract allows for a subset, with the question on your owner questions page.',
    '- These tests assert entries the reset removes and will need changing with it: `tests/public-guide-humanization-queue.test.mjs` '
    '(PGQ-048 to PGQ-050 and the queue version), `tests/relational-intention-expectation.test.mjs` (PGQ-049 to PGQ-051), '
    '`tests/feeling-agency-referral.test.mjs` (PGQ-039, PGQ-043), `tests/response-focus-continuity.test.mjs` (PGQ-041, PGQ-042), '
    '`tests/critical-voice-refinements.test.mjs` (PGQ-052 to PGQ-054, and that the sync file is unchanged), '
    '`tests/performed-self-permissive-reparenting.test.mjs` (PGQ-050) and `tests/spiritual-source-paragraph.test.mjs` (PGQ-055).',
    '- `scripts/check-guide-change-provenance.mjs` refuses removed entries unless `authoring/public-guide-sync.json` changes in the same '
    'pull request.',
    '- PGQ-039 and PGQ-048 ask for a legal review of explicit jurisdictional statements before public placement. The guide\'s passage on it '
    'is the owner\'s own wording; whether it holds any statement that needs that review is yours to judge before you consume them.',
    '',
])
(HERE / 'UDA-ITEM.md').write_text(text, encoding='utf-8')
print(len(text), 'characters')
