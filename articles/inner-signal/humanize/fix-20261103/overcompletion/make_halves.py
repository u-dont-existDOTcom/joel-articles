"""Parts 2, 3 and 5 of the overcompletion read in halves (PART-2a.md and so on). Their first readers ran out of room in one
reply (the API's 64,000-token cap on a response), so each half goes to a fresh reader. Each half starts at the heading
nearest its part's middle, with two blocks of context on either side, the same format as make_chunks.py.

  python3 articles/inner-signal/humanize/fix-20261103/overcompletion/make_halves.py
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from make_chunks import GUIDE, SHA, line, sr  # noqa: E402

HALVES = {'2a': (112, 169), '2b': (169, 229), '3a': (229, 306), '3b': (306, 358), '5a': (479, 569), '5b': (569, 638)}


def main():
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == SHA, 'the guide changed'
    bl = sr.blocks(md)
    out = []
    for k, (s, e) in HALVES.items():
        assert bl[s]['level'] in (1, 2), s
        body = ['# Part %s of the guide: blocks %d to %d' % (k, s, e - 1), '',
                '## Context before this part (read it, don\'t report on it)', ''] + [line(b) for b in bl[s - 2:s]] + ['']
        body += ['## The part to read', ''] + [line(b) for b in bl[s:e]] + ['']
        body += ['## Context after this part (read it, don\'t report on it)', ''] + [line(b) for b in bl[e:e + 2]] + ['']
        (HERE / 'chunks' / ('PART-%s.md' % k)).write_text('\n\n'.join(x for x in body if x) + '\n', encoding='utf-8')
        out.append({'part': k, 'blocks': [s, e - 1], 'words': sum(len(b['text'].split()) for b in bl[s:e])})
    print(json.dumps(out))


if __name__ == '__main__':
    main()
