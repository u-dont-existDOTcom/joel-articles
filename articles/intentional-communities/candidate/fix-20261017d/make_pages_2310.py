"""The side-by-side pages after Joel's message of 2026-10-17 23:10 UTC: section 2 (his opening, and the anomie paragraph and his
screenshot if they went in), section 8 (his 54 sentence) and section 12 (if the screenshot moved out). New map versions from the
last ones (fix-20261015/make_pages.py's build()); a paragraph new to the article (the anomie paragraph) gets its own row. Highlights
are against 000ff576, the version of the pages he had at 23:00. Run from candidate/ after install_2310.py:
python3 fix-20261017d/make_pages_2310.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(CAND / 'fix-20261015'))
import make_pages as M  # noqa: E402  (its build() reads the article now on disk; its module code rebuilds ic10-v5, unchanged)

M.SINCE = '000ff576'
R, BATCH = {}, {}
for b in ('b421', 'b425'):
    r = json.loads((HERE / b / ('%s-results.json' % b)).read_text(encoding='utf-8'))
    al = HERE / b / 'aliases.json'
    for k, v in (json.loads(al.read_text()) if al.exists() else {}).items():
        r.setdefault(k, r[v])
    for k in r:
        BATCH[k] = b
    R.update(r)
art = (CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
inn = lambda f: (HERE / f).read_text(encoding='utf-8').strip() in art
S2 = next((k for k, f in (('S2v35c', 's2-v35c.md'), ('S2v35b', 's2-v35b.md'), ('S2v35', 's2-v35.md')) if inn(f)), None)
S8 = inn('s8-v32.md')


def got(k, what):
    x = R[k]
    return 'Pangram: %s %s (%d words, %s UTC, batch %sg): https://www.pangram.com/history%s' % (
        x[0].replace(' Written', '').replace(' Generated', ''), what, x[2], x[4], BATCH[k][1:], x[5])


FIRST = ('Your published section is on the left. On the right is the version now in the article so far. Highlighted words are '
         'new since the pages you had at 23:00, and struck words are ones that went.')
PAGES = []
if S2:
    ver = {'S2v35c': 'v3.5c', 'S2v35b': 'v3.5b', 'S2v35': 'v3.5'}[S2]
    intro = [FIRST, 'What changed: your opening (52 a), with your aside (53)' + {
        'S2v35c': ', and your 46 a: the anomie paragraph after your second paragraph, with your screenshot and caption.',
        'S2v35b': ', and the anomie paragraph after your second paragraph (your 46 a); the screenshot stays in section 12.',
        'S2v35': '. The anomie paragraph waits: with it, the section read AI.'}[S2], got(S2, 'whole section')]
    mp = M.build('ic02-v6.json', 'ic02-v5.json', 'Community article · section 2 · %s, 2026-10-17 night · in the article so far as a '
                 'candidate' % ver, intro,
                 fixes={'Suddenly the longing behind my father': 'Suddenly the longing to escape loneliness'},
                 changed={'Suddenly the longing to escape loneliness': ('yours tonight', [
                     'Your words (52 a: "this is human"), with the published link on "the U.S. Surgeon General" kept.',
                     got('S2v35-P1+next', 'with your second paragraph (this one is under 50 words, Pangram\'s minimum)')]),
                     'Whether you want to call that loneliness': ('yours tonight', [
                         'Your words, with your aside (53): "(it\'s literally listed in the UN Convention Against Torture)". The '
                         'Convention\'s text doesn\'t name solitary confinement: question 55.',
                         got('S2v35-P2', 'alone')] + ([got('S2v35-P2+next', 'with the Google Trends paragraph')] if S2 == 'S2v35' else []))})
    if S2 in ('S2v35b', 'S2v35c'):
        m = json.loads(mp.read_text(encoding='utf-8'))
        rows = m['blocks'][0]['rows']
        i = next(n for n, r in enumerate(rows) if r.get('article', '').startswith('Whether you want to call'))
        rows.insert(i + 1, {'label': 'your anomie point · new tonight', 'article': "What's starving them is anomie.", 'source': [],
                            'notes': ['Your 46 a: the paragraph from your words (your instruction file\'s "large societies breed '
                                      'anomie and capture by psychopaths", your "i\'m always talking about")' +
                                      (', with your screenshot and caption after it, moved from section 12.' if S2 == 'S2v35c' else
                                       '; your screenshot stays in section 12.'),
                                      got('S2v34-A46', 'alone'), got('S2v34-A46+next', 'with the Google Trends paragraph')]})
        mp.write_text(json.dumps(m, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    PAGES.append((mp, 'community-section2-side-by-side.html'))
if S8:
    PAGES.append((M.build('ic08-v6.json', 'ic08-v5.json',
                          'Community article · section 8 · v32, 2026-10-17 night · in the article so far as a candidate',
                          [FIRST, 'What changed: your sentence (54) after "if they are known to be honest."', got('S8v32', 'whole section')],
                          changed={'Protecting children is the duty': ('changed tonight', [
                              'Your 54: "And those who are known to lie a lot are especially targeted by abusers who know their '
                              'accusations won\'t be believed."', got('S8v32-truth', 'alone')])}),
                  'community-section8-side-by-side.html'))
if S2 == 'S2v35c':
    PAGES.append((M.build('ic12-v8.json', 'ic12-v7.json',
                          'Community article · section 12 · v16, 2026-10-17 night · in the article so far as a candidate',
                          [FIRST, 'What changed: your screenshot and its caption moved to section 2, after the anomie paragraph '
                           '(your 46 a).', got('S12v16', 'whole section')],
                          changed={"This doesn't surprise me": ('changed tonight', [
                              'Your screenshot and caption ("It\'s kind of a "no, duh" study.") are in section 2 now, after the '
                              'anomie paragraph (your 46 a).'])}),
                  'community-section12-side-by-side.html'))
if __name__ == '__main__':
    for mp, out in PAGES:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                            str(CAND / out), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                            '--source', str(CAND.parent / 'original.md'), '--since', M.SINCE], capture_output=True, text=True)
        print(mp.name, '->', out, 'exit', r.returncode)
        print('  ' + '\n  '.join(l for l in (r.stdout + r.stderr).strip().split('\n') if 'label number was dropped' not in l)[-1200:])
