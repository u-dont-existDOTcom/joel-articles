"""Batch 472g's API checks as a page Joel can open (E214: an API check has no Pangram page, so its link is its heading
here): API-CHECKS.md, one heading per check from API-RESULTS-*.jsonl (pangram_api.py's lines, with --windows), the AI
windows in bold with their label and confidence. It also prints each check's link, for the ledger.

  python3 articles/inner-signal/humanize/fix-20261023/b472/api_page.py   (from the repo root)
"""
import json, pathlib

B = pathlib.Path(__file__).resolve().parent
PAGE = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/'
        'fix-20261023/b472/API-CHECKS.md')
WHAT = {
    's1': 'De-hypnosis P1 with P2 after it (recheck A: the run of questions read AI, Low and one Medium, in part 7)',
    's2': 'the induction section\'s last paragraph with Come all the way back P1 (recheck A: High, part 9)',
    's3': 'Come all the way back P3 (the count) with P4 (recheck A: "Get up only ..." to "... done the count." Low, part 9)',
}


def link(name):
    return PAGE + '#' + name.lower()


def main():
    rows = []
    for f in sorted(B.glob('API-RESULTS-*.jsonl')):
        rows += [json.loads(l) for l in f.read_text(encoding='utf-8').splitlines() if l.strip()]
    cands = json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))
    out = ['# Batch 472g\'s API checks (Pangram 4.1)', '',
           'Each check went through Joel\'s API key (`tools/humanization/pangram_api.py`, run on his laptop). AI windows are '
           'in **bold**, with their label and confidence; everything else read Human. The predictions are in '
           '`../../pangram-ledger.jsonl` (batch 472g); the candidates and why are in `make_b472.py` and `DRAFTS.md`. Each '
           'check is a heading below, so its link is this page with #name at the end.', '']
    for r in rows:
        c = cands[r['name']]
        kind = 'as it stands' if r['name'].endswith('_base') else 'candidate %s' % r['name'][-1]
        out += ['## %s' % r['name'], '', '%s, %s.' % (WHAT[c['stretch']], kind), '',
                '**%s** (%s), %.0f%% AI, %d words, Pangram %s, %s.' % (r['headline'], r['prediction_short'],
                                                                       100 * r['fraction_ai'], r['words'], r['version'],
                                                                       r['utc']), '']
        parts = []
        for label, conf, words, a, b, text in r['windows']:
            if label.startswith('AI'):
                # bold each line of the window on its own, so a window that crosses a paragraph keeps its bold
                pieces, tag = [], '[AI, %s] ' % conf
                for k, line in enumerate(text.split('\n')):
                    lead = line[:len(line) - len(line.lstrip())]
                    pieces.append(lead + ('**%s%s**' % (tag if k == 0 else '', line.strip()) if line.strip() else ''))
                parts.append('\n'.join(pieces))
            else:
                parts.append(text)
        out += [x.strip() for x in ''.join(parts).split('\n')]
        out.append('')
    (B / 'API-CHECKS.md').write_text('\n\n'.join(x for x in out if x) + '\n', encoding='utf-8')
    for r in rows:
        print(r['name'], r['headline'], link(r['name']))


if __name__ == '__main__':
    main()
