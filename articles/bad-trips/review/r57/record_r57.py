"""record_r57.py - his round-57 version in OWNER-EDITS.json, KEEP-AS-IS.json and the fidelity keys (run after apply_r57.py,
from the repo root):

  python3 articles/bad-trips/review/r57/record_r57.py

New: r57-answers (his kidney paragraph as his check 33a4d738 had it; my opening of Serotonin Syndrome (SS)? at Human High).
A cut he meant: C17, the generic "get help sooner" ("changing the generic \"get help sooner\" to \"get to a hospital
ASAP.\""). The fidelity keys from now on are humanize/h01/FIDELITY-KEYS-R57.json: his version's three key losses
("large", "rhabdomyolysis", "one-gram-per-minute") are his changes.
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r57/ANSWERS-R57-20261124-2327.json'
WHEN = '2026-11-24 23:27 UTC'

o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
new = {'id': 'r57-answers', 'status': 'applied',
       'what': ('his round-57 version of the kidney paragraph (B120, TEACH-KIDNEY), whole, as the last of his six checks had '
                'it (33a4d738, Human High 115 in one window; review/r57/HIS-CHECKS-R57.md), with his bold lead and the kidney '
                'study\'s link back on its claim; the API reads it Human High 115 in one window (a1673899). And the opening of '
                'Serotonin Syndrome (SS)? (B130), mine from his post\'s text, Human High 116 in one window in two tries '
                '(a2d82519) (review/r57/apply_r57.py; humanize/h76-20261125/RESULTS.md)'),
       'joel': '%s: his round-57 export (%s), TEACH-KIDNEY, sent with his message of 2026-11-25 01:24 UTC' % (WHEN, ANS),
       'applied_by': 'review/r57/apply_r57.py',
       'must_contain_exact': [
           'People with impaired kidneys do need to be more cautious with high, rapid magnesium dosing, because they may not clear excess magnesium out well.',
           'which depletes it (and shifts other electrolytes dangerously)',
           'not to mention potential muscle breakdown and overheating',
           "However, if they have already taken the MDMA, I'm not saying they should sit there and let the jaw tension get worse.",
           "I just wouldn't tell them to copy my gram-per-minute magnesium chloride dosing approach blindly, since that's a higher-risk situation where they should be taken to a hospital ASAP.",
           'ayahuasca and other MAOI brews (or any other MAOI)',
           'the rescue measures in those other branches do not necessarily treat it'],
       'must_not_contain': ['get help sooner', 'not a reason to sit there with worsening jaw tension']}
by = {e['id']: e for e in d['entries']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

k = ART / 'KEEP-AS-IS.json'
kk = json.loads(k.read_text(encoding='utf-8'))
cuts = [
    {'id': 'C17', 'quote': 'get help sooner',
     'what': ('the last words of the kidney paragraph in his post, out in his version: "where they should be taken to a '
              'hospital ASAP" says what the help is and who does it'),
     'joel': ('ok now i made the 2nd part human by changing the generic "get help sooner" to "get to a hospital ASAP." ... i '
              'clarified "get" to hospital since they need to be taken there'), 'when': WHEN,
     'where': 'round 57, TEACH-KIDNEY (%s)' % ANS, 'basis': 'his answer'},
]
for c in cuts:
    if not any(x['id'] == c['id'] for x in kk['cuts']):
        kk['cuts'].append(c)
k.write_text(json.dumps(kk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

f55 = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R55.json'
f57 = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R57.json'
fk = json.loads(f55.read_text(encoding='utf-8'))
by_ = ('%s, card TEACH-KIDNEY (%s): his version, his check 33a4d738 (Human High): "high, rapid magnesium dosing" for "large, '
       'rapid magnesium doses", "muscle breakdown" for rhabdomyolysis, "my gram-per-minute magnesium chloride dosing approach" '
       'for "my one-gram-per-minute approach" (the one gram per minute itself stays in his amounts paragraph)') % (ANS, WHEN)
if not any(x.get('by') == by_ for x in fk['owner_changes']):
    fk['owner_changes'].append({'by': by_, 'keys_lost': {'W027': [['large']], 'W028': [['rhabdomyolysis']],
                                                         'W029': [['one-gram-per-minute']]}})
fk['about'] = fk.get('about', '') if 'R57' in fk.get('about', '') else (fk.get('about', '') + ' R57 (2026-11-25): his round-57 kidney paragraph\'s three key losses added as his changes.')
f57.write_text(json.dumps(fk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']), '| meant cuts:', len(kk['cuts']), '| fidelity owner changes:', len(fk['owner_changes']))
