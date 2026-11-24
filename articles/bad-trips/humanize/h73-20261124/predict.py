#!/usr/bin/env python3
"""predict.py - turn 65's predictions, written before the checks: five paragraphs of MDMA: Magnesium Alarm (B114, B115,
B117, B118, B120), his post's, which last read AI in the section's check of 2026-11-11 (08beb99e), through the API with his
key on his laptop."""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h73-20261124/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
_A = sys.argv[1:]
BATCH = 'h73b' if any(a.startswith('a3-') for a in _A) else 'h73a'
HUM = ('his post\'s paragraph said again with every dose, event and warning word for word (facts.py, the R50 keys); one '
       'round of the three fresh reads on version one of the whole section (reads/*-a1-sec.txt), their marks answered in '
       'version two: the limit said plainly before the finding, each "it" named, one point a sentence, the payoff first')
P = {
    'b114': ('the jaw alarm (B114)', 0.55, ['Nobody has tested this in a trial that I know of'], ['meaningful jaw tension'],
             'payoff: the alarm first, as his post had it; join: "Nobody has tested this"; plain: "what I\'ve seen again and again"'),
    'b115': ('his amounts (B115)', 0.55, ['less likely to cause diarrhea than several other kinds of magnesium'], ['I can take around twenty grams without diarrhea'],
             'payoff: a token dose may not be enough, then his amounts; join: "More than once", "also"; plain: "by mouth", "the ones people take on purpose as laxatives"'),
    'b117': ('the softer peak (B117)', 0.6, ['the risk of the night turning into an emergency'], ["I'll take slightly less euphoria for a relaxed jaw"],
             'payoff: the trade, with the theory the needed read found no use for cut; join: "also", ", but"; plain: "the night turning into an emergency"'),
    'b118': ('his second wife (B118)', 0.6, ['a broader electrolyte emergency, potassium included'], ['What happened to my second wife is why I look past magnesium'],
             'payoff: why the story is here, before the story; join: "What happened to my second wife", "So"; plain: "they found her potassium critically low"'),
    'b117p': ('the softer peak (B117)', 0.6, ['the risk of the night turning into an emergency'], ["I'll take slightly less euphoria for a relaxed jaw"],
              'payoff: the trade, with the theory the needed read found no use for cut; checked with B118 after it, since it is 41 words; join: "also", ", but"; plain: "the night turning into an emergency"'),
    'b120': ('the kidneys (B120)', 0.55, ['dangerous electrolyte shifts'], ['call medics sooner than I would for someone with healthy kidneys'],
             'payoff: whose case it is, first; join: "The MDMA is a far bigger danger", "So", "With serious kidney impairment"; plain: "skip the drug altogether", "call medics sooner"'),
}


DIAG = {
    'b114': ('try 1 read AI (9e4a7d71): Low 17 on the alarm sentence, High 52 on the evidence sentence, a long balanced '
             'claim joined by a colon, with a cliche ("again and again") and a mirror ("everyone I know who ... in people '
             'who ...", way 2). The ledger refused a rewrite (69%, gate E361), so try 2 changes only that sentence: split '
             'at the colon, "myself" for the cliche, and "the other complications that showed up when people let the '
             'tension keep going" for the mirror'),
    'b115': ('try 1 read Human High 43 / Medium 41 (eb47893c): the Medium window was "I can take around twenty grams '
             'without diarrhea, which for me only starts above about forty grams" and the review sentence; "which" could '
             'attach to the twenty grams. Try 2 changes only that: "and I only get it above about forty grams" (7% of the '
             'words, lesson bad-trips-2026-11-19b)'),
    'b117p': ('try 1 read AI High 78 over B117 and the start of B118 (b6991899): B117\'s trade said as a balanced, '
              'wise-sounding line ("but I\'ll take slightly less euphoria for a relaxed jaw, since ... the risk of the night '
              'turning into an emergency is much lower then", way 6). The ledger refused a rewrite (71%), so try 2 changes '
              'that clause only ("but I don\'t mind a little less euphoria, since ... a relaxed jaw comes with a much lower '
              'risk"), and B118\'s half as in its own try 2'),
    'b118': ('try 1 read AI High 36 / Medium 9 / High 28 (6840df55): an announcing opener ("What happened to my second '
             'wife is why I look past magnesium:") and a short line standing alone ("IV potassium was the only treatment '
             'they gave her.", way 18). The ledger refused a rewrite (54%), so try 2 changes only those: the story opens on '
             'itself ("My second wife had severe convulsions ...") and the short line is joined to it with "and"; the '
             'conclusion sentence (AI High 28) waits for the next try'),
    'b120': ('try 1 read Mixed (258a5b17), with a Human window (Low 36) on the first sentence, so the next try changes '
             'one thing a reader could take two ways (lesson bad-trips-2026-11-19b): "once someone with it has taken some", '
             'where "it" could be the kidney trouble or the drug, is "if they\'ve already taken it"'),
}


def run(key):
    b = key.split('-')[1]
    what, chance, tells, human, first = P[b]
    lin = 'bad-trips MDMA: Magnesium Alarm, %s (h73)' % what
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lin, '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', 'Human', '--chance', str(chance),
         '--detector', DET, '--decides', 'whether %s reads Human High in every window by itself before it goes in' % key,
         '--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', HUM, '--first-fix', first]
    if key.startswith('a3-'):
        a += ['--diagnosis', DIAG[b]]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1200] if r.returncode else out.splitlines()[-1][:150])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(run(k) for k in _A))
