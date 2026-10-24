"""Change the words of one paragraph of Substack editor HTML and keep its links, italics and bold on the same words.

The method of Nibbāna's batch n8 (articles/nibbana/humanize/fix-20261024/n8/gpt_2024.py, Joel's GPT edit of 2026-10-24),
made a shared tool for any edit given as plain text: the community article's caveat cuts (his answers to 64, 2026-10-24
19:52 UTC) were the second use. The paragraph's text is diffed word by word (punctuation and spaces apart) against the new
text, and each changed stretch is replaced in place: a tag outside a stretch stays where it was, a tag inside one goes on
the same words in the new text (or is dropped, and returned, when they're gone), and a tag that crosses a stretch's edge
grows or shrinks with it (returned as moved).

  set_text(inner_html, new_text) -> (new_inner_html, dropped, moved)
  paragraphs(html) -> [(start, end, inner_start, inner_end, plain_text)] for each <p> and <li><p>
"""
import difflib
import html
import re

VOID = {'img', 'wbr', 'hr', 'input', 'source'}


class Inline:
    """A paragraph's inner HTML as plain text with the positions of its inline tags."""

    def __init__(self, inner):
        spans, out, stack, pos = [], [], [], 0
        for m in re.finditer(r'<(/?)(\w+)[^>]*>|([^<]+)', inner):
            if m.group(3) is not None:
                t = html.unescape(m.group(3))
                out.append(t)
                pos += len(t)
            elif m.group(2) == 'br':
                raise ValueError('a line break inside the paragraph')
            elif m.group(2) in VOID:
                raise ValueError('a %s inside the paragraph' % m.group(2))
            elif not m.group(1):
                stack.append((m.group(0), m.group(2), pos, len(spans) + len(stack)))
            else:
                open_tag, name, start, order = stack.pop()
                assert name == m.group(2), (name, m.group(2))
                spans.append((order, [start, pos, open_tag, '</%s>' % name]))
        assert not stack
        # in the order they opened, so two tags on the same words come out nested as they were
        self.spans = [s for _o, s in sorted(spans, key=lambda x: x[0])]
        self.text = ''.join(out)

    def html(self):
        # Tags that close at one place close in the reverse of the order they opened, so nesting is kept
        events = []
        for n, (a, b, o, c) in enumerate(self.spans):
            events.append(((a, 1, -b, n), o))
            events.append(((b, 0, -a, -n), c))
        events.sort(key=lambda e: e[0])
        out, last = [], 0
        for (p, _k, _x, _n), tag in events:
            out.append(html.escape(self.text[last:p], quote=False))
            out.append(tag)
            last = p
        out.append(html.escape(self.text[last:], quote=False))
        return ''.join(out)

    def replace_span(self, i, j, new, moved):
        """The stretch text[i:j] becomes NEW; returns the tags dropped with their words."""
        d = len(new) - (j - i)
        dropped, kept = [], []
        for s in self.spans:
            a, b, o, c = s
            if b <= i:
                kept.append(s)
            elif a >= j:
                kept.append([a + d, b + d, o, c])
            elif a >= i and b <= j:
                words = self.text[a:b]
                k = new.find(words)
                if k >= 0 and new.count(words) == 1:
                    kept.append([i + k, i + k + len(words), o, c])
                else:
                    dropped.append(o + words + c)
            elif a <= i and b >= j:
                kept.append([a, b + d, o, c])
            elif a > i:
                kept.append([i, b + d, o, c])
                moved.append('%s now starts at "%s"' % (o, new[:40]))
            else:
                kept.append([a, i + len(new), o, c])
                moved.append('%s now ends at "%s"' % (o, new[-40:]))
        self.text = self.text[:i] + new + self.text[j:]
        self.spans = kept
        return dropped


def tokens(s):
    return [(m.group(0), m.start()) for m in re.finditer(r'\w+|[^\w\s]|\s+', s)]


def set_text(inner, new_text):
    """INNER (a paragraph's inner HTML) with its text made NEW_TEXT, change by change; trailing line breaks stay."""
    tail = re.search(r'(?:<br\b[^>]*>\s*)+$', inner)
    suffix = tail.group(0) if tail else ''
    p = Inline(inner[:len(inner) - len(suffix)])
    cur = p.text
    ta, tb = tokens(cur), tokens(new_text)
    dropped, moved = [], []
    ops = difflib.SequenceMatcher(None, [t for t, _ in ta], [t for t, _ in tb], autojunk=False).get_opcodes()
    for op, i1, i2, j1, j2 in reversed(ops):
        if op == 'equal':
            continue
        i = ta[i1][1] if i1 < len(ta) else len(cur)
        j = ta[i2 - 1][1] + len(ta[i2 - 1][0]) if i2 > i1 else i
        dropped += p.replace_span(i, j, ''.join(t for t, _ in tb[j1:j2]), moved)
    assert p.text == new_text, ('the text did not come out as asked', p.text[:80], new_text[:80])
    return p.html() + suffix, dropped, moved


def paragraphs(doc):
    """(start, end, inner_start, inner_end, plain text) of each <p>...</p> in DOC."""
    out = []
    for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', doc, re.S):
        plain = html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
        out.append((m.start(), m.end(), m.start(1), m.end(1), plain))
    return out
