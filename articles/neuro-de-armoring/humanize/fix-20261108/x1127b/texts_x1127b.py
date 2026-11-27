"""The humanizing pass in "Psychology is the Software; Biology is the Hardware.", the turn of his message of 2026-11-27
20:08 UTC ("ok why did you stop?"). What is left there (LEFT.md): the "Underpinning" Principle (PAIR-SW17-18, Human with
three Medium windows, #260), the one-sixteenth paragraph (P-SW19, my try 2 #266: Human Medium, AI High, AI Medium), the
underpinnings paragraph (P-SW21, his card version #263: Human Low, AI Low) and the practice paragraph (PAIR-SW22-23, AI,
#268; the Anti-Breakthrough before it went in at Human High last turn).

OLD: the paragraphs as the article has them now (HUMANIZED-SO-FAR.md 1d94ed03). STEP: one change a check from a near miss
(the ledger's rule). NEW: a rewrite where the lineage's best try had no Human window.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE.parent / 'x1126b'))
import apply_gate  # noqa: E402
import texts_x1126b as TB  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
PERRY = TB.PERRY
plain = apply_gate.plain


def block(start):
    (b,) = [b for b in ARTICLE.read_text(encoding='utf-8').split('\n\n') if b.startswith(start)]
    return b


OLD = {
    'sw17': block('The "Underpinning" Principle'),
    'sw18': block('Why does the brain build this armor?'),
    'sw19': block('We are operating on about one-sixteenth'),
    'sw21': block('Neurological De-Armoring is about fixing'),
    'sw22': block('The Anti-Breakthrough (Micro-Dosing):'),
    'sw23': block('Your goal is Micro-Dosing Safety'),
}

# P-SW19: my try 2 (#266, https://www.pangram.com/history/cd2c9d6b-ada6-44c9-b29c-67292c104927) read Human Medium over its
# first sentence, AI High over the Void sentence and AI Medium over the last two: the near miss each step starts from.
SW19_266 = TB.NEW['sw19']
STEP = {}
# Step 1, the Void sentence alone: "the "Void" this guide keeps coming back to" is a sentence about the text itself (way 20
# of his_fixes_brief.md), and "is real: it's what that missing company feels like" a colon gloss defining a label (way
# 21). The plain words come first with the guide's name for them in brackets, as his glosses go ("anhedonia (no joy or
# desire)"), and the reason joins with "since".
STEP['sw19-s1'] = SW19_266.replace(
    'So the empty feeling you may carry, the "Void" this guide keeps coming back to, is real: it\'s what that missing '
    'company feels like.',
    'So the emptiness you may feel (the "Void") is real, since it\'s what that missing company feels like.')
# Step 2, lesson neuro-2026-11-27i: "your brain will eventually reach for the armor again" has a body part doing what the
# person does; his fix of the same kind gave the act to the person ("you project").
STEP['sw19-s2'] = STEP['sw19-s1'].replace('or your brain will eventually reach for the armor again',
                                          'or you\'ll eventually reach for the armor again')
assert all(STEP[k] != v for k, v in (('sw19-s1', SW19_266), ('sw19-s2', STEP['sw19-s1'])))
# The tell panel on step 1 (panel-sw19-s1: Fable, Sonnet, Haiku) agreed on every sentence; three readers on the Void
# sentence (a validate-then-explain move, the hedge "may feel") and on the last (an imperative with an appositive gloss,
# and a personified brain in a dramatic closing line), two on the before-and-after sentence standing alone. Within the
# near-miss limit (20% of try 2's words; joining the last two sentences would count as 36%), step 2 takes the hedge off,
# folds the gloss into "a tribe of people you're close to", and gives the armor to the person (lesson
# neuro-2026-11-27i). The join waits for a later step.
STEP['sw19-s2'] = (STEP['sw19-s1']
                   .replace('So the emptiness you may feel', 'So the emptiness you feel')
                   .replace('Gather a tribe around you, people you\'re close to', 'Gather a tribe of people you\'re close to')
                   .replace('or your brain will eventually reach for the armor again', 'or you\'ll eventually reach for the '
                            'armor again'))
assert 'may feel' not in STEP['sw19-s2'] and 'your brain will' not in STEP['sw19-s2'] and 'around you,' not in STEP['sw19-s2']

# PAIR-SW22-23: the practice paragraph. Its try (#268, x1126b) read AI in every window, so a rewrite is allowed. The reads
# of the post's version (x1126b/v1/*/sw23): "Micro-Dosing Safety" read as how to microdose the drugs; "regulated
# breathing" said no pattern; the marathon line said S1 again and can go; "Frequency beats intensity" ended on a slogan.
# #268's own tells: a goal-colon opening and an analogy with a where-clause. This one says what the reader does as the
# next step of the paragraph before ("So"), keeps the post's picture (physical therapy for a broken nervous system), and
# says frequency over intensity as the reason, in plain words.
NEW = {
    'sw23': ('So your goal is 30 seconds of slow, steady breathing, twenty times a day, like physical therapy for a broken '
             'nervous system, since doing it often helps more than doing it hard.'),
}
# The fresh read of that draft against his fixes (v1/his-fixes/sw23n, Fable) marked its one sentence: three ideas in it,
# the comparison wedged between the goal and its reason; "slow, steady" a comma pair; "doing it hard" could mean
# breathing hard or one long session; "a broken nervous system" with no owner, and "like physical therapy" could attach
# to the breathing or to the schedule. The needed read of the post's version (x1126b/v1/needed/sw23) had the physical
# therapy line as one the reader can lose. So the comparison goes, and the reason says the thing, joined to the schedule.
DRAFT = {'sw23-a': NEW['sw23']}
DRAFT['sw23-b'] = ('So your goal is 30 seconds of slow and steady breathing, twenty times a day, since short sessions done '
                   'often help an armored nervous system more than one long session does.')
# The tell panel on draft b with the Anti-Breakthrough before it (panel-pair2223) agreed on all four sentences; on the
# practice sentence, that it says the paragraph's point a fourth time with a second "since ... more than" clause and
# "an armored nervous system" again, after a second "So", and that "slow and steady" is a stock pair. The Anti-Breakthrough
# reads Human High by itself (P-SW22 #303), so it stays as it went in; the practice sentence keeps only what the reader
# does, the reason being the paragraph before's, and "slow breathing" for "regulated breathing".
NEW['sw23'] = 'In practice, that means 30 seconds of slow breathing, twenty times a day.'
PAIR_SW22_23 = OLD['sw22'] + '\n\n' + NEW['sw23']


def pair_plain(*mds):
    """The words as typed into Pangram, a paragraph break between paragraphs (plain() joins them)."""
    return '\n\n'.join(plain(m) for m in mds)


# Step 2 (#312, https://www.pangram.com/history/bee687c2-f818-435b-8f5f-ae3d4b9a4630) read AI Detected, 75%: Human Medium
# over the first sentence, AI Low over the Void sentence (AI High in try 2), AI Medium over the before-and-after sentence
# and AI High over the last. Step 3, the last two sentences, within the near-miss limit: the before-and-after sentence
# tied to what came before with "And"; the last said as his judgment ("I'd", his way for advice), with what happens
# without them said as the reason ("because without them") instead of a threat ("or you'll ..."), not a second "So
# ..., since" after the Void sentence's.
STEP['sw19-s3'] = (STEP['sw19-s2']
                   .replace('Once you\'ve de-armored, going back', 'And once you\'ve de-armored, going back')
                   .replace('Gather a tribe of people you\'re close to and see most days, or you\'ll eventually reach',
                            'I\'d gather a tribe of people you\'re close to and see most days, because without them '
                            'you\'ll eventually reach'))
assert STEP['sw19-s3'] != STEP['sw19-s2']

# PAIR-SW22-23 (#313, https://www.pangram.com/history/70b05e3c-4aaf-419d-91dd-e97b043c50ed) read Human Written: High over
# the Anti-Breakthrough's first two sentences, Medium over its last with the practice sentence. "which is what I mean by
# micro-dosing here" then "In practice, that means" says what something means twice in a row; the practice sentence says
# what a dose is instead, with the word the sentence before ends on.
NEW['sw23-s1'] = 'Each dose is 30 seconds of slow breathing, and you do twenty of them a day.'


# PAIR-SW22-23 step 1 (#315, https://www.pangram.com/history/17aa8876-097f-43dd-a2f2-654c38d0bb89) read AI Detected, 66%,
# even over the Anti-Breakthrough's first two sentences: "Each dose is ..., and you do twenty of them a day" made the
# pair read worse. Back to the near miss (#313). What its practice sentence leaves out, and the post had ("Micro-Dosing
# Safety"), is what the dose is of: a reader can take 30 seconds of slow breathing as the healing work itself. One clause
# says it (lesson neuro-2026-11-27k: the word that settles what a reader could get wrong).
NEW['sw23-s2'] = 'In practice, that means 30 seconds of slow breathing to feel safe in your body, twenty times a day.'

# P-SW19: two steps of at most 20% from try 2 are checked (#312, #314), each AI Detected, so the near-miss steps are spent
# and the paragraph is rewritten from its reads (x1126b/v1/*/sw19), the tell panel (panel-sw19-s1) and lessons
# neuro-2026-11-27h to k: the first sentence as it read (Human Medium in every try); the Void sentence as the reader's own
# feeling first, its name in brackets; the before-and-after sentence joined to the act it calls for ("It also means
# ..., so"), the need said as what follows rather than an order with a threat, and the person, not the brain, puts the
# armor back on; the post's "just to survive the cold" kept.
STEP['sw19-r1'] = ('That works out to about one-sixteenth of the grown-ups per child that our brains evolved with ([Perry, '
                   '2023](' + PERRY + ')). So if you often feel empty (the "Void"), that\'s real, and it\'s that missing '
                   'company you\'re feeling. It also means that once you\'ve de-armored, going back to a lonely life will '
                   'hurt more than it did with the armor on, so you\'ll need a tribe of people you\'re close to and see most '
                   'days, or you\'ll end up putting the armor back on just to survive the cold.')

# The fresh read of that rewrite against his fixes (v1/his-fixes/sw19r1, Fable) marked all three sentences: "That" with
# nothing saying what works out, and "per child that our brains evolved with" read two ways; "that's real" two ways and
# "company" a word nothing before used; "It also means" pointing at two things with the link to de-armoring unsaid
# (the armor was numbing the loneliness); three ideas in the last; "the cold" a new label. Each is changed.
DRAFT['sw19-r1'] = STEP['sw19-r1']
STEP['sw19-r1'] = ('So a child today gets about one-sixteenth of the grown-ups that a child had when our brains evolved '
                   '([Perry, 2023](' + PERRY + ')). If you often feel empty (the "Void"), that feeling is real, since '
                   'you\'re living with a fraction of the people we\'re built to have around us. That loneliness is what '
                   'the armor has been numbing, so once you\'ve de-armored, going back to a lonely life will hurt more than '
                   'it did with the armor on. So I\'d find a tribe of people you\'re close to and see most '
                   'days, or you\'ll end up putting the armor back on just to get through the loneliness.')

# PAIR-SW22-23 step 2 (#316, https://www.pangram.com/history/beae5fbb-2ab5-4cda-a264-cf5017db761c) read Mostly Human: High
# over the first two sentences, Low over the Anti-Breakthrough's last and Low over the practice sentence; the purpose
# clause split the near miss's Medium window into two Low ones. The last try goes back to the near miss (#313) and
# changes only "that means", which says what something means right after "which is what I mean by": the practice is
# said as his advice, "I'd do", the way his warnings give theirs ("I'd quit it as soon as you notice any of that").
NEW['sw23-s3'] = 'In practice, I\'d do 30 seconds of slow breathing, twenty times a day.'

# P-SW19: the ledger takes step 2 (#312) as the lineage's best near miss, so one more step of at most 20% from it comes
# before a rewrite. Step 4 changes only the closing figure the fresh read of my rewrite marked: "the cold" is a new
# label for the loneliness, said plainly.
SW19_312 = STEP['sw19-s2']
STEP['sw19-s4'] = SW19_312.replace('just to survive the cold.', 'just to get through the loneliness.')
assert STEP['sw19-s4'] != SW19_312

# Step 4 (#317, https://www.pangram.com/history/22a255ee-3d48-4afd-8b51-6d3ac3251feb) is the best yet: Human High over the
# first sentence, Human Low over the Void sentence, AI Low over the last two (AI Medium and AI High before). Step 5, the
# before-and-after sentence: the panel called it a flat prediction stated as settled fact, and lesson
# neuro-2026-11-27j says what will happen as often as it really happens ("you'll tend to").
STEP['sw19-s5'] = STEP['sw19-s4'].replace('going back to a lonely life will feel worse', 'going back to a lonely life will '
                                          'tend to feel worse')
assert STEP['sw19-s5'] != STEP['sw19-s4']

# Step 5 (#319, https://www.pangram.com/history/84d12e88-4359-49bd-a3e8-ed6306e429f3) read Human Written: High over the
# first two sentences, Medium over the before-and-after sentence, Low over the last: "you'll tend to" moved the whole
# paragraph, as it did in his Cognitive Warning. Step 6, the last sentence: the act tied to the sentence before with "So"
# (the first half of lesson neuro-2026-11-27j), one word.
STEP['sw19-s6'] = STEP['sw19-s5'].replace('Gather a tribe of people', 'So gather a tribe of people')
assert STEP['sw19-s6'] != STEP['sw19-s5']

# Step 6 (#320, https://www.pangram.com/history/de8a85ed-e939-4b92-808f-ee2e527176e6) read Human Written: High over the
# first three sentences, Medium over the last. Step 7, its image: "reach for the armor again" is the fancier figure; the
# plain one is putting the armor back on.
STEP['sw19-s7'] = STEP['sw19-s6'].replace('or you\'ll eventually reach for the armor again', 'or you\'ll eventually put the '
                                          'armor back on')
assert STEP['sw19-s7'] != STEP['sw19-s6']

# Step 7 (#321, https://www.pangram.com/history/9f18c4aa-12e3-4806-a13d-57c8ebe5b439) read the same windows, the last
# sentence still Medium. What a reader could get wrong there (the fit read of the post's version: "MISREAD: don't bother
# alone"): a reader who lives alone can take "gather a tribe ..." as something they must already have; "start" says it is
# where they begin (lesson neuro-2026-11-27k, one word).
STEP['sw19-s8'] = STEP['sw19-s7'].replace('So gather a tribe of people', 'So start gathering a tribe of people')
assert STEP['sw19-s8'] != STEP['sw19-s7']
