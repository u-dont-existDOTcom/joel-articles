#!/usr/bin/env python3
"""apply_r39.py - his round-39 answer (ANSWERS-R39-20261112-2234.json) and his rescue medicine fix of the same message
(2026-11-12 22:34 UTC) into the guide, whole, each from his Pangram check
(../../experiments/t39-answers/JOEL-TRIES-TEACH-EVID.md):

- TEACH-EVID revised: My Brain Feels Damaged's evidence paragraph (B105) is his version (5b09da6c, Human High 137), the
  study links kept on his words, and his DMSO guide linked where he gives the ground of his belief ("you can link my dmso
  guide when it mentions my experience and the books i've read: dmso.u-dont-exist.com").
- His humic acid line: "(see humic acid evidence here and link to humicacid.u-dont-exist.com) after the p13 sentence
  ends", round 39's P13 being the protocol's first step (B144, item 1), put after its humic acid sentence ends, so his
  sentence stays whole (Q-1's "Smell humic acid first; if that doesn't help, take a 5mg lick of it.").
- Active Seizure's rescue medicine paragraph (B110) is his fix of my rescue-c10 (9320d4ec, Human High 73, checked by
  itself), its first-line source (PMC9477921) kept on "benzodiazepines", the word of his that carries the class.

  python3 articles/bad-trips/review/r39/apply_r39.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]
ans = json.loads((HERE / 'ANSWERS-R39-20261112-2234.json').read_text(encoding='utf-8'))
item = [x for x in ans['items'] if x['id'] == 'TEACH-EVID'][0]
assert item['status'] == 'revise'
HEAD = 'If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid + Electrolytes First\n\n'
assert item['your_version'].startswith(HEAD)
EVID = item['your_version'][len(HEAD):].strip()
assert EVID.endswith('DMSO calms NMDA- and AMPA-mediated excitotoxicity that kills brain cells.')

RESCUE = ("If they have a rescue medicine for epilepsy seizures with them, give it as the label instructs. These medicines are "
          "benzodiazepines in nasal spray or rectal gel, or sometimes an intramuscular shot (pills can't be swallowed). After "
          "giving it, keep a close eye on their breathing, since a benzodiazepine adds to the risk of it getting slow and "
          "shallow, especially if they've also taken other respiratory depressants like opioids or alcohol.")


def linked(text, pairs):
    for ctx, words, url in pairs:
        assert text.count(ctx) == 1, ctx
        text = text.replace(ctx, ctx.replace(words, '[%s](%s)' % (words, url)))
    return text


i = ids.index('B102')
assert B[i]['md'] == '## ' + HEAD.strip()
i = ids.index('B105')
assert B[i]['md'].startswith('I believe DMSO works better for stroke')
B[i]['md'] = linked(EVID, [
    ("my experience and those of others I've heard from, as well as the books I've read on this",
     "my experience and those of others I've heard from, as well as the books I've read on this", 'http://dmso.u-dont-exist.com/'),
    ('it shrank the area of the brain that died', 'it shrank the area of the brain that died',
     'https://pubmed.ncbi.nlm.nih.gov/15744247/'),
    ('In one human trial', 'one human trial', 'https://pubmed.ncbi.nlm.nih.gov/11783757/'),
    ('a small series of patients', 'small series of patients', 'https://pubmed.ncbi.nlm.nih.gov/6462399/'),
    ('NMDA- and AMPA-mediated excitotoxicity', 'NMDA- and AMPA-mediated excitotoxicity',
     'https://pubmed.ncbi.nlm.nih.gov/11421595/')])

i = ids.index('B144')
old = "1. **DMSO immediately. Smell humic acid first; if that doesn't help, take a 5mg lick of it. Smell the Metta NMT sniffer**"
assert B[i]['md'].count(old) == 1
B[i]['md'] = B[i]['md'].replace(old, "1. **DMSO immediately. Smell humic acid first; if that doesn't help, take a 5mg lick of it.** "
                                     "(See [humic acid evidence here](http://humicacid.u-dont-exist.com).) **Smell the Metta NMT "
                                     "sniffer**")

i = ids.index('B110')
assert B[i]['md'].startswith("If they have a rescue medicine for seizures with them")
B[i]['md'] = linked(RESCUE, [('are benzodiazepines in nasal spray', 'benzodiazepines',
                              'https://pmc.ncbi.nlm.nih.gov/articles/PMC9477921/')])

MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
have = {e['id'] for e in oe['entries']}
new = [
    {'id': 'r39-evid', 'status': 'applied',
     'what': "My Brain Feels Damaged's evidence paragraph (B105): his version, whole, from his check 5b09da6c (review/r39/apply_r39.py)",
     'joel': '2026-11-12 22:34 UTC (review/r39/ANSWERS-R39-20261112-2234.json, TEACH-EVID revised; '
             'experiments/t39-answers/JOEL-TRIES-TEACH-EVID.md)',
     'must_contain': ["based on my experience and those of others I've heard from",
                      'The clinical evidence is incomplete, but it leans this way.',
                      '(which is a good thing)',
                      'But more relevant to the drug overdose issue this article deals with, DMSO calms']},
    {'id': 'r39-humic', 'status': 'applied',
     'what': "The protocol's first step (B144): his pointer to the humic acid evidence after its humic acid sentence (review/r39/apply_r39.py)",
     'joel': '2026-11-12 22:34 UTC (review/r39/ANSWERS-R39-20261112-2234.json, TEACH-EVID comment: "you can just say (see humic '
             'acid evidence here and link to humicacid.u-dont-exist.com ) after the p13 sentence ends")',
     'must_contain': ['(See [humic acid evidence here](http://humicacid.u-dont-exist.com).)']},
    {'id': 'r39-rescue', 'status': 'applied',
     'what': "Active Seizure's rescue medicine paragraph (B110): his fix of my rescue-c10, whole, from his check 9320d4ec (review/r39/apply_r39.py)",
     'joel': '2026-11-12 22:34 UTC (his message: "look, i fixed the rescue medicine paragraph, it was super obvious stuff just '
             'clarifying and reducing redundancy, now human high"; "i also removed "I\'d" because saying that too much sounds weird")',
     'must_contain': ['If they have a rescue medicine for epilepsy seizures with them, give it as the label instructs.',
                      "(pills can't be swallowed)",
                      'especially if they\'ve also taken other respiratory depressants like opioids or alcohol.']},
]
oe['entries'] += [e for e in new if e['id'] not in have]
for e in oe['entries']:
    if e.get('id') == 'r32-seize-head':
        e['order'] = [x if x != 'If they have a rescue medicine for seizures' else 'If they have a rescue medicine for epilepsy seizures'
                      for x in e['order']]
        if '2026-11-12, turn 41' not in e['order_note']:
            e['order_note'] += '; 2026-11-12, turn 41: the rescue medicine paragraph is his fix (review/r39/apply_r39.py), in the same place'
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied: TEACH-EVID, the humic acid pointer, his rescue paragraph |', len(MD.read_text().split()), 'words')
