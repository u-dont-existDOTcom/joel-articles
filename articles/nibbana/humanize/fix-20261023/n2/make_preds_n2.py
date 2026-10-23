"""Nibbāna batch n2's predictions, written before its API round (2026-10-23, after Joel's message of 12:30 UTC): one
ledger line per text of TEXTS.json, each text written to texts/NAME.txt first (the ledger hashes that file).

Batch n2 is the rebirth sentence only. My fix of batch n1 read Human alone (n1_rebirth, the sentence's window Human, Low)
and AI, High, in place in the recheck (https://www.pangram.com/feed/6a726359-1fce-4ec3-8a06-e957032fc91e, window 120).
Each candidate is the paragraph as installed with only that sentence replaced; his own lines ("But who's going around
getting reborn ...", "More like a driverless car.", the Milindapañha) stay. "chance" is my chance of a 100% Human result.

  python3 articles/nibbana/humanize/fix-20261023/n2/make_preds_n2.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

N = pathlib.Path(__file__).resolve().parent
H = N.parents[1]
REPO = H.parents[2]
LEDGER = H / 'pangram-ledger.jsonl'
DET = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
DECIDES = ('which version of the sentence goes into the next whole-article recheck: the one whose own window reads Human '
           'with the highest confidence; a Human, Low window on it is a warning, since try 1\'s sentence read Human, Low, '
           'alone and AI, High, in place')
DIAG = ('Try 1 (n1_rebirth, mine) read Human alone, its sentence\'s window Human, Low, but AI, High, as a 26-word window '
        'of its own in the whole article: still the doctrine\'s chain in one compressed sentence with a colon '
        '("..., often called a mind-stream: craving and clinging condition becoming, and becoming becomes birth"). Joel, '
        '12:30 UTC: "for the other parts you can either learn from me or learn from emulate". bj and bk are Emulate\'s '
        'versions of the sentence (three samples of the published paragraph, emu-hg-bi, bj, bk; bi\'s "the result of the '
        'causal process whereby" left out as the most formal); mine uncompresses it the way his N2 rewrites did, and '
        'ends on "nobody riding along" so that his "More like a driverless car." follows it. Better: Human, with the '
        'sentence\'s window Human at Medium or High.')
# name: (call, chance, tells, human tells)
P = {
    'n2_rebirth_bj': ('Human', 0.6, ['a colon definition ("Rather, rebirth is seen as a causal process: ...")',
                                     'a "there is ..., but there is not ..." contrast',
                                     'the chain still as "X lead to Y, and Y leads to Z"'],
                      ['scare quotes on “thing”', '"that\'s moving from one life to the next"', 'plain words, no "condition"',
                       'his own lines around it']),
    'n2_rebirth_bk': ('Human', 0.55, ['"the causal continuation of one life into the next"', '"sometimes referred to as"',
                                      '"In brief," as a signpost before the chain'],
                      ['two short sentences instead of one with a colon', '"which leads to birth"', 'his own lines around it']),
    'n2_rebirth_mine': ('Human', 0.6, ['the chain is still there ("Craving and clinging keep “becoming” going")'],
                        ['"keep “becoming” going"', 'the name as a bracketed aside "(some call it a mind-stream)"',
                         '"with nobody riding along inside it" right before his "More like a driverless car."']),
}


def main():
    texts = json.loads((N / 'TEXTS.json').read_text(encoding='utf-8'))
    (N / 'texts').mkdir(exist_ok=True)
    for name in sys.argv[1:] or list(P):
        call, chance, tells, human = P[name]
        f = N / 'texts' / (name + '.txt')
        f.write_text(texts[name], encoding='utf-8')
        argv = [sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                '--lineage', 'NB-P228', '--scope', 'paragraph', '--text', str(f), '--call', call, '--chance', str(chance),
                '--key', name, '--batch', 'n2', '--detector', DET, '--decides', DECIDES, '--diagnosis', DIAG]
        for t in tells:
            argv += ['--tells', t]
        for t in human:
            argv += ['--human-tells', t]
        r = subprocess.run(argv, capture_output=True, text=True, cwd=REPO)
        print(name, (r.stdout + r.stderr).strip()[-200:])
        if r.returncode:
            sys.exit(1)


if __name__ == '__main__':
    main()
