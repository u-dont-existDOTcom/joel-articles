"""Replace section 11 v10 in HUMANIZED-SO-FAR.md with section 11 v11 (a candidate). Run from candidate/.
v11 = Joel's message of 2026-10-11 18:35 UTC: "willing to be seen" cut, his article version of the land paragraph
(J1 to J3) after P10, P10 and J1 to J3 moved to the end of the first subsection, and his rewrite of the second
subsection (R14 to R19)."""
import pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v10 = (C / 's11/section-v10.md').read_text(encoding='utf-8').strip()
v11 = (C / 's11/section-v11.md').read_text(encoding='utf-8').strip()
i = art.index('<!-- CANDIDATE: section 11 v10')
j = art.index('-->\n', i) + 4
k = art.index('# The Math of Absorption', j)
assert art[j:k].strip() == v10, 'the article does not hold section 11 v10; stop'
note = ('<!-- CANDIDATE: section 11 v11 (2026-10-11), Joel\'s message of 18:35 UTC: "willing to be seen" cut; his article '
        'version of the land paragraph (J1 to J3) after P10, with P10 and J1 to J3 moved to the end of the first subsection; '
        'his rewrite of the second subsection (R14 to R19; P13 unchanged). Typos fixed only ("ends by up treating"). '
        'Pangram web app: the section 100% Human (1,354 words scanned, 18:41:21 UTC, batch 232g); every paragraph passes '
        'alone or in its run. Records: s11/PREDICTIONS-s11.md (232g), s11/section-v11.md, s11/candidate-v11-keys.json, '
        's11/joel-1835/, s11/review-a5/. Not accepted until Joel says so. -->\n')
art = art[:i] + note + v11 + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 11 v11')
