# The cards of round 34, read by build_r34.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). The teaching round he asked for once the guide made sense (gate bad-trips-2026-11-07c),
# after the humanize pass's first batch (../../humanize/h42-20261111/RESULTS.md) and my first fixes
# (../../humanize/h43-20261111/RESULTS.md, where every try below has its prediction, receipt and check).

BUILT = '2026-11-11'
H = 'https://www.pangram.com/history/'
H42 = BLOB + 'articles/bad-trips/humanize/h42-20261111/RESULTS.md'
H43 = BLOB + 'articles/bad-trips/humanize/h43-20261111/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that", and 17:24 UTC: "it\'s not all the generic trip safety advice you could find with any ai search"')

INTRO = [
    'Round 34 (2026-11-11). The first Pangram batch ran in your account: 49 sections, 16 read Human Written, one Mostly '
    'Human and 32 have a window labelled AI ([every section, with each window\'s confidence and link](%s)). Your Medium '
    'windows are on the questions page, for you to fix if you want.' % H42,
    'Then my fixes, your five first (the point first, a term explained where it\'s first used, what belongs together '
    'joined, the plain word, a long list taken apart). In the guide now: Nausea Smoothers\' last sentence ([Human, '
    'High](%sd00c127c-6a07-4d03-af6e-cf7fd9eae9c7)), the Grounding Menu\'s going-outside and exercise lines ([Low to '
    'Medium](%s7fd43eaf-b126-4b77-a6f9-53b4456044e2)), DMSO\'s interactions and contraindications ([Human, High '
    'throughout](%sf0dd7b3f-af71-4078-9c23-ff4d6de8a714)), the ocean water section ([Human, High '
    'throughout](%s913f21aa-5675-4649-b12e-9ee80fe5b7ff)), and Get One Human Anchor\'s first two paragraphs '
    '([Human](%s3a3fd073-98e1-46ea-9e5d-342bd7c7ee67)), which had read AI in 38 earlier wordings. DMSO\'s seizure '
    'contraindication said again what Active Seizure says about DMSO, so it now says the contraindication and points '
    'there. Two tries read worse than the words they replaced and stayed out ([every try](%sRESULTS.md)).'
    % (H, H, H, H, H, H43),
    'Card 1 is the teaching card: Risk of Harm\'s list of when to get urgent help, which read AI in each of my wordings, '
    'including one written from two fresh readers\' notes. Its shape runs through most of the medical part. Card 2 asks '
    'about your "adjunct remedy" in Active Seizure, since keeping it keeps that sentence at Low.',
]

card(id='TEACH-HARM', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. Risk of Harm: when to get urgent help',
     reading=('The whole section in the first batch: [AI Generated, 100%%](%s44d2df44-70d3-40a7-95ec-b59dc7743cd7).' % H),
     tested=('1. Its nine reasons taken apart into five sentences, the firm ones kept firm (your fifth fix): [AI Generated, '
             '100%%](%s4c6f1bf6-513b-4f95-8a5c-35d9916efd43).\n\n'
             '2. A second wording went to two fresh readers before Pangram ([their notes](%spanel-harm-b2/PANEL.md)): both '
             'flagged every sentence, and the whole shape, an even run of "if this, call" with a thesis up front and a '
             'summing-up line at the end.\n\n'
             '3. Written from their notes: no thesis and no summing-up line, each reason said a different way, two of the '
             'body\'s signs named instead of "listed above", and an ending on the sitter\'s own doubt ("If you find '
             'yourself wondering whether this is more than you can safely handle, it probably is, so call."): [AI '
             'Generated, 100%%](%s52763d5d-523d-4c61-baba-c9e66c5fd445).') % (H, H43, H),
     sense=('Fresh readers of my tries found every reason needed; only the heading was flagged, as a repeat. The guide\'s '
            'sentence asks the reader to translate two phrases in the moment ("command voices or fixed terrifying beliefs '
            'driving action", "exceeds what the sitter can safely contain"), and "has dangerous physical symptoms" is the '
            'whole Call medics list just above it.'),
     why=('Its shape, a list of when to call for help, runs through most of the medical part, and it reads AI everywhere '
          'it is: Call medics for ([100%%](%sa491b633-dc0d-44b6-bdf1-7584860063b4)), Recent Oral Toxic Ingestion '
          '([100%%](%sbb092688-faa8-46b1-9b14-b124951061eb)), Suspected Serotonin Syndrome '
          '([100%%](%s4a5da2d5-a8b4-44f4-87d1-b86df0781db3)), Who to Contact '
          '([96%%](%seaea5237-3875-4885-bf38-ce7f596d0301)), the helper\'s "Call crisis or emergency services for ..." '
          '([100%%](%sb37b776e-bbda-46e4-8ecb-e5f82130d88e)) and Chest Pain\'s "new, severe, persistent, worsening, '
          'radiating, or exertional pain" ([AI, High](%sce00d5dc-1e58-4c03-9b82-628409d40764)). Your fifth fix, the Judge '
          'Amos list, is for a don\'t-list a reader can relax about. This is the firm kind, where someone could get hurt, '
          'and I haven\'t found your way of saying it yet.') % (H, H, H, H, H, H),
     advice_note=('Edit it: say when you\'d tell someone to get urgent help, in your words. Keep every reason, or tell me '
                  'which can go; "dangerous", "unreachable" and "severely" are kept as warnings, so keep those words or say '
                  'they can change. I\'ll carry what you do to the lists named above, test each, and put the ones that '
                  'read Human straight in.'),
     spans=[whole(P('B276'))])

FIX2 = ("While a seizure continues, the rescue medicine comes first, and I'd still consider DMSO alongside it, although "
        "that's experimental.")
FIX3 = ("While a seizure continues, the rescue medicine comes first, and I'd treat DMSO as a plausible adjunct remedy, "
        "although that's experimental.")
OLD = "I'd treat it as a plausible experimental adjunct remedy rather than something to wait on while a seizure continues."
card(id='ADJUNCT', type='question', advice='ask', title='2. Active Seizure: keep "adjunct remedy" at Low, or read higher?',
     question=('The DMSO paragraph in What Else May Help ends on a sentence that reads Human but Low. "Adjunct remedy" is on '
               'your keep list from round 5, where adding "remedy" took that paragraph to Human. How each option would '
               'read:\n\n'
               'A: as it is: "%s" [Human, Low](%sa9e74179-83f2-4805-be65-b8057c632bbc).\n\n'
               'B (my pick): "%s" [Human, Medium](%s83f4caef-593d-4931-af86-fdb8c79f53db). It says what DMSO goes '
               'alongside, which was the reason for "remedy", but "adjunct remedy" goes.\n\n'
               'C: B with "adjunct remedy" kept: "%s" [AI, Low](%s5f6a6b57-47ce-4db7-ac73-5746241a5d28).') % (OLD, H, FIX2, H, FIX3, H),
     why='"Adjunct remedy" is on your keep list, so I won\'t change it without asking, and keeping it keeps this sentence at Low.',
     stays='A, as it is.',
     advice_note='B, fairly sure: it reads higher and still says what DMSO is an add-on to.',
     spans=[span_of(P('N-CBD-3'), OLD)])
