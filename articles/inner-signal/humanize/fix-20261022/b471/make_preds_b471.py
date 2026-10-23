"""Batch 471g's forecasts, written before any check (2026-10-22): batch/PREDICTIONS.md and batch/FORECAST.json, one row per
changed paragraph as Pangram would read it in the next whole-guide recheck (as make_preds_b470.py).

No paragraph goes to pangram.com (gate E200): both are read in the real article through the temporary Substack drafts.
The forced-adulthood paragraph read Human, high, in the recheck of 2026-10-21 (part A, window 21), and gains a named term
in brackets and a changed simile. The three-roles step sat in part B's red window 16, the 518 words from Appendix B's last
list into Appendix C's prose; its row says what I expect for the step's own stretch, which depends on what Appendix C and
Appendix B's lists read around it.

  python3 articles/inner-signal/humanize/fix-20261022/b471/make_preds_b471.py   (from the repo root)
"""
import json, pathlib

B = pathlib.Path(__file__).resolve().parent
P = {
    'b471-forced-adulthood': ('Human', 0.8, 'a term in brackets, Joel\'s own ("what I call forced adulthood"), and "a baby bird" '
                                            'for "them" in the simile, in a paragraph that read dark green',
                              'a bracketed coinage; a simile at the paragraph\'s end',
                              '"The problem is, that", the casual "just ... just", the run of three ways in'),
    'b471-three-roles': ('AI', 0.35, 'the step gains its three jobs in brackets and Joel\'s clarification as a second sentence; '
                                     'the stretch around it (Appendix B\'s lists and Appendix C\'s opening) read AI, high, as one '
                                     'window',
                         'three parallel infinitives ("to warm", "to make it safe", "to point a direction") in a list of '
                         'steps', 'Joel\'s own clarification ("if need be", "coming together as well"), "3" as a numeral'),
}


def main():
    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    out, lines = {}, ['# Batch 471g: what I expect each changed paragraph to read in the next whole-guide recheck', '',
                      'Written by `make_preds_b471.py` before any check. Each row is one changed paragraph as Pangram reads '
                      'it (alone, or with a neighbor when under 50 words). "Was" is its reading in the recheck of '
                      '2026-10-21.', '', '| Paragraph | Section | Was | Call | Chance of Human | Why |', '|---|---|---|---|---|---|']
    was = {'b471-three-roles': 'red'}
    for k, t in meta['texts'].items():
        call, chance, why, tells, human = P[k]
        r = t.get('reading_41') or {}
        out[k] = {'lineage': t['lineage'], 'call': call, 'chance': chance, 'why': why, 'tells': tells, 'human_tells': human,
                  'words': t['words'], 'first_words': ' '.join(drafts[k].split()[:12]), 'was': r.get('shade') or was.get(k)}
        lines.append('| %s | %s | %s | %s | %.2f | %s |' % (k, t['section'], out[k]['was'], call, chance, why))
    (B / 'batch').mkdir(exist_ok=True)
    (B / 'batch' / 'FORECAST.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'batch' / 'PREDICTIONS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(len(out), 'forecasts')


if __name__ == '__main__':
    main()
