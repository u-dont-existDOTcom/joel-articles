"""record_r50.py - his round-50 answers in OWNER-EDITS.json and KEEP-AS-IS.json (run after apply_r50.py, from the repo
root):

  python3 articles/bad-trips/review/r50/record_r50.py

New: r50-ss-steps (steps 2, 5, 6, 7, 8 from his QUIZ-2, SS-DRINK and SS-ASKED-2 answers), r50-naloxone (his paragraph,
his check 73e392f4), r50-advice-call ("No sleep for days", "acting on a delusion"), r50-ozone-repeat (his cut).
Changed, each with what replaced it: r35-body-once (its insomnia line), r48-teach-ss (his steps 5 and 6, now carried by
his round-50 answers), r49-his-steps and r49-asked-answers (step 7's breathing line and step 8's lines, now in his
round-50 order).
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r50/ANSWERS-R50-20261123-1913.json'
WHEN = '2026-11-23 19:13 UTC'
p = ART / 'OWNER-EDITS.json'
d = json.loads(p.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}


def change(eid, old, new, note):
    e = by[eid]
    lst = e['must_contain_exact']
    if old in lst:
        lst[lst.index(old)] = new
    elif new not in lst:
        lst.append(new)
    note = ' | %s: %s' % (WHEN, note)
    if note not in e['what']:
        e['what'] += note


change('r35-body-once', '- Severe insomnia', '- No sleep for days',
       'his ADVICE-CALL answer on round 50 ("agree with all") made the line "No sleep for days" (r50-advice-call)')
change('r48-teach-ss',
       "I'd have them do some fidgeting (especially of the calf muscle, flexing the feet), which can soothe that urge "
       "without the over-activity risk.",
       "5. Since they're already overstimulated, it helps to clear out the crowd and stop any arguing.",
       'his round-50 answers replace the fidgeting with his tapping (SS-ASKED-2 e) and his drink line with his SS-DRINK '
       'and QUIZ-2 notes (r50-ss-steps); this check now holds his openings of steps 5 and 6')
change('r48-teach-ss',
       "6. Overstimulating also dehydrates them, but we can't give fluids unless they're fully alert, able to swallow and "
       "not vomiting, and then just small sips of an electrolyte drink (a hypertonic one, more concentrated than an "
       "ordinary one, may be required if they still have symptoms of lack of electrolytes).",
       "6. Overstimulating also dehydrates them, but we can't give fluids unless they're fully alert, able to swallow and "
       "not vomiting, and then just small sips of an electrolyte drink.",
       'step 6 after his first sentence is now from his SS-DRINK and QUIZ-2 notes (r50-ss-steps)')
change('r49-his-steps',
       "Keep track of how their breathing is doing, as that's one of the main indicators of how dangerous the seizure is",
       "keep track of how their breathing is doing afterward, as that's one of the main indicators of how dangerous the "
       "seizure is",
       'his breathing line now follows the seizure first aid in the same sentence (his QUIZ-2 marks on step 7; '
       'r50-ss-steps)')
change('r49-his-steps', "Topical magnesium chloride if they're not able to swallow.",
       "Topical magnesium chloride if they're not able to swallow",
       'his line goes on with his Epsom salt answer ("or Epsom salt if that\'s all you have", r50-ss-steps)')
change('r49-asked-answers', 'Niacin is actually unsafe with serotonin syndrome, since at the doses used to end a trip',
       "it's actually unsafe with serotonin syndrome, since at the doses used to end a trip",
       'step 8 now names niacin first and DMSO as one to use (his SS-ASKED-2 answer c; r50-ss-steps)')
change('r49-asked-answers',
       'Magnesium chloride is the one I would consider, since many people with serotonin syndrome run low on magnesium',
       "Magnesium chloride is the other one I'd use, since many people with serotonin syndrome run low on magnesium",
       'with DMSO now one to use, magnesium chloride is "the other one" (r50-ss-steps)')
change('r49-asked-answers', "Topical magnesium chloride if they're not able to swallow.",
       "Topical magnesium chloride if they're not able to swallow", 'as in r49-his-steps')

NEW = [
    {'id': 'r50-ss-steps', 'status': 'applied',
     'what': ('the serotonin steps from his round-50 answers, each as it read Human through the API on his laptop '
              '(humanize/h69-20261123/RESULTS.md): step 2 with his dose lines (QUIZ-2), step 5 with his tapping '
              '(SS-ASKED-2 e), step 6 from his SS-DRINK and QUIZ-2 notes, step 7 with the seizure first aid and his '
              'breathing line, step 8 with his DMSO answer and his Epsom salt (review/r50/apply_r50.py)'),
     'joel': '%s: his round-50 export (%s), QUIZ-2, SS-DRINK and SS-ASKED-2' % (WHEN, ANS),
     'applied_by': 'review/r50/apply_r50.py',
     'must_contain_exact': [
         'say to give an adult 12mg to start, then 2mg every 2 hours if symptoms persist, up to 32mg per 24 hours. And '
         'tell medics how much you gave.',
         "I'd have them do some tapping (the Emotional Freedom Technique, fingers tapping the head)",
         'That can be as simple as a salty potato broth with some magnesium chloride flakes stirred in',
         "If you don't have the flakes, Epsom salt works too, although it causes diarrhea more easily.",
         "And if they have a seizure before the ambulance gets there, I'd do the first aid in",
         "seems to help prevent seizures, so if there's any sign of an overdose, I'd have them smell it",
         "or Epsom salt if that's all you have, though Epsom salt gets through the skin less well."],
     'must_not_contain': ['do some fidgeting (especially of the calf muscle, flexing the feet)',
                          "but I wouldn't use either one here",
                          'with stem cell infusions']},
    {'id': 'r50-naloxone', 'status': 'applied',
     'what': ('his naloxone paragraph after the Call Medics For list, whole, as his check 73e392f4 read it (Human High '
              '99; review/r50/HIS-NALOXONE.txt, read back from his history)'),
     'joel': '%s: his QUIZ-2 comment on round 50 (%s), with his Pangram link' % (WHEN, ANS),
     'applied_by': 'review/r50/apply_r50.py',
     'must_contain_exact': [(ART / 'review' / 'r50' / 'HIS-NALOXONE.txt').read_text(encoding='utf-8').strip()]},
    {'id': 'r50-advice-call', 'status': 'applied',
     'what': '"No sleep for days" in the Call Medics For list and "acting on a delusion" in If Someone Might Get Hurt',
     'joel': '%s: ADVICE-CALL on round 50, "agree with all" (%s)' % (WHEN, ANS),
     'applied_by': 'review/r50/apply_r50.py',
     'must_contain_exact': ['- No sleep for days', 'acting on a delusion'],
     'must_not_contain': ['- Severe insomnia', 'acting delusional']},
    {'id': 'r50-ozone-repeat', 'status': 'applied',
     'what': 'the crying baby paragraph says the ozone point once: "No ozone gas was present, only the water."',
     'joel': '%s: REPEATS on round 50, "yes agree" (%s)' % (WHEN, ANS),
     'applied_by': 'review/r50/apply_r50.py',
     'must_contain_exact': ['No ozone gas was present, only the water.'],
     'must_not_contain': ['the residual ozone had dissipated']},
]
for e in NEW:
    if e['id'] not in by:
        d['entries'].append(e)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']))
