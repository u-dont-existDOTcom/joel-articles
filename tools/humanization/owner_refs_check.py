#!/usr/bin/env python3
"""owner_refs_check.py - file references in a message or page for Joel that he can't open.

Joel, 2026-10-12: "can you stop giving me paths to files that are relative to something? ... i thought i told you always
give me a link to click or a file to look at". The check ran only on final messages, from a worker's scratch folder, so
the hypnosis guide's questions page still named its repeats lists as repo paths in backticks, and on 2026-10-21 17:56 UTC
he answered "i didn't understand about the full lists, because you didn't give links to click". Now it lives here and
runs on the owner pages too (a lane's OWNER-QUESTIONS.md, the page he answers from) before every push that
changes one. A lane's STATUS.md is the workers' log, not a page for him, and keeps its plain paths.

  python3 tools/humanization/owner_refs_check.py FILE.md [FILE.md ...] [--sent NAME ...] [--json]

Lists every path-like reference (a relative or absolute file path, a home-relative path, or a backticked file name)
that is neither a clickable link nor a file sent with the message (--sent takes the sent files' names or paths). A
command in a fenced code block is left alone (it's for running, not for opening). Exit 1 when one is left: link it (for
a file in Git, its github.com/.../blob/BRANCH/PATH address), send it, or name it in plain words.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

EXT = r"(?:md|html?|json|jsonl|py|txt|csv|tsv|pdf|docx?|xlsx?|pptx?|js|ts|ya?ml|toml|sh|png|jpe?g|svg|zip)"
URL = re.compile(r"https?://\S+")
MD_LINK = re.compile(r"\[([^\]]*)\]\([^)\s]+\)")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
BACKTICK = re.compile(r"`([^`\n]+)`")
PATHLIKE = re.compile(
    r"(?<![\w@])("
    r"(?:~|\.{1,2})?/?(?:[\w.\-]+/)+[\w.\-]+(?:\.\w+)?/?"  # dir/sub/file.ext, ~/x/y, ./x, /abs/x
    r"|[\w\-]+(?:\.[\w\-]+)*\." + EXT +  # file.ext on its own
    r")(?![\w])"
)


def refs(text: str) -> list[str]:
    """Path-like strings in the text that aren't links, fenced commands or a link's own words."""
    body = FENCE.sub(" ", text)
    body = MD_LINK.sub(lambda m: " " if PATHLIKE.search(m.group(1)) else m.group(1), body)
    body = URL.sub(" ", body)
    found = []
    for m in BACKTICK.finditer(body):
        inner = m.group(1).strip()
        if PATHLIKE.fullmatch(inner) and ("/" in inner or re.search(r"\." + EXT + r"$", inner)):
            found.append(inner)
    plain = BACKTICK.sub(" ", body)
    for m in PATHLIKE.finditer(plain):
        tok = m.group(1).rstrip(".,;:)")
        if "/" in tok and re.search(r"[A-Za-z]", tok) and not re.fullmatch(r"\d+/\d+(?:/\d+)?", tok) and not tok.endswith("/"):
            if re.search(r"\.\w{1,5}$", tok) or tok.startswith(("~/", "./", "../", "/")):
                found.append(tok)
        elif "/" not in tok and re.search(r"\." + EXT + r"$", tok):
            found.append(tok)
    out = []
    for f in found:
        if f not in out:
            out.append(f)
    return out


def unresolved(text: str, sent: list[str]) -> list[str]:
    names = {pathlib.PurePosixPath(s).name for s in sent}
    return [r for r in refs(text) if pathlib.PurePosixPath(r.rstrip("/")).name not in names]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--sent", action="append", default=[], help="a file sent with the message (name or path)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    left = {}
    for f in a.files:
        u = unresolved(pathlib.Path(f).read_text(encoding="utf-8"), a.sent)
        if u:
            left[f] = u
    if a.json:
        print(json.dumps({"unresolved": left}, ensure_ascii=False))
    else:
        for f, u in left.items():
            for r in u:
                print("%s: NOT OPENABLE: %s (link it, send it, or name it in plain words)" % (f, r))
        print("verdict: %s" % ("FAIL" if left else "PASS"))
    return 1 if left else 0


if __name__ == "__main__":
    sys.exit(main())
