"""UPDATE-PLAN.json, for update.js and dispatch.js: Joel's "33a" of 2026-11-03 13:46 UTC, the guide (HUMANIZED-SO-FAR.md 010b9fc3) into
his post 202810155, the way it went in on 2 November (../../fix-20261102/live/record_live.py): the archival HTML parsed
with the editor's own schema, one transaction, no paste, the top image he removed (fdb94728) left out, the post's own
six native blocks (Subscribe, Share, the YouTube video, the image, the two post embeds) carried over as they are.

On 2 November the editor took the whole document (ARCHIVAL-20261102.html, the same 28 September editor copy merged with
the guide a789009c). Its 730 top-level blocks, less the top image, are the editor's 729 nodes. Today's merge
(ARCHIVAL-20261103.html, MERGE-REPORT.json PASS) has 721. The two are compared block by block here: the blocks that are
the same byte for byte parse to the same nodes, so the editor keeps those nodes as they are, and only the changed ranges
are replaced, each with today's blocks parsed by the editor's own parser, all in one transaction. update.js first checks
every one of the editor's 729 nodes against the 2 November blocks (the text of each, without whitespace, as a short
SHA-256; the native blocks by type), so nothing he changed in the draft since is overwritten; then it builds the
transaction and checks the result node by node against today's 720 blocks before anything is dispatched.

  python3 articles/inner-signal/humanize/fix-20261103/live/make_update.py
"""
import difflib
import hashlib
import html
import json
import pathlib
import re
from html.parser import HTMLParser

HERE = pathlib.Path(__file__).resolve().parent
OLD = HERE.parents[1] / 'fix-20261102' / 'live' / 'ARCHIVAL-20261102.html'
NEW = HERE / 'ARCHIVAL-20261103.html'
VOID = {'br', 'img', 'hr', 'source', 'input', 'meta', 'link', 'wbr'}
# Whitespace, by code point (the same list as update.js's WS): every whitespace character either language's \s knows.
WS = frozenset(map(chr, [0x20, 0x09, 0x0a, 0x0d, 0x0c, 0x0b, 0x85, 0xa0, 0x1680, 0x2028, 0x2029, 0x202f, 0x205f, 0x3000,
                         0xfeff, 0x1c, 0x1d, 0x1e, 0x1f] + list(range(0x2000, 0x200b))))
TOP_IMAGE = 1   # the image at the top, fdb94728, which he removed from the post before 2 November


class Top(HTMLParser):
    """The top-level blocks inside the editor's wrapper <div>, as their exact source strings."""

    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src, self.depth, self.blocks, self.start = src, 0, [], None
        self.lines = [0] + [m.end() for m in re.finditer('\n', src)]

    def off(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        o = self.off()
        if tag in VOID:
            if self.depth == 1:
                self.blocks.append(self.src[o:o + len(self.get_starttag_text())])
            return
        if self.depth == 1:
            self.start = o
        self.depth += 1

    def handle_startendtag(self, tag, attrs):
        if self.depth == 1:
            o = self.off()
            self.blocks.append(self.src[o:o + len(self.get_starttag_text())])

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        self.depth -= 1
        if self.depth == 1:
            self.blocks.append(self.src[self.start:self.src.find('>', self.off()) + 1])

    def handle_data(self, data):
        if self.depth == 1 and data.strip():
            raise ValueError('text at the top level: %r' % data[:80])


def split(src):
    p = Top(src)
    p.feed(src)
    p.close()
    head = src[:src.find('>') + 1]
    assert p.depth == 0 and head.startswith('<div') and src.endswith('</div>')
    assert ''.join(p.blocks) == src[len(head):-len('</div>')], 'the blocks do not rejoin to the body'
    return p.blocks


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def text(block):
    t = Text()
    t.feed(block)
    t.close()
    return ''.join(t.parts)


def native(block):
    """The editor's node type for a native block (compared by type, since its DOM shows text its node doesn't hold)."""
    head = block[:300]
    if 'class="captioned-image-container"' in head and block.startswith('<div'):
        return 'captionedImage'
    if 'class="button-wrapper"' in head:
        return 'button'
    if 'class="youtube-wrap"' in head:
        return 'youtube2'
    if 'class="digest-post-embed"' in head:
        return 'digestPostEmbed'
    if block.startswith('<blockquote><div class="captioned-image-container"'):
        return 'blockquote'   # his quote around an image: the image's DOM has its own text; by type
    return None


def sig(block):
    t = native(block)
    if t:
        return 't:' + t
    return hashlib.sha256(''.join(c for c in text(block) if c not in WS).encode('utf-8')).hexdigest()[:6]


def main():
    old = split(OLD.read_text(encoding='utf-8'))
    new = split(NEW.read_text(encoding='utf-8'))
    assert 'fdb94728' in old[TOP_IMAGE] and 'fdb94728' in new[TOP_IMAGE]
    assert old[:TOP_IMAGE + 1] == new[:TOP_IMAGE + 1]
    ed_old = old[:TOP_IMAGE] + old[TOP_IMAGE + 1:]      # the editor's nodes now
    ed_new = new[:TOP_IMAGE] + new[TOP_IMAGE + 1:]      # the editor's nodes after
    ops = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=ed_old, b=ed_new, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        for b in ed_old[i1:i2] + ed_new[j1:j2]:
            assert not native(b), 'a native block in a changed range: %s' % b[:120]
        ops.append({'e1': i1, 'e2': i2, 'n': j2 - j1, 'html': ''.join(ed_new[j1:j2])})
    plan = {'about': __doc__.split('\n\n')[0].replace('\n', ' '),
            'old': {'file': str(OLD.relative_to(HERE.parents[4])), 'sha256': hashlib.sha256(OLD.read_bytes()).hexdigest()},
            'new': {'file': str(NEW.relative_to(HERE.parents[4])), 'sha256': hashlib.sha256(NEW.read_bytes()).hexdigest()},
            'base': [sig(b) for b in ed_old], 'after': [sig(b) for b in ed_new], 'ops': ops}
    (HERE / 'UPDATE-PLAN.json').write_text(json.dumps(plan, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
    print('editor nodes', len(ed_old), '->', len(ed_new), '| changed ranges', len(ops),
          '| nodes out', sum(o['e2'] - o['e1'] for o in ops), '| in', sum(o['n'] for o in ops),
          '| html', sum(len(o['html']) for o in ops), 'chars')


if __name__ == '__main__':
    main()
