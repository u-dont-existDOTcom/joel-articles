#!/usr/bin/env python3
"""apply_h46.py - turn 37's carries into the guide, each only when its check read Human (RESULTS.md); --dry writes the guide
with the keys given to the scratchpad and runs the fidelity check on it, without touching the guide.

- chest-c3: Chest Pain and Injury's B124 becomes its lead-in, a list of the serious signs (H46-CHEST-LIST) and its closing
  paragraph (H46-CHEST-2).
- brain-c3: My Brain Feels Damaged's B104 becomes its lead-in, the list of checks (H46-BRAIN-LIST) and its closing paragraph
  (H46-BRAIN-2), which says what to do when a check shows a sign; B106's first sentence, which said that two paragraphs
  on, goes from there.

  python3 apply_h46.py [--dry] KEY...
"""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = HERE.parents[3]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
KEYS = ART / 'humanize/h01/FIDELITY-KEYS-R36.json'
SP = pathlib.Path('/tmp/claude-0/-home-claude/7a3d2b92-4547-585d-83c0-bf816aa7e013/scratchpad')
sys.path.insert(0, str(HERE))
from build_tests import TESTS3  # noqa: E402
STROKE = '[stroke warning signs](https://www.stroke.org/en/about-stroke/stroke-symptoms)'


def parts(key):
    head, body = TESTS3[key].split('\n\n', 1)
    lead, rest = body.split('\n', 1)
    lst, close = rest.split('\n\n', 1)
    return lead, lst, close


def apply(B, key):
    ids = [b['id'] for b in B]
    lead, lst, close = parts(key)
    if key == 'chest-c3':
        i = ids.index('B124')
        assert B[i]['md'].startswith('Mild, familiar, non-progressive discomfort')
        B[i]['md'] = lead
        B[i + 1:i + 1] = [{'id': 'H46-CHEST-LIST', 'kind': 'ul', 'md': lst, 'text': None},
                          {'id': 'H46-CHEST-2', 'kind': 'p', 'md': close, 'text': None}]
    elif key == 'brain-c3':
        i = ids.index('B104')
        assert B[i]['md'].startswith('While using DMSO, check wakefulness')
        assert 'stroke warning signs:' in lead
        B[i]['md'] = lead.replace('stroke warning signs:', STROKE + ':')
        B[i + 1:i + 1] = [{'id': 'H46-BRAIN-LIST', 'kind': 'ul', 'md': lst, 'text': None},
                          {'id': 'H46-BRAIN-2', 'kind': 'p', 'md': close, 'text': None}]
        j = [b['id'] for b in B].index('B106')
        first = 'For objective stroke-like signs, I would use DMSO immediately **while someone calls medics**. '
        assert B[j]['md'].startswith(first)
        B[j]['md'] = B[j]['md'][len(first):]
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
    out = SP / 'guide-h46-dry.md' if dry else MD
    out.write_text(text, encoding='utf-8')
    if not dry:
        BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/fidelity_keys.py'), 'check', str(KEYS), str(out)],
                       capture_output=True, text=True)
    print(('dry: ' if dry else 'applied: ') + ', '.join(keys), '|', len(text.split()), 'words')
    print((r.stdout + r.stderr).strip()[-1500:])
