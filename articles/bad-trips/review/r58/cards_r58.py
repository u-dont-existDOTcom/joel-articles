# The cards of round 58, read by build_r58.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 68: his round-57 kidney paragraph in the guide, the serotonin opening at Human
# High, and the charcoal and poison control paragraphs at Human High with three things from the review they cite
# (humanize/h76-20261125/RESULTS.md). No string here is %-formatted.

BUILT = '2026-11-25'
H = 'https://www.pangram.com/history/'
R57 = BLOB + 'articles/bad-trips/review/r57/RESULTS-R57.md'
CHECKS = BLOB + 'articles/bad-trips/review/r57/HIS-CHECKS-R57.md'
H76 = BLOB + 'articles/bad-trips/humanize/h76-20261125/RESULTS.md'
LESSONS = BLOB + 'docs/lessons/2026-11-25-0124-bad-trips.md'
LEFT = BLOB + 'articles/bad-trips/humanize/h76-20261125/LEFT.md'
REVIEW = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6620762/'
NEW1 = ('If they swallowed it within the last hour or so (slow-release pills leave a few hours more), activated charcoal may '
        'help, since it binds to a lot of drugs in the gut before the body can absorb them. It only helps with what binds to '
        'it, which leaves out alcohol and lithium among other things, and it can also adsorb medication they need. I\'d only '
        'give it to somebody who\'s fully alert and able to swallow, because anybody who is vomiting, sedated, seizing or '
        'otherwise unable to protect their airway could breathe it into their lungs (aspiration).')
NEW2 = ('If you\'re unsure charcoal would be of any value to them, poison control may be useful. They\'re also who to ask when '
        'you can\'t tell what the substance is or what it does in combination with something else they took, or when there '
        'may be a delayed risk (the worst coming hours later). I don\'t treat calling poison control as a mandatory ritual, '
        'though, since how useful they are varies by country and by whoever answers. And what they give you is help deciding, '
        'so go on with any first aid while you talk to them.')

INTRO = [
    'Round 58 (2026-11-25). Your kidney paragraph is in, whole, as your last check had it '
    '([Human High in one window](' + H + '33a4d738-d566-44b0-9fd3-5e6194848e20); the API reads it the same). The page\'s box '
    'came back unchanged, so I read the text from that check. Your bold lead is on the words it sat on, and the kidney '
    'study\'s link, which your plain text couldn\'t carry, is on "injure the kidneys". Your six checks and what each one '
    'changed are [here](' + CHECKS + '), and what they taught me is [here](' + LESSONS + ').',
    'What you did with "other dangerous electrolyte shifts" (moving it beside the depletion it belongs with) carried '
    'straight away. The opening of Serotonin Syndrome (SS)? read AI in your post\'s text; my first try read Human in three '
    'of four sentences, with the substance list AI Low; with "(or any other MAOI)" beside the brews and "the painkiller '
    'tramadol and some other opioids", the whole paragraph reads [Human High in one window](' + H +
    'a2d82519-7c1e-4578-9fee-aa547d6ae12d). It is in the guide. Every substance is kept, and "DXM cough syrup", "the '
    'painkiller tramadol" and "the antibiotic linezolid" are your own glosses from step 1, brought up to where they are '
    'first named ([every check](' + H76 + ')).',
    'The charcoal and poison control paragraphs read Human High too, on my first try, but they say three things your post '
    'didn\'t, so they are the card below and not in the guide yet. After it the work goes down '
    '[the list of what is left](' + LEFT + '): 137 of 222 blocks.',
]

card(id='CHARCOAL-HOUR', type='question', advice='ask',
     title='1. Swallowed Too Much?: the charcoal and poison control paragraphs, with the hour from the review they cite',
     whose=('the post\'s text, drafted by a model (no version of yours on record for either paragraph); the stance on poison '
            'control is yours'),
     question=('Both paragraphs as they stand read [AI Generated, High](' + H + '862a4a34-aeee-4b38-921d-64db9367992b). This '
               'version reads [Human High, 200 words in one window](' + H + '75a2458d-38e7-4413-8d12-9ac6f8e7824c):\n'
               '"' + NEW1 + '"\n'
               '"' + NEW2 + '"\n'
               'Three things in it are new, all from [the review the paragraph already cites](' + REVIEW + ') (Zellner and '
               'others, 2019), whose link now sits on "within the last hour or so" in place of the bare "Clinical review." '
               'label. It says to give charcoal "as soon as possible, within the first hour of the ingestion", and up to 6 '
               'hours after for timed-release preparations, which is my "slow-release pills leave a few hours more". Its '
               'list of what charcoal binds poorly or not at all has alcohols and lithium on it, along with iron and other '
               'metals, acids and bases, cyanides, and solvents, DMSO among them.\n'
               'One thing the same review says against your stance: a poison control centre or a doctor should be contacted '
               'before somebody who isn\'t medical gives charcoal. Your "I don\'t treat calling poison control as a mandatory '
               'ritual" stays as you have it; tell me if you want the review\'s view said next to it.\n'
               'Your closing line, "It is decision support, not first aid.", is said as what to do: "so go on with any first '
               'aid while you talk to them". All four cases of the warning stay (vomiting, sedated, seizing, unable to '
               'protect the airway), now with what happens to them.\n'
               'In, or not?'),
     why=('it reads Human High, but it sharpens a medical caution: the hour, the slow-release note and the two examples are '
          'not in your post, and your closing line becomes an instruction'),
     stays='both paragraphs as your post has them',
     advice_note='in; and leave your stance on poison control as it is',
     spans=[whole(P('B127')), whole(P('B128'))])
