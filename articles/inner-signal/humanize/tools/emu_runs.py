"""emu_runs.py - the Emulate inputs for a batch's flagged blocks, and putting Emulate's outputs back (2026-10-18).

The queue's method (articles/inner-child-therapy/experiments/emulate-20260929/GPT-OVERNIGHT-DIRECTIVE.md, Part 2): only
flagged paragraphs go to Emulate, one run per run of flagged paragraphs, with the headings kept in the paste as lines so
Emulate sees the structure; a run under 40 words goes with the paragraph next to it, and only the flagged paragraph's
rewrite is put back; a run's output is used only if it has as many paragraphs as its input. The assembled text keeps the
original headings.

  python3 tools/emu_runs.py make FLAGS.json OUTDIR [--keys K ...]     -> OUTDIR/<run>.txt and OUTDIR/runs.json
  python3 tools/emu_runs.py back OUTDIR                               -> OUTDIR/back.json: each run's segments, old and new
  python3 tools/emu_runs.py split SRCDIR OUTDIR --runs R ...          -> smaller runs (no headings) for runs that didn't map

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


WORD = re.compile(r"[a-z0-9']+")
STOP = set('a an and the of to in on for or is are be it its this that with as by at from your you i'.split())


def content(t):
    return {w for w in WORD.findall(t.lower()) if w not in STOP}


def heading_like(p):
    p = p.strip()
    return len(p.split()) <= 15 and not p.endswith(('.', ',', ';', ':')) and '\n' not in p and not p.startswith(('“', '"'))


def rewritten_heading(title, p):
    """A short line that shares a word stem with the heading and isn't much longer than it, and isn't a list item with a
    gloss in brackets (emu-i, 2026-10-18: "Iteration (revise the prompt based on real life feedback)" was taken for the
    heading "Core prompts" and the paragraphs after it were put under the wrong heading)."""
    return (heading_like(p) and '(' not in p and len(p.split()) <= max(4, 2 * len(title.split()))
            and bool(stems(title) & stems(p)))


STEM_STOP = set(('how what when where why who which can do does did not no me my we us our if so all any more one get have '
                 'has will would should could may might there here then than just also about into out up down over under again '
                 'too very re').split())


def stems(t):
    """content words cut to five letters, so "spiritually" meets "spiritual" and "processing" meets "process"
    (Emulate rewrites headings: "You get stuck in spiritual bypass" came back as "You're spiritually bypassing"); common
    words don't count (emu-i: "How" made "Resistance: What are you protecting me from? How can you trust me 1% more?"
    look like the heading "Appendix A: How to ask the subconscious a useful question")."""
    return {w[:5] for w in content(t) if w not in STEM_STOP}


def match_headings(heads, paras):
    """For each published heading of the run, in order, the index of Emulate's paragraph that stands for it: the same
    words, or a short line that shares a third of its content words, or a paragraph that starts with it (the heading
    run into the paragraph: the start is cut off there). None when one can't be found."""
    pos, start, cut = [], 0, {}
    for title in heads:
        tw = content(title)
        got = None
        for i in range(start, len(paras)):
            p = paras[i].strip()
            if p.lower().rstrip('.!?:') == title.lower().rstrip('.!?:'):
                got = i; break
            if heading_like(p) and tw and len(tw & content(p)) * 3 >= len(tw):
                got = i; break
            if rewritten_heading(title, p):
                got = i; break
            first = re.split(r'(?<=[.!?:])\s+', p, maxsplit=1)
            if len(first) == 2 and heading_like(first[0].rstrip('.:')) and tw and len(tw & content(first[0])) * 2 >= len(tw):
                got = i; cut[i] = first[1]; break
        if got is None:
            return None, None
        pos.append(got); start = got + 1
    return pos, cut


ALIGN = False  # back --align: the cut by overlap when the headings can't be found (off for the folders mapped before it)


def segments(m, blocks, paras):
    """[(published block indexes, Emulate's paragraphs)] for one run, or None when its headings can't be placed.
    With as many paragraphs as blocks, each flagged block is its own segment; otherwise each stretch between two
    headings is one segment, its published blocks for Emulate's paragraphs there."""
    sent = m['sent']
    if len(paras) == len(sent):
        return [([j], [p]) for j, p in zip(sent, paras) if j in m['flagged']]
    heads = [j for j in sent if blocks[j][2]]
    pos, cut = match_headings([blocks[j][1] for j in heads], paras)
    if pos is None:
        return aligned(m, blocks, paras, heads) if ALIGN else None
    bounds_b = [-1] + [sent.index(h) for h in heads] + [len(sent)]
    bounds_p = [-1] + pos + [len(paras)]
    out = []
    for k in range(len(bounds_b) - 1):
        bs = [sent[i] for i in range(bounds_b[k] + 1, bounds_b[k + 1])]
        ps = [paras[i] for i in range(bounds_p[k] + 1, bounds_p[k + 1])]
        if k >= 1 and bounds_p[k] in cut:   # the heading ran into its paragraph: the rest of it is this stretch's prose
            ps = [cut[bounds_p[k]]] + ps
        if not bs and not ps:
            continue
        if not bs or not ps or not set(bs) <= set(m['flagged']) | set(m.get('context', [])):
            return None
        out.append((bs, ps))
    return out


def aligned(m, blocks, paras, heads):
    """When Emulate dropped or merged the run's headings (emu-h, 2026-10-18: HG37's two runs, HG24's): Emulate's lines that
    look like a rewritten heading (a short line sharing a word with one of the run's headings) are dropped, the
    published headings stay, and Emulate's paragraphs are cut into the stretches between the headings where each
    stretch's words best match its published blocks (the cut that maximizes the summed overlap, in order). The meaning
    review checks each stretch against its published blocks, so a bad cut shows there. None when it can't be cut."""
    sent = m['sent']
    hs = [blocks[j][1] for j in heads]
    ps = [p for p in paras if not any(rewritten_heading(h, p) for h in hs)]
    bounds = [-1] + [sent.index(h) for h in heads] + [len(sent)]
    groups = [[sent[i] for i in range(bounds[k] + 1, bounds[k + 1])] for k in range(len(bounds) - 1)]
    groups = [g for g in groups if g]
    if not groups or len(ps) < len(groups) or not all(set(g) <= set(m['flagged']) | set(m.get('context', [])) for g in groups):
        return None
    gs = [stems(' '.join(blocks[j][1] for j in g)) for g in groups]
    pst = [stems(p) for p in ps]
    def score(k, a, b):  # group k gets paragraphs a..b-1
        w = set().union(*pst[a:b])
        return len(gs[k] & w) / (len(gs[k] | w) or 1)
    K, N = len(groups), len(ps)
    best = {(0, 0): (0.0, [])}
    for k in range(K):
        nxt = {}
        for (kk, a), (v, cuts) in best.items():
            if kk != k:
                continue
            for b in range(a + 1, N - (K - k - 1) + 1):
                if k == K - 1 and b != N:
                    continue
                cand = (v + score(k, a, b), cuts + [(a, b)])
                if (k + 1, b) not in nxt or cand[0] > nxt[(k + 1, b)][0]:
                    nxt[(k + 1, b)] = cand
        best = nxt
    if (K, N) not in best:
        return None
    return [(g, ps[a:b]) for g, (a, b) in zip(groups, best[(K, N)][1])]


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
        segs = segments(m, blocks, paras)
        if segs is None:
            res.append({'run': m['run'], 'key': m['key'], 'status': 'unplaced: %d paragraphs for %d blocks, headings not found'
                        % (len(paras), len(m['sent'])), 'out': paras}); continue
        how = 'ok' if len(paras) == len(m['sent']) else ('ok, regrouped' if match_headings([blocks[j][1] for j in m['sent'] if blocks[j][2]], paras)[0] is not None else 'ok, aligned (headings not in the output; --align)')
        res.append({'run': m['run'], 'key': m['key'], 'status': how,
                    'segments': [{'blocks': bs, 'old': [blocks[j][1] for j in bs], 'new': ps} for bs, ps in segs]})
    (out / 'back.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for r in res:
        print(r['run'], r['status'])


def split(src_dir, runs, outdir, md_path, editor, max_words=180):
    """Smaller runs for runs whose output couldn't be placed: each a stretch of consecutive prose blocks of the run, no
    headings (a stretch with no heading maps back as one segment whatever Emulate does with its paragraphs), at most
    MAX_WORDS where the blocks allow, at least MIN_WORDS, a lead-in (a block ending with a colon) kept with the block after
    it."""
    src = json.load(open(pathlib.Path(src_dir) / 'runs.json', encoding='utf-8'))
    kb = key_blocks(md_path, editor)
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    try:
        manifest = json.load(open(out / 'runs.json', encoding='utf-8'))
    except FileNotFoundError:
        manifest = []
    have = {m['run'] for m in manifest}
    for m in src:
        if m['run'] not in runs:
            continue
        blocks = kb[m['key']]
        prose = [j for j in m['sent'] if not blocks[j][2] and j in m['flagged']]
        # stretches of consecutive prose (a heading or a kept block ends one)
        stretches, cur = [], []
        for j in prose:
            if cur and j != cur[-1] + 1:
                stretches.append(cur); cur = []
            cur.append(j)
        if cur:
            stretches.append(cur)
        n = 0
        for st in stretches:
            pieces, cur, words = [], [], 0
            for idx, j in enumerate(st):
                w = len(blocks[j][1].split())
                lead_in = blocks[j][1].rstrip().endswith(':')
                if cur and words + w > max_words and words >= MIN_WORDS and not blocks[cur[-1]][1].rstrip().endswith(':'):
                    pieces.append(cur); cur, words = [], 0
                cur.append(j); words += w
            if cur:
                if pieces and words < MIN_WORDS:
                    pieces[-1] += cur
                else:
                    pieces.append(cur)
            for pc in pieces:
                n += 1
                name = '%s-s%d' % (m['run'], n)
                text = '\n\n'.join(blocks[j][1] for j in pc)
                if len(text.split()) < MIN_WORDS:
                    print('%s: %d words, under Emulate\'s minimum; left as published' % (name, len(text.split())))
                    continue
                (out / (name + '.txt')).write_text(text, encoding='utf-8')
                if name not in have:
                    manifest.append({'run': name, 'key': m['key'], 'sent': pc, 'flagged': pc, 'headings': [], 'words': len(text.split()),
                                     'split_from': m['run']})
                print('%-18s %4d words, blocks %s' % (name, len(text.split()), pc))
    (out / 'runs.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')


def short_with_heading(src_dir, runs, outdir, md_path, editor):
    """Runs for the stretches split() left as published (under Emulate's 40 words): each with the heading over it as a
    line, and the next heading and stretch too while it is still short, so Emulate sees a little structure and the
    output maps back by its headings (segments())."""
    src = json.load(open(pathlib.Path(src_dir) / 'runs.json', encoding='utf-8'))
    kb = key_blocks(md_path, editor)
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    try:
        manifest = json.load(open(out / 'runs.json', encoding='utf-8'))
    except FileNotFoundError:
        manifest = []
    have = {m['run'] for m in manifest}
    for m in src:
        if m['run'] not in runs:
            continue
        blocks = kb[m['key']]
        # the stretches between headings, with the heading before each
        groups, cur, head = [], [], None
        for j in m['sent']:
            if blocks[j][2]:
                if cur:
                    groups.append((head, cur))
                head, cur = j, []
            elif j in m['flagged']:
                cur.append(j)
        if cur:
            groups.append((head, cur))
        words = lambda bs: sum(len(blocks[j][1].split()) for j in bs)
        short = [g for g in groups if words(g[1]) < MIN_WORDS]
        n, i = 0, 0
        while i < len(short):
            pieces = [short[i]]
            while sum(words(g[1]) for g in pieces) < MIN_WORDS and i + 1 < len(short) and short[i + 1][1][0] == pieces[-1][1][-1] + 2:
                i += 1
                pieces.append(short[i])
            i += 1
            sent = [b for h, bs in pieces for b in ([h] if h is not None else []) + bs]
            flagged = [b for h, bs in pieces for b in bs]
            text = '\n\n'.join(blocks[j][1] for j in sent)
            if len(text.split()) < MIN_WORDS:
                print('%s: %d words with its heading, still under the minimum; left as published' % (m['run'], len(text.split())))
                continue
            n += 1
            name = '%s-h%d' % (m['run'], n)
            (out / (name + '.txt')).write_text(text, encoding='utf-8')
            if name not in have:
                manifest.append({'run': name, 'key': m['key'], 'sent': sent, 'flagged': flagged,
                                 'headings': [h for h, _ in pieces if h is not None], 'words': len(text.split()), 'short_from': m['run']})
            print('%-18s %4d words, blocks %s (headings %s)' % (name, len(text.split()), sent, [h for h, _ in pieces]))
    (out / 'runs.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('make', 'back', 'split', 'short'))
    ap.add_argument('--runs', nargs='*')
    ap.add_argument('--max', type=int, default=180)
    ap.add_argument('args', nargs='+')
    ap.add_argument('--keys', nargs='*')
    ap.add_argument('--md', default=str(H / 'source' / 'published-20260928.md'))  # the published blocks (assemble.kb())
    ap.add_argument('--editor', default=str(H / 'source' / 'substack-editor-20260928.html'))
    ap.add_argument('--align', action='store_true', help='back: when a run\'s headings are not in its output, cut its paragraphs '
                    'into the stretches between the published headings by word overlap (emu-h on; the folders mapped before '
                    'keep their mapping)')
    a = ap.parse_args()
    global ALIGN
    ALIGN = a.align
    if a.cmd == 'make':
        make(a.args[0], a.args[1], a.keys, a.md, a.editor)
    elif a.cmd == 'split':
        split(a.args[0], a.runs, a.args[1], a.md, a.editor, a.max)
    elif a.cmd == 'short':
        short_with_heading(a.args[0], a.runs, a.args[1], a.md, a.editor)
    else:
        back(a.args[0], a.md, a.editor)


if __name__ == '__main__':
    main()
