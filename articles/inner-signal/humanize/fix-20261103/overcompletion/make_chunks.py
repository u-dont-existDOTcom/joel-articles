"""Split the hypnosis guide into six parts for the overcompletion read (Joel, 2026-11-03 00:39 UTC, on card E-61: "cut all
this. you didn't notice the massive overcompletion here? prob this whole guide is full of it then.").

Each part starts at a top-level heading, and every paragraph carries its block number in the guide (sr.blocks), so the
readers' candidates point at the guide exactly. The two blocks on either side of a part come with it as context. The
outline (every heading with its block number) is OUTLINE.md.

  python3 articles/inner-signal/humanize/fix-20261103/overcompletion/make_chunks.py
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
SHA = '090588f72475fbddf5528b9db50193bf50572fc5f99542a52fab02e36db15de0'
STARTS = [0, 112, 229, 358, 479, 638]   # top-level headings: the start, Working with your inner child, Induction,
                                        # The 15-minute daily practice, Appendix B, Appendix F


def line(b):
    if b['level']:
        return '[%d] %s %s' % (b['i'], '#' * b['level'], b['text'])
    return '[%d] %s' % (b['i'], b['text'])


def main():
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == SHA, 'the guide changed'
    bl = sr.blocks(md)
    outline = ['# The guide\'s headings, with block numbers', '']
    outline += ['%s- [%d] %s' % ('  ' * (b['level'] - 1), b['i'], b['text']) for b in bl if b['level']]
    (HERE / 'OUTLINE.md').write_text('\n'.join(outline) + '\n', encoding='utf-8')
    ends = STARTS[1:] + [len(bl)]
    parts = []
    for k, (s, e) in enumerate(zip(STARTS, ends), 1):
        assert s == 0 or bl[s]['level'] == 1, s
        body = ['# Part %d of the guide: blocks %d to %d' % (k, s, e - 1), '']
        if s:
            body += ['## Context before this part (read it, don\'t report on it)', ''] + [line(b) for b in bl[max(0, s - 2):s]] + ['']
        body += ['## The part to read', ''] + [line(b) for b in bl[s:e]] + ['']
        if e < len(bl):
            body += ['## Context after this part (read it, don\'t report on it)', ''] + [line(b) for b in bl[e:e + 2]] + ['']
        p = HERE / 'chunks' / ('PART-%d.md' % k)
        p.write_text('\n\n'.join(x for x in body if x) + '\n', encoding='utf-8')
        words = sum(len(b['text'].split()) for b in bl[s:e])
        parts.append({'part': k, 'blocks': [s, e - 1], 'words': words, 'file': str(p.relative_to(ROOT))})
    (HERE / 'chunks' / 'PARTS.json').write_text(json.dumps({'guide_sha256': SHA, 'parts': parts}, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(parts, indent=1))


if __name__ == '__main__':
    main()
