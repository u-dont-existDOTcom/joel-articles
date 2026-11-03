#!/usr/bin/env python3
"""Turn 115, after the push: pull request #255 on the questions page, for him to merge.
  questions_t115c.py"""
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'OWNER-QUESTIONS.md'
PR = '[pull request #255](https://github.com/u-dont-existDOTcom/joel-articles/pull/255)'
s = P.read_text(encoding='utf-8')
a = 'For you to do: go through the docx of round 8\'s spots and send it back.'
assert s.count(a) == 1
s = s.replace(a, 'For you to do: go through the docx of round 8\'s spots and send it back, and merge pull request #255.')
a2 = '### 🔵 The two temporary Substack drafts: keep them for round 9 (turn 115)'
assert s.count(a2) == 1
s = s.replace(a2, '### 🟠 Merge pull request #255 (turn 115)\n\n'
              'The lane\'s %s holds this turn: round 8 read, lesson E276 (Inner Child), the pass and its checks, and the docx. Open it, '
              'then click "Merge pull request" and "Confirm merge". That takes about a minute, and the page then says "Merged". '
              '(You merged #252, turns 113 and 114.)\n\n' % PR + a2)
P.write_text(s, encoding='utf-8')
print('ok')
