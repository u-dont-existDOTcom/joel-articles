#!/usr/bin/env python3
"""r16 = r15 with his batch-10 answers (Joel, 2026-11-05 23:00 UTC, ../../../experiments/t15-answers/).

F10-1 to F10-3 approved: kept as r15 has them. F10-4 and F10-5 answered, worded here for the batch-11 page:
- F10-4, "HRP": "yes it was an old version of askrigor basically, we can tell them to re-check it with askrigor.com for an
  up-to-date verification (yes it will be public soon, don't need to mention it's not yet)".
- F10-5, the Gemini mode: "i just tested it with free gemini and it worked so i think gemini is able to use it on free
  mode now but i'd just tell people to use the highest thinking level they can for best answers as usual."

Writes r16.md and CHANGES.json (each change: block start, old, new, kind, why)."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r15' / 'r15.md').read_text(encoding='utf-8')
CHANGES = []


def ch(old, new, kind, why):
    global md
    assert md.count(old) == 1, (old[:60], md.count(old))
    md = md.replace(old, new)
    CHANGES.append({'old': old, 'new': new, 'kind': kind, 'why': why})


ch('so that you can directly consult with Gemini (on Flash Extended mode) to extract',
   'so that you can directly consult with Gemini to extract', 'answer',
   'F10-5: the mode is named once, in the Gem section, as his answer gives it')
ch('you can check this [HRP deep research report](',
   'you can check this [deep research report](', 'answer', 'F10-4: "HRP" out')
ch('owner_user_id=user-g2rbxGmNt0TNQzl5Kw5jDvko). Glutamine',
   'owner_user_id=user-g2rbxGmNt0TNQzl5Kw5jDvko) from an older version of AskRigor, my research tool, and re-check it with '
   'askrigor.com for an up-to-date verification. Glutamine', 'answer',
   'F10-4: where the report came from, AskRigor explained where it is first named (E369), and his "re-check it with '
   'askrigor.com for an up-to-date verification", joined to the sentence it follows (E368)')
ch('into a customized smart Gemini Pro [Gut Health Gem]', 'into a customized smart Gemini [Gut Health Gem]', 'answer',
   'F10-5: it works on free Gemini, so not "Pro"')
ch('get far better advice than you\'d get from any one of them! If you have',
   'get far better advice than you\'d get from any one of them! I tested it on free Gemini and it works, but use the '
   'highest thinking level you can for the best answers. If you have', 'answer',
   'F10-5: his test and his advice, after what the Gem is for and before the ask for books')
(HERE / 'r16.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'changes;', len(md.split()), 'words')
