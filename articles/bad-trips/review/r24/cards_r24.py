# The cards of round 24, read by build_r24.py (which defines P, PALL, T, whole, span_of and card). PALL('B284') is every
# page block of GUIDE-SO-FAR-blocks.json's B284 (a list: one page block per item; bad-trips-2026-11-07k). The checks are in
# articles/bad-trips/humanize/h31-20261107 (this pass) and h18 and h22 (earlier).

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
ASKED = ('he asked: Joel, 2026-11-07 12:08 UTC: "if you can\'t figure out how to humanize things, give me the top most '
         'important paragraphs (usually 1 or 2) that youu think i could teach you from that would help you humanize the rest, '
         'and give me your best tries on those to fix."')
ON_BASE = 'each read after the Human first half of Psychological First Aid and the section\'s heading'

INTRO = [
    'Round 24 (2026-11-07). Your don\'t list is in, and Minimum Viable Integration is cut. Then I measured what carried your '
    'list. Without Judge Amos, the BMWs and the 42 seconds it still reads Human, and with them but put back in the old '
    'one-sentence form it reads AI. So your frame did it: "maybe don\'t" over a short list that ends on the reader\'s own '
    'life ("that list of people you\'ve been meaning to..."), "Think twice before", and the slack ending. Your jokes didn\'t.',
    'But your frame with my words read AI in every try, and so did Codex\'s after three fresh readers listed the tells: 13 '
    'tries, none Human. So something in your words is still missing from mine. Here are two shapes your frame can\'t reach on '
    'its own: don\'ts that have to stay firm, and a list of labelled bullets. A fresh reader read each for sense first, and '
    'the cards say what it found.',
]

card(id='TEACH-FIRM', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title="For the Person Helping: don'ts that have to stay firm",
     reading=('As the guide has it, %s: [AI, 100%%](%s771b2b52-0d19-4b81-9998-fec9da89fb3e).' % (ON_BASE, H)),
     tested=('1. Taken apart into a paragraph, with an example of what to say ("that sounds terrifying") and what not to force '
             'said as whose call it is: [AI, 100%%](%s82966a18-0e7d-4de0-859b-c3a3212ca098).\n\n'
             '2. In your frame ("Until they\'ve come down a bit, maybe don\'t try to win an argument with ... whatever cosmic '
             'conclusions they reached ten minutes ago..."), with the don\'ts that matter for safety kept firm, after the tell '
             'panel: [AI, 100%%](%s60cb3add-aa0b-45a2-b8db-b64b9dec6253).\n\n'
             '3. Codex\'s rewrite, given the panel\'s notes and three of your Human paragraphs: '
             '[AI, 100%%](%s2124bf00-b916-4ec9-a55c-0e4596ba7131).') % (H, H, H),
     sense=('"Entities" isn\'t explained, and "Reflect the feeling" has no example. "Don\'t try to win an argument" next to '
            '"Don\'t validate harmful conclusions" leaves the helper not knowing what to say, and "harmful conclusions" has no '
            'example either. "Redirect toward ... sleep" asks for sleep while they\'re still tripping. My tries gave an example '
            'of what to say and of a harmful conclusion ("a plan that ends with somebody getting hurt"), and made sleep where '
            'the night ends. They kept "failing the medicine": all three readers called it the one human phrase in it.'),
     why=('Three don\'ts for the person helping, each a list, and your "maybe" can\'t soften them: validating harm or forcing '
          'touch is never fine. The same shape is in Abuse Memories\' "Don\'t confront tonight", the harm part\'s lines, the '
          'touch part and its consent paragraph, and Who to Contact\'s first list.'),
     advice_note=('Edit it: say it the way you\'d brief a friend who\'s about to sit for someone. Keep a don\'t firm where '
                  'someone could get hurt, and keep every item or tell me which can go. I\'ll carry what you do to the '
                  'paragraphs above, test each, and put the ones that read Human straight in.'),
     spans=[whole(i) for i in PALL('B284')])

card(id='TEACH-LABELS', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='Give the Session a Beginning and an End: a list of labelled bullets',
     reading=('As the guide has it: [AI, 100%%](%s3530eb57-4375-4968-bf17-31a0d34ae3d4), and %s: '
              '[70%%](%s47fef46e-313a-4878-b131-627485d14369), the list AI.' % (H, ON_BASE, H)),
     tested=('1. Made a paragraph in the order of a session (before, during, the end, after), with each term said plainly ("the '
             'sitter (the sober person with you) keeps you safe and offers you choices"): '
             '[AI, 100%%](%sada42227-f30e-44fb-b953-30624d9b169a).') % H,
     sense=('"Altered-state work", "low-directivity support" and "integration time" are jargon, and "let the body understand '
            'that the session has ended" and "return to the room and date" are unclear. The opening promises a beginning, '
            'middle and end, but the six items don\'t follow those three. "When you have a choice:" has nothing to refer to. '
            '"Decide in advance what requires outside help" has no example, and "eat and hydrate when safe" doesn\'t say safe '
            'how. Sleep and food come up twice. My try said each term plainly, cut "When you have a choice:", and put the '
            'items in the order of a session. It left the two mentions of sleep and food, and added no examples, since those '
            'would be new advice.'),
     why=('Six bold labels, each with a run of steps, and it reads AI in every form I\'ve tried, prose included. The same '
          'shape is in What Kind of Aftermath Is This?, the distortions list in Why Bad Trips Tend to Happen, the loop breaker, '
          'and Who to Contact\'s directories.'),
     advice_note=('Edit it: keep it a list or make it prose, whichever you\'d write, and keep every item. I\'ll carry what you '
                  'do to the lists above, test each, and put the ones that read Human straight in.'),
     spans=[whole(P('B366')), whole(P('B367'))] + [whole(i) for i in PALL('B368')])
