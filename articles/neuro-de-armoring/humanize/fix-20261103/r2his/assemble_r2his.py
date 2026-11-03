"""Round 2 of the neuro de-armoring rewrite, the way his three versions are built (../examples/WHAT-HIS-VERSIONS-DO.md,
gate E335), after his answers of 2026-11-03 17:48 UTC.

Each paragraph is rewritten from his post (the article as it stands, HUMANIZED-SO-FAR.md, which is his post with his three
versions in), never from round 1, whose versions read AI. blocks/NNN.md is paragraph NNN's new Markdown (the block's
index in the article; BLOCKS-WERE.json holds the hash each one replaced, so a change to the article underneath stops the
build). This script puts them in (CANDIDATE.md), runs fidelity_keys.py on the whole and tells_lint.py on each rewritten
paragraph (with his post's paragraph as the source), and writes the stretches the API checks (STRETCHES below; at most six
paragraphs of eight words or more, headings counted, and 1,200 words; E325, E334) as TEXTS.json, the text as the post
reads it. His three versions and his paragraphs that read Human (High) in the baseline stay out of the stretches.

  python3 articles/neuro-de-armoring/humanize/fix-20261103/r2his/assemble_r2his.py [--only V1 V2 ...]
Exits 1 when the fidelity check fails.
"""
import argparse
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

ARTICLE_SHA = '6db92b7aff987195049b8af1f99883ec4a3f2e05e62af6a978679871c7957944'
# The stretches, by block index: a heading goes with what it heads.
STRETCHES = {
    'V1': ('the agmatine and 5-HTP warnings around his X-15', [14, 16, 17, 18]),
    'V2': ('the uridine section around his X-84', [80, 81, 82, 83, 85, 86]),
    'V3': ('Psychology is the Software, the Role-Self part around his X-26', [22, 23, 24, 25, 27, 28]),
}
MAX_P, MAX_W = 6, 1200


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*')
    a = ap.parse_args()
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == ARTICLE_SHA, 'the article changed'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    was = json.loads((HERE / 'BLOCKS-WERE.json').read_text(encoding='utf-8'))
    new = {}
    for f in sorted((HERE / 'blocks').glob('*.md')):
        i = int(f.stem)
        assert hashlib.sha256(raw[i].encode('utf-8')).hexdigest() == was[f.stem]['was_sha256'], f.name
        new[i] = f.read_text(encoding='utf-8').strip()
    cand_raw = [new.get(i, r) for i, r in enumerate(raw)]
    cand = '\n\n'.join(cand_raw) + '\n'
    (HERE / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'fidelity_keys.py'), 'check',
                         str(H / 'FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE.md')], capture_output=True, text=True)
    print(fk.stdout.strip()[-3000:])
    bl, old = sr.blocks(cand), sr.blocks(md)
    assert len(bl) == len(old)
    # the linter on each rewritten paragraph, his post's paragraph as its source
    env = dict(os.environ, TELLS_LINT_PARSE=os.environ.get('TELLS_LINT_PARSE', '0'))
    lint = []
    with tempfile.TemporaryDirectory() as d:
        for i in sorted(new):
            p, s = pathlib.Path(d) / 'p.txt', pathlib.Path(d) / 's.txt'
            p.write_text(bl[i]['text'] + '\n', encoding='utf-8')
            s.write_text(old[i]['text'] + '\n', encoding='utf-8')
            r = subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'tells_lint.py'), str(p), '--source', str(s)],
                               capture_output=True, text=True, env=env)
            flags = [l for l in r.stdout.split('\n') if l.startswith('-- ') or l.startswith('  HARD: ')]
            verdict = ([l for l in r.stdout.split('\n') if l.startswith('verdict:')] or ['verdict: ?'])[0]
            lint.append({'block': i, 'verdict': verdict, 'flags': flags})
            print('B%03d %s' % (i, verdict), *('\n    ' + f for f in flags))
    (HERE / 'LINT.json').write_text(json.dumps(lint, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    rows, texts = [], {}
    for key, (name, idx) in STRETCHES.items():
        bs = [bl[i] for i in idx]
        # the text as the post reads it: an emphasis inside a link's text keeps its asterisks in sr.blocks (E326)
        t = re.sub(r'\*([^*\n]+)\*', r'\1', '\n\n'.join(b['text'] for b in bs))
        paras = sum(1 for b in bs if len(b['text'].split()) >= 8)
        words = len(t.split())
        assert paras <= MAX_P and words <= MAX_W, (key, paras, words)
        rows.append({'key': 'r2-' + key, 'name': name, 'blocks': idx, 'paragraphs': paras, 'words': words,
                     'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest()})
        if not a.only or key in a.only:
            texts['r2-' + key] = t
    (HERE / 'STRETCHES.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('candidate', hashlib.sha256(cand.encode('utf-8')).hexdigest()[:12])
    for r in rows:
        print(' ', r['key'], r['paragraphs'], 'paragraphs', r['words'], 'words |', r['name'])
    return fk.returncode


if __name__ == '__main__':
    sys.exit(main())
