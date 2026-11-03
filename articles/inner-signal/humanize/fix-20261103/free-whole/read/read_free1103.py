"""The whole guide's third free check (3 November; guide 7e77327d), read: every window below High (none read AI), the
paragraphs it covers and whose words they are (gate E306: fix every one; E312: whose words goes by paragraph), and the
shading of both parts for the ledger.

Joel's two result pages came with his message of 11:19 UTC (../joel-20261103-1119-message.txt); RESULT-A/B.json are
make_results.py's. A window's text is the checked text between its indexes; it is found in the guide's blocks with
compare_read.loose (letters and digits only). Whose words are read as in ../../../fix-20261102/free-whole-2/read/
read_free1102.py (his published version, the paragraphs he wrote or rewrote, his inner child guide), with the
near-verbatim test of ../../overcompletion/collect.py, so a sentence of his with a typo fixed counts as his. The guide is
HUMANIZED-SO-FAR.md as checked (../CANDIDATE-MASTER.md). This file lists Medium windows too, for the record, but only
Low ones are work (E278: "fix any segments that are not high confidence human"; a Medium window of one to five words is
a list number, a heading's seam or a short line).

  python3 articles/inner-signal/humanize/fix-20261103/free-whole/read/read_free1103.py
Writes WINDOWS.json and WINDOWS.md here.
"""
import collections
import difflib
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
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402


def shading(ws):
    c = collections.Counter((w['label'].split('-')[0], w['confidence']) for w in ws)
    ai = sum(v for (l, _), v in c.items() if l == 'AI')
    hu = sum(v for (l, _), v in c.items() if l == 'Human')
    part = lambda l: ', '.join('%d %s' % (c[(l, k)], k) for k in ('High', 'Medium', 'Low') if c[(l, k)])
    return '%d windows: %d AI (%s), %d Human (%s)' % (len(ws), ai, part('AI') or 'none', hu, part('Human'))


def main():
    md = (X / 'CANDIDATE-MASTER.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    flat, pos, parts = [], 0, []
    for b in bl:
        if b['level']:
            continue   # the check leaves headings out, so a window can run from one section into the next
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
        return [i for a, e, i in flat if a < end and e > at]

    orig_blocks = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
    orig = '\n'.join(cr.loose(b['text']) for b in orig_blocks)
    orig_ss = [cr.loose(x) for b in orig_blocks for x in cr.sentences(b['text']) if len(x.split()) >= 4]
    cfg = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    owner = sorted({f for g in cfg['owner'] for f in glob.glob(str(ROOT / g), recursive=True)})
    mine = cr.owner_paragraphs(owner, ROOT)
    icg_text = (H / 'fix-20261025' / 'ic-align' / 'IC-GUIDE.txt').read_text(encoding='utf-8')
    icg = cr.loose(icg_text)

    def near(x, pool):
        for y in pool:
            if abs(len(y) - len(x)) > max(12, len(x) // 4):
                continue
            sm = difflib.SequenceMatcher(None, x, y, autojunk=False)
            if sm.real_quick_ratio() >= 0.85 and sm.quick_ratio() >= 0.85 and sm.ratio() >= 0.85:
                return True
        return False

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
        if ss and any(near(x, orig_ss) for x in ss):
            return 'his, as published (near-verbatim)'
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
            if label == 'Human' and w['confidence'] == 'High':
                continue
            wtext = r['text'][w['start_index']:w['end_index']]
            if not cr.loose(wtext):
                continue
            covers = locate(wtext)
            items.append({'part': part, 'window': n, 'label': label, 'confidence': w['confidence'],
                          'calibrated': round(w['calibrated_confidence'], 3), 'words': w['word_count'],
                          'text': ' '.join(wtext.split()), 'blocks': covers, 'where': [sr.where(bl, i) for i in covers],
                          'whose': [whose(i, wtext) for i in covers], 'link': r['link'],
                          'work': label == 'AI' or w['confidence'] == 'Low'})
    (HERE / 'WINDOWS.json').write_text(json.dumps({'guide_sha256': __import__('hashlib').sha256(md.encode('utf-8')).hexdigest(),
                                                   'parts': shades, 'windows': items}, ensure_ascii=False, indent=1) + '\n',
                                       encoding='utf-8')
    out = ['# The whole guide\'s third free check (3 November): the windows below High, with whose words', '',
           'Joel\'s result pages (his message of 11:19 UTC): [part A](%s), %s, %.6f%% AI, %s; [part B](%s), %s, %.6f%% AI, %s. '
           'No window reads AI. E306 and E278: fix every Human (Low) window where a fix keeps his meaning and form; the '
           'Medium ones are listed for the record.' % (
               shades['A']['link'], shades['A']['headline'], shades['A']['fraction_ai'] * 100, shades['A']['shading'],
               shades['B']['link'], shades['B']['headline'], shades['B']['fraction_ai'] * 100, shades['B']['shading']), '',
           '## Human (Low): the work', '']
    for x in [x for x in items if x['work']]:
        out += ['- **Part %s, window %d**: %s (%s, %.3f), %d words, %s; %s' % (
            x['part'], x['window'], x['label'], x['confidence'], x['calibrated'], x['words'], '; '.join(x['where']) or '?',
            '; '.join(sorted(set(x['whose'])))), '', '  > ' + x['text'], '']
    out += ['## Human (Medium), for the record', '']
    for x in [x for x in items if not x['work']]:
        out += ['- Part %s, window %d, %d words, %s: "%s"' % (x['part'], x['window'], x['words'], '; '.join(x['where']) or '?',
                                                          x['text'][:120])]
    (HERE / 'WINDOWS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(shades['A']['shading']); print(shades['B']['shading'])
    for x in [x for x in items if x['work']]:
        print(x['part'], x['window'], x['confidence'], x['words'], x['blocks'], x['where'], sorted(set(x['whose'])))
        print('   ', x['text'])


if __name__ == '__main__':
    main()
