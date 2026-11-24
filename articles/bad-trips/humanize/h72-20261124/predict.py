#!/usr/bin/env python3
"""predict.py - turn 64's predictions, written before the checks: the dance paragraph with his MAPS-SETTING answer, and
steps 6 and 8 with their Medium windows said another way, through the API with his key on his laptop."""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h72-20261124/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
_A = sys.argv[1:]
BATCH = 'h72b' if any(a.startswith('a3-') for a in _A) else 'h72a'
HUM = ('one round of the three fresh reads on version one, their marks answered in version two (reads/*-a1-dance.txt, '
       'reads/*-a1-ss6.txt, reads/*-a1-ss8.txt): only the sentences this turn is for changed, since each text\'s other '
       'windows read High last turn (lesson bad-trips-2026-11-19b); the act first, each "it" and "those" named, the term '
       'explained where it is first used')
FIRST = {
    'a3-ss8': ('payoff: why the oil comes last, said before what the brew does; join: "The reason I\'d keep it that '
               'late", "What makes the brew"; plain: "MAO (the enzyme that clears serotonin)"'),
    'a2-dance': ('payoff: his answer that the setting isn\'t what decides, where it is the evidence for the suspicion '
                 'after it; join: "And in the same exact setting"; plain: "the pills have gone both ways on me"'),
    'a2-ss6': ('payoff: stop the chips, said before the reason; join: "So if they start vomiting"; plain: "too much '
               'potassium brings those on", the draining clause out'),
    'a2-ss8': ('payoff: what to leave out, said first ("What I\'d leave out is niacin"), and why the oil comes last '
               'before what the brew does; join: "What I\'d leave out", "The reason I\'d keep it that late", "What makes '
               'the brew"; plain: "at that dose", "MAO (the enzyme that clears serotonin)"'),
}
P = {
    'a2-dance': ('bad-trips MDMA: the dance paragraph from his round-52 answers (h71)', 'Human', 0.6,
                 ['the pills have gone both ways on me'], ['And in the same exact setting', 'couch lock'],
                 ('h71\'s try 2 read Human High in one window (73794d7e): this adds one sentence, his MAPS-SETTING '
                  'answer, and changes nothing else, so the next try starts from that one (lesson '
                  'bad-trips-2026-11-19b). The sentence is his own observation, said with "pill" where his answer said '
                  '"different mdma", since "MDMA" would have stood in three sentences in a row (lint O76)')),
    'a2-ss6': ('bad-trips serotonin step 6 from his round-51 notes (h70)', 'Human', 0.55,
               ['the chips have to stop either way while they\'re being sick'], ['Salty potato chips give the salt and the potassium'],
               ('h70 read Human High 125 / Medium 22 / High 106 (90be4010): the Medium window was one sentence, "High '
                'potassium also brings on vomiting and diarrhea, which then drain it again, so if those start, I\'d stop '
                'the chips" - the act last, "those" and "it" each pointing two ways, and a clause (the draining) that '
                'argues against the act, which all three fresh reads stumbled on. It now says the act first, and the '
                'draining clause is out; nothing else in the step changes')),
    'a2-ss8': ('bad-trips serotonin step 8 from his round-51 answers (h70)', 'Human', 0.55,
               ['at that dose'], ["What I'd leave out is"],
               ('h70 read Human High 73 / Medium 39 / High 33 / Medium 31 (3ea237f3): the two Medium windows were the '
                'niacin sentence (the don\'t after "You might also think of", "the doses used to end a trip" twice) and '
                'the last sentence ("The oil isn\'t the brew", a negation with "for that reason" pointing back and the '
                'missing study hung on the end). The niacin line now says what to leave out first, with his "unsafe with '
                'serotonin syndrome" kept. This try changes that sentence alone and nothing else: the ledger refused both '
                'Medium windows in one try (43% of the words), and his rule is one fix at a time, each checked (lesson '
                'bad-trips-2026-11-19b)')),
    'a3-ss8': ('bad-trips serotonin step 8 from his round-51 answers (h70)', 'Human', 0.55,
               ['MAO (the enzyme that clears serotonin)'], ['nobody has given the oil with MDMA in a study'],
               ('the second Medium window alone, after the niacin line\'s check: "The oil isn\'t the brew" was a negation '
                'with "for that reason" pointing back and the missing study hung on the end. His main reason for holding '
                'the oil back (nobody has given it with MDMA in a study) now comes first, then what the brew does, with '
                'MAO explained where the step first uses it')),
}


def run(key):
    lin, call, chance, tells, human, diag = P[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lin, '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', call, '--chance', str(chance),
         '--detector', DET, '--decides', 'whether %s reads Human High in every window by itself before it goes in' % key,
         '--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', HUM, '--first-fix', FIRST[key]]
    if diag:
        a += ['--diagnosis', diag]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1200] if r.returncode else out.splitlines()[-1][:160])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(run(k) for k in (_A or list(P))))
