#!/usr/bin/env python3
"""Turn 110: API-CHECKS.md, a page Joel can open for this turn's API checks (copied from experiments/t109-api/results_page.py).

Reads API-RESULTS-*.jsonl (the lines pangram_api.py printed with --windows) and NAMES.json and writes each check's text
with its windows marked: an AI window in bold, a Human window with Low or Medium confidence in italics, each with its label
(his 2026-10-25 ask, "save all the sections that pangram marked as less than human high confidence"). The page is a view
rebuilt every round, so its name has no RESULT in it (CORRECTION-T97.md)."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
NAMES = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/'


def marked(windows):
    out = []
    for label, conf, words, start, end, text in windows:
        for i, piece in enumerate(text.split('\n')):
            if i:
                out.append('\n\n')
            lead = len(piece) - len(piece.lstrip())
            if piece.strip() and label != 'Human Written':
                out.append(piece[:lead] + '**[%s, %s] %s**' % ('AI' if label == 'AI-Generated' else label, conf, piece.strip()))
            elif piece.strip() and conf != 'High':
                out.append(piece[:lead] + '*[Human, %s] %s*' % (conf, piece.strip()))
            else:
                out.append(piece)
    return ''.join(out)


def main():
    lines = ['# Turn 110\'s API checks (Pangram 4.1)', '',
             'Each check went through Joel\'s API key ([pangram_api.py](%stools/humanization/pangram_api.py)). An AI window would be in '
             '**bold** and a Human window with Low or Medium confidence is in *italics*, each with its label; everything else read '
             'Human with High confidence. The predictions are in [the ledger](%sarticles/inner-child-therapy/tools/pangram-ledger.jsonl) '
             '(batches t110-api-1 and t110-api-2). Each check is a heading below, so its link is this page with #name at the end.' % (BLOB, BLOB), '']
    for f in sorted(HERE.glob('API-RESULTS-*.jsonl')):
        for l in f.read_text(encoding='utf-8').splitlines():
            r = json.loads(l)
            fr = r['fraction_ai'] or 0
            pct = ('%.2f' % (100 * fr)) if 0.00005 <= fr < 0.01 else '%d' % round(100 * fr)
            lines += ['## %s' % r['name'], '', '%s.' % NAMES.get(r['name'], ''), '',
                      '**%s** (%s), %s%% AI, %d words, Pangram %s, %s.' % (r['headline'], r['prediction_short'], pct, r['words'],
                                                                          r['version'], r['utc']), '',
                      'Pangram\'s public page: %s' % r.get('dashboard_link', ''), '',
                      marked(r['windows']), '']
    (HERE / 'API-CHECKS.md').write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
    print('wrote', HERE / 'API-CHECKS.md')


if __name__ == '__main__':
    main()
