"""Part B of the hypnosis guide's Substack check (2026-10-20): the archival HTML from the "Appendices" heading to the end.

The first check (RESULT-41a.json) read only the first 99,999 characters of the post, 18,391 of its 26,853 words, and
stopped inside Appendix B's first pattern: the limit of Pangram's check on a Substack post. Part B is the rest, starting
at "Appendices" so that Appendix A and the start of Appendix B are read in both checks. It is cut from the archival HTML
at a top-level block of the editor body, by raw-string slicing (no parse and reserialization), so every native object in
it is carried byte for byte; the canonical generator then builds its copy page as for the whole.

  python3 articles/inner-signal/humanize/fix-20261020/substack41/make_part_b.py   (from the repo root)
"""
import hashlib, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_merge as SM

X = pathlib.Path(__file__).resolve().parent
src = (X / 'ARCHIVAL-SUBSTACK-20261020.html').read_text(encoding='utf-8')
open_end = src.index('>') + 1
close_start = src.rindex('</div>')
root_open, inner, root_close = src[:open_end], src[open_end:close_start], src[close_start:]
blocks = SM.top_blocks(inner)
assert ''.join(blocks) == inner, 'the editor body did not split into its top-level blocks exactly'
k = blocks.index('<h1>Appendices</h1>')
out = root_open + ''.join(blocks[k:]) + root_close
(X / 'ARCHIVAL-SUBSTACK-20261020-B.html').write_text(out, encoding='utf-8')
print('part B: blocks %d to %d of %d; %d characters of HTML; sha256 %s' % (
    k, len(blocks), len(blocks), len(out), hashlib.sha256(out.encode('utf-8')).hexdigest()[:12]))
