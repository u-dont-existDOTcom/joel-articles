"""Section 3 ("Why Communities Keep Dying in the Same Two Ways"), 2026-10-01: the published text split into paragraphs,
the baseline Pangram texts (each paragraph alone if it has 50 words or more, else with a neighbor, headings as published),
and the Emulate inputs (40 words at least, plain text, no headings)."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
IC = HERE.parent.parent
src = (IC / 'sections/004-original.md').read_text(encoding='utf-8').strip()
blocks = [b.strip() for b in src.split('\n\n') if b.strip()]
H1, P1, H2a, P2, P3, P4, H2b, P5, P6, P7, P8, P9 = blocks
O = dict(H1=H1, P1=P1, H2a=H2a, P2=P2, P3=P3, P4=P4, H2b=H2b, P5=P5, P6=P6, P7=P7, P8=P8, P9=P9)
json.dump(O, open(HERE / 'original-blocks.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
plain = lambda md: mdplain.plain(md).strip()
wc = {k: len(plain(v).split()) for k, v in O.items()}
print(wc)
BASE = {
 'b-H1P1H2P2': [H1, P1, H2a, P2],
 'b-P3': [P3],
 'b-P3P4': [P3, P4],
 'b-H2P5P6': [H2b, P5, P6],
 'b-P6': [P6],
 'b-P7P8': [P7, P8],
 'b-P8': [P8],
 'b-P8P9': [P8, P9],
}
for k, parts in BASE.items():
    t = plain('\n\n'.join(parts)); (HERE / 'base' / (k + '.txt')).write_text(t + '\n', encoding='utf-8'); print(k, len(t.split()))
EMU = {'e1': [P1, P2], 'e2': [P3, P4], 'e3': [P5, P6], 'e4': [P7, P8], 'e5': [P8, P9]}
(HERE / 'emu-in').mkdir(exist_ok=True)
for k, parts in EMU.items():
    t = plain('\n\n'.join(parts)); (HERE / 'emu-in' / (k + '.txt')).write_text(t + '\n', encoding='utf-8'); print(k, len(t.split()))
