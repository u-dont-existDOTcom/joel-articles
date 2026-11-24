"""record_r51.py - his round-51 answers in OWNER-EDITS.json (run after apply_r51.py, from the repo root):

  python3 articles/bad-trips/review/r51/record_r51.py

New: r51-answers (steps 6 and 8 and his MDMA paragraph from his answers). Changed, each with what replaced it:
r42-med-mdma (his salty snacks out, his answer), r49-his-steps and r49-asked-answers (step 8's magnesium moved to step 6,
the oil line and the niacin line in his new order), r50-ss-steps (step 6's broth and Epsom lines, step 8's DMSO line).
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r51/ANSWERS-R51-20261123-2335.json'
WHEN = '2026-11-23 23:35 UTC'
p = ART / 'OWNER-EDITS.json'
d = json.loads(p.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}


def change(eid, old, new, note):
    e = by[eid]
    lst = e['must_contain_exact'] if 'must_contain_exact' in e else e['must_contain']
    if old in lst:
        if new:
            lst[lst.index(old)] = new
        else:
            lst.remove(old)
    elif new and new not in lst:
        lst.append(new)
    note = ' | %s: %s' % (WHEN, note)
    if note not in e['what']:
        e['what'] += note


change('r42-med-mdma', 'give them something very salty instead, like strong broth or salty snacks',
       'give them something very salty instead, like strong broth',
       'his MDMA-SODIUM answer on round 51 ("i\'m also not sure a little salty snack will do much"): the snacks out, the amount said after it (r51-answers)')
change('r49-his-steps', "Topical magnesium chloride if they're not able to swallow",
       'I\'d stir a handful of magnesium chloride flakes into a little water and rub the mix on their skin',
       'his QUIZ-3 answer on round 51 ("it\'s totally fine to just put like a handful of mag chloride flakes in water and then rub that on their skin"); the magnesium is in step 6 now, as he asked (r51-answers)')
change('r49-asked-answers', "it's actually unsafe with serotonin syndrome, since at the doses used to end a trip",
       "it's unsafe with serotonin syndrome, since at the doses used to end a trip",
       'step 8 now gives DMSO first and niacin after it, his QUIZ-3 order (r51-answers)')
change('r49-asked-answers', "I'd also leave out this guide's Syrian rue oil for now", "The other remedy I'd keep for a last resort",
       'his SS-OIL answer on round 51: the oil as a last resort, set apart from the brew (r51-answers)')
change('r49-asked-answers', "Magnesium chloride is the other one I'd use, since many people with serotonin syndrome run low on magnesium",
       'Magnesium also runs low in many people with serotonin syndrome',
       'the magnesium moved to step 6, as he asked (r51-answers)')
change('r49-asked-answers', "Topical magnesium chloride if they're not able to swallow", None, 'as in r49-his-steps')
change('r50-ss-steps', 'That can be as simple as a salty potato broth with some magnesium chloride flakes stirred in',
       'Salty potato chips give the salt and the potassium with nothing to cook',
       'his QUIZ-3 answer on round 51: chips, no cooking (r51-answers)')
change('r50-ss-steps', "If you don't have the flakes, Epsom salt works too, although it causes diarrhea more easily.",
       "If you don't have the flakes, Epsom salt, which is magnesium sulfate rather than a kind of table salt, works the same way, just less well.",
       'his QUIZ-3 answer: on the skin, and Epsom salt is magnesium sulfate (r51-answers)')
change('r50-ss-steps', "seems to help prevent seizures, so if there's any sign of an overdose, I'd have them smell it",
       "which seems to help prevent them, going by people's reports rather than studies: at any sign of an overdose, have them smell it",
       'his QUIZ-3 answer: the things to do first, DMSO before niacin (r51-answers)')
change('r50-ss-steps', "or Epsom salt if that's all you have, though Epsom salt gets through the skin less well.", None,
       'the skin line is in step 6 now (r51-answers)')
new = {'id': 'r51-answers', 'status': 'applied',
       'what': ('his round-51 answers in the guide, each as it read Human through the API on his laptop '
                '(humanize/h70-20261123/RESULTS.md): step 6 (salty potato chips, potassium only in food, high potassium and '
                'vomiting, magnesium on the skin, Epsom salt is magnesium sulfate, step 8\'s magnesium moved here), step 8 '
                '(DMSO first, niacin, the oil as a last resort set apart from the brew), his MDMA paragraph (no dancing, '
                'why plain water lowers sodium, how much salt) (review/r51/apply_r51.py)'),
       'joel': '%s: his round-51 export (%s), MDMA-SODIUM, SS-OIL and QUIZ-3' % (WHEN, ANS),
       'applied_by': 'review/r51/apply_r51.py',
       'must_contain_exact': [
           "so I'd let them eat as many as they want",
           'High potassium also brings on vomiting and diarrhea, which then drain it again',
           'Magnesium chloride tastes too bad for most people to drink, but the skin absorbs it',
           "The oil isn't the Syrian rue brew from step 1, which blocks MAO",
           'if nothing else is helping and no medics are coming',
           "While it's natural to want to dance on MDMA, I'd tell everyone not to dance at all",
           'Plain water is the risk because MDMA makes the body hold on to water',
           'three or four bouillon cubes in half a cup of water'],
       'must_not_contain': ['salty potato broth', 'or salty snacks', 'with stem cell infusions',
                            'Low sodium seems to hit women hardest', 'feel bloated but not thirsty',
                            'almost none of the harmala alkaloids']}
if new['id'] not in by:
    d['entries'].append(new)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']))

# turn 62, after the call list's check (Human High 249): the two entries that held its old lines
NOTE = (' | 2026-11-23 23:53 UTC (turn 62): the call list said line by line the way his Active Seizure call list says its '
        'signs (f6b4e35a), every sign kept, Human High 249 by itself (humanize/h70-20261123/RESULTS.md)')
d = json.loads(p.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}
for eid, old, new in (('r35-body-once', '- Dangerous overheating (not just regular sweating), severe rigidity, or clonus with fever',
                       "- A forehead that's dangerously hot to the touch, not just sweaty"),
                      ('r38b-call-seizure', '- A seizure after taking too much (or an unknown amount), or one on a normal dose lasting over 5 minutes',
                       'after they took too much or nobody knows how much, or one on a normal dose that goes past 5 minutes')):
    e = by[eid]
    lst = e['must_contain_exact'] if 'must_contain_exact' in e else e['must_contain']
    if old in lst:
        lst[lst.index(old)] = new
    if NOTE not in e['what']:
        e['what'] += NOTE
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

