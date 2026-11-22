#!/usr/bin/env python3
"""apply_r48.py - his round-48 answers into the guide (ANSWERS-R48-20261121-1557.json and his message of 15:57 UTC):

  - TEACH-SS-STEPS: his version of the serotonin steps 5 and 6, whole, with one obvious correction ("Since, they're" ->
    "Since they're"; his rule of 2026-11-19: "no need to ask me for obvious corrections"). His Pangram check of it read
    Human High in every window (924a9caa). He cut the "Don't force fluids, food, pills, or charcoal ..." line: "it was
    redundant and also i think not giving the correct medical advice" (his card comment); its fidelity keys go in
    FIDELITY-KEYS-R48.json as his change.
  - R47-1 a: "Coffee Cherry, Brain Too", the Coffee Cherry link kept on its words.
  - R47-2 a: "Who to Contact".
  Both renames go through tools/humanization/section_links.py rename, so the catalog (SECTION-LINKS.json) follows.

  python3 articles/bad-trips/review/r48/apply_r48.py        (from the repo root)
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
ANS = json.loads((HERE / 'ANSWERS-R48-20261121-1557.json').read_text(encoding='utf-8'))
FIX = {'Since, they\'re already overstimulated': 'Since they\'re already overstimulated'}
RENAMES = {'B166': ('Coffee Cherry, Brain Too', '### [Coffee Cherry](http://coffeecherry.u-dont-exist.com/), Brain Too'),
           'B261': ('Who to Contact', '## Who to Contact')}


def his_steps():
    v = [x for x in ANS['items'] if x['id'] == 'TEACH-SS-STEPS'][0]['your_version']
    for a, b in FIX.items():
        assert v.count(a) == 1, a
        v = v.replace(a, b)
    paras = [p.strip() for p in v.split('\n') if p.strip()]
    assert len(paras) == 2, paras
    return paras


def main():
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = {b['id']: b for b in B}
    lines = ids['B136']['md'].split('\n')
    assert lines[4].startswith('5. **Keep stimulation low and prevent exertion.**'), lines[4][:60]
    assert lines[5].startswith('6. **Hydrate only when fully alert and not vomiting.**'), lines[5][:60]
    p5, p6 = his_steps()
    lines[4], lines[5] = '5. ' + p5, '6. ' + p6
    ids['B136']['md'] = '\n'.join(lines)
    for bid, (_, md) in RENAMES.items():
        assert ids[bid]['md'].startswith('#'), bid
        ids[bid]['md'] = md
    MD.write_text('\n\n'.join(x['md'] for x in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    # the catalog follows each rename (section_links.py rename: the heading's new anchor, and the links to it)
    cat = ART / 'SECTION-LINKS.json'
    old = {'B166': '(Coffee Cherry for Brain also)', 'B261': 'Who to Contact, and When'}
    for bid, (heading, _) in RENAMES.items():
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'section_links.py'), 'rename', str(cat),
                            old[bid], heading, '--write'], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        print(r.stdout.strip())
    print('applied: his steps 5 and 6, and', ', '.join(h for h, _ in RENAMES.values()))


if __name__ == '__main__':
    main()
