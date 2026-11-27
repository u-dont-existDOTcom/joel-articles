"""The receipts for this turn's two warnings (texts_x1127a.NEW), with x1126c's builder (its `his`), the reads swapped
for this turn's fresh readers (Fable, 2026-11-27: x1127a/v1/{needed,his-fixes,fit}/KEY/READ.md):

  - lma: his herbs warning with 73a and his line "i also can't recommend starting them" (his message of 2026-11-27
    15:45 UTC). The v1 readers read 73a's words as question 73 gave them (texts_x1127a.READ1); my part of the second
    sentence was then fixed for what they marked (texts_x1127a, the comment before LMA_END_2), so its v1 marks need no
    kept reason for my words; his own words in it keep theirs.
  - prec: his Precautions paragraph with 74b ("on the same day as"); every mark is on his own words and goes to him with
    my best fix (question 76 for "(will reduce tolerance)", the thoughts in OWNER-QUESTIONS.md for the rest).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127a/build_receipts_x1127a.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
sys.path.insert(0, str(FIX / 'x1126c'))
sys.path.insert(0, str(HERE))
import build_receipts_x1126c as R  # noqa: E402
import texts_x1127a as T  # noqa: E402

B, S = R.B, R.S
OUT = HERE / 'receipts'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
MSG = ('his answers "73 a  but i also can\'t recommend starting them 74 b" of 2026-11-27 15:45 UTC '
       '(fix-20261108/joel-20261127-1545-message.txt)')


def text(key):
    return T.plain(T.NEW[key])


def v1(key, n):
    """Sentence N as the v1 readers read it."""
    return S.sentences(T.plain(T.READ1[key]))[n - 1]


def reader(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-27) given tools/humanization/%s and only the paragraph as %s left it, one '
            'sentence a line (x1127a/v1/%s/%s/READ.md)' % (brief, MSG, kind, key))


def his_kept(key):
    return ('his own sentence, from ' + R.CARD[key] + ', with ' + MSG + ' put in; a change to his own words goes to him '
            'first (AGENTS.md: a tested change goes in without a card "unless ... the words are his own"), so this mark '
            'goes to him in the turn\'s report with my best fix')


# x1126c's `his` looks these up when it runs
R.text, R.v1, R.reader, R.his_kept, R.MSG = text, v1, reader, his_kept, MSG

LMA_S1_KEPT = ('his own sentence, from ' + R.CARD['lma'] + ', with his line "i also can\'t recommend starting them" (' +
               MSG + ') fitted in place of "I\'m not advising", which a reader already on lion\'s mane couldn\'t read as '
               'stop or don\'t start (question 73), 73a\'s gloss "(little pleasure or desire)", and "that last" before his '
               '"long after they stop taking them", which the second fit reader (v2/fit/lma) took as stopping bringing the '
               'problems on, now that the paragraph ends on stopping (question 75); the rest is his and goes to him first. The fit reader\'s "not about me" (a reader already on lion\'s mane) is what the second '
               'sentence answers: its stop sign is for anyone who takes either herb')
LMA_S2_KEPT = ('its start is his ("Post-ashwa and post-lion\'s mane syndrome are rare, but it\'s the same kind of thing SSRIs '
               'and finasteride can do"), his reason the rare reports are worth heeding, and his words go to him first; '
               'my part after "so" was fixed for what the reads marked in it: "either herb" (not the two drugs), one '
               'condition and then the act, "since you started it" for a baseline, and "or any sexual problems", the '
               'second effect his first sentence names (question 75). Nothing says stopping early keeps the effect from '
               'lasting, and I don\'t add that: no source shows it')


def lma():
    return R.his(
        'LMA-73A', 'lma', 'the herbs the protocol leaves out, with 73a and his line "can\'t recommend starting them"',
        'who may already take lion\'s mane or ashwagandha, or be thinking of adding them for focus or stress',
        {'I can\'t recommend': ('they learn he can\'t recommend starting either herb, though both are popular for focus '
                                'and stress, and why: some people report anhedonia (little pleasure or desire) and sexual '
                                'problems that last long after stopping', 'it is the next warning after the Cognitive Warning, '
                                'the first about a supplement the protocol leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so if they take either herb they stop it at the first loss of pleasure or desire, '
                        'or any sexual problem, since they started it', 'it weighs the reports the sentence before gives, '
                        'and then says what to watch for', 'Post-ashwa')},
        'they learn his advice on two popular supplements they may be taking or considering, why, and when to stop '
        'either',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to stop at the first sign', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(1, 2), also={1: LMA_S1_KEPT, 2: LMA_S2_KEPT})


PREC_KEPT = {
    1: ('his own sentence (' + R.CARD['prec'] + ') with 74b\'s "on the same day as" for "concurrently with" (' + MSG +
        '); a change to his own words goes to him first, so its marks go to him with my best fix: "(will reduce '
        'tolerance)" read as a plus by a kratom user is question 76; the rest is in the thoughts on his page'),
    2: ('his own words, with the subject named ("It\'s"), the near-miss step after the fold read Human Low there last '
        'turn (checks-1126r, lesson neuro-2026-11-26n); the reader who took it as agmatine only is right that it is, and '
        'whether the whole protocol is for pregnancy is his to say (a thought on his page)'),
    3: ('his own words, word for word ("Use with extreme caution" is held by fidelity key W009); question 74 offered '
        '"and ask your doctor first" and he didn\'t pick it, so it stays as he wrote it'),
}


def prec():
    return R.his(
        'PREC-74B', 'prec', 'his Precautions paragraph after the agmatine warning, with 74b', 'who takes some medication, '
        'or kratom some days, and is deciding whether agmatine is worth trying',
        {'Do not use agmatine': ('they check what they take against the drugs named, and don\'t take agmatine on the same '
                                 'day as any of them without a physician who can weigh the interactions', 'it names the '
                                 'medications the warning before says agmatine interacts with', None),
         'It\'s not recommended': ('they leave agmatine out while pregnant or breast-feeding', 'it adds the next group '
                                   'who should not take it', 'none: the next item of his precautions, which run as a '
                                   'list of who should not take it'),
         'Use with extreme': ('they take extra care, or leave it out, after a psychotic episode, with low blood pressure, '
                              'or with kidney or liver problems', 'it gives the last group, those for whom it needs '
                              'extreme caution', 'none: the last item of his precautions list, those who need extreme '
                              'caution')},
        'they learn which medications agmatine must not share a day with, so they can check their own',
        [('the drugs and groups to keep agmatine away from', R.CARD['prec'] + '; the article\'s agmatine section names the '
          'same', 'yes: they check their own medications and conditions against it', 'kept')],
        [],
        [(1, '1, 2, 4, 10, 5, 13, 7, 29: four drug groups in one sentence, built alike; "complex psychoactive stacks"; '
             '"(will reduce tolerance)" two ways; the rule before its reason; no reason for the blood pressure drugs; '
             '"other" with nothing it is other than'),
         (2, '5, 12: an authority\'s passive; a new case standing alone'),
         (3, '4, 15, 5, 1, 19, 16: "extreme caution" names no act; label wording about patients; three unlike '
             'conditions; low blood pressure apart from the blood pressure drugs')],
        [(1, 'CAN\'T TELL what counts as a "complex psychoactive stack", a "competent" doctor, nitrates or PDE-5 '
             'inhibitors among my pills; MISREAD: "will reduce tolerance" sounds like a plus to a kratom user'),
         (2, 'MISREAD: "It\'s" as agmatine only, so the rest of the protocol sounds fine in pregnancy'),
         (3, 'CAN\'T TELL what "extreme caution" asks, what "lower end" blood pressure is; FROM: drug-label wording')],
        'read the section for agmatine\'s interactions: the warning before says it interacts with more medications, '
        'and this names them; the article\'s agmatine section gives the same list',
        'right after the agmatine warning, where the post has it', also=PREC_KEPT)


LMA2_S1_KEPT = ('his own sentence, from ' + R.CARD['lma'] + ', with his line "i also can\'t recommend starting them" (' +
                MSG + ') fitted in place of "I\'m not advising", which a reader already on lion\'s mane couldn\'t read as '
                'stop or don\'t start (question 73), and 73a\'s gloss "(little pleasure or desire)"; the rest is his and '
                'goes to him first. "That last", tried in LMA-73A for the fit reader who took "long after they stop" as '
                'stopping bringing the problems on, is out: the try read AI, and the second sentence now says to stop the '
                'moment the problems show, while taking the herb')
LMA2_S2_KEPT = ('its start is his ("Post-ashwa and post-lion\'s mane syndrome are rare, but it\'s the same kind of thing '
                'SSRIs and finasteride can do"), his reason the rare reports are worth heeding, and his words go to him '
                'first; my part after "so" says the stop sign the way he says advice ("I\'d", as his "I wouldn\'t push '
                'through that signal"), with his baseline "than before you started", "either herb" (not the two drugs), '
                '"already" for the reader who takes one now, and "or any sexual problems", the second effect his first '
                'sentence names (question 75)')


def lma2():
    return R.his(
        'LMA-73A-T2', 'lma', 'the herbs the protocol leaves out, with 73a and his line "can\'t recommend starting them"; try 2',
        'who may already take lion\'s mane or ashwagandha, or be thinking of adding them for focus or stress',
        {'I can\'t recommend': ('they learn he can\'t recommend starting either herb, though both are popular for focus '
                                'and stress, and why: some people report anhedonia (little pleasure or desire) and sexual '
                                'problems long after stopping', 'it is the next warning after the Cognitive Warning, the '
                                'first about a supplement the protocol leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so if they already take either herb they stop the moment they notice less pleasure '
                        'or desire than before they started, or any sexual problem', 'it weighs the reports the sentence '
                        'before gives, and then says what to watch for', 'Post-ashwa')},
        'they learn his advice on two popular supplements they may be taking or considering, why, and when to stop '
        'either',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to stop at the first sign', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(2,), also={1: LMA2_S1_KEPT, 2: LMA2_S2_KEPT}, t=T.plain(T.TRY['lma-2']))


LMA3_S1_KEPT = ('his own sentence, from ' + R.CARD['lma'] + ', with his line "i also can\'t recommend starting them" (' +
                MSG + ') said in his own opening ("I\'m not advising anyone to start"), which tells a reader already on '
                'lion\'s mane that it\'s about starting (question 73), and 73a\'s gloss said as bluntly as his "(no desire)" '
                'was, "(no pleasure or desire)"; the rest is his and goes to him first. "I can\'t recommend starting" and the '
                'measured gloss (tries 1 and 2) read AI over this sentence, and the tell panel agreed on both (panel-lma-t2)')
LMA3_S2_KEPT = ('its start is his ("Post-ashwa and post-lion\'s mane syndrome are rare, but it\'s the same kind of thing '
                'SSRIs and finasteride can do"), his reason the rare reports are worth heeding, and his words go to him '
                'first; my part after "so" is 73a\'s stop sign, pointing back at what his first sentence names instead of '
                'repeating it (the tell panel agreed the repeat read as a model closing its loop): "notice any of that '
                'starting", which also says the problems start while taking the herb and covers both of them (question '
                '75), "I\'d quit it" last, "either herb" (not the two drugs), "already" for the reader who takes one now')


def lma3():
    return R.his(
        'LMA-73A-T3', 'lma', 'the herbs the protocol leaves out, with 73a and his line; try 3',
        'who may already take lion\'s mane or ashwagandha, or be thinking of adding them for focus or stress',
        {'I\'m not advising anyone': ('they learn he advises nobody to start either herb, though both are popular for '
                                      'focus and stress, and why: some people report anhedonia (no pleasure or desire) '
                                      'and sexual problems long after stopping', 'it is the next warning after the '
                                      'Cognitive Warning, the first about a supplement the protocol leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so if they already take either herb they quit it when they notice either problem '
                        'starting', 'it weighs the reports the sentence '
                        'before gives, and then says what to watch for', 'Post-ashwa')},
        'they learn his advice on two popular supplements they may be taking or considering, why, and when to quit '
        'either',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to quit at the first sign', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(1, 2), also={1: LMA3_S1_KEPT, 2: LMA3_S2_KEPT}, t=T.plain(T.TRY['lma-3']))


LMA4_S3_KEPT = ('mine: 73a\'s stop sign as its own short sentence after his two, in his first-person voice for advice '
                '("I\'d", as his "I wouldn\'t push through that signal"), pointing back at what his first sentence names '
                '("any of that": the anhedonia and the sexual dysfunction, question 75) instead of repeating it; his '
                'slack ending before it stays, since every try that replaced it read AI (tries 1 to 3)')


def lma4():
    return R.his(
        'LMA-73A-T4', 'lma', 'the herbs the protocol leaves out, with 73a and his line; try 4',
        'who may already take lion\'s mane or ashwagandha, or be thinking of adding them for focus or stress',
        {'I\'m not advising anyone': ('they learn he advises nobody to start either herb, though both are popular for '
                                      'focus and stress, and why: some people report anhedonia (no pleasure or desire) '
                                      'and sexual problems long after stopping', 'it is the next warning after the '
                                      'Cognitive Warning, the first about a supplement the protocol leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so they weigh it', 'it weighs the reports the sentence before gives', 'Post-ashwa'),
         'If I were already': ('if they already take either herb, they quit it the day they notice either problem',
                               'it says what he would do, which is what to watch for', 'none: his advice for the reader '
                               'already on one, after the weighing')},
        'they learn his advice on two popular supplements they may be taking or considering, why, and when to quit '
        'either',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to quit at the first sign', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(1, 2), also={1: LMA3_S1_KEPT, 2: ('his own sentence, from ' + R.CARD['lma'] + ', word for word as it '
                              'read High in the fold; his words go to him first; ' + LMA4_S3_KEPT)},
        t=T.plain(T.TRY['lma-4']))


def lma_step(name, key, s2, also2, extra=None, gloss='(no pleasure or desire)'):
    spec = {'I\'m not advising anyone': ('they learn he advises nobody to start either herb, though both are popular for '
                                         'focus and stress, and why: some people report anhedonia ' + gloss + ' and sexual '
                                         'problems long after stopping', 'it is the next warning after the Cognitive '
                                         'Warning, the first about a supplement the protocol leaves out', None),
            'Post-ashwa': s2}
    spec.update(extra or {})
    return R.his(
        name, 'lma', 'the herbs the protocol leaves out, a step from the fold (W-LMA-his) toward 73a and his line',
        'who may already take lion\'s mane or ashwagandha, or be thinking of adding them for focus or stress', spec,
        'they learn his advice on two popular supplements they may be taking or considering, and why',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(1, 2), also={1: LMA3_S1_KEPT, 2: also2}, t=T.plain(T.STEP[key]))


def lma_s1():
    return lma_step('LMA-S1', 'lma-s1',
                    ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                     'finasteride, so they keep it in mind', 'it weighs the reports the sentence before gives',
                     'Post-ashwa'),
                    'his own sentence, from ' + R.CARD['lma'] + ', word for word as it read High in the fold; his words go '
                    'to him first. 73a\'s stop sign comes in the next step, a check of its own (the near-miss rule): this '
                    'step is his line and the gloss only')


def lma_s2():
    r = lma_step('LMA-S2', 'lma-s2',
                 ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and finasteride, '
                  'so they keep it in mind', 'it weighs the reports the sentence before gives', 'Post-ashwa'),
                 'his own sentence, from ' + R.CARD['lma'] + ', word for word as it read High in the fold; his words go to '
                 'him first; this step is his line alone, the gloss as he had it, to find which change turned step 1',
                 gloss='(no desire)')
    return r


def lma_s3():
    return R.his(
        'LMA-S3', 'lma', 'the herbs the protocol leaves out, step 3 from the fold: his first sentence as it read High, 73a\'s '
        'stop sign for the reader already on either herb', 'who may already take lion\'s mane or ashwagandha, or be '
        'thinking of adding them for focus or stress',
        {'I\'m not advising lion': ('they learn he advises neither herb, though both are popular for focus and stress, and '
                                    'why: some people report anhedonia (no desire) and sexual problems long after '
                                    'stopping', 'it is the next warning after the Cognitive Warning, the first about a '
                                    'supplement the protocol leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so if they are already on either herb they quit as soon as they notice any of it',
                        'it weighs the reports the sentence before gives, and says what to do if already on one',
                        'Post-ashwa')},
        'they learn his advice on two popular supplements they may be taking or considering, why, and when to quit '
        'either',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to quit at the first sign', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(1, 2), also={
            1: ('his own sentence, from ' + R.CARD['lma'] + ', word for word as it read High in the fold: his line (" i also '
                'can\'t recommend starting them") is carried by his own "I\'m not advising lion\'s mane or ashwagandha" '
                'with the stop sign after it addressed to the reader already on one, which answers what question 73\'s '
                'reader couldn\'t tell (stop, or only not start); "anyone to start" weakened this sentence by itself (step '
                '2), and 73a\'s gloss with it more (step 1), so the gloss waits for a step of its own'),
            2: ('its start is his, word for word; my part is 73a\'s stop sign in place of his slack ending, addressed to the '
                'reader already on either herb ("either herb", not the two drugs), in his voice ("I\'d quit"), pointing '
                'back at what his first sentence names ("any of that": both effects, question 75)')},
        t=T.plain(T.STEP['lma-s3']))


def lma_s4():
    r0 = R.his
    return R.his(
        'LMA-S4', 'lma', 'the herbs the protocol leaves out, step 4: 73a\'s gloss in plain words, and "it" after "I\'d quit"',
        'who may already take lion\'s mane or ashwagandha, or be thinking of adding them for focus or stress',
        {'I\'m not advising lion': ('they learn he advises neither herb, though both are popular for focus and stress, and '
                                    'why: some people report anhedonia (no joy or desire) and sexual problems long after '
                                    'stopping', 'it is the next warning after the Cognitive Warning, the first about a '
                                    'supplement the protocol leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so if they are already on either herb they quit it as soon as they notice any of it',
                        'it weighs the reports the sentence before gives, and says what to do if already on one',
                        'Post-ashwa')},
        'they learn his advice on two popular supplements they may be taking or considering, why, and when to quit '
        'either',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to quit at the first sign', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(1, 2), also={
            1: ('his own sentence, from ' + R.CARD['lma'] + ', as it read High in the fold and in step 3, with 73a\'s gloss '
                'in plain words ("(no joy or desire)": the pleasure question 73\'s reader missed, as bluntly as his "(no '
                'desire)"; "(no pleasure or desire)" weakened this sentence in step 1); his line is carried by his own "I\'m '
                'not advising lion\'s mane or ashwagandha" with the stop sign addressed to the reader already on one'),
            2: ('its start is his, word for word; my part is 73a\'s stop sign in place of his slack ending, addressed to the '
                'reader already on either herb, in his voice ("I\'d quit it": "it" the herb, which step 3 left to guess), '
                'pointing back at what his first sentence names ("any of that": both effects, question 75)')},
        t=T.plain(T.STEP['lma-s4']))


def lma_s5():
    r0 = R.his
    return R.his(
        'LMA-S5', 'lma', 'the herbs the protocol leaves out, step 5: 73a\'s gloss in plain words, the stop sign in his idiom',
        'who may already take lion\'s mane or ashwagandha, or be thinking of adding them for focus or stress',
        {'I\'m not advising lion': ('they learn he advises neither herb, though both are popular for focus and stress, and '
                                    'why: some people report anhedonia (no joy or desire) and sexual problems long after '
                                    'stopping', 'it is the next warning after the Cognitive Warning, the first about a '
                                    'supplement the protocol leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so they stop either herb right away if they notice any of it',
                        'it weighs the reports the sentence before gives, and says what to do if already on one',
                        'Post-ashwa')},
        'they learn his advice on two popular supplements they may be taking or considering, why, and when to quit '
        'either',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to quit at the first sign', 'kept')],
        [],
        [(1, '1, 4: three ideas, "even though" an aside; "sexual dysfunction" a category word; "long after" says not how '
             'long'),
         (2, '10, 12, 21, 8, 7: "it" after "are rare"; "either" right after the two drugs; the "so" link; the coined '
             'name; two ifs; the stop sign leaves out the sexual dysfunction')],
        [(1, 'MISREAD: "can\'t recommend starting" read as not about a reader already on lion\'s mane, until the second '
             'sentence'),
         (2, 'ANYWAY and CAN\'T TELL: "than before" has no before for a reader already on it and already numb; MISREAD: '
             '"post-" makes stopping sound like when the trouble comes')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it',
        changed=(1, 2), also={
            1: ('his own sentence, from ' + R.CARD['lma'] + ', as it read High in the fold and in step 3, with 73a\'s gloss '
                'in plain words ("(no joy or desire)": the pleasure question 73\'s reader missed, as bluntly as his "(no '
                'desire)"; "(no pleasure or desire)" weakened this sentence in step 1); his line is carried by his own "I\'m '
                'not advising lion\'s mane or ashwagandha" with the stop sign addressed to the reader already on one'),
            2: ('its start is his, word for word; my part is 73a\'s stop sign in place of his slack ending, addressed to the '
                'reader on either herb, in one clause in his own idiom (his agmatine paragraph: "so stop it right away if you '
                'notice"), "either herb" so it can\'t be read as the two drugs, '
                'pointing back at what his first sentence names ("any of that": both effects, question 75)')},
        t=T.plain(T.STEP['lma-s5']))


ALL = {'lma': lma, 'prec': prec, 'lma-2': lma2, 'lma-3': lma3, 'lma-4': lma4, 'lma-s1': lma_s1, 'lma-s2': lma_s2, 'lma-s3': lma_s3, 'lma-s4': lma_s4, 'lma-s5': lma_s5}

if __name__ == '__main__':
    keys = sys.argv[1:] or list(ALL)
    bad = [x for k in keys for x in ALL[k]()]
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')
    sys.exit(1 if bad else 0)
