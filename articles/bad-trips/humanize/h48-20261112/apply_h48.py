#!/usr/bin/env python3
"""apply_h48.py - turn 38's carries into the guide, each only when its check read Human (RESULTS.md); --dry writes the guide
with the keys given to the scratchpad and runs the fidelity check on it, without touching the guide.

- brain-p1: My Brain Feels Damaged's B104 becomes its lead-in (the action before the checks), the list of checks
  (H48-BRAIN-LIST) and its closing line (H48-BRAIN-2); B106's first sentence, which said the action two paragraphs on,
  goes from there (as apply_h46.py had it for brain-c3).
- acute-c1: Acute Medical and Neurological Rescue's B100 becomes the one paragraph, and B76, whose six conditions it now
  points to on the Call medics list, goes.

  python3 apply_h48.py [--dry] KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = HERE.parents[3]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
KEYS = ART / 'humanize/h01/FIDELITY-KEYS-R36.json'
SP = pathlib.Path('/tmp/claude-0/-home-claude/7a3d2b92-4547-585d-83c0-bf816aa7e013/scratchpad')
sys.path.insert(0, str(HERE))
from build_tests import TESTS  # noqa: E402
STROKE = '[stroke warning signs](https://www.stroke.org/en/about-stroke/stroke-symptoms)'


def apply(B, key):
    ids = [b['id'] for b in B]
    head, body = TESTS[key].split('\n\n', 1)
    if key == 'brain-p1':
        lead, rest = body.split('\n', 1)
        lst, close = rest.split('\n\n', 1)
        i = ids.index('B104')
        assert B[i]['md'].startswith('While using DMSO, check wakefulness')
        assert lead.count('stroke warning signs') == 1
        B[i]['md'] = lead.replace('stroke warning signs', STROKE)
        B[i + 1:i + 1] = [{'id': 'H48-BRAIN-LIST', 'kind': 'ul', 'md': lst, 'text': None},
                          {'id': 'H48-BRAIN-2', 'kind': 'p', 'md': close, 'text': None}]
        j = [b['id'] for b in B].index('B106')
        first = 'For objective stroke-like signs, I would use DMSO immediately **while someone calls medics**. '
        assert B[j]['md'].startswith(first)
        B[j]['md'] = B[j]['md'][len(first):]
    elif key == 'acute-c1':
        i = ids.index('B100')
        assert B[i]['md'].startswith('An emergency means act now.')
        assert B[i + 1]['id'] == 'B76' and B[i + 1]['md'].startswith('When the person is breathing normally')
        B[i]['md'] = body
        del B[i + 1]
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
    out = SP / 'guide-h48-dry.md' if dry else MD
    out.write_text(text, encoding='utf-8')
    if not dry:
        BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/fidelity_keys.py'), 'check', str(KEYS), str(out)],
                       capture_output=True, text=True)
    print(('dry: ' if dry else 'applied: ') + ', '.join(keys), '|', len(text.split()), 'words')
    print((r.stdout + r.stderr).strip()[-1500:])
