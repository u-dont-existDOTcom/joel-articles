#!/usr/bin/env python3
"""apply_h45.py - turn 36's changes to the guide from this folder: his round-35 moves carried (TEACH-ORAL's promise, "I'll
carry what you do to the sections named above, test each, and put the ones that read Human straight in").

Each key goes in only when its check read Human (RESULTS.md); --dry writes the guide with every key given to the
scratchpad and runs the fidelity check on it, without touching the guide.

  python3 apply_h45.py [--dry] KEY...      (KEY: ss-r1, acute-r1, or either's -fix2)
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = HERE.parents[3]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
KEYS = ART / 'humanize/h01/FIDELITY-KEYS-R34.json'
SP = pathlib.Path('/tmp/claude-0/-home-claude/7a3d2b92-4547-585d-83c0-bf816aa7e013/scratchpad')
sys.path.insert(0, str(HERE))
from build_tests import TESTS, TESTS2  # noqa: E402
TESTS = dict(TESTS, **TESTS2)


def paras(key):
    return TESTS[key].split('\n\n')


def apply(B, key):
    ids = [b['id'] for b in B]
    if key.startswith('ss-r1'):
        head, p1, p2 = paras(key)
        assert B[ids.index('B131')]['md'] == '### ' + head
        # B132 (the lead-in), B133 (the Hunter list) and B134 (the recognition-aid line) become his two paragraphs' shape
        B[ids.index('B132')]['md'] = p1
        B[ids.index('B134')]['md'] = p2
        del B[ids.index('B133')]
    elif key.startswith('acute-r1'):
        head, p1, p2 = paras(key)
        assert B[ids.index('B99')]['md'] == '# ' + head and ids.index('B76') == ids.index('B100') + 1
        B[ids.index('B100')]['md'] = p1
        B[ids.index('B76')]['md'] = p2
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
    out = SP / 'guide-h45-dry.md' if dry else MD
    out.write_text(text, encoding='utf-8')
    if not dry:
        BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/fidelity_keys.py'), 'check', str(KEYS), str(out)],
                       capture_output=True, text=True)
    print(('dry: ' if dry else 'applied: ') + ', '.join(keys), '|', len(text.split()), 'words')
    print((r.stdout + r.stderr).strip()[-1500:])
