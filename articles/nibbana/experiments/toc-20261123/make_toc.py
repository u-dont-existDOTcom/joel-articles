#!/usr/bin/env python3
"""A proposal's contents as a reader sees it: TOC-<NAME>-SIDEBAR.md (numbered lines, cut as the sidebar cuts them, with
each section's words from CONTENTS-NOW.json) and LINES-<NAME>.json (line number to section id).

  python3 make_toc.py PROPOSAL-<NAME>.json NAME
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from make_files import render

prop, name = sys.argv[1], sys.argv[2]
words = {e['id']: e['words'] for e in json.load(open(os.path.join(HERE, 'CONTENTS-NOW.json'), encoding='utf-8'))}
E = [{'id': e['id'], 'level': e['level'], 'heading': e['heading'], 'words': words[e['id']]}
     for e in json.load(open(os.path.join(HERE, prop), encoding='utf-8'))]
side, nums = render(E, 'Contents as the sidebar shows it', True)
open(os.path.join(HERE, 'TOC-%s-SIDEBAR.md' % name), 'w', encoding='utf-8').write(side)
json.dump(nums, open(os.path.join(HERE, 'LINES-%s.json' % name), 'w'), indent=0)
import toc_sidebar as ts
print('%s: %d headings, %d cut off in the sidebar' % (name, len(E), sum(1 for e in E if not ts.shown(e['heading'], e['level'])[0])))
