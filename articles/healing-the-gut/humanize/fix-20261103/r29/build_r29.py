#!/usr/bin/env python3
"""r29 = r24 (the wording of Phase 4's organ cases that read High after Phase 4's first paragraph in both section checks,
#194 and #195) with the one numbered step joined to that paragraph, as r28 joined r27's wording.

r28's join worked for the paragraph's own sentences (Human, High and Medium, #204), but r27's post-panel wording of the
two cases read AI after them, where r24's wording had read High after the same sentences (#194: one 143-word High window;
#195). So the join stays and the cases go back to r24's wording; "(Brown)" goes, since the paragraph's first sentence
names Brown as the phase's only source. Writes r29.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r24' / 'r24.md').read_text(encoding='utf-8')
lead = '(those two are Phase 6, below).'
step_old = '\n\n  1. So check your organs (Brown), starting with your pancreas:'
step_new = ' So check your organs, starting with your pancreas:'
assert md.count(lead + step_old) == 1
md = md.replace(lead + step_old, lead + step_new)
CHANGES = [{'old': (lead + step_old).replace('\n', '\\n'), 'new': lead + step_new, 'kind': 'structure',
            'why': 'the step by itself read AI (#196, #199, #203); joined to the paragraph whose last sentence gives its '
                   'reason, in the wording that read High after that paragraph (#194, #195); "(Brown)" dropped since the '
                   'paragraph names Brown as the phase\'s only source'}]
(HERE / 'r29.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
