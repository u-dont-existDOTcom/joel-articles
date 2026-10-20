"""Paragraph checks (2026-10-18, batch 442g on): every paragraph of each fixed section that read 100% Human whole (the edit
records "<key>-fix" of 434g and later), alone or with a neighbor, before the section is installed (Joel's rule of
2026-10-01: "every paragraph passes alone"). The texts come from tools/install_fixed.py: section_md() is the Markdown
that will be installed, para_texts() the fewest texts paragraphs_alone.py will look for. A paragraph whose check text was
sent before (any batch, any result) isn't sent again.

Each text goes as an Emulate screen ("kind": "emulate", its blocks from the section's Emulate runs, the published text
and its fixed.json): it is a piece of a text that passed the edit gate (march, linter, meaning reviews) whole.

Predictions: the community lane's paragraph-sized texts read Human 70% at 50-79 words, 77% at 80-119, 79% at 120-160
(articles/intentional-communities/candidate, every b*/ batch with results, 455 texts of one or two blocks, 2026-10-18);
+5 points when the section read under 0.10 AI likelihood whole, -5 when 0.15 or more.

  python3 make_b442.py [--batch N] [--only KEY,KEY] [--write]
"""
import glob, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(H / 'tools'))
import install_fixed as I  # noqa: E402
import paragraphs_alone as PA  # noqa: E402
from mkbatch import write_batch  # noqa: E402


def passed_fixes():
    """[(batch, key, gate record, result)] of the fixed sections that read Human whole."""
    out = []
    for g in sorted(HERE.glob('b4*/GATE.json')):
        res = g.parent / ('%s-results.json' % g.parent.name)
        if not res.exists():
            continue
        r = json.loads(res.read_text(encoding='utf-8'))
        for k, v in json.loads(g.read_text(encoding='utf-8')).items():
            if v.get('kind') == 'edit' and k.endswith('-fix') and k in r and r[k][0].startswith('Human'):
                out.append((g.parent.name, k[:-4], v, r[k]))
    return out


def band(words):
    return 0.70 if words < 80 else (0.77 if words < 120 else 0.79)


if __name__ == '__main__':
    num = int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 442
    only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None
    dirs = [d for d in sorted(glob.glob(str(HERE / 'b4*'))) if glob.glob(d + '/*-results.json')]
    seen = set(PA.results(dirs))
    drafts, gate, preds = {}, {}, {}
    for b, key, g, r in passed_fixes():
        if only and key not in only:
            continue
        fixed = 'articles/inner-signal/humanize/fix-20261018/' + g['reviews']
        md = I.section_md(HERE / g['reviews'])
        adj = 0.05 if r[1] < 0.10 else (-0.05 if r[1] >= 0.15 else 0)
        for i, t, x in I.para_texts(md, seen):
            kind = 'alone' if x == t else ('next' if x.startswith(t) else ('prev' if x.endswith(t) else 'run'))
            name = '%s-p%d%s' % (key, i + 1, '' if kind == 'alone' else '+' + kind)
            drafts[name] = x
            gate[name] = {'kind': 'emulate', 'emulate': g.get('emulate'), 'published': g.get('published'), 'fixed': [fixed],
                          'lint': 'REVIEW', 'paragraph': i + 1, 'check': kind,
                          'section': '%s %s-fix, %s, AI likelihood %.2f: https://www.pangram.com/history%s' % (b, key, r[0], r[1], r[5])}
            w = len(x.split())
            c = round(min(0.95, max(0.05, band(w) + adj)), 2)
            preds[name] = ('Human' if c >= 0.5 else 'Mixed', c, 'paragraph %d of %s (%s), %d words; the section read %s at %.2f whole (%s); '
                           'chance = the community lane\'s rate for paragraph-sized texts of this length%s'
                           % (i + 1, key, kind, w, r[0], r[1], b, '' if not adj else (', %+d points' % round(adj * 100))))
    print(len(drafts), 'texts:', ' '.join(drafts))
    if '--write' in sys.argv and drafts:
        intro = ('Pangram\'s web app. The paragraph checks of the fixed sections that read 100% Human whole: each paragraph alone '
                 '(50 words or more) or with a neighbor under its heading, the texts paragraphs_alone.py looks for. '
                 'Predictions written before the run.')
        write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
