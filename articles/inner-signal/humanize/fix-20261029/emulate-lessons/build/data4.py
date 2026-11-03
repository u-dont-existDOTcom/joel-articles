"""Failures: Emulate's own text that read AI, with the input it came from. 'kept_or_made' names the AI shape still in it."""
from ex import T, J
from data1 import L, O

SCR = 'fix-20261022/screen/RESULT-S.json'
PUB17 = 'fix-20261018/emu-bc/HG17-pub2.txt'
FX17 = 'fix-20261018/emu-be/HG17-fx1.txt'
APPC_IN = 'fix-20261018/emu-bg/HG32-pr1.txt'
W41B = 'fix-20261020/result41/WINDOWS-41b.json'
W41R2B = 'fix-20261020/result41/WINDOWS-41r2-b.json'
W41R3A = 'fix-20261020/result41/WINDOWS-41r3-a.json'
R1022A = 'fix-20261022/recheck/RESULT-A.json'
R1023B = 'fix-20261023/recheck/RESULT-B.json'
RB2 = 'fix-20261023/recheck-b2/RESULT-B.json'
RA3 = 'fix-20261023/recheck-a3/RESULT-A.json'
R1025B = 'fix-20261025/recheck/RESULT-B.json'
R480A = 'fix-20261026/b480/recheck/read/RESULT-A.json'
R480B = 'fix-20261026/b480/recheck/read/RESULT-B.json'
R481A = 'fix-20261026/b481/recheck/read/RESULT-A.json'
R481B = 'fix-20261026/b481/recheck/read/RESULT-B.json'
R1029A = 'fix-20261029/recheck/read/RESULT-A.json'
R1029B = 'fix-20261029/recheck/read/RESULT-B.json'
API472 = 'fix-20261023/b472/API-CHECKS.md'

K = {  # the AI shapes the failing text kept or made
    'examples': 'a run of vivid examples or options in one breath',
    'fragments': 'verbless fragment list or one-word fragment sentences',
    'colonlist': 'colon followed by a list',
    'parallel': 'parallel or anaphoric run (If it is really X ...; By X? By Y?; If you X, Y ...)',
    'steps': 'instruction-step run: one short command per sentence',
    'permission': 'permission formula ("You don\'t have to X", "you can Y")',
    'contrast': 'balanced good/bad or X/Y contrast',
    'aphorism': 'aphorism or tidy maxim',
    'coach': 'coach or option register ("You may want to", "You can", "There are all sorts of ways")',
    'rhetq': 'rhetorical question answered at once',
    'triple': 'list of three abstract items',
    'labelcolon': 'label with a colon before each item',
}


def pairs():
    P = []

    def f(pid, batch, det, kind, inp, in_read, emu, emu_read, labels, kept, meaning, note):
        return dict(id=pid, batch=batch, detector=det, kind=kind, input=inp, input_reading=in_read,
                    emulate=emu, emulate_reading=emu_read, labels=labels, kept_or_made=kept,
                    meaning_error=meaning, note=note)

    # ---- 4.1, the screening post of 2026-10-22: raw samples, the sibling sample of the same input passed ----
    P.append(f('fail-41-screen-S1-metaphors', 'screen 2026-10-22 (emu-bc)', 'Pangram 4.1', 'fail',
        T(PUB17, 'Choose one purpose, one starting anchor', 'stops helping.'),
        'The published section read AI (High) in the 4.0 baseline (batch 429); see screen-S2-metaphors',
        T('fix-20261018/emu-bc/HG17-pub2.out.txt', 'Keep it simple. One reason for the trance', 'but do it consciously.'),
        'AI (Low, 0.727, 15 words) and AI (Medium, 0.979, 49 words), screening post S1 (%s)' % SCR,
        [L['q'], O['poly'], L['quip_out'], O['etc']],
        [K['fragments'], K['examples']],
        '',
        'Emulate kept the verbless triad ("One reason for the trance, one starting anchor or image, one way to get back.") and turned the options into two long "or ... or ... or" questions, a run of vivid examples in one breath. Sample bd of the same input (screen-S2-metaphors) made the options things the reader may want to do, ended them on "etc.", and read Human (High).'))
    P.append(f('fail-41-screen-S1-imagery', 'screen 2026-10-22 (emu-bc)', 'Pangram 4.1', 'fail',
        T(PUB17, 'Imagery is optional.', 'reverse the journey when you finish.'),
        'The published section read AI (High) in 4.0 (batch 429)',
        T('fix-20261018/emu-bc/HG17-pub2.out.txt', "There's no need for any imagery at all", 'meaningful in that world.'),
        'AI (Low, 0.503, 15 words), AI (Low, 0.757, 25 words) and AI (Low, 11 words), screening post S1 (%s)' % SCR,
        [L['colon'], L['split'], L['casual']],
        [K['examples'], K['steps']],
        '',
        'Emulate kept the noun list nearly word for word ("sensation, rhythm, movement, words, spatial, simple knowing, or no response at all") and split the colon instruction into separate short commands. Sample bd (screen-S2-imagery) rewrote the list with a quoted inner phrase and joined the commands into one hedged sentence, and read Human (High).'))
    P.append(f('fail-41-screen-S3-active', 'screen 2026-10-22 (emu-be)', 'Pangram 4.1', 'fail',
        T(FX17, 'If your state of being still', 'disappear inward.'),
        'AI in 4.1, windows marked humanized (whole-guide check 41r3-a, %s)' % W41R3A,
        T('fix-20261018/emu-be/HG17-fx1.out.txt', 'If you find your state of stillness', 'without trying to disappear.'),
        'AI (Medium, 0.989, 17 words) for "You don\'t have to relax more ..." and AI (High, 0.996, 51 words) for the instructions after it, screening post S3 (%s)' % SCR,
        [L['split'], L['casual']],
        [K['permission'], K['contrast'], K['steps']],
        '',
        'Emulate turned the explanation into a permission formula with a contrast ("You don\'t have to relax more to go deeper into hypnosis, you can become more alert.") and kept a run of commands. Sample bf of the same input (screen-S4-active) wrote "Instead of getting more relaxed ..., try getting more alert." and one long spoken sentence, and read Human (High).'))
    P.append(f('fail-41-screen-S5-ifrun', 'screen 2026-10-22 (emu-bg)', 'Pangram 4.1', 'fail',
        T(APPC_IN, 'If it’s true, it can handle my questions.', 'give up my adult self.”'),
        'AI (High): this prose (Claude\'s, batch 469) read AI as one 518-word window in check 41r2-b (%s)' % W41R2B,
        T('fix-20261018/emu-bg/HG32-pr1.out.txt', 'Remember: if it’s true', 'give up being an adult.'),
        'AI (Low, 57 words, from "Let me slow it down" through "Remember: if it\'s true ..."), AI (Medium, 9 words), AI (Low, 13 words), AI (Low, 17 words), screening post S5 (%s)' % SCR,
        [O['note'], O['anaphora'], O['formal']],
        [K['parallel'], K['aphorism']],
        '',
        'The input had already broken the parallel ("If it\'s true, it can handle ... If it\'s real love, it\'ll survive ... And real guidance will ... Anything that\'s really for me ..."). Emulate rebuilt it into four identical "If it\'s really X, it will Y" maxims behind a "Remember:" label. Emulate moved toward the AI shape here; sample bh did the same (four "If it\'s ..." lines, AI Medium and Low).'))
    P.append(f('fail-41-screen-S5-obey', 'screen 2026-10-22 (emu-bg)', 'Pangram 4.1', 'fail',
        T(APPC_IN, 'I don’t have to obey it, and I don’t have to attack it either.'),
        'AI (High), as fail-41-screen-S5-ifrun (%s)' % W41R2B,
        T('fix-20261018/emu-bg/HG32-pr1.out.txt', 'I don’t have to obey. I don’t have to attack.'),
        'AI (Medium, 12 words), screening post S5 (%s)' % SCR,
        [L['split']],
        [K['parallel'], K['permission']],
        '',
        'Splitting one joined sentence made a matched pair of two short sentences.'))
    P.append(f('fail-41-screen-S6-fragments', 'screen 2026-10-22 (emu-bh)', 'Pangram 4.1', 'fail',
        T(APPC_IN, 'Before acting on it, look for the usual signs', 'money or sex from you.'),
        'AI (High), as fail-41-screen-S5-ifrun (%s)' % W41R2B,
        T('fix-20261018/emu-bh/HG32-pr1.out.txt', 'Before giving in to whatever it is', 'money or sex from you.'),
        'Human (Low, 14 words) for the first sentence, then AI (Low, 4 words, "Sexual charge. Spiritual superiority.", marked humanized) and AI (Medium, 41 words, marked humanized), screening post S6 (%s)' % SCR,
        [L['split_list'], O['quote']],
        [K['fragments']],
        '',
        'A counter-case for "list split into sentences": the list was split into one- and two-word sentences ("Urgency. Secrecy. Shame.") and read AI, marked humanized.'))
    P.append(f('fail-41-screen-S6-guide', 'screen 2026-10-22 (emu-bh)', 'Pangram 4.1', 'fail',
        T(APPC_IN, 'You can tell a good guide', 'A bad guide can’t.'),
        'AI (High), as fail-41-screen-S5-ifrun (%s)' % W41R2B,
        T('fix-20261018/emu-bh/HG32-pr1.out.txt', 'A good guide will help you to become more of your adult self.', 'place of your adult self.'),
        'AI (Medium, 52 words, marked humanized), screening post S6 (%s)' % SCR,
        [O['q2s'], O['reason'], O['formal']],
        [K['contrast']],
        '',
        'The input\'s question ("And can they take your no?") became a statement, and the passage became a matched good guide / bad guide pair with a because-clause. Joel\'s own Appendix C, written after this screen, read Human (High) (his answer 13).'))
    P.append(f('fail-41-screen-S6-commands', 'screen 2026-10-22 (emu-bh)', 'Pangram 4.1', 'fail',
        T(APPC_IN, 'If you see several of these, slow down.', 'get some counsel and so on.'),
        'AI (High), as fail-41-screen-S5-ifrun (%s)' % W41R2B,
        T('fix-20261018/emu-bh/HG32-pr1.out.txt', 'If many of the above apply, then slow down.', 'get counsel, etc.'),
        'AI (Medium, 30 words), AI (High, 6 words, "Don\'t go deeper into trance."), AI (Medium, 5 words), AI (High, 15 words), AI (Medium, 52 words), all marked humanized, screening post S6 (%s)' % SCR,
        [L['split'], O['etc']],
        [K['steps']],
        '',
        'The input\'s joined command ("Don\'t go deeper into trance, and don\'t make a decision you can\'t undo.") was split into two short commands, and each short command read AI on its own.'))
    # ---- 4.1: Emulate text that had passed in 4.0 or in a screen, read AI in place ----
    P.append(f('fail-41-byx', '431/437 (emu-a, HG16) read in the recheck of 2026-10-22', 'Pangram 4.1 (passed 4.0)', 'fail-after-passing-4.0',
        T('fix-20261018/emu-a/HG16-r1.txt', 'Screens, advertising, politics', 'and repetition all do it.'),
        'AI (High), the whole section one 543-word window, 4.0 baseline (batch 429)',
        T('fix-20261018/emu-a/HG16-r1.out.txt', 'By a screen?', 'By repetition?'),
        'Pangram 4.0: Human (High), the first 300-word window of batch 431 and the 744-word section of batch 437. Pangram 4.1: AI (Low, 3 words), AI (Low, 10 words), AI (Medium, 10 words), AI (Low, 7 words), AI (Low, 2 words), recheck of 2026-10-22 part A (%s)' % R1022A,
        [L['q'], L['split_list'], O['anaphora']],
        [K['parallel'], K['fragments']],
        '',
        'A list turned into a run of ten fragment questions ("By a screen? By a specific ad? ...") passed 4.0 and failed 4.1. Claude\'s fix b472-s1b, the same items in brackets ending on "etc.", read Human (High) through the API (%s) and in place.' % API472))
    P.append(f('fail-41-emu-ax-if', '463 (emu-ax, HG18) read in the recheck of 2026-10-22', 'Pangram 4.1 (passed 4.0)', 'fail-after-passing-4.0',
        T('fix-20261018/emu-ax/HG18-aw1.txt', 'Reverse whatever you used to enter.', 'and adult judgment.'),
        'AI (High), the whole section one 317-word window, 4.0 baseline (batch 429)',
        T('fix-20261018/emu-ax/HG18-aw1.out.txt', "Make sure to reverse anything you've done", 'under control of the adult mind.'),
        'Pangram 4.0: Human (High), 524 words, batch 463 (HG18-wb). Pangram 4.1: AI (High) through the API (b472_s2_base, %s); AI (Medium, 25 words) and AI (High, 36 words), recheck of 2026-10-22 part A (%s)' % (API472, R1022A),
        [O['soft'], L['casual'], O['aside'], L['people']],
        [K['parallel'], K['steps']],
        '',
        'Emulate softened every command ("Make sure to", "make sure you") and added contractions and an aside, but kept the run of "If you\'ve X, (make sure you) Y" sentences. 4.0 passed it; 4.1 did not. Its re-run (seam-bk-reverse) kept the run too and passed in a pair check, so the run alone does not decide it.'))
    P.append(f('fail-41-emu-ax-look', '463 (emu-ax, HG18) read in recheck A3', 'Pangram 4.1 (passed 4.0)', 'fail-after-passing-4.0',
        T('fix-20261018/emu-ax/HG18-aw1.txt', 'Name the day or date.', 'near, and far.'),
        'AI (High), 4.0 baseline (batch 429)',
        T('fix-20261018/emu-ax/HG18-aw1.out.txt', 'When you come out, remind yourself what day', 'something near, and something far.'),
        'Pangram 4.0: Human (High), batch 463 (HG18-wb). Pangram 4.1: AI (Low, 0.644, 31 words), AI (Low, 0.575, 7 words: "Look to your left and your right."), AI (Low, 0.531, 7 words: "Look at something near, and something far."), recheck A3 (%s)' % RA3,
        [L['split_list'], L['split']],
        [K['steps']],
        '',
        'Emulate split "Look left, right, near, and far." into two short commands. Joined back into one comma-run instruction by sample bo, it read Human (High, 0.995) in recheck A4 (b475-reorient).'))
    P.append(f('fail-41-emu-ba-ways', 'emu-ba (HG17, installed unscreened) read in check 41r3-a', 'Pangram 4.1', 'fail',
        T('fix-20261018/emu-ba/HG17-az1.txt', 'Counting is one way in.', 'can also organize attention.'),
        'AI (High), 4.0 baseline (batch 429)',
        T('fix-20261018/emu-ba/HG17-az1.out.txt', 'There are all sorts of ways to do this.', 'make use of curiosity.'),
        'AI (Medium, 9 words, marked humanized) for the first sentence and AI (High, a 342-word window, marked humanized) for the rest, whole-guide check 41r3-a (%s)' % W41R3A,
        [L['people'], O['soft'], L['casual']],
        [K['coach'], K['examples']],
        '',
        'A counter-case for "abstract nouns turned into people doing things": the nouns became things "You might just" do, in a casual frame, and it still read AI, marked humanized. The whole sample read AI in 48 windows, 42 of them marked humanized: in 4.1 a raw Emulate sample that was never screened was not safe.'))
    P.append(f('fail-41-emu-ba-not', 'emu-ba (HG17) read in check 41r3-a', 'Pangram 4.1', 'fail',
        T('fix-20261018/emu-ba/HG17-az1.txt', 'You don’t have to surrender, play asleep, or obey anyone.'),
        'AI (High), 4.0 baseline (batch 429)',
        T('fix-20261018/emu-ba/HG17-az1.out.txt', 'They are not about surrendering, playing asleep, or obeying someone.'),
        'AI (Low, 10 words), whole-guide check 41r3-a (%s)' % W41R3A,
        [O['formal'], L['subj']],
        [K['triple']],
        '',
        'Emulate moved the sentence away from the reader ("You don\'t have to ..." became "They are not about ...") and kept the list of three.'))
    P.append(f('fail-41-emu-w-q', '451 (emu-w, HG35) read in check 41b', 'Pangram 4.1 (passed 4.0)', 'fail-after-passing-4.0',
        T('fix-20261018/emu-w/HG35-fxw1.txt', 'How do we hold all of this?', None),
        'The lane\'s meaning-fixed text; its section read AI in places in 4.0 (batch 434)',
        T('fix-20261018/emu-w/HG35-fxw1.out.txt', 'So how do we hold all of this?', 'it can all be true.'),
        'Pangram 4.0: Human (High), the section\'s 1144 words, batch 451 (HG35-refix3). Pangram 4.1: AI (Low, 8 words) for the question, and the answer after it, in the lane\'s fixed words, AI (High, 29 words), check 41b (%s)' % W41B,
        [O['conn']],
        [K['rhetq']],
        '',
        'A counter-case for "a question added": a question the next sentence answers at once ("So how do we hold all of this? We simply remember ...") read AI.'))
    P.append(f('fail-41-br-fix', '477 (br)', 'Pangram 4.1', 'fail-unstable',
        J('fix-20261023/b477/EDITS-b477.json', '0/old'),
        'AI (Low, 0.503, 11 words) for "You don\'t have to fix this. I\'m here now.", recheck of 2026-10-23 part B (%s)' % R1023B,
        T('fix-20261023/b477/br/HG-B-love.out.txt', 'You don’t have to fix it.', 'to listen to you.”'),
        'Human (Low, 0.638, 36 words) in recheck B2 (%s); AI (Low, 0.64, 7 words) and AI (Medium, 0.987, 29 words) on 2026-10-25 (%s); Human (Medium, 0.909) and Human (High, 0.994) in batch 480\'s recheck (%s); AI (Low, 7 words) and AI (High, 29 words) on 2026-10-29 (%s)' % (RB2, R1025B, R480B, R1029B),
        [L['join'], O['minimal']],
        [K['permission']],
        '',
        'Emulate changed two words and joined two short lines; the permission formula ("You don\'t have to fix it.") stayed, and the line flipped between Human and AI in five checks.'))
    P.append(f('fail-41-emu-bf-ones', 'screen 2026-10-22 (emu-bf), installed; read on 2026-10-29', 'Pangram 4.1', 'fail-context',
        T('fix-20261018/emu-bf/HG17-fx1.txt', 'One purpose, one anchor or image to start', 'or neutral witnessing).'),
        'AI in 4.1 (the installed sample ba read AI, marked humanized, in check 41r3-a)',
        T('fix-20261018/emu-bf/HG17-fx1.out.txt', 'One thing you\'re doing, one anchor/image', 'whatever) for yourself.'),
        'Human (High) in the screening post (%s), in batch 480\'s recheck (0.994, %s) and in batch 481\'s (0.997, %s); AI (Low, 0.649, 34 words) on 2026-10-29 (%s), after the comprehension fixes changed the sentences around it' % (SCR, R480A, R481A, R1029A),
        [O['etc'], O['aside'], L['casual']],
        [K['fragments'], K['examples']],
        '',
        'Emulate kept the verbless "One X, one Y, one Z" triad, with the options in brackets ending on "whatever". It read High three times, then AI when its neighbours changed. Batch 482\'s writers rewrote it (target T5).'))
    P.append(f('fail-41-emu-r-somatic', '443 (emu-r, HG33), read on 2026-10-29', 'Pangram 4.1', 'fail-context',
        T('fix-20261018/emu-r/HG33-fxw1.txt', 'Other body approaches that may help include', 'massage gun used carefully, etc.'),
        'The lane\'s meaning-fixed text, whose section read AI (High, 868 words) in batch 434 (fix-20261018/b434/b434-results.json)',
        T('fix-20261018/emu-r/HG33-fxw1.out.txt', 'There are many other somatic approaches you can try', 'a massage gun, etc.'),
        'Human (High, 201 words) in batch 480\'s and 481\'s rechecks (%s, %s); AI (Low, 0.793, 28 words) on 2026-10-29 (%s), when the published quip after it was restored (reverse-X9.10, AI High)' % (R480B, R481B, R1029B),
        [O['etc']],
        [K['examples']],
        '',
        'A run of six examples ending on "etc." read High twice and AI once its next sentence became the restored "tiny wellness trade show" quip. Neighbours decide short windows.'))
    # ---- 4.0: the sibling sample of the same input passed ----
    P.append(f('fail-40-HG04-a', '431 (emu-a, HG04)', 'Pangram 4.0', 'fail',
        T('fix-20261018/emu-a/HG04-r1.txt', 'As you listen, a sensation, image, phrase', 'real-world action it calls for.'),
        'AI (High), the whole section one 337-word window, batch 429',
        T('fix-20261018/emu-a/HG04-r1.out.txt', 'As you do the induction, something will happen', 'to make this work.'),
        'AI (High, 108 words), batch 431 (fix-20261018/b431/b431-results.json)',
        [O['etc'], L['casual']],
        [K['colonlist']],
        '',
        'Emulate made two colon lists ("something will happen that you can notice: a sensation, an image, ..."; "This will vary based on what you need: warmth, a boundary, direction, time, and more."). Sample emu-h of the same input put the list in dashes and read Human (High) (40-HG04-h).'))
    P.append(f('fail-40-HG16-a', '431 (emu-a, HG16)', 'Pangram 4.0', 'fail',
        T('fix-20261018/emu-a/HG16-r1.txt', 'Permissive words can still conceal coercion.', 'merely suggestive.'),
        'AI (High), the whole section one 543-word window, batch 429',
        T('fix-20261018/emu-a/HG16-r1.out.txt', 'Language that’s permissive but that still takes your choice away includes:', 'or use suggestions.'),
        'AI (High, a 418-word window running through the list), batch 431 (fix-20261018/b431/b431-results.json)',
        [O['formal']],
        [K['colonlist'], K['labelcolon']],
        '',
        'Emulate kept a colon-introduced list with one gerund item per line. Sample emu-h of the same list numbered the items as "1) Utilizing ...", ran them as full clauses, and read Human (High) in 4.0 (batch 437).'))
    P.append(f('fail-40-HG29-a', '431 (emu-a, HG29+30)', 'Pangram 4.0', 'fail',
        T('fix-20261018/emu-a/HG29_30-r1.txt', 'For daydreaming:', 'what I need to deal with.”'),
        'AI (High), the whole section one 585-word window, batch 429',
        T('fix-20261018/emu-a/HG29_30-r1.out.txt', 'Prompt for daydreaming:', 'needs to be dealt with.'),
        'AI (High, a 163-word window), batch 431 (fix-20261018/b431/b431-results.json)',
        [L['casual']],
        [K['parallel'], K['labelcolon']],
        '',
        'Emulate kept the matched pair of conditional requests ("If this daydream has ..., please .... If it is only to avoid ..., please ..."). Sample emu-i broke the pair ("Show me if ..., or if .... If it is the latter, ...") and read Human (High) (40-HG29-i-daydream).'))
    return P
