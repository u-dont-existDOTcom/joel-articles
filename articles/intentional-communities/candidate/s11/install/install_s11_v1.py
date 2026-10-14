"""Replace the published section 11 in HUMANIZED-SO-FAR.md with section 11 v8 (a candidate). Run from candidate/.
The article must still hold the published section exactly as in ../original.md; otherwise this stops."""
import pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
orig = (C.parent / 'original.md').read_text(encoding='utf-8')
v8 = (C / 's11/section-v8.md').read_text(encoding='utf-8').strip()
H, NEXT = '# Founderism: The Four Questions', '# The Math of Absorption'
i = art.index(H)
k = art.index(NEXT, i)
a = orig.index(H)
b = orig.index(NEXT, a)
assert art[i:k].strip() == orig[a:b].strip(), 'the article does not hold the published section 11; stop'
note = ('<!-- CANDIDATE: section 11 v8 (2026-10-10), under Joel\'s "continue" of 15:23 UTC. Pangram web app (the final '
        'test): the section 100% Human (1,004 words scanned, 18:02:27 UTC, batch 227g); the published section read 100% AI '
        '(201g). Every paragraph passes alone or beside a neighbor that passes alone. Gate: stance ledger s11, linter '
        '(REVIEW, no FAIL), three rounds of traces, cold reads and whole-article stance checks (review-a1 to a3, with '
        'dispositions). Kept for Joel, with tries counted: P8 "even just general reputation" (2), P15 "a lot of" (5), '
        'P15 "things … it … the gatekeepers" (5). Records: s11/PREDICTIONS-s11.md (201g to 227g), s11/section-v8.md, '
        's11/candidate-v8-keys.json, s11/fix-v1-parts.json to fix-v19-parts.json, s11/review-a1 to a3. '
        'Not accepted until Joel says so. -->\n')
art = art[:i] + note + v8 + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 11 v8')
