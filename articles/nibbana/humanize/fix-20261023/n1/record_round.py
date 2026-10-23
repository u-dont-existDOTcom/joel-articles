"""Records one API round of Nibbāna batch n1 in the ledger (2026-10-23): a result line for each check of
API-RESULTS-N.jsonl, its verdict by the ledger's own rule (verdict_of: Human only for a 100% Human result), its link the
check's heading on API-CHECKS.md.

  python3 articles/nibbana/humanize/fix-20261023/n1/record_round.py N   (from the repo root)
"""
import json, pathlib, subprocess, sys

N = pathlib.Path(__file__).resolve().parent
H = N.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import pangram_ledger as L  # noqa: E402

PAGE = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/'
        'fix-20261023/n1/API-CHECKS.md')
DET = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'


def main():
    rnd = sys.argv[1]
    for line in (N / ('API-RESULTS-%s.jsonl' % rnd)).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        verdict = L.verdict_of(r['headline'], fraction_ai=r['fraction_ai'])
        shading = '; '.join('%s %s (%dw)' % ('AI' if w[0].startswith('AI') else 'Human', w[1], w[2]) for w in r['windows'])
        argv = [sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'result',
                str(H / 'pangram-ledger.jsonl'), '--key', r['name'], '--verdict', verdict, '--link', PAGE + '#' + r['name'],
                '--headline', r['headline'], '--ai-fraction', '%.4f' % r['fraction_ai'], '--words', str(r['words']),
                '--shading', shading, '--detector', DET, '--at', r['utc']]
        p = subprocess.run(argv, capture_output=True, text=True, cwd=REPO)
        print(r['name'], verdict, (p.stdout + p.stderr).strip()[-160:])
        if p.returncode:
            sys.exit(1)


if __name__ == '__main__':
    main()
