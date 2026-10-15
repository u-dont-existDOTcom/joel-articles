"""Section 13, Emulate round d (2026-10-15): the three units whose round b versions both lost the published meaning
(H4-P4 the long visit: both dropped the five states; H4-P9 non-members' rights: one invented "the commons proposal",
the other turned every claim into a question; H5-P3 "Outside": both changed who reviews whom). Each unit goes twice:
as published (g01, g03, g05; g01 carries the short visit too, since the long visit alone is 39 words and Emulate needs 40) and as draft v6 (g02, g04, g06), two calls each. Plain text, links as their words.
Run from this folder: python3 make_inputs.py"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parents[1]

def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]

def plain(t):
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t).replace('*', '')
    return re.sub(r'\s+', ' ', t).strip()

def by_heading(bs):
    out = []
    for x in bs:
        if x.startswith('#'):
            out.append([])
        elif not x.startswith('<!--'):
            out[-1].append(x)
    return out

s = (CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = s.index('# Your Little Forming Group Already Is the Community'); b = s.index('\n# ', a + 5)
pub = by_heading(blocks(s[a:b]))
v6 = by_heading(blocks((HERE.parent / 'v6.md').read_text(encoding='utf-8')))
inputs = {
    'g01': plain(pub[3][3]) + ' ' + plain(pub[3][4]), 'g02': plain(v6[3][3]),
    'g03': plain(pub[3][9]), 'g04': plain(v6[3][8]),
    'g05': plain(pub[4][2]), 'g06': plain(v6[4][2]),
}
assert inputs['g01'].startswith('Short visit.') and 'Long visit.' in inputs['g01'] and inputs['g02'].startswith('Long visit:')
assert inputs['g03'].startswith('Visitors') and inputs['g04'].startswith('Visitors')
assert inputs['g05'].startswith('“Outside”') and inputs['g06'].startswith('“Outside”')
units = {'g01': [[3, 3], [3, 4], 'published P4 and P5 (P5 alone is 39 words; Emulate needs 40)'], 'g02': [[3, 4], 'v6'], 'g03': [[3, 9], 'published P10'], 'g04': [[3, 9], 'v6'],
         'g05': [[4, 3], 'published P3'], 'g06': [[4, 3], 'v6']}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'units.json').write_text(json.dumps(units, indent=1) + '\n', encoding='utf-8')
for k, v in inputs.items():
    print(k, len(v.split()), 'words:', v[:90])
