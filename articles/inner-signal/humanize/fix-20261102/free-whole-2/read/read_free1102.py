"""The whole guide's second free check of 2 November (after batch f1102; guide 66eb95e7), read: every window that reads AI or Human (Low), the paragraphs it covers,
the section they belong to and whose words they are (gate E306: fix every one; E312: whose words goes by paragraph), and
the shading of both parts for the ledger.

Joel's two result pages came with his message of 23:07 UTC (../joel-20261102-2307-message.txt); RESULT-A/B.json are
make_results.py's. A window's text is the checked text between its indexes; it is found in the guide's blocks with
compare_read.loose (letters and digits only), which gives the blocks it covers. Sections and whose words are read as in
../../whole/read_w1102.py (batch s1101's sections, carried to the guide's blocks; his published version, the paragraphs he
wrote or rewrote, his inner child guide). The guide is HUMANIZED-SO-FAR.md as checked (66eb95e7, ../CANDIDATE-MASTER.md).

  python3 articles/inner-signal/humanize/fix-20261102/free-whole-2/read/read_free1102.py
Writes WINDOWS.json and WINDOWS.md here.
"""
import collections
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
X = HERE.parent
F = X.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(F / 'whole'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
import read_w1102 as prev  # noqa: E402


def shading(ws):
    c = collections.Counter((w['label'].split('-')[0].replace('AI', 'AI'), w['confidence']) for w in ws)
    ai = sum(v for (l, _), v in c.items() if l == 'AI')
    hu = sum(v for (l, _), v in c.items() if l == 'Human')
    part = lambda l: ', '.join('%d %s' % (c[(l, k)], k) for k in ('High', 'Medium', 'Low') if c[(l, k)])
    return '%d windows: %d AI (%s), %d Human (%s)' % (len(ws), ai, part('AI') or 'none', hu, part('Human'))


def main():
    md = (X / 'CANDIDATE-MASTER.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    flat, pos = [], 0
    parts = []
    for b in bl:
        s = cr.loose(b['text'])
        flat.append((pos, pos + len(s), b['i']))
        parts.append(s)
        pos += len(s) + 1
    whole = ' '.join(parts)

    def locate(wtext):
        q = cr.loose(wtext)
        at = whole.find(q)
        if at < 0 and len(q) > 40:
            at = whole.find(q[:40])
        assert at >= 0, wtext[:80]
        end = at + len(q)
        return [i for a, b, i in flat if a < end and b > at]

    m = prev.current_index_maps()
    secs = json.loads((H / 'fix-20261101' / 'sections' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']
    sec_of = {}
    for s in secs:
        for old in s['blocks']:
            for i in m.get(old, []):
                sec_of[i] = s
    orig = '\n'.join(cr.loose(b['text']) for b in sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8')))
    cfg = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    owner = sorted({f for g in cfg['owner'] for f in glob.glob(str(ROOT / g), recursive=True)})
    mine = cr.owner_paragraphs(owner, ROOT)
    icg = cr.loose((H / 'fix-20261025' / 'ic-align' / 'IC-GUIDE.txt').read_text(encoding='utf-8'))

    def whose(i, wtext):
        q = cr.loose(bl[i]['text'])
        if q and q in orig:
            return 'his, as published'
        if cr.is_his(q, mine):
            return 'his own words (a paragraph he wrote or rewrote)'
        ss = [cr.loose(x) for x in cr.sentences(wtext) if len(x.split()) >= 4]
        if ss and all(x in orig for x in ss):
            return 'his, as published (the sentence)'
        if ss and all(x in icg for x in ss):
            return 'his, from his inner child guide'
        if ss and any(x in orig or x in icg for x in ss):
            return 'partly his (published or inner child guide), partly ours'
        return 'ours'

    items, shades = [], {}
    for part in ('A', 'B'):
        r = json.loads((HERE / ('RESULT-%s.json' % part)).read_text(encoding='utf-8'))
        shades[part] = {'link': r['link'], 'headline': r['headline'], 'fraction_ai': r['fraction_ai'],
                        'words': r['word_count'], 'shading': shading(r['windows'])}
        for n, w in enumerate(r['windows'], 1):
            label = 'AI' if w['label'].startswith('AI') else 'Human'
            if label == 'Human' and w['confidence'] != 'Low':
                continue
            wtext = r['text'][w['start_index']:w['end_index']]
            if not cr.loose(wtext):
                continue
            covers = locate(wtext)
            s = sec_of.get(covers[0]) if covers else None
            items.append({'part': part, 'window': n, 'label': label, 'confidence': w['confidence'],
                          'calibrated': round(w['calibrated_confidence'], 3), 'words': w['word_count'],
                          'text': ' '.join(wtext.split()), 'blocks': covers, 'where': [sr.where(bl, i) for i in covers],
                          'section': s['key'] if s else None, 'section_name': s['name'] if s else None,
                          'whose': [whose(i, wtext) for i in covers], 'link': r['link']})
    (HERE / 'WINDOWS.json').write_text(json.dumps({'parts': shades, 'windows': items}, ensure_ascii=False, indent=1) + '\n',
                                       encoding='utf-8')
    out = ['# The whole guide\'s second free check of 2 November: the windows to fix (AI or Human (Low)), with whose words', '',
           'Joel\'s result pages (his message of 23:07 UTC): [part A](%s), %s, %.2f%% AI, %s; [part B](%s), %s, %.2f%% AI, %s. '
           'E306: fix every AI or Human (Low) window where a fix keeps his meaning and form.' % (
               shades['A']['link'], shades['A']['headline'], shades['A']['fraction_ai'] * 100, shades['A']['shading'],
               shades['B']['link'], shades['B']['headline'], shades['B']['fraction_ai'] * 100, shades['B']['shading']), '']
    for x in items:
        out += ['- **Part %s, window %d**: %s (%s), %d words, %s; %s; %s' % (
            x['part'], x['window'], x['label'], x['confidence'], x['words'], '; '.join(x['where']) or '?',
            x['section'] or '?', '; '.join(sorted(set(x['whose'])))), '', '  > ' + x['text'], '']
    (HERE / 'WINDOWS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(shades['A']['shading']); print(shades['B']['shading'])
    print(len(items), 'windows;', collections.Counter(x['label'] + ' ' + x['confidence'] for x in items))
    print(collections.Counter('; '.join(sorted(set(x['whose']))) for x in items))


if __name__ == '__main__':
    main()
