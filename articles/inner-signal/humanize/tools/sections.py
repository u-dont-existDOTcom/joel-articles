"""sections.py - the hypnosis guide's h1 sections as Pangram reads them (2026-10-18).

The working copy (HUMANIZED-SO-FAR.md) is Markdown converted from Joel's Substack editor HTML, with markers standing for the
native objects (images, Share, Subscribe, the YouTube video, the two post embeds and their card text). Those markers aren't his
article text, so the plain text skips them: the editor HTML's own inventory (project-sources/html_islands.py.txt) says which
objects there are, and tools/humanization/substack_merge.py's island_groups() finds each one's markers in the Markdown, the
same way the merge does. Headings lose their #, links keep their words, emphasis marks go.

  from sections import sections, text_of
  sections(markdown_text, editor_html_path) -> [(heading, [(markdown_block, plain_block), ...]), ...]
  text_of(blocks) -> the text Pangram reads for those blocks
"""
import json, re, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_merge as SM  # noqa: E402


def plain(md):
    t = re.sub(r'^#{1,6}\s+', '', md.strip())
    t = re.sub(r'(?m)^>\s?', '', t)  # a blockquote's marks aren't text
    t = SM.MD_LINK.sub(lambda m: m.group(1), t).replace('*', '')
    return re.sub(r'[ \t]+', ' ', t).strip()


def island_blocks(blocks, editor_html):
    hi = SM.islands_module()
    tmp = Path(tempfile.mkdtemp())
    hi.inventory(Path(editor_html), tmp / 'objects.json')
    objs = json.loads((tmp / 'objects.json').read_text(encoding='utf-8'))['objects']
    groups = SM.island_groups(blocks, [o['type'] for o in objs], [o.get('canonical_url') for o in objs])
    return {k for s, e in groups for k in range(s, e)}


LIST = re.compile(r'(?m)^\s*(?:[-*+]|\d+[.)])\s+')


def text_of(blocks):
    """The text Pangram reads for these (markdown, plain) blocks: paragraphs joined by a blank line, list marks taken off
    (copying a list from the page gives its items' words, not its bullets or numbers)."""
    return '\n\n'.join(LIST.sub('', p) for _, p in blocks)


def sections(md, editor_html):
    """[(heading, [(markdown_block, plain_block), ...]), ...]: the h1 sections, heading block first. Text before the first
    h1 (the guide's opening line) comes first with heading None."""
    blocks = SM.md_blocks(md)
    skip = island_blocks(blocks, editor_html)
    out, cur = [], None
    for k, b in enumerate(blocks):
        if k in skip or b['kind'] == 'comment':
            continue
        if b['kind'] == 'heading' and re.match(r'^# ', b['md']):
            cur = (b['md'], [(b['md'], plain(b['md']))])
            out.append(cur)
        else:
            if cur is None:
                cur = (None, [])
                out.append(cur)
            cur[1].append((b['md'], plain(b['md'])))
    return out
