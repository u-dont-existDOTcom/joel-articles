"""SC-DMSOb: the DMSO item again, after the 1967 paper he sent on 2026-11-13 (14:05 UTC): Ramírez & Luza, "Dimethyl
sulfoxide in the treatment of mental patients", Annals of the New York Academy of Sciences 141 (1967), 655-667, doi
10.1111/j.1749-6632.1967.tb34937.x, read in full (13 pages; DMSO-PTSD.md, "His 1967 paper"). SC-DMSO said no trial had
tested DMSO for anxiety; this study gave it to nine people with severe anxiety or obsessive-compulsive disorder among 42
psychiatric inpatients. So the item gains what was seen in people, at its strength, and its last sentence narrows to PTSD.
"""
import texts_x1112c as C

RAMIREZ = 'https://doi.org/10.1111/j.1749-6632.1967.tb34937.x'
LU, HANSLICK = C.LU, C.HANSLICK
BEFORE, AFTER = C.BEFORE, C.AFTER
S1 = C.S1
S2 = C.S2
S3 = C.S3
S4 = ('Back in 1967, doctors in Lima injected it into the muscles of 42 psychiatric inpatients, and nine of them had '
      'severe anxiety or obsessive-compulsive disorder.')
S5 = ('Within days they grew calmer, and the acute cases went home sooner than 16 patients with similar diagnoses who got '
      'the usual treatments of the time, such as electroshock, insulin comas and tranquilizers ([Ramírez & Luza, '
      '1967](%s)).' % RAMIREZ)
S6 = 'There was no placebo, though, and the patients they were compared with weren\'t picked at random.'
S7 = ('In a second dish study, DMSO at 0.5%% and 1%% killed rat brain cells by itself, and injections of it set off '
      'widespread cell death in young mice\'s brains ([Hanslick, et al, 2009](%s)).' % HANSLICK)
S8 = 'So if you\'re pregnant, don\'t use it, and keep it away from children.'
S9 = 'Nobody has measured how much reaches your brain when you smell it.'
S10 = ('And no trial has tested it for PTSD, so for PTSD it rests on what people report, and many say it helps.')
# the version the needed read and the read against his fixes saw (needed/spdmsob, his-fixes/spdmsob)
READ = {4: 'In people, a 1967 study in Lima gave DMSO, injected into the muscle, to 42 psychiatric inpatients, nine of them '
           'with severe anxiety or obsessive-compulsive disorder.',
        5: 'They grew calmer within days, and the acute cases left the hospital sooner than similar patients on the usual '
           'treatments of that time (Ramírez & Luza, 1967).',
        7: 'But in a second dish study, DMSO at 0.5% and 1% killed rat brain cells by itself, and injected into young mice, it '
           'set off widespread cell death in their brains (Hanslick, et al, 2009).',
        8: 'So keep it away from pregnancy and children.',
        9: 'How much reaches your brain when you smell it hasn\'t been measured, and no trial has tested it for PTSD, so for '
           'that, it rests on what people report, and many say it helps.'}
NEW = ' '.join([S1, S2, S3, S4, S5, S6, S7, S8, S9, S10])
FOR = C.FOR
plain = C.plain
