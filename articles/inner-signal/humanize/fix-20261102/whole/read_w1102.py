"""Batch w1102's windows, read: every window of the whole-guide check that reads AI or Human (Low), the paragraphs it covers,
the section they belong to and whose words they are (gate E306: fix every one; E312: whose words goes by paragraph).

Joel, 2026-11-02 19:11 UTC (../joel-20261102-1911-message.txt): "but you're saying we still ahve to fix some stretches",
and "28a": one more check of the whole section after each fix, each with my prediction written first.

The two halves were made from the guide's blocks joined by blank lines (make_whole.py); each window's own text, as the
API gives it, is found in its half with spaces collapsed, which gives the blocks it covers. Sections are batch s1101's
(../../fix-20261101/sections/SECTIONS.json), carried to the guide as it is now through APPLIED-S1101.json's block map and
APPLIED-R1102.json (block 282, the script, cut), so a section's checks keep their lineage (HG1101-NN).

  python3 articles/inner-signal/humanize/fix-20261102/whole/read_w1102.py
Writes WINDOWS.json and WINDOWS.md here.
"""
import glob
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

L = 'https://www.pangram.com/history/'


def current_index_maps():
    """s1101 block index -> current (a789009c) block indices."""
    bm = json.loads((F / 'APPLIED-S1101.json').read_text(encoding='utf-8'))['block_map']
    out = {}
    for old, new in bm.items():
        cur = []
        for i in new:
            if i == 282:          # W-283b: the script cut (APPLIED-R1102.json)
                continue
            cur.append(i if i < 282 else i - 1)
        out[int(old)] = cur
    return out


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    texts = json.loads((HERE / 'TEXTS.json').read_text(encoding='utf-8'))
    log = [json.loads(x) for x in (HERE / 'API-ROUND1.log').read_text(encoding='utf-8').splitlines()]
    k = [b['i'] for b in bl if b['level'] == 1 and b['text'] == 'The 15-minute daily practice'][0]
    halves = {'w1102-A': list(range(0, k)), 'w1102-B': list(range(k, len(bl)))}
    spans = {}
    for key, idx in halves.items():
        pos, sp = 0, []
        for i in idx:
            sp.append((pos, pos + len(bl[i]['text']), i))
            pos += len(bl[i]['text']) + 2
        assert '\n\n'.join(bl[i]['text'] for i in idx) == texts[key], key
        spans[key] = sp
    # the window's own text (the API gives it), found in the half with spaces collapsed, gives the blocks it covers
    flat = {}
    for key, idx in halves.items():
        pos, sp, parts = 0, [], []
        for i in idx:
            s = ' '.join(bl[i]['text'].split())
            sp.append((pos, pos + len(s), i))
            parts.append(s)
            pos += len(s) + 1
        flat[key] = (' '.join(parts), sp)

    def locate(wtext, fk):
        whole, sp = fk
        at = whole.find(wtext)
        if at < 0:
            at = whole.find(wtext[:60])
        assert at >= 0, wtext[:80]
        end = at + len(wtext)
        return [i for a, b, i in sp if a < end and b > at]

    m = current_index_maps()
    secs = json.loads((F.parent / 'fix-20261101' / 'sections' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']
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

    items = []
    for d in log:
        key, t = d['name'], texts[d['name']]
        for n, w in enumerate(d['windows'], 1):
            label = 'AI' if w[0].lower().startswith('ai') else 'Human'
            if label == 'Human' and w[1] != 'Low':
                continue
            wtext = ' '.join((w[5] or '').split())
            covers = locate(wtext, flat[key])
            s = sec_of.get(covers[0]) if covers else None
            items.append({'half': key, 'window': n, 'label': label, 'confidence': w[1], 'words': w[2], 'text': wtext,
                          'blocks': covers, 'where': [sr.where(bl, i) for i in covers],
                          'section': s['key'] if s else None, 'section_name': s['name'] if s else None,
                          'whose': [whose(i, wtext) for i in covers], 'link': d['dashboard_link']})
    (HERE / 'WINDOWS.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = ['# Batch w1102: the windows to fix (AI or Human (Low)), with whose words they are', '',
           'From the whole-guide check in two halves ([A](%s), [B](%s)); E306: fix every AI or Human (Low) window.' % (
               log[0]['dashboard_link'], log[1]['dashboard_link']), '']
    for x in items:
        out += ['- **%s, window %d**: %s (%s), %d words, in %s (%s); %s' % (
            x['half'], x['window'], x['label'], x['confidence'], x['words'], x['section_name'] or '?', x['section'] or '?',
            '; '.join(sorted(set(x['whose'])))), '', '  > ' + x['text'].replace('\n', ' '), '']
    (HERE / 'WINDOWS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    from collections import Counter
    print(len(items), 'windows;', Counter(x['label'] + ' ' + x['confidence'] for x in items))
    print(Counter('; '.join(sorted(set(x['whose']))) for x in items))
    print(Counter(x['section'] for x in items))


if __name__ == '__main__':
    main()
