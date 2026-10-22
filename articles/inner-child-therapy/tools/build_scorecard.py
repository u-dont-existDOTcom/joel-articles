#!/usr/bin/env python3
"""Build this lane's Pangram scorecard and the universal one (turn 94, 2026-10-22).

Joel, 2026-10-22 19:50 UTC: "where is the scorecard isn't that something you are keeping track of so we can help you get
better at your predictions etc?" tools/humanization/pangram_lanes.json gives this lane "page": false, because its article is
under a parallel-write lock and only its own writer may add files here. The writer never built the page, and the universal
page hadn't been rebuilt since 2026-10-21. So the writer runs this after every recorded result:
  python3 articles/inner-child-therapy/tools/build_scorecard.py
It writes articles/inner-child-therapy/tools/SCORECARD.md and state/PANGRAM-SCORECARD.md, and leaves every other lane's page
alone. Their pages are their writers' to build. It does that by building from a copy of the lanes file in which only this
lane has a page.
"""
import json
import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[3]
LANES = REPO / 'tools/humanization/pangram_lanes.json'
cfg = json.loads(LANES.read_text(encoding='utf-8'))
for lane in cfg['lanes']:
    lane['page'] = 'articles/inner-child-therapy/tools/SCORECARD.md' if lane['lane'] == 'inner child guide' else False
with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
    json.dump(cfg, f)
sys.exit(subprocess.run([sys.executable, str(REPO / 'tools/humanization/pangram_ledger.py'), 'build', '--lanes', f.name,
                         '--universal', str(REPO / 'state/PANGRAM-SCORECARD.md')], cwd=REPO).returncode)
