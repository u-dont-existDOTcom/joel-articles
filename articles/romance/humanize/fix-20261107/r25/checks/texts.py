"""r25's check text in the romance article (2026-11-07), linted before its check (gate bad-trips-2026-11-07h).

r24's Jealousy stretch (366 to 370) read 94.8% AI (#131) although each new paragraph read Human by itself (#124, #127,
#128): S2's pattern. The stretch alone is all argument, with none of the section's story before it. This is the whole
section (357 to 370, the live post's words from its heading on) with r22's 367 and r23's 368 and 369 in it: one check
after the fix (its two tries spent, #83 and #94). If it still reads AI, the paragraphs go to Joel on the marking page
with these tries (gate bad-trips-2026-11-07c)."""
import importlib.util
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
spec = importlib.util.spec_from_file_location('r24_texts', HERE.parent.parent / 'r24' / 'checks' / 'texts.py')
R24 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R24)
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
PRED = {d['id']: d for d in map(json.loads, LEDGER.read_text(encoding='utf-8').splitlines()) if d.get('type') == 'prediction'}
R83 = [p for p in re.split(r'\n\s*\n', PRED['romance-low-jeal#83']['text']) if p.strip()]
assert R83[9] == R24.LIVE[366] and R83[13] == R24.LIVE[370]
TEXTS = {'r25-jeal': '\n\n'.join(R83[:10] + [R24.NEW[367], R24.NEW[368], R24.NEW[369], R24.LIVE[370]])}
