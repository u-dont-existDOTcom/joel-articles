"""Replace the published section 10 in HUMANIZED-SO-FAR.md with section 10 v1 (a candidate). Run from candidate/."""
import pathlib, re
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
orig = (C.parent / 'original.md').read_text(encoding='utf-8')
i = orig.index('\n# From One Community to a Movement') + 1
k = orig.index('\n# Founderism: The Four Questions', i) + 1
pub = orig[i:k].strip()
start = art.index('\n# From One Community to a Movement') + 1
end = art.index('# Founderism: The Four Questions', start)
block = art[start:end].strip()
assert block == pub, 'the article does not hold the published section 10; stop'
new = (C / 's10/section-v1.md').read_text(encoding='utf-8').strip()
note = ('<!-- CANDIDATE: section 10 v1 (2026-10-10). Pangram web app (the final test): the section 100% Human (744 words '
        'scanned, 00:40:49 UTC, batch 198g); every paragraph passes alone. Published P3 and P4 are one paragraph (a proposal). '
        'Gate: traces E1, E2, F and G, stance checks e1, e2 and e4, cold reads e1 to e3, abstract-agent judge e1 and e2, linter '
        'REVIEW. Records: s10/PREDICTIONS-s10.md (batches 183g to 198g), s10/section-v1.md, s10/review-e1 to e4. Not accepted '
        'until Joel says so. -->\n')
art = art[:start] + note + new + '\n\n' + art[end:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 10 v1')
