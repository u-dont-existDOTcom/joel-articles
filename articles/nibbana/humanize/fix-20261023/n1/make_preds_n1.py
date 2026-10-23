"""Nibbāna batch n1's predictions, written before its API round (2026-10-23): one ledger line per text of TEXTS.json.

Each text is a fixed paragraph (with the question before it for the last test, and both paragraphs for the driving
caution) as the check reads it. "chance" is my chance of a 100% Human result. The windows were High or Medium in the check
of 2026-10-20 (https://www.pangram.com/feed/1ffe8aed-a00a-4273-846c-635ae22b2917).

  python3 articles/nibbana/humanize/fix-20261023/n1/make_preds_n1.py NAME ...   (from the repo root)
"""
import json, pathlib, subprocess, sys

N = pathlib.Path(__file__).resolve().parent
H = N.parents[1]
REPO = H.parents[2]
LEDGER = H / 'pangram-ledger.jsonl'
DET = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
# name: (lineage, scope, call, chance, tells, human tells)
P = {
    'n1_unification': ('NB-P64', 'paragraph', 'Human', 0.55, ['a definition remains ("When I say X, I mean ...") with a list of four'],
                       ['"whatever pulls everything together", "answer a text", "there\'s no separate knower in there", and his '
                        '"(well, if they\'re happy)" after it']),
    'n1_nde': ('NB-P92', 'paragraph', 'Human', 0.5, ['a "can\'t ..., but ..." contrast', 'the three sources still in one list'],
               ['"If you want to dig in, there\'s this", "wasn\'t stuck at the body\'s vantage point anymore", "floating around '
                'noticing specific details"']),
    'n1_percentages': ('NB-P134', 'paragraph', 'Human', 0.5, ['the two percentages still in parallel ("at around 1% ..., and by '
                                                                'roughly 5% ...")'],
                       ['"just playful shorthand", "the range I give", "can still do everything fine", "can barely function"; '
                        'the sentences before it read Human']),
    'n1_burden': ('NB-P165', 'paragraph', 'AI', 0.4, ['still two colons ("keeps two things apart: ...", "agrees that binding is '
                                                       'heavy, literally: ...")', 'his two short lines at the end, one of them '
                                                       'red in place ("Matter weighs what its binding weighs.")'],
                  ['"heavy all by itself", "(even an arahant still feels the first dart)", "craving is why we keep carrying it", '
                   '"actually agrees"']),
    'n1_last_test': ('NB-P227', 'pair', 'Human', 0.55, ['the question before it read AI, Low, in place, and is unchanged'],
                     ['"I\'m asking that last one because", "won\'t turn somebody into a therapist, let alone a saint", "like '
                      'other folks"']),
    'n1_rebirth': ('NB-P228', 'paragraph', 'Human', 0.5, ['the doctrine\'s chain stays ("craving and clinging condition '
                                                           'becoming, and becoming becomes birth")'],
                   ['"with no traveler riding along", his "More like a driverless car.", "But who\'s going around getting '
                    'reborn ...", "There is actually quite a lot of ..."']),
    'n1_diamond': ('NB-P230', 'paragraph', 'Human', 0.55, ['two sources in one sentence'],
                   ['"Turns out", "do have images that are pretty close, though", his "I used to attribute ..." before it']),
    'n1_science': ('NB-P237', 'paragraph', 'AI', 0.45, ['four findings still in one colon list'],
                   ['"only gets to circle", "some wild stuff out there", his "The full nerdy tour" and "third wheel, making it '
                    'safer to ride" after it']),
    'n1_driving': ('NB-P266', 'pair', 'Human', 0.55, ['a run of possibilities ("or ..., or ..., or ...")'],
                   ['"Maybe he was just lucky", "or God only knows", "I wouldn\'t keep driving through that myself", "I\'d stay '
                    'away from", his "That\'s my own CYA showing. 😇"']),
    # try 2: the five that read AI on their own in try 1, each with its frame changed
    'n1_nde_t2': ('NB-P92', 'paragraph', 'Human', 0.5, ['the sources still listed at the end'],
                  ['"The closest thing I can compare it to", "(controversially)", "can\'t back mine up", "They just help me '
                   'show", "If you want to go down that rabbit hole"']),
    'n1_percentages_t2': ('NB-P134', 'paragraph', 'AI', 0.45, ['two short parallel sentences ("Around 1% ... Around 5% ...")'],
                          ['"a playful way of saying", "can still do everything fine", "can hardly do anything", the '
                           'bracketed afterthought']),
    'n1_burden_t2': ('NB-P165', 'paragraph', 'AI', 0.4, ['a colon before the physics', 'his two short lines at the end'],
                     ['"puts the weight in one place and the carrying in another", "lugging it around", "and I mean '
                      'literally"']),
    'n1_diamond_t2': ('NB-P230', 'paragraph', 'Human', 0.5, ['the two sources in one sentence'],
                      ['"were already reaching for the same kind of pictures, though", "form is like foam", "look at the '
                       'world like a bubble, or a mirage"']),
    'n1_driving_t2': ('NB-P266', 'pair', 'Human', 0.5, ['a run of possibilities, now inside one "Whether ..., God only knows"'],
                      ['"he got it wrong about what was happening", "God only knows" as the main clause, "I wouldn\'t keep '
                       'driving through that myself", his "That\'s my own CYA showing. 😇"']),
    # round 3: science's try 2 (the reader's fix of try 1's frame) and try 3 of the four that read AI, High, twice
    'n1_science_t2': ('NB-P237', 'paragraph', 'Human', 0.5, ['the four findings still in one colon list',
                                                              '"here\'s some of what it finds" is a signpost'],
                      ['"out there", "who can seem like two knowers sharing a skull", his "The full nerdy tour" and "third '
                       'wheel, making it safer to ride" after it']),
    'n1_nde_t3': ('NB-P92', 'paragraph', 'AI', 0.35, ['his first sentence, inside the High window both times',
                                                       '"don\'t prove anything about mine" is still a disclaimer'],
                  ['the sources as a bracketed aside after the claim they back', '"Nobody could check anything like that"',
                   '"They might still help explain"']),
    'n1_burden_t3': ('NB-P165', 'paragraph', 'AI', 0.3, ['the doctrine still stated as a pair ("the five aggregates are the '
                                                          'burden and craving is what picks it up")',
                                                          'his two short lines at the end, AI alone both times'],
                     ['his own "splits the accounting cleanly" back, now after the doctrine it sums up', 'the physics as a '
                      'bracketed aside', '"The tangle\'s heavy", "craving\'s what keeps us carrying it"']),
    'n1_diamond_t3': ('NB-P230', 'paragraph', 'AI', 0.4, ['the two sources still compared in one sentence, now in brackets'],
                      ['his correction told as a story ("until I found out")', '"do have closely related images"']),
    'n1_driving_t3': ('NB-P266', 'pair', 'Human', 0.5, ['his own "My buddy E. told me ..." and "That\'s my own CYA showing. 😇" '
                                                         'read AI, Low, alone both times'],
                      ['the possibilities as his kind of bracketed list ending in "etc" (the guide\'s s1b read Human that way '
                       'on its first try)', '"God only knows why"', 'the caution that read Human in both tries']),
}
DIAG = {
    'n1_nde_t2': ('Try 1 read AI, High, as one window over the whole paragraph, his first two sentences included: the frame '
                  'is still a careful hedge ("can\'t vouch for ..., but ...") and a source list. Try 2 says it as he would '
                  'tell it: what it is closest to, what his event lacked, that those cases can\'t back his up, what they '
                  'help show, and where to read more. Better: Human, or the red shrinks to the source list.'),
    'n1_percentages_t2': ('Try 1 read AI, High, on the percentage sentence (a long sentence with a colon and two halves) and '
                          'AI, Low, on the sentence before it. Try 2 breaks it into short plain sentences and puts the range '
                          'caveat in brackets as an afterthought. Better: Human, or Low.'),
    'n1_burden_t2': ('Try 1 read AI throughout, his two short lines too. The frames left were the colon split and "Physics '
                     'actually agrees ...:". Try 2 opens with an image of the split ("puts the weight in one place and the '
                     'carrying in another") and gives the physics as his aside ("and I mean literally"). Better: Human, or the '
                     'red shrinks to his two lines, which are his to change.'),
    'n1_diamond_t2': ('Try 1 read AI, High, as one window over the paragraph. Its frame stayed: a correction, then the sources '
                      'as two parallel "X compares A to B" clauses. Try 2 gives the images as images ("form is like foam") and '
                      'the Pāli texts a stance ("were already reaching for the same kind of pictures"). Better: Human.'),
    'n1_driving_t2': ('Try 1 read AI, High, on "Maybe he was just lucky, or ..., or ..., or ..., or God only knows": still a '
                      'run of possibilities. Try 2 makes "God only knows" the main clause, with the possibilities inside one '
                      '"Whether ...". Better: Human, or Low.'),
    'n1_science_t2': ('Try 1 read Human, but the reader found two additions a reader would take as claims ("only gets to", '
                      '"some wild stuff"; REVIEW.md, item 4). Try 2 is the reader\'s fix of that frame, the findings as in '
                      'try 1. Better: Human, which would put it in the working copy.'),
    'n1_nde_t3': ('Tries 1 and 2 read AI, High, over nearly the whole paragraph, his first sentence included, and a pair '
                  'through the API reproduces a High window (E226), so the shape is the problem, not the alone check. Both '
                  'kept the order: comparison, the difference, the "not proof, but" frame, then the reading list. Try 3 puts '
                  'the sources in brackets right after the claim they back, gives the difference and the disclaimer as one '
                  'consequence, and ends on what the comparison helps explain. Better: Human, or the red shrinks to his '
                  'first two sentences.'),
    'n1_burden_t3': ('Tries 1 and 2 read AI throughout, High on the doctrine and the physics, Medium and Low on his two '
                     'short lines. Both kept his order (the Buddha splits it, then the halves, then the physics as "Physics '
                     'agrees ...:"). Try 3 states the doctrine first and his "splits the accounting cleanly" after it, as '
                     'the point it sums up, and gives the physics as a bracketed aside. Better: Human, or the red shrinks to '
                     'his two short lines.'),
    'n1_diamond_t3': ('Tries 1 and 2 read AI, High, on the stanza\'s source and the two Pāli images, and try 2 on his first '
                      'sentence too (Medium). Both kept a correction followed by the sources as a sentence of their own. Try 3 '
                      'tells the correction as a story ("until I found out ...") and gives the sources as a bracketed aside. '
                      'Better: Human.'),
    'n1_driving_t3': ('Tries 1 and 2 read AI, High, on the possibilities however they were joined (a run of "or"s, then '
                      'one "Whether ..."). Try 3 gives them the way Joel lists things in his own passing text, a bracketed '
                      'list ending in "etc" after "God only knows why", which is how the guide\'s De-hypnosis questions read '
                      'Human (s1b). The caution is try 1\'s, which read Human twice. Better: Human, or Low.'),
}


def main():
    for name in sys.argv[1:] or [k for k in P if not k.endswith('_t2')]:
        lin, scope, call, chance, tells, human = P[name]
        argv = [sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                '--lineage', lin, '--scope', scope, '--text', str(N / 'texts' / (name + '.txt')), '--call', call,
                '--chance', str(chance), '--key', name, '--batch', 'n1', '--detector', DET,
                '--decides', 'whether the fix reads Human on its own, before it goes to the reviews and the working copy']
        if name in DIAG:
            argv += ['--diagnosis', DIAG[name]]
        for t in tells:
            argv += ['--tells', t]
        for t in human:
            argv += ['--human-tells', t]
        r = subprocess.run(argv, capture_output=True, text=True, cwd=REPO)
        print(name, (r.stdout + r.stderr).strip()[-200:])
        if r.returncode:
            sys.exit(1)


if __name__ == '__main__':
    main()
