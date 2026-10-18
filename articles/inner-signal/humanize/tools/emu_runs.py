"""emu_runs.py - the Emulate inputs for a batch's flagged blocks, and putting Emulate's outputs back (2026-10-18).

The queue's method (articles/inner-child-therapy/experiments/emulate-20260929/GPT-OVERNIGHT-DIRECTIVE.md, Part 2): only
flagged paragraphs go to Emulate, one run per run of flagged paragraphs, with the headings kept in the paste as lines so
Emulate sees the structure; a run under 40 words goes with the paragraph next to it, and only the flagged paragraph's
rewrite is put back; a run's output is used only if it has as many paragraphs as its input. The assembled text keeps the
original headings.

  python3 tools/emu_runs.py make FLAGS.json OUTDIR [--keys K ...]     -> OUTDIR/<run>.txt and OUTDIR/runs.json
  python3 tools/emu_runs.py back OUTDIR                               -> OUTDIR/back.json: each run's blocks, old and new

FLAGS.json is flagged.py's report (each key's flagged blocks); the keys' texts are rebuilt from the working copy the same
way make_b429.py built them (sections.py), so every block knows whether it is a heading.
"""
import argparse, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(HERE))
import sections as S  # noqa: E402

MIN_WORDS = 40


def key_blocks(md_path, editor):
    """key -> [(markdown, plain_for_pangram, is_heading)], the groups make_b429.py checked."""
    secs = S.sections(pathlib.Path(md_path).read_text(encoding='utf-8'), editor)
    opening, secs = secs[0][1], secs[1:]
    out, i = {}, 0
    while i < len(secs):
        g = [i]
        while sum(len(S.text_of(secs[k][1]).split()) for k in g) < 50 and g[-1] + 1 < len(secs):
            g.append(g[-1] + 1)
        key = 'HG%02d' % (g[0] + 1) + ''.join('+%02d' % (k + 1) for k in g[1:])
        blocks = (opening if g[0] == 0 else []) + [b for k in g for b in secs[k][1]]
        out[key] = [(m, S.LIST.sub('', p), m.lstrip().startswith('#')) for m, p in blocks]
        i = g[-1] + 1
    return out


def runs_for(blocks, flagged):
    """[[block index, ...]] of consecutive flagged prose blocks; a heading between two flagged blocks stays in the run,
    and a heading just before a run is put at its start as a line."""
    fl = sorted(set(flagged))
    runs, cur = [], []
    for k in range(len(blocks)):
        if k in fl and not blocks[k][2]:
            if cur and any(j not in fl and not blocks[j][2] for j in range(cur[-1] + 1, k)):
                runs.append(cur); cur = []
            cur.append(k)
    if cur:
        runs.append(cur)
    out = []
    for r in runs:
        a, b = r[0], r[-1]
        while a > 0 and blocks[a - 1][2]:
            a -= 1
        out.append(list(range(a, b + 1)))
    return out


def make(flags_path, outdir, keys, md_path, editor):
    flags = json.load(open(flags_path, encoding='utf-8'))
    kb = key_blocks(md_path, editor)
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    manifest = []
    for key in keys or [k for k in flags if flags[k]['flagged_blocks']]:
        blocks = kb[key]
        fl = flags[key]['flagged_blocks']
        for n, r in enumerate(runs_for(blocks, fl), 1):
            send = list(r)
            prose = lambda ks: sum(len(blocks[j][1].split()) for j in ks if not blocks[j][2])
            while prose(send) < MIN_WORDS:
                nxt = send[-1] + 1
                prv = send[0] - 1
                if nxt < len(blocks) and not blocks[nxt][2]:
                    send.append(nxt)
                elif prv >= 0 and not blocks[prv][2]:
                    send.insert(0, prv)
                else:
                    break
            name = '%s-r%d' % (key.replace('+', '_'), n)
            text = '\n\n'.join(blocks[j][1] for j in send)
            (out / (name + '.txt')).write_text(text, encoding='utf-8')
            manifest.append({'run': name, 'key': key, 'sent': send, 'flagged': [j for j in send if j in fl and not blocks[j][2]],
                             'headings': [j for j in send if blocks[j][2]], 'words': len(text.split())})
    (out / 'runs.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')
    for m in manifest:
        print('%-14s %4d words, blocks %s, put back %s' % (m['run'], m['words'], m['sent'], m['flagged']))
    print(len(manifest), 'runs,', sum(m['words'] for m in manifest), 'words')


def back(outdir, md_path, editor):
    out = pathlib.Path(outdir)
    manifest = json.load(open(out / 'runs.json', encoding='utf-8'))
    kb = key_blocks(md_path, editor)
    res = []
    for m in manifest:
        f = out / (m['run'] + '.out.txt')
        if not f.exists():
            res.append({'run': m['run'], 'status': 'no output'}); continue
        paras = [p.strip() for p in re.split(r'\n\s*\n', f.read_text(encoding='utf-8')) if p.strip()]
        blocks = kb[m['key']]
        if len(paras) != len(m['sent']):
            res.append({'run': m['run'], 'key': m['key'], 'status': 'paragraph count %d, sent %d' % (len(paras), len(m['sent'])),
                        'out': paras}); continue
        pairs = []
        for j, p in zip(m['sent'], paras):
            if j in m['flagged']:
                pairs.append({'block': j, 'old': blocks[j][1], 'new': p})
            elif blocks[j][2] and p.strip().lstrip('#').strip() != blocks[j][1]:
                pairs.append({'block': j, 'heading_changed_to': p})
        res.append({'run': m['run'], 'key': m['key'], 'status': 'ok', 'pairs': pairs})
    (out / 'back.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for r in res:
        print(r['run'], r['status'])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('make', 'back'))
    ap.add_argument('args', nargs='+')
    ap.add_argument('--keys', nargs='*')
    ap.add_argument('--md', default=str(H / 'HUMANIZED-SO-FAR.md'))
    ap.add_argument('--editor', default=str(H / 'source' / 'substack-editor-20260928.html'))
    a = ap.parse_args()
    if a.cmd == 'make':
        make(a.args[0], a.args[1], a.keys, a.md, a.editor)
    else:
        back(a.args[0], a.md, a.editor)


if __name__ == '__main__':
    main()
