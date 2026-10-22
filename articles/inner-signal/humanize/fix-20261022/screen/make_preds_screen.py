"""The screening post's predictions (2026-10-22), written before the post was pasted, let alone checked.

Each sample is its own lineage (one stretch of a Substack check each), so a sample's result settles only its own call. The
text of each is its span of TEXT-S.txt (SPANS.json), as TEXT-S1.txt and so on.

  python3 articles/inner-signal/humanize/fix-20261022/screen/make_preds_screen.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

S = pathlib.Path(__file__).resolve().parent
REPO = S.parents[4]
LEDGER = S.parents[1] / 'pangram-ledger.jsonl'
DETECTOR = "pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)"
DECIDES = {'HG17': 'whether this sample is the one the induction section\'s meaning work starts from (the sample that reads '
                   'Human, or the one with the fewest red windows, else none of these and a different method)',
           'HG32': 'whether this sample is the one Appendix C\'s general checklist starts from (the one that reads Human, '
                   'else my prose is reworked with a diagnosis, or the question goes to Joel)'}
P = {
    'S1': ('AI', 0.35,
           'the listening script as short spoken imperatives, seven "Bring to mind" lines in a row in the open and awake '
           'parts; formal, translated-sounding lines ("To contain a state you are already in, rather than intensify."); the '
           'opening explains utilization in general terms; the shortcut\'s last paragraphs are tidy warnings',
           'typos kept ("solar plexis", "subtlely"), "etc, etc, etc", the first person ("something I threw together for a '
           'session and I like how it turned out", "My dad has a mudra"), uneven sentence lengths, headings run into their '
           'paragraphs'),
    'S2': ('AI', 0.45,
           'the listening script\'s short lines ("Take a moment to do that…", "What do you notice in response?") read like '
           'the steps that read red at try 1; the before-you-begin part is a run of "If you say ... If you say" lines',
           'a loose, spoken register ("shamelessly stolen from the Gerson hypnosis course", "it\'s all just soup" kind of '
           'asides), a misspelling ("twich"), the dad\'s mudra in the first person, long rambling sentences in the '
           'shortcut part'),
    'S3': ('AI', 0.40,
           'long chains of "or ... or ... or"; the before-you-begin steps as numbered instructions; the closing paragraphs '
           'of the shortcut are a list of rules; its input was the version that read AI, humanized, in the guide',
           'numbering that changes style halfway ("1)" then "4."), broken lines Emulate left ("Don\'t read out the '
           'instructions in , but"), casual asides ("It\'s good to relax while driving"), capitals for stress ("NOT", '
           '"PICKING")'),
    'S4': ('Human', 0.55,
           'its input was the version that read AI, humanized; the script\'s quoted lines are long and smooth; the '
           'shortcut\'s rules come as a row of "Be able to ..." sentences',
           'the most casual of the four ("by all means, just do that", "It\'s all just soup", "To be done: check out '
           'Nymja\'s sleep playlist"), numbering in Roman numerals after Arabic ones, fragments and run-ons, a misspelled '
           'name, "she" for the person speaking'),
    'S5': ('AI', 0.30,
           'Appendix C\'s content is a list whatever its form: twelve tricks in one comma list, four questions in a row, '
           'then the good and bad guide in parallel sentences; the published list and my prose both read AI',
           'a curse ("slow the fuck down"), "(usual)" in brackets, plain words, "etc." twice'),
    'S6': ('AI', 0.35,
           'the tricks as one-word fragments ("Urgency. Secrecy. Shame."), a list in all but name; the four tests in the '
           'same "If it\'s really X, it will Y" shape; the published list read AI',
           'a slightly foreign register ("Before giving in to whatever it is, check, if the usual methods are used."), '
           '"whatever is the poison of the day", "him- or herself", plain words'),
}


def ledger(*args):
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py')] + [str(a) for a in args],
                       capture_output=True, text=True, cwd=REPO)
    print(' '.join(str(a) for a in args[:2]), (r.stdout or r.stderr).strip()[-300:])
    return r.returncode


def main():
    spans = json.loads((S / 'SPANS.json').read_text(encoding='utf-8'))
    full = (S / 'TEXT-S.txt').read_text(encoding='utf-8')
    rc = 0
    for label, sp in spans.items():
        f = S / ('TEXT-%s.txt' % label)
        f.write_text(full[sp['start']:sp['end']], encoding='utf-8')
        call, chance, tells, human = P[label]
        rc |= ledger('predict', LEDGER, '--lineage', '%s-%s' % (sp['section'], sp['sample']), '--scope', 'stretch',
                     '--text', f, '--key', 'screen-%s' % label, '--batch', 'screen-20261022', '--call', call,
                     '--chance', str(chance), '--tells', tells, '--human-tells', human,
                     '--diagnosis', 'a new Emulate sample (%s, %s), screened before any meaning work: the last sample, ba, was '
                                    'chosen by meaning alone and read AI, humanized, in the guide' % (sp['sample'], sp['run']),
                     '--decides', DECIDES[sp['section']], '--detector', DETECTOR)
    return rc


if __name__ == '__main__':
    sys.exit(main())
