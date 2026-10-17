"""Section 16, Emulate round i (2026-10-17, after batches 354g to 358g): round h's sentences (sent the published text, meaning
put back) read Human in every run of three over H3-P3 to H3-P7 (356g, 0.00 to 0.09), where every hand-written shape read AI
(354g, 0.80 to 1.00). Inside the whole section, every v16 shape read AI from H3-P3's second sentence to the section's end (332 to
343 words) and over H2-P6's last sentence, the heading and H3-P2's question (43 words): the hand-written H3-P2 and H3-P3 are in
both. So this round sends the whole subsection as published:
- i01: the published H3-P2 to H3-P11 (the first month's practice to the close), without the lead-in line and the sentences the
  dedup carries elsewhere (H3-P8's Senegal sentence, section 2; H3-P9's film, foundation and experiments sentence, section 14;
  preservation-keys.json U41 and U44), H3-P9 reading "The Bruderhof shaped my father. Decades later I'm publishing the film he
  made and writing this."
Four calls, plain text, on the laptop (emulate-runs/community-s16i). Run from this folder: python3 make_inputs.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE.parent / 'v0.md').read_text(encoding='utf-8')) if b.strip()]
i = bl.index('## What to Do This Month')
h3 = [b for b in bl[i + 1:] if not SKIP.match(b)]
assert h3[0].startswith('Here is the first month'), h3[0]
P = {'H3-P%d' % n: h3[n - 1] for n in range(2, 12)}
assert P['H3-P2'].startswith('Start the inner pl/ork'), P['H3-P2']
assert P['H3-P11'].startswith('If you build something real'), P['H3-P11']
SEN = 'I’m in Sénégal and expect to buy land, but I’m not announcing a commune. '
assert P['H3-P8'].count(SEN) == 1
P['H3-P8'] = P['H3-P8'].replace(SEN, '')
FILM = ('The Bruderhof shaped my father. He made a film, founded a research organization, and carried me through communal '
        'experiments. Decades later I’m publishing the film and writing this.')
assert P['H3-P9'] == FILM, P['H3-P9']
P['H3-P9'] = 'The Bruderhof shaped my father. Decades later I’m publishing the film he made and writing this.'
G = {'i01': ['H3-P%d' % n for n in range(2, 12)]}
CALLS = {'i01': 'ABCD'}
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
