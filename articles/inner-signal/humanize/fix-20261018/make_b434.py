"""Batch 434g (2026-10-18): the test of the meaning fixes. Each section whose Emulate screen read 100% Human, with my
meaning fixes in (rev-a to rev-e, the second reader's round 2, the adjudication of its findings, the breaks put back),
as one edit record: "was" is the screen that read Human (with its link), "march_was" and "march" the newest march read
of each fixed stretch's two versions (march-a to march-d). A section goes only when every fixed stretch has a current
march read and the reviews are done; the rest are listed. Never installed from here: a section that stays Human goes on
to its paragraph checks.

  python3 make_b434.py --dry      list each section's screen, its fixes and the stretches still needing a march read
  python3 make_b434.py --write    write the batch (predictions first) for the sections that are ready
"""
import glob, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(H / 'tools'))
import march_pairs as M  # noqa: E402
from mkbatch import write_batch  # noqa: E402

SUPERSEDED = {'rev-a/HG27.fixed.json'}  # rev-e redid the closing


def screens():
    """{text: (batch, name, headline, link)} of every Emulate screen."""
    out = {}
    for f in sorted(HERE.glob('b4*/drafts.json')):
        b = f.parent.name
        res = f.parent / ('%s-results.json' % b)
        if not res.exists():
            continue
        r = json.loads(res.read_text(encoding='utf-8'))
        for name, text in json.loads(f.read_text(encoding='utf-8')).items():
            if name in r and '-emu' in name:
                out[text] = (b, name, r[name][0], 'https://www.pangram.com/history' + r[name][5])
    return out


def sections():
    sc = screens()
    out = []
    for fx in sorted(glob.glob(str(HERE / 'rev-*' / '*.fixed.json'))):
        rel = str(pathlib.Path(fx).relative_to(HERE))
        if rel in SUPERSEDED:
            continue
        d = json.loads(pathlib.Path(fx).read_text(encoding='utf-8'))
        src = json.loads(pathlib.Path(fx.replace('.fixed.json', '.units.json')).read_text(encoding='utf-8'))
        was_text = '\n\n'.join(p for u in src['units'] for p in u['paras'])
        new_text = '\n\n'.join(p for u in d['units'] for p in u['paras'])
        scr = sc.get(was_text)
        stretches, need = [], []
        for u in d['units']:
            if u['kind'] != 'emulate' or not u.get('fixes'):
                continue
            k = '%s-B%d' % (d['key'], u['blocks'][0])
            old = next(x['paras'] for x in src['units'] if x['blocks'] == u['blocks'])
            r = M.lookup(str(HERE), k, old, u['paras'])
            (stretches if r else need).append((k, r))
        out.append({'key': d['key'], 'fixed': rel, 'screen': scr, 'was_text': was_text, 'text': new_text, 'stretches': stretches,
                    'need': [k for k, _ in need], 'n_fixes': sum(len(u.get('fixes') or []) for u in d['units']),
                    'units': d['units']})
    return out


def changed_share(s):
    a, b = s['was_text'].split(), s['text'].split()
    import difflib
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    same = sum(m.size for m in sm.get_matching_blocks())
    return 1 - same / max(len(a), len(b))


if __name__ == '__main__':
    secs = sections()
    if '--dry' in sys.argv:
        for s in secs:
            sc = s['screen']
            print('%-8s %-24s fixes %3d  changed %4.1f%%  march: %d current, %d needed %s' % (
                s['key'], ('%s %s %s' % (sc[0], sc[1], sc[2])) if sc else 'NO SCREEN MATCH', s['n_fixes'], 100 * changed_share(s),
                len(s['stretches']), len(s['need']), ' '.join(x.split('-B')[1] for x in s['need'])))
        sys.exit(0)
    # Which sections go: every fixed stretch has a current march read and the section's meaning work is done
    # (meaning-status.json: {key: {"done": true, "verify": ..., "adjudication": ..., "notes": ...}}).
    status = json.loads((HERE / 'meaning-status.json').read_text(encoding='utf-8'))
    go = [s for s in secs if not s['need'] and status.get(s['key'], {}).get('done') and s['screen']]
    held = [(s['key'], 'march' if s['need'] else ('meaning' if not status.get(s['key'], {}).get('done') else 'screen')) for s in secs if s not in go]
    drafts, gate, preds = {}, {}, {}
    for s in go:
        b, name, head, link = s['screen']
        st = status[s['key']]
        mw, mn, reads = [], [], {}
        for k, (folder, w, n) in s['stretches']:
            mw += w; mn += n; reads[k] = folder
        sg = json.loads((HERE / b / 'GATE.json').read_text(encoding='utf-8'))[name]
        nm = s['key'] + '-fix'
        drafts[nm] = s['text']
        gate[nm] = {'kind': 'edit', 'was': '%s %s, 100%% Human: %s' % (b, name, link), 'was_kind': 'emulate', 'lint_was': sg.get('lint'),
                    'march_was': mw, 'march': mn, 'march_reads': reads, 'cold': 'OK', 'grounding': 'OK', 'stance': 0, 'missing': [],
                    'repeats': st.get('repeats', 0), 'lint': 'REVIEW', 'reviews': s['fixed'], 'verify': st.get('verify'),
                    'adjudication': st.get('adjudication'), 'notes': st.get('notes', ''), 'emulate': sg.get('emulate'),
                    'published': sg.get('published'), 'fixes': s['n_fixes']}
        ch = changed_share(s)
        c = max(0.2, min(0.8, 0.8 - 1.2 * ch))
        preds[nm] = ('Human' if c >= 0.5 else 'Mixed', c, '%d meaning fixes, %d%% of the words changed from the screen that read Human; '
                     'chance = 0.8 - 1.2 x the share changed' % (s['n_fixes'], round(100 * ch)))
    print('going:', ' '.join(s['key'] for s in go))
    print('held:', ' '.join('%s(%s)' % x for x in held))
    if '--write' in sys.argv and drafts:
        intro = ('Pangram\'s web app. The test of the meaning fixes: each section whose Emulate screen read 100% Human, with '
                 'my fixes of what Emulate bent or dropped (reviewed against the published text, then a second reader). '
                 'Predictions written before the run.')
        write_batch(HERE, 434, drafts, gate, preds, intro, lint_article=H / 'HUMANIZED-SO-FAR.md')
