"""The side-by-side pages for sections 1, 4, 8 and 12 after Joel's message of 2026-10-17 13:11 UTC: his answer to question 39
(section 4), the PsyPost study he sent (section 12), and the sweep of his "this is not the same as it" and "quietly" rules
(sections 1 and 8). New map versions from the last ones (fix-20261015/make_pages.py's build()): the same rows, last turn's
notes dropped, today's notes on the rows that changed. Highlights are against c6f3a78e, the version on the pages he read this
morning. Sections 15 and 16 have their own pages (s15/make_page_v13.py, s16/make_page.py).
Run from the candidate folder, after the install: python3 fix-20261017/make_pages.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(CAND / 'fix-20261015'))
import make_pages as M  # noqa: E402  (its build() reads the article now on disk)

M.SINCE = 'c6f3a78e'
R = {}
for b in ('b410', 'b411', 'b412'):
    R.update(json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8')))


def got(k, what):
    x = R[k]
    return 'Pangram: %s %s (%d words, %s UTC, batch %s): https://www.pangram.com/history%s' % (
        x[0].replace(' Written', '').replace(' Generated', ''), what, x[2], x[4],
        next(b[1:] + 'g' for b in ('b410', 'b411', 'b412') if k in json.loads((HERE / b / ('%s-results.json' % b)).read_text())), x[5])


FIRST = ('Your published section is on the left. On the right is the version now in the article so far. Highlighted words are '
         'new since the pages you read this morning, and struck words are ones that went.')
PAGES = [
 (M.build('ic04-v9.json', 'ic04-v8.json',
   'Community article · section 4 · v11.4, 2026-10-17 · in the article so far as a candidate',
   [FIRST, 'What changed: your answer to question 39, after the container line, with "I\'d say" dropped.',
    got('S4v114', 'whole section')],
   changed={'The first three parts are the inside': ('changed today', [
       'Your 39: "i\'d say it\'s the practical logistical foundation that gets built once the architects can work well together". '
       'It answers the question: the container is what the community stands on, and it gets built once the people building it can '
       'work together, which is section 16\'s order. "The architects" fits the house diagram above.',
       got('S4v114-container+prev', 'with the paragraph before'), got('S4v114-container+next', 'with the paragraph after')])}),
  'community-section4-side-by-side.html'),
 (M.build('ic12-v6.json', 'ic12-v5.json',
   'Community article · section 12 · v14, 2026-10-17 · in the article so far as a candidate',
   [FIRST, 'What changed: the PsyPost study you sent, at the end of your paragraph on the career market, and your screenshot '
    'after that paragraph (question 44 asks whether that is the place).', got('S12v14', 'whole section')],
   changed={"This doesn't surprise me": ('changed today', [
       'Your paragraph as you wrote it, then the study: "A new study found that where relationships are easy to make and break, '
       'people even feel less on the same page with whoever doesn\'t help them reach their goals. Kind of a "no, duh" study, but '
       'still." The link is on "new study"; your screenshot follows the paragraph.',
       'Checked against the write-up: it supports this (the experiment found less shared reality with career contacts who '
       'weren\'t helpful; shared reality with helpful ones didn\'t change, so the sentence says only the first). As a paragraph of its '
       'own, two cold reads couldn\'t see why the study was there; at the end of yours, your "So then a lot of people end up '
       'thinking they aren\'t good enough" follows from it, and the third cold read found every paragraph OK.',
       got('S12v14-P2', 'alone')])}),
  'community-section12-side-by-side.html'),
 (M.build('ic01-v4.json', 'ic01-v3.json',
   'Community article · section 1 · 2026-10-17 · in the article so far as a candidate',
   [FIRST, 'What changed: one word, from the sweep of your 13:11 rule ("this" is not the same as "it").', got('S1sw', 'whole section')],
   changed={'The East Wind commune was almost': ('changed today', [
       '"That\'s the sort of thing that doesn\'t make it into the history books." for "It\'s the sort of thing ...": your published '
       'sentence points back with "These" ("These are the questions history books neglect.").',
       got('S1sw-EastWind', 'alone')])}),
  'community-section1-side-by-side.html'),
 (M.build('ic08-v4.json', 'ic08-v3.json',
   'Community article · section 8 · v30, 2026-10-17 · in the article so far as a candidate',
   [FIRST, 'What changed: one word out, from the sweep of your 13:11 rule ("remove "quietly" that\'s an ai tell").',
    got('S8v30', 'whole section')],
   changed={'This could be badly misunderstood': ('changed today', [
       '"Older kids can\'t be allowed to boss the younger ones around there." without "quietly"; the sentence before ("The adults '
       'still have to pay attention ...") keeps what it added, bossing the adults don\'t see.',
       got('S8v30-safeguards+prev', 'with the paragraph before'), got('S8v30-safeguards+next', 'with the paragraph after')])}),
  'community-section8-side-by-side.html'),
]

if __name__ == '__main__':
    for mp, out in PAGES:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                            str(CAND / out), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                            '--source', str(CAND.parent / 'original.md'), '--since', M.SINCE],
                           capture_output=True, text=True)
        print(mp.name, '->', out, 'exit', r.returncode)
        print('  ' + '\n  '.join(l for l in (r.stdout + r.stderr).strip().split('\n') if 'label number was dropped' not in l))
