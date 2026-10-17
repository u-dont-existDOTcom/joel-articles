"""Section 15 draft v4 (2026-10-17, after batch 323g): v3 with
- H1-P4 as variant x (../v3-variants.json): the workshop and the aunt as a question at the end. Both versions read Human alone
  and inside the subsection (323g: v3 0.25 and 0.25; x 0.08 and 0.19); x puts the joke where a joke goes, last, and reads
  lower.
- H2-P1 as CHOICE below picks (batch 325g): the paradise subsection read "Mostly Human" in 323g, a 40-word AI window, low,
  over its heading and P1. Variants: a and b by hand (the published meaning in a looser shape), c from Emulate round c
  (../emu-c/, the heading with P1 and P2 sent whole).
Writes v4.md (with CHOICE) and v4-variants.json (every H2-P1 variant). Run from this folder: python3 make_v4.py [CHOICE]"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v3.md').read_text(encoding='utf-8')
X = json.loads((HERE / 'v3-variants.json').read_text(encoding='utf-8'))['H1-P4x']
P4 = [b for b in t.split('\n\n') if b.startswith('In the villages and families')]
assert len(P4) == 1
t = t.replace(P4[0], X)
P1 = ("But does this mean I think Sénégal is some magical place that's kept its communal paradise? No! The warmth has hard "
      "limits, and for LGBTQ+ people who cross them, it can be brutal.")
assert t.count(P1) == 1
VAR = {
 'v3': P1,
 'a': ("But does this mean I think Sénégal is some magical place that's kept its communal paradise? No! For LGBTQ+ people it "
       "can be a brutal place, because the warmth has hard limits and they pay for crossing them."),
 'b': ("But does this mean I think Sénégal is some magical place that's kept its communal paradise? No! The warmth has hard "
       "limits here, and LGBTQ+ people can pay a brutal price for crossing them."),
}
c = HERE / 'emu-c' / 'H2-P1-c.txt'
if c.exists():
    VAR['c'] = c.read_text(encoding='utf-8').strip()
choice = sys.argv[1] if len(sys.argv) > 1 else 'v3'
t = t.replace(P1, VAR[choice])
(HERE / 'v4.md').write_text(t, encoding='utf-8')
(HERE / 'v4-variants.json').write_text(json.dumps(VAR, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v4.md with H2-P1', choice, '; variants', list(VAR))
