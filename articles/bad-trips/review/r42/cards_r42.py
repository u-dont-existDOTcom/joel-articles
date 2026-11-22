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
NEW1 = ("(sodium might be too low by then for an electrolyte drink to fix; while you wait for medics, if they're alert and "
        "not vomiting, give them something very salty instead, like strong broth or salty snacks)")
OLD2 = 'A seizure or collapse can result from low potassium,'
NEW2 = 'A seizure or collapse can result from low sodium, magnesium or potassium,'
_b119 = T(P('B119'))

card(id='MED-MDMA', type='safety', advice='approve',
     title='1. MDMA: what "too late for an easy fix" means, and sodium and magnesium in the seizure line',
     what=('Two places in your MDMA paragraph. "(sodium might be too low and it could be too late for an easy fix)" '
           'becomes "%s". "A seizure or collapse can result from low potassium," becomes "A seizure or collapse can result '
           'from low sodium, magnesium or potassium,". Nothing else changes.' % NEW1),
     tested=('Your version read [Human High 132](%sc45651d9-f45e-4f3e-8496-f340eae874b0); with both fixes as here, after '
             'your message of 15:41 UTC (salty food while waiting; magnesium), [Human Written, 0%% AI, one window Human '
             'High](%s597c5351-fd56-4dbf-9b27-038b9c2d4de5) over all 157 words. The first wording, "so don\'t give them any '
             'more to drink", read [Human High 142](%se1cf44d8-f5fe-4a33-98ac-24780393acd7).' % (H, H, H)),
     why=('Your questions: no more electrolyte drinks once those signs show, since they carry far less salt than blood '
          'and still thin it (the wilderness-medicine guidelines name water and sports drinks as the cause of low sodium '
          'from overdrinking, and restrict fluids once it\'s suspected); and yes to something hypertonic: the same '
          'guidelines treat mild low sodium with salt by mouth, a very strong broth or salty food, when the person is alert '
          'and can keep it down, and MDMA harm-reduction advice says the same (salty snacks, less water, get ready to get '
          'help). Hospitals use a concentrated salt drip. "Too late for an easy fix" read as "nothing can be done", and a '
          'fresh reader of my first wording couldn\'t tell whether to call or to feed them, so it now says "while you wait '
          'for medics". And the seizure line: low sodium and low magnesium both bring seizures, and low magnesium often '
          'brings low potassium with it and keeps potassium from coming back up, which fits your magnesium-first '
          'experience; very low potassium brings weakness and heart rhythm trouble.'),
     stays='Every other word of your paragraph, and your sipping line before the signs, which is for before any of them show.',
     deciding=('Approve puts both in. Revise if you\'d say them your way. The fresh readers also asked two things, not '
               'changed: the seizure line names causes but no action (your "The following indicators would justify '
               'calling medics:" covers it), and "like my second wife had" is your story from the paragraph before.'),
     advice_note='Approve: both hold up against the sources, and the paragraph still reads Human High.',
     ask_because=('his own: two places in his round-41 version change, which he asked me to check ("altho i\'m not sure i '
                  'clarified it correctly medically speaking. check to make sure")'),
     whose='his own: his round-41 version of the MDMA paragraph (TEACH-MDMA, c45651d9)',
     receipt='articles/bad-trips/humanize/h56-20261119/TEST-mdma-hisfix2.receipt.json',
     found_by='your question, and a check of the paragraph against the guidelines',
     edits=[{'block': P('B119'), 'before': _b119, 'after': _b119.replace(OLD1, NEW1).replace(OLD2, NEW2)}],
     spans=[span_of(P('B119'), OLD1), span_of(P('B119'), 'low potassium, and can also come')])
