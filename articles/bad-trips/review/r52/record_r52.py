"""record_r52.py - his round-52 answers in OWNER-EDITS.json (run after apply_r52.py, from the repo root):

  python3 articles/bad-trips/review/r52/record_r52.py [--ledger PATH]

New: r52-answers (his women sentence in his MDMA paragraph, and the dance paragraph after it, from WOMEN-RISK and
DANCE-ENERGY). Changed in r51-answers, each with what replaced it: the dance line (moved to the new paragraph, its "it's
natural to want to dance" out, since he says real MDMA doesn't give that pull) and the plain-water line (fewer words).
"""
import argparse
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r52/ANSWERS-R52-20261124-0126.json'
WHEN = '2026-11-24 01:25 UTC'
ap = argparse.ArgumentParser()
ap.add_argument('--ledger', default=str(ART / 'OWNER-EDITS.json'))
p = pathlib.Path(ap.parse_args().ledger)
d = json.loads(p.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}


def change(eid, old, new, note, key=None):
    e = by[eid]
    k = key or ('must_contain_exact' if 'must_contain_exact' in e else 'must_contain')
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


change('r51-answers', "While it's natural to want to dance on MDMA, I'd tell everyone not to dance at all",
       "I'd tell everyone not to dance on MDMA at all",
       'his DANCE-ENERGY answer on round 52 ("Real MDMA ... is NOT the kind of mdma that people want to dance on"): the '
       'line moved to the paragraph after (R52-DANCE), without "it\'s natural to want to dance on MDMA" (r52-answers)')
change('r51-answers', 'Plain water is the risk because MDMA makes the body hold on to water',
       'Plain water is the risk because the drug keeps them from peeing out the extra',
       'the same why in fewer words, its window having read Medium (r52-answers; AGENTS.md: a Medium window is work to do)')
new = {'id': 'r52-answers', 'status': 'applied',
       'what': ('his round-52 answers in the guide, each as it read through the API on his laptop '
                '(humanize/h71-20261124/RESULTS.md): his MDMA paragraph (B119) with his sentence that women are most at '
                'risk and what it rests on; the paragraph after it (R52-DANCE): no dancing on MDMA, San Pedro or '
                'mescaline for dancing, real MDMA as couch lock, a pill that makes someone feel like dancing as one he '
                'suspects, and the lab study his WOMEN-RISK answer asked to note, with the other way the lab differed '
                '(review/r52/apply_r52.py)'),
       'joel': '%s: his round-52 export (%s), WOMEN-RISK and DANCE-ENERGY' % (WHEN, ANS),
       'applied_by': 'review/r52/apply_r52.py',
       'must_contain_exact': [
           'Women are most at risk of this, based on the results we have',
           'sodium was mildly low in 1 in 4 of the women on ecstasy vs only 3% of the men',
           'with women at four times the odds',
           'San Pedro cactus or mescaline, which is way way safer, and still very therapeutic',
           "isn't the kind people want to dance on",
           'I NEED TO DANCE!',
           'It\'s not like "I don\'t feel like dancing", it\'s like "I can barely move", couch lock',
           "I'm highly suspicious that it contains amphetamines",
           'a lab study that gave people pure MDMA and water found no difference between them',
           'the lab dosed everyone by their weight, and at a festival a small woman takes the same pill as a big guy'],
       'must_not_contain': ["While it's natural to want to dance on MDMA"]}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']), '->', p)
