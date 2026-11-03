"""The nonsense read's second pass, with planted errors to measure it (the first pass's nine readers took about half a
minute each and found one to three things apiece, so how much they miss isn't known).

Three parts, each with three planted real-word errors of the "oily" kind (a real word, the sentence still grammatical,
the meaning wrong). The readers don't know about them (CANARIES.json is outside pass2/parts/ and isn't named in the
brief). A reader's recall on its three tells how far its other findings and its silence can be trusted. Each reader
also lists every block it read, so none can be skipped.

  python3 articles/inner-signal/humanize/fix-20261103/nonsense/make_pass2.py
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import suggestion_review as sr  # noqa: E402
from make_parts import GUIDE, SHA, line  # noqa: E402

PARTS = {'A': (0, 247), 'B': (247, 485), 'C': (485, 762)}
# (part, a phrase that finds the block, the words as they are, the planted words)
CANARIES = [
    ('A', 'Inductions serve to gather your awareness', 'more receptive form', 'more deceptive form'),
    ('A', 'If you can\'t find any warmth today', 'find any warmth today', 'find any wealth today'),
    ('A', 'Taking a break. Sometimes it may be wise to remove yourself', 'wise to remove yourself', 'wise to remodel yourself'),
    ('B', 'The induction and the inner meeting get you to where you can listen.', 'where you can listen.', 'where you can glisten.'),
    ('B', 'Fifteen minutes is just a handy appointment with yourself', 'a handy appointment with yourself', 'a handy ointment with yourself'),
    ('B', 'Go for more sleep, more eating, more grounding', 'more eating, more grounding', 'more eating, more grinding'),
    ('C', 'you tap gently on your body while you say something like', 'and you stay with what you feel', 'and you stray with what you feel'),
    ('C', 'while you have compassion for it, the door is closed', 'the door is closed', 'the door is cloaked'),
    ('C', 'fill in something very specific for them', 'something very specific for them', 'something very pacific for them'),
]


def main():
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == SHA, 'the guide changed'
    bl = sr.blocks(md)
    texts = {b['i']: b['text'] for b in bl}
    planted = []
    for part, find, old, new in CANARIES:
        hits = [b['i'] for b in bl if find in b['text']]
        assert len(hits) == 1, (find, hits)
        i = hits[0]
        s, e = PARTS[part]
        assert s <= i < e, (find, i, part)
        assert texts[i].count(old) == 1, old
        texts[i] = texts[i].replace(old, new)
        planted.append({'part': part, 'block': i, 'was': old, 'planted': new})
    for part, (s, e) in PARTS.items():
        body = ['# Part %s of the guide: blocks %d to %d' % (part, s, e - 1), '']
        if s:
            body += ['## Context before this part (read it, don\'t report on it)', ''] + [line(dict(b, text=texts[b['i']])) for b in bl[s - 2:s]] + ['']
        body += ['## The part to read', ''] + [line(dict(b, text=texts[b['i']])) for b in bl[s:e]] + ['']
        if e < len(bl):
            body += ['## Context after this part (read it, don\'t report on it)', ''] + [line(dict(b, text=texts[b['i']])) for b in bl[e:e + 2]] + ['']
        (HERE / 'pass2' / 'parts' / ('PART-%s.md' % part)).write_text('\n\n'.join(x for x in body if x) + '\n', encoding='utf-8')
    (HERE / 'CANARIES.json').write_text(json.dumps({'guide_sha256': SHA, 'canaries': planted}, indent=1) + '\n', encoding='utf-8')
    print(len(planted), 'planted;', {p: sum(len(b['text'].split()) for b in bl[s:e]) for p, (s, e) in PARTS.items()})


if __name__ == '__main__':
    main()
