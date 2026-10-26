"""My check of every community finding a reader marked "matters", and every slip (READS-ALL.json), with what became of it:
a card on the marking page, or why it stays. Writes TRIAGE.md.

  python3 articles/intentional-communities/candidate/joel-20261025/emulate-check/triage.py

READS-ALL.json has "explained" set where the lane's trace of 2026-10-25 found the change was his: his own words (his
rulings in OWNER-EDITS.json, his messages, his Substack edits of 2026-10-20), or a loss that happened after my version of
2026-10-18 (MY-FINAL-20261018.md), so in his edits or his answers 57 to 65. The trace looked up each finding's words in
my version, in his paste of 2026-10-20 and in the article now.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
DECIDED = {
    '1.9': 'stays: "live on" for "own" is small, in a paragraph of his rulings for section 1',
    '1.20': 'stays: his own (his messages say "psychopaths" four times; this is his anomie paragraph)',
    '1.23': 'stays: his Rule Scoring Sheet answer F2 took out the sentence it was in ("i don\'t think it was really needed")',
    '1.26': 'stays: an explanation in his voice that keeps his point',
    '2.6': 'IC-E1 (his own words, from his answer)', '2.10': 'IC-E2',
    '2.17': 'stays: his own Substack edit of 2026-10-20 took out the three names',
    '3.2': 'stays: a how-to rule in keeping with the manual', '3.4': 'stays: how-to questions in keeping with the manual',
    '3.6': 'IC-Q1', '3.25': 'IC-Q1', '7.15': 'IC-Q1',
    '3.18': 'stays: gone in his Substack edits of 2026-10-20', '3.19': 'stays: gone in his caveat cuts (answers 64 and 65)',
    '4.2': 'stays: gone in his caveat cuts (answers 64 and 65)', '4.8': 'stays: gone in his Substack edits of 2026-10-20',
    '4.11': 'stays: he kept the sentence (65.14 B)', '4.12': 'IC-T1',
    '6.6': 'stays: the added detail is right (the 1984 Island Pond raid: the judge found no specific case, and the children went home that day)',
    '7.1': 'stays: gone in his Substack edits of 2026-10-20', '7.5': 'stays: his own rewrite of the paragraph (his messages)',
    '7.7': 'stays: his own paragraph (his grandmother example, his messages)',
    '7.9': 'stays: gone in his caveat cuts (answers 64 and 65)', '7.11': 'stays: gone in his Substack edits of 2026-10-20',
    '7.14': 'stays: gone in his Substack edits of 2026-10-20', '7.19': 'stays: his own rewrite of the paragraph',
    '7.21': 'stays: the quote marks carry his point (a "right" that is only on paper)', '7.22': 'stays: "--" is his own style',
    '7.23': 'IC-E3', '7.24': 'IC-E3', '7.25': 'IC-E4 (the Zapatista example stays out: the list already has autonomous regional institutions)',
    '7.26': 'IC-E4', '8.6': 'stays: gone in his caveat cuts (answers 64 and 65)',
}


def main():
    R = json.loads((HERE / 'READS-ALL.json').read_text(encoding='utf-8'))
    m = [x for x in R if x['severity'] == 'matters' or x['kind'] == 'error']
    lines = ['# The strict Emulate check: what became of each community finding that matters', '',
             'Made by `triage.py` from `READS-ALL.json` (%d findings; %d marked "matters" or a slip). A card id is on the marking'
             ' page (`REVIEW-EMULATE.json`).' % (len(R), len(m)), '', '| Finding | Where | What the reader saw | What became of it |', '|---|---|---|---|']
    missing = []
    for x in m:
        fate = DECIDED.get(x['id']) or ('stays: ' + x['explained'] if x['explained'] else None)
        if fate is None:
            missing.append(x['id'])
            continue
        lines.append('| %s | %s | %s | %s |' % (x['id'], x['where'].replace('|', '/'), x.get('why', '').replace('|', '/')[:180], fate.replace('|', '/')))
    assert not missing, missing
    (HERE / 'TRIAGE.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(len(m), 'findings written')


if __name__ == '__main__':
    main()
