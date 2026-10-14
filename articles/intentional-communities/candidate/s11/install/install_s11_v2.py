"""Replace section 11 v8 in HUMANIZED-SO-FAR.md with section 11 v10 (a candidate). Run from candidate/.
v10 = v8 with Joel's answers of 2026-10-11 02:57 UTC: his P10j after P10, P18z (his 5A), P19t (his 6A)."""
import pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v8 = (C / 's11/section-v8.md').read_text(encoding='utf-8').strip()
v10 = (C / 's11/section-v10.md').read_text(encoding='utf-8').strip()
i = art.index('<!-- CANDIDATE: section 11 v8')
j = art.index('-->\n', i) + 4
k = art.index('# The Math of Absorption', j)
assert art[j:k].strip() == v8, 'the article does not hold section 11 v8; stop'
note = ('<!-- CANDIDATE: section 11 v10 (2026-10-11), Joel\'s answers of 02:57 UTC in: 1 to 3 A (kept items stay), '
        'his own paragraph after P10 on land and admission (P10j, typos fixed only, his straight apostrophes kept), '
        'P18 "the prerequisites for it are a ceremony rule the community holds, separate from the personal principles above" (5A), '
        'P19 "different from the daily signs above" (6A). Pangram web app (the final test): the section 100% Human '
        '(1,199 words scanned, 04:07:38 UTC, batch 231g); every paragraph passes alone or beside a neighbor that passes alone. '
        'Gate: review-a4 (trace D1, cold read a5, stance a4 and a focused re-check), with dispositions. 4 A waits for his words '
        'for "willing to be seen". Records: s11/PREDICTIONS-s11.md (228g to 231g), s11/section-v10.md, s11/candidate-v10-keys.json. '
        'Not accepted until Joel says so. -->\n')
art = art[:i] + note + v10 + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 11 v10')
