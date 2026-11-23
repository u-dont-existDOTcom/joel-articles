"""The receipts for his new warnings (texts_x1123a): the lion's mane and ashwagandha item (LMA), agmatine's stop line with
its added sentence (AGM) and 5-HTP's stop signs with theirs (HTP). The reads are reads-KEY.md (one fresh Haiku reader per
text, given needed_read_brief.md, his_fixes_brief.md and fit_read_brief.md in turn, of the versions LMA0, AGM_ADD0 and
HTP_ADD0); sources: x1122a/WARNINGS-SOURCES.md. In AGM and HTP only the added sentence is new: the rest is the post's text
as the article has it, kept by this change, and the marks the reads put on it are recorded with that reason.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123a/build_receipts_x1123a.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'sci-cde'))
import sense_receipt as S  # noqa: E402
import texts_x1123a as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

SRC = 'x1122a/WARNINGS-SOURCES.md'
OLD = ('the post\'s text as the article has it, kept by this change, which only adds the new sentence his warning asked '
       'for; its own marks wait for a pass on this paragraph')


def reader_line(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Haiku, 2026-11-23) given tools/humanization/%s and only the text, one sentence a line, before '
            'the new sentence was revised (x1123a/reads-%s.md)' % (brief, key))


def fill(r, spec):
    for x in r['sentences']:
        if x.get('his'):
            continue
        (k,) = [k for k in spec if x['s'].startswith(k)]
        x['payoff'], x['follows'] = spec[k][0], spec[k][1]
        if 'link' in x:
            link = spec[k][2]
            assert link and link in x['s'], (k, link)
            x['link'] = link


def build(key, text, where, reader, spec, opens, checked, needed, his_fixes, fit, same, place):
    r = S.make(text, where, reader)
    fill(r, spec)
    r['opens'] = {'first_sentence': r['sentences'][0]['s'], 'why_reading': opens}
    r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in checked]
    r['needed'], r['his_fixes'], r['fit'] = needed, his_fixes, fit
    r['same_point'], r['placement'] = same, place
    r['questions'] = dict(Q_ANS)
    r['questions']['Q2'] = ('PASS: each instruction says what it is for in the reader\'s terms (why not to start them, '
                            'what to stop for)')
    (HERE / ('%s.receipt.json' % key)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % key)).write_text(text + '\n', encoding='utf-8')
    return ['%s: %s' % (key, x) for x in S.check(text, r)]


def lma3():
    t = T.LMA3
    s2 = S.sentences(T.LMA2)
    return build(
        'LMA3', t, 'A Complete Guide to Bio-De-Armoring, the warnings: a new item after the Cognitive Warning',
        'an adult with trauma reading the warnings at the top before starting, who may already take lion\'s mane or '
        'ashwagandha, or be thinking of adding them for focus or stress',
        {'Lion\'s Mane & Ashwagandha:': ('they learn why people take these two and that he\'d leave both out, so they do',
                                         'it is the next item of the warnings, the first about a supplement the protocol '
                                         'doesn\'t use', None),
         'People say these herbs': ('they learn what the rare reports describe: anhedonia, explained where the article first '
                                    'uses it, and sexual dysfunction that lasted after stopping, and where the reports come '
                                    'from', 'it says why to leave them out, after the advice', 'People say these herbs'),
         'Nobody has studied': ('they learn how far the reports go (not studied) and that the same kind of lasting harm is '
                                'one regulators already recognize for SSRIs and finasteride, so the rare reports are worth '
                                'heeding', 'it weighs the reports the sentence before gives', 'Nobody has studied these '
                                'effects')},
        'they learn the protocol\'s advice on two popular supplements they may be taking or considering, and why',
        [('rare reports of lasting anhedonia and sexual dysfunction after lion\'s mane and ashwagandha',
          'no trial or case report found; trials report mostly mild side effects; the reports are community ones (his '
          'finding), as ' + SRC + ' says', 'yes: they learn to leave both out, from reports said as reports', 'kept'),
         ('regulators warn about the same kind of lasting effect after SSRIs and finasteride',
          'the EMA recognized lasting sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems '
          'continuing after stopping to finasteride\'s labels in 2011 and 2012 (' + SRC + ')',
          'yes: they learn the kind of harm the reports describe is one regulators already recognize', 'kept')],
        {'reader': reader_line('needed', 'lma2'), 'unneeded': [s2[2]],
         'kept': {s2[2]: 'they learn the lasting harm the reports describe is a kind regulators already recognize for '
                         'drugs (his point in his message), so they take rare reports seriously enough to leave the herbs '
                         'out; LMA3 names its referents and says it as what regulators warn about'}},
        {'reader': reader_line('his-fixes', 'lma2'),
         'marked': [{'s': s2[1], 'difference': '11'}, {'s': s2[2], 'difference': '7, 10'}], 'kept': {}},
        {'reader': reader_line('fit', 'lma2'),
         'marked': [{'s': s2[1], 'found': 'anyway: a numb reader may feel nothing is good already; can\'t tell: from the '
                                          'herb or the trauma'},
                    {'s': s2[2], 'found': 'from: drug-regulation text; misread: an SSRI user alarmed'}],
         'kept': {}},
        'read the section from its heading to the next for lion\'s mane and ashwagandha: no other item names them, and the '
        'article advises neither anywhere (checked 2026-11-22)',
        'a new item of the warnings at the top, after the Cognitive Warning and before the Agmatine Warning, so its '
        '"anhedonia" is the article\'s first and is said in plain words there; the agmatine and 5-HTP lines after it can '
        'then use the word')


def main():
    bad = []
    bad += lma3()
    # ---- LMA
    t = T.LMA
    s0 = S.sentences(T.LMA0)
    bad += build(
        'LMA', t, 'A Complete Guide to Bio-De-Armoring, the warnings: a new item after the Cognitive Warning',
        'an adult with trauma reading the warnings at the top before starting, who may already take lion\'s mane or '
        'ashwagandha, or be thinking of adding them for focus or stress',
        {'Lion\'s Mane & Ashwagandha:': ('they learn why people take these two and that the protocol doesn\'t advise or use '
                                         'them, so they leave them out', 'it is the next item of the warnings, the first '
                                         'about a supplement the protocol doesn\'t use', None),
         'People on forums and YouTube': ('they learn what the rare reports describe: anhedonia, explained where it is '
                                          'first used in the article, and sexual problems lasting months after stopping',
                                          'it says why not, after the don\'t', 'People on forums and YouTube'),
         'These lasting effects': ('they learn how far the reports go (not studied yet) and what makes them credible: the same '
                                 'kind of lasting effect regulators warn about after SSRIs and finasteride',
                                 'it weighs the reports the sentence before gives', 'These lasting effects')},
        'they learn the protocol leaves out two popular supplements they may be taking or considering, and why',
        [('rare reports of lasting anhedonia and sexual problems after lion\'s mane and ashwagandha',
          'no trial or case report found; trials report mostly mild side effects; the reports are community ones (his '
          'finding), as ' + SRC + ' says',
          'yes: they learn to leave both out, from reports said as reports', 'kept'),
         ('regulators warn about the same kind of lasting effect after SSRIs and finasteride',
          'the EMA recognized lasting sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems '
          'continuing after stopping to finasteride\'s labels in 2011 and 2012 (' + SRC + ')',
          'yes: they learn the kind of effect the reports describe is one regulators already recognize for drugs', 'kept')],
        {'reader': reader_line('needed', 'lma'), 'unneeded': [], 'kept': {}},
        {'reader': reader_line('his-fixes', 'lma'),
         'marked': [{'s': s0[0], 'difference': '14'}, {'s': s0[1], 'difference': '10'},
                    {'s': s0[2], 'difference': '1, 3, 10'}], 'kept': {}},
        {'reader': reader_line('fit', 'lma'),
         'marked': [{'s': s0[1], 'found': 'anyway: a numb reader may already feel nothing is good; can\'t tell: from the '
                                          'supplement or the trauma'},
                    {'s': s0[2], 'found': 'from: prescription-drug warnings carried over; misread: "mild" before the '
                                          'warning'}],
         'kept': {}},
        'read the section from its heading to the next for lion\'s mane and ashwagandha: no other item names them, and the '
        'article advises neither anywhere (checked 2026-11-22)',
        'a new item of the warnings at the top, after the Cognitive Warning and before the Agmatine Warning, so its '
        '"anhedonia" is the article\'s first and is said in plain words there; the agmatine and 5-HTP lines after it can '
        'then use the word')
    # ---- AGM
    t = T.agm_paragraph()
    s = S.sentences(t)
    assert len(s) == 4, len(s)
    bad += build(
        'AGM', t, 'Agmatine Warning (The Voltage Governor), the stop line',
        'an adult with trauma about to try agmatine for glutamate storms, reading its warning to decide what would make '
        'them stop',
        {'Stop immediately': ('they learn the signs that mean stopping agmatine', 'it follows the precautions with the '
                              'signs to stop at', None),
         'Only the stomach problems': ('they learn the flatness comes from practice, not the trials, so they stop rather '
                                       'than push through numbness', 'it says where the signs before come from',
                                       'Only the stomach problems'),
         'In rare reports': ('they learn the anhedonia can outlast stopping, for weeks, so stopping early matters',
                             'it says why not to push through, right after the line that says so', 'In rare reports'),
         'If agmatine makes the world': ('they learn a grayer world means agmatine is the wrong tool for the gray phase, '
                                         'where the protocol stops it', 'it closes the line on the case the protocol\'s '
                                         'own timeline meets', 'If agmatine makes the world')},
        'they learn the signs that mean stopping agmatine, which they need before starting it',
        [('rare reports of anhedonia lasting weeks after stopping agmatine',
          'trials report only stomach upset (Shopsin 2013); emotional dullness while taking it is reported in nootropic '
          'summaries; weeks after stopping is his finding (' + SRC + ')',
          'yes: they learn the flatness can last after stopping, so they stop at the first sign', 'kept')],
        {'reader': reader_line('needed', 'agm'), 'unneeded': [s[3]],
         'kept': {s[3]: 'they learn that agmatine graying the world means it is the wrong tool for the gray phase, the '
                        'case Weeks 3-5 meets when it says to stop agmatine there; ' + OLD}},
        {'reader': reader_line('his-fixes', 'agm'),
         'marked': [{'s': s[0], 'difference': '1, 19'}, {'s': s[1], 'difference': '9, 14'},
                    {'s': s[3], 'difference': '6, 10'}],
         'kept': {s[0]: OLD, s[1]: OLD, s[3]: OLD}},
        {'reader': reader_line('fit', 'agm'),
         'marked': [{'s': s[0], 'found': 'anyway, can\'t tell'}, {'s': s[1], 'found': 'anyway'},
                    {'s': s[2], 'found': 'anyway, can\'t tell: lasting anhedonia from the drug or the trauma'},
                    {'s': s[3], 'found': 'anyway, can\'t tell'}],
         'kept': {s[0]: OLD, s[1]: OLD, s[3]: OLD,
                  s[2]: 'his warning: the reports are of anhedonia after stopping; it tells the reader why stopping early '
                        'matters, and whether a sign is new is the reader\'s judgment, as with every sign in the line'}},
        'read the warnings from the Agmatine Warning to the next item for anhedonia after stopping: none; the cycle rule in '
        'the Glutamate Shield gives the same stop signs for the phase, without this',
        'the Agmatine Warning\'s stop line, right after "do not push through numbness", whose reason it gives')
    # ---- HTP
    t = T.htp_paragraph()
    s = S.sentences(t)
    assert len(s) == 3, len(s)
    bad += build(
        'HTP', t, 'Serotonin Bottleneck Pattern: 5-HTP + Low-Dose P5P, its stop signs',
        'an adult with trauma and low mood or poor sleep trying 5-HTP for a few nights, reading what would make them stop',
        {'Side effects / stop signs': ('they learn the dangerous signs, serotonin syndrome\'s, that mean stopping now',
                                       'it follows the trial\'s first signs of working with its signs of harm', None),
         'Other stop signs': ('they learn the milder signs that mean stopping too', 'it goes from the dangerous signs to '
                              'the milder ones', 'Other stop signs'),
         'And rarely': ('they learn anhedonia can linger for weeks after stopping, so they watch for it after they quit',
                        'it adds what can outlast the stop', 'And rarely')},
        'they learn the dangerous signs first, which decide whether they stop now',
        [('rare reports of anhedonia lasting weeks after stopping 5-HTP',
          'documented side effects are stomach upset, headache, sleeplessness and palpitations; low mood up to a week after '
          'stopping in a doctors\' answer, four weeks of panic and depression in a user review; weeks of anhedonia is his '
          'finding (' + SRC + ')', 'yes: they learn it can linger after they stop', 'kept')],
        {'reader': reader_line('needed', 'htp'), 'unneeded': [], 'kept': {}},
        {'reader': reader_line('his-fixes', 'htp'),
         'marked': [{'s': s[0], 'difference': '1'}, {'s': s[1], 'difference': '1, 3, 4, 19'}],
         'kept': {s[0]: OLD, s[1]: OLD}},
        {'reader': reader_line('fit', 'htp'),
         'marked': [{'s': s[0], 'found': 'can\'t tell, misread'}, {'s': s[1], 'found': 'anyway, can\'t tell'},
                    {'s': s[2], 'found': 'can\'t tell: from stopping or from their low mood'}],
         'kept': {s[0]: OLD, s[1]: OLD,
                  s[2]: 'his warning: it tells them lost pleasure can follow stopping, for weeks; telling it from their '
                        'own low mood is theirs to judge, as with every sign in the paragraph'}},
        'read the 5-HTP section from its heading to the next for what lingers after stopping: none',
        'the end of the 5-HTP stop signs, after the milder signs, since it is what can follow the stop')
    for x in bad:
        print(x)
    print('ok' if not bad else 'PROBLEMS')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
