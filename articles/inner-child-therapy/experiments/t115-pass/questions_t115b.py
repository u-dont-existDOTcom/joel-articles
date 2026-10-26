#!/usr/bin/env python3
"""Turn 115, after the API checks of the pass came in: the questions page's Decided item says how they read.
  questions_t115b.py"""
import pathlib

P = pathlib.Path(__file__).resolve().parents[2] / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/'
s = P.read_text(encoding='utf-8')
a = ('each reviewed by three fresh readers and the five rewordings by the owner-delivery gate ([PASS.md](%st115-pass/PASS.md)). '
     'They\'re in the docx as tracked changes for you to decide; the rest is shaded there.' % B)
b = ('each reviewed by three fresh readers and the five rewordings by the owner-delivery gate, then checked with its block: no '
     'checked paragraph reads Low or AI now, four read Human, high throughout, and one check, F09\'s, timed out ([PASS.md](%st115-pass/PASS.md), '
     '[API-CHECKS.md](%st115-api/API-CHECKS.md)). They\'re in the docx as tracked changes for you to decide; the rest is shaded there.' % (B, B))
assert s.count(a) == 1
s = s.replace(a, b)
P.write_text(s, encoding='utf-8')
print('ok')
