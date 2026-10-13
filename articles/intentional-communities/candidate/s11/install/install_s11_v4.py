"""Replace section 11 v11 in HUMANIZED-SO-FAR.md with section 11 v12 (a candidate), and fix "Decide the process before
the name" in section 13's "When Somebody Has to Go". Run from candidate/.
v12 = Joel's answers of 2026-10-11 23:12 UTC fitted into his paragraphs (J3b, J4, R14c, R16c, R16d, R18b)."""
import pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v11 = (C / 's11/section-v11.md').read_text(encoding='utf-8').strip()
v12 = (C / 's11/section-v12.md').read_text(encoding='utf-8').strip()
i = art.index('<!-- CANDIDATE: section 11 v11')
j = art.index('-->\n', i) + 4
k = art.index('# The Math of Absorption', j)
assert art[j:k].strip() == v11, 'the article does not hold section 11 v11; stop'
note = ('<!-- CANDIDATE: section 11 v12 (2026-10-12), Joel\'s answers of 2026-10-11 23:12 UTC fitted into his paragraphs under '
        'his 18:35 rule (an answer in chat is content, fitted in context, changes shown): J3b names the divorce half; J4 his '
        'answer on terms for visiting friends; R14c his answer on private practices, with "some practices go too far against '
        'the communal spirit" from a cold read\'s "no principle"; R16c and R16d his answer on members who don\'t fit in; R18b '
        'his grandmother case. Pangram web app: the section 100% Human (1,682 words scanned, 00:00:52 UTC, batch 233g); every '
        'changed paragraph 100% Human alone and in its run. Gate round a6 (s11/review-a6/). Records: s11/PREDICTIONS-s11.md '
        '(233g), s11/section-v12.md, s11/candidate-v12-keys.json, s11/fix-v25-parts.json, s11/joel-2312/. Not accepted '
        'until Joel says so. -->\n')
art = art[:i] + note + v12 + '\n\n' + art[k:]
old = 'The power to remove somebody is also one of the easiest powers to abuse. Decide the process before the name: '
new = 'The power to remove somebody is also one of the easiest powers to abuse. So work out the process before it\'s about anyone in particular: '
assert art.count(old) == 1, 'the "Decide the process before the name" line is not in the article; stop'
art = art.replace(old, new)
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 11 v12, and fixed the line in When Somebody Has to Go')
