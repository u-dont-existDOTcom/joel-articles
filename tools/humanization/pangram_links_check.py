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
bare address, which his app shows as text. Addresses inside `code` are a command's text and are left alone. And every
file it points to is a link he can click, never a path in the repository (repo_links.py; Joel, 2026-10-25 00:24 UTC: "i
have no idea where the 3 files are that i'm supposed to read"). A link in it goes to a page he can read, never to a
folder (Joel, 2026-10-25 12:39 UTC, on two folder links in my message: "edit wasn't even a page, it was a directory so i
wasn't sure what that was for").

With --chat, a lane turn's final message (one that ends with a handoff's resume line, "Continue my ... work: on my laptop,
read ~/claude-acceptance-transfer/handoffs/....md") also needs the whole article sent with it: pass each file sent with the
message as --sent FILE, and one of them must be a page from render_article_so_far.py whose article is unchanged since the
page was made (its two <meta> tags name the Markdown and its SHA-256). OWNER-FACING-TURN-CONTRACT.md has asked for that page
every turn since 2026-09-17, the Inner Child handoff note and the renderer said so too, and still the page dropped out of
the turns after a context summary left it out of the routine: Joel, 2026-10-25 21:40 UTC, "idk why you stopped giving me
the full humanized article on each turn" (E271 (Inner Child)). A turn with nothing for him to review, which the contract
lets go without the page, says why with --nothing-to-review "REASON".

  python3 tools/humanization/pangram_links_check.py --chat FINAL.md --sent ARTICLE-PAGE.html [--sent MORE ...]
"""
import hashlib
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from html_links import bare_urls  # noqa: E402
from repo_links import paths as repo_paths  # noqa: E402

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


# A link to a folder on GitHub (its tree view), which shows a list of files, not something to read.
FOLDER_LINK = re.compile(r'\]\((https://github\.com/[^)\s]+/tree/[^)\s]+)\)')


# A help request, and the tell panel record it has to link (E253 (Inner Child)).
HELP = re.compile(r"tells? I'?m missing|help (?:me )?(?:show|find|see)[^.?!]{0,40}\btells?\b|can you help[^.?!]{0,80}\btells?\b", re.I)
PANEL_LINK = re.compile(r'PANEL\.md|t\d+-panel/', re.I)


def unpaneled_help(text):
    """Paragraphs and list items that ask Joel's help with tells and link no tell panel record."""
    return [u for u in units(text) if HELP.search(u) and not PANEL_LINK.search(u)]


# A lane turn's final message ends with the handoff's resume line (UDA cross-account-continuity.md).
RESUME = re.compile(r'Continue my .{1,80}? work: on my laptop, read ~/claude-acceptance-transfer/handoffs/[\w.-]+\.md')
META = re.compile(r'<meta name="article-(source|sha256)" content="([^"]*)">')


def whole_article_gaps(text, sent, root='.'):
    """What's wrong with the whole-article page a lane turn's final message needs (E271 (Inner Child)); [] when it's fine
    or the message doesn't end a lane turn."""
    if not RESUME.search(text):
        return []
    pages, gaps = 0, []
    for f in sent:
        try:
            page = pathlib.Path(f).read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError):
            continue
        meta = dict(META.findall(page))
        if not {'source', 'sha256'} <= set(meta):
            continue
        pages += 1
        src = pathlib.Path(root) / meta['source']
        if not src.is_file():
            gaps.append('the whole-article page %s was made from %s, which isn\'t here' % (f, meta['source']))
        elif hashlib.sha256(src.read_bytes()).hexdigest() != meta['sha256']:
            gaps.append('the whole-article page %s is older than %s: render it again (render_article_so_far.py)' % (f, meta['source']))
    if not pages:
        gaps.append('a lane turn\'s final message with no whole-article page sent: render it (render_article_so_far.py), '
                    'send it, and pass it as --sent PAGE (OWNER-FACING-TURN-CONTRACT.md, E271)')
    return gaps


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
    sent, paths, waive, i = [], [], None, 0
    while i < len(argv):
        if argv[i] == '--sent' and i + 1 < len(argv):
            sent.append(argv[i + 1])
            i += 2
        elif argv[i] == '--nothing-to-review' and i + 1 < len(argv):
            waive = argv[i + 1]
            i += 2
        else:
            if argv[i] != '--chat':
                paths.append(argv[i])
            i += 1
    bad = 0
    for p in paths:
        text = pathlib.Path(p).read_text(encoding='utf-8')
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
            for _, _, _, written in repo_paths(text):
                bad += 1
                print('%s: a path Joel can\'t open (give a link): %s' % (p, written))
            for m in FOLDER_LINK.finditer(text):
                bad += 1
                print('%s: a link to a folder, not a page (link the page he needs, or say what the folder holds): %s'
                      % (p, m.group(1)))
            gaps = whole_article_gaps(text, sent)
            if gaps and waive and waive.strip():
                print('%s: no whole-article page, since there is nothing to review: %s' % (p, waive.strip()))
            else:
                for g in gaps:
                    bad += 1
                    print('%s: %s' % (p, g))
    print('verdict: %s' % ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
