"""The second screening post's predictions (2026-10-22), written before the post was pasted, let alone checked.

Each sample is its own lineage (one stretch of a Substack check each), so a sample's result settles only its own call. The
text of each is its span of TEXT-S2.txt (SPANS-S2.json), as TEXT-B0.txt and so on.

  python3 articles/inner-signal/humanize/fix-20261022/screen2/make_preds_screen2.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

S = pathlib.Path(__file__).resolve().parent
REPO = S.parents[4]
LEDGER = S.parents[1] / 'pangram-ledger.jsonl'
DETECTOR = "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"
LINEAGE = {'B0': 'HG31-nlp-tail', 'C0': 'HG32-469g', 'C1': 'HG32-c1', 'C2': 'HG32-c2'}
DECIDES = {'B0': 'whether the first half of the recheck\'s red window 16 (part B) is Appendix B\'s, so its lists need a fix '
                 'of their own',
           'C0': 'whether Appendix C as installed reads AI without the window it shared with Appendix B (if Human, it stays '
                 'and Appendix B\'s stretch is the one to fix)',
           'C1': 'whether this candidate is the Appendix C that goes into the guide (the one that reads Human; if none '
                 'does, the question goes back to Joel)',
           'C2': 'whether this candidate is the Appendix C that goes into the guide (the one that reads Human; if none '
                 'does, the question goes back to Joel)'}
DIAGNOSIS = {
    'B0': 'not a fix: Appendix B\'s stretch as installed (Emulate\'s text, batches 470g and 471g in), read on its own to find '
          'where the recheck\'s 518-word red window comes from',
    'C0': 'not a fix: Appendix C as installed (469g), read right after B0 as in the guide, but in a check of its own',
    'C1': 'the opening\'s three litanies (six sources, six "I can" moves, four maxims of one shape) read AI in every version; '
          'here they are said as a person says them, with a question and its short answer among the tests, two tests in '
          'one sentence and the last as a plain warning (the shapes that read Human, high, in C0\'s last two paragraphs); '
          'bg\'s middle, which read Human, with two published words back; C0\'s end, which read Human, high',
    'C2': 'as C1, with the known names for what the opening describes ("the sniff test", "the voice in your head"), a test '
          'with its own logic ("Real guidance keeps overnight, so sleep on it") and the statement\'s questions asked plainly, '
          'one left elliptical',
}
P = {
    'B0': ('AI', 0.30,
           'six sentences in a row opening "I do not use NLP"; a ten-step list of imperatives, each with a bracketed list',
           '"too high/dissociated", "psychosis-like state" in quotes, "is NOT consent", the space before the colon in "the '
           'entire NLP process :", "(If...then... statement)", Joel\'s clarification of the three roles'),
    'C0': ('AI', 0.30,
           'the opening\'s list of six sources with "stuff like that"; the statement\'s run of moves; the four tests in four '
           'shapes that still read as maxims; "It\'s a warning if ... Same if ... Or if ..."',
           '"stuff like that", "like the dishes and your friends don\'t matter anymore", "Being rescued counts too.", '
           '"you name it", the question and its short answer about the guide'),
    'C1': ('AI', 0.40,
           'the list of six sources is still a list; the statement is still a run of moves; three of the tests are still '
           'short maxims ("Love can live with your boundaries")',
           '"anything like that", "for a minute", "My body\'s telling me something", "Can it handle your questions? '
           'Something true can.", "(usual)", the twelve tricks in one comma list (Human, high in bg), "you name it"'),
    'C2': ('AI', 0.35,
           'three short sentences of one shape in the tests ("True things can stand up to questions. Love can take a '
           'boundary."); "Here\'s my checklist" opening a list; the closing test is a tidy line',
           '"slow way down", "who gets something out of it", the elliptical "What would truth, or humility, or my ordinary '
           'life?", "the sniff test", "keeps overnight", bg\'s middle and C0\'s end as in C1'),
}


def ledger(*args):
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py')] + [str(a) for a in args],
                       capture_output=True, text=True, cwd=REPO)
    print(' '.join(str(a) for a in args[:2]), (r.stdout or r.stderr).strip()[-300:])
    return r.returncode


def main():
    spans = json.loads((S / 'SPANS-S2.json').read_text(encoding='utf-8'))
    full = (S / 'TEXT-S2.txt').read_text(encoding='utf-8')
    rc = 0
    for label, sp in spans.items():
        f = S / ('TEXT-%s.txt' % label)
        f.write_text(full[sp['start']:sp['end']], encoding='utf-8')
        call, chance, tells, human = P[label]
        rc |= ledger('predict', LEDGER, '--lineage', LINEAGE[label], '--scope', 'stretch', '--text', f,
                     '--key', 'screen2-%s' % label, '--batch', 'screen2-20261022', '--call', call, '--chance', str(chance),
                     '--tells', tells, '--human-tells', human, '--diagnosis', DIAGNOSIS[label], '--decides', DECIDES[label],
                     '--detector', DETECTOR)
    return rc


if __name__ == '__main__':
    sys.exit(main())
