"""The side-by-side page after Joel's message of 2026-10-15 11:04 UTC: section 4 (his 27, "this passes").

ic04-v8 from ic04-v7 (fix-20261014b/make_pages.py's): the same rows and source starts, the start that changed fixed
("And this reparenting journey is built on"), last turn's notes dropped, today's notes on his two paragraphs.
Highlights are against main at 934d64c9, the version Joel last merged (pull request 175).

Run from the candidate folder: python3 fix-20261015b/make_pages.py
"""
import json, pathlib, subprocess, sys

CAND = pathlib.Path(__file__).resolve().parent.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(CAND / 'fix-20261015'))
import make_pages as M  # noqa: E402  (fix-20261015's build(), which reads the article now on disk)

B = json.loads((CAND / 'fix-20261015b' / 'gui' / 'b287-results.json').read_text(encoding='utf-8'))
M.SINCE = '934d64c9'


def got(k, what):
    x = B[k]
    return 'Pangram: Human %s (%d words, %s UTC, batch 287g): %s' % (what, x['words'], x['utc'][11:19], x['link'])


FIRST = ('Your published section is on the left. On the right is the version now in the article so far. '
         'Highlighted words are new since the version you merged last (pull request 175), and struck words are ones that went.')
PAGES = [(M.build('ic04-v8.json', 'ic04-v7.json',
    'Community article · section 4 · v11.3, 2026-10-15 11:04 · your final section, in the article so far as a candidate',
    [FIRST,
     'What changed: your two paragraphs under "Inner pl/ork" ("27: this passes"), as you wrote them. The links stay on '
     '"Inner-child reparenting" and "somatic regulation", since a paste from the page carries the words but not the links.',
     'Pangram: the whole section 100%% Human, high (%d words, %s UTC, batch 287g): %s' % (B['S4v113']['words'], B['S4v113']['utc'][11:19], B['S4v113']['link'])],
    fixes={'And inner pl/ork is built on': 'And this reparenting journey is built on'},
    changed={
        'Inner-child reparenting means learning': ('yours, changed today', [
            'Your 27: "the best holistic inner adult" and "your little one gains more freedom to remain alive inside you, which brings back the joy of life that many adults have forgotten about."',
            got('J4-P11d', 'alone')]),
        'And this reparenting journey is built on': ('yours, changed today', [
            'Your 27: "And this reparenting journey" names what\'s built on somatic regulation (my I1 fix had "inner pl/ork"), and "I.e., listening".',
            got('J4-P11dP12d', 'with the paragraph before (it\'s under 50 words)')])}),
    'community-section4-side-by-side.html')]

if __name__ == '__main__':
    for mp, out in PAGES:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                            str(CAND / out), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                            '--source', str(CAND.parent / 'original.md'), '--since', M.SINCE],
                           capture_output=True, text=True)
        print(mp.name, '->', out, 'exit', r.returncode)
        print('  ' + '\n  '.join(l for l in (r.stdout + r.stderr).strip().split('\n') if 'label number was dropped' not in l))
