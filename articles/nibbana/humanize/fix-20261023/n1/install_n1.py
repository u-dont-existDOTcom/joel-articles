"""Nibbāna batch n1's fixes that go in (2026-10-23): the working copy HUMANIZED-SO-FAR.html, Joel's editor HTML of
2026-10-22 with the edits that read Human on their own through the API and passed the reader's check (REVIEW.md), and
EDITS-n1.json, the record of each (its check's link and try, its review).

The post itself is never touched: the working copy goes into a temporary draft for the whole-article recheck, and Joel
applies the fixes to his post when he wants them.

  python3 articles/nibbana/humanize/fix-20261023/n1/install_n1.py   (from the repo root)
"""
import importlib.util, json, pathlib

N = pathlib.Path(__file__).resolve().parent
H = N.parents[1]
spec = importlib.util.spec_from_file_location('make_n1', N / 'make_n1.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
PAGE = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/'
        'fix-20261023/n1/API-CHECKS.md')
# key: (the API check that read Human, its try in its lineage, the edits). n1-science is not here: its try 1 read Human,
# but the reader found two additions a reader would take as claims (REVIEW.md, item 4), and the reader's own fix read AI
# (n1_science_t2), so try 1's words go to Joel as a question first.
GO = {
    'n1-unification': ('n1_unification', 1, M.E['n1-unification'][2]),
    'n1-percentages': ('n1_percentages_t2', 2, M.T2['n1-percentages']),
    'n1-last-test': ('n1_last_test', 1, M.E['n1-last-test'][2]),
    'n1-rebirth': ('n1_rebirth', 1, M.E['n1-rebirth'][2]),
}


def main():
    results = {}
    for f in sorted(N.glob('API-RESULTS-*.jsonl')):
        for l in f.read_text(encoding='utf-8').splitlines():
            if l.strip():
                r = json.loads(l)
                results[r['name']] = r
    src = M.SRC.read_text(encoding='utf-8')
    work, rec = src, []
    for key, (check, tr, pairs) in GO.items():
        r = results[check]
        assert r['headline'] == 'Human Written', (key, r['headline'])
        for old, new in pairs:
            assert work.count(old) == 1, key
            work = work.replace(old, new)
            rec.append({'key': key, 'windows': M.E[key][0], 'shape': M.E[key][1], 'old': old, 'new': new,
                        'check': PAGE + '#' + check, 'try': tr,
                        'result': '%s (Pangram %s, the API, %s; %d words on its own)' % (r['headline'], r['version'],
                                                                                          r['utc'], r['words']),
                        'review': 'fix-20261023/n1/REVIEW.md'})
    (H / 'HUMANIZED-SO-FAR.html').write_text(work, encoding='utf-8')
    (N / 'EDITS-n1.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('HUMANIZED-SO-FAR.html: %d edits in, from %s' % (len(rec), M.SRC.name))


if __name__ == '__main__':
    main()
