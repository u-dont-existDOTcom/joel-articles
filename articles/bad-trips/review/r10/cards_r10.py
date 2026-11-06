# The card of round 10, read by build_r10.py (which defines P, T, whole, span_of, cut_block, replace_words and card).
# P('B238') is the page block of GUIDE-SO-FAR-blocks.json's B238 (the guide after round 9). The checks are in
# articles/bad-trips/humanize/h08-20261106/RESULTS.md; the tell panel on the stretch is that folder's panel-STRETCH/PANEL.md.

BUILT = '2026-11-06'
H = 'https://www.pangram.com/history/'
HUMB = BLOB + 'articles/bad-trips/humanize/h08-20261106/'

INTRO = [
    'Round 10 (2026-11-06). Your round-9 approval is in: the room\'s first part is one paragraph now, with your '
    'annoying-room line said plainly at its start.',
    'In place, though, the room stretch still reads AI. Each part reads Human on its own, but your first paragraph and '
    'your next two read AI together, in one window. Three readers say why, and four of the sentences they agree on are '
    'yours, so the one card asks for your version of the stretch.',
]

TYPES = {
    'yours': {'label': 'Your version', 'about': 'paragraphs that read AI together, where the readers agree on your '
              'sentences: your new words are the fix'},
}

card(id='STRETCH-YOURS', type='yours', advice='edit', keep_label='keep them as they are',
     title='The room stretch, in place: Human apart, AI together',
     reading=('Each paragraph, and all three together:\n'
              '- The first (the fix you approved), alone: [Human Written, 0%%](%s07e19481-bb99-4b40-932f-ab16315f4502); '
              'High, Medium, then Low on its last sentence.\n'
              '- The second and third (your round-8 version), alone: [Human Written, 0%%](%s26e9138d-9b91-44e0-bb5c-7a21a7e4dddc); '
              'Medium, High, Medium.\n'
              '- All three, as the guide has them now: [AI, 100%%, High](%s34d92f15-18c7-4849-9972-983239961bf9), one '
              'window. With my checks of things your paragraph fixes taken out of the first: '
              '[AI, 100%%, High](%s3d9ca55e-df3a-4ea4-8866-2d6071ba1b10).') % (H, H, H, H),
     why=('All three readers ([their notes](%spanel-STRETCH/PANEL.md)) agree on how the stretch is built: a list of '
          'problems, then the remedies in the same order, then a sample line, nearly every sentence a short tip. Two or '
          'three of them agree on four sentences, all in your second and third paragraphs: "They\'re feeling overwhelmed, '
          'so dim the lights, and clear out the extra people around them." (formulaic after a list of problems), "Ask if '
          'they\'d like a hand on the shoulder." and "Speak slowly and use fewer words." (tips stacked in a row), and "If a '
          'track starts pulling the experience somewhere unwanted, go ahead and change it." ("somewhere unwanted" doesn\'t '
          'say what the music does). All three paragraphs are yours to change, the first one included.') % HUMB,
     advice_note=('Edit it: say the stretch your way; the order and the paragraph breaks are yours too. Or keep them as '
                  'they are; together they read AI.'),
     found_by='checking the stretch in place after round 9 (a changed paragraph is checked where it stands, gate E197)',
     spans=[whole(P('B238')), whole(P('B240')), whole(P('B241'))])
