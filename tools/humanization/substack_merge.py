#!/usr/bin/env python3
"""substack_merge.py - put a humanized Markdown master into the raw Substack editor HTML it was humanized from (2026-10-18).

Joel, 2026-10-18 01:29 UTC: "merge the final article into the substack html. i'm pasting the latest one i have. use the
validated clipboard helper to give me a copy button". The helper itself is built only by the canonical generator
(project-sources/substack_transfer_helper.py.txt, docs/SUBSTACK-HELPER-DELIVERY-GATE.md) from the archival HTML this writes.
This tool makes that archival HTML, the way the Romance R7 merge did (work/romance-owner-manual-dedup-20260827/): raw-string
replacement of the text blocks, never a parse and reserialization of the document.

- Native objects (images with their captions, embeds, YouTube, Share, Subscribe) are frozen with the canonical
  project-sources/html_islands.py.txt, carried byte-for-byte, restored and verified.
- The published Markdown (the text the master was humanized from, converted from an earlier copy of the same editor HTML)
  is the bridge. Its text blocks must match the editor's text blocks one for one; the tool checks that first. That
  conversion lost some of the editor's formatting (lists, bold lead-ins, line breaks, rules), so each master paragraph takes
  the formatting of the published paragraph it aligns with: list membership, a bold lead-in when the master starts with the
  same words, and a bold block of line-broken questions when it has the same number of questions.
- Anchors (the native objects and the headings all three share) cut the article into segments; inside a segment the
  master's blocks replace the editor's, in the master's order. Rules and empty paragraphs stay where the editor had them,
  next to the anchor they touch.
- Checks: the islands verify; the merged text, read as plain words, equals the master's text blocks word for word; every
  link in the master is in the merge with the editor's link attributes.

Usage (from the repo root):
  python3 tools/humanization/substack_merge.py --editor RAW.html --master MASTER.md --published PUBLISHED.md \\
      --out ARCHIVAL.html --report REPORT.json
Exits 1 on any failed check, with the reasons in the report.
"""
import argparse, difflib, hashlib, html, importlib.util, json, re, sys, tempfile
from importlib.machinery import SourceFileLoader
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LINK_ATTRS = 'target="_blank" rel="noopener noreferrer nofollow"'
VOID = {'br', 'img', 'hr', 'source', 'input', 'meta', 'link', 'wbr'}
TAG = re.compile(r'<(/?)([a-zA-Z0-9]+)([^>]*?)(/?)>|<!--.*?-->', re.S)
ISLAND = re.compile(r'^<!--HVA_ISLAND_(\d+)-->$')


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def islands_module():
    src = REPO / 'project-sources' / 'html_islands.py.txt'
    loader = SourceFileLoader('html_islands', str(src))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['html_islands'] = mod
    loader.exec_module(mod)
    return mod


def top_blocks(inner):
    """The editor body's top-level children, as raw strings that join back to it exactly."""
    out, depth, start, last = [], 0, 0, 0
    for m in TAG.finditer(inner):
        g = m.group(0)
        if g.startswith('<!--'):
            if depth == 0:
                out.append(g); last = m.end()
            continue
        close, name, selfc = m.group(1), m.group(2).lower(), m.group(4)
        if name in VOID or selfc:
            if depth == 0:
                out.append(g); last = m.end()
            continue
        if not close:
            if depth == 0:
                if inner[last:m.start()].strip():
                    raise SystemExit('text outside any element in the editor body: %r' % inner[last:m.start()][:80])
                start = m.start()
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                out.append(inner[start:m.end()]); last = m.end()
    if ''.join(out) != inner:
        raise SystemExit('the editor body did not split into whole top-level elements')
    return out


def plain_html(frag):
    t = re.sub(r'<br[^>]*>|</(p|li|h[1-6])>', ' ', frag)   # a block boundary is a space between words
    t = re.sub(r'<[^>]+>', '', t)
    return norm(html.unescape(t))


MD_LINK = re.compile(r'\[((?:[^\[\]]|\[[^\]]*\])*)\]\(((?:[^()\s]|\([^()\s]*\))*)\)')


def plain_md(t):
    t = MD_LINK.sub(lambda m: m.group(1), t)
    t = re.sub(r'\*{1,3}', '', t)
    return norm(t)


def norm(t):
    t = t.replace(' ', ' ')
    return re.sub(r'\s+', ' ', t).strip()


def words(t):
    return t.split()


# --- Markdown blocks ----------------------------------------------------------------------------------------------------

def md_blocks(md):
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]:
        if b.startswith('<!--'):
            kind = 'comment'
        elif re.match(r'^#{1,6} ', b):
            kind = 'heading'
        elif re.match(r'^\[image \d+\](\(.*\))?$', b):
            kind = 'image'
        elif b.startswith('[caption]'):
            kind = 'caption'
        elif b == '[Share](%%share_url%%)':
            kind = 'share'
        elif b.startswith('[Subscribe') and '%%checkout_url%%' in b:
            kind = 'subscribe'
        elif b == 'Double click to interact with video':
            kind = 'youtube'
        else:
            kind = 'para'
        out.append({'kind': kind, 'md': b})
    return out


def island_groups(blocks, types, urls):
    """For each native object, in order, the master's (or published text's) blocks that stand for it: [start, end)."""
    groups, i = [], 0
    for n, (typ, url) in enumerate(zip(types, urls)):
        while i < len(blocks):
            b = blocks[i]
            if typ == 'image' and b['kind'] == 'image' and '(' in b['md']:
                j = i + 1
                if j < len(blocks) and blocks[j]['kind'] == 'caption':
                    j += 1
                break
            if typ in ('share', 'subscribe', 'youtube') and b['kind'] == typ:
                j = i + 1
                break
            if typ == 'substack_video_post_embed':
                if b['kind'] == 'image' and '(' not in b['md'] and i + 1 < len(blocks) and blocks[i + 1]['md'].endswith('Copy link'):
                    j = i + 2
                    break
                if url and re.match(r'^\[.*\]\(%s\)\[$' % re.escape(url), b['md']):
                    j = next(k for k in range(i, len(blocks)) if blocks[k]['md'] == '[Read full story](%s)' % url) + 1
                    break
            i += 1
        else:
            raise SystemExit('object %d (%s) has no marker in the Markdown after block %d' % (n + 1, typ, groups[-1][1] if groups else 0))
        groups.append((i, j))
        i = j
    return groups


# --- inline Markdown to Substack HTML -----------------------------------------------------------------------------------

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def inline(t):
    """[text](url), ***x***, **x**, *x* -> the editor's markup (links with its attributes; bold-italic as strong>em)."""
    out, pos = [], 0
    for m in MD_LINK.finditer(t):
        out.append(emph(esc(t[pos:m.start()])))
        out.append('<a %s href="%s">%s</a>' % (LINK_ATTRS, esc(m.group(2)), emph(esc(m.group(1)))))
        pos = m.end()
    out.append(emph(esc(t[pos:])))
    return ''.join(out)


def emph(t):
    t = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


def heading_html(md, level=None):
    m = re.match(r'^(#{1,6}) +(.*)$', md)
    lv = level or len(m.group(1))
    return '<h%d>%s</h%d>' % (lv, inline(m.group(2).strip()), lv)


# --- formatting carried from the editor ---------------------------------------------------------------------------------

def editor_units(el):
    """A text element's units for alignment with the published blocks, each with how the editor formats it."""
    tag = re.match(r'<([a-zA-Z0-9]+)', el).group(1).lower()
    if tag in ('ul', 'ol'):
        out = []
        for k, it in enumerate(re.findall(r'<li>(.*?)</li>', el, re.S)):
            for para in re.findall(r'<p>.*?</p>', it, re.S):   # an item can hold several paragraphs
                out.append({'text': plain_html(para), 'list': tag, 'item': k, 'li': para})
        return out
    if tag == 'p':
        if not plain_html(el):
            return []
        return [{'text': plain_html(el), 'p': el}]
    if re.match(r'h[1-6]$', tag):
        return [{'text': plain_html(el), 'heading': el}]
    return [{'text': plain_html(el), 'other': el}]


def lead_bold(inner_html):
    m = re.match(r'^(?:<p>)?<strong>(.*?)</strong>', inner_html, re.S)
    return plain_html(m.group(1)) if m else None


def render_para(md, unit):
    """One master paragraph in the editor's markup, with the formatting of the published paragraph it aligns with."""
    body = inline(md)
    src = unit and (unit.get('li') or unit.get('p')) or ''
    whole = re.match(r'^(?:<p>)?<strong>(.*)</strong>(?:</p>)?$', src, re.S)
    if whole and '<br' in whole.group(1):
        qs = re.findall(r'[^?]+\?', plain_md(md))
        if len(qs) == len(re.findall(r'<br', whole.group(1))) + 1 and ''.join(qs).strip() == plain_md(md):
            return '<p><strong>%s</strong></p>' % '<br>'.join(inline(q.strip()) for q in qs), 'bold lines'
    lead = lead_bold(src) if src else None
    if lead and plain_md(md).startswith(lead) and not md.startswith('**'):
        # the lead-in's words, as they start the master's paragraph (the master's own markup kept inside it)
        k = next(k for k in range(1, len(md) + 1) if plain_md(md[:k]) == lead)
        return '<p><strong>%s</strong>%s</p>' % (inline(md[:k]), inline(md[k:])), 'bold lead-in'
    return '<p>%s</p>' % body, ''


def align(pub, mas):
    """Align published units with master blocks in order by word similarity (a DP, so a cut or an added paragraph costs
    one gap). Returns {master index: published index}."""
    P, M = [words(u) for u in pub], [words(m) for m in mas]
    sim = [[difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() for b in M] for a in P]
    n, m = len(P), len(M)
    MATCH = 0.25   # below this two paragraphs aren't the same paragraph, however the order goes
    best = [[0.0] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            c = []
            if i and j and sim[i - 1][j - 1] >= MATCH:
                c.append((best[i - 1][j - 1] + sim[i - 1][j - 1], 'match'))
            if i:
                c.append((best[i - 1][j], 'cut'))
            if j:
                c.append((best[i][j - 1], 'add'))
            best[i][j], back[i][j] = max(c)
    i, j, pairs = n, m, {}
    while i or j:
        op = back[i][j]
        if op == 'match':
            pairs[j - 1] = (i - 1, sim[i - 1][j - 1]); i, j = i - 1, j - 1
        elif op == 'cut':
            i -= 1
        else:
            j -= 1
    return pairs


# --- the merge ------------------------------------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--editor', required=True, type=Path)
    ap.add_argument('--master', required=True, type=Path)
    ap.add_argument('--published', required=True, type=Path)
    ap.add_argument('--out', required=True, type=Path)
    ap.add_argument('--report', required=True, type=Path)
    a = ap.parse_args()
    hi = islands_module()
    rep = {'format': 'substack-merge-v1', 'editor': {'path': str(a.editor), 'sha256': sha(a.editor.read_bytes())},
           'master': {'path': str(a.master), 'sha256': sha(a.master.read_bytes())},
           'published': {'path': str(a.published), 'sha256': sha(a.published.read_bytes())}, 'failures': [], 'notes': []}
    fail = rep['failures'].append
    tmp = Path(tempfile.mkdtemp(prefix='substack-merge-'))
    hi.inventory(a.editor, tmp / 'objects.json')
    hi.freeze(a.editor, tmp / 'editable.html', tmp / 'islands.json')
    objs = json.loads((tmp / 'objects.json').read_text(encoding='utf-8'))['objects']
    types = [o['type'] for o in objs]
    urls = [o.get('canonical_url') for o in objs]
    editable = (tmp / 'editable.html').read_text(encoding='utf-8')
    open_end = editable.index('>') + 1
    close_start = editable.rindex('</div>')
    root_open, inner, root_close = editable[:open_end], editable[open_end:close_start], editable[close_start:]
    eb = top_blocks(inner)
    master, pub = md_blocks(a.master.read_text(encoding='utf-8')), md_blocks(a.published.read_text(encoding='utf-8'))
    gm, gp = island_groups(master, types, urls), island_groups(pub, types, urls)
    for n, ((ms, me), (ps, pe)) in enumerate(zip(gm, gp)):
        if [b['md'] for b in master[ms:me]] != [b['md'] for b in pub[ps:pe]]:
            fail('object %d (%s): the master stands for it differently from the published text: %r vs %r'
                 % (n + 1, types[n], [b['md'][:60] for b in master[ms:me]], [b['md'][:60] for b in pub[ps:pe]]))
    # editor anchors: islands and headings, with their positions in eb
    e_isl = [k for k, b in enumerate(eb) if ISLAND.match(b)]
    assert len(e_isl) == len(objs), 'islands and inventory differ'
    e_head = [k for k, b in enumerate(eb) if re.match(r'<h[1-6]>', b)]
    in_group = lambda gs, k: any(s <= k < e for s, e in gs)
    p_head = [k for k, b in enumerate(pub) if b['kind'] == 'heading' and not in_group(gp, k)]
    m_head = [k for k, b in enumerate(master) if b['kind'] == 'heading' and not in_group(gm, k)]
    if [plain_html(eb[k]) for k in e_head] != [plain_md(pub[k]['md'].lstrip('#')) for k in p_head]:
        fail('the editor\'s headings and the published text\'s differ')
    sm = difflib.SequenceMatcher(None, [plain_md(pub[k]['md'].lstrip('#')) for k in p_head],
                                 [plain_md(master[k]['md'].lstrip('#')) for k in m_head], autojunk=False)
    head_pairs = []   # (editor block, published block, master block) for headings all three share (renames 1:1)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
            for d in range(i2 - i1):
                head_pairs.append((e_head[i1 + d], p_head[i1 + d], m_head[j1 + d]))
                if op == 'replace':
                    rep['notes'].append('heading renamed: %r -> %r' % (pub[p_head[i1 + d]]['md'], master[m_head[j1 + d]]['md']))
        else:
            rep['notes'].append('headings not shared (%s): published %r, master %r' % (
                op, [pub[k]['md'] for k in p_head[i1:i2]], [master[k]['md'] for k in m_head[j1:j2]]))
    anchors = sorted([('island', e_isl[n], gp[n], gm[n], n) for n in range(len(objs))] +
                     [('heading', e, (p, p + 1), (m, m + 1), None) for e, p, m in head_pairs], key=lambda x: x[1])
    # anchor order must agree in all three
    for x, y in zip(anchors, anchors[1:]):
        if not (x[2][1] <= y[2][0] and x[3][1] <= y[3][0]):
            fail('anchors out of order: %r then %r' % (x[:2], y[:2]))
    if rep['failures']:
        return finish(a, rep, None)
    out, carried, merged_words_master = [], [], []
    prev = (-1, (0, 0), (0, 0))
    bounds = [(prev[0], prev[1][1], prev[2][1])] + [(x[1], x[2][1], x[3][1]) for x in anchors]
    starts = [(x[1], x[2][0], x[3][0]) for x in anchors] + [(len(eb), len(pub), len(master))]
    for s in range(len(starts)):
        e0, p0, m0 = bounds[s][0] + 1, bounds[s][1], bounds[s][2]
        e1, p1, m1 = starts[s]
        seg = eb[e0:e1]
        # rules and empty paragraphs at the segment's edges stay with the anchor they touch
        deco = lambda b: b.startswith('<hr') or (b.startswith('<p') and not plain_html(b))
        lead, trail = [], []
        while seg and deco(seg[0]):
            lead.append(seg.pop(0))
        while seg and deco(seg[-1]):
            trail.insert(0, seg.pop())
        if any(deco(b) for b in seg):
            rep['notes'].append('segment %d: a rule or empty paragraph inside the text, dropped with it: %r' % (s, [b[:40] for b in seg if deco(b)]))
        units = []
        for bi, b in enumerate(seg):
            for u in editor_units(b):
                u['lid'] = bi
                units.append(u)
        ptext = [b for b in pub[p0:p1] if b['kind'] in ('para', 'heading')]
        if [u['text'] for u in units] != [plain_md(b['md'].lstrip('#') if b['kind'] == 'heading' else b['md']) for b in ptext]:
            ed = [u['text'][:70] for u in units]
            pt = [plain_md(b['md'])[:70] for b in ptext]
            fail('segment %d: the editor\'s text and the published text differ: %s' % (
                s, list(difflib.unified_diff(pt, ed, lineterm='', n=0))[:12]))
            continue
        mtext = [b for b in master[m0:m1] if b['kind'] in ('para', 'heading')]
        for b in master[m0:m1]:
            if b['kind'] == 'comment':
                rep['notes'].append('segment %d: a comment in the master, not in the merge: %r' % (s, b['md'][:120]))
            elif b['kind'] not in ('para', 'heading'):
                fail('segment %d: a %s marker in the master outside any object: %r' % (s, b['kind'], b['md'][:80]))
        pairs = align([u['text'] for u in units], [plain_md(b['md']) for b in mtext])
        html_blocks, open_list = [], None
        for j, b in enumerate(mtext):
            u = units[pairs[j][0]] if j in pairs else None
            if b['kind'] == 'heading':
                if open_list:
                    html_blocks.append(close_list(open_list)); open_list = None
                html_blocks.append(heading_html(b['md']))
                continue
            frag, how = render_para(b['md'], u)
            if how:
                carried.append({'segment': s, 'how': how, 'master': b['md'][:80]})
            key = (u['list'], u['lid']) if u and u.get('list') else None
            if key is None and open_list:
                # a new paragraph inside a list: it stays in the current item when the list goes on after it
                nxt = next((units[pairs[k][0]] for k in range(j + 1, len(mtext)) if k in pairs), None)
                if nxt and nxt.get('list') and (nxt['list'], nxt['lid']) == open_list['key']:
                    if nxt['item'] == open_list['item']:   # between two paragraphs of one item: it's that item's too
                        open_list['items'][-1].append(frag)
                    else:                                  # in place of an item the master rewrote: an item of its own
                        open_list['items'].append([frag]); open_list['item'] = ('new', j)
                    carried.append({'segment': s, 'how': 'new paragraph kept in the list', 'master': b['md'][:80]})
                    continue
            if key:
                if open_list and open_list['key'] != key:
                    html_blocks.append(close_list(open_list)); open_list = None
                if not open_list:
                    open_list = {'key': key, 'items': [], 'item': None}
                if open_list['item'] != u['item']:
                    open_list['items'].append([]); open_list['item'] = u['item']
                open_list['items'][-1].append(frag)
                carried.append({'segment': s, 'how': 'list item (%s)' % u['list'], 'master': b['md'][:80]})
            else:
                if open_list:
                    html_blocks.append(close_list(open_list)); open_list = None
                html_blocks.append(frag)
        if open_list:
            html_blocks.append(close_list(open_list))
        unaligned = [mtext[j]['md'][:80] for j in range(len(mtext)) if j not in pairs]
        cut = [units[i]['text'][:80] for i in range(len(units)) if i not in {v[0] for v in pairs.values()}]
        if unaligned or cut:
            rep['notes'].append('segment %d: master paragraphs with no published counterpart %r; published ones with none in the master %r'
                                % (s, unaligned, cut))
        out += lead + html_blocks + trail
        merged_words_master += [w for b in mtext for w in words(plain_md(b['md'].lstrip('#') if b['kind'] == 'heading' else b['md']))]
        if s < len(anchors):
            x = anchors[s]
            if x[0] == 'island':
                out.append(eb[x[1]])
            else:
                lv = int(re.match(r'<h([1-6])>', eb[x[1]]).group(1))
                mh = master[x[3][0]]['md']
                if len(re.match(r'^(#+)', mh).group(1)) != lv:
                    rep['notes'].append('heading level: master %r, editor h%d (the editor\'s kept)' % (mh, lv))
                out.append(heading_html(mh, lv))
                merged_words_master += words(plain_md(mh.lstrip('#')))
    if rep['failures']:
        return finish(a, rep, None)
    merged_editable = root_open + ''.join(out) + root_close
    (tmp / 'merged-editable.html').write_text(merged_editable, encoding='utf-8')
    hi.restore(tmp / 'merged-editable.html', a.out, tmp / 'islands.json')
    try:
        hi.verify(a.out, tmp / 'islands.json')
        rep['islands_verify'] = 'PASS: %d islands byte-for-byte and in order' % len(objs)
    except SystemExit as e:
        fail('html_islands verify failed: %s' % e)
    # the merged text, as words, equals the master's text blocks (the objects' own text aside)
    got = [w for b in out if not ISLAND.match(b) for w in words(plain_html(b))]
    if got != merged_words_master:
        d = list(difflib.unified_diff(merged_words_master, got, lineterm='', n=2))[:40]
        fail('the merged text differs from the master\'s: %s' % d)
    else:
        rep['prose_check'] = 'PASS: %d words, the same as the master\'s text blocks, in order' % len(got)
    mlinks = [m.group(2) for b in master if b['kind'] in ('para', 'heading') for m in MD_LINK.finditer(b['md'])]
    merged = a.out.read_text(encoding='utf-8')
    missing = [u for u in mlinks if ('href="%s"' % esc(u)) not in merged]
    if missing:
        fail('links in the master missing from the merge: %r' % missing[:10])
    rep['links'] = {'master_links': len(mlinks), 'missing': missing}
    rep['carried_formatting'] = carried
    rep['objects'] = {'count': len(objs), 'types': types}
    return finish(a, rep, merged)


def close_list(open_list):
    tag = open_list['key'][0]
    return '<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % ''.join(item) for item in open_list['items']), tag)


def finish(a, rep, merged):
    if merged is not None:
        rep['out'] = {'path': str(a.out), 'sha256': sha(merged.encode('utf-8'))}
    rep['verdict'] = 'FAIL' if rep['failures'] else 'PASS'
    a.report.write_text(json.dumps(rep, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('substack_merge:', rep['verdict'], '-', len(rep['failures']), 'failure(s),', len(rep['notes']), 'note(s) ->', a.report)
    for f in rep['failures'][:8]:
        print('  FAIL', f[:400])
    return 1 if rep['failures'] else 0


if __name__ == '__main__':
    sys.exit(main())
