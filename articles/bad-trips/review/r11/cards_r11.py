# The cards of round 11, read by build_r11.py (which defines P, T, whole, span_of, replace_words and card).
# P('B234') is the page block of GUIDE-SO-FAR-blocks.json's B234 (the guide after his cuts of 19:43). The checks are in
# articles/bad-trips/humanize/h10-20261106/RESULTS.md; each changed paragraph's making-sense receipt is in that folder's
# receipts/.

BUILT = '2026-11-06'
H = 'https://www.pangram.com/history/'
REC = 'articles/bad-trips/humanize/h10-20261106/receipts/'

INTRO = [
    'Round 11 (2026-11-06). Your cuts are in: the room stretch keeps "They\'re feeling overwhelmed, so dim the lights, and '
    'clear out the extra people around them." Water, the hand on the shoulder, speaking slowly and the music paragraph '
    'went, since the Do list, Touch, Consent, and Compassion, Get One Human Anchor and the Grounding Menu say them more '
    'fully, and the sips moved to the Do list\'s "Water?". Round 10 is withdrawn.',
    'Two cards for the rest of Psychological First Aid: its AI lines said plainly, and one paragraph moved next to the '
    'script it belongs with. Pangram still reads the section AI with them, so they are for reading, like the cuts; the '
    'Pangram work on the section goes on.',
]

NEW = {
    'B234': ("The triage app gives the order. This section is about carrying it out without becoming one more source of "
             "pressure.",
             "The triage app gives you the order to do things in, and this section is about doing them in a way that takes "
             "pressure off the person."),
    'B238': ("Somebody might be touching them when they don't want it, or they're stuck beside someone they don't trust.",
             "Somebody might be touching them and they hate it, or they're stuck beside someone they're wary of."),
    'B242': ("Give them ordinary reality:",
             "Then remind them where they are and what's happening, since a trip can make them lose track of it:"),
    'B243': ("You took [substance, if known]. These effects rise, peak, and change. This is intense, but it will change. We "
             "don't need to solve your life tonight.",
             "You took [substance, if known], and its effects will peak and then change. It's intense right now, and it'll "
             "pass. We can sort out the rest of your life tomorrow."),
    'B244': ("When the state came from meditation, breathwork, fasting, kundalini-style practice, extreme stretching, ritual, "
             "or a retreat, say:",
             "If the state came from a practice, like meditation or fasting, the person can say:"),
    'B245': ("I am in an intense state. I am stopping the practice now. My job is ordinary safety.",
             "I'm in an intense state, so I'm stopping the practice now, and my only job is to stay safe."),
    'B246': ("From there, choose one safe body experiment and one calm human. The next two sections explain those choices. "
             "Protect sleep, especially when the person is euphoric or grandiose, and let meaning wait until the nervous "
             "system has somewhere to stand.",
             "Then help them pick one safe thing to try with their body and one calm person to stay with them, which the next "
             "two sections are about. Protect their sleep too, especially if they're euphoric or grandiose, and leave what it "
             "all meant until they've slept."),
    'B247': ("A non-drug altered state may have a less predictable clock than a substance. The practical move remains simple: "
             "stop the practice, eat something ordinary when safe, let the body settle, keep warm, and sleep. An open portal "
             "does not obligate you to keep pushing through it.",
             "A state from a practice has no drug wearing off on a schedule, so there's no telling how long it will last. "
             "Once they can eat safely, food and warmth help their body settle."),
}
ORDER = ['B234', 'B238', 'B242', 'B243', 'B244', 'B245', 'B246', 'B247']
EDITS = [replace_words(P(b), NEW[b][0], NEW[b][1]) for b in ORDER]

card(id='PFA-PLAIN', type='plain', advice='approve',
     title='Psychological First Aid: its AI lines said plainly',
     reading=('The section as the guide has it after your cuts: [AI, 100%%, High](%s61c41c42-af3a-4799-8e71-0c5b012f5ddc), '
              'one window of 400 words.') % H,
     tested=('With these changes: [AI, 100%%, High](%sd84fe208-0c91-4c8e-bd31-3ac86bc7c5e5), one window of 423 words; its '
             'first half, the intro, the dangers and the room: [AI, High](%s253d68a8-a75d-462c-b441-bbc2e2bbef08); its second '
             'half, the scripts and what comes next: [AI](%s24b4a581-d85d-4705-b54d-42090068ac6d), in seven windows.')
            % (H, H, H),
     what=('Eight paragraphs get your usual fix. The intro is one sentence. The room\'s "when they don\'t want it" and '
           '"someone they don\'t trust" say what is so. The two scripts each speak in one voice, with no triad, and their '
           'lead-ins say what each is for and who speaks. The practice paragraph says why that state needs its own care, '
           'without the portal line. The last paragraph says who picks.'),
     why=('These were the section\'s AI lines, untouched until now. "My job is ordinary safety", "let meaning wait until the '
          'nervous system has somewhere to stand" and "An open portal does not obligate you to keep pushing through it" '
          'are the quips your standing order covers, and the room\'s two phrases are "X does not Y". Fresh readers also '
          'couldn\'t tell who says the practice script, or who picks the body experiment.'),
     stays=('The dangers paragraph, the rest of the room paragraph, the overwhelmed sentence, every safety point and the '
            'triage app\'s link.'),
     deciding='Approve puts all eight in; Revise lets you change any of them first.',
     advice_note=('Approve: it reads better and does what your quips and "X does not Y" orders ask. Pangram still reads the '
                  'section AI, so the work on it goes on.'),
     found_by='fixing the section after your cuts (h10-20261106)',
     receipt=[REC + 'RECEIPT-%s.json' % b for b in ORDER],
     edits=EDITS,
     spans=[span_of(P(b), NEW[b][0]) for b in ORDER])

card(id='PFA-MOVE', type='structure', advice='approve',
     title='The practice paragraph moves next to its script',
     what=('The paragraph about a state that came from a practice moves up, to right after that state\'s script, before '
           'the paragraph that sends the reader on to the next two sections.'),
     why=('It is about the practice case, so it reads best with that case\'s script; the last paragraph then closes the '
          'section and leads into the two sections it names.'),
     stays='Every word; the wording is the other card\'s.',
     deciding='Approve moves it.',
     advice_note='Approve.',
     found_by='a fresh reader of the section, who couldn\'t tell which case the eating and warmth were for',
     card_after=P('B247'),
     moves=[{'blocks': [P('B247')], 'before': P('B246')}])
