# The cards of round 4, read by build_r04.py (which defines P, T, whole, span_of, cut_block, cut_words, replace_words and
# card). P('B111') is the page block of GUIDE-SO-FAR-blocks.json's B111 (the guide after round 3). Sources opened on
# 2026-11-04: PubMed (Patel et al. 2025; O'Brien et al. 2022) and the FDA's Epidiolex label of May 2026.

BUILT = '2026-11-04'
APP = 'https://ibogaqueen.com/1625-2/'
FDA = 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/210365s024s029s030lbl.pdf'

INTRO = [
    'Round 3\'s answers are in: the 7 you approved are in the guide (the page file sent with this message), W-GLORY '
    'stays out, and your two cuts are on the keep-as-is list so no later pass puts them back.',
    'This page has the rest. W-CBD2 is the CBD paragraph redone from what you sent with your Revise, each point checked. '
    'The four APP cards point the guide\'s mentions of the Quick Bad Trip Checklist at the triage app, because the '
    'checklist leaves the guide once the app shows version 9 (your message of 11:35). Nothing changes until you approve '
    'it.',
]

TYPES = {
    'redo': {'label': 'Your Revise, redone', 'about': 'a paragraph you sent back to revise, redone from what you sent'},
    'app': {'label': 'The checklist moves to the app', 'about': 'a line that points to the checklist, pointed at the '
            'triage app'},
}

CBD_OLD = ('CBD has established antiseizure activity in several epilepsy syndromes, and transdermal CBD reaches systemic '
           'circulation, although it has not been validated as rapid seizure rescue.')
CBD_NEW = ('Purified oral CBD is approved for the seizures of Lennox-Gastaut syndrome, Dravet syndrome and tuberous '
           'sclerosis complex. For focal seizures outside those syndromes, the evidence is mixed. In a 12-week trial, a '
           'CBD skin gel reached the blood at levels like oral CBD\'s but did no better than placebo. In a 2025 study of '
           'high-dose oral CBD, around 23 mg/kg a day (about 1,400 mg for a 60 kg adult), focal seizures fell by about '
           'half to three quarters over nearly three years, but it had no placebo group to compare with. None of it '
           'tested CBD as rapid seizure rescue.')
card(id='W-CBD2', type='redo', advice='approve', title='CBD and seizures, from what you sent',
     what=('The CBD sentences become: "%s" "approved" would link the FDA label, "12-week trial" the trial the guide '
           'links now, and "2025 study" that study.' % CBD_NEW),
     why=('You sent back a summary of the evidence on CBD for focal seizures, and each point checks out. '
          'In the 2025 study (PubMed: [Patel et al. 2025](https://doi.org/10.1111/epi.18496)), 140 people with '
          'treatment-resistant focal epilepsy took purified oral CBD (Epidiolex) in an open program. In the 107 without '
          'tuberous sclerosis, the median dose was 23 mg/kg a day, and focal seizures fell by a median of 46 to 75%% '
          'through 144 weeks. 96%% had side effects, nobody got a placebo, and five of its nine authors work for the '
          'maker. The FDA label approves it for the seizures of Lennox-Gastaut syndrome, Dravet syndrome and tuberous '
          'sclerosis complex, from age 1 ([FDA label, May 2026](%s)). The skin-gel trial is the one the guide links '
          '(PubMed: [O\'Brien et al. 2022](https://doi.org/10.1001/jamanetworkopen.2022.20189)). So high-dose oral CBD '
          'shows a signal for focal seizures, and the skin gel, which is closest to your DMSO-with-CBD plan, didn\'t '
          'beat placebo.' % FDA),
     stays='Your plan of topical magnesium chloride and DMSO with a known CBD preparation, and the DMSO seizure lines.',
     deciding=('The label also lists two interactions for people already on seizure drugs. CBD raises the active form of '
               'clobazam (sleepiness in 46% of those on clobazam, against 16% of the rest), and with valproate it raises '
               'liver enzymes more often. Revise to add a line if your readers may be on those. The question at the end '
               'of what you sent, about which kind of focal seizure, was the tool\'s question to you, and it doesn\'t '
               'change the paragraph.'),
     advice_note='Approve, or Revise.', found_by='your Revise on round 3\'s W-CBD, each point checked',
     edits=[replace_words(P('B111'), CBD_OLD, CBD_NEW)],
     spans=[span_of(P('B111'), CBD_OLD)])


def pointer(cid, bid, old, new, title):
    card(id=cid, type='app', advice='approve', title=title,
         what='"%s" becomes "%s", with "triage app" linking the app.' % (old, new),
         why=('Once the app shows version 9, the Quick Bad Trip Checklist leaves the guide (your message of 11:35 UTC: '
              '"rewrite web app to match the guide if you can, but if you\'re blockewd by guardrails then keep checlist '
              'int he guide"), so this line would point at nothing. The app has the same steps, the 3 a.m. plan '
              'included.'),
         stays='The rest of the paragraph.',
         deciding=('Whether you\'d call it something else. The guide\'s first line calls it "Quick Triage Web-App '
                   'Version", and you called it "the triage app".'),
         advice_note='Approve.', found_by='the checklist\'s move to the app (OWNER-EDITS checklist-to-app)',
         edits=[replace_words(P(bid), old, new)],
         spans=[span_of(P(bid), old)])


pointer('APP-1', 'B234', 'The checklist above gives the order.', 'The triage app gives the order.',
        '"The checklist above gives the order"')
pointer('APP-2', 'B272', 'The quick checklist above contains the stripped-down 3 a.m. plan.',
        'The triage app has the stripped-down 3 a.m. plan.', '"The quick checklist above" and the 3 a.m. plan')
pointer('APP-3', 'B370', 'return to the acute checklist instead', 'return to the triage app instead',
        '"Return to the acute checklist"')
pointer('APP-4', 'B437', 'use the checklist first', 'use the triage app first',
        '"Use the checklist first"')
