#!/usr/bin/env python3
"""predict.py - this folder's predictions (pangram_ledger.py predict), written before the checks.

  python3 predict.py KEY...
"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
DET = 'Pangram web app (his account, Pangram Professional)'
H = 'https://www.pangram.com/history/'
MOVES = ("the lessons of rounds 37 and 38 (lessons bad-trips-2026-11-12h and i): the action first and what it serves after it "
         "(his Chest Pain try 7, flipped AI Generated, 100% to Human), the paragraph rebuilt around it (acute-c1, brainopen-c1, "
         "er-c3: Human High), each line the kind of thing its lead-in says; and since his fixes of 19:44 UTC (5e41c575, "
         "a0b8ac56), the fit read (lesson bad-trips-2026-11-12j): nothing true anyway of someone tripping, nothing a friend "
         "can't tell, no rule from another setting")
P = {
 'rescue-c8': dict(call='Human', chance=0.55, scope='section', batch='h50a',
   lineage="bad-trips Active Seizure's rescue medicine, rounds 37-38 lessons carried (h50)",
   tells=["These are benzodiazepines, the same first drugs doctors reach for when a seizure won't stop.",
          "After giving it, keep watching their breathing, since a benzodiazepine adds to the risk of it getting slow and "
          "shallow, especially if they've also taken respiratory depressants like opioids or alcohol."],
   human=["A few are intramuscular shots.", "- They get dangerously hot (not just regular sweating)."],
   first=("payoff: the paragraph opens on what to do with a rescue medicine on hand ('follow its label for when and how to "
          "give it'), then what it is, its forms, and what to watch after giving it; join: the forms one sentence with their "
          "reason, the breathing sentence with its reason and 'especially if', his shape (his electrolytes sentence, "
          "a0b8ac56); plain: 'an appropriate rapid seizure-rescue benzodiazepine' as 'a rescue medicine for seizures ..., "
          "like one they carry for epilepsy', 'the established first-line drug class for status epilepticus' as 'the same "
          "first drugs doctors reach for when a seizure won't stop', 'respiratory depressants in the mix change the risk' as "
          "what to watch, in his call list's words ('slow and shallow')"),
   diagnosis=("h42a read Active Seizure (1 of 2) AI Detected, 31% (" + H + "6280b126-8af7-4def-9ae2-f8d11b722990), B110 in "
              "three AI windows (High 54 from its first sentence, Medium 11, High 62); his first aid and call list since then "
              "read Human, High (" + H + "5e41c575-7ebf-4b42-9059-adddbf2c5a7f). This is B110 rebuilt after eight drafts and "
              "their reads, checked with his lists as they stand. Better: Human windows over B110"),
   unchanged=("the heading, the lead-ins, the first aid and the call list, as he wrote them at 19:44 UTC (5e41c575, Human "
              "High); the last paragraph is mine")),
 'brainev-c1': dict(call='AI', chance=0.4, scope='paragraph', batch='h50a',
   lineage="bad-trips My Brain Feels Damaged's evidence paragraph, rounds 37-38 lessons carried (h50)",
   tells=["My judgment goes further than the clinical evidence, but that evidence points the same way.",
          "It also suppresses NMDA- and AMPA-mediated excitotoxicity, the overexcited nerve signaling that kills brain cells "
          "after a stroke."],
   human=["People who'd had a stroke from a clot may have recovered better on DMSO in a preliminary trial."],
   first=("payoff: his belief first as it is, then how far the evidence goes, then each study saying what it means for the "
          "reader, ending the animal study on what to do ('so it may still help if you start late'); join: one study a "
          "sentence instead of three in one with semicolons; plain: 'preliminary human ischemic-stroke trial reported "
          "possible neurological benefit' as 'People who'd had a stroke from a clot may have recovered better', "
          "'intracranial hypertension' as 'dangerous pressure inside the skull', 'substantial infarct reduction even when "
          "treatment began after ischemia' as 'shrank the area of the brain that died, even when treatment started after the "
          "stroke', 'That judgment is stronger than the clinical evidence, but the evidence is not empty' as 'My judgment "
          "goes further than the clinical evidence, but that evidence points the same way'"),
   diagnosis=("h42a read My Brain Feels Damaged AI Detected, 65% (" + H + "4076db14-325a-4854-88b1-fc3c82da040a); B105 has not "
              "been read alone. His checks above it read Human, High (" + H + "a0b8ac56-c015-4374-afbc-996a9a37f870). This is "
              "B105 with its heading. Better: Human windows over B105"),
   unchanged="the heading and the first sentence (his belief), as the guide has them; the rest is mine"),
}

P['rescue-c9'] = dict(P['rescue-c8'], batch='h50b', chance=0.55, call='Human',
   tells=["It's a benzodiazepine, which is what doctors reach for first when a seizure won't stop."],
   human=["Because a pill is no use while someone's seizing, it comes as a nasal spray or a rectal gel, or sometimes an "
          "intramuscular shot.", "If there's a rescue medicine for seizures on hand, like one they carry for epilepsy, follow "
          "its label for when and how to give it."],
   first=("payoff: unchanged, the action first; join: the forms and the shot one sentence, with the reason first; plain: the "
          "class said of what they hold ('It's a benzodiazepine, which is what doctors reach for first ...') instead of an "
          "appositive definition ('These are benzodiazepines, the same first drugs ...')"),
   diagnosis=("rescue-c8 read AI Detected, 17% (" + H + "ed4fe070-ae91-4317-b946-a25cfd4bf60f): his lists Human High, my "
              "first sentence and last two Human Low, and AI Low 44 over 'These are benzodiazepines, the same first drugs "
              "doctors reach for ...' and 'They come in forms you don't have to swallow ...'. This says those two as what "
              "they hold and what it will be. Better: no AI window"))

P['brainev-c2'] = dict(P['brainev-c1'], batch='h50b', chance=0.45, call='AI',
   tells=["It also calms the overexcited nerve signaling that kills brain cells after a stroke (NMDA- and AMPA-mediated "
          "excitotoxicity)."],
   human=["That's more than the clinical evidence shows so far, but what there is points the same way."],
   first=("payoff: after his belief and how far the evidence goes, the finding the reader can act on ('so it may still help "
          "after the damage has started'); join: the two findings in people one sentence of two shapes, not one study a "
          "sentence; plain: the mechanism said plainly with its term in brackets after it, his shape"),
   diagnosis=("brainev-c1 read AI Detected, 72% (" + H + "a8a986e7-f324-4e8a-9561-b542fa57b413): his belief and the heading "
              "Human Low, every sentence after it AI, the animal study with its 'so it may still help if you start late' AI "
              "High. This rebuilds it around that finding. Better: Human windows after his belief"))

P['rescuep-c9'] = dict(P['rescue-c9'], scope='paragraph', batch='h50b',
   lineage="bad-trips Active Seizure's rescue paragraph (B110) by itself, rounds 37-38 lessons carried (h50)",
   human=P['rescue-c9']['human'],
   unchanged="nothing: the paragraph is mine, checked by itself as the ledger asks after its section read Mixed")

P['rescuep-c10'] = dict(P['rescuep-c9'], batch='h50c', chance=0.5, call='Human',
   tells=["It's a benzodiazepine, the kind of drug doctors reach for first when a seizure won't stop."],
   human=["If they have a rescue medicine for seizures with them, like one they carry for epilepsy, I'd give it when and how "
          "its label says.", "After giving it, I'd keep a close eye on their breathing, since a benzodiazepine adds to the "
          "risk of it getting slow and shallow, especially if they've also taken respiratory depressants like opioids or "
          "alcohol."],
   first=("voice: the same facts said in his first person ('I'd give it when and how its label says', 'I'd keep a close eye "
          "on their breathing'), his condition-first shape ('For steady chest pain that's mild, I'd just use DMSO ...'); "
          "plain: the forms said as what it will be ('so it'll be a nasal spray or a rectal gel, or sometimes an "
          "intramuscular shot')"),
   diagnosis=("rescuep-c9 read AI Generated, 100% by itself (" + H + "9f5b6765-c18b-4d59-9d64-036539a08f20), every window AI; "
              "its four sentences explain in the guide's impersonal register. My carries that read Human High this week spoke "
              "in his first person (acute-c1, 97bf9589). Better: Human windows"))

P['rescue-c10'] = dict(P['rescue-c8'], batch='h50d', chance=0.45, call='AI',
   narrowed="bad-trips Active Seizure's rescue paragraph (B110) by itself, rounds 37-38 lessons carried (h50)",
   tells=["After giving it, I'd keep a close eye on their breathing, since a benzodiazepine adds to the risk of it getting "
          "slow and shallow, especially if they've also taken respiratory depressants like opioids or alcohol."],
   human=["A pill is no use while someone's seizing, so it'll be a nasal spray or a rectal gel, or sometimes an "
          "intramuscular shot."],
   first=P['rescuep-c10']['first'],
   diagnosis=("rescue-c8 read AI Detected, 17% in its section (" + H + "ed4fe070-ae91-4317-b946-a25cfd4bf60f), AI Low over "
              "its two middle sentences; narrowed to the paragraph, rescuep-c9 read AI Generated, 100% (" + H +
              "9f5b6765-c18b-4d59-9d64-036539a08f20) and rescuep-c10, in his first person, AI Detected, 79% (" + H +
              "cdc63980-b7da-43a7-b684-819d7d4ac1c8), its forms sentence Human. This is rescuep-c10 back in its section, "
              "where his lists read Human High. Better: no AI window"))


def predict(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', p['lineage'], '--scope', p['scope'], '--text',
         'articles/bad-trips/humanize/h50-20261112/TEST-%s.txt' % key, '--key', key, '--batch', p['batch'],
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h50-20261112/TEST-%s.receipt.json' % key,
         '--humanized', MOVES, '--first-fix', p['first'], '--diagnosis', p['diagnosis'], '--unchanged', p['unchanged'],
         '--decides', "whether it goes into the guide (his \"continue\" of 19:44 UTC; no card while my rebuilt carries pass)"]
    if p.get('narrowed'):
        a += ['--narrowed', p['narrowed']]
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
