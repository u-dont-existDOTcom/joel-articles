"""Records one API round of the hypnosis guide's batch 474 (2026-10-23) and writes its page.

For each check of API-RESULTS-N.jsonl: a ledger result line, its verdict by the ledger's own rule (verdict_of: Human only
for a 100% Human result), its link the check's public Pangram page (pangram_api.py --public; Joel, 2026-10-23 02:29 UTC:
"public pangram links are ok"). Then API-CHECKS.md over every round, each AI window in bold and labelled on every line
(E230), with each check's Pangram link.

  python3 articles/inner-signal/humanize/fix-20261023/b474/record_b474.py N   (from the repo root)
"""
import json, pathlib, subprocess, sys

N = pathlib.Path(__file__).resolve().parent
H = N.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import pangram_ledger as L  # noqa: E402

TITLE = "The hypnosis guide's batch 474 API checks (Pangram 4.1): recheck A's three red stretches"
DET = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'


def rows():
    out = []
    for f in sorted(N.glob('API-RESULTS-*.jsonl')):
        out += [json.loads(l) for l in f.read_text(encoding='utf-8').splitlines() if l.strip()]
    return out


def record(rnd):
    for line in (N / ('API-RESULTS-%s.jsonl' % rnd)).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        verdict = L.verdict_of(r['headline'], fraction_ai=r['fraction_ai'])
        shading = '; '.join('%s %s (%dw)' % ('AI' if w[0].startswith('AI') else 'Human', w[1], w[2]) for w in r['windows'])
        argv = [sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'result',
                str(H / 'pangram-ledger.jsonl'), '--key', r['name'], '--verdict', verdict, '--link', r['dashboard_link'],
                '--headline', r['headline'], '--ai-fraction', '%.4f' % r['fraction_ai'], '--words', str(r['words']),
                '--shading', shading, '--detector', DET, '--at', r['utc']]
        p = subprocess.run(argv, capture_output=True, text=True, cwd=REPO)
        print(r['name'], verdict, (p.stdout + p.stderr).strip()[-160:])
        if p.returncode:
            sys.exit(1)


def page():
    out = ['# ' + TITLE, '',
           'Each check went through Joel\'s API key (`tools/humanization/pangram_api.py --public`, run on his laptop); its '
           'Pangram page is linked under its heading. AI windows (AI-Generated or AI-Assisted) are in **bold**, labelled on '
           'every line; everything else read Human. The predictions are in `../../pangram-ledger.jsonl` (lineage '
           'HG17-drive-seam, HG18-B311, HG24-trouble); the Emulate samples are in `bl/`, `bm/` and `bn/`, the splices in `CANDIDATES.json`.', '']
    for r in rows():
        out += ['## %s' % r['name'], '', '**%s** (%s), %.0f%% AI, %d words, Pangram %s, %s. [Its Pangram page](%s).' % (
            r['headline'], r['prediction_short'], 100 * r['fraction_ai'], r['words'], r['version'], r['utc'],
            r['dashboard_link']), '']
        for label, conf, words, a, b, text in r['windows']:
            if label.startswith('AI'):
                kind = 'AI-assisted' if 'Assist' in label else 'AI'
                lines = [x.strip() for x in text.split('\n') if x.strip()]
                out += ['**[%s, %s%s] %s**' % (kind, conf, '' if i == 0 else ', same window', x) for i, x in enumerate(lines)]
            else:
                out += ['[Human, %s, %d words] %s' % (conf, words, x.strip()) for x in text.split('\n') if x.strip()]
            out.append('')
    (N / 'API-CHECKS.md').write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')


if __name__ == '__main__':
    record(sys.argv[1])
    page()
