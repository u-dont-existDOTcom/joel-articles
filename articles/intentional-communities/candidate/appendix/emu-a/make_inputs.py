"""The appendix, Emulate round a (2026-10-17): draft v1 of "Appendix: Watch These, Then Read These" whole (the published
appendix with Joel's fix of 2026-10-16 23:38 UTC and the two dedup cuts, ../make_v1.py), its headings and entries as plain text
(links as their words, no emphasis). Batch 329g read the published films entries Human in groups (A to C) and every group
from Doucleff's entry on AI (D to G); the whole appendix read Human for its first 111 words and AI for the rest. Two calls, A
and B, on the laptop (emulate-runs/community-apxa). The headings, titles, authors and years stay Joel's whatever Emulate does
with them; his meaning goes back in afterwards, inside Emulate's sentences. Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v1.md').read_text(encoding='utf-8')) if b.strip()]
inputs = {'s01': '\n\n'.join(plain(b.lstrip('#').strip()) for b in bl)}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words')
