"""The side-by-side pages for sections 2, 9 and 12 after Joel's message of 2026-10-17 17:16 UTC: his 44c (section 12: his P2 as
written, the screenshot with his caption), the anomie proposal (question 46, a proposal row on section 2's page), and the
faithfulness pass's fixes (section 2's "starving", section 9's limit). New map versions from the last ones
(fix-20261015/make_pages.py's build()). Highlights are against the head Joel saw this afternoon (7b30e2a2). Sections 15 and 16
have their own pages (s15/make_page_v14.py, s16/make_page_v29.py).
Run from the candidate folder, after the install: python3 fix-20261017b/make_pages.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(CAND / 'fix-20261015'))
import make_pages as M  # noqa: E402

M.SINCE = '7b30e2a2'
R = {}
for b in ('b415', 'b417'):
    R.update(json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8')))
BATCH = {k: b for b in ('b415', 'b417') for k in json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8'))}


def got(k, what):
    x = R[k]
    return 'Pangram: %s %s (%d words, %s UTC, batch %sg): https://www.pangram.com/history%s' % (
        x[0].replace(' Written', '').replace(' Generated', ''), what, x[2], x[4], BATCH[k][1:], x[5])


FIRST = ('Your published section is on the left. On the right is the version now in the article so far. Highlighted words are '
         'new since the pages you read this afternoon, and struck words are ones that went.')
ANOMIE = [b.strip() for b in (HERE / 'anomie' / 'draft-v2.md').read_text(encoding='utf-8').split('\n\n') if b.strip()][0]
S2P2 = 'Whether you want to call that loneliness'
PAGES = [
 (M.build('ic02-v5.json', 'ic02-v4.json',
   'Community article · section 2 · v3.2, 2026-10-17 evening · in the article so far as a candidate, unchanged',
   [FIRST, 'Nothing in section 2 changed this evening. The faithfulness pass put your published "starving" in for Emulate\'s '
    '"starvin\'" (your section 5 rule calls unusual spellings cheating), and the paragraph then read AI alone, so it\'s question 47. '
    'Below it, a proposal for your 44c, the anomie point (question 46).'],
   proposals=[{'label': 'Your anomie point (PROPOSAL, question 46)', 'after': S2P2, 'text': ANOMIE, 'notes': [
       'From your words: your instruction file\'s "large societies breed anomie and capture by psychopaths", your "large societies '
       'are run by psychopaths due to anomie" and your "i\'m always talking about". Your screenshot and caption would follow it.',
       got('A46', 'alone'), got('A46+next', 'with the next paragraph'), got('S2-A46b', 'section 2 with it and the screenshot'),
       'In the section, the first paragraph (installed text) became its own AI window; alone and with its neighbor the new '
       'paragraph reads Human.',
       'A cold read of section 2 with it: every paragraph OK but the screenshot\'s caption ("I can\'t see why the screenshot is here '
       'or what the "no, duh" is about").']}]),
  'community-section2-side-by-side.html'),
 (M.build('ic09-v6.json', 'ic09-v5.json',
   'Community article · section 9 · v17, 2026-10-17 evening · in the article so far as a candidate',
   [FIRST, 'What changed: your published limit back, "I\'m not claiming the Zapatistas already proved my whole model."',
    got('S9v17', 'whole section')],
   changed={'As part of my research': ('changed this evening', [
       'The faithfulness pass: I had cut it on 2026-10-14 as a repeat of your money-free economy line; under your dedup rule (cut '
       'only if no important meaning is lost) it lost meaning, since yours covers only the economy and this one the whole model.',
       got('S9v17-evid', 'alone')])}),
  'community-section9-side-by-side.html'),
 (M.build('ic12-v7.json', 'ic12-v6.json',
   'Community article · section 12 · v15, 2026-10-17 evening · in the article so far as a candidate',
   [FIRST, 'What changed: your 44c. Your paragraph as you wrote it, and your screenshot after it with your aside as the caption '
    '("It\'s kind of a "no, duh" study.", the link on "study"). Question 46 asks whether the screenshot moves to section 2.',
    got('S12v15', 'whole section')],
   changed={"This doesn't surprise me": ('changed this evening', [
       'Your words again, without my two sentences about the study.', got('S12v15-P2cap', 'with the caption')])}),
  'community-section12-side-by-side.html'),
]

if __name__ == '__main__':
    for mp, out in PAGES:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                            str(CAND / out), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                            '--source', str(CAND.parent / 'original.md'), '--since', M.SINCE],
                           capture_output=True, text=True)
        print(mp.name, '->', out, 'exit', r.returncode)
        print('  ' + '\n  '.join(l for l in (r.stdout + r.stderr).strip().split('\n') if 'label number was dropped' not in l))
