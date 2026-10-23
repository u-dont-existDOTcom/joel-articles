"""The hypnosis guide's batch 473 predictions, written before its API round (2026-10-23, after Joel's message of 12:30
UTC): one ledger line per text of TEXTS.json, each text written to texts/NAME.txt first (the ledger hashes that file).

Batch 473 is question 14's seam, the induction section's last paragraph (retiring the shortcut), checked alone in lineage
HG17-B306. Six versions of mine read AI, High (E227); the last two alone. Joel, 12:30 UTC: "there is another emulate
trick, you can take text emulate gives which doesn't pass, and re-run it, and then it can pass". The seam is Emulate's text
(sample bf) with my meaning fixes, so emu-seam/ re-ran the installed pair through Emulate three times (emu-hg-bi, bj, bk).
bj and bk are checked here with the two points they dropped put back first (FIXES.json): "qualified" for who to get help
from, and that saying it is gone does not end it right away. bi kept both but stays close to the input that read AI, so
it waits with the lineage's last try. "chance" is my chance of a 100% Human result.

  python3 articles/inner-signal/humanize/fix-20261023/b473/make_preds_b473.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
REPO = H.parents[2]
LEDGER = H / 'pangram-ledger.jsonl'
DET = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
DECIDES = ('whether this paragraph goes into recheck A\'s seam, with bk\'s return paragraph (the only sample that keeps '
           '"your body belongs to you"), or the lineage\'s last try goes to another re-run')
DIAG = ('Tries 4 and 5 of mine (b472_s2e_alone, b472_s2f_alone) read AI, High, alone: my rewordings in his register and '
        'without the tidy closer kept the installed text\'s shape. This is a causally different method, Joel\'s re-run '
        'trick: the installed pair (itself Emulate\'s text with my meaning fixes) run through Emulate again, so the shape '
        'and register are Emulate\'s, not mine. Only two meaning points it dropped are put back. Better: Human, or Low.')
# name: (call, chance, tells, human tells)
P = {
    'b473_seam_bj_p1': ('Human', 0.55, ['the instruction list ("take it out of your recordings, take it out of your apps ...")',
                                        '"If you want to ..., that\'s fine."', '"who\'s qualified" put back by me'],
                        ['the rough catch-all "(..., whatever)" in brackets (E208)', '"this one"', '"not practice it anymore"',
                         '"in your waking life"', '"it will be over for today"']),
    'b473_seam_bk_p1': ('AI', 0.45, ['"the best way to remove it is to simply stop rehearsing it"', '"simply" three times',
                                     'formal "will not" twice', '"immediately" and "who\'s qualified" put back by me'],
                        ['"a certain trance trigger"', '"at times you don\'t want to"', '"that is fine, but for now"',
                         'a new order (the decision first, then how)']),
}


def main():
    texts = json.loads((B / 'TEXTS.json').read_text(encoding='utf-8'))
    (B / 'texts').mkdir(exist_ok=True)
    for name in sys.argv[1:] or list(P):
        call, chance, tells, human = P[name]
        f = B / 'texts' / (name + '.txt')
        f.write_text(texts[name], encoding='utf-8')
        argv = [sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                '--lineage', 'HG17-B306', '--scope', 'paragraph', '--text', str(f), '--call', call, '--chance', str(chance),
                '--key', name, '--batch', '473', '--detector', DET, '--decides', DECIDES, '--diagnosis', DIAG,
                '--emulate-share', '0.97']
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
