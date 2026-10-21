"""The recheck's predictions (2026-10-21), written to the lane ledger before the Substack checks: part A (the whole guide;
Substack's check reads its first 99,999 characters) as HG-whole's try 2, part B (Appendices to the end) as HG-rest-B's
try 2. Both lineages read Mixed at try 1, so each prediction carries the diagnosis (what changed since) the ledger asks for.
The first version of this recheck (keys HG-whole-41r-a and HG-rest-41r-b, 01:04 UTC) was never read and was voided after
Joel's answers of 17:56 UTC changed the guide; this is its rebuild, with batch 469g in it.

  python3 articles/inner-signal/humanize/fix-20261020/substack41r/make_preds_recheck.py   (from the repo root)
"""
import pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
X = pathlib.Path(__file__).resolve().parent
LEDGER = REPO / 'articles' / 'inner-signal' / 'humanize' / 'pangram-ledger.jsonl'
CHANGED = ('since try 1 (2026-10-20): the 4.1 edits of 467g and 468g (HG12, HG15, Appendices D and F) and Joel\'s own edit '
           'of HG15 (his check, Human); the NLP appendix (HG31) and the return steps (HG18) as their Human versions (his '
           'answers 3 a and 4 d; 4.0 checks, never read in 4.1); and batch 469g, read here for the first time (gate E200): '
           'Appendix C\'s general checklist as prose, the return steps\' lost points put back, and the inner-adult sweep\'s '
           'five fixes (fix-20261021/b469/batch/PREDICTIONS.md has each changed paragraph\'s forecast)')
PREDS = [
    dict(lineage='HG-whole', scope='article', key='HG-whole-41r2-a', text=X / 'WHOLE-GUIDE-41r-A.txt', call='AI', chance=0.02,
         tells='the listening script as published (question 4) read red at try 1 and is unchanged; the NLP appendix\'s and '
               'the return steps\' Human versions were checked only in 4.0; Appendix C\'s prose had no break in its march read; '
               'HG15\'s closing pair is Joel\'s own wording now',
         human='Joel\'s HG15 edit read Human in his own check; every other installed section read dark green at try 1; the '
               'inner-adult fixes change a few words each in paragraphs that read Human, high',
         shading='red: the listening script and its bridge (HG16-HG17), as at try 1; some of the NLP appendix (4.0 only) and '
                 'of the return count (five numbered steps); light green or red: Appendix C\'s prose, if part A reaches it; '
                 'dark green: HG12, HG15 with Joel\'s edit, the five inner-adult fixes, the rest',
         decides='whether the installed Human versions hold in 4.1 (the NLP appendix, the return steps, Joel\'s edit), which '
                 'of batch 469g\'s paragraphs need a try on pangram.com, and what goes to Joel'),
    dict(lineage='HG-rest-B', scope='stretch', key='HG-rest-41r2-b', text=X / 'WHOLE-GUIDE-41r-B.txt', call='AI', chance=0.05,
         tells='Appendix C\'s prose had no break in its march read and keeps a run of signs and a good/bad guide contrast; '
               'its audit list of seven questions stays as published (question 2, c); the NLP appendix\'s Human version '
               'was checked only in 4.0',
         human='Appendices D and F fixed and Human alone; Appendix G\'s and H\'s inner-adult fixes change a few words in '
               'paragraphs that read Human, high; the NLP appendix read 100% Human whole and in every paragraph in 4.0',
         shading='red: Appendix C\'s audit list and some of its prose (the signs, the tests, the good and bad guide); maybe '
                 'part of the NLP appendix; light green: Appendix F\'s quoted promise; dark green: Appendices D to K, '
                 'the fixes included',
         decides='whether Appendix C\'s prose and the NLP appendix\'s Human version read Human in 4.1, which paragraphs need '
                 'a try, and what goes to Joel'),
]


def main():
    for p in PREDS:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                            '--lineage', p['lineage'], '--scope', p['scope'], '--text', str(p['text']), '--key', p['key'],
                            '--batch', 's41r2', '--call', p['call'], '--chance', str(p['chance']), '--tells', p['tells'],
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
