"""Texts and gate records for this turn's Pangram batches (Joel's answers of 2026-10-14 21:19 UTC).

  python3 fix-20261014b/make_batch.py           # writes drafts.json and GATE.json from HUMANIZED-SO-FAR.md

Every changed text is Joel's own (his section 11 paste, his section 10 paragraph) or his words with a cut or a word
he approved (questions 24 and 26), so each paragraph's record is an owner record. A section's record lists its
parts and the repeats check's result (E172: the repeats run of this turn, gate/REPEATS.md), which pangram_gate.py
requires before the section goes.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
paras = [p.strip() for p in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', art, flags=re.S)) if p.strip()]


def para(start):
    m = [p for p in paras if p.startswith(start)]
    assert len(m) == 1, (start, len(m))
    return plain(m[0])


def pair(a, b):
    return para(a) + '\n\n' + para(b)


Q = '2026-10-14 21:19 UTC'
texts = {
    'J11-P2P3': (pair('That person ends up', "I've seen founderism"), 'his P2 (37 words, under 50) with his P3: "i fixed it, pasted.passes pangram"'),
    'J11-P3': (para("I've seen founderism"), 'his P3'),
    'J11-P4': (para('A few things help keep that in check'), 'his P4: "there was too much stuff in that p4"'),
    'J11-R15': (para('Peer counseling can become peer surveillance'), 'his R15 without the "living balance" sentence ("sect 11: agree agree")'),
    'J10-P5': (para('Whenever you create or apply a rule'), 'his paragraph: "this version is clearer and passes"'),
    'J4-P1pair': (pair('Nothing suppressed, everything processed.', 'Speaking of dynamically weaving'),
                  'his P1 of "Founded on Freedom" without "and don\'t freeze into doctrine" ("sect 4: yes"; 33 words, so with his P2)'),
    'J4-P10pair': (pair('The first three parts are the inside', 'If one of the four gets skipped'),
                   'his "If one of the four gets skipped" ("p10 agree"; under 50 words, so with the paragraph before)'),
    'J9-P14': (para("And that's not me saying that"), 'his P14 with "The useful thing is how they learn:" ("sect 9: yes")'),
    'S4v112': (section(art, '# The Four Parts That Have to Pl/ork Together'), None),
    'S9v16': (section(art, '# The Best Model I’ve Seen: Zapatistas'), None),
    'S10v3': (section(art, '# From One Community to a Movement'), None),
    'S11v15': (section(art, '# Founderism: The Four Questions'), None),
}
drafts, gate = {}, {}
for k, (t, why) in texts.items():
    drafts[k] = t
    if why:
        gate[k] = {'kind': 'owner', 'joel': '%s: %s' % (Q, why), 'words': len(t.split())}
rep = json.loads((HERE / 'repeats.json').read_text(encoding='utf-8')) if (HERE / 'repeats.json').exists() else {}
for k, parts in (('S4v112', ['J4-P1pair', 'J4-P10pair', 'installed']), ('S9v16', ['J9-P14', 'installed']),
                 ('S10v3', ['J10-P5', 'installed']), ('S11v15', ['J11-P2P3', 'J11-P3', 'J11-P4', 'J11-R15', 'installed'])):
    gate[k] = {'kind': 'section', 'parts': parts, 'words': len(drafts[k].split())}
    if k in rep:
        gate[k]['repeats'] = rep[k]
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k in texts:
    print(k, gate[k].get('words'), gate[k]['kind'], gate[k].get('repeats', ''))
