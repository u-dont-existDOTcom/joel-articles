#!/usr/bin/env python3
"""para_numbers.py - one paragraph numbering for every page Joel reads.

Joel, 2026-10-11 03:47 UTC: "Why are there no numbers on many of these paragraphs? how do i identify
them?" The article page had no numbers, and the review page numbered a row only when its label was
typed with one. Both pages now take their numbers from here, so "P3" means the same paragraph on both.

The rule: paragraphs are numbered P1, P2, ... under each heading, starting again at every heading
(of any level). A list that follows a lead-in ending with ":" shares the lead-in's number, as the
review page already treats them as one paragraph. HTML comments are invisible and never numbered.
So "When the Urge to Escape Arrives, P3" is the third paragraph under that heading, the way the
records have always named paragraphs.

  number_blocks(blocks) -> [(block, label_or_None)]   blocks already split on blank lines
"""
import re

HEAD = re.compile(r'^(#{1,6})\s+(.*)$')
LIST_LINE = re.compile(r'^(\d+\.|[-*+]) ', re.M)
COMMENT = re.compile(r'<!--.*?-->', re.S)


def visible(block):
    """A block's text without its HTML comments."""
    return COMMENT.sub('', block).strip()


def number_blocks(blocks):
    """Label each block: 'P<n>' for a paragraph, None for a heading or an invisible block.

    The numbering restarts at every heading. A list block right after a visible block that ends
    with ':' gets None too (it belongs to that lead-in's number)."""
    out, n, prev_visible = [], 0, ''
    for b in blocks:
        v = visible(b)
        if not v:
            out.append((b, None))
            continue
        if HEAD.match(v):
            n, prev_visible = 0, v
            out.append((b, None))
            continue
        if LIST_LINE.match(v) and prev_visible.endswith(':'):
            out.append((b, None))
            prev_visible = v
            continue
        n += 1
        out.append((b, 'P%d' % n))
        prev_visible = v
    return out


def label_for(blocks, i):
    """The P-number of block i (after merging, as number_blocks gives it), or None."""
    return number_blocks(blocks)[i][1] if 0 <= i < len(blocks) else None
