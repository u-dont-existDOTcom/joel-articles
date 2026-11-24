"""apply_r51.py - his round-51 answers (ANSWERS-R51-20261123-2335.json, 2026-11-23 23:35 UTC) into the guide, from the
repo root:

  python3 articles/bad-trips/review/r51/apply_r51.py

Each text goes in exactly as it was checked through the Pangram API on his laptop with his key
(humanize/h70-20261123/RESULTS.md), with its links and bold back:

- Step 6 (B136, under "Act Now on SS"), from his QUIZ-3 notes: salty potato chips for the salt and potassium, as many as
  they want, potassium only in food, high potassium bringing on vomiting and diarrhea (stop the chips then), magnesium on
  the skin (it tastes too bad to drink), Epsom salt is magnesium sulfate; the magnesium of step 8 moved here, as he asked
  ("is there no way to keep it with the previous mention?"). Human, High 125 / Medium 22 / High 106 (90be4010).
- Step 8, from his SS-OIL and QUIZ-3 answers: DMSO first (the things to do first), some people react more strongly than
  others; then niacin; then Syrian rue oil as a last resort, set apart from the brew in step 1. Human, High 73 / Medium 39 /
  High 33 / Medium 31 (3ea237f3).
- His MDMA paragraph (B119), from his MDMA-SODIUM answer: no dancing on MDMA, why plain water lowers sodium, and how much
  salt (a snack is too little: the guidelines' three or four bouillon cubes in half a cup of water). Human, High 87 /
  Medium 32 / High 131 (c5f90479). The two sentences of round 51's card (women; bloated but not thirsty) stay out, as he
  said.
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
MD = ART / 'GUIDE-SO-FAR.md'
BL = ART / 'GUIDE-SO-FAR-blocks.json'
H70 = ART / 'humanize' / 'h70-20261123'


def text(name):
    return (H70 / (name + '.txt')).read_text(encoding='utf-8').strip()


def main():
    blocks = json.loads(BL.read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    lines = by['B136']['md'].split('\n')
    assert len(lines) == 8 and lines[5].startswith('6. Overstimulating also dehydrates them') and lines[7].startswith('8. ')
    lines[5] = '6. ' + text('TEST-a2-ss6')
    lines[7] = '8. ' + text('TEST-a2-ss8')
    by['B136']['md'] = '\n'.join(lines)
    old = by['B119']['md']
    assert old.startswith('Once their jaw tenses') or old == text('TEST-a2-mdma')
    by['B119']['md'] = text('TEST-a2-mdma')
    MD.write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    BL.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: steps 6 and 8, his MDMA paragraph')


if __name__ == '__main__':
    main()
