"""This round's whole-guide recheck predictions (2026-10-23), written before each part is pasted, let alone checked.

  python3 articles/inner-signal/humanize/fix-20261023/recheck/make_preds_recheck.py B   (from the repo root, after make_recheck.py)

Each part's text is TEXT-A.txt or TEXT-B.txt (make_recheck.py: the payload's text as the check reads it), so the ledger's
SHA-256 is the checked text's. Part B holds the appendices with Joel's own Appendix C (his message of 01:10 UTC, question 13:
"13 human high conf"); part A (pasted after question 14) holds batch 472g's two edits and whatever question 14 brings.
"""
import pathlib, subprocess, sys

X = pathlib.Path(__file__).resolve().parent
REPO = X.parents[4]
LEDGER = X.parents[1] / 'pangram-ledger.jsonl'
DETECTOR = "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"
P = {
    'B': dict(
        lineage='HG-rest-B', scope='article', key='HG-rest-41r4-b', batch='s41r4', call='Human', chance=0.55,
        diagnosis='since the recheck of 2026-10-21 (part B, Mostly Human Written, 4.9% AI; https://www.pangram.com/feed/'
                  '558d14f6-625d-46aa-8495-adf9141cb3a4): its one red window was Appendix C\'s prose (518 words, into the '
                  'audit\'s first line); that prose is now Joel\'s own five paragraphs, whose opening read Human, high, in his '
                  'check; Appendix B as installed read Human in the second screening post (B0, with 471g\'s three-roles '
                  'step); 470g\'s Appendix B and D edits are names in paragraphs that read dark green',
        tells='the run of short questions in Appendices E and F and the audit\'s list, light green last time, where the whole '
              'guide\'s red tends to land (recheck A turned the De-hypnosis questions from light green to red)',
        human='his Appendix C: a how-to lead with its examples in brackets, his own questions ("What would this thing influence '
              'me to believe that isn\'t true in order to get what it wants from me?"), "(as the police like to say)", "a '
              'bunch of these things", "boring/stupid/irrelevant", "seduce/scare/rescue"; every other appendix read dark or '
              'light green',
        shading='dark green: his Appendix C and the long stretches; light green: the short questions of Appendices B, E and F '
                'and the audit, as last time; red: none, or one of those short runs',
        decides='whether the appendices read Human with his Appendix C in (else which stretch gets a diagnosis), and what goes '
                'to Joel'),
    # Part A, after Joel's message of 2026-10-23 12:30 UTC: his own forces paragraph and batch 473's seam (Emulate's re-run)
    'A': dict(
        lineage='HG-whole', scope='article', key='HG-whole-41r5-a', batch='s41r5', call='AI', chance=0.35,
        diagnosis='since recheck A of 2026-10-22 (Mostly Human Written, 1.4% AI, 10 AI windows; https://www.pangram.com/feed/'
                  '47610d4b-fb69-4966-896f-317b029fc1af): windows 44 to 48 (the run of "By a screen? ..." questions) are now '
                  'Joel\'s own rewrite of the forces paragraph (his message of 12:30 UTC); windows 77 to 79 (the seam, question 14) '
                  'are Emulate\'s re-run (batch 473: Human, High, alone and as a pair, with the reader\'s two fixes, one of them '
                  'checked); windows 85 and 86 (the return\'s check that you\'re really back) are batch 472g\'s s3c, Human alone '
                  'through the API; nothing else in part A changed',
        tells='his forces paragraph was not checked on its own; the return paragraph\'s fix ("met a younger state") went in '
              'unchecked, since the pair\'s lineage had used its tries; changed text moves the windows, and Low ones can turn up '
              'next to it (recheck A turned the De-hypnosis questions from light green to red)',
        human='his forces paragraph in his own register ("that sudden "waking up"", "(as if breast implants are actually sexy)", '
              '"because one exposure won\'t do the trick"); the seam in Emulate\'s re-run register ("(..., whatever)", "it will be '
              'over for today", "Etcetera.", the closer\'s "!"); every other stretch of part A read Human last time',
        shading='green: the forces paragraph, the seam and the rest; Low red possible: the return\'s check (s3c) or a new Low '
                'window beside the changed text',
        decides='whether part A reads 100% Human with his paragraph and the seam in, and if not, which windows go to Emulate\'s '
                're-run next (E235) or to him'),
}


def main():
    part = sys.argv[1]
    p = P[part]
    text = X / ('TEXT-%s.txt' % part)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                        '--lineage', p['lineage'], '--scope', p['scope'], '--text', str(text), '--key', p['key'],
                        '--batch', p['batch'], '--call', p['call'], '--chance', str(p['chance']), '--tells', p['tells'],
                        '--human-tells', p['human'], '--diagnosis', p['diagnosis'], '--decides', p['decides'],
                        '--shading-expected', p['shading'], '--detector', DETECTOR], capture_output=True, text=True, cwd=REPO)
    print((r.stdout or r.stderr).strip()[-400:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
