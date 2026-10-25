"""repo_links.py - a document or message for Joel points to files with links he can click, never repository paths.

Usage (from the repo root):
  python3 tools/humanization/repo_links.py check FILE [FILE ...]
  python3 tools/humanization/repo_links.py fix FILE [FILE ...] [--branch BRANCH]

Joel, 2026-10-25 00:24 UTC, on ENGAGING.md (sent to him in turn 106): "ok i checked engaging doc" but i have no idea where
the 3 files are that i'm supposed to read...". It pointed to `../t102-safety/BOOKS.md`, `caveats/`, `edit/` and
`IDEAS.md`, paths inside the repository that his app shows as text. AGENTS.md already said "Every file or document you
point him to is a file you send or a link he can click, never a repository path", and nothing checked it.

A path is a `code` span without spaces that names a file or a folder (it ends in one of the extensions below, or in a
slash), or a bare word that ends in one of those extensions. Paths inside a link (its words or its address), a fenced
code block, an HTML comment, a quote, or a `code` span with spaces (a command) are left alone, and so are web addresses.

check prints each path and exits 1 if there are any. fix turns each path it can find into a link to the file on GitHub
(the lane branch unless --branch names another), resolved against the document's folder, then the repository root, then
the article folder the document is in (articles/<id>/); a path it can't find stays, and check still reports it.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
REPO = 'https://github.com/u-dont-existDOTcom/joel-articles'
BRANCH = 'handoff/claude-dangerous-adult-20260924-1631'
EXT = r'(?:md|json|jsonl|py|txt|html|csv|png|js)'
CODE_PATH = re.compile(r'`((?:\.{1,2}/)*[\w.@+-]+(?:/[\w.@+-]+)*(?:\.' + EXT + r'|/))`')
BARE_PATH = re.compile(r'(?<![\w/.:@`#-])((?:\.{1,2}/)*(?:[\w@+-][\w.@+-]*/)*[\w@+-][\w.@+-]*\.' + EXT + r')(?![\w/-])')
SKIP = [re.compile(r'```.*?```', re.S), re.compile(r'<!--.*?-->', re.S),
        re.compile(r'\[[^\]\n]*\]\([^)\s]*(?:\([^)\s]*\)[^)\s]*)*\)'),     # a link: its words and its address
        re.compile(r'<https?://[^>]*>'), re.compile(r'https?://\S+'), re.compile(r'www\.\S+'),
        re.compile(r'"[^"\n]*"|“[^”\n]*”')]                               # a quote: someone's words, not a pointer
CODE_SPAN = re.compile(r'`[^`\n]*`')


def _mask(text):
    """The text with every place a path is allowed blanked out (same length, so positions hold)."""
    out = text
    for rx in SKIP:
        out = rx.sub(lambda m: ' ' * len(m.group(0)), out)
    # code spans pair up left to right; one with a space in it is a command, which may name paths
    return CODE_SPAN.sub(lambda m: ' ' * len(m.group(0)) if re.search(r'\s', m.group(0)) else m.group(0), out)


def paths(text):
    """[(start, end, path, written)]: each path a reader can't open; written is what's on the page (with its backticks)."""
    masked, found = _mask(text), []
    for m in CODE_PATH.finditer(masked):
        found.append((m.start(), m.end(), m.group(1), m.group(0)))
    taken = [(a, b) for a, b, _, _ in found]
    for m in BARE_PATH.finditer(masked):
        if not any(a <= m.start() < b for a, b in taken):
            found.append((m.start(1), m.end(1), m.group(1), m.group(1)))
    return sorted(found)


def resolve(path, doc):
    """The repository path a document's path names, or None."""
    doc = pathlib.Path(doc).resolve()
    bases = [doc.parent, ROOT]
    parts = doc.relative_to(ROOT).parts if ROOT in doc.parents else ()
    if len(parts) > 2 and parts[0] == 'articles':
        bases.append(ROOT / 'articles' / parts[1])
    for base in bases:
        p = (base / path).resolve()
        if p.exists() and ROOT in p.parents:
            return p.relative_to(ROOT).as_posix() + ('/' if p.is_dir() else '')
    return None


def link(path, doc, branch=BRANCH):
    """The markdown link for a path, or None when it doesn't resolve."""
    rel = resolve(path, doc)
    if rel is None:
        return None
    words = re.sub(r'^(?:\.{1,2}/)+', '', path)
    return '[%s](%s/%s/%s/%s)' % (words, REPO, 'tree' if rel.endswith('/') else 'blob', branch, rel.rstrip('/'))


def fix(text, doc, branch=BRANCH):
    out, last = [], 0
    for a, b, path, _ in paths(text):
        md = link(path, doc, branch)
        if md:
            out += [text[last:a], md]
            last = b
    return ''.join(out) + text[last:]


def main(argv):
    if len(argv) < 2 or argv[0] not in ('check', 'fix'):
        print(__doc__)
        return 2
    branch = BRANCH
    if '--branch' in argv:
        k = argv.index('--branch')
        branch = argv[k + 1]
        argv = argv[:k] + argv[k + 2:]
    bad = 0
    for f in argv[1:]:
        text = pathlib.Path(f).read_text(encoding='utf-8')
        if argv[0] == 'fix':
            new = fix(text, f, branch)
            if new != text:
                pathlib.Path(f).write_text(new, encoding='utf-8')
                print('%s: linked %d path(s)' % (f, len(paths(text)) - len(paths(new))))
            text = new
        for a, _, path, written in paths(text):
            bad += 1
            line = text.count('\n', 0, a) + 1
            print('%s:%d: a path Joel can\'t open (give a link): %s' % (f, line, written))
    print('verdict: %s' % ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
