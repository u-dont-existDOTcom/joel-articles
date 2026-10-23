"""Batch 472g's predictions, written before its first API round (2026-10-23): one ledger line per text of TEXTS.json.

Each pair is a stretch of recheck A that read AI, as it stands (base) and with a candidate (a, b). "chance" is my chance
of a 100% Human result. The base texts say whether the API, on two paragraphs, sees what the whole-guide check saw; if a
base reads Human, a candidate's Human reading there says little, and the next recheck decides.

  python3 articles/inner-signal/humanize/fix-20261023/b472/make_preds_b472.py NAME ...   (from the repo root)

The ledger takes one open check per lineage, so each round predicts only the texts it sends: the three bases first, then
a candidate per stretch once its lineage's last check has its result.
"""
import json, pathlib, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
REPO = H.parents[2]
DET = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
IN_PLACE = 'recheck A, https://www.pangram.com/feed/47610d4b-fb69-4966-896f-317b029fc1af'
P = {
    'b472_s1_base': ('AI', 0.3, ['a run of ten "By X?" questions, which read AI in place (Low, one Medium; %s, part 7) and a '
                                 'run of questions read AI in the Inner Child lane (E217)' % IN_PLACE],
                     ['"It\'s all around you.", the run-on "Sometimes it\'s benign - like lullabies or prayers or being '
                      'taught by a good teacher ...", the next paragraph\'s rough list ("not be included", "confused")'],
                     'whether the API, on this pair, sees the questions as the recheck did'),
    'b472_s1a': ('Human', 0.6, ['a list of ten in one sentence after "It could be"'],
                 ['"or just hearing the same thing over and over" for repetition; the rest as it read Human in place'],
                 'whether one sentence with the ten items reads Human where the questions read AI'),
    # round 2, after round 1's bases (s1 and s3 read Human on their pairs, s2 AI throughout): s1b and s3b are checked
    # for not being worse than the base on the pair; s2b for whether rewording the return's first paragraph is enough
    'b472_s1b': ('Human', 0.85, ['a list of ten'],
                 ['the list in brackets after the noun it lists, ending "etc.", the construction of Joel\'s Appendix C '
                  'opening ("(person, ad, ideology, ..., etc.)"), which read Human, high, in his check'],
                 'whether his bracketed list reads Human in this paragraph'),
    'b472_s2_base': ('AI', 0.15, ['"make sure" four times in the return\'s first paragraph',
                                  'four parallel "If you\'ve ..." conditions',
                                  'its first sentence ends on "when you come out of it" right after the induction\'s last '
                                  'sentence does',
                                  'read AI in place, High (%s, part 9), and the same first sentence after the earlier '
                                  'induction version (2026-10-21)' % IN_PLACE],
                     ['"(of your choice, of course)", "Etcetera.", the induction paragraph\'s long run-on instructions '
                      '(Human, High, in the first screening post)'],
                     'whether the API, on this pair, sees the seam as the recheck did'),
    'b472_s2a': ('AI', 0.35, ['the "If you\'ve ..." chain and three of the "make sure"s stay, and two of their windows read '
                              'Medium and High in place'],
                 ['a first sentence that doesn\'t echo the sentence before it ("As you come back, undo anything you did to '
                  'change your state on the way in.")'],
                 'whether the window belongs to the first sentence alone (E198)'),
    'b472_s2b': ('AI', 0.4, ['four parallel "If you ..." conditions remain',
                             'the induction\'s last paragraph, unchanged, opens the pair and was in its first AI window (High) '
                             'with the return\'s first two sentences, so it may read AI on its own here'],
                 ['no "make sure"; the conditions differ in length and verb ("come back down and regain", "grow back", '
                  '"come back to feeling all of you here and now, in a body that\'s yours"); "(of your choice, of course)", '
                  '"Etcetera.", "the things you actually want to bring"'],
                 'whether the return\'s first paragraph, reworded throughout, lets the seam read Human'),
    'b472_s3_base': ('AI', 0.4, ['four short commands in a row ("Get up only when you feel steady. Make sure you\'re truly '
                                 'oriented and alert. Don\'t just assume it ...")',
                                 'read AI in place, Low, in the same words twice (%s, part 9; 2026-10-21)' % IN_PLACE],
                     ['"(or date)", "Look at something near, and something far.", the count before it with its "1..." steps'],
                     'whether the API, on this pair, sees the commands as the recheck did'),
    'b472_s3a': ('Human', 0.6, ['a reason clause closing the sentence ("because doing the count doesn\'t always bring you all '
                                'the way back")'],
                 ['the commands joined into two sentences, in plain words'],
                 'whether joining the commands with a plain reason reads Human'),
    'b472_s3b': ('Human', 0.85, ['an explanation in brackets'],
                 ['a gloss in brackets in plain words ("the count is supposed to bring you back, but it doesn\'t always do '
                  'the whole job"), "don\'t get up until"'],
                 'whether a gloss in brackets reads Human'),
    # round 3, the seam: the induction's last paragraph reworded, with P1 as installed (c) and with b's P1 (d)
    'b472_s2c': ('AI', 0.25, ['the return\'s paragraph as installed, whose later sentences read AI in windows of their own in '
                              'the base ("If you\'ve regressed or met parts ..." and "Make sure that the only things ...", '
                              'High)'],
                 ['the induction\'s paragraph names the cue ("the shortcut"), says what to do in fewer words ("take it out of '
                  'your recordings and out of any apps you\'ve set up with it"), and ends without the return\'s '
                  '"when you come out of it"'],
                 'whether the induction\'s last paragraph drives the seam\'s window'),
    'b472_s2d': ('Human', 0.5, ['the return\'s four "If you ..." conditions remain'],
                 ['both paragraphs reworded: the cue named, no "make sure", no echo between their last and first sentences, '
                  '"(of your choice, of course)", "Etcetera."'],
                 'whether the seam reads Human with both paragraphs reworded'),
    # round 4, the seam in his register (E194, E223): both paragraphs as e has them, and e's induction paragraph alone
    'b472_s2e': ('Human', 0.5, ['still two runs of instructions: the steps to retire the cue, then four "If you ..." '
                                'reversals'],
                 ['his casual words ("quit practicing", "kicking in", "spacey", "that\'s fine"), what to expect said as a '
                  'warning ("Don\'t be surprised if it still works on you for a while, though."), images for the reversals '
                  '("like a balloon", "little again for a while", "with your adult self in the driver\'s seat"), '
                  '"(whatever weight you choose, of course)", "Etcetera."'],
                 'whether the seam reads Human with both paragraphs in his register'),
    'b472_s2e_alone': ('Human', 0.55, ['a run of steps in its first sentence'],
                       ['as in b472_s2e: "quit practicing", "Don\'t be surprised if it still works on you for a while, '
                        'though.", "kicking in", "spacey", "that\'s fine"'],
                       'whether the induction\'s last paragraph in his register reads Human on its own (E190)'),
    # round 5: the tidy closers out of both paragraphs
    'b472_s2f': ('Human', 0.5, ['two runs of instructions remain', 'the "If you ..." reversals'],
                 ['no closer at either end: the induction paragraph ends on a specific referral ("like a therapist who knows '
                  'hypnosis"), the return\'s on "Etcetera."; "Don\'t be surprised if it still works on you for a while, '
                  'though"; the images of e'],
                 'whether taking out the closers lets the seam read Human'),
    'b472_s2f_alone': ('Human', 0.5, ['a run of steps in its first sentence'],
                       ['ends on the specific referral, no closer; "Don\'t be surprised if it still works on you for a while, '
                        'though, since saying it\'s gone doesn\'t erase it overnight."'],
                       'whether the induction paragraph without its closer reads Human alone'),
    # round 6: the wordings that go in, each b with the linter rule it brought taken out
    'b472_s1c': ('Human', 0.85, ['a list of ten in brackets'],
                 ['as b (Human on this pair), with "It\'s all around you." joined on: "..., repetition, etc.), and it\'s all '
                  'around you."'],
                 'whether the wording that goes in reads as b did'),
    'b472_s3c': ('Human', 0.85, ['an explanation in brackets'],
                 ['as b (Human on this pair), with the installed "truly" for "actually"'],
                 'whether the wording that goes in reads as b did'),
}

# a retry after an AI result needs its diagnosis: what changed, why it should help, what counts as better
DIAG = {
    'b472_s2b': ('Round 1\'s base read AI throughout on the pair, its first window (High) holding the induction\'s last '
                 'paragraph and the return\'s first two sentences. The return\'s first paragraph says "make sure" four '
                 'times, its first sentence echoes the end of the sentence before it ("when you come out of it"), and its '
                 'conditions are four parallel "If you\'ve ..." sentences. s2b rewords that whole paragraph: a first sentence '
                 'with no echo, no "make sure", conditions of different lengths and verbs, the aside and "Etcetera." kept. '
                 'Better: the return\'s paragraph reads Human; if the induction\'s paragraph still reads AI in its own '
                 'window, the seam\'s window belongs to it, and it is the next try.'),
    'b472_s2d': ('b (the return\'s paragraph reworded) still read AI, High, as one 241-word window starting on the '
                 'induction\'s last paragraph, unchanged in a and b; so d rewords that paragraph too: the cue named "the '
                 'shortcut", its steps in fewer words, its last sentence no longer ending as the return\'s first one does. '
                 'c (the same paragraph with the return\'s as installed) is checked beside it, in its own lineage. Better: '
                 'd reads Human; if c does too, the return\'s paragraph can stay as installed.'),
    'b472_s2e': ('d (both paragraphs reworded) still read AI, High, as one window, like b and c: every version so far kept '
                 'the instruction lists as lists in the installed text\'s register. e changes what the sentences do, in '
                 'Joel\'s register (E194, E223): the decision is the reader\'s ("Decide that while you\'re wide awake"), '
                 'what to expect is a warning ("Don\'t be surprised if it still works on you for a while"), his casual '
                 'words, and an image for each reversal. Better: the pair reads Human, or its window shrinks to one of the '
                 'two paragraphs (then the other is the next try, part by part, E190).'),
    'b472_s2e_alone': ('c (the induction\'s paragraph reworded, with the return\'s as installed) read AI, High, as one '
                       'window over both. Here the same paragraph is in Joel\'s register (as in b472_s2e) and checked '
                       'alone, to see which side of the seam reads AI on its own (E190). Better: Human alone; if it reads '
                       'AI alone, it is the stuck one.'),
    'b472_s2f': ('e read AI in the pair (and its induction paragraph alone), and the return paragraph\'s last sentence read '
                 'AI, High, in a window of its own: every version of both paragraphs ends on a tidy closer, a shape the '
                 'gate lists among what read red. f keeps e\'s register and takes the closers out (the induction paragraph '
                 'ends on its referral, made specific; today\'s trance ending is left to the return\'s script, which says '
                 'it; "keep only what you chose" moves into the return paragraph\'s first sentence, which then ends on '
                 '"Etcetera."). Better: Human, or the red shrinks to the instruction runs.'),
    'b472_s2f_alone': ('e\'s induction paragraph read AI, High, alone, ending on "Either way, today\'s trance ends when you '
                       'come back."; f\'s ends on its referral instead, made specific. Better: Human alone.'),
}


def main():
    cands = json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))
    led = H / 'pangram-ledger.jsonl'
    for name in sys.argv[1:]:
        call, chance, tells, human, decides = P[name]
        argv = [sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(led),
                '--lineage', cands[name]['lineage'], '--scope', 'paragraph' if cands[name].get('alone') else 'pair',
                '--text', str(B / 'texts' / (name + '.txt')),
                '--call', call, '--chance', str(chance), '--decides', decides, '--key', name, '--batch', '472g',
                '--detector', DET]
        if name in DIAG:
            argv += ['--diagnosis', DIAG[name]]
        for t in tells:
            argv += ['--tells', t]
        for t in human:
            argv += ['--human-tells', t]
        r = subprocess.run(argv, capture_output=True, text=True, cwd=REPO)
        print(name, r.returncode, (r.stdout + r.stderr).strip()[-300:])
        if r.returncode:
            sys.exit(1)


if __name__ == '__main__':
    main()
