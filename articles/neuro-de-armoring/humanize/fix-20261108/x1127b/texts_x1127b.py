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


# the paragraphs as the article had them at the start of this turn (1d94ed03), saved so the texts don't move once one of
# them goes in
import json as _json
OLD = _json.loads((HERE / 'OLD-X1127B.json').read_text(encoding='utf-8'))['old']

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


# P-SW21, the underpinnings paragraph (his card version of 2026-11-03, #263, https://www.pangram.com/history/59682079-eaf9-4049-b366-98ac3f421bcd:
# Human Low over the first sentence, AI Low over the second). A near miss, so two steps of at most 20% come before a
# rewrite. The reads of it (x1126b/v1/*/sw21): two words for one thing ("underpinnings" in S1, "foundation" in S2), and S2
# a chain of hung clauses (a stray comma in "dig under the house, and pour"), the means before the payoff, four pictures
# for one thing, and "to allow us to dig" hanging off the ketones. Step 1, what a reader could take two ways: the same
# word for the same thing, and the stray comma.
SW21_263 = OLD['sw21']
STEP['sw21-s1'] = (SW21_263.replace('is about fixing the underpinnings, not redecorating.', 'is about fixing the foundation, '
                                    'not redecorating.')
                   .replace('dig under the house, and pour a new foundation', 'dig under the house and pour a new '
                            'foundation'))
assert STEP['sw21-s1'] != SW21_263

# Step 1 (#323, https://www.pangram.com/history/0dcc395b-86a9-4a0c-8d04-8d56a7ebcd83) read AI Generated, 100%: AI Low
# over the first sentence (Human Low in his version) and AI High over the second (AI Low): "the foundation" for his
# "underpinnings" made both read worse, so his word stays. Step 2, from his version again, the second sentence's tail:
# "to allow us to dig" hangs off the ketones (the needed read), the stray comma, and "so we can" said for the dig and
# again for the update; said as "so we can dig ... and pour ..., and eventually update ...".
STEP['sw21-s2'] = SW21_263.replace('to allow us to dig under the house, and pour a new foundation, so we can eventually '
                                   'update the psychological software upstairs.',
                                   'so we can dig under the house and pour a new foundation, and eventually update the '
                                   'psychological software upstairs.')
assert STEP['sw21-s2'] != SW21_263

# The tell panel on step 2 (panel-sw21-s2: Fable, Sonnet, Haiku) agreed on both sentences: "serves as" for "is" (all
# three), and the house picture turning into software at the end (all three); within the near-miss limit, "works like"
# for "serves as", and the house held to the end ("the psychology upstairs").
DRAFT['sw21-s2'] = STEP['sw21-s2']
STEP['sw21-s2'] = (STEP['sw21-s2'].replace('It\'s a protocol that serves as a metabolic solvent', 'It\'s a protocol that works '
                                           'like a metabolic solvent')
                   .replace('and eventually update the psychological software upstairs.', 'and eventually work on the '
                            'psychology upstairs.'))
assert STEP['sw21-s2'] != DRAFT['sw21-s2']

# Step 2 (#324, https://www.pangram.com/history/fce546f2-99e5-47a3-b38f-a2ec75d14e15) read as his version did: Human Low
# over the first sentence, AI Low over the second. The two small steps from his version are checked, so the second
# sentence is rewritten from the reads (x1126b/v1/*/sw21): one house picture held from start to finish (what has set hard,
# what the protocol does to it, what goes in its place, the work upstairs after), each mechanism with a few plain words
# on what it does, the softening said as the protocol's act, and "concrete" as what trauma set hard, not the foundation.
# His first sentence stays (the only Human window).
STEP['sw21-r1'] = ("Neurological De-Armoring is about fixing the underpinnings, not redecorating. Trauma leaves the "
                   "brainstem set hard, like concrete, and the protocol softens it the way a solvent would, by calming "
                   "glutamate (the brain's main \"go\" signal) and with ketones (BHB), which block HDACs, the enzymes that "
                   "can keep new learning from sticking. Then we can dig under the house and pour a new foundation, and "
                   "only after that work on the psychology upstairs.")

# The fresh read of that rewrite (v1/his-fixes/sw21r1, Fable) marked all three sentences: "X, not Y" answering no worry,
# and "underpinnings" of nothing named; one sentence packing the picture and every mechanism, two glosses built alike,
# "which block HDACs" pointing two ways, what new learning has to do with the concrete unsaid; "the house" with nothing
# saying the brainstem is its foundation, and digging under a softened foundation to pour a new one. Each is changed: the
# picture named first (Perry's house, section's paragraph two), the old concrete dug out before the new is poured.
DRAFT['sw21-r1'] = STEP['sw21-r1']
STEP['sw21-r1'] = ("In Perry's picture, the brainstem is the foundation of the house, and Neurological De-Armoring works on "
                   "it before any redecorating upstairs. Trauma leaves that foundation set hard, like concrete, so the "
                   "protocol softens it the way a solvent would, by calming glutamate (the brain's main \"go\" signal) and "
                   "adding the ketone BHB, which blocks enzymes called HDACs that can keep new learning from sticking. "
                   "Then we can dig out the old concrete and pour a new foundation, and only after that work on the "
                   "psychology upstairs.")

# The ledger takes step 2 (#324) as the best near miss, so two more steps of at most 20% from it come before the rewrite
# above. Step 3, what a reader could take two ways (the read: "which of the three does what"): HDAC inhibition is said
# where the ketones are, since BHB is what blocks the HDACs (section C).
SW21_324 = STEP['sw21-s2']
STEP['sw21-s3'] = (SW21_324.replace('works like a metabolic solvent, via HDAC inhibition, that softens', 'works like a '
                                    'metabolic solvent that softens')
                   .replace('supplementing Ketones (BHB) so we can', 'supplementing Ketones (BHB, which block HDACs) so '
                            'we can'))
assert STEP['sw21-s3'] != SW21_324


# PAIR-SW17-18, the "Underpinning" Principle with the Gibson paragraph after it (#260,
# https://www.pangram.com/history/fbca5c0c-2de5-44ae-8172-d041973cb42c: Human Medium over the label and Perry's first
# sentence, High, Medium over "You cannot hang curtains in a collapsing house. Why does the brain build this armor?", High,
# Medium over "As Dr.", High). A near miss, so small steps first. Step 1, the splits: "Dr." off Perry in both places (the
# window Pangram splits at the title, as his 71 took it off Epley and lesson neuro-2026-11-27e off Perry in the
# Anti-Breakthrough), and the label marked off with a colon, as the Anti-Breakthrough's is (the fit read took "The
# "Underpinning" Principle Dr. Bruce Perry" as a title for Perry).
STEP['sw17-s1'] = OLD['sw17'].replace('The "Underpinning" Principle Dr. Bruce Perry compares', 'The "Underpinning" '
                                      'Principle: Bruce Perry compares')
STEP['sw18-s1'] = OLD['sw18'].replace('As Dr. Bruce Perry explains', 'As Bruce Perry explains')
assert STEP['sw17-s1'] != OLD['sw17'] and STEP['sw18-s1'] != OLD['sw18']

# Step 1 (#326, https://www.pangram.com/history/45b4feb9-8030-40e0-bfd6-547069ed7b55) read Human Written: High over the
# label and the first two sentences, Medium over "You cannot hang curtains in a collapsing house." with the Gibson
# paragraph's question, High over the rest: the splits at "Dr." closed. Step 2, the curtains line: a short line standing
# alone that says the sentence before again (the read against his fixes, ways 6, 18, 16): joined to the sentence it draws
# on (lesson neuro-2026-11-26o), its "cannot" said the way he talks.
STEP['sw17-s2'] = STEP['sw17-s1'].replace('while the foundation (the Brainstem) is crumbling. You cannot hang curtains in a '
                                          'collapsing house.', 'while the foundation (the Brainstem) is crumbling, and you '
                                          'can\'t hang curtains in a collapsing house.')
assert STEP['sw17-s2'] != STEP['sw17-s1']

# Step 2 (#327, https://www.pangram.com/history/7316e9b0-455f-4fb4-9bdc-0ec0b33fad13) read the whole Principle High (45
# words) and the Gibson paragraph High but for its opening question, "Why does the brain build this armor?", Human
# Medium (7 words); that question opens the part under its own heading ("The Modern "Role-Self" vs. The Ancient
# "True-Self""), which the pair check leaves out, and the Gibson paragraph reads High by itself (#261). The Principle sits
# in the same part as the paragraph before it, his own version of 2026-11-06 (High by itself, #259), so it is checked
# with that neighbour: lineage PAIR-SW16-17.
