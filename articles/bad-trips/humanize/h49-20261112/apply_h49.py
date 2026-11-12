#!/usr/bin/env python3
"""apply_h49.py - turn 39's carries into the guide, each only when its check read Human (RESULTS.md); --dry writes the guide
with the keys given to the scratchpad and runs the fidelity check on it, without touching the guide.

- brainopen-c1: My Brain Feels Damaged's B103, its first three sentences said as one ("Don't dismiss ..."), his remedy
  lines and his electrolytes reason after it as they are (links kept).
- er-c3: Acute Medical's emergency room paragraph (B77), its opening gone (acute-c1 says it), the drugs said plainly.
- seize-c3: Active Seizure's B109 becomes its lead-in and one step a line (H49-SEIZE-LIST); B112 becomes "Call medics if
  any of these happen:" and its list (H49-SEIZE-CALL), moved to follow the first aid, before the rescue medicine (B110).

  python3 apply_h49.py [--dry] KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = HERE.parents[3]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
KEYS = ART / 'humanize/h01/FIDELITY-KEYS-R38.json'
SP = pathlib.Path('/tmp/claude-0/-home-claude/7a3d2b92-4547-585d-83c0-bf816aa7e013/scratchpad')
sys.path.insert(0, str(HERE))
from build_tests import OPEN, FIRST_AID3 as FIRST_AID, CALL3 as CALL, ER3 as ER  # noqa: E402


def apply(B, key):
    ids = [b['id'] for b in B]
    if key == 'brainopen-c1':
        i = ids.index('B103')
        old = ('Do not dismiss that report because the person is high or cannot explain it in clinical language. It may be '
               'anxiety or excessive psychedelic intensity. It may also be acute neurological dysfunction, and the person '
               'experiencing it may be the least able to describe it neatly. ')
        assert B[i]['md'].startswith(old)
        B[i]['md'] = OPEN + ' ' + B[i]['md'][len(old):]
    elif key == 'seize-c3':
        i = ids.index('B109')
        assert B[i]['md'].startswith('Time the seizure. Protect the person from injury')
        lead, lst = FIRST_AID.split('\n', 1)
        clead, clst = CALL.split('\n', 1)
        j = ids.index('B112')
        assert B[j]['md'].startswith('Call medics for a convulsive seizure lasting about five minutes')
        call_blocks = [{'id': 'B112', 'kind': 'p', 'md': clead, 'text': None},
                       {'id': 'H49-SEIZE-CALL', 'kind': 'ul', 'md': clst, 'text': None}]
        del B[j]
        B[i]['md'] = lead
        B[i + 1:i + 1] = [{'id': 'H49-SEIZE-LIST', 'kind': 'ul', 'md': lst, 'text': None}] + call_blocks
    elif key == 'er-c3':
        i = ids.index('B77')
        assert B[i]['md'].startswith('The emergency room is not magic')
        B[i]['md'] = ER
    else:
        raise SystemExit('no such key: %s' % key)


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    keys = [a for a in sys.argv[1:] if not a.startswith('--')]
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    for k in keys:
        apply(B, k)
    text = '\n\n'.join(b['md'] for b in B) + '\n'
    out = SP / 'guide-h49-dry.md' if dry else MD
    out.write_text(text, encoding='utf-8')
    if not dry:
        BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/fidelity_keys.py'), 'check', str(KEYS), str(out)],
                       capture_output=True, text=True)
    print(('dry: ' if dry else 'applied: ') + ', '.join(keys), '|', len(text.split()), 'words')
    print((r.stdout + r.stderr).strip()[-1500:])
