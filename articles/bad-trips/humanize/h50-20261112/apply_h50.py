#!/usr/bin/env python3
"""apply_h50.py - turn 40's carries into the guide, each only when its check read Human (RESULTS.md); --dry writes the guide
with the keys given to the scratchpad and runs the fidelity check on it, without touching the guide.

- rescue-c10: Active Seizure's rescue medicine paragraph (B110), its link kept on "doctors reach for first when a seizure
  won't stop".
- brainev-c2: My Brain Feels Damaged's evidence paragraph (B105), its four links kept on the studies.

  python3 apply_h50.py [--dry] KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = HERE.parents[3]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
KEYS = ART / 'humanize/h01/FIDELITY-KEYS-R39.json'
SP = pathlib.Path('/tmp/claude-0/-home-claude/7a3d2b92-4547-585d-83c0-bf816aa7e013/scratchpad')
sys.path.insert(0, str(HERE))
from build_tests import RESCUE10 as RESCUE, EVID2 as EVID  # noqa: E402
LINKS_B105 = [('A preliminary trial in people', 'A preliminary trial', 'https://pubmed.ncbi.nlm.nih.gov/11783757/'),
              ('in a small series of patients', 'small series of patients', 'https://pubmed.ncbi.nlm.nih.gov/6462399/'),
              ('In animal stroke research', 'animal stroke research', 'https://pubmed.ncbi.nlm.nih.gov/15744247/'),
              ('NMDA- and AMPA-mediated excitotoxicity', 'NMDA- and AMPA-mediated excitotoxicity', 'https://pubmed.ncbi.nlm.nih.gov/11421595/')]


def linked(text, pairs):
    for ctx, words, url in pairs:
        assert text.count(ctx) == 1, ctx
        text = text.replace(ctx, ctx.replace(words, '[%s](%s)' % (words, url)))
    return text


def apply(B, key):
    ids = [b['id'] for b in B]
    if key == 'rescue-c10':
        i = ids.index('B110')
        assert B[i]['md'].startswith('If an appropriate rapid seizure-rescue benzodiazepine is available')
        B[i]['md'] = linked(RESCUE, [("the kind of drug doctors reach for first when a seizure won't stop", "doctors reach for first when a seizure won't stop",
                                      'https://pmc.ncbi.nlm.nih.gov/articles/PMC9477921/')])
    elif key == 'brainev-c2':
        i = ids.index('B105')
        assert B[i]['md'].startswith('I believe DMSO works better for stroke')
        B[i]['md'] = linked(EVID, LINKS_B105)
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
    out = SP / 'guide-h50-dry.md' if dry else MD
    out.write_text(text, encoding='utf-8')
    if not dry:
        BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/fidelity_keys.py'), 'check', str(KEYS), str(out)],
                       capture_output=True, text=True)
    print(('dry: ' if dry else 'applied: ') + ', '.join(keys), '|', len(text.split()), 'words')
    print((r.stdout + r.stderr).strip()[-1500:])
