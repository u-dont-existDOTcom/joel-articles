"""record_r48.py - record his round-48 changes where the checks read them.

Run from the repo root after apply_r48.py:
  python3 articles/bad-trips/review/r48/record_r48.py

1. humanize/h01/FIDELITY-KEYS-R48.json: R47 plus his TEACH-SS-STEPS change. His steps 5 and 6 took out the
   sentence "Don't force fluids, food, pills, or charcoal when someone is confused, vomiting, sleepy, or at seizure
   risk." (unit W043). His step 6 keeps its fluids half in his words ("we can't give fluids unless they're fully
   alert, able to swallow and not vomiting"), so the keys "fluids" and "7" (step 6 still comes before step 7) stay
   held; "pills", "don't" and "risk" went with the sentence. The last two would otherwise match the list by chance
   ("Don't drive yourself", "raises the risk of their muscles breaking down"), the R47 lesson.
2. OWNER-EDITS.json: his steps 5 and 6 (r48-teach-ss) and his two heading answers (r48-headings).
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
ANSWERS = 'articles/bad-trips/review/r48/ANSWERS-R48-20261121-1557.json'


def keys_r48():
    src = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R47.json'
    out = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R48.json'
    d = json.loads(src.read_text(encoding='utf-8'))
    by = ('%s, card TEACH-SS-STEPS (his version of steps 5 and 6, 2026-11-21 15:57 UTC): he took out "Don\'t force '
          'fluids, food, pills, or charcoal when someone is confused, vomiting, sleepy, or at seizure risk." as '
          'redundant and not the right medical advice ("now i fixed the last part, it was redundant and also i think '
          'not giving the correct medical advice"); his step 6 keeps the fluids condition in his words, and his step 2 '
          'already gives its pill only "If the person is fully alert and able to swallow"' % ANSWERS)
    if not any(c.get('by') == by for c in d['owner_changes']):
        d['owner_changes'].append({'by': by, 'keys_lost': {'W043': [['pills'], ["don't"], ['risk']]}})
    note = (' | R48 (2026-11-21 15:57 UTC, turn 59): R47 with his round-48 steps 5 and 6 (TEACH-SS-STEPS), which take '
            'out the "Don\'t force fluids, food, pills, or charcoal" sentence (W043: "pills", "don\'t" and "risk" out; '
            '"fluids" and "7" still held by his step 6)')
    if note not in d['about']:
        d['about'] += note
    out.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('wrote', out.relative_to(REPO))


def owner_edits():
    p = ART / 'OWNER-EDITS.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    new = [
        {'id': 'r48-teach-ss', 'status': 'applied',
         'what': ('his steps 5 and 6 of Act Now on SS in whole, from his TEACH-SS-STEPS version, with one obvious '
                  'correction (the comma after "Since" out); the old step 5 and 6 text and the "Don\'t force fluids, '
                  'food, pills, or charcoal" sentence out, his change (review/r48/apply_r48.py)'),
         'joel': ('2026-11-21 15:57 UTC: his round-48 export (%s), card TEACH-SS-STEPS: "now i fixed the last part, it '
                  'was redundant and also i think not giving the correct medical advice, now all human high"' % ANSWERS),
         'applied_by': 'review/r48/apply_r48.py',
         'must_contain_exact': [
             "5. Since they're already overstimulated, it helps to clear out the crowd and stop any arguing.",
             'the problem is that creates more body heat, and it raises the risk of their muscles breaking down into '
             'the blood, which hurts the kidneys (rhabdomyolysis).',
             "I'd have them do some fidgeting (especially of the calf muscle, flexing the feet), which can soothe that "
             'urge without the over-activity risk.',
             "6. Overstimulating also dehydrates them, but we can't give fluids unless they're fully alert, able to "
             'swallow and not vomiting, and then just small sips of an electrolyte drink (a hypertonic one, more '
             'concentrated than an ordinary one, may be required if they still have symptoms of lack of electrolytes).'],
         'must_not_contain': ['Keep stimulation low and prevent exertion.',
                              'Hydrate only when fully alert and not vomiting.',
                              "Don't force fluids, food, pills, or charcoal",
                              "Since, they're"]},
        {'id': 'r48-headings', 'status': 'applied',
         'what': ('his answers to R47-1 and R47-2: the coffee cherry heading "Coffee Cherry, Brain Too" (its link kept '
                  'on "Coffee Cherry") and "Who to Contact"; the section links catalog renamed with them'),
         'joel': '2026-11-21 15:57 UTC: "r47-1a / r47-2a"',
         'applied_by': 'review/r48/apply_r48.py',
         'must_contain_exact': ['### [Coffee Cherry](http://coffeecherry.u-dont-exist.com/), Brain Too',
                                '## Who to Contact'],
         'must_not_contain': ['(Coffee Cherry for Brain also)', 'Who to Contact, and When']},
    ]
    have = {e['id'] for e in d['entries']}
    for e in new:
        if e['id'] not in have:
            d['entries'].append(e)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('owner edits:', len(d['entries']))


if __name__ == '__main__':
    keys_r48()
    owner_edits()
