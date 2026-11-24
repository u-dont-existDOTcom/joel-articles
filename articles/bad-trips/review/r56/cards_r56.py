# The cards of round 56, read by build_r56.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 66: his round-55 versions in the guide, why magnesium chloride said in his
# amounts paragraph, and the softer-peak paragraph at Human High (humanize/h74-20261124/RESULTS.md).

BUILT = '2026-11-24'
H = 'https://www.pangram.com/history/'
R55 = BLOB + 'articles/bad-trips/review/r55/RESULTS-R55.md'
H74 = BLOB + 'articles/bad-trips/humanize/h74-20261124/RESULTS.md'
REPLAY = BLOB + 'articles/bad-trips/humanize/h74-20261124/replay/RESULTS.md'
LESSON = BLOB + 'docs/lessons/2026-11-24-1953-bad-trips.md'

INTRO = [
    'Round 56 (2026-11-24). Both of your versions are in as your checks had them. You were right about "meaningful": it '
    'was in the post, which a model drafted in parts, and I was wrong to call it a word of yours that the fidelity check '
    'held. It is now a cut you meant, and the lesson says whose a word is comes from your versions and answers, never from '
    'the check. Each point has its fate in [the record](%s).' % R55,
    'Why magnesium chloride is now in your amounts paragraph: "I use it mostly because it absorbs far better than magnesium '
    'oxide, so you can see how it\'s helping, usually within a minute." It read [Human High in one window](%saf5fd4f9-ee90-40f4-8bf5-cedf55c61914) '
    'on the sixth try, the last two fixes being your ways (the two reasons apart, and "And" tying the diarrhea line to yours). '
    'The softer-peak paragraph also reads [Human High](%s686d3bd1-6132-4f5c-b3d9-bec01f8f8455). Every check is in '
    '[the record](%s).' % (H, H, H74),
    'Your fixes are in the repo for every lane ([the lessons](%s)), and a fresh writer that never saw your versions took '
    'your second wife\'s paragraph to Human High from them alone ([the blind test](%s)).' % (LESSON, REPLAY),
]

card(id='CHLORIDE-CLAIM', type='question', advice='ask',
     title='1. Your amounts paragraph: why magnesium chloride',
     whose='his own: his TEACH-JAW comment of round 55 ("it absorbs faster and better than any other form, so you can see how it\'s helping usually within a minute")',
     question=('You wrote that magnesium chloride "absorbs faster and better than any other form". The study the sentence '
               'links ([Firoz and Graber 2001](https://pubmed.ncbi.nlm.nih.gov/11794633/)) found magnesium oxide poorly '
               'absorbed (4%%), and chloride, lactate and aspartate absorbed about equally well, and I found no study '
               'comparing how fast the forms act. So the guide says: "I use it mostly because it absorbs far better than '
               'magnesium oxide, so you can see how it\'s helping, usually within a minute", with the minute as what you '
               'see.\n'
               'a) Keep it as it is.\n'
               'b) Say "any other form" anyway, as your experience, in your words in the box.\n'
               'c) Something else: say it in the box.'),
     why='it is your claim, and the source only backs part of it',
     stays='the sentence as it is',
     advice_note='a: it says what the study shows, and your minute stays yours',
     spans=[whole(P('B115'))])

card(id='WIFE-LAST', type='question', advice='ask',
     title='2. Your second wife\'s paragraph: its last phrase',
     whose='his own: his TEACH-WIFE version of round 55, its last sentence',
     question=('Your version is in as you wrote it. Two things about its last phrase, "since potassium gets depleted after '
               'magnesium":\n'
               'A fresh reader took "after magnesium" as the magnesium causing the potassium loss, which could scare someone '
               'off the very thing you tell them to give. What you meant holds: low magnesium makes the kidneys lose '
               'potassium ([Huang and Kuo 2007](https://pubmed.ncbi.nlm.nih.gov/17804670/)).\n'
               'And in the API your paragraph reads [High in one window](%s9a72854c-b5a3-4515-a622-b4a2ae99b9b6) only with '
               'the double space you pasted after "At the hospital,"; with one space, the way a published page shows it, its '
               'last sentence reads [Medium](%s590654bf-e074-4d55-aa0f-3d3ea076bd37). With "since potassium gets depleted '
               'once magnesium runs low", it reads [Human High in one window](%se74a7e6b-7047-4e54-af54-64070d2b5879) with one '
               'space.\n'
               'a) "since potassium gets depleted once magnesium runs low".\n'
               'b) Keep yours.\n'
               'c) Your own words in the box.' % (H, H, H)),
     why='it is your sentence, and the change is one phrase of it',
     stays='your version as it is',
     advice_note='a: it says what you meant, and it reads High as the page will show it',
     spans=[whole(P('B118'))])
