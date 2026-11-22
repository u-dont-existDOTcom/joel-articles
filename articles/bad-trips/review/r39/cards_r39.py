# The cards of round 39, read by build_r39.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After his fixes of 2026-11-12 19:44 UTC (../r38/apply_r38b.py,
# ../../experiments/t38-answers/JOEL-VERSIONS-20261112-1944.md) and the carries of turn 40
# (../../humanize/h50-20261112/RESULTS.md).

BUILT = '2026-11-12'
H = 'https://www.pangram.com/history/'
H50 = BLOB + 'articles/bad-trips/humanize/h50-20261112/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-12 14:45 UTC, card MEDICAL-HOW: "a"')

INTRO = [
    'Round 39 (2026-11-12). Your two fixes of 19:44 UTC are in, whole: Active Seizure ([Human Written, High](%s5e41c575-'
    '7ebf-4b42-9059-adddbf2c5a7f)) and My Brain Feels Damaged ([Human Written, High](%sa0b8ac56-c015-4374-afbc-'
    '996a9a37f870)). The Call medics list at the top still said to call for "repeated seizures without normal recovery, or '
    'a first or substantially different seizure", the two you cut from Active Seizure, so its line now says what yours says: '
    '"A convulsive seizure lasting over 5 minutes". Tell me if you want the old line back.' % (H, H),
    'The three lines you cut were each something a friend couldn\'t use right then: a first seizure is what to expect when '
    'an overdose brings one on, nobody can tell a second seizure from the first, and anyone tripping sees differently. '
    'Every read I had asked whether a line was needed or read like your fixes, and these were needed and plain. So before '
    'any check now, a fresh reader asks of each line whether it is true anyway of someone tripping, whether a friend could '
    'tell, and whether it is a rule from another setting. On twelve lines none of your fixes touched, it marked all seven I '
    'expected and passed four of five ([the scores](%sFIT-CALIBRATION.md)). On your own Active Seizure lines it keeps '
    'marking two: "over 5 minutes" (it calls the five-minute wait an epilepsy rule, since a seizure from a drug is already '
    'an emergency) and "dangerously hot" (without a thermometer a friend can\'t tell). Both stay as you wrote them.' % H50,
    'Carried: Active Seizure\'s rescue medicine, rebuilt over ten drafts and said in your first person ("I\'d give it when and '
    'how its label says"), read [Human Written](%s8522369e-b999-481a-84c0-3ab4c0518bef) in its section and is in: your '
    'lists High and Medium, my four sentences Medium, Low, High, Low. The two Low ones are mine to fix next. My Brain Feels '
    'Damaged\'s evidence paragraph read AI however I built it, so it is card 1 ([every test](%sRESULTS.md)).' % (H, H50),
]

card(id='TEACH-EVID', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. My Brain Feels Damaged: why you trust DMSO, and how far the evidence goes',
     reading=('In the first whole-section check, "That judgment is stronger than the clinical evidence, but the evidence is '
              'not empty: ..." read AI High 55 ([AI Detected, 65%%](%s4076db14-325a-4854-88b1-fc3c82da040a)).' % H),
     tested=('One study a sentence, each saying what it found in plain words ("People who\'d had a stroke from a clot may have '
             'recovered better on DMSO in a preliminary trial."), the animal study ending on what it means for the reader '
             '("so it may still help if you start late"): [AI Detected, 72%%](%sa8a986e7-f324-4e8a-9561-b542fa57b413). The '
             'heading and your belief read Human Low; every sentence after them read AI, the animal study AI High.\n\n'
             'Rebuilt around that finding: your belief, how far the evidence goes ("That\'s more than the clinical evidence '
             'shows so far, but what there is points the same way."), then the animal study first, the two findings in '
             'people in one sentence, and the mechanism said plainly with its term in brackets after it, the way you put '
             '"(respiratory depression, from opioids, benzos and alcohol)": [AI Generated, 100%%](%sf7576565-13c8-47d2-9ecb-'
             '02e2a092f284).') % (H, H),
     sense=('A fresh reader said someone deciding whether to trust DMSO could do without the mechanism sentence ("A '
            'mechanism is a plausibility story, not evidence that DMSO works"); the reader against your fixes marked the two '
            'findings in people as packed into one sentence, and the bracketed term as giving the reader nothing to act on.'),
     why=('An evidence paragraph, your belief and then the studies behind it, reads AI whichever way I order or join it. '
          'The guide has more of them: Chest Pain\'s cardiovascular science, the cyproheptadine evidence in the Serotonin '
          'Syndrome steps, the MDMA studies. How you\'d say why you trust DMSO here, and how far the studies go, teaches me '
          'how to say those.'),
     advice_note=('Edit it: why you trust DMSO for a damaged brain, and how far the evidence goes, in your words. Keep your '
                  'belief, that it goes further than the clinical evidence, the clot-stroke trial, the small series for '
                  'pressure inside the skull, the animal research (it still shrank the area of the brain that died when '
                  'given after the stroke) and the NMDA- and AMPA-mediated excitotoxicity, each with its link. Your version '
                  'goes in whole, and I carry what it teaches to the other evidence paragraphs and test them.'),
     spans=[whole(P('B105'))])
