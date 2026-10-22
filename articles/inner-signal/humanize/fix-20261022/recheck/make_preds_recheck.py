"""The next whole-guide recheck's predictions (2026-10-22), written before each part is pasted, let alone checked.

  python3 articles/inner-signal/humanize/fix-20261022/recheck/make_preds_recheck.py A   (from the repo root, after make_recheck.py)
  python3 articles/inner-signal/humanize/fix-20261022/recheck/make_preds_recheck.py B

Each part's text is TEXT-A.txt or TEXT-B.txt (make_recheck.py: the payload's text as the check reads it, cut at 99,999
characters), so the ledger's SHA-256 is the checked text's. Part A holds the induction section from sample bf with its
meaning fixes (fix-20261022/hg17-bf/), batch 470g's names in the guide's body and batch 471g's forced adulthood; part B holds
the appendices: Appendix C as the second screening post decides it (fix-20261022/screen2/), 470g's Appendix B and D edits
and 471g's three-roles step.
"""
import pathlib, subprocess, sys

X = pathlib.Path(__file__).resolve().parent
REPO = X.parents[4]
LEDGER = X.parents[1] / 'pangram-ledger.jsonl'
DETECTOR = "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"
P = {
    'A': dict(
        lineage='HG-whole', scope='article', key='HG-whole-41r4-a', batch='s41r4', call='AI', chance=0.10,
        diagnosis='since the recheck of 2026-10-21 (part A, AI Detected, 13.8% AI): the induction section (HG17), red there as '
                  'sample ba with every lost point put back, is now sample bf (Human in every window of the first screening '
                  'post, 46 windows, 23 of them light green) with 31 meaning fixes inside its own sentences, Joel\'s 11 b '
                  'word for word and the published headings; the return\'s three short red windows (HG18) are unchanged; '
                  'batch 470g (Joel\'s answers 9 and 10: childhood protector parts, the Inner Child article\'s names, 23 '
                  'paragraphs) and 471g\'s forced adulthood are read for the first time',
        tells='the return (HG18) still has the three short stretches that read red; bf\'s fixes add short instructions to a '
              'script ("Leave a little space.", "Say it as an invitation and notice how it\'s received."); half of bf\'s '
              'windows were light green in the screening, where the whole article\'s red tends to land',
        human='bf read Human in all 46 windows on its own; every other section read dark green in the last recheck, and 470g\'s '
              'changes are names in paragraphs that read dark green',
        shading='light green or red: the return\'s three stretches, some of bf\'s light-green windows; dark green: the rest',
        decides='whether the induction section from bf reads Human in the guide (else which of its stretches get a diagnosis), '
                'whether 470g\'s and 471g\'s paragraphs hold, and what goes to Joel'),
    'B': dict(
        lineage='HG-rest-B', scope='article', key='HG-rest-41r4-b', batch='s41r4', call='Human', chance=0.5,
        diagnosis='since the recheck of 2026-10-21 (part B, Mostly Human Written, 4.9% AI, Appendix C\'s prose one red window): '
                  'Appendix C as the second screening post decided it; 470g\'s Appendix B and D edits; 471g\'s three-roles '
                  'step',
        tells='Appendix B\'s lists before Appendix C; the three-roles step\'s three parallel infinitives',
        human='every other appendix read dark green in the last recheck',
        shading='dark green except, perhaps, Appendix B\'s lists and Appendix C\'s opening',
        decides='whether the appendices read Human with Appendix C as chosen, and what goes to Joel'),
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
