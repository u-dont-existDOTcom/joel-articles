#!/usr/bin/env python3
"""run.py - turn 72's helper (copied from h79) for the checks through the API on his laptop (his key), from this folder:

  python3 run.py texts BATCH KEY...     TEXTS-BATCH.json: each TEST-KEY.txt as Pangram should see it (no links, no bold)
  python3 run.py predict BATCH KEY...   each KEY's prediction into the ledger, from PREDICT.json (before its check)
  python3 run.py results BATCH          RESULTS-BATCH.json from laptop-BATCH.jsonl (the API tool's results.jsonl lines),
                                        then into the ledger

The laptop run: cd /home/joel/ai-work/claude-dangerous-lane && python3 joel-articles/tools/humanization/pangram_api.py
check bad-trips-t72/TEXTS-BATCH.json bad-trips-t72/out-BATCH --expect 4.1 --windows --public
"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h80-20261127/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'


def plain(md):
    t = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', md)
    t = t.replace('**', '')
    t = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'\1', t)
    return t.strip()


def texts(batch, keys):
    out = {k: plain((HERE / ('TEST-%s.txt' % k)).read_text(encoding='utf-8')) for k in keys}
    (HERE / ('TEXTS-%s.json' % batch)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for k, t in out.items():
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])


def predict(batch, keys):
    P = json.loads((HERE / 'PREDICT.json').read_text(encoding='utf-8'))
    rc = 0
    for k in keys:
        p = P[k]
        cmd = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope',
               p.get('scope', 'paragraph'), '--text', REL + 'TEST-%s.txt' % k, '--call', p['call'], '--chance', str(p['chance']), '--key', k,
               '--batch', batch, '--detector', DET, '--decides', p['decides']]
        for t in p['tells']:
            cmd += ['--tells', t]
        for t in p['human']:
            cmd += ['--human-tells', t]
        for flag, field in (('--unchanged', 'unchanged'), ('--his', 'his'), ('--humanized', 'humanized'),
                            ('--first-fix', 'first_fix'), ('--diagnosis', 'diagnosis'), ('--big-change', 'big'),
                            ('--narrowed', 'narrowed')):
            if p.get(field):
                cmd += [flag, p[field]]
        if p.get('panel'):
            cmd += ['--panel', REL + p['panel']]
        if p.get('receipt'):
            cmd += ['--receipt', REL + p['receipt']]
        r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
        print(k, '|', (r.stdout + r.stderr).strip()[-700:])
        rc = rc or r.returncode
    return rc


def results(batch):
    out = {}
    for line in (HERE / ('laptop-%s.jsonl' % batch)).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        d = json.loads(line)
        w = [dict(zip(('label', 'confidence', 'words', 'start', 'end', 'text'), x)) if isinstance(x, list) else x
             for x in (d.get('windows') or [])]
        ws = '; '.join('%s, %s, %s' % (x['label'], x.get('confidence') or '', x.get('words') or '') for x in w)
        flagged = [x.get('text', '').strip() for x in w if not (x['label'].startswith('Human') and x.get('confidence') == 'High')]
        link = d.get('public_dashboard_link') or d.get('dashboard_link') or d.get('link') or ''
        out[d['name']] = [d['headline'], d.get('fraction_ai'), d.get('words'), ws, d.get('utc') or d.get('at'),
                          '/' + link.rstrip('/').split('/')[-1] if link else '', flagged]
    p = HERE / ('RESULTS-%s.json' % batch)
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, 'tools/humanization/pangram_ledger.py', 'results', L, str(p), '--detector', DET],
                       cwd=REPO, capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()[-1500:])
    return r.returncode


if __name__ == '__main__':
    cmd, batch, keys = sys.argv[1], sys.argv[2], sys.argv[3:]
    sys.exit({'texts': lambda: texts(batch, keys), 'predict': lambda: predict(batch, keys),
              'results': lambda: results(batch)}[cmd]() or 0)
