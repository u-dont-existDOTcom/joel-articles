"""My check of every finding a reader marked "matters" (READS-ALL.json), with what became of it: a card on the marking
page, or why it stays as it is. Writes TRIAGE.md.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/triage.py

READS-ALL.json is every reader finding with "explained" set where his own words account for it (his messages, the new
sentences he approved, his inner child guide and his inner child texts of 2026-09-11); the script that set it is the
lane's triage step of 2026-10-25 (its rule: the finding's new words are in one of those texts, or half the paragraph's
sentences are).
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
DECIDED = {
    '1.17': 'stays: "you\'ll find" is his casual voice, and the guide says throughout that a dramatic trance isn\'t the point',
    '1.30': 'stays: he approved RP-1.3 today, which cut the sentence that carried it ("consider what one thing you\'re going to be working on")',
    '1.82': 'EM-1', '2.7': 'EM-2', '2.8': 'EM-2',
    '2.1': 'stays: "forced adulthood" is his term (his inner child texts of 2026-09-11)',
    '2.11': 'stays: "just borrow what you need right now, warmth or a boundary or direction" keeps his limit',
    '2.17': 'stays: the adult hat is from his inner child texts', '2.45': 'stays: "the fluffy stuff" is from his inner child texts',
    '2.63': 'stays: a small nuance, not against his meaning',
    '3.13': 'stays: a reassurance said many times in the guide; his rule is to say a safety line once, where it changes what the reader does',
    '3.24': 'EM-3', '3.26': 'stays: the paragraph\'s "you can do reparenting and finding yourself in parallel" carries his point for the harder group',
    '3.32': 'EM-4', '3.33': 'stays: "One way of explaining this" already frames it as one explanation', '3.34': 'EM-5 (the sentence after it)',
    '3.36': 'stays: the long-term break is from his inner child texts (approved today in the alignment)',
    '3.68': 'stays: his good-guide test is in Appendix C ("A good guide can take no. A bad guide can\'t take no."); this paragraph\'s "guide" is the list of questions, and reads right',
    '4.8': 'stays: a small condition; the paragraph is about a simple test',
    '4.15': 'EM-6', '4.20': 'EM-7', '4.38': 'stays: the next paragraph says to give it time ("stick around till she gets it all out")',
    '5.11': 'EM-8', '5.20': 'EM-9', '5.23': 'stays: the section\'s next paragraph says to answer what comes up ("Respond to each thing that comes up ...")',
    '5.61': 'stays: "not a proven fact" keeps his caution, said again nearby ("images ... can be meaningful without being actual memories"); its stray comma is fixed',
    '6.16': 'EM-10', '6.57': 'EM-11', '6.69': 'stays: "seek professional help promptly" keeps his point',
    '7.23': 'stays: "in a way I can integrate it" keeps his limit', '7.25': 'EM-12',
    '7.35': 'stays: close to his meaning', '7.43': 'stays: the next paragraph names the part that argues back',
    '7.55': 'stays: "please don\'t use it except to presume ..." keeps his limit', '7.61': 'EM-13', '8.1': 'EM-14',
    '8.10': 'stays: in Appendix B he writes about using NLP with others too',
    '8.26': 'stays: the paragraph\'s "I am using the noticing of the synchronicity to WAKE UP" carries it',
    '8.29': 'stays: his published cue has "the highest perspective I can access"',
    '8.35': 'stays: the guide calls the third adult the Guide throughout, as his inner child guide does', '8.50': 'stays: as 8.35',
    '8.38': 'stays: he approved the CV-6 cuts of those lines today', '8.39': 'stays: as 8.38 (CV-6.12)',
    '8.41': 'stays: close to his meaning', '8.48': 'stays: a small step',
    '8.65': 'EM-15', '9.0': 'stays: his 12 c answer, three roles in one inner adult',
    '9.6': 'stays: a small check; the step keeps its body check and evidence',
    '9.19': 'stays: he answered this paragraph in the 4.1 round (questions page, Appendix D)',
    '9.24': 'stays: a note in his voice that adds no claim against his line',
    '10a.0': 'stays: his own capitals and his General Rule say the same', '10a.1': 'stays: an example, not a claim',
    '10a.2': 'EM-16', '10a.3': 'stays: a boundary line in keeping with "door closed"', '10b.0': 'stays: said many times in the guide',
    '10b.1': 'EM-S2', '10b.2': 'stays: he approved CV-8.8 today, which cut the line it replaced',
}


def main():
    R = json.loads((HERE / 'READS-ALL.json').read_text(encoding='utf-8'))
    m = [x for x in R if x['severity'] == 'matters']
    lines = ['# The strict Emulate check: what became of each finding that matters', '',
             'Made by `triage.py` from `READS-ALL.json` (%d findings; %d marked "matters" by a reader). "his own words" means his'
             ' messages, the new sentences he approved, or his inner child texts account for it. A card id is on the marking'
             ' page (`REVIEW-EMULATE.json`).' % (len(R), len(m)), '', '| Finding | Where | What the reader saw | What became of it |', '|---|---|---|---|']
    missing = []
    for x in m:
        fate = 'stays: his own words (%s)' % x['explained'] if x['explained'] else DECIDED.get(x['id'])
        if fate is None:
            missing.append(x['id'])
            continue
        lines.append('| %s | %s | %s | %s |' % (x['id'], x['where'].replace('|', '/'), x.get('why', '').replace('|', '/')[:180], fate.replace('|', '/')))
    assert not missing, missing
    (HERE / 'TRIAGE.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(len(m), 'findings written')


if __name__ == '__main__':
    main()
