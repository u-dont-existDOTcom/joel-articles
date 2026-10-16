"""Section 13 draft v17 (2026-10-15): v16 with a new H3-P1, the land-title paragraph, which reads Human alone and AI under
its heading (292g, 293g: the same text, AI likelihood 0.61 and 0.56). Three ways, each a hypothesis, each through the gate
(round r11) and to Pangram under the heading:
  A (v17.md): the same paragraph with the published "welcome packet" for "the literature" (a concrete thing), and his
     phrase "a landlord with a philosophy" whole again (Emulate's "just" out; his preference: keep his catchy phrases).
  B (v17b.md): Emulate round h's k02-emuA (the paragraph alone), with the published meaning put back.
  C (v17c.md): A without the opening question (a heading then a rhetorical question is a common AI blog shape), the
     exclamation first.
Writes v17.md, v17b.md, v17c.md and v17-fixes.json. Run from this folder: python3 make_v17.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v16 = blocks((HERE / 'v16.md').read_text(encoding='utf-8'))
i = v16.index('## Resources, Land, and Exit Terms') + 1
OLD = v16[i]
assert OLD.startswith('Who has the title to the land? It matters so much!')
A_FIX = [("then they're really a landlord just with a philosophy.", "then they're really a landlord with a philosophy.",
          'his phrase whole, as published ("a landlord with a philosophy")'),
         ("even if the literature says everyone's equal.", "even if the welcome packet says everyone's equal.",
          'the published "welcome packet", a concrete thing for Emulate\'s "the literature"')]
A = OLD
for o, n, _ in A_FIX:
    assert A.count(o) == 1, o
    A = A.replace(o, n)
emu = (HERE / 'emu-h' / 'out' / 'k02-emuA.txt').read_text(encoding='utf-8')
B_FIX = [("This is very important.", "This is very important!", 'a reaction, as "It matters so much!" was (the march break)'),
         ("The person who holds the title has", "Whoever holds the title has",
          'the published "Whoever owns the land": not one person'),
         ("If the land is in the name of the founder, for instance, then he is essentially a landlord with a philosophy.",
          "If the deed is in the founder's name, for instance, then they're essentially a landlord with a philosophy.",
          'the published deed (key U25), and a founder who is no one in particular ("you have a landlord"); his phrase whole'),
         ("If the land is owned by three out of twelve members,", "If three out of twelve members own everything,",
          'the published "own everything", not only the land'),
         ("despite what the group's literature may say.", "despite what the group's literature may say about everyone being equal.",
          'the published "equal" (key U26)')]
B = emu
for o, n, _ in B_FIX:
    assert B.count(o) == 1, o
    B = B.replace(o, n)
C_FIX = [("Who has the title to the land? It matters so much! Whoever has it", "It matters so much who has the title to the land! Whoever has it",
          'no question right after the heading; the exclamation first (not "The title ...": a third paragraph opening "The" fails B13)')]
C = A
for o, n, _ in C_FIX:
    assert C.count(o) == 1, o
    C = C.replace(o, n)
log = []
for name, txt, fixes, src in (('A', A, A_FIX, 'v16 H3-P1'), ('B', B, B_FIX, 'emu-h/out/k02-emuA.txt'), ('C', C, A_FIX + C_FIX, 'v16 H3-P1')):
    out = list(v16)
    out[i] = txt
    fn = {'A': 'v17.md', 'B': 'v17b.md', 'C': 'v17c.md'}[name]
    (HERE / fn).write_text('\n\n'.join(out) + '\n', encoding='utf-8')
    log.append({'id': 'H3-P1', 'variant': name, 'file': fn, 'source': src,
                'fixes': [{'old': o, 'new': n, 'why': w} for o, n, w in fixes], 'text': txt})
    print(name, '|', txt)
(HERE / 'v17-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
