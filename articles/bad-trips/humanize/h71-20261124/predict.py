#!/usr/bin/env python3
"""predict.py - turn 63's predictions, written before the checks: his MDMA paragraph (B119) with his women sentence, and
the dance paragraph after it (R52-DANCE), from his round-52 answers (2026-11-24 01:25 UTC), through the API with his key
on his laptop."""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h71-20261124/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
_A = sys.argv[1:]
BATCH = 'h71b' if any(a.startswith('a3-') for a in _A) else 'h71a'
HUM = ('written from his round-52 answers; one round of the three fresh reads on version one, their marks answered in '
       'version two (reads/*-a1-mdma.txt, reads/*-a1-dance.txt): the tie at each sentence\'s start, each "it" and "that" '
       'named, his words kept where they are his view, the field vs lab note after his suspicion of the pills')
FIRST = {
    'a3-dance': ('payoff: as a2, with the lab\'s other difference said as what happens at a festival; join: "Then again, '
                 'the lab"; plain: "a small woman takes the same pill as a big guy"'),
    'a2-mdma': ('payoff: his sentences stay; mine say why plain water lowers sodium in fewer words, and who is most at '
                'risk; join: "Plain water is the risk because", "Women are most at risk of this", "found the same '
                'pattern"; plain: "keeps them from peeing out the extra", "the salt in their blood"'),
    'a2-dance': ('payoff: the act first (no dancing on MDMA), then what he would take instead, then his view and what the '
                 'lab study shows; join: "That\'s why", "And really", "For that", "So if a pill", "That might also be '
                 'why", "The lab also"; plain: "I can barely move", "a similar drug"'),
}
P = {
    'a2-mdma': ('bad-trips MDMA: Magnesium Alarm from his round-52 answers (h71)', 'Human', 0.6,
                ['based on the results we have'], ['Women are most at risk of this'],
                ('a new lineage because his round-52 answers change what the paragraph says (his women sentence in, the '
                 'dance line out to the next paragraph), not a rewrite to pass: the ledger refused it in the h70 lineage '
                 '(#648) at 31% changed words. The h70 try read Human High 87 / Medium 32 / High 131 (c5f90479): the Medium window was my why-plain-water '
                 'sentence, an explanation added after his line with a qualifier hung on its end ("all the more after '
                 'they\'ve sweated a lot"), way 8 and way 9; it is now one plain clause with no qualifier, and the dance '
                 'line has moved to the next paragraph; his women sentence goes in after it (AGENTS.md since 2026-11-24: a '
                 'Medium window is work to do)')),
    'a2-dance': ('bad-trips MDMA: the dance paragraph from his round-52 answers (h71)', 'Human', 0.6,
                 ['That might also be why women get low sodium'], ['I NEED TO DANCE!', 'couch lock'], None),
    'a3-dance': ('bad-trips MDMA: the dance paragraph from his round-52 answers (h71)', 'Human', 0.6,
                 ['so she\'s getting a lot more for her size'], ['a small woman takes the same pill as a big guy'],
                 ('a2 read Mostly Human, High 243 / AI Low 24 (232c1e87): the AI window was only my last sentence, "The '
                  'lab also dosed everyone by their weight, though, so it couldn\'t show how much harder the same pill '
                  'hits a smaller body", a caveat hung on the end of the paragraph in abstract words (way 9, and way 18\'s '
                  'plain closing line); now it says the same thing as what happens at a festival, a small woman taking '
                  'the same pill as a big guy, and only that sentence changes')),
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
