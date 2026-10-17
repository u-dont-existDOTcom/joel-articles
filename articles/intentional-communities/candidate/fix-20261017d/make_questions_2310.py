"""The questions page after Joel's message of 2026-10-17 23:10 UTC (52 to 54 answered, and the scorecard): runs make_questions.py
(the 21:37 page, built from version 13 as published), then moves 52 to 54 to Decided with what was done and 425g's checks, and
asks 55 (his new aside: the Convention Against Torture's text doesn't list solitary confinement). Idempotent.
Run from candidate/: python3 fix-20261017d/make_questions_2310.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
subprocess.run([sys.executable, str(HERE / 'make_questions.py')], cwd=C, check=True, capture_output=True)
page = (C / 'OWNER-QUESTIONS.md').read_text(encoding='utf-8')
R = {}
for b in ('b421', 'b422', 'b423', 'b424', 'b425', 'b426', 'b427'):
    f = HERE / b / ('%s-results.json' % b)
    if f.exists():
        r = json.loads(f.read_text(encoding='utf-8'))
        al = HERE / b / 'aliases.json'
        for k, v in (json.loads(al.read_text()) if al.exists() else {}).items():
            r.setdefault(k, r[v])
        R.update(r)
L = lambda k: '[check](https://www.pangram.com/history%s)' % R[k][5]
human = lambda k: k in R and R[k][0].startswith('Human') and R[k][3].startswith('Human') and '; AI' not in R[k][3]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
ROWS = len(json.loads((C / 'prediction-review' / 'prediction-calls-rows.json').read_text(encoding='utf-8'))['rows'])
IN = {k: (HERE / f).read_text(encoding='utf-8').strip() in art for k, f in
      (('S2v35', 's2-v35.md'), ('S2v35b', 's2-v35b.md'), ('S2v35c', 's2-v35c.md'), ('S8v32', 's8-v32.md'))}
S2 = next((k for k in ('S2v35c', 'S2v35b', 'S2v35') if IN[k]), None)

OLD_HEAD = re.search(r'Last updated 2026-10-17 at night, after your message of 21:37.*?what\'s coming up next\.\n', page, flags=re.S).group(0)
open_n = 1 if S2 else 2
NEW_HEAD = ('Last updated 2026-10-17 at night, after your message of 23:10 (52 to 54, and the scorecard): done (Decided, below). '
            '**Open questions: %d** (%s). Every question is here at the top, numbered, with its options; nothing further down needs '
            'an answer. To answer, reply in chat with the number and the letter (for example "55 a"), or in your own words. Below '
            'the questions: what\'s for you to do, what you decided and what I did about it, and what\'s coming up next.\n' % (open_n, '55' if S2 else '55 and 56'))
assert page.count(OLD_HEAD) == 1
page = page.replace(OLD_HEAD, NEW_HEAD)
a, b = page.index('## Open questions'), page.index('## For you to do')
OPEN = ('## Open questions\n\n'
        '> [!IMPORTANT]\n'
        ('> One question. It quotes its passage.\n\n' if S2 else '> Two questions, both on section 2\'s opening. Each quotes its passage.\n\n') +
        
        '**🟣 55. Section 2, your aside: the Convention Against Torture doesn\'t list it.** "(it\'s literally listed in the UN '
        'Convention Against Torture)": the Convention\'s text (1984) defines torture in general terms and lists no practices; '
        'solitary confinement isn\'t in it. What does name it: the UN\'s special rapporteur on torture said in 2011 that solitary '
        'confinement beyond 15 days is torture or cruel, inhuman or degrading treatment, and the UN\'s rules for prisoners (the '
        'Mandela Rules) ban it past 15 days ([a summary of the international law, with both](https://www.prisonlegalnews.org/news/'
        'publications/international-human-rights-law-solitary-confinement-hrf-2015); [the rules themselves](https://www.'
        'solitaryconfinement.org/un-nelson-mandela-rules)). A check of the Convention is easy to get wrong this way: the UN '
        'committee that oversees it has criticized solitary confinement, but the treaty itself never names it.\n'
        '- a) "(the UN\'s torture expert literally calls more than 15 days of it torture)". **My pick**: close to your "literally", '
        'and true.\n'
        '- b) "(it\'s literally banned as torture in the UN\'s rules for prisoners)".\n'
        '- c) Keep yours.\n'
        '- d) Your words.\n\n'
        'I check whichever you pick alone and in the section. If you don\'t answer, c: it stays as you wrote it.\n\n')
if not S2:
    OPEN += ('**🟣 56. Section 2: your first sentence, read on its own.** Your opening reads Human as you checked it, and in the '
             'section too except for one window: Pangram cuts off the heading and your first sentence (50 words) and reads that '
             'AI, low confidence as you pasted it (%s) and medium with the anomie paragraph after it (%s). Your two paragraphs read '
             'Human together (%s) and your second alone (%s), and joining them into one paragraph didn\'t change it (%s). The '
             'sentence:\n\n'
             '> Suddenly the longing to escape loneliness which inspired my father’s movie is everywhere again, and in 2023 the U.S. '
             'Surgeon General even put out an advisory, saying roughly half of American adults experience loneliness, and it '
             'treated social connection as a public-health issue.\n\n'
             '- a) Your rewording of that sentence; I check it alone, with your second paragraph, and in the section with the anomie '
             'paragraph and your screenshot. **My pick**: your rewrites have read Human every time today.\n'
             '- b) I try rewordings of it myself, keeping your words where I can, and bring back the ones that pass.\n'
             '- c) Keep section 2\'s old opening for now; the master then goes ahead without your opening and the anomie paragraph.\n\n'
             'If you don\'t answer, b.\n\n' % (L('S2v35'), L('S2v35c'), L('S2v35-P1+next'), L('S2v35-P2'), L('S2v35m')))
page = page[:a] + OPEN + page[b:]

r52 = []
if S2:
    r52.append('in: section 2 now opens with your two paragraphs, as you wrote them (the link on "the U.S. Surgeon General" '
               'kept). Your first paragraph with your second reads Human (%s), your second alone (%s), and the section 100%% Human '
               '(%s).' % (L('S2v35-P1+next'), L('S2v35-P2'), L(S2)))
    if S2 == 'S2v35c':
        r52.append('Your 46 a is in with it: the anomie paragraph after your second paragraph, then your screenshot and caption, '
                   'moved from section 12 (section 12 reads 100%% Human without them, %s).' % L('S12v16'))
    elif S2 == 'S2v35b':
        r52.append('The anomie paragraph is in after your second paragraph (your 46 a), but your screenshot and caption stay in '
                   'section 12: with them in section 2 as well, the section read AI (%s).' % L('S2v35c'))
    else:
        r52.append('The anomie paragraph (your 46 a) isn\'t: with it after your paragraph, the section read AI (%s), and with the '
                   'screenshot too (%s). Section 2 is as you pasted it, and the screenshot stays in section 12.'
                   % (L('S2v35b'), L('S2v35c')))
else:
    r52.append('not in yet: with your opening, the section reads one AI window, the heading and your first sentence, so '
               'question 56. Your 46 a waits with it; section 2 is as it was, and the screenshot is still in section 12.')
r54 = ('in: "Make sure kids understand what they say will be taken seriously if they are known to be honest. And those who are known '
       'to lie a lot are especially targeted by abusers who know their accusations won\'t be believed." The paragraph reads Human '
       '(%s), section 8 100%% Human (%s).' % (L('S8v32-truth'), L('S8v32'))) if IN['S8v32'] else (
       'not in yet: with it, section 8 read AI (%s).' % L('S8v32'))
DEC = ('- 🟢 2026-10-17 23:10 UTC, 52 to 54 and the scorecard:\n'
       '  - 52 a, your words for section 2\'s opening ("this is human"): ' + ' '.join(r52) + '\n'
       '  - 53 "fixed (fact checked with gemini)": your aside is in as you wrote it, "(it\'s literally listed in the UN Convention '
       'Against Torture)". The Convention\'s text doesn\'t name solitary confinement, though: question 55.\n'
       '  - 54: ' + r54 + '\n'
       '  - "your scorecard is always empty": it was, and it was my fault twice over. The page counts one row per check, and the '
       'file I kept giving it was a summary, so it had nothing to count. And each time I updated it I uploaded a new file without '
       'pointing the page at it, then deleted the old one, so the page was reading a file that no longer existed. Its own error log '
       'said so ("Couldn\'t load the file (404)"), and I never read it. Fixed: the page now reads one row per check (%s of them, '
       'through tonight), and the update steps are written down where the next session will follow them. What it\'s for: your '
       '"i want to see you improving on that" (12 October). It shows how often my guess of each Pangram result was right, against '
       'always guessing AI, batch by batch, and lists every miss since the review of 10 October with its text, so you can see '
       'whether I\'m getting better at telling what reads AI.\n' % '{:,}'.format(ROWS))
d = page.index('> Answered, with what I did.')
d = page.index('\n', d) + 1
page = page[:d] + '\n' + DEC + page[d:].lstrip('\n')
UP_OLD = ('- 🔵 Section 2, once question 52 is settled: your paragraph (with question 53\'s aside), then the anomie paragraph and your '
          'screenshot (46 a), each checked alone and in the section.\n'
          '- 🔵 Then your 45 a: the humanized article becomes the registered master, with a record of the change.\n')
assert page.count(UP_OLD) == 1
PROMOTED = (C.parent / 'master.md').exists()
UP_NEW = ('' if S2 else '- 🔵 Section 2, once question 56 is settled: your opening, then the anomie paragraph and your screenshot '
          '(46 a), each checked alone and in the section.\n') + ('' if PROMOTED else '- 🔵 Then your 45 a: the humanized article '
          'becomes the registered master, with a record of the change.\n')
page = page.replace(UP_OLD, UP_NEW)
(C / 'OWNER-QUESTIONS.md').write_text(page, encoding='utf-8')
print('wrote OWNER-QUESTIONS.md; section 2:', S2, '; section 8 in:', IN['S8v32'], '; promoted:', PROMOTED)
