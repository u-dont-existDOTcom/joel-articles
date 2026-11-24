#!/usr/bin/env python3
"""predict.py - turn 62's predictions, written before the checks: steps 6 and 8 and his MDMA paragraph from his round-51
answers (2026-11-23 23:35 UTC), through the API with his key on his laptop."""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h70-20261123/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
_A = sys.argv[1:]
BATCH = 'h70b' if any(a.startswith('a3-') for a in _A) else 'h70a'
HUM = ('written from his round-51 answers; one round of the three fresh reads on version one, their marks answered in '
       'version two (reads/*-a1-ss.txt, reads/*-a1-mdma.txt): what to do first, then what not to do, the doubt answered '
       'where it comes up, each "it" named, one point a sentence')
FIRST = {
    'a2-ss6': ('payoff: what to give first (chips for salt and potassium, magnesium on the skin); join: each sentence tied '
               'at its start (Salty, That\'s, Their potassium, High potassium also, Magnesium also, If you don\'t have); '
               'plain: "rub the mix on their skin", "Epsom salt, which is magnesium sulfate"'),
    'a2-ss8': ('payoff: what to use first (DMSO), then what to leave out (niacin), then the last resort (the oil); join: '
               '"Since a seizure", "also", "The other remedy", "The oil"; plain: the oil set apart from the brew in step 1'),
    'a2-mdma': ('payoff: his sentences stay; mine say what to do (no dancing), why plain water lowers sodium, how much salt; '
                'join: "While it\'s natural", "Plain water is the risk because", "That has to be"; plain: "hold on to '
                'water", "thins out the salt"'),
}
P = {
    'a2-ss6': ('bad-trips serotonin step 6 from his round-51 notes (h70)', 'Human', 0.55,
               ['Magnesium also runs low in many people'], ['Salty potato chips give the salt and the potassium']),
    'a2-ss8': ('bad-trips serotonin step 8 from his round-51 answers (h70)', 'Human', 0.55,
               ['going by people\'s reports rather than studies'], ['The other remedy I\'d keep for a last resort']),
    'a2-mdma': ('bad-trips MDMA: Magnesium Alarm from his round-51 answer (h70)', 'Human', 0.6,
                ['Plain water is the risk because'], ['That has to be a lot of salt, more than a snack gives']),
}


def run(key):
    lin, call, chance, tells, human = P[key]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lin, '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', call, '--chance', str(chance),
         '--detector', DET, '--decides', 'whether %s reads Human High by itself before it goes in' % key,
         '--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', HUM, '--first-fix', FIRST[key]]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:900] if r.returncode else out.splitlines()[-1][:160])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(run(k) for k in (_A or list(P))))
