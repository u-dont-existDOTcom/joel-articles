"""The recheck's predictions (2026-10-21), written to the lane ledger before the Substack checks: part A (the whole guide;
Substack's check reads its first 99,999 characters) as HG-whole's try 2, part B (Appendices to the end) as HG-rest-B's
try 2. Both lineages read Mixed at try 1, so each prediction carries the diagnosis (what changed since) the ledger asks for.

  python3 articles/inner-signal/humanize/fix-20261020/substack41r/make_preds_recheck.py   (from the repo root)
"""
import pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
X = pathlib.Path(__file__).resolve().parent
LEDGER = REPO / 'articles' / 'inner-signal' / 'humanize' / 'pangram-ledger.jsonl'
CHANGED = ('since try 1 (2026-10-20), six 4.1 edits are installed (../EDITS41.json): HG12\'s restating closer cut and its '
           'story\'s closer said plainly, HG15\'s "inherited parent", Appendix D\'s breathing steps, Appendix F\'s '
           'forgiveness list said about the people and its self-forgiveness lines; each read Human alone on pangram.com '
           '(467g, 468g), HG12 and Appendix D Human whole')
PREDS = [
    dict(lineage='HG-whole', scope='article', key='HG-whole-41r-a', text=X / 'WHOLE-GUIDE-41r-A.txt', call='AI', chance=0.01,
         tells='the four sections as published (questions 2 to 4: the two scripts, Appendix B, Appendix C) read red at try 1 '
               'and are unchanged; HG15\'s "Those can all be real gifts. They become a bargain for belonging ..." is as '
               'installed (red, low, at try 1; both fixes read red alone)',
         human='HG12\'s two red sentences fixed and its section Human whole; every other installed section read dark green at '
               'try 1',
         shading='red: HG17 and HG18 as published, HG31 from its start, the HG16-HG17 bridge, HG15\'s closer (low); light '
                 'green: a few in HG12, HG16\'s question list; HG12\'s fixed sentences dark or light green; every other '
                 'installed section dark green',
         decides='whether the 4.1 fixes hold in the whole guide, and what goes to Joel'),
    dict(lineage='HG-rest-B', scope='stretch', key='HG-rest-41r-b', text=X / 'WHOLE-GUIDE-41r-B.txt', call='AI', chance=0.01,
         tells='Appendices B and C as published (questions 2 and 3) read red at try 1 and are unchanged; Appendix F\'s quoted '
               'promise is as installed (light green at try 1, AI low in its section check and with its neighbor)',
         human='Appendix D\'s instruction and Appendix F\'s forgiveness and self-forgiveness lines fixed, each Human high alone; '
               'every other installed appendix read dark green at try 1',
         shading='red: Appendices B and C as published; Appendix F\'s quoted promise light green or red (low); Appendix D\'s '
                 'breathing steps and Appendix F\'s fixed lines dark green; the rest dark green',
         decides='whether the appendices\' 4.1 fixes hold in context, and what goes to Joel'),
]


def main():
    for p in PREDS:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                            '--lineage', p['lineage'], '--scope', p['scope'], '--text', str(p['text']), '--key', p['key'],
                            '--batch', 's41r', '--call', p['call'], '--chance', str(p['chance']), '--tells', p['tells'],
                            '--human-tells', p['human'], '--diagnosis', CHANGED, '--decides', p['decides'],
                            '--shading-expected', p['shading'],
                            '--detector', "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"],
                           capture_output=True, text=True, cwd=REPO)
        print(p['key'], (r.stdout or r.stderr).strip()[-300:])
        if r.returncode:
            return r.returncode
    return 0


if __name__ == '__main__':
    sys.exit(main())
