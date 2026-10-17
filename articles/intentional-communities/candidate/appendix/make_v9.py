"""The appendix, draft v9 (2026-10-17): v8 (every run Human, 341g; paragraphs_alone PASS; the whole 100% Human, 0.18; trace,
cold read and stance round r14) with the stance check's one conflict fixed. "If you're curious how I got to all this" makes the
research the route by which the author reached his whole model (review-r14/STANCE-pub.md); the essay presents it as a source
audit that checks claims, and the section's published heading is "Research Behind This Article". So the opening takes the
heading's own words: "If you're curious about the research behind this, it was a much bigger source audit than would
comfortably fit in an article (a lot bigger!)." (round r7's stance check had found no conflict in the same opening; the
published sentence decides.)
Writes v9.md. Run from this folder: python3 make_v9.py"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v8.py')], check=True, capture_output=True)
t = (HERE / 'v8.md').read_text(encoding='utf-8')
OLD = "If you're curious how I got to all this, the research behind it was a much bigger source audit"
NEW = "If you're curious about the research behind this, it was a much bigger source audit"
assert t.count(OLD) == 1
(HERE / 'v9.md').write_text(t.replace(OLD, NEW), encoding='utf-8')
print('wrote v9.md')
