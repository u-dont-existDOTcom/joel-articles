# The card of round 5, read by build_r05.py (which defines P, T, whole, span_of and card). P('B111') is the page block of
# GUIDE-SO-FAR-blocks.json's B111 (the guide after round 4): the CBD paragraph, round 4's W-CBD2 as he approved it.
# The checks are in ../../humanize/h02-cbd/RESULTS.json, the readers' notes in ../../humanize/h02-cbd/panel-C2/PANEL.md.

BUILT = '2026-11-04'
H = 'https://www.pangram.com/history/'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261103/articles/bad-trips/humanize/h02-cbd/'
BLOB3 = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261103/articles/bad-trips/humanize/h03-pfa/'

INTRO = [
    'Round 4\'s answers are in: W-CBD2 and the four APP cards are in the guide, and the checklist is out now that the '
    'app shows version 9. The three things only the checklist had (its stroke warning signs link, the Chantress Seba '
    'line with your music page, and your love page link) moved into the long part.',
    'This page asks for your help with two paragraphs. You asked me to make the CBD paragraph pass Pangram, and four '
    'versions of it all read AI: three of mine and one by GPT, on your laptop. Then the humanizing started on the '
    'first five minutes, and my versions of its dangers paragraph read AI too. Your own version is what has worked '
    'when that happens, and most of the guide\'s how-to sections read like that one.',
]

TYPES = {
    'yours': {'label': 'Your version', 'about': 'a paragraph every version of mine read AI on: your words are the fix'},
}

card(id='CBD-YOURS', type='yours', advice='edit', title='The CBD paragraph, in your words',
     reading=('Pangram on the section with this paragraph in: [AI Generated, 100%%](%s4a1f3bb6-6bd3-481b-94c1-477de1ea3c8e), '
              'every window AI (High, Medium, High). The paragraph alone, four versions: mine '
              '[100%% AI](%sec075547-e302-4256-856c-e44a9afc3520) (Medium, High), '
              '[95%% AI](%s5edcd0d9-1a19-4c2d-a158-0ef666bde712) (Low, Medium, High) and '
              '[100%% AI](%s926b3ab8-73a1-494a-bcbb-88b6eb578488) (Medium, High); GPT\'s '
              '[100%% AI](%s6d4a8f3f-886e-4ee1-9cd4-671cae701cc7) (Low, Medium, Low, High, Medium).') % (H, H, H, H, H),
     why=('Every version keeps reading AI, in every window. Three fresh readers (Codex, Sonnet, Haiku) say why: it\'s built '
          'like a balanced mini-review, every finding followed by its caveat, the sentences all the same length, and it '
          'ends on a tidy verdict ([their notes](%spanel-C2/PANEL.md)). Even your opening sentence, "I would also use '
          'topical magnesium chloride ...", reads AI (Medium or Low) in every version. The human things they saw in my second version were '
          'small: "people taking a lot of it", "got into the blood", "still did no better", and "I wouldn\'t wait on it '
          'while a seizure keeps going". What it has to keep: purified oral CBD approved for Lennox-Gastaut, Dravet and '
          'tuberous sclerosis complex; for other focal seizures the evidence going both ways; the 12-week trial (a CBD '
          'skin gel reached the blood like oral CBD but did no better than placebo); the 2025 study (high-dose oral CBD, '
          'around 23 mg/kg a day, about 1,400 mg for a 60 kg adult, focal seizures down by half to three quarters over '
          'nearly three years, no placebo group); none of it tested as a fast rescue; DMSO\'s rat studies; and your '
          'judgment that DMSO is an experimental extra you wouldn\'t wait on during a seizure. GPT\'s version had the '
          'weakest AI windows, if you want a start: it put your DMSO judgment first and split the approval in two '
          '([its text](%sC4-codex.txt)).' % (BLOB, BLOB)),
     advice_note=('Edit it: say it your way, keeping those points (the links go back on the study names). Or Keep it as '
                  'it is, if you\'d rather leave this one AI for now.'),
     found_by='your comment on W-CBD2, "now fix it so it passes pangram"',
     spans=[whole(P('B111'))])

card(id='PFA-YOURS', type='yours', advice='edit', title='The first five minutes: the dangers paragraph, in your words',
     reading=('Pangram on the section as I rewrote it: [AI Generated, 100%%](%s38061cf5-7095-4cfb-8d3b-9f50bfa4f111), one '
              'window (High). This paragraph alone: my first try [100%% AI](%s3c87417a-c673-4611-bb59-e08b0dc943d8) (High), '
              'and my second, after the readers\' notes, [100%% AI](%sf2e819da-1d18-4b53-813a-58740905c8b9) (High, then '
              'Medium on the phone sentence).') % (H, H, H),
     why=('Fresh readers agree on why it keeps reading AI. On my first try all three (Codex, Sonnet, Haiku) saw a safety '
          'checklist turned into prose, one hazard to a clause in an even rhythm ([their notes](%spanel-P3T1/PANEL.md)). '
          'On my second, Sonnet and Haiku said that with no first person and nothing at stake for the writer, it reads '
          '"assembled rather than lived" ([their notes](%spanel-P3T2/PANEL.md)). That part I can\'t supply: what you\'ve '
          'seen or what you do yourself is yours to tell. The human things they saw in my two tries were small: "go '
          'somewhere you\'re not", "nobody '
          'tripping should be getting behind a wheel", "or water for that matter", "text an ex" and "take the phone". '
          'The published post\'s check read most of the guide\'s how-to sections this way, so your version shows me '
          'how to do the rest. What it has to keep: the next five minutes come first; the car keys put away and the '
          'stove off; away from roads, balconies and water, weapons, crowds and strangers; and the phone taken when '
          'they\'re about to post a revelation or message an ex.' % (BLOB3, BLOB3)),
     advice_note=('Edit it: say it your way, keeping those points. Or Keep it as it is, and I\'ll try another way '
                  'first.'),
     found_by='the humanize pass, first section (the published post\'s check read it AI, High)',
     spans=[whole(P('B236'))])
