"""Score the 4.1 risk read (fix-20261020/risk41/RISK-ITEMS.json, written before any result was read) against a Pangram 4.1
result of the guide (a RESULT-41*.json saved from the check's page).

  python3 articles/inner-signal/humanize/fix-20261020/result41/score_forecast.py RESULT.json [RESULT.json ...] --out SCORE.md

Each forecast sentence is found in the checked text and given the reading of the window it falls in: red (AI-Generated),
light (Human, Medium or Low) or dark (Human, High); a sentence found in no checked text is "unchecked". Then the other
way round: each red window, and each red sentence, and whether the forecast named it. A sentence found in two results
(part B repeats Appendix A and the start of Appendix B) is scored with the later result.
"""
import argparse, collections, json, pathlib, re

D = pathlib.Path(__file__).resolve().parents[1]


def norm(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', t).strip()


def shade(w):
    if w['label'] != 'Human':
        return 'red'
    return 'dark' if w['confidence'] == 'High' else 'light'


def sentences(t):
    return [s for s in re.split(r'(?<=[.!?…])["”\')]*\s+', t.strip()) if len(s.split()) >= 3]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('results', nargs='+')
    ap.add_argument('--out', required=True)
    a = ap.parse_args(argv)
    items = json.loads((D / 'risk41' / 'RISK-ITEMS.json').read_text(encoding='utf-8'))
    results = [json.loads(pathlib.Path(p).read_text(encoding='utf-8')) for p in a.results]
    texts = [(norm(r['text']), r) for r in results]

    def reading(quote):
        q = norm(quote).rstrip('.!?')
        got = None
        for nt, r in texts:
            j = nt.find(q[:80])
            if j < 0:
                continue
            # map the normalized offset back by proportion of the raw text (the normalization only shrinks whitespace and quotes)
            raw = r['text']
            k = int(j * len(raw) / max(1, len(nt)))
            w = next((w for w in r['windows'] if w['start_index'] <= k < w['end_index']), r['windows'][-1])
            got = (shade(w), w)
        return got

    rows, table = [], collections.Counter()
    for it in items:
        rd = reading(it['quote'])
        sh = rd[0] if rd else 'unchecked'
        table[(it['kind'], sh)] += 1
        rows.append((it, sh))
    # recall: red windows and red sentences
    forecast = [(norm(it['quote']).rstrip('.!?')[:80], it['kind']) for it in items]
    win_rows, sent_hit, sent_all = [], 0, 0
    for nt, r in texts:
        for i, w in enumerate(r['windows']):
            if shade(w) != 'red':
                continue
            wt = norm(r['text'][w['start_index']:w['end_index']])
            named = [k for q, k in forecast if q and q in wt]
            ss = sentences(r['text'][w['start_index']:w['end_index']])
            hit = sum(any(q and (q in norm(s) or norm(s)[:60] in q) for q, _ in forecast) for s in ss)
            sent_hit += hit; sent_all += len(ss)
            win_rows.append((i, w['word_count'], w['confidence'], len(named), hit, len(ss), wt[:110]))
    checked = [r for r in rows if r[1] != 'unchecked']
    n_red = sum(1 for it, sh in checked if it['kind'] == 'RED')
    n_light = sum(1 for it, sh in checked if it['kind'] == 'LIGHT')
    out = ['# The 4.1 risk read against the result', '',
           'Results: %s. Forecast items in checked text: %d of %d (%d RED, %d LIGHT).' % (
               ', '.join(pathlib.Path(p).name for p in a.results), len(checked), len(rows), n_red, n_light), '',
           '| forecast | read red | read light green | read dark green |', '|---|---|---|---|']
    for k in ('RED', 'LIGHT'):
        out.append('| %s | %d | %d | %d |' % (k, table[(k, 'red')], table[(k, 'light')], table[(k, 'dark')]))
    out += ['', 'Precision: %d of %d forecast RED sentences read red (%s); %d read red or light green.' % (
        table[('RED', 'red')], n_red, '%.0f%%' % (100.0 * table[('RED', 'red')] / n_red) if n_red else '-',
        table[('RED', 'red')] + table[('RED', 'light')]),
        'Recall: the forecast named a sentence in %d of %d red windows; %d of %d sentences in red windows were named.' % (
            sum(1 for r in win_rows if r[3] or r[4]), len(win_rows), sent_hit, sent_all), '',
        '## Red windows', '', '| window | words | confidence | forecast items in it | sentences named | sentences | text |',
        '|---|---|---|---|---|---|---|']
    for i, wc, conf, n, hit, ns, t in win_rows:
        out.append('| %d | %d | %s | %d | %d | %d | %s |' % (i, wc, conf, n, hit, ns, t.replace('|', '/')))
    out += ['', '## Forecast RED sentences that read red', '']
    out += ['- part %d, %s: "%s" (pattern %d)' % (it['part'], it['section'], it['quote'], it['pattern'])
            for it, sh in checked if it['kind'] == 'RED' and sh == 'red']
    out += ['', '## Forecast sentences by pattern (checked text only)', '', '| pattern | RED forecast | of them red | LIGHT forecast | of them red or light |', '|---|---|---|---|---|']
    for p in range(1, 7):
        rr = [sh for it, sh in checked if it['pattern'] == p and it['kind'] == 'RED']
        ll = [sh for it, sh in checked if it['pattern'] == p and it['kind'] == 'LIGHT']
        out.append('| %d | %d | %d | %d | %d |' % (p, len(rr), rr.count('red'), len(ll), sum(s in ('red', 'light') for s in ll)))
    pathlib.Path(a.out).write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out[2:12]))


if __name__ == '__main__':
    main()
