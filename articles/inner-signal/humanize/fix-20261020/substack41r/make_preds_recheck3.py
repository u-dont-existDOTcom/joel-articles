"""Part A of the recheck again, with the listening script in it (2026-10-21, after HG17's fixed version went into the working
copy): the old part A prediction is voided and the new one written before the re-paste.

Part A (key HG-whole-41r2-a, 19:23 UTC) had not been opened when the induction section's fixed version was installed:
no result in Joel's History or the app's pane by 20:40 UTC, and he had not answered the 19:32 message. So part A was rebuilt
from the working copy (make_recheck.py) and pasted into the same temporary draft, and one opening reads both batch 469g and
the listening script. Part B (Appendices to the end) doesn't hold the section; its text and prediction (HG-rest-41r2-b)
stay as they were.

  python3 articles/inner-signal/humanize/fix-20261020/substack41r/make_preds_recheck3.py   (from the repo root)
"""
import hashlib, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
X = pathlib.Path(__file__).resolve().parent
LEDGER = REPO / 'articles' / 'inner-signal' / 'humanize' / 'pangram-ledger.jsonl'
CHANGED = ('since try 1 (2026-10-20): the 4.1 edits of 467g and 468g (HG12, HG15, Appendices D and F) and Joel\'s own edit '
           'of HG15 (his check, Human); the NLP appendix (HG31) and the return steps (HG18) as their Human versions (his '
           'answers 3 a and 4 d; 4.0 checks, never read in 4.1); batch 469g, read here for the first time (gate E200): '
           'Appendix C\'s general checklist as prose, the return steps\' lost points put back, and the inner-adult sweep\'s '
           'five fixes (fix-20261021/b469/batch/PREDICTIONS.md); and the induction section (HG17), which read red as '
           'published at try 1, now Emulate\'s sample ba with every point it lost put back (fix-20261018/rf-zg/, '
           'HG17.fixed.json; its meaning, cold read, march and stance reviews there)')
NEW_A = dict(
    lineage='HG-whole', scope='article', key='HG-whole-41r3-a', text=X / 'WHOLE-GUIDE-41r-A.txt', call='AI', chance=0.03,
    tells='the listening script\'s count and its two-hand lines are short spoken steps, and its sample was never read in '
          'Pangram (E200); the NLP appendix\'s and the return steps\' Human versions were checked only in 4.0; Appendix C\'s '
          'prose had no break in its march read; the induction section\'s restored points are mine, in plain words',
    human='the induction section is Emulate\'s text in a personal register (the samples of 459g read 17 of 17 paragraphs '
          'Human); Joel\'s HG15 edit read Human in his own check; every other installed section read dark green at try 1',
    shading='light green or red: parts of the listening script (the count, the two-hand lines, the shortcut\'s steps) and '
            'the bridge before it (HG16); some of the NLP appendix (4.0 only) and of the return count; light green or red: '
            'Appendix C\'s prose, if part A reaches it; dark green: HG12, HG15 with Joel\'s edit, the five inner-adult '
            'fixes, the rest',
    decides='whether the induction section\'s fixed version reads Human in the real article (else which of its paragraphs '
            'go to pangram.com with a diagnosis), whether the installed Human versions hold in 4.1, which of batch 469g\'s '
            'paragraphs need a try, and what goes to Joel')


def ledger(*args):
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py')] + [str(a) for a in args],
                       capture_output=True, text=True, cwd=REPO)
    print(' '.join(str(a) for a in args[:2]), (r.stdout or r.stderr).strip()[-300:])
    return r.returncode


def main():
    import json
    old = [json.loads(l) for l in LEDGER.read_text(encoding='utf-8').splitlines() if l.strip()]
    pa = next(r for r in old if r.get('type') == 'prediction' and r.get('key') == 'HG-whole-41r2-a')
    if not any(r.get('type') == 'void' and r.get('prediction') == pa['id'] for r in old):
        rc = ledger('void', LEDGER, '--sha', pa['sha256'], '--reason',
                    'never opened: part A of the recheck was rebuilt with the induction section\'s fixed version (HG17) and '
                    'pasted into the same temporary draft before Joel opened the 19:32 UTC links (no result in his History '
                    'or the app\'s pane at 20:40 UTC); key HG-whole-41r3-a is its text now')
        if rc:
            return rc
    p = NEW_A
    sha = hashlib.sha256(p['text'].read_bytes()).hexdigest()
    if sha == pa['sha256']:
        raise SystemExit('part A did not change: run make_recheck.py after the install')
    return ledger('predict', LEDGER, '--lineage', p['lineage'], '--scope', p['scope'], '--text', p['text'], '--key', p['key'],
                  '--batch', 's41r3', '--call', p['call'], '--chance', str(p['chance']), '--tells', p['tells'],
                  '--human-tells', p['human'], '--diagnosis', CHANGED, '--decides', p['decides'],
                  '--shading-expected', p['shading'],
                  '--detector', "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)")


if __name__ == '__main__':
    sys.exit(main())
