# The cards of round 23, read by build_r23.py (which defines P, T, whole, span_of, replace_words, cut_words, cut_block and
# card). P('B318') is the page block of GUIDE-SO-FAR-blocks.json's B318 (the guide after round 22's answers). The checks are
# in articles/bad-trips/humanize/h29-20261107 (this pass) and h19, h25 and h26 (earlier).

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
ASKED = ('he asked: Joel, 2026-11-07 12:08 UTC: "if you can\'t figure out how to humanize things, give me the top most '
         'important paragraphs (usually 1 or 2) that youu think i could teach you from that would help you humanize the rest, '
         'and give me your best tries on those to fix."')
ON_BASE = 'each read after the Human first half of Psychological First Aid and the section\'s heading'

INTRO = [
    'Round 23 (2026-11-07). Your two versions from round 22 are in. Your denial move made six more paragraphs read Human. '
    'Your After the Storm moves didn\'t carry in my hands: 0 of 12 tries read Human, though I used a question to the reader, '
    'the why, "(or false)"-style nuance, "an" for "one", and the list said in a voice\'s own words. So here are the next two '
    'paragraphs to teach me from. They\'re the kinds most of the stuck instructions share: a long list of don\'ts, and a '
    'numbered list of steps. A fresh reader read each one for sense first, and the cards say what it found.',
    'Everything that tested well and kept the meaning went into the guide without a card; my message lists it.',
]

card(id='TEACH-DONTS', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='No Rash Actions: a long list of don\'ts',
     reading=('As the guide has it, with the action lock before it, %s: [AI, 100%%](%s173cdc51-97bf-4765-ba5a-87b141a65ca8).'
              % (ON_BASE, H)),
     tested=('1. "What really can\'t wait until you\'ve slept and eaten? Usually nothing, so don\'t drive, travel, break up, ..." '
             '[AI, 100%%](%sf59db310-a21b-42a9-9964-8c6cc58f9439). This try puts a question to the reader first and keeps the '
             'list.\n\n'
             '2. The lock said as talk ("Give it 24–72 hours before you act on anything."), with the list after it: '
             '[73%%](%s424017ee-a823-4d47-bff5-fa5903d0f8c0).') % (H, H),
     sense=('"Send the message" and "post the revelation" don\'t say which message, or post where. The 24–72 hour lock just '
            'above it and this list\'s "until you have slept and eaten" give two different ends. Driving and travel have no '
            'emergency exception (getting to a hospital). "Confront" and "accuse" overlap. The list never says why (judgment is '
            'off, and none of these can be undone), and what to do instead is the next line ("Write it down, get some sleep, '
            'and go back over it sober with one grounded person"). My tries above didn\'t fix any of these. "Make a grand '
            'purchase" is the item you approved in round 21.'),
     why=('Fifteen don\'ts in one sentence, and it reads AI in every wording I\'ve tried. The same shape is in After the Storm\'s '
          '"another ceremony" list, Shadow Thoughts\' during-a-trip paragraph, the helper\'s don\'ts, the harm part\'s lines, '
          'and Abuse Memories\' "Don\'t confront tonight".'),
     advice_note=('Edit it: say it the way you\'d tell someone at 3 a.m. Keep every item, or tell me which can go. I\'ll carry '
                  'what you do to the paragraphs above, test each, and put the ones that read Human straight in.'),
     spans=[whole(P('B318'))])

card(id='TEACH-STEPS', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='Minimum Viable Integration: a numbered list of steps',
     reading=('As the guide has it, %s: [66%%](%s4b8c71dd-d48b-40bf-81e8-e1b89c15b779).' % (ON_BASE, H)),
     tested=('1. The why put inside two steps ("write down the facts while you still remember them"; "think about what the '
             'experience may have meant ... (it may mean less than it felt like, or more)"): '
             '[75%%](%s0ce22da5-c317-48aa-8f72-095be4450e94).\n\n'
             '2. The third step said as talk: [73%%](%s6dfd0d19-13a4-4600-a727-1977d8f3104e).') % (H, H),
     sense=('The heading\'s "Minimum Viable Integration" is startup jargon, and "integration" isn\'t explained anywhere before '
            'it. "Ordinary contact", "no big moves", "behavioral changes" and "increase love" are vague, and "no big moves" '
            'repeats No Rash Actions\' lock. "Then" and "Last" give no timing. The list never says why facts come before '
            'meaning (so the story doesn\'t rewrite what happened), or why to write down the substance and dose (to be safer '
            'next time). My first try covered only some of these.'),
     why=('Four labeled steps, and it reads AI in every wording I\'ve tried. The same shape is in Give the Session a Beginning '
          'and an End\'s list, What Kind of Aftermath Is This?, the distortions list in Why Bad Trips Tend to Happen, the '
          'loop breaker, and Who to Contact\'s directories.'),
     advice_note=('Edit it: keep it a list or make it prose, whichever you\'d write, and keep every step. I\'ll carry what you '
                  'do to the lists above, test each, and put the ones that read Human straight in.'),
     # Published with spans=[whole(P('B423'))], which covered only the list's first item: the page he answered at 22:38 UTC
     # highlighted one line ("i don't understand how you work, you want me to correct only that one line?"). P now refuses a
     # list's first item by default; this is what the card should have spanned. The published REVIEW-R23 files are kept as he
     # saw them, so this script is not re-run for round 23.
     spans=[whole(i) for i in PALL('B423')])
