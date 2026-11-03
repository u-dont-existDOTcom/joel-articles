"""Pangram 4.0 pairs (2026-10-18): the published guide, which read AI, beside Emulate's raw samples whose sections read Human."""
from ex import T
from data1 import L, O

B429 = 'fix-20261018/b429/b429-results.json'
W41A = 'fix-20261020/result41/WINDOWS-41a.json'


def res(b):
    return 'fix-20261018/%s/%s-results.json' % (b, b)


def pairs():
    P = []

    def p40(pid, run, inp, out, in_read, out_read, labels, meaning, note, folder='emu-a', kind='pass', in_folder=None):
        screened = out_read.split('batch ')[1].split(' ')[0].rstrip(',;)')
        return dict(id=pid, batch='%s (sample %s)' % (screened, folder),
                    detector='Pangram 4.0', kind=kind,
                    input=T('fix-20261018/%s/%s.txt' % (in_folder or folder, run), *inp),
                    input_reading=in_read,
                    emulate=T('fix-20261018/%s/%s.out.txt' % (folder, run), *out),
                    emulate_reading=out_read, labels=labels, meaning_error=meaning, note=note)

    P.append(p40('40-HG06-consent', 'HG06-r1',
        ('Conscious agreement is one thing.', 'clearly chosen the influence.'),
        ('Consciously or unconsciously, emotionally or legally', 'fully grown adult.'),
        'AI (High), the whole section one 183-word window, AI likelihood 0.89, batch 429 (%s)' % B429,
        'Human (High), the section one 244-word window, AI likelihood 0.10, batch 430 (%s)' % res('b430'),
        [L['notxy'], L['join'], L['people'], L['casual'], L['closer']],
        'The published point that these are four separate things is lost (they become "ways to gain someone\'s consent"), and "without the adult self having clearly chosen the influence" became "even if they are a fully grown adult". Joel\'s own revision of 28 October put the point back ("All of these are separate factors to consider: ..."), and that line read AI (Low, 18 words) on 2026-10-29.',
        'Shape: an anaphoric run of five short sentences ("X is one thing. Y is another. Z is another. ...") and a summing-up line became one sentence about people ("there are a lot of ways to gain someone\'s consent, or influence their mind").'))
    P.append(p40('40-HG06-form', 'HG06-r1',
        ('Influence doesn’t wait for the conscious mind to sign a form.', None),
        ('Even when not actively engaging the conscious mind, there are many ways to influence people.', None),
        'AI (High), batch 429 (%s)' % B429,
        'Human (High), batch 430 (%s); the same sentence read Human (High, 476-word window) in the first 4.1 check of the installed guide (41a, %s)' % (res('b430'), W41A),
        [L['quip_out'], L['people']],
        '',
        'Shape: a personified quip (influence that won\'t wait for a signed form) became a plain statement about influencing people.'))
    P.append(p40('40-HG06-training', 'HG06-r1',
        ('Advertising, fear, craving, screens', 'adult choice more available.'),
        ('Since there are a lot of forces out there', 'fully conscious adult.'),
        'AI (High), batch 429 (%s)' % B429,
        'Human (High), batch 430 (%s)' % res('b430'),
        [L['join'], L['colon'], L['short_list'], L['subj'], O['reason'], L['casual']],
        '"listening closely" is dropped from what self-hypnosis lets you practice.',
        'Shape: a nine-noun subject list and a colon reveal with three gerunds became one "Since there are a lot of forces out there trying to train your mind, via ..., you can ..." sentence: the list is demoted to a "via" aside and the three practices become two.'))
    P.append(p40('40-HG10-evidence', 'HG10-r1',
        ('Hypnosis has real evidence, although it doesn’t have magical evidence.', None),
        ('Is there REAL (not magical) evidence for Hypnosis? Yes.', None),
        'AI (High), the whole section one 191-word window, batch 429 (%s)' % B429,
        'Human (High), 208 words, batch 430 (%s); still Human (High) in 4.1\'s first check (41a, %s)' % (res('b430'), W41A),
        [L['q'], O['caps'], O['aside'], L['uneven'], L['notxy']],
        '',
        'Shape: a balanced "X, although not Y" claim became a reader\'s question with the contrast in brackets and a one-word answer.'))
    P.append(p40('40-HG10-distinction', 'HG10-r1',
        ('That distinction matters here.', 'trance recordings.'),
        ('Here I will be teaching you a real self-skill', 'audio trance files.'),
        'AI (High), batch 429 (%s)' % B429,
        'Human (High), batch 430 (%s); Human (High) in 41a (%s)' % (res('b430'), W41A),
        [O['signpost_out'], L['concrete'], L['subj']],
        '',
        'Shape: a signpost line ("That distinction matters here.") was dropped, and "a consumer of increasingly elaborate trance recordings" became the concrete "buy more audio trance files".'))
    P.append(p40('40-HG11-state', 'HG11-r1',
        ('A powerful state matters only if something survives it', 'ordinary life.'),
        ('And of course it’s got to be a powerful state', 'in your life!'),
        'AI (High), the whole section one 202-word window, batch 429 (%s)' % B429,
        'Human (High), 230 words, batch 430 (%s)' % res('b430'),
        [L['colon'], L['short_list'], L['casual'], O['excl']],
        'Drops the five outcomes and turns the point around: published says a powerful state matters only if something good survives it; Emulate says it has to be a powerful state. Restoring the list later read AI in 4.1 (reverse-X1.11).',
        'Shape: a colon reveal with a five-item list of abstract nouns became a short casual exclamation.'))
    P.append(p40('40-HG22-dishes', 'HG22-r1',
        ('Do the ordinary action immediately when possible.', 'exactly where they were.'),
        ('Wherever possible take any normal action', 'no point in doing them.'),
        'AI (Low), the whole section one 95-word window, AI likelihood 1.00, batch 429 (%s)' % B429,
        'Human (Medium), 130 words, batch 430 (%s)' % res('b430'),
        [L['join'], L['quip_out'], L['notxy'], L['hedge'], O['runon']],
        '"teaches the subconscious that the adult heard and acted" became "impress on the subconscious that something has changed".',
        'Shape: a command plus a wry "instead of staging another beautiful internal meeting and then leaving the dishes ..." became one run-on sentence that reasons in the subconscious\'s voice ("otherwise it may think that because the dishes have not been done ... that there is no point in doing them").'))
    P.append(p40('40-HG27-enemy', 'HG27-r1',
        ('The subconscious isn’t the enemy.', 'properly introduced.'),
        ('Most of these things will become easier', 'up at the time.'),
        'AI (Medium), the whole section one 111-word window, batch 429 (%s)' % B429,
        'Human (Medium), 133 words, batch 430 (%s)' % res('b430'),
        [L['notxy'], L['people'], L['join'], L['quip_out'], L['casual']],
        'Drops "Most of them have been trying to help"; adds a claim ("Most of these things will become easier once ...").',
        'Shape: a negation run ("X isn\'t the enemy. Neither are A, B, or C.") with a wry closer ("without ever being properly introduced") became one sentence of things you stop doing ("once you stop being afraid of ..., and when you stop fighting ...").'))
    P.append(p40('40-HG27-kid', 'HG27-r1',
        ('Listen until the kid is willing to come closer.', 'occasionally sit down.'),
        ('Then listen to her when she wants to come closer.', 'relax a bit.'),
        'AI (Medium), batch 429 (%s)' % B429,
        'Human (Medium), batch 430 (%s)' % res('b430'),
        [L['hedge'], O['reason'], L['casual'], L['quip_out']],
        'Changed person: "the kid" became "her" (a gender for the little one, which the lane has caught before); "enough small promises" became "some of your promises".',
        'Shape: two tight commands with a wry image ("so the guards can occasionally sit down") became a hedged pair with a because-clause ("It\'s easiest if ..., too, because then the guards can relax a bit.").'))
    P.append(p40('40-HG12-sober', 'HG12-r1',
        ('Self-hypnosis became much more useful for me', 'trust and precision.'),
        ('Have I mentioned I\'m a big fan of self-hypnosis?', 'work very well for me.'),
        'AI (High, a 170-word window), batch 429 (%s)' % B429,
        'Human (High), the section one 513-word window, batch 431 (%s)' % res('b431'),
        [L['q'], L['first'], L['hedge'], L['casual'], L['notxy'], L['closer']],
        'Invented present fact: "I was sober" became "I\'m sober right now"; the point "The larger issue was trust and precision" is dropped.',
        'Shape: four flat declaratives ending on a verdict ("The larger issue was trust and precision.") became a chatty first-person opener with a rhetorical question, scare quotes ("a \\"professional\\""), and a suspicion ("but I suspect that\'s not even the main reason").'))
    P.append(p40('40-HG12-essay', 'HG12-r1',
        ('When I’m giving the suggestion', 'little essay called yes.'),
        ('When I do it on my own, I can detect', 'or something else.'),
        'AI (High, a 170-word window), batch 429 (%s)' % B429,
        'Human (High), batch 431 (%s); the first sentence read Human (High, 170 words) in 4.1\'s first check (41a, %s)' % (res('b431'), W41A),
        [L['quip_out'], L['people'], O['poly']],
        'Drops the third sentence (catching the body\'s no before the conscious mind argues it into a yes).',
        'Shape: a noun list ("guidance, fear, avoidance, wishful thinking, or something I don\'t yet understand") became clauses about what the image tells me, joined by "or ... or ... or"; the closing quip ("writes a persuasive little essay called yes") is gone.'))
    P.append(p40('40-HG18-orient', 'HG18-r1',
        ('Name the day or date.', 'Then do something normal.'),
        ('It is a good idea to say to yourself what day it is', 'doing something normal.'),
        'AI (High), the whole section one 317-word window, batch 429 (%s)' % B429,
        'Human (High), 465 words, AI likelihood 0.07, batch 431 (%s)' % res('b431'),
        [L['join'], O['soft'], O['runon']],
        'Drops "repeating the count is not proof of a complete return" and "only" ("Note only what actually appeared"), and "stand only when steady" became "stand up and make sure that you are oriented".',
        'Shape: six short commands became two long run-on sentences opened by "It is a good idea to".'))
    P.append(p40('40-HG19-response', 'HG19-r1',
        ('The response may be a phrase', 'today’s practice is over.'),
        ('You might hear a phrase', 'enough listening for today.'),
        'AI (High), the whole section one 220-word window, batch 429 (%s)' % B429,
        'Human (High), 298 words, batch 431 (%s)' % res('b431'),
        [L['people']],
        'Garbled: "an urge to stop" became part of "know that your need to do something".',
        'Shape: a thirteen-noun list ("a phrase, sensation, memory, color, child, protector, pain, warmth, silence, task, ...") became verbs the reader does ("You might hear a phrase, feel a sensation, notice a memory, see a color, be contacted by ...").'))
    P.append(p40('40-HG19-believe', 'HG19-r1',
        ('Listen to all of it. Believe none of it automatically.', None),
        ('Listen to it all and believe none of it.', None),
        'AI (High), batch 429 (%s)' % B429,
        'Human (High), batch 431 (%s)' % res('b431'),
        [L['join'], L['notxy']],
        'Changed strength: "automatically" is gone, so "believe none of it" now means believe nothing.',
        'Shape: two parallel imperatives (a tidy closing pair) became one sentence.'))
    P.append(p40('40-HG23-rule', 'HG23-r1',
        ('Altered-state rule: do not ask for hidden truth', 'Ask for capacity, not content.'),
        ('NOTE: If it is medically unsafe for you', 'destabilize to know it!'),
        'AI (High), the whole section one 317-word window, batch 429 (%s)' % B429,
        'Human (High), 370 words, batch 431 (%s)' % res('b431'),
        [O['note'], O['caps'], L['people'], L['closer'], L['notxy'], O['excl']],
        'Drops the closing rule "Ask for capacity, not content."',
        'Shape: a label-colon rule with a long condition list, then two short verdicts, became a capitalised "NOTE:" with an "If it is ... for you, or you are ..." condition, and an exclamation; the "not content" aphorism is gone.'))
    P.append(p40('40-HG23-tuesday', 'HG23-r1',
        ('That pressure can produce flooding', 'generally worse Tuesday.'),
        ('This can lead to flooding', 'making your day suck more.'),
        'AI (High), batch 429 (%s)' % B429,
        'Human (High), batch 431 (%s); Human (High, 257-word window) in 4.1\'s first check (41a, %s)' % (res('b431'), W41A),
        [L['quip_out'], L['casual']],
        '',
        'Shape: a list ending on a wry punchline ("or a generally worse Tuesday") ended instead on blunt slang ("and just generally making your day suck more").'))
    P.append(p40('40-HG26-relationship', 'HG26-r1',
        ('Use self-hypnosis as a relationship with yourself.', 'substitute for it.'),
        ('Self-hypnosis is a relationship you have with yourself', 'more than that.'),
        'AI (High), the whole section one 361-word window, batch 429 (%s)' % B429,
        'Human (High), 532 words, batch 431 (%s)' % res('b431'),
        [L['join'], L['hedge']],
        'Changed strength: "the guide shouldn\'t become a substitute for [actual care]" became "sometimes the situation calls for more than that".',
        'Shape: a command and a "When X, Y shouldn\'t Z" rule became one soft compound sentence with "sometimes".'))
    P.append(p40('40-HG26-feedback', 'HG26-r1',
        ('If the practice makes ordinary life more loving', 'outside support.'),
        ('The ultimate feedback on whether your process is working well', 'support from others.'),
        'AI (High), batch 429 (%s)' % B429,
        'Human (High), batch 431 (%s)' % res('b431'),
        [L['people'], L['concrete'], 'other: topic sentence added at the start'],
        '',
        'Shape: two balanced conditionals ("If the practice makes ordinary life more ..., continue gently. If it makes ordinary life less stable, ...") became sentences about the reader ("If you\'re being more loving ...", "If you\'re functioning less well ...") with fuller particulars ("getting enough sleep, eating, grounding yourself, ..."), after a new topic sentence.'))
    P.append(p40('40-HG36-lighting', 'HG36-r1',
        ('Intensity then gets mistaken for meaning.', 'excellent lighting.'),
        ('The problem is that people think', 'should believe it.'),
        'AI (High), the whole section one 355-word window, batch 429 (%s)' % B429,
        'Human (High), 499 words, batch 431 (%s)' % res('b431'),
        [L['people'], L['join'], L['casual'], O['anaphora']],
        '"or shame, grief, anger, longing ... asking for care" became "shame/grief/anger or other parts coming out".',
        'Shape: an abstract opener ("Intensity then gets mistaken for meaning.") became people thinking ("The problem is that people think that because ..."), and three tidy "X isn\'t automatically Y" clauses with a quip became a casual "Just because ..., just because ... and just because ..." run. Emulate made an anaphora here, and 4.0 passed it.'))
    P.append(p40('40-HG01-nav', 'HG01-r1',
        ('Begin with Quick start', 'together in Appendix K.'),
        ('This is a very big guide.', 'All sources used are in Appendix K.'),
        'AI (Low), one 83-word window, AI likelihood 0.98, batch 429 (%s)' % B429,
        'Human (High), 157 words, batch 431 (%s)' % res('b431'),
        [L['split'], L['people'], L['casual'], L['uneven']],
        '',
        'Shape: a compressed instruction sentence and a noun-list sentence ("extra tools for questions, NLP language, anxiety, daydreaming, ...") became a looser walk-through ("To make it easier, you can ... Then, you can ... You can also ...") with the list as activities ("working with anxiety, working with daydreams, ... what to do if you experience ...").'))
    # same input, two samples: the passing one here, the failing one in the failures
    P.append(p40('40-HG04-h', 'HG04-r1',
        ('As you listen, a sensation, image, phrase', 'real-world action it calls for.'),
        ('you\'ll follow whatever you notice', 'any real-world actions.'),
        'AI (High), the whole section one 337-word window, batch 429 (%s)' % B429,
        'Human (High), 356 words, batch 437 (%s)' % res('b437'),
        [O['aside'], O['etc'], L['uneven'], O['noise'], L['join']],
        '"objection" became "rebellion"; "Use warmth, a boundary, direction, or more time" became "to be responsive & warm, to create a boundary, to proceed, etc."',
        'Shape: the list became a dashed aside inside an instruction ("you\'ll follow whatever you notice - sensation, image, ... - as you\'re invited"), the next list ends on "etc.", ampersands appear, and a three-word sentence stands alone ("Complete the return."). The same input\'s sample emu-a kept two colon lists and read AI (fail-40-HG04-a).',
        folder='emu-h'))
    P.append(p40('40-HG16-a', 'HG16-r1',
        ('Pause there. Don’t obey immediately', 'Wake up inside the influence.'),
        ('If you’re being hypnotically influenced, stop.', 'you’re being influenced.'),
        'AI (High), the whole section one 543-word window, batch 429 (%s)' % B429,
        'Human (High), the section\'s first 300-word window (its other 418-word window, the list, read AI: fail-40-HG16-a), batch 431 (%s); with the list from sample emu-h the whole section read Human (High, 744 words), batch 437 (%s)' % (res('b431'), res('b437')),
        [L['uneven'], L['quip_out'], L['casual'], 'other: conditional "If you..." opening added'],
        '"Don\'t obey immediately" became "Don\'t listen" (stronger and different); "automatic rebellion" lost "automatic".',
        'Shape: a slogan closer ("Wake up inside the influence.") became a plain step ("just stop and realize that you\'re being influenced"), after a one-word command ("stop."). The same window\'s "By a screen? By a specific ad? ..." run passed 4.0 and read AI in 4.1 (fail-41-byx).'))
    P.append(p40('40-HG29-i-daydream', 'HG29_30-r1',
        ('For daydreaming:', 'what I need to deal with.”'),
        ('Daydreaming: Show me if this daydream', 'let me deal with my life.'),
        'AI (High), the whole section one 585-word window, batch 429 (%s)' % B429,
        'Human (High), 643 words, batch 438 (%s)' % res('b438'),
        [L['notxy'], L['join']],
        '"reveal the guidance inside it" became "Show me if this daydream is useful and guiding me"; "gently" is gone.',
        'Shape: a parallel pair of conditional requests ("If this daydream is useful, reveal .... If it is avoidance, bring me ...") became one either-or question and a back-reference ("Show me if ..., or if .... If it is the latter, ..."). The same input\'s sample emu-a kept the parallel pair and read AI (fail-40-HG29-a).',
        folder='emu-i'))
    # refix: the lane's meaning-fixed text, which read AI, sent back to Emulate
    P.append(p40('40-refix-HG11', 'HG11-fxw1',
        ('Love without analysis can become fantasy', 'correct the others.'),
        ('Without the mind of love the mind of analysis can be sterile.', 'can correct each other.'),
        'AI (High), the whole fixed section one 239-word window, batch 434 (%s). The lane\'s meaning-fixed text, mostly Emulate\'s words with the published points put back.' % res('b434'),
        'Human (High), 239 words, batch 443 (%s); in 4.1 its lines read only Human (Medium) and Human (Low) (batch 480\'s recheck and 2026-10-29)' % res('b443'),
        [L['notxy'], O['anaphora'], L['split']],
        '',
        'Shape: two chiasmus pairs ("A without B can become X, B without A can become Y") became four separate "Without X, Y can be Z" sentences: the paired balance is broken, but an anaphora is made, and in 4.1 that run sat at Medium and Low.',
        folder='emu-r', kind='pass'))
    P.append(p40('40-refix-HG19', 'HG19-fxw1',
        ('You’re asking your conscious mind to listen without forcing an answer.', None),
        ('Ask your conscious mind to listen.', None),
        'AI (High), the whole fixed section one 289-word window, batch 434 (%s)' % res('b434'),
        'Human (High), 302 words, batch 443 (%s); Human (High, a 1863-word window) in 4.1\'s first check (41a, %s)' % (res('b443'), W41A),
        [L['def'], L['uneven']],
        'Drops "without forcing an answer".',
        'Shape: a sentence that explains what you are doing ("You\'re asking ... to listen without forcing an answer.") became a five-word command.',
        folder='emu-r'))
    P.append(p40('40-HG12-outside', 'HG12-r1',
        ('An outside hypnotist can’t easily conduct', 'with the system itself.'),
        ('A hypnotist working on me', 'regulated and safe.)'),
        'AI (Medium, a 71-word window), batch 429 (%s)' % B429,
        'Human (High), the section one 513-word window, batch 431 (%s). In 4.1 the dropped sentence, reworded by the lane ("But doing it myself has one advantage nobody outside can copy: immediate dialogue with my own system."), read AI (Medium, 17 words) in check 41a (%s), and put back word for word by the comprehension pass it read AI (Low, 0.793, 16 words) on 2026-10-29 (fix-20261029/recheck/read/RESULT-A.json)' % (res('b431'), W41A),
        [L['closer'], L['first'], O['caps'], O['aside']],
        'Drops the closing claim (self-hypnosis has one advantage nobody outside can duplicate); "they" became "he" for the hypnotist.',
        'Shape: three sentences ending on a colon aphorism ("Self-hypnosis simply has one advantage nobody outside can duplicate: immediate dialogue with the system itself.") became one first-person sentence ("A hypnotist working on me ... since he isn\'t IN my mind.") and a bracketed "(Of course, ...)" concession, with no closer. Batch 482\'s target T3 is that closer.'))
    P.append(p40('40-refix-HG33-quip', 'HG33-fxw1',
        ('Others settle with warmth, darkness', 'around the anxiety.'),
        ('You may find that you settle down', 'technology you use to relax, etc.'),
        'AI (High), the whole fixed section one 868-word window, batch 434 (%s)' % res('b434'),
        'Human (High), 913 words, batch 443 (%s); the paragraph read Human (High, 201 words) in batch 481\'s recheck (fix-20261026/b481/recheck/read/RESULT-B.json) until the joke was put back (reverse-X9.10)' % res('b443'),
        [L['quip_out'], L['closer'], O['soft'], O['etc']],
        'Drops the published joke and its point (use the one support that helps rather than piling them up).',
        'Shape: a list sentence and a closing joke ("rather than building a tiny wellness trade show around the anxiety") became one hedged list sentence ending on "etc.", with no closer.',
        folder='emu-r'))
    return P
