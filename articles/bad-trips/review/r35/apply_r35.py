#!/usr/bin/env python3
"""apply_r35.py - round 35's answers (Joel, exported 2026-11-12 13:37:05 UTC; ANSWERS-R35-20261112-1337.json) put into the
guide.

- BODY-ONCE, his comment: "my paragraph should not say anything that should be going in that above list. so cut this
  section or move it up/merge it". His Risk of Harm paragraph's body signs move up into the Call medics list (merged):
  his "(not just regular sweating)" goes on the list's overheating line, "severe insomnia" becomes its own line, and
  "trouble breathing" is the list's first line already. What stays in his paragraph is his own catch-all, his words as he
  wrote them: "If for whatever reason you feel like this is more than you can handle, reach out."
- TEACH-ORAL, revised: his version, the text of his last check (7e898f05, Human, High; his five tries in
  ../../experiments/t35-answers/JOEL-TRIES-TEACH-ORAL.md), with one typo fixed ("from from").

  python3 apply_r35.py
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
A = json.loads((HERE / 'ANSWERS-R35-20261112-1337.json').read_text(encoding='utf-8'))
R = json.loads((HERE / 'REVIEW-R35.json').read_text(encoding='utf-8'))
assert A['review_id'] == R['review_id'] == 'bad-trips-r35'
assert hashlib.sha256((HERE / 'PAGE-R35.md').read_bytes()).hexdigest() == A['article']['sha256']
I = {x['id']: x for x in A['items']}
assert I['BODY-ONCE']['comment'].startswith('my paragraph should not say anything that should be going in that')
assert I['TEACH-ORAL']['status'] == 'revise' and '7e898f05-9c97-4f23-9513-cfca78be8905' in I['TEACH-ORAL']['comment']
HIS_ORAL = I['TEACH-ORAL']['your_version']
assert HIS_ORAL.startswith('"Overdose" is too vague to choose a remedy. Figure out how much of what was swallowed')
HIS_ORAL = HIS_ORAL.replace('(respiratory depression, from from opioids', '(respiratory depression, from opioids').strip()


def unit(bid):
    return [b for b in BLOCKS if b['id'] == bid][0]


def swap(bid, old, new):
    b = unit(bid)
    assert b['md'].count(old) == 1, (bid, old)
    b['md'] = b['md'].replace(old, new)


# BODY-ONCE: his body signs merged up into the Call medics list; his catch-all stays in his paragraph
swap('R34-HARM-2', 'If their body is flashing warning signs like severe overheating (not just regular sweating), severe '
                   'insomnia, or trouble breathing, or if for whatever reason you feel',
     'If for whatever reason you feel')
swap('B94', '- Dangerous overheating, severe rigidity, or clonus with fever',
     '- Dangerous overheating (not just regular sweating), severe rigidity, or clonus with fever\n- Severe insomnia')
# TEACH-ORAL: his version
b = unit('B126')
assert b['md'].startswith('"Overdose" is too vague to choose a remedy. Ask what was swallowed')
b['md'] = HIS_ORAL

MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('words: %d -> %d' % (len(before_md.split()), len(MD.read_text(encoding='utf-8').split())))
print(unit('R34-HARM-2')['md'])
print(unit('B126')['md'])
