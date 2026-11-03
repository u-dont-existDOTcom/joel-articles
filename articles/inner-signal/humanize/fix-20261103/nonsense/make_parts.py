"""Split the hypnosis guide into nine parts for the nonsense read (Joel, 2026-11-03 13:46 UTC: "i also noticed the tag
questions part above says "oily" instead of old. do we have more nonsense in here (from emulate i guess)? how are you not
catching this?"). Same format as ../overcompletion/make_chunks.py: every paragraph with its block number, two blocks of
context on either side, each part starting at a heading.

  python3 articles/inner-signal/humanize/fix-20261103/nonsense/make_parts.py
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
SHA = 'bb5fc57de174b36c9e1bed333354a0f79e2c74811564f505a505950c5b5e7300'
STARTS = [0, 88, 168, 247, 329, 386, 485, 594, 686]


def line(b):
    return '[%d] %s%s' % (b['i'], ('#' * b['level'] + ' ') if b['level'] else '', b['text'])


def main():
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == SHA, 'the guide changed'
    bl = sr.blocks(md)
    ends = STARTS[1:] + [len(bl)]
    out = []
    for k, (s, e) in enumerate(zip(STARTS, ends), 1):
        assert s == 0 or bl[s]['level'] in (1, 2), s
        body = ['# Part %d of the guide: blocks %d to %d' % (k, s, e - 1), '']
        if s:
            body += ['## Context before this part (read it, don\'t report on it)', ''] + [line(b) for b in bl[s - 2:s]] + ['']
        body += ['## The part to read', ''] + [line(b) for b in bl[s:e]] + ['']
        if e < len(bl):
            body += ['## Context after this part (read it, don\'t report on it)', ''] + [line(b) for b in bl[e:e + 2]] + ['']
        (HERE / 'parts' / ('PART-%d.md' % k)).write_text('\n\n'.join(x for x in body if x) + '\n', encoding='utf-8')
        out.append({'part': k, 'blocks': [s, e - 1], 'words': sum(len(b['text'].split()) for b in bl[s:e])})
    (HERE / 'parts' / 'PARTS.json').write_text(json.dumps({'guide_sha256': SHA, 'parts': out}, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
