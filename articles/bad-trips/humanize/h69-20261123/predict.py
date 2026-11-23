#!/usr/bin/env python3
"""predict.py - turn 61's predictions (pangram_ledger.py predict), written before the checks: the serotonin steps from
his round-50 answers (2 with his dose lines, 5 with his tapping, 6 from his notes, 7 with his seizure line, 8 with his
DMSO answer), and the three edits he approved on round 50's cards (the call list's "No sleep for days", "acting on a
delusion", the shungite water's ozone line). Through the API with his key, on his laptop (he added credits on
2026-11-23: "they added api credits to my pangram also if you want to do any testing that would benefit from the api
result").

  python3 predict.py [KEY...]
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h69-20261123/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
_A = __import__('sys').argv[1:]
BATCH = 'h69d' if any(a.startswith('a8-') for a in _A) else 'h69c' if any(a.startswith('a7-') for a in _A) else 'h69b' if any(a.startswith('a6-') for a in _A) else 'h69a'
HUM = ('written from his round-50 answers the ways his checks showed: each sentence ties to the one before at its start, '
       'the payoff first, the reader\'s doubt answered where it comes up, the state an act depends on said first; one round '
       'of the three fresh reads, their marks answered (reads/*-a5-ss.txt)')
FIRST = {
    'a5-ss6': ('payoff: what to make first ("a salty potato broth"), then what to do with it ("give it slowly"); join: each '
               'sentence tied at its start (That, If you don\'t have the flakes, Whatever you give, So); plain: which way '
               'potassium goes said outright, as he asked; the sentence his checks showed reading AI ("And while you might '
               'think to add potassium too ...") is gone, its point now his'),
    'a5-ss7': ('payoff: his seizure line as he checked it ("If they have a seizure while you wait for an ambulance"); join: '
               '"Then"; plain: what to tell the medics; no two sentences in a row start with "And"'),
    'a5-ss8': ('payoff: the remedy first in each sentence (niacin unsafe, DMSO seems to help, the other one magnesium); join: '
               'though, Then, also, the other one; plain: how to start DMSO and why slowly'),
    'a5-ss5': ('payoff: what to have them do instead; join: "But" and "instead"; plain: the tapping said before its name'),
}
P = {
    'a5-ss2': ('bad-trips serotonin step 2 with his dose lines (h69)', 'Human', 0.7, [], ['And tell medics how much you gave.'],
               'step 2 as the guide has it with his two dose sentences from his QUIZ-2 answer of 2026-11-23 ("If you can get it, the guidelines say to give an adult 12mg to start ... And tell medics how much you gave."), "the guidelines" linked to the Maryland Poison Center sheet'),
    'a5-ss5': ('bad-trips serotonin step 5 with his tapping (h69)', 'Human', 0.65,
               ['(the Emotional Freedom Technique)'], ['"burn it off,"'], None),
    'a5-ss6': ('bad-trips serotonin step 6 from his round-50 notes (h69)', 'Human', 0.55,
               ['since their potassium could be running low or high: MDMA can drain it'], ['salty potato broth'], None),
    'a5-ss7': ('bad-trips serotonin step 7 with his seizure line (h69)', 'Human', 0.7, [],
               ['If they have a seizure while you wait for an ambulance'], None),
    'a5-ss8': ('bad-trips serotonin step 8 with his DMSO answer (h69)', 'Human', 0.5,
               ['seizures have happened when a lot of DMSO went straight into the blood with stem cell infusions'],
               ['mixed with about 30% water if it makes the skin itch'], None),
    'a5-call': ('bad-trips Call Medics For with "No sleep for days" (h69)', 'Human', 0.6, [], ['No sleep for days'],
                'the Call Medics For list as the guide has it, with "No sleep for days" for "Severe insomnia", the wording he approved on round 50 (ADVICE-CALL: "agree with all")'),
    'a5-harm': ('bad-trips If Someone Might Get Hurt with "acting on a delusion" (h69)', 'Human', 0.75, [], ['fall off a cliff, etc.'],
                'his If Someone Might Get Hurt paragraph as the guide has it, with "acting on a delusion" for "acting delusional", the wording he approved on round 50 (ADVICE-CALL: "agree with all")'),
    'a5-ozone': ('bad-trips Shungite, Holy Water, the crying baby paragraph (h69)', 'Human', 0.75, [], ['calm a crying baby'],
                 'his paragraph as the guide has it, with "No ozone gas was present, only the water." for the repeat, the cut he approved on round 50 (REPEATS: "yes agree")'),
}

# second tries (batch h69b): each after the first try's window read AI or Mixed (pangram_ledger.py explain, 2026-11-23)
DIAG = {
    'a6-ss5': ('a5-ss5 read Mixed: my tapping sentence put two asides in brackets in one sentence and named the technique '
               'after a made-up description ("tap their fingertips on their head instead (the Emotional Freedom '
               'Technique)"); this try keeps his form from his round-50 answer ("do some tapping (the Emotional Freedom '
               'Technique, fingers tapping the head)")'),
    'a6-ss7b': ('a5-ss7 read AI: the seizure lines did not follow the step ("while you wait for an ambulance" right after '
                '"before the ambulance comes"), "do" broke his "I\'d", and "Then I\'d tell the medics" added a step he '
                'never had; this try ties the seizure to the ambulance already coming and keeps his breathing line from '
                'round 49 in the same sentence'),
    'a6-ss7c': ('a5-ss7 read AI (as for a6-ss7b); this try is the same fix with the breathing line as its own sentence, '
                'to see whether the one long sentence or the two read better'),
    'a6-ss8': ('a5-ss8 read Mixed with the DMSO lines in the AI window: two sentences for DMSO, a dose aside, and a stem '
               'cell reason he never asked for; this try puts DMSO in one sentence in his order (reason, when, how, then '
               'more slowly), drops the stem cell reason, and puts back his fragment for the skin with his Epsom salt answer'),
}
DIAG['a7-ss8'] = ('a6-ss8 read Human with one Low window (32 words) on "If they\'re fully alert and able to swallow, I\'d give it by '
                  'mouth, especially with MDMA-related jaw tension or muscle activity": the reader asks why especially '
                  'those and the sentence never says; this try says why where the doubt comes up (those can be signs '
                  'they\'re running low, as his MDMA: Magnesium Alarm treats jaw tension), every other sentence unchanged')
DIAG['a8-ss8'] = ('a7-ss8 read Human (High, Medium, High) but lost "MDMA-related", a term his post had in this sentence '
                  '("especially with MDMA-related jaw tension or muscle activity") and the fidelity keys hold, and it widened '
                  'his claim beyond MDMA; this try puts his words back with "twitching" for "muscle activity" and keeps '
                  'the reason, every other sentence unchanged')
BIG = {
    'a6-ss7b': ('the change is the two sentences of mine that broke sense (the wait said twice, a telling-the-medics step he '
                'never had); his two sentences stay word for word; they are half the step, so replacing only them is 54%'),
    'a6-ss7c': ('as a6-ss7b: only my two seizure sentences change, his two stay word for word; this try differs from '
                'a6-ss7b by splitting the breathing line into its own sentence'),
}
FIRST.update({
    'a8-ss8': ('payoff: give it by mouth first; join: "especially with" then "since"; plain: his post\'s words, '
               '"twitching" for "muscle activity", and why they matter'),
    'a7-ss8': ('payoff: give it by mouth first; join: "especially if" then "since"; plain: the jaw and the muscles '
               'said as things to see, and why they matter'),
    'a6-ss5': FIRST['a5-ss5'] + '; now his own form of the aside',
    'a6-ss7b': ('payoff: the seizure first aid while they wait; join: "And if" at the start, tied to the ambulance; plain: '
                'his breathing line says why to watch the breathing'),
    'a6-ss7c': ('payoff: the seizure first aid while they wait; join: "before the ambulance" in the first five words, '
                '"And" for the breathing; plain: his breathing line as its own sentence'),
    'a6-ss8': ('payoff: the remedy first in each sentence; join: though, also, the other one; plain: DMSO in his order, '
               'his fragment for the skin'),
})
P.update({
    'a8-ss8': ('bad-trips serotonin step 8 with his DMSO answer (h69)', 'Human', 0.6, ['MDMA-related jaw tension or twitching'],
               ["since those can be signs they're running low"], None),
    'a7-ss8': ('bad-trips serotonin step 8 with his DMSO answer (h69)', 'Human', 0.65, ["Magnesium chloride is the other one I'd use"],
               ["especially if their jaw is tense or their muscles twitch"], None),
    'a6-ss5': ('bad-trips serotonin step 5 with his tapping (h69)', 'Human', 0.65, ['which can soothe that urge'],
               ['(the Emotional Freedom Technique, fingers tapping the head)'], None),
    'a6-ss7b': ('bad-trips serotonin step 7 with his seizure line (h69)', 'Human', 0.6, [],
                ["keep track of how their breathing is doing afterward"], None),
    'a6-ss7c': ('bad-trips serotonin step 7 with his seizure line (h69)', 'Human', 0.55,
                ['If a seizure comes before the ambulance does'], ["And I'd keep track"], None),
    'a6-ss8': ('bad-trips serotonin step 8 with his DMSO answer (h69)', 'Human', 0.5,
               ['made at home it has almost none of the harmala alkaloids'],
               ["Topical magnesium chloride if they're not able to swallow"], None),
})


def run(key):
    lin, call, chance, tells, human, unch = P[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lin, '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', call, '--chance', str(chance),
         '--detector', DET, '--decides', ('whether %s reads Human High by itself; if not, the window says where to read '
                                         'it again for sense' % key)]
    if unch:
        a += ['--unchanged', unch]
    else:
        a += ['--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', HUM, '--first-fix', FIRST[key]]
        if key in DIAG:
            a += ['--diagnosis', DIAG[key]]
        if key in BIG:
            a += ['--big-change', BIG[key]]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:900] if r.returncode else out.splitlines()[-1][:160])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(run(k) for k in (sys.argv[1:] or list(P))))
