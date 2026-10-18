"""refix_runs.py - Emulate runs whose input is my meaning-fixed text of a stretch, not the published text (2026-10-18).

When a section whose Emulate screen read 100% Human reads AI again after my meaning fixes (the fixes are my words, and
often the published words, which read AI in 429g), the fixed stretch can go back to Emulate: its input already says what
the published text says, so Emulate's new version needs fewer fixes, and it is Emulate's voice again. Each run is one
fixed stretch, without headings, so its output is one segment for the stretch's published blocks (emu_runs.py back).

  python3 tools/refix_runs.py make OUTDIR FIXED.json:BLOCK [FIXED.json:BLOCK ...]   -> OUTDIR/<run>.txt, runs.json, BUNDLE.json

BLOCK is the stretch's first published block (the review's "block"). The runs go to Emulate like any other
(run_emulate.py on the laptop), then `python3 tools/emu_runs.py back OUTDIR`, and the section is screened with OUTDIR last
in its list of folders. Its new text needs a meaning check again (a second reader is enough when Emulate kept the points).
"""
import argparse, hashlib, json, pathlib, sys


def make(outdir, specs):
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    manifest, bundle = [], {}
    for spec in specs:
        path, block = spec.rsplit(':', 1)
        d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
        u = next(x for x in d['units'] if x['kind'] == 'emulate' and x['blocks'][0] == int(block))
        text = '\n\n'.join(u['paras'])
        name = '%s-fx-B%d' % (d['key'].replace('+', '_'), u['blocks'][0])
        (out / (name + '.txt')).write_text(text, encoding='utf-8')
        bundle[name] = text
        manifest.append({'run': name, 'key': d['key'], 'sent': u['blocks'], 'flagged': u['blocks'], 'headings': [],
                         'words': len(text.split()), 'input': 'meaning-fixed text', 'from': '%s B%d' % (path, u['blocks'][0])})
    (out / 'runs.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')
    s = json.dumps(bundle, ensure_ascii=False)
    (out / 'BUNDLE.json').write_text(s, encoding='utf-8')
    print(len(manifest), 'runs,', sum(m['words'] for m in manifest), 'words; BUNDLE.json sha256', hashlib.sha256(s.encode('utf-8')).hexdigest())
    return manifest


def flagged_stretches(fixed_path, draft_blocks):
    """The units of a fixed section (FIXED.json) that a check's flagged draft blocks fall in (flagged.py counts the
    checked text's blank-line blocks): [(first published block, kind)], in order."""
    import re
    d = json.loads(pathlib.Path(fixed_path).read_text(encoding='utf-8'))
    fl, i, out = set(draft_blocks), 0, []
    for u in d['units']:
        hit = False
        for p in u['paras']:
            for _ in [x for x in re.split(r'\n\s*\n', p) if x.strip()]:
                hit = hit or i in fl
                i += 1
        if hit:
            out.append((u['blocks'][0], u['kind']))
    return out


def window_runs(outdir, cases, keep=None, min_words=40):
    """Runs of a fixed section's units inside a check's AI windows (cases: [(fixed.json, flagged draft blocks)]): each
    stretch of consecutive flagged units becomes one run, its fixed paragraphs (my meaning-fixed text) and any flagged
    published paragraph as they are, the headings inside and just before it as lines, so emu_runs.py back maps it like
    any run. Joel's own lines (assemble.KEEP) are never sent. A run under MIN_WORDS takes the next unit, then the one
    before. Writes OUTDIR/<run>.txt, runs.json and BUNDLE.json."""
    import re
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import assemble as A
    keep = A.KEEP if keep is None else keep
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    manifest, bundle = [], {}
    for path, draft_blocks in cases:
        d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
        key, us = d['key'], d['units']
        hit = {b for b, _ in flagged_stretches(path, draft_blocks)}
        k_keep = keep.get(key, set())
        flagged = [i for i, u in enumerate(us) if u['blocks'][0] in hit and not u.get('heading') and not set(u['blocks']) & k_keep]
        groups, cur = [], []
        for i in flagged:
            if cur and any(not us[j].get('heading') for j in range(cur[-1] + 1, i)):
                groups.append(cur); cur = []
            cur.append(i)
        if cur:
            groups.append(cur)
        words = lambda ix: sum(len(' '.join(us[j]['paras']).split()) for j in ix if not us[j].get('heading'))
        n = 0
        for g in groups:
            ix = list(range(g[0], g[-1] + 1))
            while words(ix) < min_words:
                nx, pv = ix[-1] + 1, ix[0] - 1
                if nx < len(us) and not us[nx].get('heading') and not set(us[nx]['blocks']) & k_keep:
                    ix.append(nx)
                elif pv >= 0 and not us[pv].get('heading') and not set(us[pv]['blocks']) & k_keep:
                    ix.insert(0, pv)
                else:
                    break
            while ix[0] > 0 and us[ix[0] - 1].get('heading'):
                ix.insert(0, ix[0] - 1)
            n += 1
            name = '%s-fxw%d' % (key.replace('+', '_'), n)
            text = '\n\n'.join(p for j in ix for p in us[j]['paras'])
            (out / (name + '.txt')).write_text(text, encoding='utf-8')
            bundle[name] = text
            sent = [b for j in ix for b in us[j]['blocks']]
            manifest.append({'run': name, 'key': key, 'sent': sent, 'flagged': [b for j in ix if not us[j].get('heading') for b in us[j]['blocks']],
                             'headings': [b for j in ix if us[j].get('heading') for b in us[j]['blocks']], 'words': len(text.split()),
                             'input': 'meaning-fixed text', 'from': path})
    (out / 'runs.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')
    s = json.dumps(bundle, ensure_ascii=False)
    (out / 'BUNDLE.json').write_text(s, encoding='utf-8')
    print(len(manifest), 'runs,', sum(m['words'] for m in manifest), 'words; BUNDLE.json sha256', hashlib.sha256(s.encode('utf-8')).hexdigest())
    return manifest


def assembled_fixed(fixed_path, refix_dirs):
    """A fixed section with the stretches some refix run rewrote put in from that run (later folders win): (text, the
    run files used). Units no run covers keep their fixed (or published) paragraphs."""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import assemble as A
    d = json.loads(pathlib.Path(fixed_path).read_text(encoding='utf-8'))
    out, files = [], set()
    for kind, u in _merge(d, A.run_segments(refix_dirs)):
        out += u['paras'] if kind == 'base' else u[1]
        if kind == 'seg':
            files.add(u[3])
    return '\n\n'.join(out), sorted(files)


def _merge(d, segs):
    """[('base', unit) | ('seg', segment)] in order: each unit of a fixed section, or the refix segments that replace it.
    A segment can cover one block of a stretch that was one unit (a run's output split one paragraph per block): then
    every block of that unit must come from a segment, or the unit must have one paragraph per block so the blocks no
    segment covers keep theirs. Anything else raises, instead of dropping the blocks after the first segment (until
    2026-10-18 they were dropped: HG36 lost B10-B12 that way, HG24 B43, B44, B47 and B48)."""
    key, out, skip_to = d['key'], [], -1
    for u in d['units']:
        bl = u['blocks']
        if bl[-1] <= skip_to:
            continue
        mine, b = [], bl[0]
        while b <= bl[-1]:
            sg = segs.get((key, b))
            if sg:
                mine.append(sg); b = sg[0][-1] + 1
            else:
                b += 1
        if not mine:
            if bl[0] <= skip_to:
                raise ValueError('%s: unit %s starts inside a segment that ends at B%d' % (key, bl, skip_to))
            out.append(('base', u)); continue
        cover = {x for sg in mine for x in sg[0]}
        if set(bl) <= cover:
            out += [('seg', sg) for sg in mine]
        elif len(u['paras']) == len(bl):
            for i, x in enumerate(bl):
                sg = next((s for s in mine if s[0][0] == x), None)
                if sg:
                    out.append(('seg', sg))
                elif x not in cover:
                    out.append(('base', dict(u, blocks=[x], paras=[u['paras'][i]])))
        else:
            raise ValueError('%s: segments %s cover only part of unit %s, whose %d paragraphs don\'t line up with its blocks'
                             % (key, [sg[0] for sg in mine], bl, len(u['paras'])))
        skip_to = max(skip_to, max(cover))
    return out


def _nblocks(u):
    import re
    return sum(len([x for x in re.split(r'\n\s*\n', p) if x.strip()]) for p in u['paras'])


def hit_published(units_path, draft_blocks):
    """The published blocks of the units of a checked text (UNITS_PATH: a fixed.json or a refix units file) whose
    blank-line blocks a check flagged (flagged.py's draft blocks)."""
    d = json.loads(pathlib.Path(units_path).read_text(encoding='utf-8'))
    fl, i, out = set(draft_blocks), 0, set()
    for u in d['units']:
        n = _nblocks(u)
        if fl & set(range(i, i + n)):
            out |= set(u['blocks'])
        i += n
    return out


def fixed_draft_blocks(fixed_path, pub_blocks):
    """The fixed text's own blank-line blocks under those published blocks: what window_runs() takes, so a second refix
    sample of a window that read AI starts again from my meaning-fixed text."""
    d = json.loads(pathlib.Path(fixed_path).read_text(encoding='utf-8'))
    i, out = 0, []
    for u in d['units']:
        n = _nblocks(u)
        if set(u['blocks']) & set(pub_blocks):
            out += list(range(i, i + n))
        i += n
    return out


def units_fixed(fixed_path, refix_dirs):
    """The units of assembled_fixed(): {"key", "units"} with each refix segment as an "emulate" unit ("refix": the run),
    every other unit as the fixed section has it. faithful.py verify and apply read it like assemble.units()."""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import assemble as A
    d = json.loads(pathlib.Path(fixed_path).read_text(encoding='utf-8'))
    out = []
    for kind, u in _merge(d, A.run_segments(refix_dirs)):
        if kind == 'seg':
            out.append({'kind': 'emulate', 'blocks': u[0], 'paras': u[1], 'run': u[2], 'file': u[3], 'refix': True})
        else:  # the fixed text is now the baseline: its review's fixes and verdicts stay in its own file
            out.append({k: v for k, v in u.items() if k not in ('fixes', 'verdict', 'redo', 'paras_was')})
    return {'key': d['key'], 'from': str(fixed_path), 'refix_dirs': [str(x) for x in refix_dirs], 'units': out}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('make', 'units'))
    ap.add_argument('outdir')
    ap.add_argument('specs', nargs='+')
    a = ap.parse_args()
    if a.cmd == 'units':  # units OUT.json FIXED.json REFIX_DIR [REFIX_DIR ...]
        u = units_fixed(a.specs[0], a.specs[1:])
        pathlib.Path(a.outdir).write_text(json.dumps(u, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('%s: %d units, %d from refix runs -> %s' % (u['key'], len(u['units']), sum(bool(x.get('refix')) for x in u['units']), a.outdir))
        return
    make(a.outdir, a.specs)


if __name__ == '__main__':
    sys.exit(main())
