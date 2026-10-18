"""Section 8's side-by-side page after Joel's message of 2026-10-17 21:37 UTC (his 49): v31 in the article so far, beside the
published section. A new map version from the last one (fix-20261015/make_pages.py's build()): the same rows, last turn's notes
dropped, tonight's notes on the rows that changed or that he said to keep. Highlights are against 08ca113a, the version on the
pages he read this evening (section 13 v35, 19:44 UTC). Batch 421g (fix-20261017d/b421) holds the checks.
Run from the candidate folder, after the install: python3 fix-20261017d/make_pages_s8.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(CAND / 'fix-20261015'))
import make_pages as M  # noqa: E402  (its build() reads the article now on disk)

M.SINCE = '08ca113a'
B = ('b421',)
R = {}
for b in B:
    R.update(json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8')))


def got(k, what):
    x = R[k]
    return 'Pangram: %s %s (%d words, %s UTC, batch %s): https://www.pangram.com/history%s' % (
        x[0].replace(' Written', '').replace(' Generated', ''), what, x[2], x[4],
        next(b[1:] + 'g' for b in B if k in json.loads((HERE / b / ('%s-results.json' % b)).read_text())), x[5])


FIRST = ('Your published section is on the left. On the right is the version now in the article so far. Highlighted words are '
         'new since the pages you read this evening, and struck words are ones that went.')
RUM = 'Amish young people, from about age 16, go'   # the Rumspringa paragraph's first words now (the map had "Amish young people, age 16")
PAGES = [
 (M.build('ic08-v5.json', 'ic08-v4.json',
   'Community article · section 8 · v31, 2026-10-17 night · in the article so far as a candidate',
   [FIRST, 'What changed: two of the four points of your 49; the other two stay as you wrote them.', got('S8v31', 'whole section')],
   fixes={'Amish young people, age 16': RUM},
   changed={
    RUM: ('changed tonight', [
        'Your 49: "yes fix rumspringa age": "Amish young people, from about age 16, go through a period of freedom from parental '
        'control called Rumspringa." It ends when they\'re baptized or leave, so it has no fixed length.',
        got('S8v31-rumspringa', 'alone')]),
    'Kids also need transferable skills': ('changed tonight', [
        'Your 49: "yes put punishing departure back": "If it can\'t, it can still avoid punishing departure." is back after the '
        'transition help, the published point.',
        got('S8v31-skills', 'alone'), got('S8v31-skills+next', 'with the paragraph after')]),
    # the paragraph with "Make sure kids understand what they say will be taken seriously" starts "Protecting children is the duty"
    'Protecting children is the duty': ('kept as you wrote it', [
        'Your 49: "yes dishonesty is a reason to dismiss the report that\'s why i changed that". Question 54 has one thing of '
        'mine on it.']),
    # the paragraph with "Kids in or outside of intentional communities" starts "Unlimited freedom isn't realistic"
    "Unlimited freedom isn't realistic": ('kept as you wrote it', [
        'Your 49: "parents handle money for kids, in or outside of community."'])}),
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
