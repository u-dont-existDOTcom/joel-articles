"""pangram_links_check.py - a message to Joel that reports a Pangram result as AI gives the check's link.

Usage (from the repo root):
  python3 tools/humanization/pangram_links_check.py MESSAGE.md [MORE.md ...]

Joel, 2026-10-15 09:33 UTC, after trying to reproduce a pair I had told him read AI ("27 i actually could not
reproduce the pangram failure on this part, so there's nothing to change. for future reference, give me the
pangram check links when you tell me to check something on pangram"). The questions page had said "reads AI beside
the reparenting paragraph before it ... (278g, a control)" with no link to the check, so he couldn't see what was
tested (E171 already asked for the link on a flag; nothing checked that it was there).

A paragraph or list item that reports an AI result (reads AI, read AI, AI-Generated, AI Detected, an AI window,
Mostly Human) needs a https://www.pangram.com/history/ link (or a https://www.pangram.com/feed/ link, for a check of a
Substack post) in the same paragraph or item. Prints each one that
doesn't have one, and exits 1 if there are any. Passing results can point to the turn's results file, which lists
each check's link.

A help request (asking Joel to show me the tells I'm missing) needs a link to the tell panel's record, a PANEL.md made by
tell_panel.py, in the same paragraph or item. Joel, 2026-10-23 23:21 UTC, after I asked his help on a paragraph whose tells
three fresh readers found at once: "so why don't you fix your process before asking for help" (E253 (Inner Child)).

With --chat (a message for the chat, not a page), every address must also be one Joel can click: written as
[text](url). Joel, 2026-10-16 21:05 UTC: "(your links are not clickable btw)"; my final message had given each check as a
bare address, which his app shows as text. Addresses inside `code` are a command's text and are left alone.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from html_links import bare_urls  # noqa: E402

# A result word Pangram itself shows, or "reads AI" where the unit is about a check (a batch name, Pangram, a %).
# "a list of three reads AI" (a rule, not a result) isn't one.
RESULT_WORDS = re.compile(r'\bAI[- ](?:Generated|Detected|window)\b|\bMostly Human\b|\bAI-generated\b', re.I)
READS_AI = re.compile(r'\b(?:reads?|reading|read as)\s+(?:as\s+)?AI\b', re.I)
CHECK_CONTEXT = re.compile(r'\bPangram\b|\b\d{3}g\b|\d+%', re.I)
# A check's page: its History entry, or (2026-10-20) the page of Pangram's check of a Substack post, which isn't in the
# History list (the hypnosis guide's whole-guide check through a temporary Substack post: pangram.com/feed/<uuid>).
# An API check (Joel's key, E218) has no Pangram page, so its link is its heading on the batch's API-CHECKS.md page in the
# repository (E214; 2026-10-23: the hypnosis guide's b472 and Nibbāna's n1).
LINKS = ('pangram.com/history/', 'pangram.com/feed/', '/API-CHECKS.md#')


# A help request, and the tell panel record it has to link (E253 (Inner Child)).
HELP = re.compile(r"tells? I'?m missing|help (?:me )?(?:show|find|see)[^.?!]{0,40}\btells?\b|can you help[^.?!]{0,80}\btells?\b", re.I)
PANEL_LINK = re.compile(r'PANEL\.md|t\d+-panel/', re.I)


def unpaneled_help(text):
    """Paragraphs and list items that ask Joel's help with tells and link no tell panel record."""
    return [u for u in units(text) if HELP.search(u) and not PANEL_LINK.search(u)]


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
    return [u for u in units(text)
            if not any(k in u for k in LINKS) and (RESULT_WORDS.search(u) or (READS_AI.search(u) and CHECK_CONTEXT.search(u)))]


def main(argv):
    chat = '--chat' in argv
    paths = [a for a in argv if a != '--chat']
    bad = 0
    for p in paths:
        text = open(p, encoding='utf-8').read()
        for u in missing(text):
            bad += 1
            print('%s: an AI result with no Pangram check link: %s' % (p, u[:200]))
        for u in unpaneled_help(text):
            bad += 1
            print('%s: a help request with no tell panel record (tell_panel.py, E253): %s' % (p, u[:200]))
        if chat:
            for url in bare_urls(text):
                bad += 1
                print('%s: a link Joel can\'t click (write it as [text](url)): %s' % (p, url))
    print('verdict: %s' % ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
