"""article_with.py - the article so far with a section 13 draft in place of the installed section (2026-10-15).

  python3 article_with.py DRAFT.md OUT.md      # from s13/

For whole-article checks (the repeats check, E172) on a draft that isn't installed yet. The draft starts with the section's
own heading, as the vN.md files do.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = '# Your Little Forming Group Already Is the Community'
art = (HERE.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H); b = art.index('\n# ', a + 5)
draft = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8').strip()
assert draft.startswith(H), 'the draft must start with ' + H
pathlib.Path(sys.argv[2]).write_text(art[:a] + draft + '\n' + art[b:], encoding='utf-8')
print(sys.argv[2], len(art[:a].split()) + len(draft.split()) + len(art[b:].split()), 'words')
