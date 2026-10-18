"""The questions page after Joel's messages of 2026-10-18 01:29 UTC (55 b, 56 a; the merge, the helper, the next article) and
01:54 UTC (signed in to another Pangram account): no open questions; 55 and 56 to Decided with what was done (batch 428g, the
master, the merge and the helper); "For you to do" is the paste and the merge; "Coming up" the next article. Idempotent: it
rebuilds the top from the page as it stood after 23:10 (fix-20261017d/make_questions_2310.py) each time.
Run from candidate/: python3 fix-20261018/make_questions_0129.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
subprocess.run([sys.executable, str(C / 'fix-20261017d' / 'make_questions_2310.py')], cwd=C, check=True, capture_output=True)
page = (C / 'OWNER-QUESTIONS.md').read_text(encoding='utf-8')
R = json.loads((HERE / 'b428' / 'b428-results.json').read_text(encoding='utf-8'))
L = lambda k: '[check](https://www.pangram.com/history%s)' % R[k][5]
PR = 'https://github.com/u-dont-existDOTcom/joel-articles/pull/191'

OLD_HEAD = re.search(r'Last updated 2026-10-17 at night, after your message of 23:10.*?what\'s coming up next\.\n', page, flags=re.S).group(0)
NEW_HEAD = ('Last updated 2026-10-18, after your messages of 01:29 (55 b, 56 a, the merge and the next article) and 01:54 (the other '
            'Pangram account): done (Decided, below). **Open questions: 0.** When there are some, they\'re here at the top, '
            'numbered, with their options; nothing further down needs an answer. Below: what\'s for you to do, what you decided and '
            'what I did about it, and what\'s coming up next.\n')
assert page.count(OLD_HEAD) == 1
page = page.replace(OLD_HEAD, NEW_HEAD)
a, b = page.index('## Open questions'), page.index('## For you to do')
page = page[:a] + '## Open questions\n\n> [!IMPORTANT]\n> None right now.\n\n' + page[b:]
a, b = page.index('## For you to do'), page.index('## Decided')
page = page[:a] + ('## For you to do\n\n'
                   '> [!WARNING]\n'
                   '> Two things, when you\'re back.\n\n'
                   '- 🟠 Paste the article into Substack: open the copy helper (COPY-TO-SUBSTACK.html, the file I sent with my message, '
                   'also [in Git](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/'
                   'intentional-communities/exports/COPY-TO-SUBSTACK.html)) in Opera and click "Copy Article". Paste it into a new draft '
                   'first and check the images, the three post embeds, the two YouTube videos, Share and Subscribe; then the same into '
                   'the post. Then upload your PsyPost screenshot in section 12, after the paragraph that starts "This doesn\'t surprise '
                   'me, since we\'re taught to put on a show of competence", with the caption It\'s kind of a "no, duh" study. (the link '
                   'on "study" to the PsyPost write-up), and the image linked to the same page.\n'
                   '- 🟠 Merge when you\'ve looked: `gh pr merge 191 -R u-dont-existDOTcom/joel-articles --merge` ([the pull request](%s)). '
                   'It has section 2, the master, the merge and the helper.\n\n' % PR) + page[b:]
DEC = ('- 🟢 2026-10-18 01:29 and 01:54 UTC, 55 and 56, the merge:\n'
       '  - 56 a, your first paragraph for section 2 ("i checked the section, it passes as human when first part is this"): in, as '
       'you wrote it, with the published link on "the U.S. Surgeon General" and your bold on "public-health". It reads Human alone '
       '(%s) and with the heading (%s).\n'
       '  - 55 b: in, "(the UN\'s rules for prisoners literally ban more than 15 days of it)". Your second paragraph reads Human '
       'alone (%s) and with the next (%s).\n'
       '  - 46 a, the anomie paragraph: in, after your second paragraph; section 2 reads 100%% Human with it (%s). With your '
       'screenshot there as well, one window read AI, 63 words in the Instagram paragraphs (%s), so the screenshot stays in '
       'section 12, where you upload it.\n'
       '  - 45 a: done. The humanized article is the registered master (`master.md`, with a promotion receipt); your published '
       'text stays as the published source.\n'
       '  - The merge: the master is in your Substack HTML of 01:29, with every image, embed, video and button as it was in your '
       'paste, the published lists and bold leads kept where the paragraphs line up, and every link (103). The copy helper is the '
       'repository\'s own (its generator built and checked it; its Copy button passed a test in a browser). Making it showed that '
       'Substack\'s editor now wraps the article differently, so the part that finds the article in your paste got a fix, or the '
       'helper would have copied the editor\'s wrapper too.\n'
       '  - Pangram: after your 01:29 message the browser was signed out and the API key had no credits; you signed in to another '
       'account at 01:54, and the checks above ran there.\n'
       % (L('S2v36-P1'), L('S2v36-P1+head'), L('S2v36-P2'), L('S2v36-P2+next'), L('S2v36b'), L('S2v36c')))
d = page.index('> Answered, with what I did.')
d = page.index('\n', d) + 1
page = page[:d] + '\n' + DEC + page[d:].lstrip('\n')
a = page.index('## Coming up (not a question yet)')
b = page.index('\n- 🔵 Image 7', a)
page = page[:a] + ('## Coming up (not a question yet)\n\n'
                   '> [!NOTE]\n'
                   '> Work that\'s next. Nothing here needs an answer.\n\n'
                   '- 🔵 The next article in your queue, the hypnosis guide, from Emulate\'s work, section by section, the same way.\n'
                   '- 🔵 The prediction scorecard: better guesses of what Pangram will say, and how fast and how often my fixes pass.') + page[b:]
(C / 'OWNER-QUESTIONS.md').write_text(page, encoding='utf-8')
print('wrote OWNER-QUESTIONS.md')
