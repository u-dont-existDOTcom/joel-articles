#!/usr/bin/env python3
"""Turn 104: record an API results file in the ledger, one result per check, with the ledger's own verdict rule.

  python3 record.py API-RESULTS-N.jsonl

Each line's verdict comes from pangram_ledger.verdict_of (its headline, its windows and its AI fraction), its link is
the check's public page, and its time is the check's own. Prints the key, verdict, AI fraction and windows only."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from pangram_ledger import verdict_of  # noqa: E402


def main(path):
    for line in open(path, encoding='utf-8'):
        r = json.loads(line)
        labels = [', '.join(str(x) for x in w[:2]) for w in r.get('windows', [])]
        v = verdict_of(r['headline'], labels, r['fraction_ai'])
        cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'result', str(LEDGER),
               '--key', r['name'], '--verdict', v, '--link', r['dashboard_link'], '--headline', r['headline'],
               '--ai-fraction', '%.6f' % r['fraction_ai'], '--words', str(r['words']), '--detector', 'pangram-4.1-api',
               '--at', r['utc']]
        out = subprocess.run(cmd, capture_output=True, text=True)
        if out.returncode:
            sys.exit('%s: %s%s' % (r['name'], out.stdout[-600:], out.stderr[-600:]))
        ai_windows = [w for w in r.get('windows', []) if str(w[0]).lower().startswith('ai')]
        print('%-28s %-6s %.4f%% AI, %d windows (%d AI) | %s' % (r['name'], v, 100 * r['fraction_ai'],
                                                                   len(r.get('windows', [])), len(ai_windows),
                                                                   out.stdout.strip().split('\n')[-1][:120]))


if __name__ == '__main__':
    main(sys.argv[1])
