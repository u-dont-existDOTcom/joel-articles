"""The receipts for x1123b's tries (texts_x1123b): AGM4, the agmatine stop-signs paragraph with his lasting-anhedonia
warning, and LMA5, the lion's mane and ashwagandha item. The reads are reads-agm3.md and reads-lma4.md (fresh Fable
readers given needed_read_brief.md, his_fixes_brief.md and fit_read_brief.md, of AGM3 and LMA4), and the tell panel on
LMA3 (panel-lma3); every sentence they marked is changed in AGM4 and LMA5. Sources: x1122a/WARNINGS-SOURCES.md.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123b/build_receipts_x1123b.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE))
import build_receipts_x1123a as B  # noqa: E402
import texts_x1123b as T  # noqa: E402

B.HERE = HERE


def fill(r, spec):
    """B.fill, with a link of "none: why" allowed (a question the sentence before sets up)."""
    for x in r['sentences']:
        if x.get('his'):
            continue
        (k,) = [k for k in spec if x['s'].startswith(k)]
        x['payoff'], x['follows'] = spec[k][0], spec[k][1]
        if 'link' in x:
            link = spec[k][2]
            assert link and (link.startswith('none:') or link in x['s']), (k, link)
            x['link'] = link


B.fill = fill
S = B.S
SRC = B.SRC


def reader(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-23) given tools/humanization/%s and only the text, one sentence a line, of the '
            'try before this one (x1123b/reads-%s.md)' % (brief, key))


def main():
    bad = []
    a3 = S.sentences(T.AGM3)
    bad += B.build(
        'AGM4', T.AGM4, 'Agmatine Warning (The Voltage Governor), the stop line: the one full list of its stop signs (his 35a)',
        'an adult with trauma about to try agmatine for glutamate storms, reading its warning to decide what would make '
        'them stop',
        {'Agmatine can leave you flat': ('they learn agmatine itself can leave them flat and numb, which users report even '
                                         'though the trials missed it, so they watch for it from the start',
                                         'it opens the stop line on the side effect the rest is about, after the '
                                         'precautions', None),
         'So stop it right away': ('they learn which changes in mood, against how they were before starting, mean '
                                   'stopping now', 'it gives the act the warning before it calls for',
                                   'So stop it right away'),
         'Stop too if it winds': ('they learn the other side effects that mean stopping too, each as they would notice it',
                                  'it adds the other kind of sign after the mood ones', 'Stop too if'),
         "It's natural to want": ('they learn not to wait the numbness out, since in rare reports it went on for weeks '
                                  'after stopping, so they stop at the first sign', 'it answers the wish to wait, which '
                                  'the stop rule before it leaves open', "It's natural to want")},
        'they learn at once that agmatine itself can leave them flat and numb, a state they would recognize, so they read '
        'on for when to stop',
        [('rare reports of anhedonia lasting weeks after stopping agmatine',
          'trials report only stomach upset (Shopsin 2013); emotional dullness while taking it is reported in nootropic '
          'summaries; weeks after stopping is his finding (' + SRC + ')',
          'yes: they learn the numbness can last after stopping, so they stop at the first sign', 'kept')],
        {'reader': reader('needed', 'agm3'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'agm3'),
         'marked': [{'s': a3[0], 'difference': '13, 19, 2'}, {'s': a3[1], 'difference': '1, 2, 19, 4'},
                    {'s': a3[2], 'difference': '9, 11, 1, 10, 4, 16, 14'}], 'kept': {}},
        {'reader': reader('fit', 'agm3'),
         'marked': [{'s': a3[0], 'found': 'anyway, can\'t tell: a numb reader\'s baseline swings'},
                    {'s': a3[1], 'found': 'anyway, can\'t tell; misread: cravings assume quitting, and being wound up '
                                          'reads backwards for a calming tool'},
                    {'s': a3[2], 'found': 'misread: the trials clause reassures first; "rare" read as "not me"'}],
         'kept': {}},
        'read the warnings from the Agmatine Warning to the next item for agmatine\'s stop signs: this is the one list; the '
        'cycle rule in the Glutamate Shield and Weeks 1-2 point to it (his 35a)',
        'the Agmatine Warning\'s stop line, after its precautions; the one full list of its stop signs, which the cycle '
        'rule and Weeks 1-2 point to')
    l4 = S.sentences(T.LMA4)
    bad += B.build(
        'LMA5', T.LMA5, 'A Complete Guide to Bio-De-Armoring, the warnings: a new item after the Cognitive Warning',
        'an adult with trauma reading the warnings at the top before starting, who may already take lion\'s mane or '
        'ashwagandha, or be thinking of adding them for focus or stress',
        {'Lion\'s Mane & Ashwagandha:': ('they learn he would leave both out of the protocol, and why: rare reports of '
                                         'anhedonia, explained where the article first uses it, or sexual dysfunction '
                                         'lasting after stopping', 'it is the next item of the warnings, the first about '
                                         'supplements the protocol doesn\'t use', None),
         'Lasting effects like these': ('they learn how rare it is, and that the same lasting harm is a known risk with '
                                        'SSRIs and finasteride (his point in his message), so they weigh the reports '
                                        'without alarm', 'it weighs the reports the sentence before gives',
                                        'Lasting effects like these')},
        'they learn the protocol leaves out two popular supplements they may be taking or considering, and why',
        [('rare reports of lasting anhedonia and sexual dysfunction after lion\'s mane and ashwagandha',
          'no trial or case report found; trials report mostly mild side effects; the reports are community ones (his '
          'finding), as ' + SRC + ' says', 'yes: they learn to leave both out, from reports said as reports', 'kept'),
         ('lasting sexual dysfunction is a known risk after SSRIs and finasteride',
          'the EMA recognized lasting sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems '
          'continuing after stopping to finasteride\'s labels in 2011 and 2012 (' + SRC + ')',
          'yes: they learn the kind of harm the reports describe is a known risk with drugs, so they take it seriously',
          'kept')],
        {'reader': reader('needed', 'lma4'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'lma4') + ', and the tell panel on LMA3 (x1123b/panel-lma3/PANEL.md)',
         'marked': [{'s': l4[0], 'difference': '4'}, {'s': l4[1], 'difference': '10, 1, 12'}], 'kept': {}},
        {'reader': reader('fit', 'lma4'),
         'marked': [{'s': l4[0], 'found': 'can\'t tell: stop now, or only not add them'},
                    {'s': l4[1], 'found': 'anyway, can\'t tell: from the herb or the trauma; misread: the SSRI comparison '
                                          'as a flat statement'}],
         'kept': {}},
        'read the section from its heading to the next for lion\'s mane and ashwagandha: no other item names them, and the '
        'article advises neither anywhere (checked 2026-11-22)',
        'a new item of the warnings at the top, after the Cognitive Warning and before the Agmatine Warning, so its '
        '"anhedonia" is the article\'s first and is said in plain words there')
    print('\n'.join(bad) or 'receipts PASS')


def second():
    """AGM6 and LMA7: their read against his fixes is of AGM5 and LMA6 (reads-agm5-lma6.md); the needed and fit reads
    are of AGM3 and LMA4, whose points these keep."""
    bad = []
    a5 = S.sentences(T.AGM5)
    q = 'none: one of the checks the sentence before it says to make, asked as the reader would ask it'
    bad += B.build(
        'AGM6', T.AGM6, 'Agmatine Warning (The Voltage Governor), the stop line: the one full list of its stop signs (his 35a)',
        'an adult with trauma about to try agmatine for glutamate storms, reading its warning to decide what would make '
        'them stop',
        {'Agmatine can leave you flat': ('they learn agmatine itself can leave them flat and numb, which users report even '
                                         'though the trials missed it, so they watch for it', 'it opens the stop line on '
                                         'the side effect the rest is about, after the precautions', None),
         'So keep checking yourself': ('they learn to judge each sign against how they were before starting, since their '
                                       'trauma already brings some of them', 'it says what to do about the side effect '
                                       'it follows', 'So keep checking yourself'),
         'Am I flatter': ('they check the mood signs: flatter or more depressed, no pleasure, not caring', 'the first check',
                          q),
         'Am I more irritable': ('they check the signs of being wound up: irritable, sleeping worse', 'the next check', q),
         'Do I have dizziness': ('they check the body signs: dizziness, palpitations, nausea, loose stools', 'the next '
                                 'check', q),
         "And if you're quitting": ('they check the cravings, if they are quitting something', 'the last check, for the '
                                    'readers it applies to', "And if you're quitting"),
         'If the answer to any': ('they learn to stop agmatine at any yes, and not to wait the numbness out, since in rare '
                                  'reports it lasted weeks after stopping', 'it gives the act the checks lead to',
                                  'If the answer to any')},
        'they learn at once that agmatine itself can leave them flat and numb, a state they would recognize, so they read '
        'on for when to stop',
        [('rare reports of anhedonia lasting weeks after stopping agmatine',
          'trials report only stomach upset (Shopsin 2013); emotional dullness while taking it is reported in nootropic '
          'summaries; weeks after stopping is his finding (' + SRC + ')',
          'yes: they learn the numbness can last after stopping, so they stop at the first sign', 'kept')],
        {'reader': reader('needed', 'agm3'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'agm5-lma6'),
         'marked': [{'s': a5[i], 'difference': d} for i, d in ((1, '23'), (2, '19'), (3, '8, 3'), (4, '1, 4, 25'),
                                                               (5, '10'), (6, '16, 7'))], 'kept': {}},
        {'reader': reader('fit', 'agm3'), 'marked': [], 'kept': {}},
        'read the warnings from the Agmatine Warning to the next item for agmatine\'s stop signs: this is the one list; the '
        'cycle rule in the Glutamate Shield and Weeks 1-2 point to it (his 35a)',
        'the Agmatine Warning\'s stop line, after its precautions; the one full list of its stop signs, which the cycle '
        'rule and Weeks 1-2 point to')
    l6 = S.sentences(T.LMA6)
    bad += B.build(
        'LMA7', T.LMA7, 'A Complete Guide to Bio-De-Armoring, the warnings: a new item after the Cognitive Warning',
        'an adult with trauma reading the warnings at the top before starting, who may already take lion\'s mane or '
        'ashwagandha, or be thinking of adding them for focus or stress',
        {'Lion\'s Mane & Ashwagandha:': ('they learn he isn\'t advising either, though many take them, so they leave '
                                         'them out', 'it is the next item of the warnings, the first about supplements '
                                         'the protocol doesn\'t use', None),
         "That's because": ('they learn why: rare reports of anhedonia, explained where the article first uses it, and '
                            'sexual dysfunction lasting after stopping, and the name people give it', 'it gives the reason '
                            'for the stance before it', "That's because"),
         'The same thing is': ('they learn the same lasting harm is a known risk with two drugs, so they take the reports '
                               'seriously', 'it weighs the reports the sentence before gives', 'The same thing is')},
        'they learn the protocol leaves out two popular supplements they may be taking or considering, and why',
        [('rare reports of lasting anhedonia and sexual dysfunction after lion\'s mane and ashwagandha',
          'no trial or case report found; trials report mostly mild side effects; the reports are community ones (his '
          'finding), as ' + SRC + ' says', 'yes: they learn to leave both out, from reports said as reports', 'kept'),
         ('lasting sexual dysfunction is a known risk after SSRIs and finasteride',
          'the EMA recognized lasting sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems '
          'continuing after stopping to finasteride\'s labels in 2011 and 2012 (' + SRC + ')',
          'yes: they learn the kind of harm the reports describe is a known risk with drugs, so they take it seriously',
          'kept')],
        {'reader': reader('needed', 'lma4'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'agm5-lma6'),
         'marked': [{'s': l6[1], 'difference': '12, 13, 9, 10'}, {'s': l6[2], 'difference': '10, 7, 4, 8, 12'}],
         'kept': {}},
        {'reader': reader('fit', 'lma4'), 'marked': [], 'kept': {}},
        'read the section from its heading to the next for lion\'s mane and ashwagandha: no other item names them, and the '
        'article advises neither anywhere (checked 2026-11-22)',
        'a new item of the warnings at the top, after the Cognitive Warning and before the Agmatine Warning, so its '
        '"anhedonia" is the article\'s first and is said in plain words there')
    print('\n'.join(bad) or 'receipts 2 PASS')


def third():
    """AGM7 and LMA8: the reads are the tell panels on AGM6 and LMA3 and the reads against his fixes of AGM5 and LMA6;
    the needed and fit reads of AGM3 and LMA4, whose points these keep."""
    bad = []
    a6 = S.sentences(T.AGM6)
    bad += B.build(
        'AGM7', T.AGM7, 'Agmatine Warning (The Voltage Governor), the stop line: the one full list of its stop signs (his 35a)',
        'an adult with trauma about to try agmatine for glutamate storms, reading its warning to decide what would make '
        'them stop',
        {'Agmatine can leave you flat': ('they learn agmatine can leave them flat and numb, which users get though the trials '
                                         'missed it, and the mood changes, against before they started, that mean stopping '
                                         'now', 'it opens the stop line on the side effect the rest is about, after the '
                                         'precautions', None),
         'Same if it winds': ('they learn the other side effects that mean stopping too', 'it adds the other signs to the '
                              'first ones', 'Same if'),
         'Unfortunately a few': ('they learn the numbness can last weeks after stopping, so they don\'t wait it out',
                                 'it gives the reason not to wait, after the signs', 'Unfortunately')},
        'they learn at once that agmatine itself can leave them flat and numb, a state they would recognize, and when to stop',
        [('rare reports of anhedonia lasting weeks after stopping agmatine',
          'trials report only stomach upset (Shopsin 2013); emotional dullness while taking it is reported in nootropic '
          'summaries; weeks after stopping is his finding (' + SRC + ')',
          'yes: they learn the numbness can last after stopping, so they stop at the first sign', 'kept')],
        {'reader': reader('needed', 'agm3'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'agm5-lma6') + ', and the tell panel on AGM6 (x1123b/panel-agm6/PANEL.md)',
         'marked': [{'s': a6[i], 'difference': 'panel'} for i in (0, 1, 2, 3, 4, 6)], 'kept': {}},
        {'reader': reader('fit', 'agm3'), 'marked': [], 'kept': {}},
        'read the warnings from the Agmatine Warning to the next item for agmatine\'s stop signs: this is the one list; the '
        'cycle rule in the Glutamate Shield and Weeks 1-2 point to it (his 35a)',
        'the Agmatine Warning\'s stop line, after its precautions; the one full list of its stop signs, which the cycle '
        'rule and Weeks 1-2 point to')
    l6 = S.sentences(T.LMA6)
    bad += B.build(
        'LMA8', T.LMA8, 'A Complete Guide to Bio-De-Armoring, the warnings: a new item after the Cognitive Warning',
        'an adult with trauma reading the warnings at the top before starting, who may already take lion\'s mane or '
        'ashwagandha, or be thinking of adding them for focus or stress',
        {'Lion\'s Mane & Ashwagandha:': ('they learn he isn\'t advising either, so they leave them out', 'it is the next '
                                         'item of the warnings, the first about supplements the protocol doesn\'t use',
                                         None),
         "They're popular": ('they learn why, though many take them: reports of anhedonia, explained where the article '
                             'first uses it, and sexual dysfunction lasting after stopping, and the name people give it',
                             'it gives the reason for the stance before it', "They're popular"),
         "It's rare": ('they learn how rare it is, and that two known drugs can do the same, so they keep it in mind',
                       'it weighs the reports the sentence before gives', "It's rare")},
        'they learn at once that he isn\'t advising two popular supplements they may be taking or considering',
        [('rare reports of lasting anhedonia and sexual dysfunction after lion\'s mane and ashwagandha',
          'no trial or case report found; trials report mostly mild side effects; the reports are community ones (his '
          'finding), as ' + SRC + ' says', 'yes: they learn to leave both out, from reports said as reports', 'kept'),
         ('lasting sexual dysfunction is a known risk after SSRIs and finasteride',
          'the EMA recognized lasting sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems '
          'continuing after stopping to finasteride\'s labels in 2011 and 2012 (' + SRC + ')',
          'yes: they learn the kind of harm the reports describe is a known risk with drugs, so they keep it in mind',
          'kept')],
        {'reader': reader('needed', 'lma4'), 'unneeded': [], 'kept': {}},
        {'reader': reader('his-fixes', 'agm5-lma6') + ', and the tell panel on LMA3 (x1123b/panel-lma3/PANEL.md)',
         'marked': [{'s': l6[1], 'difference': '12, 13, 9, 10'}, {'s': l6[2], 'difference': '10, 7, 4, 8, 12'}],
         'kept': {}},
        {'reader': reader('fit', 'lma4'), 'marked': [], 'kept': {}},
        'read the section from its heading to the next for lion\'s mane and ashwagandha: no other item names them, and the '
        'article advises neither anywhere (checked 2026-11-22)',
        'a new item of the warnings at the top, after the Cognitive Warning and before the Agmatine Warning, so its '
        '"anhedonia" is the article\'s first and is said in plain words there')
    print('\n'.join(bad) or 'receipts 3 PASS')


if __name__ == '__main__':
    third() if 'third' in sys.argv else (second() if 'second' in sys.argv else main())
