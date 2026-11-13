#!/usr/bin/env python3
"""apply_h53.py - the Lu & Mattson merge he asked for (2026-11-13 14:59 UTC: "i wasn't clear on why Lu & Mattson need to be
described in 2 places, maybe we can merge that?") and the Hanslick point he said yes to (14:56 UTC), into the guide, each
only once its check by itself read Human High (tools/humanization/apply_gate.py, gate bad-trips-2026-11-12l).

- B105 (My Brain Feels Damaged's evidence paragraph): its last sentence carries the study in the plain words of his DMSO
  text, with where it was found, the link on the words that name what DMSO did (brainev-m1).
- R39B-DMSO-3 (the DMSO section): the two sentences describing the same study go (said once, in B105); the Hanslick
  sentence says what that study found, and opens on DMSO since its "But" turned on Lu & Mattson (dmso-h1).
- The fidelity keys: his DMSO text's "0.5 to 1.5%" (FIDELITY-KEYS-R41's numbers_new "0.5to1.5") goes with the
  description he asked to have said once: an owner change, R42.

The text each replaces, so it can be undone:
  B105's last sentence: "But more relevant to the drug overdose issue this article deals with, DMSO calms [NMDA- and
  AMPA-mediated excitotoxicity](https://pubmed.ncbi.nlm.nih.gov/11421595/) that kills brain cells."
  R39B-DMSO-3: "In rat brain cells in a dish, DMSO at 0.5 to 1.5% quickly turned down the signals glutamate sends through
  its NMDA and AMPA receptors, and the calcium they let in. It also kept glutamate from killing the cells ([Lu & Mattson,
  2001](https://pubmed.ncbi.nlm.nih.gov/11421595/)). But it also appears to be neurotoxic to healthy mice neurons when
  they are exposed for too long ([Hanslick, et al, 2009](https://pubmed.ncbi.nlm.nih.gov/19100327/)). Translating mouse
  research to humans isn't straightforward."

  python3 articles/bad-trips/humanize/h53-20261113/apply_h53.py [--only brainev|dmso|cp]      (from the repo root)
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
LEDGER = ART / 'humanize' / 'pangram-ledger.jsonl'

B105_OLD = ("But more relevant to the drug overdose issue this article deals with, DMSO calms [NMDA- and AMPA-mediated "
            "excitotoxicity](https://pubmed.ncbi.nlm.nih.gov/11421595/) that kills brain cells.")
B105_NEW = ("But more relevant to the drug overdose issue this article deals with, in rat brain cells in a dish, DMSO quickly "
            "[calmed the overstimulation by glutamate](https://pubmed.ncbi.nlm.nih.gov/11421595/) (through its NMDA and AMPA "
            "receptors) that kills brain cells.")
D3_OLD = ("In rat brain cells in a dish, DMSO at 0.5 to 1.5% quickly turned down the signals glutamate sends through its NMDA and "
          "AMPA receptors, and the calcium they let in. It also kept glutamate from killing the cells ([Lu & Mattson, 2001]"
          "(https://pubmed.ncbi.nlm.nih.gov/11421595/)). But it also appears to be neurotoxic to healthy mice neurons when they "
          "are exposed for too long ([Hanslick, et al, 2009](https://pubmed.ncbi.nlm.nih.gov/19100327/)). Translating mouse "
          "research to humans isn't straightforward.")
D3_NEW = ("Young brains may be at risk from DMSO, though: it killed brain cells in mice up to a month old, even at a low dose, "
          "and in a dish of rat neurons ([Hanslick, et al, 2009](https://pubmed.ncbi.nlm.nih.gov/19100327/)). Translating mouse "
          "research to humans isn't straightforward.")
CP_OLD = ("The cardiovascular science is preclinical but relevant. In rats, DMSO pretreatment reduced myocardial infarct size by "
          "about three quarters and sharply reduced cardiac injury markers. Other work found inhibition of tissue factor, platelet "
          "activation, and arterial thrombus formation. [Myocardial-ischemia study](https://pubmed.ncbi.nlm.nih.gov/19904216/); "
          "[tissue-factor and thrombosis study](https://pubmed.ncbi.nlm.nih.gov/17000906/); [human platelet study]"
          "(https://pubmed.ncbi.nlm.nih.gov/20035720/).")
CP_NEW_C3 = ("The heart research on DMSO is only in animals and lab dishes so far, but it leans the same way. [In rats given DMSO "
          "before a heart attack](https://pubmed.ncbi.nlm.nih.gov/19904216/), about three quarters less heart muscle died than in "
          "rats without it. Most heart attacks come from a clot blocking an artery, and DMSO [slowed clotting]"
          "(https://pubmed.ncbi.nlm.nih.gov/17000906/) too, including [in human platelets](https://pubmed.ncbi.nlm.nih.gov/20035720/).")

CHANGES = {
    'brainev': [('B105', B105_OLD, B105_NEW, 'TEST-brainev-m2.txt')],
    'dmso': [('R39B-DMSO-3', D3_OLD, D3_NEW, 'TEST-dmso-h2.txt')],
    'cp': [('B123', CP_OLD, CP_NEW_C3, 'TEST-cp-c4.txt')],
}


def gate(test_file):
    """apply_gate.py on the checked text: Human High in every window, by itself."""
    r = subprocess.run([sys.executable, 'tools/humanization/apply_gate.py', str(LEDGER.relative_to(REPO)), '--file',
                        str((HERE / test_file).relative_to(REPO))], cwd=REPO, capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()[-600:])
    return r.returncode == 0


def main(only):
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = [b['id'] for b in B]
    done = []
    for name, changes in CHANGES.items():
        if only and name not in only:
            continue
        for bid, old, new, test in changes:
            md = B[ids.index(bid)]['md']
            if new in md:
                done.append(name)
                continue
            if not gate(test):
                print('NOT APPLIED (no Human High check by itself):', name)
                continue
            assert old in md, (bid, md[:200])
            B[ids.index(bid)]['md'] = md.replace(old, new)
            done.append(name)
    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied:', done, '|', len(MD.read_text(encoding='utf-8').split()), 'words')
    return done


if __name__ == '__main__':
    only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None
    main(only)
