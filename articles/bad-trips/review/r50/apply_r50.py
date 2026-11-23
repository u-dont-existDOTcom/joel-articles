"""apply_r50.py - his round-50 answers (ANSWERS-R50-20261123-1913.json, 2026-11-23 19:13 UTC) into the guide, from the
repo root:

  python3 articles/bad-trips/review/r50/apply_r50.py

Each text goes in exactly as it was checked through the Pangram API on his laptop with his key (humanize/h69-20261123/,
RESULTS.md there has every link), with its links and bold back:

- Serotonin steps (B136, under "Act Now on SS"):
  - step 2: his two dose lines from his QUIZ-2 answer ("the guidelines say to give an adult 12mg to start ...") after
    the step as it stood, "the guidelines" linked to the Maryland Poison Center sheet (TEST-a5-ss2, Human High 128);
  - step 5: his tapping from his SS-ASKED-2 answer (e), in his form "(the Emotional Freedom Technique, fingers tapping
    the head)" (TEST-a6-ss5, Human High 96);
  - step 6: from his SS-DRINK and QUIZ-2 notes: the salty potato broth with magnesium chloride flakes, Epsom salt if
    there are no flakes, slowly, potassium from food (TEST-a5-ss6, Human High 157);
  - step 7: his two sentences as they were, then the seizure first aid while waiting for the ambulance with his
    breathing line (TEST-a6-ss7b, Human High 91);
  - step 8: his DMSO answer (c) in his order, his line for the skin with his Epsom salt answer, and why MDMA-related
    jaw tension or twitching matters (TEST-a8-ss8, Human High 227, the whole step one window).
- His naloxone paragraph (his check 73e392f4, Human High 99, read back from his history: HIS-NALOXONE.txt) after the
  Call Medics For list, as its own paragraph.
- The call list's "Severe insomnia" made "No sleep for days" and the harm paragraph's "acting delusional" made "acting
  on a delusion" (ADVICE-CALL: "agree with all"; TEST-a5-call read AI High as before, the list goes on the humanize
  list whole; TEST-a5-harm Human High 67).
- The crying baby paragraph's repeat cut to "No ozone gas was present, only the water." (REPEATS: "yes agree";
  TEST-a5-ozone Human High 38).
"""
import difflib
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
MD = ART / 'GUIDE-SO-FAR.md'
BL = ART / 'GUIDE-SO-FAR-blocks.json'
H69 = ART / 'humanize' / 'h69-20261123'
HERE = pathlib.Path(__file__).resolve().parent

STEPS = {2: 'TEST-a5-ss2', 5: 'TEST-a6-ss5', 6: 'TEST-a5-ss6', 7: 'TEST-a6-ss7b', 8: 'TEST-a8-ss8'}
SWAPS = {  # block: (test file, the only changes it may make)
    'B94': ('TEST-a5-call', [('Severe insomnia', 'No sleep for days')]),
    'B276': ('TEST-a5-harm', [('delusional', 'on a delusion')]),
    'B196': ('TEST-a5-ozone', [('; this was contact with the water after ozonation had ended and the residual ozone had '
                                'dissipated', ', only the water')]),
}


def text(name):
    return (H69 / (name + '.txt')).read_text(encoding='utf-8').strip()


def main():
    blocks = json.loads(BL.read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    b = by['B136']
    lines = b['md'].split('\n')
    assert len(lines) == 8 and lines[6].startswith("7. The ER doctors will want to know"), lines[6][:60]
    for n, name in STEPS.items():
        lines[n - 1] = '%d. %s' % (n, text(name))
    b['md'] = '\n'.join(lines)
    for bid, (name, allowed) in SWAPS.items():
        old, new = by[bid]['md'], text(name)
        if old == new:
            continue
        ops = [(old[i1:i2], new[j1:j2]) for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new).get_opcodes()
               if t != 'equal']
        assert ops == allowed, (bid, ops)
        by[bid]['md'] = new
    if 'R50-NALOXONE' not in by:
        nal = (HERE / 'HIS-NALOXONE.txt').read_text(encoding='utf-8').strip()
        i = [x['id'] for x in blocks].index('B94')
        blocks.insert(i + 1, {'id': 'R50-NALOXONE', 'kind': 'p', 'md': nal, 'text': None})
    MD.write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    BL.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: steps 2, 5, 6, 7, 8; his naloxone paragraph after the call list; No sleep for days; acting on a '
          'delusion; the ozone repeat cut')


if __name__ == '__main__':
    main()
