#!/usr/bin/env python3
"""predict.py - this folder's predictions (pangram_ledger.py predict), written before the checks.

  python3 predict.py KEY...      (from anywhere) predict the named tests
"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
DET = 'Pangram web app (his account, Pangram Professional)'
H = 'https://www.pangram.com/history/'
MOVES = ("his round-35 moves (lesson bad-trips-2026-11-12e, SKILL.md's sixth fix): a diagnostic list said as the questions "
         "the reader asks of the body, plain words first and the term in brackets, varied question openers, every state "
         "kept; his five fixes first (the point first, the plain word, what belongs together joined, a long list taken "
         "apart)")
P = {
 'ss-r1': dict(call='AI', chance=0.3,
   lineage="bad-trips Suspected Serotonin Syndrome's recognition part, his round-35 moves carried (h45)",
   tells=['Any one of the following patterns makes serotonin toxicity more likely.',
          'Dangerous heat, rigidity, clonus, confusion, or rapid worsening deserves medical help.'],
   human=['Do you see their eyes darting back and forth in a fast rhythm by themselves',
          'like when you flex their ankle up quickly'],
   first="payoff: the part opens on what one pattern means ('Any one of the following patterns makes serotonin toxicity "
         "more likely'), the Hunter criteria's name cut as a source label (NEEDED-READ.md); join: each criterion one "
         "question, its sign and its companion sign together ('and come with agitation or sweating'); plain: each "
         "criterion said as what the reader sees, the term in brackets after ('muscles contracting and relaxing in a rhythm "
         "on their own ... (spontaneous clonus)', 'eyes darting back and forth in a fast rhythm by themselves (ocular "
         "clonus)'), 'a recognition aid rather than a command to wait for every criterion' to 'Don't wait to see every one "
         "of these before you act'",
   diagnosis="h42a read Suspected Serotonin Syndrome (SS) AI Generated, 100%% (%s4a5da2d5-a8b4-44f4-87d1-b86df0781db3); "
             "this is its recognition part (B131 to B134), the first try in this lineage" % H),
 'acute-r1': dict(call='AI', chance=0.35,
   lineage="bad-trips Acute Medical and Neurological Rescue, its first two paragraphs, his round-35 moves carried (h45)",
   tells=["Someone who's severely altered but physically stable may come down sooner with your help than after an "
          "ambulance ride and hours in an emergency room.",
          "If all of that's true, calming and stabilizing the trip may be enough."],
   human=['An emergency means act now, and sometimes the fastest help is right where they are.',
          'Are they awake enough to work with you, and can you keep them physically safe?'],
   first="payoff: the section opens on acting now and where the fastest help may be ('sometimes the fastest help is right "
         "where they are'); join: B76's six conditions in three questions, two a question; plain: 'not dangerously hot' to "
         "'is their temperature safe', 'has no neurological-injury concern' to 'nothing suggesting a brain injury', "
         "'remains conscious enough to cooperate' to 'awake enough to work with you', 'field rescue' to 'with your help', "
         "'It does not always mean that an ambulance is the first or only useful action' said as what can help instead, "
         "the ambulance pictured ('an ambulance ride and hours in an emergency room')",
   diagnosis="h42a read Acute Medical and Neurological Rescue AI Generated, 100%% (%s0df121e8-abda-428e-aa4f-a93887e4bf18); "
             "this is its first two paragraphs (B100, B76), the first try in this lineage" % H),
}


def predict(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', p['lineage'], '--scope', 'pair', '--text',
         'articles/bad-trips/humanize/h45-20261112/TEST-%s.txt' % key, '--key', key, '--batch', 'h45a',
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h45-20261112/TEST-%s.receipt.json' % key,
         '--humanized', MOVES, '--first-fix', p['first'], '--diagnosis', p['diagnosis'],
         '--decides', "whether it goes into the guide (TEACH-ORAL's promise) and whether his round-35 moves carry in my words"]
    for t in p['tells']:
        a += ['--tells', t]
    for t in p['human']:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1] if out else r.returncode)
    if r.returncode:
        print(out)

P['ss-r1-fix2'] = dict(call='AI', chance=0.35, lineage=P['ss-r1']['lineage'], batch='h45b',
   tells=['Any one of the following patterns makes serotonin toxicity more likely.',
          'Dangerous heat, rigidity, clonus, confusion, or rapid worsening deserves medical help.'],
   human=['Are they shaking, with reflexes that are way too brisk?',
          'Does the jerking start when you stretch a muscle, like flexing their foot up quickly'],
   first="payoff: unchanged, the part opens on what one pattern means; join: each criterion still one question, its "
         "companion sign joined in a looser shape ('and are they also agitated or sweating?'); plain: one clinical term "
         "for the whole list, named where first used ('that's called clonus'), the other signs only in plain words "
         "('reflexes that are way too brisk', 'that eye or stretch-triggered clonus')",
   diagnosis="try 1 read AI Generated, 100%% (%s02fb701a-4fdd-44dc-b43b-c8cfba529429), one AI High window over the whole "
             "text: a bracketed clinical term closed every question, an even rhythm. His five oral tries "
             "(experiments/t35-answers/JOEL-TRIES-TEACH-ORAL.md) went Human on a working construction for a tidy parallel "
             "one and a list left loose, with one bracketed term for the whole list. This try names clonus once and says "
             "the rest in plain words, the questions in looser shapes; better is any window below AI High" % H)
P['acute-r1-fix2'] = dict(call='AI', chance=0.35, lineage=P['acute-r1']['lineage'], batch='h45b',
   tells=["An emergency means act now, and sometimes the fastest help is right where they are."],
   human=['No seizures, and nothing that looks like a brain injury?', 'If all that checks out'],
   first="payoff: unchanged, the section opens on acting now and where the fastest help may be; join: the speed claim put "
         "on the reader ('you may bring them down faster yourself than an ambulance ride and hours in an emergency room "
         "would'); plain: the Medium window kept as it was ('So check the body first. Are they breathing normally, and is "
         "their temperature safe?'), 'with nothing suggesting a brain injury' to 'nothing that looks like a brain injury', "
         "'can you keep them physically safe' to 'can you keep them from getting hurt', 'If all of that's true' to 'If all "
         "that checks out'",
   diagnosis="try 1 read AI Generated, 100%% (%seedc2eec-ceb0-493b-a41b-366d703ab11c): AI High on the opening, Medium on "
             "'So check the body first' and the first check, High on the rest. The Medium part stays as it was; the "
             "comparison sentence gives the faster help to the reader instead of to 'Someone ... with your help', and the "
             "last two checks break the 'Are they X, and Y?' rhythm with a fragment question; better is any window below "
             "AI High" % H)


def predict2(key):
    p = P[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', p['lineage'], '--scope', 'pair', '--text',
         'articles/bad-trips/humanize/h45-20261112/TEST-%s.txt' % key, '--key', key, '--batch', p['batch'],
         '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h45-20261112/TEST-%s.receipt.json' % key,
         '--humanized', MOVES, '--first-fix', p['first'], '--diagnosis', p['diagnosis'],
         '--decides', "whether it goes into the guide (TEACH-ORAL's promise) and whether his round-35 moves carry in my words"]
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
        (predict2 if k.endswith('-fix2') else predict)(k)
