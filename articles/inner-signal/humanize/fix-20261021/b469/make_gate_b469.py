"""Batch 469g's gate records (2026-10-21), then the in-page batch through the gate.

The texts are ./drafts.json (make_b469.py). Each record cites its reviews: the march read of the installed paragraph and
the edit (march-labels.txt, decoded here into march.json by march-map.json), the cold read (SENSE-HG32.md and
SENSE-HG18.md for the two rewrites; CONFLATION-REVIEW.md for the sweep's five fixes, which read each fixed paragraph in its
context), the meaning check (VERIFY.md for the rewrites; CONFLATION-REVIEW.md's CHANGED for the fixes) and the stance check
(STANCE.md). A reviewer's finding that is answered rather than fixed is answered in gate-answers.json, which fills or
overrides these records. Round 1's reviews are in r1/.

No text goes to pangram.com from here (gate E200: many paragraphs are read in the real article through free Substack posts,
here the whole-guide recheck); GATE.json records that each edit cleared the meaning reviews before it went into the
working copy, and the gate's verdict on each (b469.js is written by pangram_gate.py but not run). Appendix C's prose has no
break in its march read, which the gate holds for a paid call; it is read in the recheck, where its forecast names that
risk (batch/PREDICTIONS.md).

  python3 articles/inner-signal/humanize/fix-20261021/b469/make_gate_b469.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
OUT = B / 'batch'
FEED_A = 'https://www.pangram.com/feed/fd91cf34-925f-48ca-8100-5fee8d5766c4'
FEED_B = 'https://www.pangram.com/feed/6a48b3ce-6631-4c99-aec3-b127409dc2f8'
HIST = 'https://www.pangram.com/history/'
APPC_KEYS = ['HG32-prose-p%d' % n for n in range(1, 8)]   # round 2 on: seven paragraphs
CF_KEYS = ['HG14-cf-addressee', 'HG20-cf-roles', 'HG24-cf-grownup', 'HG36-cf-protector', 'HG37-cf-nurturer', 'HG24-cf-anxious']
KEYS = ['HG18-count-feet', 'HG18-stopped-press'] + APPC_KEYS + CF_KEYS


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def march_reads():
    """march.json from the reader's labels: {edit key: {'was': [labels per paragraph], 'new': [...]}}."""
    labels = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (B / 'march-labels.txt').read_text(encoding='utf-8'), re.M))
    out = {}
    for m in json.loads((B / 'march-map.json').read_text(encoding='utf-8')):
        seq = ' '.join(labels[str(m['start'] + j + 1)] for j in range(m['n']))
        out.setdefault(m['key'], {}).setdefault(m['ver'], []).append(seq)
    (B / 'march.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    return out


def lint(text, article=None):
    f = OUT / 'texts' / '_lint.txt'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), str(f)]
                       + (['--installed', str(article)] if article else []), capture_output=True, text=True, cwd=REPO)
    return next((l.split(':', 1)[1].strip() for l in r.stdout.split('\n') if l.startswith('verdict:')), None)


def main():
    OUT.mkdir(exist_ok=True)
    drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    texts = meta['texts']
    edits = {e['key']: e for e in meta['edits']}
    mr = march_reads()
    hsf = REPO / 'articles' / 'inner-signal' / 'humanize' / 'HUMANIZED-SO-FAR.md'
    rec = {}
    hg18 = '466g HG18-smp1 (Pangram 4.0), 100%% Human whole and in every paragraph: %sf456f1ca-b66b-4830-8f96-45d8d8e64bac' % HIST
    for k in ('HG18-count-feet', 'HG18-stopped-press'):
        rec[k] = {'kind': 'edit', 'was': hg18 + '; not read in 4.1 yet (installed after the first whole-guide check)',
                  'was_kind': 'emulate', 'lint_was': lint(edits[k]['old']), 'march_was': mr[k]['was'], 'march': mr[k]['new'],
                  'cold_read': rel(B / 'SENSE-HG18.md'), 'grounding_note': rel(B / 'VERIFY.md'), 'stance_note': rel(B / 'STANCE.md')}
    # Appendix C's general part: a draft (my prose for the published list, question 2, c). Each text's march is the labels
    # of the paragraphs Pangram reads in it.
    new_paras = [p for p in edits['HG32-prose']['new'].split('\n\n') if p.strip()]
    labels = mr['HG32-prose']['new']
    for n, k in enumerate(APPC_KEYS, 1):
        inside = [i for i, p in enumerate(new_paras) if p.strip() in drafts[k]]
        rec[k] = {'kind': 'draft', 'march': [labels[i] for i in inside], 'cold_read': rel(B / 'SENSE-HG32.md'),
                  'grounding_note': rel(B / 'VERIFY.md'), 'stance_note': rel(B / 'STANCE.md'),
                  'was': 'Appendix C as published: AI 1.00 alone (Pangram 4.0, %s61b917ae-8792-410b-b7a7-853f7bd4a121); AI, '
                         'high, in the whole guide (4.1, window 6 of part B, %s)' % (HIST, FEED_B)}
    cf_was = {'HG14-cf-addressee': '456g HG14-smp2 (Pangram 4.0); Human, high, in the whole guide (4.1, window 36 of part A, %s)' % FEED_A,
              'HG20-cf-roles': '452g HG20-rfix2 (Pangram 4.0); Human, high, in the whole guide (4.1, window 66 of part A, %s)' % FEED_A,
              'HG24-cf-grownup': '460g HG24-fix (Pangram 4.0); Human, high, in the whole guide (4.1, window 71 of part A, %s)' % FEED_A,
              'HG36-cf-protector': '462g HG36-fix (Pangram 4.0); Human, high, in the whole guide (4.1, window 30 of part B, %s)' % FEED_B,
              'HG37-cf-nurturer': '455g HG37-smp (Pangram 4.0); Human, high, in the whole guide (4.1, window 30 of part B, %s)' % FEED_B,
              'HG24-cf-anxious': '460g HG24-fix (Pangram 4.0); Human, high, in the whole guide (4.1, window 71 of part A, %s)' % FEED_A}
    for k in CF_KEYS:
        rec[k] = {'kind': 'edit', 'was': cf_was[k], 'was_kind': 'emulate', 'lint_was': lint(edits[k]['old']),
                  'march_was': mr[k]['was'], 'march': mr[k]['new'], 'cold_read': rel(B / 'CONFLATION-REVIEW.md'),
                  'grounding_note': rel(B / 'CONFLATION-REVIEW.md'), 'stance_note': rel(B / 'STANCE.md')}
    for k, r in rec.items():
        r.setdefault('cold', None)
        r.setdefault('grounding', None)
        r.setdefault('stance', None)
        r.update({'missing': [], 'words': texts[k]['words'], 'march_reads': rel(B / 'march.json')})
    over = B / 'gate-answers.json'
    if over.exists():
        for k, v in json.loads(over.read_text(encoding='utf-8')).items():
            rec[k].update(v)
    (OUT / 'drafts.json').write_text(json.dumps({k: drafts[k] for k in KEYS}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
    (OUT / 'GATE.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(OUT / 'drafts.json'),
                        str(OUT / 'GATE.json'), str(OUT / 'b469.js'), '--name', 'B469log', '--lint-article', str(hsf)] + KEYS,
                       capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-3000:], r.stderr[-2000:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
