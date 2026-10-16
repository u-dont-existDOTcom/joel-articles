"""Section 13 draft v31 (2026-10-16): v30a (make_v30v.py), that is v30 with H1-P4 as in v29. v30, with all of round r19's fixes,
read AI over two windows (310g); v30a, the same without the two H1-P4 fixes (T1-1's ", if you have any?" and T1-3's "gets
exhausted"), read 100% Human as a whole (311g, AI likelihood 0.10), while putting back H2-P4 or H2-P3b alone left the windows
(v30b, v30d). The two H1-P4 findings are kept with their reasons in review-r19/DISPOSITIONS-r19.md. Run from this folder:
python3 make_v31.py"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
(HERE / 'v31.md').write_text((HERE / 'v30a.md').read_text(encoding='utf-8'), encoding='utf-8')
print('v31 = v30a')
