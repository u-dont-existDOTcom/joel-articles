"""The receipts for this turn's texts of mine (texts_x1127b), with x1126b's builder and the fresh reads of each paragraph
as it stood (x1126b/v1 for the one-sixteenth and practice paragraphs; x1127b/v1 for the "Underpinning" Principle and the
read of my new practice paragraph).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127b/build_receipts_x1127b.py KEY ...
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1126b'))
sys.path.insert(0, str(HERE))
import build_receipts_x1126b as RB  # noqa: E402
import texts_x1127b as T  # noqa: E402

B = RB.B
OUT = HERE / 'receipts'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
v1sw, rsw, SEC, WHO = RB.v1sw, RB.rsw, RB.SEC, RB.WHO


def sw19_step(name, text):
    """One step from my try 2 (#266): x1126b's receipt for it, with the Void sentence's new opening; from step 2 the
    last two sentences are one, joined with "so"."""
    joined = ', so gather a tribe' in text
    return B.build(
        name, text, SEC + ', after Perry\'s ratio of grown-ups to children', WHO + ', who lives mostly alone',
        {'That works out': ('they learn how far short of the grown-ups per child our brains evolved with we fall, about a '
                            'sixteenth, from Perry\'s ratio just before', 'it works out the ratio the paragraph before gives',
                            'That works out'),
         'So the emptiness': ('they learn the emptiness they may feel is that missing company, and that the guide calls it '
                              'the Void', 'it says what that shortfall feels like', 'So'),
         'And once you\'ve de-armored': ('they learn a lonely life will feel worse once the armor is off', 'it adds what '
                                         'the shortfall means after the protocol', 'And'),
         'So start gathering': ('they start gathering people they\'re close to and see most days, and know the armor '
                                'comes back without them', 'it gives the act the sentence before calls for', 'So'),
         'So gather a tribe': ('they gather people they\'re close to and see most days, and know the armor comes back '
                               'without them', 'it gives the act the sentence before calls for', 'So'),
         'I\'d gather': ('they gather people they\'re close to and see most days, and know the armor comes back '
                         'without them', 'it gives the act the sentence before calls for, as his judgment', 'none: the '
                         'act the before-and-after sentence calls for, said as his advice'),
         'Once you\'ve de-armored': (('they learn a lonely life will feel worse once the armor is off, so they gather '
                                      'people they\'re close to and see most days, and know the armor comes back without '
                                      'them') if joined else 'they learn a lonely life will feel worse once the armor is off',
                                     'it says what the shortfall means after the protocol' + (', and the act it calls for'
                                                                                              if joined else ''),
                                     'none: it turns from now to after de-armoring, which ' + ('its own "so" answers'
                                                                                             if joined else
                                                                                             'the next sentence answers')),
         'Gather a tribe': ('they gather people they\'re close to and see most days, and know the armor comes back '
                            'without them', 'it gives the act the sentence before calls for', 'Gather')},
        'they learn how little company modern life gives us, and what to do about it once they de-armor',
        [('about one-sixteenth of the grown-ups per child', 'Perry\'s ratio in the paragraph before (4 mature adults per '
          'child then, 1 immature adult per 4 children now) and his approved card SC-24 (Perry, 2023)', 'yes: they see '
          'the size of the shortfall', 'kept'),
         ('the Void', 'the guide\'s own term for the gray, empty state (Scenario C, Weeks 3 to 7)', 'yes: they know the '
          'emptiness has a name they will meet again', 'kept')],
        {'reader': rsw('needed', 'sw19'), 'unneeded': [v1sw('sw19', 2), v1sw('sw19', 4)], 'kept': {}},
        {'reader': rsw('his-fixes', 'sw19'),
         'marked': [{'s': v1sw('sw19', n), 'difference': d} for n, d in (
             (1, '4, 21, 11: "relational density" counts nothing; opens on the measure'),
             (2, '18, 12, 10: a short line tied to nothing; "Void" and "real" unexplained'),
             (3, '3, 14, 10, 27: "cannot simply return" corrects nobody; reads two ways'),
             (4, '5, 13, 21, 4, 15, 1, 10, 6: a rule with no act; labels; a wise-sounding end'))],
         'kept': {}},
        {'reader': rsw('fit', 'sw19'),
         'marked': [{'s': v1sw('sw19', 1), 'found': 'CAN\'T TELL what it counts; FROM: a number with no source said'},
                    {'s': v1sw('sw19', 3), 'found': 'CAN\'T TELL when it applies; MISREAD: life will be unbearable'},
                    {'s': v1sw('sw19', 4), 'found': 'CAN\'T TELL how many or how often; MISREAD: don\'t bother alone'}],
         'kept': {}},
        'his post\'s line, with his approved card SC-24\'s figure and source: we live on far less of the company our '
        'biology expects, the Void is real, a de-armored person can\'t go back to a lonely life, and without a tribe the '
        'armor comes back "just to survive the cold"',
        'after the Gibson and Perry paragraph, where the post has it')


if __name__ == '__main__':
    bad = []
    for k in sys.argv[1:]:
        if k.startswith('sw19-'):
            bad += sw19_step('SW19-' + k.split('-')[1].upper(), T.plain(T.STEP[k]))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


def v1sw23(n):
    return v1sw('sw23', n)


def sw2223(name, text):
    """The Anti-Breakthrough as it went in (P-SW22's step 2, Human High) with my new practice paragraph, as a pair (the
    practice paragraph is under 50 words)."""
    spec = {'The Anti-Breakthrough': ('they learn an alarmed brain can take in healing work for only seconds at a time, '
                                      'from Perry', 'the next idea of the section', None),
            'So for now we': ('they set aside the hour-long breakthrough for now, knowing why', 'it follows from the '
                              'seconds-long window', 'So'),
            'Instead, this protocol': ('they learn the protocol works in doses of seconds, and what micro-dosing means '
                                       'here', 'it gives the act the two before call for', 'Instead'),
            'In practice': ('they do 30 seconds of slow breathing, twenty times a day', 'it gives the daily practice the '
                            'doses of a few seconds come to', 'In practice'),
            'Each dose is': ('they do doses of 30 seconds of slow breathing, twenty a day', 'it says what each of the '
                             'doses of a few seconds is, and how many', 'Each dose')}
    if 'I\'d do 30 seconds' in text:
        spec['In practice'] = ('they do 30 seconds of slow breathing, twenty times a day, as his advice', 'it gives the '
                               'daily practice the doses of a few seconds come to', 'In practice')
    if 'to feel safe in your body' in text:
        spec['In practice'] = ('they do 30 seconds of slow breathing to feel safe in their body, twenty times a day',
                               'it gives the daily practice the doses of a few seconds come to, and what each is a dose '
                               'of', 'In practice')
    return B.build(
        name, text, SEC + ', the Anti-Breakthrough and the practice after it', WHO + ', used to hour-long therapy '
        'sessions', spec, 'they learn why the protocol works in seconds-long doses, and the daily practice',
        [('the window is often only seconds long', 'his post, from Perry', 'yes: they work in doses of seconds', 'kept'),
         ('an hour of trauma work overwhelms an armored nervous system', 'his post ("that is a flood, not a fix")',
          'yes: they set the hour-long session aside for now', 'kept'),
         ('30 seconds of breathing, twenty times a day', 'his post ("30 seconds of regulated breathing, twenty times a '
          'day")', 'yes: they breathe slowly and steadily for 30 seconds, twenty times a day', 'kept'),
         ('frequency beats intensity', 'his post ("Frequency beats intensity")', 'yes: they keep to short doses many times '
          'a day, the Anti-Breakthrough saying why and this sentence how many', 'kept')],
        {'reader': rsw('needed', 'sw22') + ' and x1126b/v1/needed/sw23/READ.md', 'unneeded': [v1sw('sw22', 2),
                                                                                         v1sw23(2)], 'kept': {}},
        {'reader': rsw('his-fixes', 'sw22') + ', x1126b/v1/his-fixes/sw23/READ.md, a fresh reader (Fable, 2026-11-27) of '
                   'my first draft of the practice paragraph (x1127b/v1/his-fixes/sw23n/READ.md), and the tell panel on my '
                   'second (x1127b/panel-pair2223/PANEL.md)',
         'marked': [{'s': v1sw('sw22', n), 'difference': d} for n, d in (
             (1, '11, 5, 13, 4, 21, 7: the source before the point; labels; no act'),
             (2, '3, 6, 18, 21, 8, 10, 4: "a flood, not a fix"; "metabolize ... processing"'),
             (3, '5, 9, 12, 8, 28, 4, 21, 10, 6, 7: the authority first; "therapeutic window" unexplained'))] +
                   [{'s': v1sw23(n), 'difference': d} for n, d in (
                       (1, '21, 13, 4: "Micro-Dosing Safety" a label; "regulated breathing" unexplained'),
                       (2, '3, 2, 21: "not a marathon; physical therapy" the not-X-Y turn'),
                       (3, '18, 6, 16: a three-word slogan at the end'))],
         'kept': {}},
        {'reader': rsw('fit', 'sw22') + ' and x1126b/v1/fit/sw23/READ.md',
         'marked': [{'s': v1sw('sw22', 1), 'found': 'MISREAD: "Micro-Dosing" as the drug doses; "abandon therapy"'},
                    {'s': v1sw('sw22', 2), 'found': 'CAN\'T TELL if it is me; MISREAD: my therapy hours harmed me'},
                    {'s': v1sw('sw22', 3), 'found': 'CAN\'T TELL what to do with seconds; FROM; MISREAD: a dose range'},
                    {'s': v1sw23(1), 'found': 'CAN\'T TELL the breathing pattern; MISREAD: microdosing drugs'}],
         'kept': {}},
        'his post\'s Anti-Breakthrough: give up the hour-long breakthrough for now; an armored nervous system can\'t take '
        'an hour of trauma work; Perry finds the window is often seconds long; and the goal, 30 seconds of breathing '
        'twenty times a day, frequency over intensity',
        'where the post has it, before Part 1')


if __name__ == '__main__' and 'pair2223s1' in sys.argv:
    bad = sw2223('SW22-23-4', T.pair_plain(T.OLD['sw22'], T.NEW['sw23-s1']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


if __name__ == '__main__' and 'pair2223' in sys.argv:
    bad = sw2223('SW22-23-3', T.pair_plain(T.OLD['sw22'], T.NEW['sw23']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


def sw19_rewrite(name, text):
    """The rewrite after the near-miss steps were spent (#312, #314), from the reads of the paragraph as it stood, the
    tell panel, and the fresh read of my first rewrite."""
    return B.build(
        name, text, SEC + ', after Perry\'s ratio of grown-ups to children', WHO + ', who lives mostly alone',
        {'So a child today': ('they learn a child today gets about a sixteenth of the grown-ups a child had when our brains '
                              'evolved, from Perry\'s ratio just before', 'it works out the ratio the paragraph before gives',
                              'So'),
         'If you often feel empty': ('they learn the emptiness they may feel is real and what it is, and that the guide '
                                     'calls it the Void', 'it says what that shortfall feels like', 'none: it turns from '
                                     'the child to the reader, whose feeling it names'),
         'That loneliness is': ('they learn the armor has been numbing that loneliness, so a lonely life will hurt more '
                                'once it is off', 'it says what the shortfall means after de-armoring, and why', 'That '
                                'loneliness'),
         'So I\'d find': ('they find people they\'re close to and see most days, and know the armor comes back without '
                          'them', 'it gives the act the sentence before calls for, as his advice', 'So')},
        'they learn how little company modern life gives us, and what to do about it once they de-armor',
        [('about one-sixteenth of the grown-ups per child', 'Perry\'s ratio in the paragraph before (4 mature adults per '
          'child then, 1 immature adult per 4 children now) and his approved card SC-24 (Perry, 2023)', 'yes: they see '
          'the size of the shortfall', 'kept'),
         ('the Void', 'the guide\'s own term for the gray, empty state (Scenario C, Weeks 3 to 7)', 'yes: they know the '
          'emptiness has a name they will meet again', 'kept'),
         ('the armor has been numbing the loneliness', 'his post: without a tribe the brain reaches for the armor again '
          '"just to survive the cold"', 'yes: they see why a lonely life hurts more once the armor is off', 'kept')],
        {'reader': rsw('needed', 'sw19'), 'unneeded': [v1sw('sw19', 2), v1sw('sw19', 4)], 'kept': {}},
        {'reader': rsw('his-fixes', 'sw19') + ', the tell panel on my step 1 (x1127b/panel-sw19-s1/PANEL.md), and a fresh '
                   'reader (Fable, 2026-11-27) of my first rewrite (x1127b/v1/his-fixes/sw19r1/READ.md)',
         'marked': [{'s': v1sw('sw19', n), 'difference': d} for n, d in (
             (1, '4, 21, 11: "relational density" counts nothing; opens on the measure'),
             (2, '18, 12, 10: a short line tied to nothing; "Void" and "real" unexplained'),
             (3, '3, 14, 10, 27: "cannot simply return" corrects nobody; reads two ways'),
             (4, '5, 13, 21, 4, 15, 1, 10, 6: a rule with no act; labels; a wise-sounding end'))],
         'kept': {}},
        {'reader': rsw('fit', 'sw19'),
         'marked': [{'s': v1sw('sw19', 1), 'found': 'CAN\'T TELL what it counts; FROM: a number with no source said'},
                    {'s': v1sw('sw19', 3), 'found': 'CAN\'T TELL when it applies; MISREAD: life will be unbearable'},
                    {'s': v1sw('sw19', 4), 'found': 'CAN\'T TELL how many or how often; MISREAD: don\'t bother alone'}],
         'kept': {}},
        'his post\'s line, with his approved card SC-24\'s figure and source: we live on far less of the company our '
        'biology expects, the Void is real, a de-armored person can\'t go back to a lonely life, and without a tribe the '
        'armor comes back to survive the loneliness ("just to survive the cold")',
        'after the Gibson and Perry paragraph, where the post has it')


if __name__ == '__main__' and 'sw19r' in sys.argv:
    bad = sw19_rewrite('SW19-R1', T.plain(T.STEP['sw19-r1']))
    bad += sw2223('SW22-23-5', T.pair_plain(T.OLD['sw22'], T.NEW['sw23-s2']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


if __name__ == '__main__' and 'last' in sys.argv:
    bad = sw2223('SW22-23-6', T.pair_plain(T.OLD['sw22'], T.NEW['sw23-s3']))
    bad += sw19_step('SW19-S4', T.plain(T.STEP['sw19-s4']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


if __name__ == '__main__' and 's5' in sys.argv:
    bad = sw19_step('SW19-S5', T.plain(T.STEP['sw19-s5']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


if __name__ == '__main__' and 's6' in sys.argv:
    bad = sw19_step('SW19-S6', T.plain(T.STEP['sw19-s6']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


if __name__ == '__main__' and 's7' in sys.argv:
    bad = sw19_step('SW19-S7', T.plain(T.STEP['sw19-s7']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


if __name__ == '__main__' and 's8' in sys.argv:
    bad = sw19_step('SW19-S8', T.plain(T.STEP['sw19-s8']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


def sw23_alone(name, text):
    """The practice sentence by itself, as the card's box would put it in (its checks were with the Anti-Breakthrough
    before it, the pair: the receipt of the pair is SW22-23-6)."""
    return B.build(
        name, text, SEC + ', the practice after the Anti-Breakthrough', WHO + ', used to hour-long therapy sessions',
        {'In practice': ('they do 30 seconds of slow breathing, twenty times a day, as his advice', 'it gives the daily '
                         'practice the doses of a few seconds just named come to', 'In practice')},
        'they learn what they do each day: the doses of a few seconds come to 30 seconds of slow breathing, twenty times '
        'a day',
        [('30 seconds of breathing, twenty times a day', 'his post ("30 seconds of regulated breathing, twenty times a '
          'day")', 'yes: they breathe slowly for 30 seconds, twenty times a day', 'kept'),
         ('frequency beats intensity', 'his post ("Frequency beats intensity")', 'yes: they keep to short doses many '
          'times a day, the Anti-Breakthrough before it saying why', 'kept')],
        {'reader': 'x1126b/v1/needed/sw23/READ.md', 'unneeded': [v1sw23(2)], 'kept': {}},
        {'reader': 'x1126b/v1/his-fixes/sw23/READ.md, x1127b/v1/his-fixes/sw23n/READ.md and x1127b/panel-pair2223/PANEL.md',
         'marked': [{'s': v1sw23(n), 'difference': d} for n, d in (
             (1, '21, 13, 4: "Micro-Dosing Safety" a label; "regulated breathing" unexplained'),
             (2, '3, 2, 21: "not a marathon; physical therapy" the not-X-Y turn'),
             (3, '18, 6, 16: a three-word slogan at the end'))],
         'kept': {}},
        {'reader': 'x1126b/v1/fit/sw23/READ.md',
         'marked': [{'s': v1sw23(1), 'found': 'CAN\'T TELL the breathing pattern; MISREAD: microdosing drugs'}],
         'kept': {}},
        'his post\'s goal: 30 seconds of regulated breathing, twenty times a day, frequency over intensity',
        'after the Anti-Breakthrough, where the post has it')


if __name__ == '__main__' and 'cards' in sys.argv:
    bad = sw19_step('SW19-S7-CARD', T.STEP['sw19-s7'])
    bad += sw23_alone('SW23-S3-CARD', T.NEW['sw23-s3'])
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')



def v1sw21(n):
    """The underpinnings paragraph's sentences as its reads had them (x1126b/v1/*/sw21/TEXT.txt)."""
    return B.S.sentences((HERE.parent / 'x1126b' / 'v1' / 'his-fixes' / 'sw21' / 'TEXT.txt').read_text(encoding='utf-8')
                         .strip())[n - 1]


STEP21 = ('unchanged in this step: the paragraph read with a Human window (#263), so its changes go a word or two a '
          'check (the ledger\'s near-miss rule), and this sentence\'s rewrite from the reads comes after two such steps')


def sw21_step(name, text, changed):
    """A step from his card version (#263). CHANGED: the numbers of the reads' sentences this step rewords."""
    kept_h = {v1sw21(n): STEP21 for n in (1, 2) if n not in changed}
    return B.build(
        name, text, SEC + ', after the role-self paragraph', WHO,
        {'Neurological De-Armoring': ('they learn the protocol works on what their mind stands on, not on the thoughts '
                                      'above it', 'the section\'s point, said as the house', None),
         'It\'s a protocol': ('they learn what the protocol does to the brainstem and why it comes before the psychology',
                              'it says how the foundation gets fixed', 'It\'s')},
        'they learn the protocol works on the brain\'s foundation before the psychology',
        [('HDAC inhibition', 'the article\'s section C ("The ketone BHB blocks enzymes called HDACs", Shimazu 2013)',
          'yes: they learn the ketones do the softening, which section C explains', 'kept'),
         ('Ketones (BHB)', 'the protocol\'s BHB supplements and keto diet (the science sections)', 'yes: they know the '
          'ketones are part of what they take', 'kept')],
        {'reader': rsw('needed', 'sw21'), 'unneeded': [v1sw21(2)],
         'kept': {v1sw21(2): ('the reader needs its job, the only sentence that says what the protocol does to the brain '
                              '(the needed read listed it for its words, not its job); its words are the next steps\'')}},
        {'reader': rsw('his-fixes', 'sw21'),
         'marked': [{'s': v1sw21(1), 'difference': '3, 4, 21, 16: "X, not Y"; underpinnings of what; a label; said again '
                                                    'in S2'},
                    {'s': v1sw21(2), 'difference': '1, 4, 10, 11, 13, 21, 8: one chain carrying four pictures; terms '
                                                    'unexplained; which does what; the means first'}],
         'kept': kept_h},
        {'reader': rsw('fit', 'sw21'),
         'marked': [{'s': v1sw21(2), 'found': 'CAN\'T TELL what HDAC inhibition and glutamate modulation are or what the '
                                               'concrete is; FROM: textbook terms; MISREAD: dissolving my brain'}],
         'kept': {v1sw21(2): STEP21} if 2 not in changed else {}},
        'his card version of 2026-11-03: the protocol fixes the foundation, not the decor; it softens what has set hard in '
        'the brainstem with glutamate modulation and ketones (BHB, which block HDACs), so a new foundation can go in and '
        'the psychological work can follow',
        'after the role-self paragraph, where his card version has it')


if __name__ == '__main__' and 'sw21s1' in sys.argv:
    bad = sw21_step('SW21-S1', T.plain(T.STEP['sw21-s1']), (1,))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')


if __name__ == '__main__' and 'sw21s2' in sys.argv:
    bad = sw21_step('SW21-S2', T.plain(T.STEP['sw21-s2']), (2,))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')



def sw21_rewrite(name, text):
    """The rewrite after the two small steps from his version (#323, #324), from the reads of his version, the panel
    on step 2 and the fresh read of my first rewrite."""
    return B.build(
        name, text, SEC + ', after the role-self paragraph', WHO,
        {'In Perry\'s picture': ('they learn the protocol works on the brainstem, the foundation in Perry\'s house, before '
                                 'the psychology upstairs', 'it names the picture the section began with', 'none: it '
                                 'turns from why the protocol was built to what it works on, in the section\'s picture'),
         'Trauma leaves that': ('they learn what is wrong with that foundation and how the protocol softens it, with what '
                                'each part does', 'it says what the protocol does to the foundation', 'none: it says what '
                                'is wrong with the foundation the sentence before named'),
         'Then we can': ('they learn the old concrete comes out and a new foundation goes in, and the psychology comes '
                         'after', 'it gives what the softening is for', 'Then')},
        'they learn what the protocol does to the brain, in the house picture, before the psychology',
        [('HDACs, which BHB blocks, can keep new learning from sticking', 'the article\'s section C ("The ketone BHB '
          'blocks enzymes called HDACs", Shimazu 2013; an HDAC blocker made new learning last in mice, Whittle & '
          'Singewald 2014)', 'yes: they learn why the ketone is in the protocol', 'kept'),
         ('calming glutamate', 'the protocol\'s glutamate shield (Part 3) and section B', 'yes: they learn the other half '
          'of what the protocol does to the brainstem', 'kept'),
         ('the brainstem as the foundation of Perry\'s house', 'the section\'s second paragraph (Perry compares treating '
          'trauma to building a house; the foundation is the brainstem)', 'yes: they hold one picture through the '
          'paragraph', 'kept')],
        {'reader': rsw('needed', 'sw21'), 'unneeded': [v1sw21(2)],
         'kept': {v1sw21(2): 'the reader needs its job, what the protocol does to the brain, now in the house picture'}},
        {'reader': rsw('his-fixes', 'sw21') + ', the tell panel on step 2 (x1127b/panel-sw21-s2/PANEL.md), and a fresh '
                   'reader (Fable, 2026-11-27) of my first rewrite (x1127b/v1/his-fixes/sw21r1/READ.md)',
         'marked': [{'s': v1sw21(1), 'difference': '3, 4, 21, 16: "X, not Y"; underpinnings of what; a label; said again '
                                                    'in S2'},
                    {'s': v1sw21(2), 'difference': '1, 4, 10, 11, 13, 21, 8: one chain carrying four pictures; terms '
                                                    'unexplained; which does what; the means first'}],
         'kept': {}},
        {'reader': rsw('fit', 'sw21'),
         'marked': [{'s': v1sw21(2), 'found': 'CAN\'T TELL what HDAC inhibition and glutamate modulation are or what the '
                                               'concrete is; FROM: textbook terms; MISREAD: dissolving my brain'}],
         'kept': {}},
        'his card version of 2026-11-03: the protocol fixes the foundation, not the decor; it softens what has set hard in '
        'the brainstem with glutamate modulation and ketones (BHB, which block HDACs), so a new foundation can go in and '
        'the psychological work can follow',
        'after the role-self paragraph, where his card version has it')


if __name__ == '__main__' and 'sw21r' in sys.argv:
    bad = sw21_rewrite('SW21-R1', T.plain(T.STEP['sw21-r1']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')



if __name__ == '__main__' and 'sw21s3' in sys.argv:
    bad = sw21_step('SW21-S3', T.plain(T.STEP['sw21-s3']), (2,))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')



def v1sw17(n):
    return B.S.sentences((HERE / 'v1' / 'his-fixes' / 'sw17' / 'TEXT.txt').read_text(encoding='utf-8').strip())[n - 1]


STEP17 = ('unchanged in this step: the pair read with Human windows (#260), so its changes go a word or two a check (the '
          'ledger\'s near-miss rule); this sentence\'s fix from the reads comes in the next steps')


JOINED17 = ('its words are kept in this step, with the curtains line joined to it: the pair read with Human windows, so '
            'its changes go a word or two a check (the ledger\'s near-miss rule), and its two glosses come next')


def pair1718(name, text):
    """A step of the "Underpinning" Principle with the Gibson paragraph after it (the Principle is under 50 words)."""
    spec = {'The "Underpinning" Principle': ('they learn Perry compares treating trauma to building a house', 'the '
                                            'section\'s second point: why therapy aimed at thoughts can fail', None),
            'Standard CBT': ('they learn thought-aimed therapies work on the cortex while the brainstem, the foundation, '
                             'is damaged' + (', and that the foundation comes first' if 'and you can\'t hang' in text
                                             else ''), 'it says what the house picture means for therapy', 'none: it '
                             'fills in the picture the sentence before names'),
            'You cannot hang curtains': ('they learn the foundation comes first', 'it says what follows from the picture',
                                         'none: it draws the picture\'s consequence'),
            'Why does the brain build this armor?': ('they ask where the armor comes from', 'the next part of the section, '
                                                    'under its own heading', 'none: a new part of the section'),
            'Psychologist Lindsay Gibson explains': ('they learn children of emotionally immature parents build a '
                                                     'Role-Self to please and manage them', 'it answers the question',
                                                     'none: it answers the question before it'),
            'But we can\'t just blame': ('they learn their parents aren\'t the whole cause', 'it turns from the parents '
                                         'to the society', 'But'),
            'It really is true what they say': ('they learn the saying that it takes a village', 'it says what the '
                                               'parents were missing', 'none: it gives the saying the sentence before '
                                               'leads to'),
            'The modern large society': ('they learn one or two caregivers aren\'t enough', 'it says how modern life '
                                         'falls short of the village', 'none: it applies the saying to now'),
            'As Bruce Perry explains': ('they learn the ratio our brains evolved with, 4 adults to a child', 'it gives the '
                                        'number behind the village', 'As'),
            'Today, our': ('they learn today\'s ratio, 1 immature adult to 4 children', 'it gives the number for now',
                           'Today')}
    marked = {1: '4, 10, 11, 13: the source before the point; "Underpinning" unexplained',
              2: '1, 2, 4, 21: two glosses at the same place; category words; therapies doing the act',
              3: '6, 18, 16: a short wise-sounding line saying S2 again'}
    return B.build(
        name, text, SEC + ', the "Underpinning" Principle and the Gibson paragraph after it', WHO, spec,
        'they learn why therapy aimed at thoughts can fail while the brain\'s foundation is damaged',
        [('Perry compares treating trauma to building a house', 'his post, from Perry', 'yes: they hold the picture the '
          'section uses', 'kept'),
         ('4 mature adults to 1 child then, 1 immature adult to 4 children now', 'his post, from Perry (his approved card '
          'SC-24, Perry 2023)', 'yes: they see how far short modern life falls', 'kept')],
        {'reader': 'a fresh reader (Fable, 2026-11-27) given tools/humanization/needed_read_brief.md and only the '
                   'Principle as it stood (x1127b/v1/needed/sw17/READ.md)', 'unneeded': [], 'kept': {}},
        {'reader': 'a fresh reader (Fable, 2026-11-27) given tools/humanization/his_fixes_brief.md and only the Principle '
                   'as it stood (x1127b/v1/his-fixes/sw17/READ.md)',
         'marked': [{'s': v1sw17(n), 'difference': d} for n, d in marked.items()],
         'kept': ({v1sw17(2): JOINED17} if 'and you can\'t hang' in text else {v1sw17(n): STEP17 for n in (2, 3)})},
        {'reader': 'a fresh reader (Fable, 2026-11-27) given tools/humanization/fit_read_brief.md and only the Principle '
                   'as it stood (x1127b/v1/fit/sw17/READ.md)',
         'marked': [{'s': v1sw17(2), 'found': 'CAN\'T TELL how I\'d know my brainstem is crumbling; FROM: EMDR is not '
                                               'thought work; MISREAD: brain damage, my therapy wasted'},
                    {'s': v1sw17(3), 'found': 'MISREAD: therapy is pointless until the body is fixed'}],
         'kept': ({v1sw17(2): JOINED17} if 'and you can\'t hang' in text else {v1sw17(n): STEP17 for n in (2, 3)})},
        'his post: Perry\'s house, therapies that decorate while the foundation crumbles; why the brain builds armor '
        '(Gibson\'s Role-Self), the village, and Perry\'s ratios',
        'where the post has them')


if __name__ == '__main__' and 'sw17s1' in sys.argv:
    bad = pair1718('SW17-18-S1', T.pair_plain(T.STEP['sw17-s1'], T.STEP['sw18-s1']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')



if __name__ == '__main__' and 'sw17s2' in sys.argv:
    bad = pair1718('SW17-18-S2', T.pair_plain(T.STEP['sw17-s2'], T.STEP['sw18-s1']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')



def pair1617(name, text):
    """The Principle as step 2 has it, with the paragraph before it (his own version of 2026-11-06, Human High by itself,
    #259); the Principle is under 50 words."""
    spec = {'Have you done years': ('they ask whether years of therapy have left them still triggered', 'the section\'s '
                                    'opening question, to the reader', None),
            'One reason to think about': ('they learn therapy rewrites the code while the motherboard is overheating or '
                                          'damaged', 'it answers the question', 'none: it answers the question before it'),
            'So to address that': ('they learn the protocol goes after five problems in the brain before, or alongside, '
                                   'the psychology', 'it gives what the protocol does about it', 'So'),
            'The "Underpinning" Principle': ('they learn Perry compares treating trauma to building a house', 'the same '
                                            'point in Perry\'s picture', 'none: the Principle\'s label opens it, the same '
                                            'point in another picture'),
            'Standard CBT': ('they learn thought-aimed therapies work on the cortex while the brainstem, the foundation, '
                             'is damaged, and that the foundation comes first', 'it says what the house picture means for '
                             'therapy', 'none: it fills in the picture the sentence before names')}
    return B.build(
        name, text, SEC + ', its first paragraph and the "Underpinning" Principle', WHO, spec,
        'they ask whether years of therapy have left them still triggered, and learn why that can happen',
        [('Perry compares treating trauma to building a house', 'his post, from Perry', 'yes: they hold the picture the '
          'section uses', 'kept'),
         ('5 specific neuro-biological problems', 'his version of 2026-11-06 (A to E below)', 'yes: they follow the link to '
          'the five problems, A to E, that come next', 'kept')],
        {'reader': 'a fresh reader (Fable, 2026-11-27) given tools/humanization/needed_read_brief.md and only the '
                   'Principle as it stood (x1127b/v1/needed/sw17/READ.md)', 'unneeded': [], 'kept': {}},
        {'reader': 'a fresh reader (Fable, 2026-11-27) given tools/humanization/his_fixes_brief.md and only the Principle '
                   'as it stood (x1127b/v1/his-fixes/sw17/READ.md)',
         'marked': [{'s': v1sw17(n), 'difference': d} for n, d in (
             (1, '4, 10, 11, 13: the source before the point; "Underpinning" unexplained'),
             (2, '1, 2, 4, 21: two glosses at the same place; category words; therapies doing the act'),
             (3, '6, 18, 16: a short wise-sounding line saying S2 again'))],
         'kept': {v1sw17(2): JOINED17}},
        {'reader': 'a fresh reader (Fable, 2026-11-27) given tools/humanization/fit_read_brief.md and only the Principle '
                   'as it stood (x1127b/v1/fit/sw17/READ.md)',
         'marked': [{'s': v1sw17(2), 'found': 'CAN\'T TELL how I\'d know my brainstem is crumbling; FROM: EMDR is not '
                                               'thought work; MISREAD: brain damage, my therapy wasted'},
                    {'s': v1sw17(3), 'found': 'MISREAD: therapy is pointless until the body is fixed'}],
         'kept': {v1sw17(2): JOINED17}},
        'his version of the section\'s first paragraph (2026-11-06), and his post\'s Principle: Perry\'s house, therapies '
        'that decorate while the foundation crumbles',
        'where the post has them')


if __name__ == '__main__' and 'sw1617' in sys.argv:
    bad = pair1617('SW16-17-S2', T.pair_plain(T.OLD['sw16'], T.STEP['sw17-s2']))
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')
