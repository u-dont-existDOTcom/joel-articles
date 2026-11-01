"""Batch s1101's results, read (gate E306, E307, E278).

RESULTS.json is what the dashboard tab's reader returned for each section (the page's history, matched by SHA-256): the
headline, the AI likelihood, the words read, every window as "label, confidence, words", the time (UTC), the result's
link, and each window that isn't Human (High) with its words. This script writes:
- RESULTS.md: each section's result with its link and every window's confidence, and the try (1 of 2, the ledger's
  section cap);
- CONFIDENCE.md: every window that reads AI or Human (Low), to fix now (E306), and every Human (Medium) one, to list and
  to read again for meaning, each with the paragraphs it covers and whose words they are (his as published, his own
  words, or ours);
- s1101-results.json in the compact form fill_preds.py and pangram_ledger.py take.

  python3 articles/inner-signal/humanize/fix-20261101/sections/read_s1101.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' '})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(FLAT)).strip()


def main():
    secs = {s['key']: s for s in json.loads((HERE / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']}
    res = json.loads((HERE / 'RESULTS.json').read_text(encoding='utf-8'))
    preds = {p['key']: p for p in json.loads((HERE / 'PREDICTIONS.json').read_text(encoding='utf-8'))}
    import suggestion_review as sr
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    orig = '\n'.join(cr.loose(b['text']) for b in sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8')))
    cfg = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    import glob
    owner = sorted({f for g in cfg['owner'] for f in glob.glob(str(ROOT / g), recursive=True)})
    mine = cr.owner_paragraphs(owner, ROOT)

    def whose(i):
        q = cr.loose(bl[i]['text'])
        if q and q in orig:
            return 'his, as published'
        if cr.is_his(q, mine):
            return 'his own words'
        return 'ours'

    compact, rows, fix, med = {}, [], [], []
    for k, s in secs.items():
        r = res.get(k)
        if not r:
            rows.append('| %s | %s | %d | not read yet | | |' % (k, s['name'], s['words']))
            continue
        ws = r['windows']
        verdict = 'Human' if r['headline'].startswith('Human') else ('AI' if all(not w['label'].startswith('Human') for w in ws) else 'Mixed')
        conf = '; '.join('%s (%s%s), %d words' % ('Human' if w['label'] == 'Human' else 'AI', w['confidence'],
                                                 ', %.2f' % w['calibrated'] if w.get('calibrated') is not None else '',
                                                 w['words']) for w in ws)
        rows.append('| %s | %s | %d | [%s](%s), AI likelihood %.2f | %s | 1 of 2 |' % (
            k, s['name'], s['words'], r['headline'], r['link'], r['likelihood'], conf))
        compact[k] = [r['headline'], r['likelihood'], r['words'],
                      '; '.join('%s, %s, %d' % (w['label'], w['confidence'], w['words']) for w in ws),
                      r['utc'], r['link'], [w['label'] + ' (' + str(w['words']) + ' words): ' + w.get('text', '')
                                            for w in ws if w['label'] != 'Human']]
        for n, w in enumerate(ws, 1):
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            t = norm(w.get('text', ''))
            covers = [i for i in s['blocks'] if norm(bl[i]['text'])[:60] in t or t[:60] in norm(bl[i]['text'])
                      or (len(t) > 80 and t[20:80] in norm(bl[i]['text']))]
            item = {'key': k, 'section': s['name'], 'window': n, 'label': w['label'], 'confidence': w['confidence'],
                    'calibrated': w.get('calibrated'), 'words': w['words'], 'text': w.get('text', ''),
                    'blocks': covers, 'where': [sr.where(bl, i) for i in covers], 'whose': [whose(i) for i in covers],
                    'link': r['link']}
            (fix if (w['label'] != 'Human' or w['confidence'] == 'Low') else med).append(item)
    out = ['# Batch s1101: each section of the guide by itself, read', '',
           'Pangram 4.1 in his account (the web app), one check of each section alone (gate E307), try 1 of 2 for each '
           'section. Every window\'s confidence is given (E278); the windows to fix and to list are in CONFIDENCE.md.', '',
           '| key | section | words | result | windows | try |', '|---|---|---|---|---|---|'] + rows
    (HERE / 'RESULTS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    c = ['# Batch s1101: the windows below Human (High)', '',
         '## To fix now: AI or Human (Low) (E306)', '']
    for x in fix:
        c += ['- **%s, window %d** (%s): %s (%s%s), %d words, in %s; %s. [Result](%s)' % (
            x['key'], x['window'], x['section'], 'AI' if x['label'] != 'Human' else 'Human', x['confidence'],
            ', %.2f' % x['calibrated'] if x['calibrated'] is not None else '', x['words'],
            ', '.join(x['where']) or 'its section', ', '.join(sorted(set(x['whose']))) or 'not matched to a paragraph',
            x['link']), '', '  > ' + x['text'].strip().replace('\n', ' '), '']
    c += ['## To list, and to read again for meaning: Human (Medium)', '']
    for x in med:
        c.append('- %s, window %d (%s): Human (Medium%s), %d words, in %s; %s' % (
            x['key'], x['window'], x['section'], ', %.2f' % x['calibrated'] if x['calibrated'] is not None else '',
            x['words'], ', '.join(x['where']) or 'its section', ', '.join(sorted(set(x['whose']))) or 'not matched'))
    (HERE / 'CONFIDENCE.md').write_text('\n'.join(c) + '\n', encoding='utf-8')
    (HERE / 'CONFIDENCE.json').write_text(json.dumps({'fix': fix, 'medium': med}, ensure_ascii=False, indent=1) + '\n',
                                          encoding='utf-8')
    (HERE / 's1101-results.json').write_text(json.dumps(compact, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    from collections import Counter
    v = Counter(r[0] for r in compact.values())
    print(len(compact), 'read;', dict(v), '; to fix', len(fix), '; medium', len(med))
    print('right calls:', sum(1 for k, r in compact.items() if (preds[k]['call'] == 'Human') == r[0].startswith('Human')))


if __name__ == '__main__':
    main()
