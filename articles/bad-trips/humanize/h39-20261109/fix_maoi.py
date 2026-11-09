#!/usr/bin/env python3
"""fix_maoi.py - "MAOI" and "serotonergic substance" explained where the guide first uses them (the call-medics list).

SKILL.md, Writing for Pangram, fix 2: a term a high-school graduate wouldn't know is explained once, where it is first
used, without asking him. The guide first says "MAOI" in "Call medics for:" and uses it again in the serotonin
syndrome section and in his new Syrian rue oil entry (round 30), and never says what one is. The examples are the
guide's own: ayahuasca and harmalas (Recognizing serotonin toxicity, the serotonin stop list), MDMA and antidepressants
(the same lists). Words are only added, so the warning and its keys stay as they were.

  python3 fix_maoi.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
OLD = '- Concerning symptoms after an MAOI plus a serotonergic substance'
NEW = ('- Concerning symptoms after an MAOI, which slows the breakdown of serotonin (some older antidepressants, and the '
       'harmalas in ayahuasca and Syrian rue seeds), plus a serotonergic substance, one that raises serotonin, like MDMA '
       'or most antidepressants')
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
hits = [b for b in blocks if OLD in (b['md'] or '')]
assert len(hits) == 1 and hits[0]['id'] == 'B94', [b['id'] for b in hits]
assert hits[0]['md'].count(OLD) == 1 and hits[0]['md'].endswith(OLD)
hits[0]['md'] = hits[0]['md'].replace(OLD, NEW)
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(NEW)
