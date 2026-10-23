#!/usr/bin/env python3
"""Turn 102: API-CHECKS.md, a page Joel can open for this turn's API checks (copied from experiments/t100-api/results_page.py;
E214: every stretch I ask him to fix comes with the check that shows it). Since turn 98 each API check also has a public
Pangram page (E227), linked under its heading here.

Reads API-RESULTS-*.jsonl (the lines pangram_api.py printed with --windows) and NAMES.json, and writes each check's
text with its AI windows in bold, labelled with their confidence. The page is a view rebuilt every round, so its name has no
RESULT in it: scripts/register_article_artifacts.py makes every experiments/*RESULT* file a detector result that never changes
(API-RESULTS.md is round 1's page as first written; CORRECTION-T97.md).
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
NAMES = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))


def marked(windows):
    out = []
    for label, conf, words, start, end, text in windows:
        pieces = text.split('\n')
        for i, piece in enumerate(pieces):
            if i:
                out.append('\n\n')
            if piece.strip() and label != 'Human Written':
                tag = 'AI' if label == 'AI-Generated' else label
                lead = len(piece) - len(piece.lstrip())
                out.append(piece[:lead] + '**[%s, %s] %s**' % (tag, conf, piece.strip()))
            else:
                out.append(piece)
    return ''.join(out)


def main():
    lines = ['# Turn 102\'s API checks (Pangram 4.1)', '',
             'Each check went through Joel\'s API key (`tools/humanization/pangram_api.py`). AI windows are in **bold**, with '
             'their label and confidence; everything else read Human. The predictions are in `../../tools/pangram-ledger.jsonl` '
             '(batches t102-api, t102-api-2 and t102-api-3). Each check is a heading below, so its link is this page with #name at the end.', '']
    for f in sorted(HERE.glob('API-RESULTS-*.jsonl')):
        for l in f.read_text(encoding='utf-8').splitlines():
            r = json.loads(l)
            pct = round(100 * (r['fraction_ai'] or 0))
            lines += ['## %s' % r['name'], '', '%s.' % NAMES.get(r['name'], ''), '',
                      '**%s** (%s), %d%% AI, %d words, Pangram %s, %s.' % (r['headline'], r['prediction_short'], pct, r['words'],
                                                                          r['version'], r['utc']), '',
                      'Pangram\'s public page: %s' % r.get('dashboard_link', ''), '',
                      marked(r['windows']), '']
    (HERE / 'API-CHECKS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('wrote', HERE / 'API-CHECKS.md')


if __name__ == '__main__':
    main()
