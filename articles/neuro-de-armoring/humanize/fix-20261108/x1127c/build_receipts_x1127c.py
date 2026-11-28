"""The receipts for this turn's texts of mine (texts_x1127c): Part 1's intro line with the paragraph after it (P030-P032,
the pair it is checked as, since the line is under 50 words), and "A. The Metabolic Red Line"'s two paragraphs by
themselves (P032, P033), each fixed for sense from its three fresh reads (x1127c/v1, Fable, 2026-11-27).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127c/build_receipts_x1127c.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import build_receipts_x1123a as B  # noqa: E402
import texts_x1127c as T  # noqa: E402

S = B.S
OUT = HERE / 'receipts'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
SCI = 'Part 1: THE SCIENCE (Why We Do This), and its first subsection, A. The Metabolic Red Line'
RED = 'A. The Metabolic Red Line (in Part 1: THE SCIENCE)'
WHO = ('an adult with trauma who has done years of therapy (CBT, EMDR) and still gets triggered, starting the science '
       'behind this protocol\'s tools')


def old(key, n):
    return S.sentences(T.plain(T.OLD[key]))[n - 1]


def reader(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-27) given tools/humanization/%s and only the paragraph as it stood, one '
            'sentence a line (x1127c/v1/%s/%s/READ.md)' % (brief, kind, key))


SPEC = {
    'To see what the tools': ('they learn why the science comes before the tools: the tools are built to fix what goes '
                              'wrong in the brain',
                              'the part\'s first line, after the practice the section before ends on', None),
    'If you\'ve tried to talk': ('they learn why they couldn\'t talk themselves out of a trigger: blood flow leaves the part '
                                 'of the brain that reasons for the part that keeps them alive',
                                 'it opens the first failure, A, on something the reader has lived',
                                 'If you\'ve tried to talk yourself out of a trigger'),
    'That happens once': ('they learn when it happens (a resting heart rate higher than usual, or the time between beats '
                          'varying less than usual, both of which a smartwatch shows) and that it passes once they calm '
                          'down',
                          'it says when the shift the sentence before describes happens, and how long it lasts',
                          'That happens'),
    'Perry describes the point': ('they learn the names the protocol uses for that point and for the state past it, which '
                                  'come back later (the red-line test in Part 4)',
                                  'it names what the two sentences before describe', 'the point where that happens'),
    'If you try to process': ('they learn that working on trauma above the line adds armor instead of taking it off',
                              'it says what the red line means for trauma work, the point before its reason',
                              'If you try to process trauma while you\'re above this red line'),
    'Above the line your': ('they learn why: above the line they can\'t think as well, and stress chemicals flood a '
                            'reward center deep in the brain and build up DeltaFosB, which this protocol treats as the '
                            'armor itself, and how settled that is', 'it gives the reason for the sentence before',
                            'Above the line'),
    'There they switch on': ('they learn the second part: those chemicals switch on the protein researchers suspect holds '
                             'the armor in place, so not settled', 'it says what the chemicals do where they flood',
                             'There they'),
    'Only work on your': ('they keep their trauma work under the line, and know the name therapists use for that',
                          'it gives the act the three sentences before call for', 'Only work on your trauma while you\'re '
                          'under that line'),
}
CHECKED_RED = [
    ('Perry\'s "Metabolic Red Line" and his "Fear" state',
     'one web search (2026-11-27 23:3x UTC, "Bruce Perry "metabolic red line" heart rate trauma") found no use of the '
     'term by Perry; his model is state-dependent functioning, with fear one of its states (calm, arousal, alarm, fear, '
     'terror); not an absence claim: one search', 'yes: they learn the name the protocol uses for the line, and whose '
     'idea it is; the attribution stays as the post has it and goes to Joel as a question', 'kept'),
    ('the line in the reader\'s terms: heart rate above its usual resting rate',
     'his 62a: the red line\'s test reads "back down to your usual resting rate, and under 90 BPM" in its three places '
     '(x1124b)', 'yes: they know what crossing the line means for them', 'changed')]
CHECKED_33 = [
    ('DeltaFosB may hold the armor in place, and the research isn\'t settled',
     'his 39a moved section B\'s caveat here (x1123b/apply_x1123b.py); the needed read\'s correction: catecholamines '
     'don\'t "transcribe" proteins, they set off the making of DeltaFosB', 'yes: they know how far to trust the armor\'s '
     'chemistry', 'kept')]
Q = {'Q1': 'PASS: each sentence opens on its point or on the reader\'s own case',
     'Q2': 'PASS: the one instruction (work on trauma only under the line) says what it is for: not adding armor',
     'Q3': 'PASS: each thing is named exactly (the part that reasons, the Cortex, the Brainstem, the line, the protein)',
     'Q4': 'PASS: each unfamiliar term is said in plain words where it is first used (catecholamines as stress '
           'chemicals, the window of tolerance as working under the line)',
     'Q5': 'PASS: each "so", "and" and "though" turns on the clause before it',
     'Q6': 'PASS: the claim, then why, then the limit (may, isn\'t settled)',
     'Q7': 'PASS: each fact is about what happens to the reader when triggered',
     'Q8': 'N/A: no group or list inside these paragraphs but the protocol\'s scope (trauma, withdrawal or chronic stress)',
     'Q9': 'PASS: one step a clause, with the small words that carry the relation kept'}


def build(name, keys, text, where, opens, checked, same, place, needed, his, fit, his_answer=None):
    errs = B.build(name, text, where, WHO, SPEC, opens, checked, needed, his, fit, same, place)
    import json
    f = OUT / ('%s.receipt.json' % name)
    r = json.loads(f.read_text(encoding='utf-8'))
    r['questions'] = dict(Q)
    if his_answer is not None:
        r['his_answer'] = his_answer
    f.write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return ['%s: %s' % (name, x) for x in S.check(text, r)]


HIS30 = [(1, '5, 13: opens on a rule before why the reader needs it'), (1, '16: "the tools" twice'),
         (1, '21: "Hardware Failures" hung on as a label'), (1, '8: "actually" says nothing')]
FIT30 = [(1, 'FROM: "withdrawal" from an addiction text (the protocol is for trauma and addiction, so it stays); MISREAD: '
             '"Hardware Failures" sounds permanent; "must understand ... before applying" sounds like the breathing '
             'waits')]
HIS32 = [(1, '21, 16: "anatomy overrides intellect", two abstract nouns acting, said again by S2'),
         (2, '5, 11, 1, 2, 4, 10: Perry and his term before the reader; packed; glosses built alike; past what; "(a state '
             'of "Fear")"')]
FIT32 = [(1, 'MISREAD: "anatomy overrides intellect" reads as always'),
         (2, 'ANYWAY: heart rate up after coffee; CAN\'T TELL: HRV, no number, "resting" is measured calm; FROM: '
             'wearable readings; MISREAD: blood flow shifting sounds like damage')]
HIS33 = [(2, '5, 3, 21, 28, 12: opens on "many trauma therapies"; "rather than overwhelming activation"; the advice '
             'before the mechanism'),
         (3, '10, 1, 9, 16: "In that state" two ways; packed; the doubt said twice in a bracket')]
FIT33 = [(3, 'FROM: animal stress research said as fact; MISREAD: "In that state" after the window of tolerance; '
             '"the armor itself" against "isn\'t settled"')]


def marks(key, ms, field):
    return [{'s': old(key, n), field: d} for n, d in ms]


def p030_032():
    text = T.plain(T.NEW['p030']) + '\n\n' + T.plain(T.NEW['p032'])
    return build('P030-P032-S1', ['p030', 'p032'], text, SCI,
                 'they learn the science part tells them what each tool in the protocol is for',
                 CHECKED_RED,
                 'none: read Part 1 from its heading to B (the red line: what it is and what it means for trauma work); '
                 'the Cognitive Warning at the top and Part 4\'s Step 2 give the red line\'s test and point here',
                 'Part 1\'s intro line and the first paragraph under A, where the post has them',
                 {'reader': reader('needed', 'p030') + '; ' + reader('needed', 'p032'), 'unneeded': [], 'kept': {}},
                 {'reader': reader('his-fixes', 'p030') + '; ' + reader('his-fixes', 'p032'),
                  'marked': marks('p030', HIS30, 'difference') + marks('p032', HIS32, 'difference'), 'kept': {}},
                 {'reader': reader('fit', 'p030') + '; ' + reader('fit', 'p032'),
                  'marked': marks('p030', FIT30, 'found') + marks('p032', FIT32, 'found'), 'kept': {}},
                 his_answer=[])


def p032():
    return build('P032-S1', ['p032'], T.plain(T.NEW['p032']), RED,
                 'they recognize their own failure to talk themselves out of a trigger, and learn why it happens',
                 CHECKED_RED,
                 'none: read A from its heading to B (the red line: what it is, then what it means for trauma work)',
                 'the first paragraph under A, where the post has it',
                 {'reader': reader('needed', 'p032'), 'unneeded': [], 'kept': {}},
                 {'reader': reader('his-fixes', 'p032'), 'marked': marks('p032', HIS32, 'difference'), 'kept': {}},
                 {'reader': reader('fit', 'p032'), 'marked': marks('p032', FIT32, 'found'), 'kept': {}},
                 his_answer=[])


def p033():
    unneeded = old('p033', 3)
    return build('P033-S1', ['p033'], T.plain(T.NEW['p033']), RED,
                 'they learn what working on their trauma above the line does to them, and what to do instead',
                 CHECKED_33,
                 'none: read A from its heading to B; section B\'s copy of the red line went with his 39a, its window of '
                 'tolerance and DeltaFosB caveat moved here',
                 'the second paragraph under A, after the line is named',
                 {'reader': reader('needed', 'p033'), 'unneeded': [unneeded],
                  'kept': {unneeded: 'they learn why above the line adds armor (they think less clearly, and stress '
                                     'chemistry makes the protein that may hold it), and how settled that is; the needed '
                                     'read listed only its bracket, which his 39a moved here, now one clause'}},
                 {'reader': reader('his-fixes', 'p033'), 'marked': marks('p033', HIS33, 'difference'), 'kept': {}},
                 {'reader': reader('fit', 'p033'), 'marked': marks('p033', FIT33, 'found'), 'kept': {}},
                 his_answer=[{'said': '39a', 'in': ' '.join(S.sentences(T.plain(T.NEW['p033']))[1:3]), 'words': {}}])


ALL = {'P030-P032': p030_032, 'P032': p032, 'P033': p033}

if __name__ == '__main__':
    bad = []
    for k in (sys.argv[1:] or list(ALL)):
        bad += ALL[k]()
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')
    sys.exit(1 if bad else 0)
