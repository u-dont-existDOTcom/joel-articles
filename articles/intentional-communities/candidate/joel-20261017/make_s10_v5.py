"""Section 10 v5 (2026-10-17): v4 as installed (s10-v4-installed.md, cut from HUMANIZED-SO-FAR.md) with question 36 a, Joel's
pick at 02:07 UTC ("36a"): "(with private details protected)" after "store the full case history" in the last paragraph, his
text of 2026-10-14. A reader had pointed out that "what happened", kept in full, could expose the people in an intimate case
(a sexual boundary violation, a child's report, a health crisis). My wording, his pick. Writes s10-v5.md. Run from this
folder: python3 make_s10_v5.py"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 's10-v4-installed.md').read_text(encoding='utf-8')
OLD = "it's best practice to store the full case history so it can be re-evaluated in future"
NEW = "it's best practice to store the full case history (with private details protected) so it can be re-evaluated in future"
assert t.count(OLD) == 1
(HERE / 's10-v5.md').write_text(t.replace(OLD, NEW), encoding='utf-8')
print('wrote s10-v5.md')
