#!/usr/bin/env python3
"""build_tests.py - turn 43 (2026-11-13, his messages of 14:56 and 14:59 UTC): the texts this turn reads and checks.

- brainev-m1: My Brain Feels Damaged's evidence paragraph (B105, his round-39 version, Human High 137 by itself, 5b09da6c)
  with its last sentence merged with the DMSO section's description of the same study (his 14:59 UTC message: "i wasn't
  clear on why Lu & Mattson need to be described in 2 places, maybe we can merge that?"). The study is said once, here,
  where his paragraph makes it "more relevant to the drug overdose issue this article deals with": in the plain words of
  his DMSO text ("turned down the signals glutamate sends through its NMDA and AMPA receptors ... kept glutamate from
  killing the cells") instead of the term "NMDA- and AMPA-mediated excitotoxicity", and with where it was found ("in rat
  brain cells in a dish"), as his paragraph says where each other study was done ("In animals", "one human trial").
- dmso-h1: the DMSO section's two evidence paragraphs from his DMSO text, with the two changes he said yes to at 14:56 UTC
  ("organ or stem cell transplants" made "stem cell transplants"; "healthy mice neurons" said as what Hanslick et al.
  found: baby mice from birth to 30 days old, and rat neurons in a dish), and the Lu & Mattson description gone from here
  (said once, in brainev-m1). Its Hanslick sentence opens on DMSO, since the "But" it had turned on Lu & Mattson.
- cp-c3: Chest Pain's evidence paragraph (B123), the next draft turn 42's reads asked for (../h52-20261113/RESULTS.md):
  the findings kept, each said with what it means for the friend, his round-39 way.

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent

B105_HEAD = ("I believe, based on my experience and those of others I've heard from, as well as the books I've read on this, that "
             "DMSO works better for most acute brain damage than anything else readily available. The clinical evidence is "
             "incomplete, but it leans this way. In animals, when given after a stroke, it shrank the area of the brain that "
             "died (which is a good thing). In one human trial, some clot stroke patients seemed to recover better on DMSO, and "
             "doctors have used it in a small series of patients to bring down dangerous pressure inside the skull.")
B105_OLD_END = ("But more relevant to the drug overdose issue this article deals with, DMSO calms NMDA- and AMPA-mediated "
                "excitotoxicity that kills brain cells.")
B105_NEW_END = ("But more relevant to the drug overdose issue this article deals with, DMSO quickly turned down the signals "
                "glutamate sends through its NMDA and AMPA receptors in rat brain cells in a dish, and kept glutamate from "
                "killing them.")

DMSO2 = ("One famous 1967 study by Ramirez & Luza found it more effective than the best antipsychotic drugs at the time, "
         "slashing mental patients' psych ward stays in half, although it hasn't been tested (that I know of, yet) specifically "
         "for anxiety or PTSD, although those patients surely had both of those conditions. It's routinely used in humans who "
         "receive stem cell transplants, as it is the best cell preservative that we've found so far. There is evidence "
         "(Kortleve, et al, 2023) that using too much DMSO (10% vs 5%) in stem cell transfusions increases mild side effects in "
         "adult humans.")
DMSO3 = ("DMSO also appears to kill brain cells when they're exposed to it for too long, as it did in baby mice (from birth to "
         "30 days old) and in a dish of rat neurons (Hanslick, et al, 2009). Translating mouse research to humans isn't "
         "straightforward.")

CP3 = ("The heart research on DMSO is only in animals and lab dishes so far, but it leans the same way. In rats given DMSO "
       "before a heart attack, about three quarters less heart muscle died than in rats without it. Most heart attacks come "
       "from a clot blocking an artery, and DMSO slowed clotting too, including in human platelets.")

TESTS = {
    'brainev-m1': B105_HEAD + ' ' + B105_NEW_END,
    'dmso-h1': DMSO2 + '\n\n' + DMSO3,
    'cp-c3': CP3,
}

if __name__ == '__main__':
    for k, t in TESTS.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])


def section_text(first_id, last_id, heading=None):
    """A stretch of the guide as Pangram gets it: links as their words, no bold, a heading's marks off."""
    import json, re
    B = json.loads((HERE.parents[1] / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    ids = [b['id'] for b in B]
    out = [heading] if heading else []
    for b in B[ids.index(first_id):ids.index(last_id) + 1]:
        s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', b['md']).replace('**', '')
        out.append(re.sub(r'^#{1,6}\s+', '', s))
    return '\n\n'.join(out)


# seize-c12: Active Seizure in place with his call list f6b4e35a and the paragraph after it cut (review/r39/apply_r39c.py),
# checked as it stands (his first aid, his call list, his rescue medicine paragraph).
if __name__ == '__main__':
    t = section_text('B109', 'B110', heading='Active Seizure')
    (HERE / 'TEST-seize-c12.txt').write_text(t + '\n', encoding='utf-8')
    print('seize-c12', len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])


# After the three fresh reads of brainev-m1, dmso-h1 and cp-c3 (reads/), each marked sentence of mine changed:
# - brainev-m2: the term said as what it is, with why glutamate matters in it ("the overstimulation by glutamate ... that
#   kills brain cells", his "calms ... that kills brain cells"), the receptor names (a fidelity key, his) kept in brackets.
# - dmso-h2: the Hanslick sentence said as what the study found (PubMed 19100327's abstract, read 2026-11-13: mice from
#   birth to 30 days old, damage at every age, worst at 7 days, at the lowest dose tested; rat neurons in a dish): young
#   brains, even a low dose. "When they are exposed for too long" is not what it found (the reads: "how long counts?").
# - cp-c4: where the research was done said plainly; the rats' three days before the heart attack, and that the study
#   didn't give it after (PubMed 19904216's abstract: pretreatment only); "so" for the clot's link, platelets explained,
#   mice and human platelets in a dish (PubMed 17000906, 20035720).
B105_M2_END = ("But more relevant to the drug overdose issue this article deals with, in rat brain cells in a dish, DMSO quickly "
               "calmed the overstimulation by glutamate (through its NMDA and AMPA receptors) that kills brain cells.")
DMSO3_H2 = ("Young brains may be at risk from DMSO, though: it killed brain cells in mice up to a month old, even at a low dose, "
            "and in a dish of rat neurons (Hanslick, et al, 2009). Translating mouse research to humans isn't straightforward.")
CP4 = ("The heart research on DMSO has only been in animals and lab dishes so far. Rats given DMSO for three days before a heart "
       "attack lost about three quarters less heart muscle than rats without it, though that study didn't try giving it after "
       "the attack had started. Most heart attacks come from a clot blocking an artery, so it's a good sign that DMSO also "
       "slowed clotting, in mice and in human platelets (the blood cells that start clots) in a dish.")
TESTS2 = {'brainev-m2': B105_HEAD + ' ' + B105_M2_END, 'dmso-h2': DMSO2 + '\n\n' + DMSO3_H2, 'cp-c4': CP4}
if __name__ == '__main__':
    for k, t in TESTS2.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])
