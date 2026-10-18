"""Edit checks and paragraph checks of the refix sections (2026-10-18, batch 446g on).

A refix section (rf-a/, rf-b/: KEY.units.json is the refix text that read 100% Human in its screen, 443g or 445g) has had
its second reader and the triage of its findings (KEY.triage.json, applied by tools/triage_apply.py into KEY.fixed.json).
  - With fixes: one edit record (was: the refix screen; march_was and march: the newest march read of each fixed stretch,
    march-h on). Held when a fixed stretch has no march read yet.
  - Without fixes (the triage let every finding stand, or there were none): its paragraph checks, from the refix text.
  - An edit that read Human in an earlier batch: its paragraph checks, from the fixed text.
A paragraph whose check text was sent before isn't sent again.

Predictions: an edit's chance is 0.85 when it changes under 18% of the words (11 of 12 such edits stayed Human: 3 of 3
fixed sections in 434g to 444g, 8 of 9 triaged refixes in 449g), 0.1 above (2 of 30); a paragraph check 0.70 to 0.79 by length (the community lane's rate; 442g: 17 of 23).

  python3 make_b446.py --batch N [--only KEY,KEY] [--write]
"""
import glob, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
import install_fixed as I  # noqa: E402
import march_pairs as M  # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import triage_apply as T  # noqa: E402
from mkbatch import write_batch  # noqa: E402

rel = lambda p: str(pathlib.Path(p).resolve().relative_to(REPO))


def screens():
    """{text: (batch, name, headline, ai, link, gate record)} of every refix screen and Emulate screen with a result."""
    out = {}
    for f in sorted(HERE.glob('b4*/drafts.json')):
        b = f.parent.name
        res = f.parent / ('%s-results.json' % b)
        if not res.exists():
            continue
        r = json.loads(res.read_text(encoding='utf-8'))
        g = json.loads((f.parent / 'GATE.json').read_text(encoding='utf-8'))
        for name, text in json.loads(f.read_text(encoding='utf-8')).items():
            if name in r and ('-refix' in name or '-emu' in name):  # plan C (rf-g): a first Emulate screen with only its major fixes
                out[text] = (b, name, r[name][0], r[name][1], 'https://www.pangram.com/history' + r[name][5], g.get(name, {}))
    return out


def results_by_name():
    out = {}
    for f in sorted(HERE.glob('b4*/b4*-results.json')):
        for k, v in json.loads(f.read_text(encoding='utf-8')).items():
            out[k] = (f.parent.name, v)
    return out


def band(w):
    return 0.70 if w < 80 else (0.77 if w < 120 else 0.79)


def para_items(key, md_source, base, why_of, seen, drafts, gate, preds, tag):
    md = I.section_md(md_source)
    for i, t, x in I.para_texts(md, seen):
        kind = 'alone' if x == t else ('next' if x.startswith(t) else ('prev' if x.endswith(t) else 'run'))
        name = '%s-%s-p%d%s' % (key, tag, i + 1, '' if kind == 'alone' else '+' + kind)
        drafts[name] = x
        gate[name] = dict(base, paragraph=i + 1, check=kind)
        w = len(x.split())
        preds[name] = ('Human', band(w), 'paragraph %d of %s (%s), %d words; %s; the community lane\'s rate for this length'
                       % (i + 1, key, kind, w, why_of))


def collect(only=None):
    """(drafts, gate, preds, held) for the refix sections that are ready."""
    sc, byname = screens(), results_by_name()
    dirs = [d for d in sorted(HERE.glob('b4*')) if list(d.glob('*-results.json'))]
    seen = set(PA.results(dirs))
    installed = json.loads((HERE / 'installed.json').read_text(encoding='utf-8'))
    drafts, gate, preds, held = {}, {}, {}, []
    for uf in sorted(glob.glob(str(HERE / 'rf-*' / '*.units.json'))):
        d = json.loads(pathlib.Path(uf).read_text(encoding='utf-8'))
        key = d['key']
        if (only and key not in only) or key in installed:
            continue
        text = '\n\n'.join(p for u in d['units'] for p in u['paras'])
        s = sc.get(text)
        if not s or not s[2].startswith('Human'):
            continue  # not a refix that read Human
        tri = pathlib.Path(uf).with_name('%s.triage.json' % key)
        ver = sorted(pathlib.Path(uf).parent.glob('%s.verify.part*.out.txt' % key))
        if not ver:
            held.append((key, 'no second reading yet')); continue
        clean = all(all(l.strip().endswith(': OK') or l.startswith('REPEATS: 0') or not l.strip() for l in v.read_text(encoding='utf-8').splitlines()) for v in ver)
        if not clean and not tri.exists():
            held.append((key, 'findings not triaged yet')); continue
        b, sname, head, ai, link, sg = s
        base = {'kind': 'emulate', 'emulate': sg.get('emulate'), 'published': sg.get('published'), 'fixed': sg.get('fixed'), 'lint': 'REVIEW'}
        fx = pathlib.Path(uf).with_name('%s.fixed.json' % key)
        if not clean and tri.exists():
            tj = json.loads(tri.read_text(encoding='utf-8'))
            if tj.get('resample'):
                held.append((key, 'stretch(es) %s to resample' % tj['resample'])); continue
            if any(f.get('problems') for f in tj.get('fixes', [])) and (not fx.exists() or fx.stat().st_mtime < tri.stat().st_mtime):
                held.append((key, 'triage fixes not applied yet (tools/triage_apply.py)')); continue
        if clean or not fx.exists() or '\n\n'.join(p for u in json.loads(fx.read_text(encoding='utf-8'))['units'] for p in u['paras']) == text:
            # no fixes: the refix text goes to its paragraph checks as it is
            para_items(key, uf, dict(base, section='%s %s, %s %.2f: %s' % (b, sname, head, ai, link)),
                       'the section\'s refix read %s whole (%s %s)' % (head, b, sname), seen, drafts, gate, preds, 'r')
            continue
        fd = json.loads(fx.read_text(encoding='utf-8'))
        new_text = '\n\n'.join(p for u in fd['units'] for p in u['paras'])
        nm = key + '-rfix'
        if nm in byname:
            bb, v = byname[nm]
            if v[0].startswith('Human'):
                base2 = dict(base, fixed=(sg.get('fixed') or []) + [rel(fx)])
                para_items(key, fx, dict(base2, section='%s %s, %s %.2f' % (bb, nm, v[0], v[1])),
                           'its triaged fixes read %s whole (%s %s)' % (v[0], bb, nm), seen, drafts, gate, preds, 'f')
            else:
                held.append((key, 'its fixes read AI in %s: a refix of those windows is next' % bb))
            continue
        mw, mn, reads, need = [], [], {}, []
        src = {u['blocks'][0]: u for u in d['units']}
        for u in fd['units']:
            if u['kind'] != 'emulate' or not u.get('fixes'):
                continue
            k = '%s-B%d' % (key, u['blocks'][0])
            r = M.lookup(str(HERE), k, src[u['blocks'][0]]['paras'], u['paras'])
            if r:
                folder, w, n = r
                mw += w; mn += n; reads[k] = folder
            else:
                need.append(k)
        if need:
            held.append((key, 'march needed for %s' % ' '.join(need))); continue
        ch = T.changed(text, new_text)
        drafts[nm] = new_text
        gate[nm] = {'kind': 'edit', 'was': '%s %s, 100%% Human: %s' % (b, sname, link), 'was_kind': 'emulate', 'lint_was': sg.get('lint'),
                    'march_was': mw, 'march': mn, 'march_reads': reads, 'cold': 'OK', 'grounding': 'OK', 'stance': 0, 'missing': [],
                    'repeats': 0, 'lint': 'REVIEW', 'reviews': rel(fx), 'verify': [rel(v) for v in ver], 'adjudication': rel(tri),
                    'emulate': sg.get('emulate'), 'published': sg.get('published'), 'fixes': sum(len(u.get('fixes') or []) for u in fd['units'])}
        c = 0.85 if ch < 0.18 else 0.1
        preds[nm] = ('Human' if c >= 0.5 else 'AI', c, '%d triaged fixes, %d%% of the refix\'s words changed; under 18%%: 11 of 12 '
                     'stayed Human (449g: 8 of 9 triaged refixes; before: 3 of 3 fixed sections), above: 2 of 30' % (gate[nm]['fixes'], round(100 * ch)))
    return drafts, gate, preds, held


if __name__ == '__main__':
    num = int(sys.argv[sys.argv.index('--batch') + 1])
    only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None
    drafts, gate, preds, held = collect(only)
    print(len(drafts), 'texts:', ' '.join(drafts))
    print('held:', ' '.join('%s (%s)' % x for x in held) or '-')
    if '--write' in sys.argv and drafts:
        intro = ('Pangram\'s web app. The refix sections: edit checks of their triaged meaning fixes, and the paragraph checks of '
                 'those with no fixes or whose fixes read Human. Predictions written before the run.')
        write_batch(HERE, num, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
