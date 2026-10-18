"""mkbatch.py - write a Pangram batch for the hypnosis lane: drafts, gate records, the gate's run, the items file and the
predictions table, in fix-YYYYMMDD/bNNN/ (2026-10-18).

  from mkbatch import write_batch
  write_batch(folder, 430, drafts, gate, preds, intro)   # preds: {key: (mine, chance 0..1, why)}

The predictions are written before the run, as the lane requires; write_batch refuses a key without one. The gate
(tools/humanization/pangram_gate.py) decides whether the batch may go; nothing is written to the items file if it says no.
"""
import hashlib, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]


def write_batch(folder, num, drafts, gate, preds, intro, lint_article=None):
    out = pathlib.Path(folder) / ('b%d' % num)
    out.mkdir(parents=True, exist_ok=True)
    missing = [k for k in drafts if k not in preds]
    if missing:
        raise SystemExit('no prediction for %s: predictions come before the run' % ', '.join(missing))
    for k in drafts:
        gate[k]['words'] = len(drafts[k].split())
    (out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    cmd = [sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'), str(out / 'GATE.json'),
           str(out / ('b%d.js' % num)), '--name', 'B%d' % num]
    if lint_article:
        cmd += ['--lint-article', str(lint_article)]
    r = subprocess.run(cmd + list(drafts), capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-1500:], r.stderr[-3000:])
        raise SystemExit('the gate said no')
    items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
    f = out / ('b%d-items.json' % num)
    f.write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
    rows = ['| %s | %s | %d%% | %s |  |' % (k, preds[k][0], round(preds[k][1] * 100), preds[k][2].replace('|', '/')) for k in drafts]
    (out / 'PREDICTIONS.md').write_text('# Predictions and Pangram results: batch %dg\n\n%s\n\n## Batch %dg\n\n'
                                        '| text | mine | chance | why | Pangram |\n|---|---|---|---|---|\n%s\n' % (num, intro, num, '\n'.join(rows)),
                                        encoding='utf-8')
    print('batch %dg: %d items, %d words, items sha %s' % (num, len(items), sum(len(t.split()) for t in drafts.values()),
                                                            hashlib.sha256(f.read_bytes()).hexdigest()))
    return out
