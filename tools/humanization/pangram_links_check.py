"""pangram_links_check.py - a message to Joel that reports a Pangram result as AI gives the check's link.

Usage (from the repo root):
  python3 tools/humanization/pangram_links_check.py MESSAGE.md [MORE.md ...]

Joel, 2026-10-15 09:33 UTC, after trying to reproduce a pair I had told him read AI ("27 i actually could not
reproduce the pangram failure on this part, so there's nothing to change. for future reference, give me the
pangram check links when you tell me to check something on pangram"). The questions page had said "reads AI beside
the reparenting paragraph before it ... (278g, a control)" with no link to the check, so he couldn't see what was
tested (E171 already asked for the link on a flag; nothing checked that it was there).

A paragraph or list item that reports an AI result (reads AI, read AI, AI-Generated, AI Detected, an AI window,
Mostly Human) needs a https://www.pangram.com/history/ link in the same paragraph or item. Prints each one that
doesn't have one, and exits 1 if there are any. Passing results can point to the turn's results file, which lists
each check's link.
"""
import re
import sys

AI_RESULT = re.compile(r'\b(?:reads?|reading|read as)\s+(?:as\s+)?AI\b|\bAI[- ](?:Generated|Detected|window)\b|'
                       r'\bMostly Human\b|\bAI-generated\b', re.I)
LINK = 'pangram.com/history/'


def units(text):
    """Paragraphs and list items: a blank line or a new list item starts the next one."""
    out, cur = [], []
    for line in text.split('\n'):
        if not line.strip() or re.match(r'\s*(?:[-*+]|\d+[.)])\s', line):
            if cur:
                out.append(' '.join(cur))
            cur = [line.strip()] if line.strip() else []
        else:
            cur.append(line.strip())
    if cur:
        out.append(' '.join(cur))
    return out


def missing(text):
    return [u for u in units(text) if AI_RESULT.search(u) and LINK not in u]


def main(paths):
    bad = 0
    for p in paths:
        for u in missing(open(p, encoding='utf-8').read()):
            bad += 1
            print('%s: an AI result with no Pangram check link: %s' % (p, u[:200]))
    print('verdict: %s' % ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
