"""Section 14, Emulate round a (2026-10-16): the published section whole, after batch 300g read it AI in every group and as a
whole (https://www.pangram.com/history/a2df8630-0e60-4f47-8487-b1f8c68ed1d7). One stretch (s01): the heading and the seven
paragraphs, plain text (links as their words, no emphasis, no image). Two calls, A and B, on the laptop
(emulate-runs/community-s14a). The heading stays Joel's whatever Emulate does with it; his meaning goes back in afterwards.
Run from this folder: python3 make_inputs.py"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import section  # noqa: E402
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
inputs = {'s01': section(art, '# Dissolution and Exit')}
units = {'s01': ['heading', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(units) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words')
