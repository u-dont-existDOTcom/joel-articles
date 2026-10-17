"""Section 16, Emulate round h (2026-10-17, after batches 351g and 353g): every Emulate round on H3 so far (e, f, g) was sent a
draft that opens its paragraphs on questions ("Where do you find them?", "Have you ever visited an actual community?", "What do
you get out of a visit?"), and every call kept them (emu-e/out, emu-f/out, emu-g/out). With those openers, the run H3-P4 to
H3-P6 reads AI in every draft (348g 0.69, 349g 0.73, 350g 0.98) and the whole section reads AI from H3-P4's end to the section's
end (351g, 250 words, https://www.pangram.com/history/53673eef-b6e6-4e3c-879e-da1505286134). In the march, those questions were
the paragraphs' breaks (review-r20), so the drafts kept them. This round sends the published text, which has no questions:
- h01: the published H3-P4 to H3-P8 (where to meet people, the visit, what it teaches, land after the three things, nothing to
  sell; the Senegal sentence is carried by section 2, preservation-keys.json U41);
- h02: the same with the published H3-P3 (the practice group) before it, whose colon sentence reads AI in v15 q (351g, 35 words,
  https://www.pangram.com/history/c0bc5526-2a20-48b4-8b2a-1eb8da148509).
Three calls on h01 and two on h02, plain text, on the laptop (emulate-runs/community-s16h). Run from this folder:
python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v0.md').read_text(encoding='utf-8')) if b.strip()]
i = bl.index('## What to Do This Month')
h3 = [b for b in bl[i + 1:] if not SKIP.match(b)]
# h3[0] is the published lead-in line ("Here is the first month without the heroic land purchase:"); H3-P2 is h3[1]
assert h3[0].startswith('Here is the first month'), h3[0]
P = {'H3-P%d' % n: h3[n - 1] for n in range(2, 9)}
assert P['H3-P3'].startswith('Find two or three people'), P['H3-P3']
assert P['H3-P8'].startswith('I have no application form'), P['H3-P8']
SEN = 'I’m in Sénégal and expect to buy land, but I’m not announcing a commune. '
assert P['H3-P8'].count(SEN) == 1
P['H3-P8'] = P['H3-P8'].replace(SEN, '')
G = {'h01': ['H3-P%d' % n for n in range(4, 9)], 'h02': ['H3-P%d' % n for n in range(3, 9)]}
CALLS = {'h01': 'ABC', 'h02': 'AB'}
asc = {'’': "'", '‘': "'", '“': '"', '”': '"', '—': ' - ', '–': '-', '…': '...', 'é': 'e'}


def ascii_(t):
    for a, b in asc.items():
        t = t.replace(a, b)
    t.encode('ascii')
    return t


inputs = {k: ascii_('\n\n'.join(plain(P[p]) for p in v)) for k, v in G.items()}
(HERE / 'inputs.json').write_text(json.dumps(inputs, ensure_ascii=True, indent=1) + '\n', encoding='ascii')
(HERE / 'units.json').write_text(json.dumps(dict(G, calls=CALLS, source='v0 (published)')) + '\n', encoding='utf-8')
print({k: len(v.split()) for k, v in inputs.items()})
