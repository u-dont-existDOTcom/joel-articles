#!/usr/bin/env python3
"""predict.py - turn 45's predictions (pangram_ledger.py predict), written before the checks.

  python3 articles/bad-trips/humanize/h55-20261119/predict.py [KEY...]      (from the repo root)
"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
DET = 'Pangram web app (his account, Pangram Professional), in the desktop app\'s browser pane'
H = 'https://www.pangram.com/history/'
DEC = 'whether it goes into the guide: only Human High by itself (gate bad-trips-2026-11-12l)'
SECT_SS = ('h42-12 read the whole Suspected Serotonin Syndrome section AI Generated, 100%, one AI High window over it all ('
           + H + '4a5da2d5-a8b4-44f4-87d1-b86df0781db3)')
SECT_MDMA = ('h42-09 read the MDMA section AI Detected, 96%, its last window, from his second wife\'s story to the kidney '
             'paragraph, AI High (' + H + '08beb99e-4d7b-45b4-ac6f-32c9bfe3823a)')
P = {
 'cyp-c3': dict(call='Human', chance=0.55, scope='paragraph', batch='h55a',
   lineage="bad-trips Suspected Serotonin Syndrome's cyproheptadine step (h55)",
   tells=["So far, the evidence for it has only been case reports"],
   human=["I wouldn't wait to see whether it does before doing the other steps."],
   humanized=("his round-40 move carried: the limit that decides how far the reader can lean on it (only case reports, which "
              "a review found too weak) first, said once; the five-patient series cut on all three reads; contractions"),
   first=("payoff: the limit of its evidence opens the sentence after the step (lesson 19a); join: the receptors joined to "
          "the step with since; plain: blocks for antagonizes"),
   diagnosis=SECT_SS + ("; this step's sentences are the original's research summary (\"Case reports describe rapid "
                        "improvement, including ..., while a recent systematic review found ...\"), the shape his round-40 "
                        "version replaced. Better: Human High in every window")),
 'mdma-c3': dict(call='Human', chance=0.5, scope='paragraph', batch='h55a',
   lineage="bad-trips MDMA's paragraph after his second wife's story (h55)",
   tells=["If a headache keeps getting worse, the vomiting keeps coming back, or they're getting more and more confused"],
   human=["Once their jaw tenses, that's their last dose of MDMA, so get them to slow down and cool off."],
   humanized=("the original's two lists of signs and concerns taken apart into what each sign can mean and what to do, the "
              "trial said as what decides it first (drinking a lot of plain water) and what to do (sip an electrolyte drink), "
              "its number cut, the kidney review moved to the next paragraph's same claim"),
   first=("payoff: each sentence opens on what the reader sees or does; join: each sign joined to what it means with so; "
          "plain: their last dose, sip, call medics"),
   diagnosis=SECT_MDMA + ("; this paragraph is two compressed lists (\"Worsening headache, confusion, vomiting, weakness, "
                          "palpitations, collapse, or seizure raises concern about sodium, potassium, ...\") and a research "
                          "summary (\"is documented to cause\", \"controlled research confirms\"). Better: Human High")),
 'mdma-c4': dict(call='Human', chance=0.5, scope='paragraph', batch='h55a',
   lineage="bad-trips MDMA's paragraph after his second wife's story (h55)",
   tells=["Is a headache getting worse and worse, does the vomiting keep coming back, or are they more and more confused?"],
   human=["Their sodium may be getting too low, so call medics."],
   humanized=("as mdma-c3, with the signs asked as his triage asks them (\"are they suffering from slow and shallow "
              "breathing ...? Or is it rapid breathing ...?\", the read against his fixes' way 1)"),
   first=("payoff: each sign group asked, then what it can mean and what to do; join: the water line hung on the sodium; "
          "plain: their last dose, sip, call medics"),
   diagnosis=SECT_MDMA + "; c4 tests his triage questions against c3's statements. Better: Human High"),
 'b106-now': dict(call='AI', chance=0.3, scope='paragraph', batch='h55a',
   lineage="bad-trips My Brain Feels Damaged's DMSO-and-bleeding paragraph (h55)",
   tells=["The larger adjacent risk is losing a treatment window or missing a bleed because the symptoms improved enough to "
          "feel reassuring."],
   human=["It's not a powerful blood thinner like heparin, unless maybe injected; it's basically a dietary blood thinner."],
   unchanged=("B106 as the guide has it: two sentences of the original's, which his round-38 version left, then his bleed "
              "lines (KEEP-AS-IS K4); never checked by itself"),
   diagnosis=("never checked by itself; in the section check of 2026-11-11 (h42) it sat in My Brain Feels Damaged's AI "
              "windows. A baseline before changing it: if it reads Human High, it stays")),
 'b106-c2': dict(call='Human', chance=0.6, scope='paragraph', batch='h55a',
   lineage="bad-trips My Brain Feels Damaged's DMSO-and-bleeding paragraph (h55)",
   tells=["So if any of the checks above fail, call medics right away, before the window for treating a stroke closes."],
   human=["I've never had any issues with bleeding too much from consuming DMSO, and never heard of it either, but if "
          "bleeding is already a medical issue I'd want to think about that more."],
   humanized=("his bleed lines first, the limit that decides whether DMSO is for this reader at all (lesson 19a); the "
              "original's two sentences said as what feeling better can hide and what to do (\"call medics right away\")"),
   first=("payoff: his decision first, then what to do; join: the action joined to what it answers with so; plain: \"a "
          "clot or a bleed still there\" for \"missing a bleed\", \"the window for treating a stroke\" for \"a treatment "
          "window\""),
   diagnosis=("b106-now, checked in the same batch, is the baseline; this one puts his lines first and mine after them, "
              "in plain words. Better: Human High"),
   big=("his lines kept whole and moved ahead; the original's two sentences rewritten, which a small fix can't do: \"The "
        "larger adjacent risk is ...\" is the shape his fixes change (way 5, a rule with the reader outside it)")),
}


# h55b, after h55a's results (RESULTS-h55a.json), each with its diagnosis
P['cyp-c4'] = dict(P['cyp-c3'], batch='h55c', chance=0.55,
   tells=["So far, the evidence for it has only been case reports"],
   human=["When doctors gave it to five patients, three had no signs left within two hours, and the other two took longer"],
   humanized=("his round-40 shape whole: the limit first, said as why case reports can't show it works (no one to compare "
              "against), then the study's concrete finding, then what it means for what the reader does"),
   first=("payoff: the finding ends on what to do (keep going with the other steps); join: the finding and its payoff with "
          "so; plain: right away for early, no one to compare against for too weak"),
   diagnosis=("cyp-c3 read AI Detected, 79% (" + H + "33e3c66b-d1ae-4d23-b27a-36eaaee156da): the step Human Low, the limit and "
              "the don't-wait line AI Medium, a bare limit with nothing in it a reader can see. His round-40 version kept "
              "the study's concrete finding after the limit; this brings the series back as what to expect, which the read "
              "against his fixes asked for. Better: Human High"),
   big=("c3's limit sentence read AI Medium as it was: the limit is said again as why (no one to compare against) and the "
        "study's finding comes back as his round-40 version has its rats; a small fix of c3's words keeps the bare limit"))

P['mdma-c4b'] = dict(P['mdma-c3'], batch='h55c', chance=0.5,
   tells=["The same goes for muscles getting weaker and weaker, or palpitations where the heart skips beats"],
   human=["A headache that gets worse and worse is how low sodium tends to show up, often with throwing up or confusion, and "
          "it's time to call medics."],
   humanized=("as mdma-c3, with each sign line built its own way (a statement of how it shows up; \"The same goes for\"; a "
              "seizure as the toxicity become an emergency), the water line in his first person"),
   first=("payoff: each line opens on what the reader sees, ends on what to do; join: the potassium signs joined to the "
          "sodium line's call with \"The same goes for\"; plain: skips beats, gets worse and worse"),
   diagnosis=("mdma-c3 read AI Detected, 87% (" + H + "adc38bd4-0651-498e-90be-4f06c7540ad8): the first line Human Low, the "
              "water line AI Medium, the three sign lines AI High together, each built the same way (\"If ... keeps getting "
              "worse ..., so call medics. Do the same if ... keep getting ...\"). This builds each one differently and puts "
              "the water line in his first person. Better: Human High"),
   big=("c3's three sign lines read AI High as one pattern, so each is rebuilt in its own way; a small fix of one line keeps "
        "the pattern the window sat on"))

P['cyp-c5'] = dict(P['cyp-c3'], batch='h55d', chance=0.5,
   tells=["The evidence for it is only case reports so far"],
   human=["(nobody has compared it against people who didn't get it)"],
   humanized=("his first person (\"I'd give them\"), the drug said as what it is, an aside in brackets, the limit still "
              "first; his bleed lines' way of saying a recommendation, which read Human High in b106-now"),
   first=("payoff: the step and what the drug is lead, the limit opens the evidence, the last line says what keeps going; "
          "join: the finding hung on the limit with but; plain: an old allergy medicine"),
   diagnosis=("cyp-c4 read AI Generated, 100% (" + H + "f65ebe7a-5080-4218-870a-59159cea92bb), one AI High window, worse "
              "than c3's 79%: c3 and c4 changed order and build in my plain instructing voice. In b106-now (" + H +
              "7caaa2f9-b611-4d1f-931c-de6584ed18e0) his lines read Human High beside my AI High two, in his first person "
              "with hedges and asides. This try is in that voice. Better: Human High"),
   big=("c3 and c4 kept my instructing voice and read AI; the voice is what changes, which no fix of a word or two does"))
P['mdma-c5'] = dict(P['mdma-c3'], batch='h55d', chance=0.5,
   tells=["And a seizure or collapse means MDMA toxicity has turned into an emergency"],
   human=["I'd also watch how much plain water they drink, because if they're downing bottle after bottle"],
   humanized=("his first person (\"I'd make that their last dose\", \"I'd also watch\", \"that's when I'd call medics\"), "
              "an aside in brackets, each sign said as it gets past what MDMA does anyway"),
   first=("payoff: each line opens on what the reader sees; join: the water line's reason with because; plain: bottle "
          "after bottle, can barely stand, a heartbeat that feels irregular"),
   diagnosis=("mdma-c4b read AI Generated, 100% (" + H + "1ffa53a8-6c90-4b25-9ea5-9a1523a572cf), one AI High window, worse "
              "than c3's 87%: c3 and c4b changed order and build in my plain instructing voice. In b106-now his lines read "
              "Human High beside my AI High two, in his first person. This try is in that voice. Better: Human High"),
   big=("c3 and c4b kept my instructing voice and read AI; the voice is what changes, which no fix of a word or two does"))

def predict(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope', p['scope'],
         '--text', 'articles/bad-trips/humanize/h55-20261119/TEST-%s.txt' % key, '--key', key, '--batch', p['batch'],
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET, '--diagnosis', p['diagnosis'], '--decides', DEC]
    if p.get('unchanged'):
        a += ['--unchanged', p['unchanged']]
    else:
        a += ['--receipt', 'articles/bad-trips/humanize/h55-20261119/TEST-%s.receipt.json' % key,
              '--humanized', p['humanized'], '--first-fix', p['first']]
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
