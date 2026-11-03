"""Collect the six readers' overcompletion candidates (reads/READ-1.json to READ-6.json), check that each cut is the guide's
text exactly, and say whose words each one is, the way the free checks' readings do (read_free1102.py): his published
guide, a paragraph he wrote or rewrote himself, his inner child guide, or ours.

  python3 articles/inner-signal/humanize/fix-20261103/overcompletion/collect.py
Writes CANDIDATES.json and CANDIDATES.md here.
"""
import glob
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
SHA = '090588f72475fbddf5528b9db50193bf50572fc5f99542a52fab02e36db15de0'


def main():
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == SHA, 'the guide changed since the read'
    bl = sr.blocks(md)
    orig = '\n'.join(cr.loose(b['text']) for b in sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8')))
    cfg = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    owner = sorted({f for g in cfg['owner'] for f in glob.glob(str(ROOT / g), recursive=True)})
    mine = cr.owner_paragraphs(owner, ROOT)
    icg = cr.loose((H / 'fix-20261025' / 'ic-align' / 'IC-GUIDE.txt').read_text(encoding='utf-8'))

    def whose(i, text):
        q = cr.loose(bl[i]['text'])
        if q and q in orig:
            return 'his, as published'
        if cr.is_his(q, mine):
            return 'his own words (a paragraph he wrote or rewrote)'
        ss = [cr.loose(x) for x in cr.sentences(text) if len(x.split()) >= 4]
        if ss and all(x in orig for x in ss):
            return 'his, as published (the sentence)'
        if ss and all(x in icg for x in ss):
            return 'his, from his inner child guide'
        if ss and any(x in orig or x in icg for x in ss):
            return 'partly his (published or inner child guide), partly ours'
        return 'ours'

    out, bad = [], []
    for f in sorted(glob.glob(str(HERE / 'reads' / 'READ-*.json'))):
        r = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
        for n, c in enumerate(r['candidates'], 1):
            i = c['block']
            ok = 0 <= i < len(bl) and c['cut'] in bl[i]['text']
            c = dict(c, part=r['part'], id='P%d-%02d' % (r['part'], n), exact=ok,
                     whole_block=ok and c['cut'].strip() == bl[i]['text'].strip(),
                     where=sr.where(bl, i) if 0 <= i < len(bl) else '?',
                     whose=whose(i, c['cut']) if ok else '?')
            if not ok:
                bad.append(c['id'])
            out.append(c)
    (HERE / 'CANDIDATES.json').write_text(json.dumps({'guide_sha256': SHA, 'candidates': out, 'not_exact': bad},
                                                     ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    lines = ['# Overcompletion candidates from the six readers (guide %s)' % SHA[:8], '',
             '%d candidates, %d clear; not found exactly in their block: %s' % (
                 len(out), sum(c['strength'] == 'clear' for c in out), ', '.join(bad) or 'none'), '']
    for c in out:
        lines += ['## %s [%d] %s (%s, %s; %s)' % (c['id'], c['block'], c['where'], c['kind'], c['strength'], c['whose']), '',
                  '- cut%s: %s' % (' (the whole paragraph)' if c['whole_block'] else '', c['cut']),
                  '- already said: %s' % c['already_said'], '- adds: %s' % c['adds'], '- loses: %s' % c['loses']]
        if c.get('join'):
            lines.append('- join: %s' % c['join'])
        lines.append('')
    (HERE / 'CANDIDATES.md').write_text('\n'.join(lines), encoding='utf-8')
    print(len(out), 'candidates;', sum(c['strength'] == 'clear' for c in out), 'clear; not exact:', bad)
    import collections
    print(collections.Counter(c['whose'] for c in out))


if __name__ == '__main__':
    main()
