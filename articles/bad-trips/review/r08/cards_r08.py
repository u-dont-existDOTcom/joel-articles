# The cards of round 8, read by build_r08.py (which defines P, T, whole, span_of, replace_words and card). P('B238') is
# the page block of GUIDE-SO-FAR-blocks.json's B238 (the guide after round 7 and "non-profit"). Every check below is in
# articles/bad-trips/humanize/h07-20261105/RESULTS.md, with its prediction in ../../humanize/pangram-ledger.jsonl.

BUILT = '2026-11-05'
H = 'https://www.pangram.com/history/'
HUMB = BLOB + 'articles/bad-trips/humanize/h07-20261105/'
ASKRIGOR = ASKRIGOR_NOTE  # set in build_r08.py from the AskRigor task's report

INTRO = [
    'Round 8 (2026-11-05). Your round-7 answers are in the guide as you approved them, all four cards, and so is '
    '"non-profit": your cannabis paragraph now says "by a non-profit patients\' association called ABRACE", and it read '
    '[Human Written, 0%%](%sa8da55b2-865a-4d5a-88b2-894326eb6851), one window, High.' % H,
    'From the Gemini write-up on ABRACE\'s YouTube channel, nothing else went into the guide. Nearly all of it is about '
    'children with epilepsy (West syndrome, Dravet, refractory cases) taking ABRACE\'s oils by mouth for months, and '
    'how their seizures and quality of life changed, which does nothing for someone whose friend is seizing on MDMA or a '
    'psychedelic right now. Its first-aid video says what the Active Seizure section already says (on their side, nothing '
    'in the mouth, medics at about five minutes), and the THC nasal spray is already in your paragraph, from the '
    'testimony in Congress. ' + ASKRIGOR,
    'The humanize pass then went on to the next stretch of Psychological First Aid: your four paragraphs after the '
    'dangers paragraph, from "Then look at the room" to "This is a bad time to defend the playlist." They read AI as they '
    'are, and so did every version I could make, so the one card is for your version.',
]

TYPES = {
    'yours': {'label': 'Your version', 'about': 'paragraphs that read AI as they are and in every version I made: your '
              'new words are the fix'},
}

READ_HIS = ('Your four paragraphs as they are, checked as two pairs: the room and the annoying room '
            '[AI, 100%%](%s3b1372f7-25fb-4d0d-ae1e-ebb33f5b2159) (Medium on "Then look at the room.", High on the rest), '
            'and the fixes with the music [AI, 100%%](%sadbfab8a-0e1b-4b3e-9718-f7e207d1ed33) (the same). ' % (H, H))
TRIES_B1 = ['59d91e5b-7c0b-4c72-a069-4186cf15d2f9', '89b18a81-c6cf-41be-bb19-791d9619229e',
            '4fe2d34c-39e0-46dd-b12d-a86ebbbc4a50', '35bb7c93-a1cd-4883-8ab7-f4b13891536b',
            'ecfed313-207a-4d78-91e8-d54a8579e652']
TRIES_B23 = ['d40b990c-ff4a-40b7-9ec6-f17fc5633897', '935c6330-d355-4457-90ef-3daff9309d0f',
             '647e8d30-1364-43ab-afb4-f91186802f73', '8d476af3-4e68-484a-a377-ec4e30a683c2',
             'ad0a126d-1ef5-4a92-ac5a-d23405e040d0']
READ_TRIES = ('Five versions each, all AI, 100%%, every window High but "Then look at the room." on its own (Low in the '
              'third room version, Medium in the fourth): the room [1](%s%s), [2](%s%s), [3](%s%s), [4](%s%s), [5](%s%s); '
              'the music, talking and water [1](%s%s), [2](%s%s), [3](%s%s), [4](%s%s), [5](%s%s). The fifth of each is '
              'the other writer\'s.' % tuple(x for k in TRIES_B1 + TRIES_B23 for x in (H, k)))

card(id='ROOM-YOURS', type='yours', advice='edit', keep_label='keep them as they are',
     title='The room, the music and the water, in your words',
     reading=READ_HIS + READ_TRIES,
     why=('Every version had its making-sense receipt and a fresh reader. From the third on, three readers (Codex, Sonnet '
          'and Haiku) said what reads AI before I changed it, and the fifth came from a writer of another model family '
          '(Codex), working from their notes ([the room](%spanel-ROOM-B1-try5/PANEL.md), [the music and water]'
          '(%spanel-ROOM-B2B3-try5/PANEL.md); every round is in [the results](%sRESULTS.md)). What they flagged every '
          'time: a run of instructions all the same length and shape, and your three lines read to them as polished '
          'quips ("a frightened nervous system stuck in an annoying room", "This is a bad time to defend the playlist", '
          '"Please don\'t explain the universe at somebody who is already frightened by it"). I kept those three as you '
          'wrote them, since they\'re yours. What it has to keep: look at the room next, with your reason; the big light '
          'off and a lamp on; five concerned people cut to one or two who stay; nobody touches them unless they want it, '
          'you included; move them away from somebody they don\'t trust; too hot, too cold, desperate for the bathroom; '
          '"music or quiet?", kept low, and a song that makes it worse changed; speak slowly, use fewer words, no '
          'explaining the universe; water offered, not pushed, and sipped, since a lot of water fast is dangerous on '
          'MDMA (that reason is mine: a fresh reader asked what sipping was for). Your dangers paragraph just above went '
          'the same way in round 6: four versions of mine read AI, and yours read [Human Written, 0%%](%se9d8d85c-5c0f-46b6-b780-91652f1efd15).') % (HUMB, HUMB, HUMB, H),
     advice_note=('Edit it: say it your way, keeping those points. The order and the paragraph breaks are yours to change, '
                  'and so are your three lines if you want. Or keep them as they are; they read AI.'),
     found_by='the humanize pass, Psychological First Aid, the paragraphs after your dangers paragraph',
     spans=[whole(P('B238')), whole(P('B239')), whole(P('B240')), whole(P('B241'))])
