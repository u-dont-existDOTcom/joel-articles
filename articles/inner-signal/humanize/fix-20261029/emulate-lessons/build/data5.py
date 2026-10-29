"""Reverse pairs: Emulate's words read Human in batch 481's recheck; the comprehension fix of 28 October, which put back
the published point (often its published shape), read AI on 2026-10-29. Input = the text that read AI, emulate = Emulate's."""
from ex import T, J
from data1 import L, O

KEPT = 'fix-20261028/comprehension/fix/KEPT.json'
R481A = 'fix-20261026/b481/recheck/read/RESULT-A.json'
R481B = 'fix-20261026/b481/recheck/read/RESULT-B.json'
R480A = 'fix-20261026/b480/recheck/read/RESULT-A.json'
R1029A = 'fix-20261029/recheck/read/RESULT-A.json'
R1029B = 'fix-20261029/recheck/read/RESULT-B.json'


def pairs():
    P = []

    def r(pid, idx, labels, meaning, note, in_read, out_read, inp=None, emu=None):
        return dict(id=pid, batch='comprehension fix of 2026-10-28 (card %s), read on 2026-10-29' % pid.split('-', 1)[1],
                    detector='Pangram 4.1', kind='reverse',
                    input=inp or J(KEPT, 'fixes/%d/with' % idx), input_reading=in_read,
                    emulate=emu or J(KEPT, 'fixes/%d/replace' % idx), emulate_reading=out_read,
                    labels=labels, meaning_error=meaning, note=note)

    P.append(r('reverse-X1.11', 10, [L['colon'], L['short_list'], O['excl']],
        'Emulate\'s line drops the five outcomes (the published list), which the comprehension pass put back.',
        'The published list after a colon came back with the point, and the line read AI. Batch 482\'s writers (target T2) kept the outcomes as sentences about people, without the colon.',
        'AI (Low, 0.784, 21 words), 2026-10-29 part A (%s)' % R1029A,
        'Human (Medium, 0.989, 14 words, with the line before it) in batch 480\'s recheck (%s); "It\'s got to lead somewhere!" read Human (High) in batch 481\'s (%s)' % (R480A, R481A)))
    P.append(r('reverse-X1.5', 4, [L['notxy'], L['colon'], L['def']],
        'Emulate\'s line ("Put this screen on the shelf and conduct the practice.") lost "not a checklist to keep reading".',
        'The published "X; the practice is something you learn to conduct, not a checklist to keep reading" (semicolon, definition, "not X") read AI where Emulate\'s plain instruction had read High. Batch 482\'s target T1.',
        'AI (Low, 0.575, 35 words), 2026-10-29 part A (%s)' % R1029A,
        'Human (High, 0.999, 303 words), batch 481\'s recheck part A (%s)' % R481A))
    P.append(r('reverse-X5.3', 43, [L['def'], L['quip_out'], L['closer']],
        'Emulate\'s version had dropped what fractionation is and why you name it first.',
        'The published definition ("Fractionation means ...") and aphorism ("Used openly, it teaches that trance has a door in both directions.") came back, and read AI (Low and High). Emulate had kept only the instruction. Batch 482\'s target T7.',
        'AI (Low, 0.754, 27 words) and AI (High, 0.997, 12 words), 2026-10-29 part A (%s)' % R1029A,
        'Human (High, 0.998, 304 words), batch 481\'s recheck part A (%s)' % R481A,
        inp=J(KEPT, 'fixes/43/with', 'Fractionation means', 'door in both directions.')))
    P.append(r('reverse-X8.4', 82, [L['def'], L['notxy']],
        'Emulate\'s version had dropped what an embedded invitation is and that it mustn\'t hide a demand; only the example was left.',
        'A textbook definition ("An embedded invitation places a small direction inside a larger sentence.") and a "not X" rule came back and read AI (High). Batch 482\'s target T9.',
        'AI (High, 0.994, 22 words), 2026-10-29 part B (%s)' % R1029B,
        'Human (Medium, 1 word) and Human (High, 0.999, 329 words), batch 481\'s recheck part B (%s)' % R481B,
        inp=J(KEPT, 'fixes/82/with', 'An embedded invitation places', 'not hide a demand.')))
    P.append(r('reverse-X9.10', 101, [L['quip_out'], L['closer']],
        'Emulate\'s refix (batch 443) had dropped the published closing joke.',
        'The published joke ("rather than assembling a tiny wellness trade show around the anxiety") came back as the paragraph\'s last line and read AI (High), and Emulate\'s example sentence before it, High twice before, read AI (Low) too (fail-41-emu-r-somatic). Batch 482\'s target T14.',
        'AI (High, 0.997, 17 words) for the joke and AI (Low, 0.793, 28 words) for the sentence before it, 2026-10-29 part B (%s)' % R1029B,
        'Human (High, 0.998, 201 words): the paragraph ended on the example list, batch 481\'s recheck part B (%s)' % R481B,
        inp=J(KEPT, 'fixes/101/with', 'Use the support that actually helps', 'around the anxiety.')))
    P.append(r('reverse-X4.6', 31, [L['short_list']],
        '',
        'Two published examples ("such as warmth or steadiness") went into a bracketed aside and it read AI (Low, marked humanized). Batch 482\'s target T6.',
        'AI (Low, 0.784, 16 words, marked humanized), 2026-10-29 part A (%s)' % R1029A,
        'Human (High, 0.997, 326 words), batch 481\'s recheck part A (%s); Human (Medium, 0.987, 21 words with the sentence before) in batch 480\'s (%s)' % (R481A, R480A),
        inp=T('fix-20261029/recheck/TEXT-A.txt', '(You can borrow qualities such as warmth', 'who you are.)'),
        emu=T('fix-20261026/b481/recheck/TEXT-A.txt', '(You can borrow qualities, but', 'who you are.)')))
    P.append(r('reverse-X10.7', 112, [O['caps'], L['notxy']],
        'Emulate\'s line lost the published "while you build usable access"; its "what you OPEN yourself up to" changed the point.',
        'The published balance ("show you what\'s possible, while you build a way to get to it in everyday life") read AI (Low) where Emulate\'s shorter line had read High. Batch 482\'s target T16.',
        'AI (Low, 0.64, 20 words), 2026-10-29 part B (%s)' % R1029B,
        'Human (High, 0.999, 348 words), batch 481\'s recheck part B (%s)' % R481B))
    P.append(r('reverse-X11.13', 129, [L['short_list'], L['closer']],
        'Emulate\'s version dropped what may come (the bracketed list) and "without interpreting it as proof".',
        'In a label-colon recipe ("Autonomous signal: ...", "Deepener: ...", "Handoff: ..."), the restored bracketed list and caveat read AI (Low), and so did the next two restored lines (cards X11.14, X11.15). Batch 482\'s target T17.',
        'AI (Low, 0.531, 18 words), with X11.14 and X11.15 after it AI (Low, 0.721, 41 words) and AI (Low, 0.503, 17 words), 2026-10-29 part B (%s)' % R1029B,
        'Human (High, 0.999, 1671 words), batch 481\'s recheck part B (%s)' % R481B))
    return P
