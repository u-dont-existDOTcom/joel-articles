#!/usr/bin/env python3
"""apply_h54.py - turn 44 (his message of 2026-11-14 22:08 UTC) into the guide, each change of mine only once its check by
itself read Human High in every window (tools/humanization/apply_gate.py; RESULTS.md has the links).

- DMSO section: his 1967 sentence as he said yes to ("yes i agree to add the anxietry point on dmso patients"), and the
  Hanslick line's "Young brains" said as the study's own concern, children (dmso-h4, Human High 142).
- Metta NMT sniffer: its last sentence says the formula now has creatine and mango leaf tea, that a sniffer from him now has
  everything, and what to buy without one (sniffer-c2, Human High 161).
- Two new entries after Humic Acid, his words of 22:08 UTC fitted: creatine (smell, not snort) and mango leaf tea (smell it
  while it's hot) (remedies-c6, Human High 95).
- My Brain Feels Damaged's evidence paragraph: the study said with where it was done ("at least in rat brain cells in a
  dish"), and its human-trial sentence opened on the people, as the read against his fixes asked (brainev-m6, Human High
  137, one window).

The text each replaces, so it can be undone, is in OLD below.

  python3 articles/bad-trips/humanize/h54-20261114/apply_h54.py      (from the repo root)
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
LEDGER = 'articles/bad-trips/humanize/pangram-ledger.jsonl'

OLD = {
 'R39B-DMSO-2': ("slashing mental patients' psych ward stays in half, although it hasn't been tested (that I know of, yet) "
                 "specifically for anxiety or PTSD, although those patients surely had both of those conditions."),
 'R39B-DMSO-3': "Young brains may be at risk from DMSO, though:",
 'B182': ("It's a bunch of stuff in the formula, but one of the things in here you can buy directly on Amazon for super cheap "
          "right now and it works also very well:"),
 'B105-trial': ("In [one human trial](https://pubmed.ncbi.nlm.nih.gov/11783757/), some clot stroke patients seemed to recover "
                "better on DMSO, and doctors have used it in a [small series of patients](https://pubmed.ncbi.nlm.nih.gov/"
                "6462399/) to bring down dangerous pressure inside the skull."),
 'B105-dish': "that kills brain cells.",
}
NEW = {
 'R39B-DMSO-2': ("slashing mental patients' psych ward stays in half, and that included patients with severe anxiety, though "
                 "it hasn't been tested (that I know of, yet) for PTSD."),
 'R39B-DMSO-3': "Children's brains may be at risk from DMSO, though:",
 'B182': ("It's a bunch of stuff in the formula, and I've now added creatine and mango leaf tea to it, so one you get from me "
          "now already has everything. If you don't have one, three of the things in it you can buy directly on Amazon for "
          "super cheap right now, and they also work very well:"),
 'B105-trial': ("Some patients whose stroke came from a clot seemed to recover better on DMSO in [a human trial](https://"
                "pubmed.ncbi.nlm.nih.gov/11783757/), and doctors have used it in [a handful of patients](https://pubmed.ncbi."
                "nlm.nih.gov/6462399/) to bring down dangerous pressure inside the skull."),
 'B105-dish': "that kills brain cells, at least in rat brain cells in a dish.",
}
NEW_BLOCKS = [
 ('H54-CREATINE-H', 'h3', '### Creatine Is Blissful and Good for the Brain'),
 ('H54-CREATINE', 'p', ("I just discovered that smelling creatine (NOT snorting it, people keep thinking I mean snorting when I "
                        "say smell) is incredible for brain health while high on psychedelics. Just hold the open container "
                        "near your nose and breathe in gently: it's very blissful, and it fixes posture instantly. Like DMSO, "
                        "it seems to strongly protect the brain from inflammation.")),
 ('H54-MANGO-H', 'h3', '### Mango Leaf Tea Relaxes Without Killing the Trip'),
 ('H54-MANGO', 'p', "Mango leaf tea is super relaxing and very blissful, so brew some and smell it while it's hot."),
]
CHECKED = {   # each changed paragraph's checked text (by itself, or with its neighbour when under 50 words)
 'R39B-DMSO-2': 'TEST-dmso-h4.txt', 'R39B-DMSO-3': 'TEST-dmso-h4.txt', 'B182': 'TEST-sniffer-c2.txt',
 'B105': 'TEST-brainev-m6.txt', 'H54-CREATINE': 'TEST-remedies-c6.txt', 'H54-MANGO': 'TEST-remedies-c6.txt',
}


def gate(test):
    r = subprocess.run([sys.executable, 'tools/humanization/apply_gate.py', LEDGER, '--file',
                        str((HERE / test).relative_to(REPO))], cwd=REPO, capture_output=True, text=True)
    if r.returncode:
        sys.exit('refused by apply_gate.py for %s:\n%s' % (test, (r.stdout + r.stderr)[-800:]))


def main():
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    for t in sorted(set(CHECKED.values())):
        gate(t)
    ids = [b['id'] for b in B]
    def sub(bid, key):
        md = B[ids.index(bid)]['md']
        if NEW[key] in md:
            return
        assert md.count(OLD[key]) == 1, (bid, key)
        B[ids.index(bid)]['md'] = md.replace(OLD[key], NEW[key])
    sub('R39B-DMSO-2', 'R39B-DMSO-2')
    sub('R39B-DMSO-3', 'R39B-DMSO-3')
    sub('B182', 'B182')
    sub('B105', 'B105-trial')
    sub('B105', 'B105-dish')
    if 'H54-CREATINE' not in ids:
        i = ids.index('B184')
        assert B[i - 1]['md'] == '### Humic Acid Brings Brain to Optimal Function'
        for n, (bid, kind, md) in enumerate(NEW_BLOCKS):
            B.insert(i + 1 + n, {'id': bid, 'kind': kind, 'md': md, 'text': ''})
    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    have = {e['id'] for e in oe['entries']}
    new = [
     {'id': 'h54-1967-anxiety', 'status': 'applied',
      'what': "The DMSO section's 1967 sentence: the anxiety patients the paper had, and PTSD as what hasn't been tested (humanize/h54-20261114/apply_h54.py)",
      'joel': '2026-11-14 22:08 UTC: "yes i agree to add the anxietry point on dmso patients"',
      'must_contain': ['and that included patients with severe anxiety, though it hasn\'t been tested (that I know of, yet) for PTSD.'],
      'must_not_contain': ['although those patients surely had both of those conditions']},
     {'id': 'h54-creatine-mango', 'status': 'applied',
      'what': ("Creatine (smell, not snort) and mango leaf tea (smell it while it's hot) as entries after Humic Acid, and the "
               "sniffer's formula with both (humanize/h54-20261114/apply_h54.py)"),
      'joel': ('2026-11-14 22:08 UTC: "i want to add another super relaxing herbal remedy which is very blissful and does not '
               'kill the trip: mango leaf tea (smell it while hot) ... smelling creatine (NOT SNORTING IT, ppl keep thinking i '
               'mean snorting when i say smell) is incredible for brain health ... I\'ve add the mango leaf tea and creatine '
               'into my Metta NMT sniffer formula now so if they have that it\'s already got everything, if not they can just '
               'buy these on amazon"'),
      'must_contain': ['### Creatine Is Blissful and Good for the Brain', '### Mango Leaf Tea Relaxes Without Killing the Trip',
                       'NOT snorting it', "so brew some and smell it while it's hot",
                       "I've now added creatine and mango leaf tea to it"]},
    ]
    oe['entries'] += [e for e in new if e['id'] not in have]
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied |', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    main()
