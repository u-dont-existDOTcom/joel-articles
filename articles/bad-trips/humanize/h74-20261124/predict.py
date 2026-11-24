#!/usr/bin/env python3
"""predict.py - turn 66's predictions for my texts, written before the checks, through the API with his key on his
laptop: B115 with why magnesium chloride (his round-55 question), and B117 and B120 from his post's text with the ways of
his round-55 fixes (a causally different method from my rewrites of turn 65, which read AI twice each)."""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h74-20261124/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
_A = sys.argv[1:]
BATCH = 'h74g' if any(a.startswith('a7-') for a in _A) else 'h74f' if any(a.startswith('a6-') for a in _A) else 'h74e' if any(a.startswith('a5-') for a in _A) else 'h74d' if any(a.startswith('a4-') for a in _A) else ('h74c' if any(a.startswith('a3-') for a in _A) else 'h74b')
HUM = ('one round of the three fresh reads on version one of the whole section with his round-55 versions in it '
       '(reads/*-a1-sec.txt), their marks answered in version two: each "it" named, the absorption said as the source shows '
       'it and his experience as his, the don\'t after the do, the term explained where it is first used')
P = {
    'b115': ('bad-trips MDMA: Magnesium Alarm, his amounts with why magnesium chloride (h74)', 0.6,
             ["it's absorbed far better than magnesium oxide"], ['Around twenty grams is fine for my gut'],
             'payoff: why this kind, right after the flakes; join: "I use magnesium chloride because"; plain: "start helping within a minute"',
             None),
    'b117': ('bad-trips MDMA: Magnesium Alarm, the softer peak from his post\'s text with his round-55 ways (h74)', 0.5,
             ["calms some of the MDMA's stimulation"], ["I'm fine trading a little euphoria for a relaxed jaw"],
             'payoff: what magnesium does to the high, then the trade; join: "which makes me think", "I\'m fine trading"; plain: "the jaw relaxing comes with"',
             ('my two rewrites of turn 65 read AI (b6991899, a74bc7a7); this starts again from his post\'s text with the ways of '
              'his round-55 fixes, which took his two paragraphs of this section to Human High: the opener tic out ("Interestingly"), '
              'the label named ("the state escalating" as "the MDMA toxicity symptoms", his own words in B114), the finished '
              'principle said as his choice ("I\'m fine trading"), each pointer named')),
    'b120': ('bad-trips MDMA: Magnesium Alarm, the kidneys from his post\'s text with his round-55 ways (h74)', 0.5,
             ['But the MDMA is a far bigger danger to their kidneys'], ['their worsening jaw tension still needs treating'],
             'payoff: whose case it is, first; join: "But", "So", "With serious kidney impairment, though"; plain: "muscle breaking down into the blood"',
             ('my two rewrites of turn 65 read Mixed then AI (258a5b17, 230891b4); this starts again from his post\'s text with '
              'the ways of his round-55 fixes: the dash aside ("--not a reason to sit there with worsening jaw tension") said as '
              'its own clause, the contrast softened where one thing follows from the other ("So ... and if they\'ve taken it '
              'anyway"), the do before the don\'t, the term explained')),
}


DIAG3 = {
    'b115': ('try 1 read AI Assisted (59518a51): Human High 43, then AI-Assisted Low 24 on my new sentence ("I use magnesium '
             'chloride because it\'s absorbed far better than magnesium oxide, and I can usually see it start helping within a '
             'minute"), and the two lines after it flipped with it. The try had a Human window, so this one changes only that '
             'sentence (lesson bad-trips-2026-11-19b): his own words for it from his comment ("so you can see how it\'s '
             'helping usually within a minute"), the passive "it\'s absorbed" made active'),
    'b117': ('try 1 read Human High 37 / Low 29 (cc038ec8): the Low window is the trade, "I\'m fine trading a little '
             'euphoria for a relaxed jaw, since in my experience the jaw relaxing comes with ..." - a trade formula and a '
             'pointer ("the jaw relaxing comes with") a reader could take as the trade or the jaw. This changes only that: "I '
             'don\'t mind a little less euphoria, since in my experience a relaxed jaw means a much lower risk ..."'),
}


def run(key):
    b = key.split('-')[1]
    lin, chance, tells, human, first, diag = P[b]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lin, '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', 'Human', '--chance', str(chance),
         '--detector', DET, '--decides', 'whether %s reads Human High in every window by itself before it goes in' % key,
         '--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', HUM, '--first-fix', first]
    if key.startswith('a3-'):
        diag = DIAG3[b]
    if key.startswith('a7-'):
        diag = ('try 5 read Human High 61 / Medium 24 / High 24 (93247bd7), the best so far, with my sentence High at the end: the '
                'Medium window is the diarrhea line, which opens on its own subject ("Magnesium chloride is also less likely ...") '
                'right after his line about his own diarrhea, with nothing tying the two (way 12, his round-55 fix of connecting '
                'a sentence to the one before). This changes only its opening: "And magnesium chloride is"')
    if key.startswith('a6-'):
        diag = ('try 4 read Human High 61 / Medium 24 / Low 23 (873cac55): the two reasons for this kind sat side by side, built '
                'alike ("because it absorbs far better than magnesium oxide" / "also less likely to cause diarrhea than several '
                'other kinds", way 2), and the second stayed Low. This try moves the diarrhea line back after his tolerance line, '
                'where it read High last turn (8afe7ed1), and my sentence to the end as the main reason ("I use it mostly '
                'because"); the move is free and the words change by three')
    if key.startswith('a5-'):
        diag = ('try 3 read Human High 61 / Medium 24 / Low 24 (613b2a95): the move took the tolerance line to High; the Low window '
                'is the line after my sentence, which opens on "Magnesium chloride" right after "I use magnesium chloride because", '
                'the same name twice in a row (lint O76\'s kind). This changes only those two words to "It\'s"')
    if key.startswith('a4-'):
        diag = ('try 2 read Human High 43 / Medium 24 / Low 18 / Low 24 (41ec7d55): my sentence in his words lifted its window to '
                'Medium, but the two lines after it stayed Low, each now following a sentence about why this kind instead of the '
                'dose it qualifies. This try only moves my sentence after his tolerance line, so the method runs into his own '
                'limit and the two reasons for this kind sit together ("... within a minute. Magnesium chloride is also ..."); '
                'a move changes no words (gate E361)')
    if diag:
        a += ['--diagnosis', diag]
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
