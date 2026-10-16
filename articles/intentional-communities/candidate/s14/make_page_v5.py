"""Section 14's side-by-side page for Joel: v5, now in the article, beside the published section, each paragraph with the
checks that read its exact text Human (batches 305g, 305g-x and 306g). Run from the repo root:
  python3 articles/intentional-communities/candidate/s14/make_page_v5.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S14 = C / 's14'
R = {}
for f in ('b305/b305-results.json', 'b305/b305x-results.json', 'b306/b306-results.json'):
    R.update(json.loads((S14 / f).read_text(encoding='utf-8')))
def says(key, batch):
    r = R[key]
    return '%s: %s (%s) %s' % (batch, r['headline'].replace(' Written', ''), key, r['link'])
pub = [b.strip() for b in re.split(r'\n\s*\n', (S14 / 'v0.md').read_text(encoding='utf-8')) if b.strip() and not b.startswith('#') and not b.startswith('[image')]
new = [b.strip() for b in re.split(r'\n\s*\n', (S14 / 'v5.md').read_text(encoding='utf-8')) if b.strip() and not b.startswith('#') and not b.startswith('[image')]
assert len(pub) == len(new) == 7
NOTES = {
 1: [says('S14v4x-1P12', '305g-x') + ', with the heading and P2 (P1 is under 50 words)'],
 2: [says('S14v4x-P2', '305g-x'), 'At 11 words shorter (v4) this paragraph split into two windows and its last 33 words read AI alone (305g, ' + R['S14v4-P2']['link'] + '); at this length it reads as one Human window.'],
 3: [says('S14v4-P34', '305g') + ', with P4'],
 4: [says('S14v4-P34', '305g') + ', with P3'],
 5: [says('S14v4-P5', '305g')],
 6: [says('S14v4-P67', '305g') + ', with P7', says('S14v4-P567', '305g') + ', with P5 and P7', 'Your published list ("It shaped the foundation he started, the film he made, the places he took me, and the questions I’m still asking.") read AI with P7 every time (301g, 303g); split in two sentences it reads Human.'],
 7: [says('S14v4-P67', '305g') + ', with P6'],
}
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
rows = [{'label': '', 'article': start(new[i]), 'source': [' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', pub[i]).split()[:5])],
         'notes': NOTES[i + 1] + ([says('S14v5', '306g') + ': the whole section'] if i == 6 else [])} for i in range(7)]
out = {'title': 'Dissolution and Exit · section 14, v5 beside the published one',
       'meta': 'Community article · section 14 · v5, 2026-10-16 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v5, now in the article, is on the right.',
                 'The whole section reads 100% Human, high confidence (' + R['S14v5']['link'] + '), and so does every group of it. '
                 'Each row shows the check that read its text Human.',
                 'What is Emulate\'s and what is mine: the sentence shapes are mostly Emulate\'s (its round on the whole section); the words '
                 'that carry your points back are mine, and so are the breaks ("Who would?", "That\'s a lot of loose ends!", "who\'s making '
                 'breakfast tomorrow?", "Who wants that?", "What a relief!", "(as you may have noticed!)", "I hope so, anyway."). Your '
                 'father lines keep your words, split in two sentences.'],
       'blocks': [{'headings': ['# Dissolution and Exit'], 'rows': rows}]}
mp = S14 / 'page' / 'ic14-v5.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section14-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
