"""Replace section 10 v1 in HUMANIZED-SO-FAR.md with section 10 v2 (a candidate). Run from candidate/.
v2 = v1 with Joel's changes of 2026-10-10 12:22 UTC (P3+P4 without "boring" and the super-commune sentence, P6's
"slide into" for "quietly turn into", his heading "Federated Communities Make a Movement")."""
import pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v1 = (C / 's10/section-v1.md').read_text(encoding='utf-8').strip()
v2 = (C / 's10/section-v2.md').read_text(encoding='utf-8').strip()
i = art.index('<!-- CANDIDATE: section 10 v1')
j = art.index('-->\n', i) + 4
k = art.index('# Founderism: The Four Questions', j)
assert art[j:k].strip() == v1, 'the article does not hold section 10 v1; stop'
note = ('<!-- CANDIDATE: section 10 v2 (2026-10-10), Joel\'s changes of 12:22 UTC in: P3+P4 without "boring" and without '
        '"I don\'t want one super-commune with a nicer logo.", P6 "slide into" for "quietly turn into" (trace H OK), and his '
        'heading "Federated Communities Make a Movement" (his 13:00 answer, after grounding f1 and stance f1 flagged '
        '"Improve Resilience"). Pangram web app (the final test): the section 100% Human (731 words scanned, 13:04:52 UTC, '
        'batch 200g); P3+P4 and P6 pass alone, the heading with P3+P4 and P2 across it pass. Records: '
        's10/PREDICTIONS-s10.md (199 to 200g), s10/section-v2.md, s10/review-f1/. Not accepted until Joel says so. -->\n')
art = art[:i] + note + v2 + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 10 v2')
