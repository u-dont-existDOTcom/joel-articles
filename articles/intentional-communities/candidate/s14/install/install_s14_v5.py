"""Replace the published section 14 ("Dissolution and Exit") in HUMANIZED-SO-FAR.md with draft v5 (2026-10-16), after every
group and the whole section read Human (batches 305g, 305g-x and 306g) with every record complete. Run from candidate/:
python3 s14/install/install_s14_v5.py"""
import pathlib, re
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H, NEXT = '# Dissolution and Exit', '# What This Looks Like From Sénégal'
a = art.index(H); b = art.index(NEXT, a)
v0 = (C / 's14' / 'v0.md').read_text(encoding='utf-8').strip()
v5 = (C / 's14' / 'v5.md').read_text(encoding='utf-8').strip()
cur = art[a:b].strip()
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'\[image 18\]\([^)]*\)', '[image 18]', s)).strip()
assert norm(cur) == norm(v0) or norm(cur).replace('[image 18] ', '') == norm(v0), 'the article does not hold the published section 14; stop'
img = re.search(r'\[image 18\]\([^)]*\)', cur)
assert img and img.group(0) in v5, 'image 18 differs between the article and v5; stop'
note = ('<!-- CANDIDATE: section 14 v5 (2026-10-16): Emulate round a\'s call A of the published section with the preservation '
        'keys and Emulate\'s slips put back (s14/make_v1.py), a break in each paragraph (make_v2.py), the meaning reviews\' fixes '
        '(make_v3.py, make_v4.py), ending W2 for the father lines and the close, and P2 at the length that reads as one window '
        '(make_v5.py). Records: s14/review-r1 to review-r5 with DISPOSITIONS-r3.md and DISPOSITIONS-r5.md; key-word check PASS '
        '(s14/preservation-keys.json); lint REVIEW. Pangram web app, every group Human (305g, 305g-x) and the whole section 100% '
        'Human, high (382 words, AI likelihood 0.19, 19:54:06 UTC, batch 306g, '
        'https://www.pangram.com/history/c04a43b6-a611-4d68-bb76-2f644ee64654). Not accepted until Joel says so. -->\n')
art = art[:a] + note + v5 + '\n\n' + art[b:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 14 v5')
