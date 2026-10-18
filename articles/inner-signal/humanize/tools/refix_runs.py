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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('make',))
    ap.add_argument('outdir')
    ap.add_argument('specs', nargs='+')
    a = ap.parse_args()
    make(a.outdir, a.specs)


if __name__ == '__main__':
    sys.exit(main())
