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
