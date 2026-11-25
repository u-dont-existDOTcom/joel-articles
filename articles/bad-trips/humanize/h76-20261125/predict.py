#!/usr/bin/env python3
"""predict.py - turn 68's predictions for my two tries, written before the checks, through the API with his key on his
laptop: the charcoal and poison control paragraphs of Swallowed Too Much? (B127, B128, together since B128 is 41 words) and
the opening of Serotonin Syndrome (SS)? (B130). Each is one try from his post's text, after the three fresh reads and the
tell panel on that text and three more fresh reads on my first draft (fill_h76.py).

  python3 predict.py a2-b127-b128 a2-b130
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h76-20261125/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
BATCH = 'h76a'
P = {
    'b127': dict(
        lineage='bad-trips Swallowed Too Much?, the charcoal and poison control paragraphs (B127, B128) as they stand, together (h75)',
        call='AI', chance=0.15, panel='panel-b127/PANEL.md',
        tells=['anybody who is vomiting, sedated, seizing or otherwise unable to protect their airway',
               'They\'re also who to ask when you can\'t tell what the substance is or what it does in combination'],
        human=["I don't treat calling poison control as a mandatory ritual, though", 'by whoever answers',
               'so go on with any first aid while you talk to them'],
        hum=('the three fresh reads and the tell panel on his post\'s text (reads/*-asis-swallowed-sec.txt, panel-b127/PANEL.md: all '
             'six sentences agreed), then three fresh reads on my first draft (reads/*-a1-swallowed-sec.txt), every mark changed or '
             'answered in the receipt; the ways of his round-57 kidney fix: each sentence tied to the one before by what they '
             'share, the exact act for the generic one, the caution in the first person'),
        first=('payoff: whether charcoal is still worth giving comes first, tied to "how long ago" in his paragraph before; '
               'join: "since it binds", "It only helps with what binds to it, which leaves out", "because anybody who", '
               '"They\'re also who to ask", "though, since", "And what they give you is help deciding, so"; plain: "could '
               'breathe it into their lungs (aspiration)", "the worst coming hours later"'),
        diag=('try 1, his post\'s two paragraphs as they stand, read AI High 95 in one window (862a4a34), and the tell panel '
              'agreed on all six sentences: the stacked hedges of the opener, the three caveats with a four-item list, the bare '
              '"Clinical review." label, the four abstract nouns of the poison control sentence, the balanced "by country and by '
              'whoever answers", and the closing slogan "decision support, not first aid"; both said each paragraph runs claim, '
              'qualifications, short closing line. This try keeps every warning and says each as what happens or what to do: the '
              'review\'s link sits on what it shows (the first hour), the four cases of the list get what happens to them, the '
              'four nouns are clauses with the charcoal one first, and the slogan is the act it stands for'),
        big=('his post\'s text read AI High in one window with no Human window to start from, and the panel agreed on every one '
             'of its six sentences, so no sentence could stay as it was; every warning, condition and stance is kept')),
    'b130': dict(
        lineage='bad-trips Serotonin Syndrome (SS)?, its opening paragraph (B130) as it stands, by itself (h75)',
        call='AI', chance=0.2, panel='panel-b130/PANEL.md',
        tells=['ayahuasca and other MAOI brews, MDMA, DXM cough syrup and many antidepressants, as well as other MAOIs',
               'do not necessarily treat it'],
        human=["but I'd suspect it most when two of them were combined", 'so check for it too whenever they\'ve had something that raises serotonin'],
        hum=('the three fresh reads and the tell panel on his post\'s text (reads/*-asis-ss-open.txt, panel-b130/PANEL.md: all '
             'three sentences agreed), then three fresh reads on my first draft (reads/*-a1-ss-open.txt), every mark changed or '
             'answered in the receipt; the ways of his round-57 kidney fix: the pivot tied to the sentence before, the vague '
             'cases said as what happened'),
        first=('payoff: what serotonin syndrome can look like, then what to do about it (check for it too); join: "since it can '
               'also bring on", "But ... so check for it too", "That includes", "Too much of any one of them ..., and so can ..., '
               'but I\'d suspect it most when"; plain: "a medication that was just started or had its dose raised" for '
               '"serotonergic medication changes"'),
        diag=('try 1, his post\'s paragraph as it stands, read AI Low 20 on its first sentence and AI High 31 on the rest '
              '(c068929c), and the tell panel agreed on all three sentences: the cross-reference with "do not necessarily", the '
              'triad of abstract nouns ("changes, combinations, or excessive exposure"), and the evenly weighted list ending on '
              '"especially in combinations", which says "combinations" twice. This try names the symptoms the first sentence '
              'points back at, gives the sentence an act, says the three cases as what happened with the combination last and '
              'once, and glosses three of the substances with step 1\'s own words; "do not" stays, a fidelity key (W035)'),
        big=('his post\'s text read AI in both windows with no Human window to start from, and the panel agreed on all three '
             'sentences, so none could stay as it was; every substance and the warning are kept')),
}

# try 3 of the serotonin opening: the near miss (a2: Human High 21, Human Medium 26, AI Low 28, Human Low 38; f626837b) with
# its one AI sentence changed and nothing else (lesson bad-trips-2026-11-19b)
P['a3-b130'] = dict(
    lineage=P['b130']['lineage'], call='Human', chance=0.5, panel='panel-b130/PANEL.md',
    tells=['MDMA, DXM cough syrup and many antidepressants', 'do not necessarily treat it'],
    human=['ayahuasca and other MAOI brews (or any other MAOI)', 'the painkiller tramadol and some other opioids',
           "but I'd suspect it most when two of them were combined"],
    hum=('try 2 read Human in three of its four sentences (f626837b); this try changes only words in the sentence that read AI '
         'Low, the substance list, the way his round-57 kidney fix moved the electrolyte shifts beside the depletion they '
         'belong with: "any other MAOI" stands beside the MAOI brews, and tramadol beside the other opioids'),
    first=('payoff: unchanged from try 2 (what it can look like, then check for it too); join: unchanged; plain: "(or any other '
           'MAOI)" beside the brews for "other MAOIs" four items later, "some other opioids" after tramadol'),
    diag=('try 2 read Human High 21, Human Medium 26, AI Low 28 and Human Low 38 (f626837b). The AI Low window is the substance '
          'list alone, and two things in it can be taken two ways: "other MAOIs" stood four items after "ayahuasca and other MAOI '
          'brews", so a reader can\'t tell what it is other than; and "some opioids" stood apart from tramadol, which is one, as '
          'if tramadol were not. A first version of this try regrouped the whole list (29% of the words) and the ledger refused '
          'it, rightly; this one moves "other MAOIs" beside the brews as "(or any other MAOI)", puts tramadol last before "some '
          'other opioids", and changes nothing else'),
    big=None)


def run(key):
    p = P.get(key) or P[key.split('-')[1]]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', p['call'], '--chance', str(p['chance']),
         '--detector', DET, '--decides', ('whether %s reads Human High in every window by itself; if it does it goes to him as a '
                                          'card to approve (it sharpens a warning from its source), and if not it goes to him as '
                                          'a teaching card with the panel and this try') % key,
         '--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', p['hum'], '--first-fix', p['first'],
         '--diagnosis', p['diag'], '--panel', REL + p['panel']]
    if p.get('big'):
        a += ['--big-change', p['big']]
    for t in p['tells']:
        a += ['--tells', t]
    for t in p['human']:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=str(REPO), capture_output=True, text=True)
    print(key, '|', (r.stdout + r.stderr).strip()[-900:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(run(k) for k in sys.argv[1:]))
