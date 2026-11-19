# The card of round 42, read by build_r42.py. After his round-41 export of 2026-11-19 15:15 UTC and his question on the
# MDMA paragraph ("check to make sure. is that right, that their sodium is too low, should people not also give them some
# electrolytes then while they call medics ...?").

BUILT = '2026-11-19'
H = 'https://www.pangram.com/history/'
H56 = BLOB + 'articles/bad-trips/humanize/h56-20261119/'

INTRO = [
    'Round 42 (2026-11-19). In from round 41: your bleed lines first in My Brain Feels Damaged, and your versions of the '
    'cyproheptadine step ([cc5e6563](%scc5e6563-f430-4386-8377-2b28592c2ebc), Human High 58) and the MDMA paragraph '
    '([c45651d9](%sc45651d9-f45e-4f3e-8496-f340eae874b0), Human High 132), whole, the studies linked on your words '
    '([your checks](%sHIS-TRIES-R41.md)).' % (H, H, H56),
    'One card: you asked me to check the MDMA paragraph medically. Two points of it don\'t hold as worded; this card fixes '
    'them in place, and the paragraph still reads Human High by itself.',
]

OLD1 = '(sodium might be too low and it could be too late for an easy fix)'
NEW1 = "(sodium might be too low by then for even an electrolyte drink to fix, so don't give them any more to drink)"
OLD2 = 'A seizure or collapse can result from low potassium,'
NEW2 = 'A seizure or collapse can result from low sodium or potassium,'
_b119 = T(P('B119'))

card(id='MED-MDMA', type='safety', advice='approve',
     title='1. MDMA: what "too late for an easy fix" means, and low sodium in the seizure line',
     what=('Two places in your MDMA paragraph. "(sodium might be too low and it could be too late for an easy fix)" '
           'becomes "%s". "A seizure or collapse can result from low potassium," becomes "A seizure or collapse can result '
           'from low sodium or potassium,". Nothing else changes.' % NEW1),
     tested=('Your version read [Human High 132](%sc45651d9-f45e-4f3e-8496-f340eae874b0); with the two fixes, [Human Written, '
             '0%% AI, one window Human High](%se1cf44d8-f5fe-4a33-98ac-24780393acd7) over all 142 words.' % (H, H)),
     why=('Your question, whether to keep giving electrolytes while calling medics: no, nothing more to drink once those '
          'signs show. Electrolyte and sports drinks carry far less salt than blood, so drinking more of them still thins it; '
          'the wilderness-medicine guidelines on low sodium from overdrinking name water and sports drinks as the cause and '
          'restrict fluids once it\'s suspected, and hospitals treat it with fluid restriction or a concentrated salt drip '
          '(for MDMA too). Vomiting means a drink won\'t stay down, and confusion makes choking a risk. "Too late for an '
          'easy fix" meant that, but it reads as "nothing can be done". And low sodium, not potassium, is what most often '
          'brings the seizures in MDMA cases; very low potassium brings weakness and heart rhythm trouble, which is how '
          'it can bring a collapse.'),
     stays='Every other word of your paragraph, and your sipping line before the signs, which is for before any of them show.',
     deciding=('Approve puts both in. Revise if you\'d say them your way. The fresh readers also asked two things, not '
               'changed: the seizure line names causes but no action (your "The following indicators would justify '
               'calling medics:" covers it), and "like my second wife had" is your story from the paragraph before.'),
     advice_note='Approve: both hold up against the sources, and the paragraph still reads Human High.',
     ask_because=('his own: two places in his round-41 version change, which he asked me to check ("altho i\'m not sure i '
                  'clarified it correctly medically speaking. check to make sure")'),
     whose='his own: his round-41 version of the MDMA paragraph (TEACH-MDMA, c45651d9)',
     receipt='articles/bad-trips/humanize/h56-20261119/TEST-mdma-hisfix.receipt.json',
     found_by='your question, and a check of the paragraph against the guidelines',
     edits=[{'block': P('B119'), 'before': _b119, 'after': _b119.replace(OLD1, NEW1).replace(OLD2, NEW2)}],
     spans=[span_of(P('B119'), OLD1), span_of(P('B119'), 'low potassium, and can also come')])
