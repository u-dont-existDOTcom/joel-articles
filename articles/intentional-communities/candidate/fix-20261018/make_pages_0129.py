"""The section 2 side-by-side page after Joel's messages of 2026-10-18 01:29 and 01:54 UTC: v3.6b, his first paragraph (56 a)
and aside (55 b), and the anomie paragraph (46 a) after his second paragraph; the screenshot stays in section 12. A new map
version from the last (fix-20261015/make_pages.py's build()), the anomie paragraph as a row of its own. Highlights are against
08ca113a (19:44 UTC on the 17th), the last section 2 page he had. Run from candidate/: python3 fix-20261018/make_pages_0129.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(CAND / 'fix-20261015'))
import make_pages as M  # noqa: E402

R = json.loads((HERE / 'b428' / 'b428-results.json').read_text(encoding='utf-8'))
R421 = json.loads((CAND / 'fix-20261017d' / 'b421' / 'b421-results.json').read_text(encoding='utf-8'))


def got(r, k, what, batch):
    x = r[k]
    return 'Pangram: %s %s (%d words, %s UTC, batch %sg): https://www.pangram.com/history%s' % (
        x[0].replace(' Written', '').replace(' Generated', ''), what, x[2], x[4], batch, x[5])


SINCE = '08ca113a'
FIRST = ('Your published section is on the left. On the right is the version now in the article. Highlighted words are new '
         'since the section 2 page you had on the 17th (19:44 UTC), and struck words are ones that went.')
intro = [FIRST, 'What changed: your first paragraph (56 a) and your aside (55 b), and the anomie paragraph after your second '
         'paragraph (46 a). Your screenshot stays in section 12: with it here as well, one window read AI, 63 words in the Instagram '
         'paragraphs (' + got(R, 'S2v36c', 'that version', 428)[len('Pangram: '):] + ').', got(R, 'S2v36b', 'whole section', 428)]
mp = M.build('ic02-v6.json', 'ic02-v5.json', 'Community article · section 2 · v3.6b, 2026-10-18 · in the article (the master)', intro,
             fixes={'Suddenly the longing behind my father': 'Suddenly, the longing to escape loneliness'},
             changed={'Suddenly, the longing to escape loneliness': ('yours', [
                 'Your words (56 a: "i checked the section, it passes as human when first part is this"), with the published link on '
                 '"the U.S. Surgeon General" and your bold on "public-health".',
                 got(R, 'S2v36-P1', 'alone', 428), got(R, 'S2v36-P1+head', 'with the heading', 428)]),
                 'Whether you want to call that loneliness': ('yours', [
                     'Your words from 23:10, with your aside of 55 b: "(the UN\'s rules for prisoners literally ban more than 15 days '
                     'of it)".', got(R, 'S2v36-P2', 'alone', 428), got(R, 'S2v36-P2+next', 'with the Google Trends paragraph', 428)])})
m = json.loads(mp.read_text(encoding='utf-8'))
rows = m['blocks'][0]['rows']
i = next(n for n, r in enumerate(rows) if r.get('article', '').startswith('Whether you want to call'))
if not any(r.get('article', '').startswith("What's starving them is anomie.") for r in rows):
    rows.insert(i + 1, {'label': 'your anomie point · new', 'article': "What's starving them is anomie.", 'source': [],
                        'notes': ['Your 46 a: the paragraph from your words (your instruction file\'s "large societies breed anomie and '
                                  'capture by psychopaths", your "i\'m always talking about"). Your screenshot stays in section 12.',
                                  got(R421, 'S2v34-A46', 'alone', 421), got(R421, 'S2v34-A46+next', 'with the Google Trends paragraph', 421)]})
mp.write_text(json.dumps(m, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(CAND / 'community-section2-side-by-side.html'), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(CAND.parent / 'original.md'), '--since', SINCE], capture_output=True, text=True)
print(mp.name, '-> community-section2-side-by-side.html exit', r.returncode)
print('  ' + '\n  '.join(l for l in (r.stdout + r.stderr).strip().split('\n') if 'label number was dropped' not in l)[-1500:])
