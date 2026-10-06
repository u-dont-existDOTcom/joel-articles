"""Copy of pangram-runs/community-s5/times.py on Joel's laptop (2026-10-06): the first and last result times of each batch log,
from the `utc` field the API tool writes. Result times in the predictions log come from here, never from memory.
Usage there: python3 community-s5/times.py 46 68"""
import json, sys
from pathlib import Path
HERE = Path(__file__).parent
for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    p = HERE / ('api%d.log' % n)
    if not p.exists():
        continue
    ts = [json.loads(l)['utc'] for l in open(p, encoding='utf-8') if l.strip().startswith('{')]
    print(n, len(ts), ts[0][11:16] if ts else '-', ts[-1][11:16] if ts else '-')
