"""Round 2 of the neuro de-armoring rewrite: Emulate on the stretches that read AI in round 1 (../r1/b/RESULTS.md: 26
stretches, 19 of them 100% AI, the best 12.7% AI), after the free rewrite in his voice failed. The repository's order
for a published article's flagged paragraphs is Emulate first (AGENTS.md; docs/EMULATE-FALLBACK.md, section 2); this
lane had set Emulate aside because its rewrites of this article broke the dose rule in 14 of 40 captures, and that rule
is now held by fidelity_keys.py, so an Emulate version goes on only when the whole draft with it passes the check.

What goes to Emulate: each round-1 stretch's text between its headings (a "segment", 40 words or more, as plain text with
no heading; docs/EMULATE-FALLBACK.md, section 3), from ../r1/CANDIDATE.md, the draft that holds every claim and number.
A segment under 40 words stays as round 1 had it. His paragraphs that read Human (High) in the baseline aren't in the
stretches and don't go (round 1's KNOWN_HUMAN).

  python3 .../r2/emulate_r2.py make            # INPUTS.json and emu-in/*.txt, for the laptop
  python3 .../r2/emulate_r2.py collect OUTDIR  # reads OUTDIR/<seg>-v1.txt: DRAFT-v1.md, TEXTS.json, FIDELITY-v1.txt
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ART = H.parent
ROOT = ART.parents[1]
R1 = HERE.parent / 'r1'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(R1))
import suggestion_review as sr  # noqa: E402
import assemble_r1 as a1  # noqa: E402


def stretch_blocks():
    """Round 1's stretches with their candidate blocks, rebuilt the way assemble_r1.py cut them."""
    cand = (R1 / 'CANDIDATE.md').read_text(encoding='utf-8')
    rows = json.loads((R1 / 'STRETCHES.json').read_text(encoding='utf-8'))
    bl = sr.blocks(cand)
    out = []
    for r in rows:
        first, last = r['blocks']
        blocks = [b for b in bl[first:last + 1] if a1.readable(b) and not (
            b['text'] == 'Introduction' or b['text'].startswith(a1.KNOWN_HUMAN[1:]))]
        t = '\n\n'.join(b['text'] for b in blocks)
        assert hashlib.sha256(t.encode('utf-8')).hexdigest() == r['sha256'], r['key']
        out.append((r['key'], blocks))
    return cand, bl, out


def segments(blocks):
    """The runs of non-heading blocks between headings: [(kind, [blocks])], kind 'head', 'emu' (40 words or more) or
    'keep' (shorter, stays as it is)."""
    segs, cur = [], []
    for b in blocks:
        if b['level']:
            if cur:
                segs.append(cur)
                cur = []
            segs.append([b])
        else:
            cur.append(b)
    if cur:
        segs.append(cur)
    out = []
    for s in segs:
        if s[0]['level']:
            out.append(('head', s))
        else:
            w = sum(len(b['text'].split()) for b in s)
            out.append(('emu' if w >= 40 else 'keep', s))
    return out


def make():
    cand, bl, rows = stretch_blocks()
    (HERE / 'emu-in').mkdir(exist_ok=True)
    inputs = []
    for key, blocks in rows:
        for n, (kind, s) in enumerate(segments(blocks)):
            if kind != 'emu':
                continue
            name = '%s-%d' % (key, n)
            t = '\n\n'.join(b['text'] for b in s)
            (HERE / 'emu-in' / (name + '.txt')).write_text(t + '\n', encoding='utf-8')
            inputs.append({'name': name, 'stretch': key, 'blocks': [s[0]['i'], s[-1]['i']], 'words': len(t.split()),
                           'sha256': hashlib.sha256((t + '\n').encode('utf-8')).hexdigest()})
    (HERE / 'INPUTS.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(inputs), 'segments,', sum(i['words'] for i in inputs), 'words')


def collect(outdir, version='v1'):
    cand, bl, rows = stretch_blocks()
    od = pathlib.Path(outdir)
    texts, repl = {}, {}
    for key, blocks in rows:
        parts = []
        for n, (kind, s) in enumerate(segments(blocks)):
            name = '%s-%d' % (key, n)
            f = od / ('%s-%s.txt' % (name, version))
            if kind == 'emu' and f.exists():
                t = f.read_text(encoding='utf-8').strip()
                paras = [p.strip() for p in t.split('\n\n') if p.strip()]
                parts += paras
                repl[(s[0]['i'], s[-1]['i'])] = paras
            else:
                parts += [b['text'] for b in s]
        texts['r2%s-%s' % (version[-1], key[3:])] = '\n\n'.join(parts)
    # the draft: the candidate with each Emulate segment's blocks replaced by Emulate's paragraphs (no links)
    raw = cand.rstrip('\n').split('\n\n')
    assert len(raw) == len(bl), (len(raw), len(bl))
    out, i = [], 0
    spans = sorted(repl)
    while i < len(raw):
        hit = [sp for sp in spans if sp[0] == i]
        if hit:
            a, z = hit[0]
            out += repl[hit[0]]
            i = z + 1
        else:
            out.append(raw[i])
            i += 1
    draft = '\n\n'.join(out) + '\n'
    (HERE / ('DRAFT-%s.md' % version)).write_text(draft, encoding='utf-8')
    (HERE / ('TEXTS-%s.json' % version)).write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'fidelity_keys.py'), 'check',
                         str(H / 'FIDELITY-KEYS.json'), str(HERE / ('DRAFT-%s.md' % version))], capture_output=True, text=True)
    (HERE / ('FIDELITY-%s.txt' % version)).write_text(fk.stdout, encoding='utf-8')
    print(fk.stdout.strip()[-4000:])
    for k, t in texts.items():
        paras = [p for p in t.split('\n\n') if len(p.split()) >= 8]
        print(' ', k, len(paras), 'paragraphs', len(t.split()), 'words', '(over the API limit)' if len(paras) > 6 or len(t.split()) > 1200 else '')


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('make')
    c = sub.add_parser('collect')
    c.add_argument('outdir')
    c.add_argument('--version', default='v1')
    a = ap.parse_args()
    if a.cmd == 'make':
        make()
    else:
        collect(a.outdir, a.version)


if __name__ == '__main__':
    main()
