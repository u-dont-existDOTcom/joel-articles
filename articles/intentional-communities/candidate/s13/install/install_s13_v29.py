"""Replace section 13 ("Your Little Forming Group Already Is the Community") in HUMANIZED-SO-FAR.md with draft v29
(2026-10-16), after the whole section read 100% Human, high (batch 309g) and every group holding a changed paragraph read
Human with its exact text (308g, 309g), with every record complete (s13/review-r19 and its DISPOSITIONS-r19.md). The article
holds the published section with Joel's one sentence of 2026-10-11 ("So work out the process before it's about anyone in
particular."); the script stops if it holds anything else. Section 14's candidate note, which sits just before section 14's
heading, stays where it is. Run from candidate/: python3 s13/install/install_s13_v29.py [DRAFT]"""
import pathlib, re, sys

C = pathlib.Path(__file__).resolve().parents[2]
DRAFT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else C / 's13' / 'v29.md'
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
note = ('<!-- CANDIDATE: section 13 %s (2026-10-16): Emulate rounds a to j with the meaning put back inside Emulate\'s sentences '
        '(s13/make_v1.py to make_v29.py; the last three rounds: v27 from round j, v28 and v29 taking my rebuilt sentences back to '
        'Emulate\'s), Joel\'s own sentences as he wrote them. Records: s13/review-r1 to review-r19 with their DISPOSITIONS files; '
        'key-word check PASS (s13/preservation-keys.json); lint REVIEW. Pangram web app, every group holding a changed paragraph '
        'Human (304g, 308g, 309g) and the whole section 100%% Human, high (2,322 words, AI likelihood 0.07, 22:11:30 UTC, batch '
        '309g, https://www.pangram.com/history/924264d4-24d9-4ee2-a46b-2eb64818b47d). Not accepted until Joel says so. -->\n'
        % DRAFT.stem)
art = art[:a] + note + new + '\n\n' + art[end:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 13', DRAFT.stem)
