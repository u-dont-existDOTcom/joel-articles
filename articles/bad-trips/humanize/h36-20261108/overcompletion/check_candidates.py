#!/usr/bin/env python3
"""check_candidates.py - each overcompletion reader's candidate (PART-N.json beside this script) checked against the guide.

For every candidate: is its cut text in its block, exactly once; and with the cut made (or the block replaced by its
"join" text), does the guide still pass the fidelity keys (R25), the keep-as-is ledger and the owner edits? Writes
CHECKED.json and prints one line a candidate. A candidate that passes is still only a candidate: each is read by hand
before anything goes in (RESULTS.md says what each came to).

  python3 check_candidates.py
"""
import json
import pathlib
import shutil
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
REPO = ART.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
KEYS = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R25.json'


def checks(md_text):
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        f = d / 'GUIDE-SO-FAR.md'
        f.write_text(md_text, encoding='utf-8')
        shutil.copy(ART / 'KEEP-AS-IS.json', d / 'KEEP-AS-IS.json')
        out = {}
        r = subprocess.run(['python3', 'tools/humanization/fidelity_keys.py', 'check', str(KEYS), str(f)], cwd=REPO,
                           capture_output=True, text=True)
        lines = (r.stdout + r.stderr).splitlines()
        out['fidelity'] = 'PASS' if any(l.strip() == 'verdict: PASS' for l in lines) else \
            '; '.join(l for l in lines if 'lost' in l)[:300] or 'FAIL'
        r = subprocess.run(['python3', 'tools/humanization/keep_as_is.py', 'check', str(f)], cwd=REPO,
                           capture_output=True, text=True)
        last = ((r.stdout + r.stderr).strip().splitlines() or [''])[-1]
        out['keep_as_is'] = 'ok' if ' 0 gone' in last and '0 ledger problems' in last else last
        r = subprocess.run(['python3', 'tools/humanization/check_owner_edits.py', '--article', str(f), '--ledger',
                            str(ART / 'OWNER-EDITS.json')], cwd=REPO, capture_output=True, text=True)
        fails = [l for l in (r.stdout + r.stderr).splitlines() if l.startswith('FAIL')]
        out['owner_edits'] = 'ok' if not fails else '; '.join(fails)[:300]
        return out


def main():
    blocks = json.loads(BJ.read_text(encoding='utf-8'))
    by_id = {b['id']: b for b in blocks}
    results = []
    for p in sorted(HERE.glob('PART-*.json')):
        data = json.loads(p.read_text(encoding='utf-8'))
        for c in data.get('candidates', []):
            bid = str(c.get('block', '')).strip()
            bid = bid if bid.startswith('B') else 'B' + bid
            b = by_id.get(bid)
            row = {'part': data.get('part'), 'block': bid, 'cut': c.get('cut', ''), 'kind': c.get('kind'),
                   'strength': c.get('strength'), 'loses': c.get('loses'), 'already_said': c.get('already_said'),
                   'join': c.get('join', '')}
            if not b:
                row['found'] = 'no such block'
            elif b['md'].count(c.get('cut', '')) != 1 or not c.get('cut'):
                row['found'] = 'cut text found %d times' % b['md'].count(c.get('cut', '') or '\0')
            else:
                row['found'] = 'ok'
                new_md = c['join'] if (c.get('join') or '').strip() else b['md'].replace(c['cut'], '').strip()
                new_md = new_md.replace('  ', ' ')
                trial = [dict(x) for x in blocks]
                for x in trial:
                    if x['id'] == bid:
                        x['md'] = new_md
                trial = [x for x in trial if x['md'].strip()]
                row.update(checks('\n\n'.join(x['md'] for x in trial) + '\n'))
            results.append(row)
            print('%-6s %-9s %-11s %-4s %s | %s' % (bid, row.get('strength'), row.get('kind'), row['found'][:4],
                  ' '.join('%s=%s' % (k, row.get(k, '-')[:40]) for k in ('fidelity', 'keep_as_is', 'owner_edits')),
                  row['cut'][:70].replace('\n', ' ')))
    (HERE / 'CHECKED.json').write_text(json.dumps(results, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(results), 'candidates')


if __name__ == '__main__':
    main()
