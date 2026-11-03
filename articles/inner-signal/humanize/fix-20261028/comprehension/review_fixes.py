"""The fix writers' answers (fix/FIXES-k.json) checked and printed for my review, and fix/KEPT.json started from them.

Each fix must name a paragraph of the guide with his answers in (BASE-ANSWERS.md), its "replace" words must occur there
exactly once, and two fixes on one paragraph must not overlap. Every finding sent to a writer must come back in a fix or
in "not_fixed". A fix I change or drop is changed in fix/MY-REVIEW.json ({"F-id or fix id": {"with": ..., "drop": why}}),
which this script applies when it writes KEPT.json, so the record shows the writer's words and mine.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/review_fixes.py [PART ...] [--quiet]
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BASE = sr.blocks((HERE / 'BASE-ANSWERS.md').read_text(encoding='utf-8'))
FIX = HERE / 'fix'


def sent_findings(k):
    """The finding ids each part's brief sent, from FIX-k.txt."""
    raw = (FIX / ('FIX-%s.txt' % k)).read_text(encoding='utf-8')
    return re.findall(r'^- (F\d+[ab]?\.\d+) \(', raw, re.M)


def main():
    quiet = '--quiet' in sys.argv
    parts = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not parts:
        parts = sorted({re.match(r'FIXES-(\w+)\.json', f.name).group(1) for f in FIX.glob('FIXES-*.json')},
                       key=lambda x: (int(re.match(r'\d+', x).group(0)), x))
    mine = json.loads((FIX / 'MY-REVIEW.json').read_text(encoding='utf-8')) if (FIX / 'MY-REVIEW.json').exists() else {}
    kept, problems = [], []
    for k in parts:
        d = json.loads((FIX / ('FIXES-%s.json' % k)).read_text(encoding='utf-8'))
        sent = set(sent_findings(k))
        seen = set()
        spans = {}
        for n, fx in enumerate(d.get('fixes', []), 1):
            fid = 'X%s.%d' % (k, n)
            i = int(fx['p'])
            text = BASE[i]['text']
            seen.update(fx.get('findings', []))
            rev = mine.get(fid) or {}
            if rev.get('replace'):   # my change can take in more of the sentence than the writer's
                fx = dict(fx, writer_replace=fx['replace'], replace=rev['replace'])
            c = text.count(fx['replace'])
            ok = c == 1
            if ok:
                a = text.index(fx['replace'])
                for (b0, b1, other) in spans.get(i, []):
                    if a < b1 and b0 < a + len(fx['replace']):
                        ok = False
                        problems.append('%s overlaps %s in P%d' % (fid, other, i))
                spans.setdefault(i, []).append((a, a + len(fx['replace']), fid))
            else:
                problems.append('%s: "replace" occurs %d times in P%d: %r' % (fid, c, i, fx['replace'][:80]))
            rec = {'id': fid, 'part': k, 'block': i, 'where': sr.where(BASE, i), 'findings': fx.get('findings', []),
                   'replace': fx['replace'], 'with': rev.get('with', fx['with']), 'writer_with': fx['with'],
                   'how': fx.get('how', ''), 'note': rev.get('note', fx.get('note', '')),
                   'mine': bool(rev.get('with')), 'valid': ok}
            if fx.get('writer_replace'):
                rec['writer_replace'] = fx['writer_replace']
            if rev.get('drop'):
                rec['dropped'] = rev['drop']
            if not quiet:
                print('=' * 90)
                print('%s  P%d  %s  %s  %s%s' % (fid, i, rec['where'], ','.join(rec['findings']), rec['how'],
                                                  '' if ok else '  ** INVALID **'))
                print('  OLD:', fx['replace'])
                print('  NEW:', fx['with'])
                if rev.get('with'):
                    print('  MINE:', rev['with'])
                if rev.get('drop'):
                    print('  DROPPED:', rev['drop'])
                print('  note:', fx.get('note', ''))
            if ok and not rev.get('drop'):
                kept.append(rec)
        for x in d.get('not_fixed', []):
            seen.add(x['finding'])
            if not quiet:
                print('-- not fixed %s: %s' % (x['finding'], x.get('why', '')))
        missing = sent - seen
        if missing:
            problems.append('part %s: findings not answered: %s' % (k, ', '.join(sorted(missing))))
    (FIX / 'KEPT.json').write_text(json.dumps({'fixes': kept}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('\n%d fixes kept; problems: %d' % (len(kept), len(problems)))
    for p in problems:
        print('  !', p)


if __name__ == '__main__':
    main()
