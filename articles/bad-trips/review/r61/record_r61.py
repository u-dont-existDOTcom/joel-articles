"""record_r61.py - his round-61 answers in the fidelity keys, OWNER-EDITS.json and KEEP-AS-IS.json (run after
humanize/h79-20261126/apply_h79.py charcoal and review/r61/apply_r61.py, from the repo root):

  python3 articles/bad-trips/review/r61/record_r61.py

CHARCOAL-WORDS "a": Activated Charcoal as it read Human High (ae42aae9) goes in, and his rule from now on: "a line whose
only warning word isn't a caution may be said in other words, as long as every fact stays". FIDELITY-KEYS-R61.json is
R58 with "not_cautions" naming the two lines (W049, "toxicity"; W051, "stop"), the form fidelity_keys.py reads since
this turn. TEACH-B155 "revise": his version of B155, whole. FROM-POST: read as (a), since he answered only the rubbing
("yes mix in water when rubbing on body"): the four lines from his ZeoCharge post stay as they went in, the post's 5g
"take more" line stays out (C21), and B158's rubbing is with zeolite mixed in water (h80, once it reads Human High).
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r61/ANSWERS-R61-20261127-1534.json'
WHEN = '2026-11-27 15:34 UTC'
RULE = ('%s, card CHARCOAL-WORDS (2026-11-27 15:34 UTC): his "a", "my version goes in, and from now on a line whose only '
        'warning word isn\'t a caution may be said in other words, as long as every fact stays"' % ANS)

k58 = json.loads((ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R58.json').read_text(encoding='utf-8'))
k61 = dict(k58)
k61['about'] = k58['about'] + (' | R61 (2026-11-27 15:34 UTC, turn 72): R58 with his round-61 CHARCOAL-WORDS "a": the two '
                               'Activated Charcoal lines whose only warning word is no caution are freed (not_cautions), '
                               'and his TEACH-B155 version, which keeps every key.')
k61['not_cautions'] = [
    {'unit': 'W049', 'cues': ['toxicity'], 'by': RULE,
     'why': '"toxicity" names what charcoal helps ("can help gut toxicity"); the line tells the reader nothing to avoid or '
            'watch for. Its facts (drugs bind to charcoal as gut toxins do, so it can flatten a trip) stay in the first '
            'paragraph of Activated Charcoal.'},
    {'unit': 'W051', 'cues': ['stop'], 'by': RULE,
     'why': '"stop" is what the reader wants charcoal for ("stop a toxic gut situation"), not an instruction to stop '
            'anything. Its facts (charcoal for someone who took too much or whose gut is toxic; zeolite when the trip '
            'should be kept) stay in the second paragraph of Activated Charcoal.'},
    {'unit': 'W054', 'cues': ['toxicity'], 'by': RULE + '; applied in turn 72 to Beach Morning Glory (humanize/h80-20261127)',
     'why': '"toxicity" is part of "serotonin toxicity", one item in a list of what the MDMA branch covers; the line warns '
            'of nothing. Its facts stay: MDMA has its own section, which the link opens, and every item of the list is said '
            'in the medical part (magnesium, overheating, sodium, potassium, water and seizures in MDMA: Magnesium Alarm; '
            'serotonin toxicity in Serotonin Syndrome (SS)?).'}]
(ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R61.json').write_text(json.dumps(k61, ensure_ascii=False, indent=1) + '\n',
                                                                 encoding='utf-8')

his = {x['id']: x for x in json.loads((ART.parents[1] / ANS).read_text(encoding='utf-8'))['items']}['TEACH-B155']['your_version']
o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
new = {'id': 'r61-answers', 'status': 'applied',
       'what': ('his round-61 answers: TEACH-B155 his version of B155, whole (his checks: Human High 65 by itself, 00eb45f1; '
                'Human High 133 with B158, 54b91410); CHARCOAL-WORDS "a", Activated Charcoal as it read Human High 94 '
                '(ae42aae9) and his rule for lines whose only warning word is no caution (FIDELITY-KEYS-R61.json, '
                'not_cautions); FROM-POST read as (a): the 5g line stays out, and the rubbing is with zeolite mixed in water '
                '(review/r61/RESULTS-R61.md)'),
       'joel': '%s: his round-61 export (%s)' % (WHEN, ANS),
       'applied_by': 'humanize/h79-20261126/apply_h79.py charcoal; review/r61/apply_r61.py',
       'must_contain_exact': [s.strip() + '.' for s in his.strip().rstrip('.').split('. ')] + [
           "I don't treat charcoal and zeolite as interchangeable, because drugs bind to activated charcoal as well as gut toxins, so it can flatten or reduce a trip."],
       'must_not_contain': ['If the zeolite dose at 5g', 'charcoal may be relevant']}
by = {e['id']: e for e in d['entries']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

k = ART / 'KEEP-AS-IS.json'
kk = json.loads(k.read_text(encoding='utf-8'))
cut = {'id': 'C21', 'quote': 'If the zeolite dose at 5g',
       'what': ('his ZeoCharge post\'s line "If the zeolite dose at 5g makes you feel worse (or only slightly better), you (usually) '
                'need to take MORE. But if taking more does make you feel worse, then you might have a bad zeolite!", left out of '
                'the guide (in a guide for someone sitting with a friend it says to give more to a person who feels worse); round '
                '61\'s FROM-POST asked, and he answered only the rubbing, which keeps it out until he says otherwise'),
       'joel': 'yes mix in water when rubbing on body', 'when': WHEN, 'where': 'round 61, FROM-POST (%s)' % ANS,
       'basis': 'his answer, read as (a): he picked neither (b) nor a line of his own'}
if not any(x['id'] == cut['id'] for x in kk['cuts']):
    kk['cuts'].append(cut)
k.write_text(json.dumps(kk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('fidelity keys R61 written | owner edits:', len(d['entries']), '| meant cuts:', len(kk['cuts']))
