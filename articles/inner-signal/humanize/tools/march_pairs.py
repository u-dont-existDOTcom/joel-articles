"""march_pairs.py - one march read for every fixed Emulate stretch, before and after my fixes (2026-10-18).

The gate's edit record (tools/humanization/pangram_gate.py, E173) needs the march of the version that passed Pangram
("march_was": Emulate's stretch, Human in its section's screen) and of the edit ("march"); an edit is held only when the
version that passed had a break and the edit has none. This writes all of them as one draft for one march reader
(tools/humanization/reviewer/reviewer.py march), and reads the labels back.

  python3 tools/march_pairs.py draft FIXED.json [FIXED.json ...] --out DIR      -> DIR/march-draft.txt, DIR/march-map.json
  python3 tools/march_pairs.py read DIR LABELS.txt                              -> DIR/march.json: {key: {"was": [...], "new": [...]}}

A stretch's key is SECTION-B<first block>. Paragraphs the march reader skips (headings, short lines without an end mark)
are skipped here the same way, by the reviewer's own march_paragraphs().
"""
import argparse, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import reviewer as R  # noqa: E402


def draft(files, out):
    out = pathlib.Path(out)
    out.mkdir(parents=True, exist_ok=True)
    paras, mp = [], []
    for f in files:
        d = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
        for u in d['units']:
            if u['kind'] != 'emulate' or not u.get('fixes'):
                continue
            key = '%s-B%d' % (d['key'], u['blocks'][0])
            old = u.get('paras_was') or None
            if old is None:  # the units file before apply() has the Emulate text
                src = json.loads(pathlib.Path(f.replace('.fixed.json', '.units.json')).read_text(encoding='utf-8'))
                old = next(x['paras'] for x in src['units'] if x['blocks'] == u['blocks'])
            for ver, ps in (('was', old), ('new', u['paras'])):
                for p in ps:
                    n = len(R.march_paragraphs(p))
                    if n:
                        paras.append(p)
                        mp.append({'key': key, 'ver': ver, 'n': n, 'start': sum(m['n'] for m in mp)})
    text = '\n\n'.join(paras)
    (out / 'march-draft.txt').write_text(text, encoding='utf-8')
    (out / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    total = len(R.march_paragraphs(text))
    assert total == sum(m['n'] for m in mp), (total, sum(m['n'] for m in mp))
    print(len(mp), 'paragraph entries,', total, 'march paragraphs ->', out / 'march-draft.txt')


def read(d, labels):
    d = pathlib.Path(d)
    mp = json.loads((d / 'march-map.json').read_text(encoding='utf-8'))
    got = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', pathlib.Path(labels).read_text(encoding='utf-8'), re.M))
    text = (d / 'march-draft.txt').read_text(encoding='utf-8')
    ps = R.march_paragraphs(text)
    out, bad = {}, []
    for m in mp:
        for i in range(m['start'], m['start'] + m['n']):
            seq = got.get(str(i + 1), '').split()
            if len(seq) != len(ps[i]):
                bad.append('T%d: %d labels for %d sentences' % (i + 1, len(seq), len(ps[i])))
            out.setdefault(m['key'], {'was': [], 'new': []})[m['ver']].append(' '.join(seq))
    (d / 'march.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    print(len(out), 'stretches read;', len(bad), 'paragraphs with the wrong number of labels')
    for b in bad[:20]:
        print(' ', b)
    return out, bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('draft', 'read'))
    ap.add_argument('args', nargs='+')
    ap.add_argument('--out')
    a = ap.parse_args()
    if a.cmd == 'draft':
        draft(a.args, a.out)
    else:
        read(a.args[0], a.args[1])


if __name__ == '__main__':
    main()
