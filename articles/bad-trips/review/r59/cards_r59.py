# The cards of round 59, read by build_r59.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 69: his round-58 charcoal and poison control paragraphs in the guide, and two
# paragraphs of My Acute Rescue Remedies at Human High (humanize/h77-20261125/RESULTS.md). No string here is %-formatted.

BUILT = '2026-11-25'
H = 'https://www.pangram.com/history/'
R58 = BLOB + 'articles/bad-trips/review/r58/RESULTS-R58.md'
H77 = BLOB + 'articles/bad-trips/humanize/h77-20261125/RESULTS.md'
LESSONS = BLOB + 'docs/lessons/2026-11-25-1743-bad-trips.md'
LEFT = BLOB + 'articles/bad-trips/humanize/h77-20261125/LEFT.md'
POISON = 'https://www.poison.org/articles/2017-jun/activated-charcoal'
NEWP = ('If you\'re unsure about the interactions between the drugs taken, it could be helpful to check with AI & Poison '
        'Control. They might have important info, especially if the drugs are well-known. They can also help you with '
        'standard first aid instructions. But I wouldn\'t ask Poison Control about charcoal. Someone I know did, and came '
        'away very confused after being told they aren\'t allowed to tell anyone to take it.')

INTRO = [
    'Round 59 (2026-11-25). Your charcoal and poison control paragraphs are in, word for word, and the two read '
    '[Human High in one window](' + H + '7b62fe4a-c50a-4bbc-9c3b-1fcf7448e3a6). The link to the remedy entry is back on '
    '"Activated charcoal", and the review\'s link is on "The usual advice", since the hour is what that review says. '
    'What I got wrong is [here](' + LESSONS + '): I kept a model\'s advice from your post (ask poison control about '
    'charcoal) as if it were yours, and I wrote a rule measured on pure, fast drugs into a guide about plant medicines. '
    '[Each point of your answer and where it went](' + R58 + ').',
    'Two more paragraphs now read Human High by themselves, both in My Acute Rescue Remedies and both in the guide '
    '([every check](' + H77 + ')). In "Nausea, heat, exhaustion ..." four words changed ("all get read as spiritual '
    'signs" for "all become spiritual content"): Low, then Medium, then [High](' + H +
    '6058dbfc-dc05-444e-b564-51b72e8acc74). The gut-driven paragraph is card 2.',
    'After these the work goes down [the list of what is left](' + LEFT + '), starting with the gut tools.',
]

card(id='POISON-LINE', type='question', advice='ask',
     title='1. Swallowed Too Much?: one clause of your poison control paragraph',
     whose='his own: the paragraph from his round-58 answer; the two sentences I suggest are mine',
     question=('Your paragraph is in as you wrote it. One clause I\'d say differently: "even if they often can\'t give '
               'actionable advice for liability reasons". What you told me is one case, about charcoal ("poison control '
               'said they aren\'t allowed to tell them to take charcoal"), and your next sentence says they do help with '
               'first aid instructions. [Poison Control\'s own page](' + POISON + ') says of charcoal that "it is not '
               'recommended to use these products at home to treat a poisoning", so anyone who asks them about it will '
               'hear what the person you know heard. This version says that, with the link on "they aren\'t allowed to '
               'tell anyone to take it", and reads [Human High, 74 words in one window](' + H +
               '9afb6a77-e533-49d1-8f65-b20306e090ca) on its first check:\n'
               '"' + NEWP + '"\n'
               '(a) leave yours as it is; (b) this one; or your own words.'),
     why=('your clause says more than your case shows ("often", "for liability reasons"), and the reader who does ask about '
          'charcoal is not told what will happen'),
     stays='your paragraph, which is in the guide now',
     advice_note='(b); fairly sure. It keeps your three sentences word for word and adds only what happened to the person you know',
     spans=[whole(P('B128'))])

card(id='GUT-SIGNS', type='question', advice='ask',
     title='2. My Acute Rescue Remedies: two things a reader in the moment couldn\'t tell',
     whose=('the post\'s paragraph, drafted by a model, with your own last line kept word for word ("A gut-driven mental '
            'hell is often mistaken as shadow work.")'),
     question=('This paragraph is in and reads [Human High, 75 words in one window](' + H +
               '8f7d99cd-1a1e-4b29-b0e5-0b1e1659c02a); your post\'s read [AI, High](' + H +
               'a378ba15-aee0-4b83-9ca8-702971cc31c6). Every sign is kept, and "a different branch" is now "the remedies '
               'below" and "the shadow work further down". Two things a fresh reader, sitting with a friend who has '
               'diarrhea and says their mind is going crazy, couldn\'t get from it, and only you know the answers:\n'
               '2.1 What would a friend actually see when someone has "loss of bodily control" or "neurological '
               'disorganization"?\n'
               '2.2 Diarrhea and nausea are common on a psychedelic anyway. How do you tell a gut-driven mental hell from '
               'a mainly emotional crisis while it is happening?\n'
               'A line or two from you on either and I\'ll put it in; or (a) leave the paragraph as it is.'),
     why='the section holds no answer to either, and a guess from me would be a model\'s advice in your guide again',
     stays='the paragraph as it now reads',
     advice_note='your answer to 2.2, even one sentence: it is the question the whole section turns on',
     spans=[whole(P('B141'))])
