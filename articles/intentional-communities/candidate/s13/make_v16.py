"""Section 13 draft v16 (2026-10-15): v15 with H1-P2, the conflict paragraph, rebuilt from Emulate round g (emu-g/out/
j02-emuA.txt, from v14, after it read AI alone in 292g), the published meaning put back word by word. Writes v16.md and
v16-fixes.json. Run from this folder: python3 make_v16.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v15 = blocks((HERE / 'v15.md').read_text(encoding='utf-8'))
assert v15[2].startswith("Don't even think about combining")
emu = (HERE / 'emu-g' / 'out' / 'j02-emuA.txt').read_text(encoding='utf-8').split('\n\n')[1]
FIXES = [
 ("at least one conflict together", "at least one real conflict together",
  'the published "one real conflict"'),
 ("Not dealt with it by writing out a vision statement and shaking hands or agreeing to leave each other alone or any other BS "
  "way of \"resolving\" things.",
  "Not dealt with it by writing out a vision statement and shaking hands, or any other fake way of \"resolving\" things, like "
  "a truce nobody believes (\"let's just leave each other alone\").",
  'the published "a truce nobody believes" (traces of r5 and r7), as the example of a fake way, so the sentence keeps two '
  'items (the linter fails two lists of three in one paragraph); Emulate\'s example as its words; "fake" for "BS", a word that '
  'isn\'t his'),
 ("giving each of you the time you need,", "giving each of you time,",
  'stance check against the article so far, r8: section 4\'s relational pl/ork gives everyone equal time; the published "Give '
  'each person time"'),
 ("(jealousy, humiliation, fear, whatever)", "(jealousy, humiliation, fear, old material, whatever)",
  'the published "old material" (key U5)'),
 ("what ever agreement", "whatever agreement", 'a typo of Emulate\'s'),
]
t, log = emu, [{'id': 'H1-P2', 'source': 'emu-g/out/j02-emuA.txt, its second paragraph (from v14)'}]
for old, new, why in FIXES:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
    log.append({'id': 'H1-P2', 'old': old, 'new': new, 'why': why})
out = list(v15)
out[2] = t
(HERE / 'v16.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v16-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(t)
