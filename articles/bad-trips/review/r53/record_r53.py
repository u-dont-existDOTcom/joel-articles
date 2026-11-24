"""record_r53.py - his round-53 answer and the Medium windows of steps 6 and 8 in OWNER-EDITS.json (run after
apply_r53.py, from the repo root):

  python3 articles/bad-trips/review/r53/record_r53.py [--ledger PATH]

New: r53-answers. Changed, each with what replaced it: r51-answers (the high-potassium line of step 6) and
r49-asked-answers (the dose in the niacin line of step 8, his "unsafe with serotonin syndrome" kept). Step 8's two
Medium windows both went with that one fix inside the niacin sentence, so his oil and brew sentence is untouched.
"""
import argparse
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r53/ANSWERS-R53-20261124-1420.json'
WHEN = '2026-11-24 14:20 UTC'
DONE = ('AGENTS.md\'s done rule of 2026-11-24, every window High (lesson romance-2026-11-23i: "i often find the medium '
        'windows indicate other issues also")')
ap = argparse.ArgumentParser()
ap.add_argument('--ledger', default=str(ART / 'OWNER-EDITS.json'))
p = pathlib.Path(ap.parse_args().ledger)
d = json.loads(p.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}


def change(eid, old, new, note):
    e = by[eid]
    k = 'must_contain_exact' if 'must_contain_exact' in e else 'must_contain'
    lst = e.setdefault(k, [])
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


change('r51-answers', 'High potassium also brings on vomiting and diarrhea, which then drain it again',
       "So if they start vomiting or get diarrhea, I'd stop the chips, since too much potassium brings those on",
       'step 6\'s Medium window said as the act, with the second half of his note (the vomiting and diarrhea then '
       'draining potassium) out, which all three fresh reads stumbled on (humanize/h72-20261124/reads); it goes to him '
       'on round 54 (r53-answers; %s)' % DONE)
change('r49-asked-answers', "it's unsafe with serotonin syndrome, since at the doses used to end a trip",
       "it's unsafe with serotonin syndrome, since at that dose",
       'the dose of step 8\'s niacin line named where the reader meets it ("at that dose", in place of the trip-ending '
       'doses said twice), and the sign said as what happens (a drop in blood pressure); his words "unsafe with serotonin '
       'syndrome" kept, and both of step 8\'s Medium windows went with that one fix (r53-answers; %s)' % DONE)
new = {'id': 'r53-answers', 'status': 'applied',
       'what': ('his round-53 answer and the Medium windows of steps 6 and 8, each as it read Human High in one window '
                'through the API on his laptop (humanize/h72-20261124/RESULTS.md): his MAPS-SETTING answer in the dance '
                'paragraph, where it is the evidence for the sentence after it; step 6\'s high-potassium line as the act, '
                'with the clause all three fresh reads stumbled on out; the dose of step 8\'s niacin line named where the '
                'reader meets it, which took both of step 8\'s Medium windows (review/r53/apply_r53.py)'),
       'joel': '%s: his round-53 export (%s), MAPS-SETTING' % (WHEN, ANS),
       'applied_by': 'review/r53/apply_r53.py',
       'must_contain_exact': [
           'And in the same exact setting, the pills have gone both ways on me',
           'some had me wanting to dance, and some left me in that couch lock',
           "So if they start vomiting or get diarrhea, I'd stop the chips",
           'since at that dose it can cause flushing and a drop in blood pressure'],
       'must_not_contain': ['which then drain it again', 'at the doses used to end a trip']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']), '->', p)
