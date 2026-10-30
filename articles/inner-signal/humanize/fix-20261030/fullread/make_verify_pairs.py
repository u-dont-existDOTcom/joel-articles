"""VERIFY-PAIRS.md: every paragraph apply_fullread.py changed, before, after, and his published version beside it (the
finding's published paragraph, or the published paragraph with the most words in common), for my read (read/VERIFY.md).

  python3 articles/inner-signal/humanize/fix-20261030/fullread/make_verify_pairs.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402


def main():
    ap = json.loads((HERE / 'APPLIED-FULLREAD.json').read_text(encoding='utf-8'))
    F = {f['id']: f for f in json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']}
    ptexts = [b['text'] for b in sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))]
    words = [set(re.findall(r'\w+', p.lower())) for p in ptexts]

    def best(t):
        w = set(re.findall(r'\w+', t.lower()))
        return ptexts[max(range(len(ptexts)), key=lambda i: len(w & words[i]) / (len(w) + 1))] if t else ''
    out = ['# The fixed paragraphs, before and after, beside his published version (fix-20261030/fullread)', '']
    for c in sorted(ap['changed'], key=lambda c: c['block']):
        pubs = []
        for fid in c['findings']:
            for pb in (F[fid].get('pub_blocks') or []) if fid in F else []:
                if ptexts[pb] not in pubs:
                    pubs.append(ptexts[pb])
        pubs = pubs or [best(c['before'] or c['after'])]
        tag = ' [taken out]' if c.get('deleted') else (' [new paragraph]' if not c['before'] else '')
        out += ['## Block %d, %s (%s)%s' % (c['block'], c['where'], ', '.join(c['findings']), tag),
                'BEFORE: ' + c['before'], 'AFTER: ' + c['after']] + ['PUBLISHED: ' + p for p in pubs] + ['']
    (HERE / 'VERIFY-PAIRS.md').write_text('\n'.join(out), encoding='utf-8')
    print(len(ap['changed']), 'paragraphs')


if __name__ == '__main__':
    main()
