"""Replace section 13 ("Your Little Forming Group Already Is the Community") in HUMANIZED-SO-FAR.md with draft v31
(2026-10-16), after the whole section read 100% Human, high, with its exact text (batch 311g, as v30a) and every subsection
holding a changed paragraph read Human with its exact text (309g, 310g), with every record complete (s13/review-r19 and
review-r20 with their DISPOSITIONS files; the gate records in s13/install/GATE-v31.json pass pangram_gate.py). The article
holds the published section with Joel's one sentence of 2026-10-11 ("So work out the process before it's about anyone in
particular."); the script stops if it holds anything else. Section 14's candidate note, which sits just before section 14's
heading, stays where it is. Run from candidate/: python3 s13/install/install_s13_v31.py"""
import pathlib, re, sys

C = pathlib.Path(__file__).resolve().parents[2]
DRAFT = C / 's13' / 'v31.md'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H = '# Your Little Forming Group Already Is the Community'
a = art.index(H)
b = art.index('\n# ', a + 5)
s14note = art.rfind('<!-- CANDIDATE: section 14', a, b)
end = s14note if s14note != -1 else b
cur = art[a:end]
orig = (C.parent / 'original.md').read_text(encoding='utf-8')
oa = orig.index(H); ob = orig.index('\n# ', oa + 5)
pub = orig[oa:ob].replace('Decide the process before the name:',
                          "So work out the process before it's about anyone in particular:")
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'<!--.*?-->', '', s, flags=re.S)).strip()
assert norm(cur) == norm(pub), 'the article does not hold the published section 13 with his 2026-10-11 sentence; stop'
new = DRAFT.read_text(encoding='utf-8').strip()
assert new.startswith(H)
note = ('<!-- CANDIDATE: section 13 v31 (2026-10-16): Emulate rounds a to j with the meaning put back inside Emulate\'s sentences '
        '(s13/make_v1.py to make_v31.py; v27 from round j, v28 and v29 taking my rebuilt sentences back to Emulate\'s, v30 and v31 '
        'the fixes of the meaning reviews), Joel\'s own sentences as he wrote them. Records: s13/review-r1 to review-r20 with their '
        'DISPOSITIONS files; key-word check PASS (s13/preservation-keys.json); lint REVIEW; gate records s13/install/GATE-v31.json. '
        'Pangram web app, every subsection holding a changed paragraph Human (309g, 310g) and the whole section 100% Human, high '
        '(2,324 words, AI likelihood 0.10, 22:57:35 UTC, batch 311g, '
        'https://www.pangram.com/history/0f17c2f0-8343-4b4a-9bb7-6b390136fd0b). Not accepted until Joel says so. -->\n')
art = art[:a] + note + new + '\n\n' + art[end:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 13', DRAFT.stem)
