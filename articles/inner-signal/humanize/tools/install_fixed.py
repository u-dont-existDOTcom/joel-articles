"""install_fixed.py - a fixed section (FIXED.json) as Markdown, its paragraph checks, and its install (2026-10-18).

A section whose fixed version read 100% Human whole goes into HUMANIZED-SO-FAR.md only when every paragraph also reads
Human alone (tools/humanization/paragraphs_alone.py; Joel's rule of 2026-10-01, "every paragraph passes alone"). The
three steps share one source here, so what is installed is what was checked:

  section_md(fixed)          the section's Markdown: headings and unchanged blocks as the published article has them
                             (links, emphasis, list marks), each Emulate stretch as its fixed paragraphs with the published
                             links put back on their words (a review's "links": the published anchor and its words in the
                             new text). A published link a stretch dropped without a "links" record stops it.
  para_texts(md, seen)       the fewest texts that give every paragraph its check, as paragraphs_alone.check() will look
                             for them (tries_for): alone at 50 words or more, a shorter one with a neighbor under its
                             heading, a list entry still under 50 in the shortest run around it. A paragraph whose check
                             is already in SEEN (texts with a Human result) needs none.
  install(article, fixed)    the article with the section's blocks replaced, every image, embed and button where it was

  python3 tools/install_fixed.py md FIXED.json
  python3 tools/install_fixed.py check FIXED.json BATCH_DIR [BATCH_DIR ...]     paragraphs_alone.py on section_md
  python3 tools/install_fixed.py install ARTICLE.md FIXED.json [...] --out NEW.md

After an install, run fix-20261020/apply_edits41.py: the Pangram 4.1 sentence edits (fix-20261020/EDITS41.json) sit on
top of the installed sections, and it puts back any that a re-install of their section replaced (or stops, naming the
edit, when its section's text changed under it).
"""
import argparse, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
REPO = H.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import assemble as A  # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import sections as S  # noqa: E402
import substack_merge as SM  # noqa: E402

LIST = re.compile(r'^\s*((?:[-*+]|\d+[.)])\s+)')


def unit_md(u, pub_md):
    """The Markdown blocks of one Emulate stretch: its fixed paragraphs, links put back, a published list's marks kept."""
    links = {}
    for m in SM.MD_LINK.finditer(pub_md):
        links.setdefault(S.plain(m.group(1)), m.group(2))
    paras = list(u['paras'])
    used = set()
    for l in u.get('links') or []:
        url = links.get(S.plain(l['published']))
        if url is None:
            raise SystemExit('%s: no published link with the words %r' % (u['blocks'], l['published']))
        for i, p in enumerate(paras):
            if l['new'] in p:
                paras[i] = p.replace(l['new'], '[%s](%s)' % (l['new'], url), 1)
                used.add(S.plain(l['published']))
                break
        else:
            raise SystemExit('%s: the words %r are not in the fixed text' % (u['blocks'], l['new']))
    lost = [a for a in links if a not in used]
    if lost:
        raise SystemExit('stretch B%d: the published link(s) %s are not in the fixed text and no "links" record says where '
                         'they went' % (u['blocks'][0], lost))
    marks = [LIST.match(x).group(1) for x in pub_md.split('\n') if LIST.match(x)]
    out = []
    for p in paras:
        lines = p.split('\n')
        if len(lines) > 1 and marks and len(lines) <= len(marks):
            p = '\n'.join(marks[k] + x.strip() for k, x in enumerate(lines))
        elif len(lines) > 1:
            raise SystemExit('stretch B%d: a paragraph of %d lines and no list to give them marks' % (u['blocks'][0], len(lines)))
        out.append(p)
    return out


def section_units(fixed_path):
    d = json.loads(pathlib.Path(fixed_path).read_text(encoding='utf-8'))
    kbk = A.kb()[d['key']]
    out = []
    for u in d['units']:
        if u['kind'] == 'emulate':
            out.append((u, unit_md(u, '\n\n'.join(kbk[b][0] for b in u['blocks']))))
        else:
            out.append((u, [kbk[b][0] for b in u['blocks']]))
    return d['key'], kbk, out


def section_md(fixed_path):
    return '\n\n'.join(m for _, ms in section_units(fixed_path)[2] for m in ms)


def para_texts(md, seen=()):
    """[(paragraph index, its text, the text to send)] for the paragraphs without a Human check in SEEN, one text each,
    a text that serves several paragraphs listed once (the first paragraph it serves)."""
    paras = PA.paragraphs(md)
    sent, out = set(), []
    for i in range(len(paras)):
        t, tries = PA.tries_for(md, paras, i)
        ok = [x for x in tries if len(x.split()) >= 50]
        if any(x in seen or x in sent for x in tries):
            continue
        if not ok:
            raise SystemExit('paragraph %d (%r): no text of 50 words or more checks it' % (i, t[:60]))
        pick = min(ok, key=lambda x: (len(x.split()), ok.index(x)))
        sent.add(pick)
        out.append((i, t, pick))
    return out


def locate(blocks, kbk, skip):
    """The article's block indexes of a key's published blocks, in order; islands (skip) may sit between them."""
    n = len(kbk)
    for s, b in enumerate(blocks):
        if b['md'] != kbk[0][0]:
            continue
        idx, j = [s], s + 1
        while len(idx) < n and j < len(blocks):
            if blocks[j]['md'] == kbk[len(idx)][0]:
                idx.append(j)
            elif j not in skip and blocks[j]['kind'] != 'comment':
                break
            j += 1
        if len(idx) == n:
            return idx
    return None


def install(article, fixed_paths, editor=None):
    editor = editor or (H / 'source' / 'substack-editor-20260928.html')
    blocks = SM.md_blocks(article)
    skip = S.island_blocks(blocks, editor)
    new = {k: b['md'] for k, b in enumerate(blocks)}
    notes = []
    for f in fixed_paths:
        key, kbk, units = section_units(f)
        idx = locate(blocks, kbk, skip)
        if idx is None:
            raise SystemExit('%s: its published blocks are not all in the article (installed already?)' % key)
        for u, ms in units:
            at = [idx[b] for b in u['blocks']]
            if any(j in skip for j in range(at[0], at[-1] + 1)):
                notes.append('%s B%d: an image or embed inside the stretch now follows it' % (key, u['blocks'][0]))
            new[at[0]] = '\n\n'.join(ms)
            for j in at[1:]:
                new[j] = None
    return '\n\n'.join(v for k, v in sorted(new.items()) if v is not None) + '\n', notes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('md', 'check', 'install'))
    ap.add_argument('args', nargs='+')
    ap.add_argument('--out')
    a = ap.parse_args()
    if a.cmd == 'md':
        print(section_md(a.args[0]))
    elif a.cmd == 'check':
        ok, report = PA.check(section_md(a.args[0]), a.args[1:])
        print('\n'.join(report))
        print('paragraphs_alone: %s' % ('PASS' if ok else 'FAIL'))
        return 0 if ok else 1
    else:
        art = pathlib.Path(a.args[0]).read_text(encoding='utf-8')
        out, notes = install(art, a.args[1:])
        pathlib.Path(a.out or a.args[0]).write_text(out, encoding='utf-8')
        print('installed %d section(s) -> %s' % (len(a.args) - 1, a.out or a.args[0]))
        for n in notes:
            print('  ' + n)
    return 0


if __name__ == '__main__':
    sys.exit(main())
