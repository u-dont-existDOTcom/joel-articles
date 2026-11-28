#!/usr/bin/env python3
"""results.py - what happened to each card of the rules audit after Joel's answers (export of 2026-11-28 10:24 UTC).

  python3 results.py      writes ../RESULTS.md

Each card: his answer and his note word for word, the rules of the rule tree (rules/TREE.md) that now carry it (found by
the card's id in a rule's "Replaces" or "Record"), the tools changed for it (TOOLS), and any question still open.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
AUDIT = HERE.parent
REPO = AUDIT.parents[2]
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'

TOOLS = {
    'C01': 'pangram_ledger.py: the 20% near-miss and 40% big-change refusals are notes now',
    'C02': 'pangram_ledger.py and suggestion_review.py: no refusal for a missing receipt; sense_receipt.py checks only what '
           'is present and wrong, and the link-position test is gone',
    'C03': 'sense_receipt.py: the opening refusal is gone',
    'C04': 'apply_gate.py: a content change he approved goes in at once, recorded with what he approved',
    'C05': 'pangram_ledger.py: ten tries a paragraph, more with a named trail; the score comparison no longer stops a try',
    'C07': 'pangram_ledger.py (with C05); pangram_api.py: the size cap warns, and refuses only half an article or more',
    'C10': 'fidelity_keys.py: a warning word the new line lacks is reported, not failed; numbers, doses and compounds stay exact',
    'C11': 'tells_lint.py: overused words are reported, not failed; a new note for "one" where "a" reads better; '
           'pangram_ledger.py: a try that adds an overused word gets a note, not a refusal',
    'C12': 'keep_as_is.py and render_article_so_far.py: an entry that is my own reading is a note, not a refusal',
    'C14': 'pangram_ledger.py: no first-fix declaration; tells_lint.py: a note for "for the thing"',
    'C17': 'sense_receipt.py: the fresh reads are optional and their marks judged; his_fixes_brief.md says the same',
    'C18': 'suggestion_review.py: a plain reason on a card, no fixed prefixes; approval_record.py: no approval count',
    'C20': 'pangram_ledger.py: no tell-panel refusal',
    'C22': 'tells_lint.py: no count fails a draft by itself',
    'C23': 'tells_lint.py and tells_registry.json: string tells with no words of his are notes',
    'C24': 'tells_lint.py: brackets around a gloss are never failed',
    'C25': 'toc_check.py: a fate only for pairs a reader marked as the same',
}


def main():
    ans = json.loads((AUDIT / 'ANSWERS-20261128-1024.json').read_text(encoding='utf-8'))
    tree = (REPO / 'rules' / 'TREE.md').read_text(encoding='utf-8')
    rules = re.findall(r'^#### (R-[a-z0-9-]+) \| (.+)$((?:\n(?!####|###|## ).*)*)', tree, re.M)
    out = ['# The rules audit: what happened to each card', '',
           'His answers: [the export of 2026-11-28 10:24 UTC](ANSWERS-20261128-1024.json) (%d approved, %d to revise), on '
           '[the cards](QUESTIONS.md). Each approved fix and each revision is now a rule of the rule tree, written once '
           '([the tree](%srules/README.md)); where a tool enforced the old rule, the tool changed too.' % (
               ans['counts'].get('approved', 0), ans['counts'].get('needs_revision', 0), GH), '']
    for it in ans['items']:
        cid = it['id']
        carried = [(rid, title) for rid, title, body in rules if re.search(r'(?<![A-Za-z0-9-])%s(?![0-9])' % re.escape(cid), body)]
        status = {'approved': 'approved', 'needs_revision': 'to revise (done as his note says)'}.get(it['status'], it['status'])
        out += ['## %s. %s' % (cid, it['title']), '', '- **His answer:** %s' % status]
        if it.get('note'):
            out.append('- **His note:** "%s"' % it['note'].replace('\n', ' ').strip())
        if carried:
            out.append('- **Now in the tree as:** ' + '; '.join('[%s](%srules/TREE.md#%s)' % (
                t, GH, re.sub(r'[^\w\- ]', '', ('%s | %s' % (r, t)).lower()).replace(' ', '-')) for r, t in carried))
        else:
            out.append('- **Now in the tree as:** (none found: see the tree)')
        if cid in TOOLS:
            out.append('- **Tools changed:** ' + TOOLS[cid])
        out.append('')
    (AUDIT / 'RESULTS.md').write_text('\n'.join(out), encoding='utf-8')
    print('RESULTS.md: %d cards' % len(ans['items']))


if __name__ == '__main__':
    main()
