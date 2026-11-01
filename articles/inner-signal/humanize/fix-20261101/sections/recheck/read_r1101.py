"""Batch r1101's results, read: the second and last check of eleven sections by themselves (gate E307), every window's
confidence (E278), and what is left to fix (E306).

RESULTS.json is what the dashboard tab returned for each section (the page's history, matched by SHA-256): headline, AI
likelihood, words, time (UTC), the result's link, and every window (label, confidence, words, character offsets in the
text as checked, its words, and Pangram's likelihood for it). This script writes:
- RESULTS.md: each section's result beside its first check's, with every window's confidence;
- CONFIDENCE.md / .json: every window below Human (High), with the paragraphs it covers and whose words they are (his as
  published, his own words, his inner child guide's, exact or near, E314; or ours);
- r1101-results.json in the compact form fill_preds.py and pangram_ledger.py take.

  python3 articles/inner-signal/humanize/fix-20261101/sections/recheck/read_r1101.py
"""
import difflib
import glob
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
H = D.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' '})


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').translate(FLAT)).strip()


def lab(w):
    return '%s (%s)' % ('Human' if w['label'] == 'Human' else 'AI', w['confidence'])


def main():
    secs = {s['key']: s for s in json.loads((HERE / 'SECTIONS-R1101.json').read_text(encoding='utf-8'))['sections']}
    res = json.loads((HERE / 'RESULTS.json').read_text(encoding='utf-8'))
    first = json.loads((D / 'RESULTS.json').read_text(encoding='utf-8'))
    preds = {p['key']: p for p in json.loads((HERE / 'PREDICTIONS.json').read_text(encoding='utf-8'))}
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    orig = '\n'.join(cr.loose(b['text']) for b in sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8')))
    cfg = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    owner = sorted({f for g in cfg['owner'] for f in glob.glob(str(ROOT / g), recursive=True)})
    mine = cr.owner_paragraphs(owner, ROOT)
    icg_raw = (H / 'fix-20261025' / 'ic-align' / 'IC-GUIDE.txt').read_text(encoding='utf-8')
    icg = cr.loose(icg_raw)
    ic_sents = [cr.loose(x) for x in cr.sentences(icg_raw) if len(x.split()) >= 3]

    def whose(i, wtext=''):
        q = cr.loose(bl[i]['text'])
        if q and q in orig:
            return 'his, as published'
        if cr.is_his(q, mine):
            return 'his own words (a paragraph he wrote or rewrote)'
        tags = set()
        for x in cr.sentences(wtext or bl[i]['text']):
            lx = cr.loose(x)
            if len(x.split()) < 3:
                continue
            if lx in orig:
                tags.add('published')
            elif lx in icg or max(difflib.SequenceMatcher(None, lx, y).ratio() for y in ic_sents) >= 0.7:
                tags.add('inner child guide')
            else:
                tags.add('ours')
        if tags == {'ours'} or not tags:
            return 'ours'
        if 'ours' in tags:
            return 'partly his (%s), partly ours' % ', '.join(sorted(tags - {'ours'}))
        return 'his (%s)' % ', '.join(sorted(tags))

    rows, compact, below = [], {}, []
    for k, s in secs.items():
        r = res.get(k)
        if not r:
            rows.append('| %s | %s | %d | not read | | |' % (k, s['name'], s['words']))
            continue
        f = first[s['first']]
        ws = r['windows']
        conf = '; '.join('%s, %d words' % (lab(w), w['words']) for w in ws)
        rows.append('| %s | %s | %d | [%s](%s), AI likelihood %.3f | %s | [%s](%s), %.3f |' % (
            k, s['name'].replace('|', '/'), s['words'], r['headline'], r['link'], r['likelihood'], conf, f['headline'],
            f['link'], f['likelihood']))
        compact[k] = [r['headline'], round(r['likelihood'], 2), r['words'],
                      '; '.join('%s, %s, %d' % (w['label'], w['confidence'], w['words']) for w in ws),
                      r['utc'][11:19], '/' + r['link'].rsplit('/', 1)[-1],
                      [w['label'] + ' (' + str(w['words']) + ' words): ' + w.get('text', '') for w in ws
                       if w['label'] != 'Human']]
        for n, w in enumerate(ws, 1):
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            t = norm(w.get('text', ''))
            covers = [i for i in s['blocks'] if t and (norm(bl[i]['text'])[:60] in t or t[:60] in norm(bl[i]['text'])
                                                       or (len(t) > 80 and t[20:80] in norm(bl[i]['text'])))]
            below.append({'key': k, 'first': s['first'], 'section': s['name'], 'window': n, 'label': w['label'],
                          'confidence': w['confidence'], 'words': w['words'], 'text': w.get('text', ''),
                          'ai_likelihood': w.get('ai_likelihood'), 'blocks': covers,
                          'where': [sr.where(bl, i) for i in covers],
                          'whose': [whose(i, w.get('text', '')) for i in covers], 'link': r['link'],
                          'fix': w['label'] != 'Human' or w['confidence'] == 'Low'})
    out = ['# Batch r1101: the second and last check of eleven sections by themselves, read', '',
           'Pangram 4.1 in his account (the web app), each section alone (gate E307), try 2 of 2, beside its first check of '
           '1 November (../RESULTS.md). Every window\'s confidence is given (E278); the windows below Human (High) are in '
           'CONFIDENCE.md.', '',
           '| key | section | words | result | windows | first check |', '|---|---|---|---|---|---|'] + rows
    (HERE / 'RESULTS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    c = ['# Batch r1101: the windows below Human (High)', '', '## AI or Human (Low)', '']
    for x in [b for b in below if b['fix']] or []:
        c += ['- **%s, window %d** (%s): %s, %d words, in %s; %s. [Result](%s)' % (
            x['key'], x['window'], x['section'], lab(x), x['words'], ', '.join(x['where']) or 'its section',
            ', '.join(sorted(set(x['whose']))) or 'not matched to a paragraph', x['link']), '',
              '  > ' + x['text'].strip().replace('\n', ' '), '']
    if not any(b['fix'] for b in below):
        c += ['None.', '']
    c += ['## Human (Medium)', '']
    for x in [b for b in below if not b['fix']]:
        c.append('- %s, window %d (%s): Human (Medium), %d words, in %s; %s: "%s"' % (
            x['key'], x['window'], x['section'], x['words'], ', '.join(x['where']) or 'its section',
            ', '.join(sorted(set(x['whose']))) or 'not matched', norm(x['text'])[:120]))
    (HERE / 'CONFIDENCE.md').write_text('\n'.join(c) + '\n', encoding='utf-8')
    (HERE / 'CONFIDENCE.json').write_text(json.dumps(below, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'r1101-results.json').write_text(json.dumps(compact, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    from collections import Counter
    v = Counter(r[0] for r in compact.values())
    print(len(compact), 'read;', dict(v), '; below High:', len(below), '(to fix %d)' % sum(1 for b in below if b['fix']))
    print('right calls:', sum(1 for k, r in compact.items() if (preds[k]['call'] == 'Human') == r[0].startswith('Human')),
          'of', len(compact))


if __name__ == '__main__':
    main()
