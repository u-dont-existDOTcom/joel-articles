#!/usr/bin/env python3
"""apply_r34.py - round 34's answers (Joel, exported 2026-11-11 23:57:59 UTC; ANSWERS-R34-20261111-2357.json) put into the
guide.

- TEACH-HARM, revised: his version is in his Pangram check, linked in the comment ("human high
  https://www.pangram.com/history/aa15e193-..."; the page's "Your version" box came back unchanged), read from his history
  and saved as ../../experiments/t34-answers/JOEL-VERSION-TEACH-HARM-aa15e193.md. It goes where he wrote it, whole: Risk of
  Harm's first paragraph, his line break kept as a paragraph break. With it, "make sure this is only said once": the
  reasons to get urgent help are now said in his paragraph, so the places that said them again go: the Call medics list's
  "Violence, self-harm, or a situation the sitter cannot physically contain", the helper's Do list's "Call for help early
  when safety is slipping.", and the harm part's list of when to call (a specific target, means, ...), whose bar is higher
  than his ("the moment you think they might hurt themselves or anybody else"). The 911 line's repeat of the same reasons
  is a fix of mine with its own check (../../humanize/h44-20261112/); the body signs his paragraph shares with the Call
  medics list are round 35's question (both stay until he answers).
- ADJUNCT, "b": the DMSO sentence becomes fix2 (Human, Medium, 83f4caef); "adjunct remedy" leaves his keep list (K12).

  python3 apply_r34.py      write the guide after round 34 and print what changed
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
A = json.loads((HERE / 'ANSWERS-R34-20261111-2357.json').read_text(encoding='utf-8'))
R = json.loads((HERE / 'REVIEW-R34.json').read_text(encoding='utf-8'))
assert A['review_id'] == R['review_id'] == 'bad-trips-r34'
assert hashlib.sha256((HERE / 'PAGE-R34.md').read_bytes()).hexdigest() == A['article']['sha256']
I = {x['id']: x for x in A['items']}
assert I['TEACH-HARM']['status'] == 'revise' and 'aa15e193-4ea0-43f9-b851-a8aee94d62cc' in I['TEACH-HARM']['comment']
assert 'make sure this is only said once' in I['TEACH-HARM']['comment']
assert I['ADJUNCT']['comment'].strip().lower() == 'b'

HIS = (ART / 'experiments/t34-answers/JOEL-VERSION-TEACH-HARM-aa15e193.md').read_text(encoding='utf-8')
HIS_P1 = ("You can sit through a lot with someone, but the moment you think they might hurt themselves or anybody else, get "
          "urgent help. It doesn't have to be a proven death wish. They might just start heading out the door and get lost, "
          "hit by a car, drown, fall off a cliff, etc. Another cue to get help is if they start acting delusional.")
HIS_P2 = ("If their body is flashing warning signs like severe overheating (not just regular sweating), severe insomnia, or "
          "trouble breathing, or if for whatever reason you feel like this is more than you can handle, reach out.")
assert HIS_P1 in HIS and HIS_P2 in HIS, 'his version as read from his check'


def ids():
    return [b['id'] for b in BLOCKS]


def unit(bid):
    return BLOCKS[ids().index(bid)]


def cut(bid, expect_start):
    b = unit(bid)
    assert b['md'].startswith(expect_start), (bid, b['md'][:80])
    BLOCKS.remove(b)


def cut_items(bid, starts):
    b = unit(bid)
    lines = b['md'].split('\n')
    keep = [l for l in lines if not any(l.startswith('- ' + s) for s in starts)]
    assert len(lines) - len(keep) == len(starts), (bid, starts)
    b['md'] = '\n'.join(keep)


def swap(bid, old, new):
    b = unit(bid)
    assert b['md'].count(old) == 1, (bid, old)
    b['md'] = b['md'].replace(old, new)


# TEACH-HARM: his version, whole, where he wrote it
b = unit('B276')
assert b['md'].startswith('Get urgent help when somebody may harm themselves')
b['md'] = HIS_P1
k = ids().index('B276') + 1
BLOCKS[k:k] = [{'id': 'R34-HARM-2', 'kind': 'p', 'md': HIS_P2, 'text': None}]
# ... and said once
cut_items('B94', ['Violence, self-harm, or a situation the sitter cannot physically contain'])
cut_items('B282', ['Call for help early when safety is slipping.'])
cut('B292', 'Call crisis or emergency services for a specific target')
# ADJUNCT b
swap('N-CBD-3', "I'd treat it as a plausible experimental adjunct remedy rather than something to wait on while a seizure "
                "continues.",
     "While a seizure continues, the rescue medicine comes first, and I'd still consider DMSO alongside it, although "
     "that's experimental.")

MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('words: %d -> %d' % (len(before_md.split()), len(MD.read_text(encoding='utf-8').split())))
