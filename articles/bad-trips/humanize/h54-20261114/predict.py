#!/usr/bin/env python3
"""predict.py - turn 44's predictions (pangram_ledger.py predict), written before the checks.

  python3 articles/bad-trips/humanize/h54-20261114/predict.py [KEY...]      (from the repo root)
"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
DET = 'Pangram web app (his account, Pangram Professional)'
H = 'https://www.pangram.com/history/'
DEC = 'whether it goes into the guide: only Human High by itself (gate bad-trips-2026-11-12l)'
P = {
 'dmso-h4': dict(call='Human', chance=0.65, scope='pair', batch='h54a',
   lineage="bad-trips DMSO section's evidence paragraphs, Lu & Mattson out and Hanslick as found (h53)",
   tells=["Children's brains may be at risk from DMSO, though"], human=["slashing mental patients' psych ward stays in half"],
   humanized=("his 1967 sentence in the wording he said yes to (the anxiety patients, then PTSD), and the Hanslick line's "
              "\"young\" said as the study's own concern, children, after the three fresh reads of dmso-h3"),
   first=("payoff: the 1967 finding leads and the anxiety patients follow it; join: his clause joined with and, though; plain: "
          "children for young brains"),
   diagnosis=("dmso-h2 read Human High 146 (" + H + "c6e7b513-a4d2-43e0-88dd-a4b950d1fc96); this changes his 1967 sentence as "
              "he said yes to and one word group of the Hanslick line. Better: Human High in every window")),
 'remedies-c4': dict(call='Human', chance=0.6, scope='pair', batch='h54a',
   lineage="bad-trips creatine and mango leaf tea entries (h54)",
   tells=["Like DMSO, it seems to strongly protect the brain from inflammation."],
   human=["When I say smell, I mean smell: people keep thinking I mean snorting it."],
   humanized=("his message's words in his first person, each claim his; how to smell it said before the snorting misreading; "
              "the mango leaf tea's reason first joined with so; after the three fresh reads of remedies-c2"),
   first=("payoff: what creatine does leads, then how; join: mango leaf tea's two sentences one with so; plain: neuroprotective "
          "against neuroinflammation as protect the brain from inflammation"),
   diagnosis=("New: his creatine and mango leaf tea, from his message of 22:08 UTC, fitted as two entries of the stabilizers part. "
              "Better: Human High in every window")),
 'sniffer-c2': dict(call='Human', chance=0.65, scope='paragraph', batch='h54a',
   lineage="bad-trips Metta NMT sniffer paragraph with the new formula (h54)",
   tells=["so one you get from me now already has everything"], human=["It turns regular ayahuasca into loveyhuasca even."],
   humanized=("his paragraph whole but its last sentence, which now says what his message says in his words (\"I've now added\", "
              "\"super cheap\"), which sniffers have it, and what to buy without one; after the three fresh reads of sniffer-c1"),
   first="payoff: what changed leads the sentence; join: none, his last line kept as one; plain: his words",
   diagnosis=("His sniffer paragraph with its last sentence changed for his message of 22:08 UTC. Better: Human High in every "
              "window")),
 'brainev-m3': dict(call='Human', chance=0.65, scope='paragraph', batch='h54a',
   lineage="bad-trips My Brain Feels Damaged's evidence paragraph with Lu & Mattson said once (h53)",
   tells=["at least in rat brain cells in a dish"], human=["In animals, when given after a stroke, it shrank the area of the brain that died (which is a good thing)."],
   humanized=("his sentence kept whole with where the study was done added at its end; no brackets, as his round-39 move "
              "(\"integrate the clearly higher academic register at the end with via instead of parens\")"),
   first=("payoff: his frame and finding lead, where it was found closes; join: the qualifier joined to his sentence; plain: his "
          "term as he integrated it"),
   diagnosis=("brainev-m2 read Human with his \"In one human trial\" sentence Low and mine Medium (" + H + "6172bd9e-4ac4-4b48-"
              "8079-da639dbeb7f6): two clauses before the subject and a bracket. This keeps his sentence's shape. Better: Human "
              "High in every window")),
 'brainev-m4': dict(call='Human', chance=0.5, scope='paragraph', batch='h54a',
   lineage="bad-trips My Brain Feels Damaged's evidence paragraph with Lu & Mattson said once (h53)",
   tells=["the glutamate overload via NMDA and AMPA receptors that kills brain cells"],
   human=["In animals, when given after a stroke, it shrank the area of the brain that died (which is a good thing)."],
   humanized=("his sentence's shape, the term said as what it is with his \"via\" instead of a bracket, and where it was found "
              "at the end"),
   first=("payoff: his frame and DMSO calming it lead; join: the gloss joined as an appositive; plain: excitotoxicity said as "
          "the glutamate overload that kills brain cells"),
   diagnosis=("brainev-m2's Medium window over my bracketed gloss; his round-39 move put the term in with via. Better: Human "
              "High in every window")),
 'cp-c7': dict(call='Human', chance=0.5, scope='pair', batch='h54a',
   lineage="bad-trips Chest Pain's evidence paragraph (h52)",
   tells=["so it's a good sign that DMSO slows clotting"], human=["After I overused erythritol, I developed angina that lasted for days."],
   humanized=("the rats cut (the needed read: no use once pain has started), the clot said first as what chest pain can come "
              "from, then where DMSO slowed it, in its own sentence, and how far that goes"),
   first=("payoff: the clot's link to chest pain leads; join: where it slowed clotting and how far the research goes in one "
          "sentence with though; plain: the blood cells that start clots"),
   diagnosis=("cp-c4 read AI Assisted in every sentence (" + H + "2c13fbe7-3693-4dcf-9726-cf6fea660532), a research summary with "
              "no one in it; the reads of c5 and c6 found the rats of no use to a friend whose pain has started. Checked with his "
              "story, the paragraph being under 50 words. Better: Human High in every window"),
   big=("the rat study goes on the needed read, so the paragraph is two sentences of c4's third rebuilt; the small fixes of c4 "
        "kept the summary its AI windows sat on")),
}

# h54b, after h54a's results (RESULTS-h54a.json), each with its diagnosis
P['remedies-c5'] = dict(P['remedies-c4'], batch='h54b', chance=0.65,
   tells=["so just hold the open container near your nose and breathe in gently"],
   first="payoff: what creatine does leads; join: the how joined to the misreading it answers, with so; plain: his words",
   diagnosis=("remedies-c4 read Human with a Low window over its short how-to sentence alone (" + H + "73b0ad36-2023-47a3-9e35-"
              "17b7752f6a12). Joined to the misreading it answers, as his fixes join short sentences. Better: Human High in "
              "every window"))
P['brainev-m5'] = dict(P['brainev-m3'], batch='h54b', chance=0.65,
   first="payoff: his frame and finding lead; join: none; plain: a human trial for one human trial, his rule on one",
   diagnosis=("brainev-m3 read Human High over my clause and Medium over his \"In one human trial\" sentence (" + H +
              "dcca4831-5f9e-4c36-8d3f-1a53ac02a1b8). \"one\" where \"a\" does is his own rule (it took a window AI High "
              "to Medium). Better: Human High in every window"))
P['cp-c8'] = dict(P['cp-c7'], batch='h54b', chance=0.5, big=None,
   tells=["and DMSO slowed clotting in mice and in a dish of human platelets"],
   first=("payoff: the clot leads, the finding follows with where it was found inside it; join: two sentences made one with "
          "and; plain: no hedge tail, no bracket"),
   diagnosis=("cp-c7 read Human with Medium over \"so it's a good sign that\" and Low over the hedge tail and the bracket (" +
              H + "dbfa1b8b-a9f1-44a3-8bf5-d06f6c7e9a74). One sentence, where it was found said with the finding. Better: "
              "Human High in every window"))

# h54c, after h54b's results (RESULTS-h54b.json)
P['remedies-c6'] = dict(P['remedies-c4'], batch='h54c', chance=0.6,
   big=("the small fixes of the snorting line are spent: c4 alone read Low, c5 joined read Medium; c6 puts back his own "
        "words of 22:08 UTC for it, which moves the first two sentences"),
   tells=["Just hold the open container near your nose and breathe in gently:"],
   human=["(NOT snorting it, people keep thinking I mean snorting when I say smell)"],
   first=("payoff: his discovery leads with the misreading answered inside it; join: the how joined to what it does; plain: "
          "his own words of 22:08 UTC"),
   diagnosis=("remedies-c5 read Medium over the snorting line with the how joined to it (" + H + "926dedd8-6d87-4c52-9526-"
              "071e37cadc13); this says it in his own words of 22:08 UTC. Better: Human High in every window"))
P['brainev-m6'] = dict(P['brainev-m3'], batch='h54c', chance=0.55,
   first=("payoff: the people lead their sentence; join: none; plain: patients whose stroke came from a clot, a handful of "
          "patients"),
   diagnosis=("brainev-m3 and m5 read Medium over his human-trial sentence (" + H + "c57fc390-e1be-4e4a-8b2f-11d8effb1555); the "
              "read against his fixes: a second \"In ...\" opening after \"In animals\", stacked nouns. Better: Human High "
              "in every window"))


def predict(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope', p['scope'],
         '--text', 'articles/bad-trips/humanize/h54-20261114/TEST-%s.txt' % key, '--key', key, '--batch', p['batch'],
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h54-20261114/TEST-%s.receipt.json' % key,
         '--humanized', p['humanized'], '--first-fix', p['first'], '--diagnosis', p['diagnosis'], '--decides', DEC]
    if p.get('big'):
        a += ['--big-change', p['big']]
    for t in p['tells']:
        a += ['--tells', t]
    for t in p['human']:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1] if out else r.returncode)
    if r.returncode:
        print(out)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(P):
        predict(k)
