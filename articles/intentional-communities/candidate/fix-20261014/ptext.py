"""ptext.py - the text Pangram reads for a section or paragraph of HUMANIZED-SO-FAR.md (2026-10-14).

A reader's view: headings without their #, links as their text, no emphasis marks, no images, no HTML comments,
paragraphs joined by a blank line (the way earlier batches joined their parts).

  from ptext import section, blocks
  section(article_text, '# The Math of Absorption')   -> the h1 section's text, heading first
  blocks(article_text, '# The Math of Absorption')    -> [(markdown, plain), ...] for that section
"""
import re

LINK = re.compile(r'\[([^\]]+)\]\((?:[^()\s]|\([^()\s]*\))*\)')
IMAGE = re.compile(r'^\[image \d+\]\(')


def plain(md):
    t = re.sub(r'^#{1,6}\s+', '', md.strip())
    t = LINK.sub(r'\1', t).replace('*', '')
    return re.sub(r'[ \t]+', ' ', t).strip()


def blocks(article, h1_start):
    art = re.sub(r'<!--.*?-->', '', article, flags=re.S)
    paras = [p.strip() for p in re.split(r'\n\s*\n', art) if p.strip()]
    i = [n for n, p in enumerate(paras) if p.startswith(h1_start)]
    assert len(i) == 1, (h1_start, len(i))
    out = []
    for p in paras[i[0]:]:
        if out and re.match(r'^# ', p):
            break
        if IMAGE.match(p):
            continue
        out.append((p, plain(p)))
    return out


def section(article, h1_start):
    return '\n\n'.join(t for _, t in blocks(article, h1_start))
