"""The questions page after Joel's message of 2026-10-17 19:14 UTC ("i agree with your excl 13 14 ideas"): question 48's
exclamations done in section 13 (Decided, with the checks of 420g), the two cuts the march held back added to question 48, which
keeps the repeat and the length. Built from the page as published at 785844de (version 12), so a second run doesn't add the new
items twice. Run from candidate/: python3 fix-20261017c/make_questions.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
sys.path.insert(0, str(HERE))
from make_s13_v35 import CHANGES  # noqa: E402

R = json.loads((HERE / 'b420' / 'b420-results.json').read_text(encoding='utf-8'))
L = lambda k: '[check](https://www.pangram.com/history%s)' % R[k][5]
page = subprocess.run(['git', 'show', '785844de:articles/intentional-communities/candidate/OWNER-QUESTIONS.md'], cwd=C,
                      capture_output=True, text=True, check=True).stdout
whole = R['S13v35']
assert whole[0].startswith('Human') and whole[3].startswith('Human') and '; AI' not in whole[3], whole
v35 = (C / 's13' / 'v35.md').read_text(encoding='utf-8')
vis = re.search(r'“Wow!.*?”', v35, flags=re.S)
q2 = re.search(r'“Wait, there’s a vaccination policy.*?”', v35, flags=re.S)
outside = v35.count('!') - vis.group(0).count('!') - q2.group(0).count('!')   # the two quoted voices keep theirs
OLD_HEAD = re.search(r'Last updated 2026-10-17 in the evening, after your message of 17:16\..*?what\'s coming up next\.\n', page, flags=re.S).group(0)
NEW_HEAD = ('Last updated 2026-10-17 in the evening, after your message of 19:14 ("i agree with your excl 13 14 ideas"): section 13\'s '
            'exclamations are done (Decided, below), except two cuts that are yours now (question 48). Your 43 and 44 are done too, '
            'and so is the whole-article faithfulness pass you asked for in 45. **Open questions: 7** (45 to 51). Every question is '
            'here at the top, numbered, with its options; nothing further down needs an answer. To answer, reply in chat with the '
            'number and the letter (for example "46 a"), or in your own words. Below the questions: what\'s for you to do, what you '
            'decided and what I did about it, and what\'s coming up next.\n')
assert page.count(OLD_HEAD) == 1
page = page.replace(OLD_HEAD, NEW_HEAD)
q48a = page.index('**🟣 48. ')
q48b = page.index("If you don't answer, c.", q48a) + len("If you don't answer, c.")
old48 = page[q48a:q48b]
rep = re.search(r'^- One repeat: .*$', old48, flags=re.M).group(0)
length = re.search(r'^- Length: .*$', old48, flags=re.M).group(0)
NEW48 = ('**🟣 48. Sections 13 and 14 (accepted): two exclamation phrases, one repeat, and length.** Your "i agree with your excl 13 '
         '14 ideas" is done (Decided, below), except two of the cuts: each phrase is its paragraph\'s only turn, and without it both '
         'readers found a run of steps, so by your 43 ("give me the paragraph and i\'ll help") these two are yours. Each is still as '
         'it was:\n'
         '- Section 13, "Resources, Land, and Exit Terms": "Who will have title to the land? Very important! Whoever has it will have '
         'enormous power over the rest of the community. If the deed is in the name of the founder, then he or she is really a '
         'landlord with a philosophy. ..."\n'
         '- The next paragraph: "... how inheritance works, what about outside debt, how improvements get handled, and what happens '
         'when someone wants to leave the community. Lots of decisions to make!"\n'
         + rep + '\n' + length + '\n'
         '- a) Your lines for the two paragraphs (I check each alone and in the section), and the repeat cut and the tightening '
         'pass. **My pick.**\n'
         '- b) The repeat cut only.\n'
         '- c) Leave both sections as they are now.\n'
         '- d) Your picks.\n\n'
         "If you don't answer, c.")
page = page[:q48a] + NEW48 + page[q48b:]
marks = [n for w, k, o, n, y in CHANGES if k == 'period' and 'missed by the list' not in y]
quote = lambda s: '"%s"' % s.strip()
DEC = ('- 🟢 2026-10-17 19:14 UTC, 48: "i agree with your excl 13 14 ideas". Done in section 13, one exclamation at a time: two fresh '
       'readers read each changed paragraph for its turn, and Pangram read each changed paragraph and the whole section. Section 14 '
       'keeps all of its own, as the list said.\n'
       '  - The mark only: ' + ', '.join(quote(m) for m in marks) + '.\n'
       '  - The phrase out: "There\'s lots you can do!" ("That\'s okay!" stays before it).\n'
       '  - Kept, as the list said: "That\'s okay!", "(And who owns the land!)", "Being open to everybody felt so spiritual!", '
       '"(Hopefully not all at once!)", and the quoted visitor\'s own.\n'
       '  - Two the list missed, because each has an emoji after its mark: "Not exactly a high bar! 😅" is now "Not exactly a high '
       'bar. 😅" (the emoji carries the feeling; say if you\'d rather keep its "!"). "(Hint: not the person who recruited them! 😜)" '
       'stays as it is: the two readers split on whether that paragraph of questions has a turn at all, so I left it.\n'
       '  - Not done: the cuts of "Very important!" and "Lots of decisions to make!" (question 48).\n'
       '  - Section 13 now has %d exclamations outside the quoted visitor where it had 24, and reads 100%% Human (%s). Every changed '
       'paragraph reads Human alone or with its neighbor (the side-by-side page has each check).\n' % (outside, L('S13v35')))
d = page.index('> Answered, with what I did.')
d = page.index('\n', d) + 1
page = page[:d] + '\n' + DEC + page[d:].lstrip('\n')
(C / 'OWNER-QUESTIONS.md').write_text(page, encoding='utf-8')
print('wrote OWNER-QUESTIONS.md', len(page), '; outside the visitor:', outside)
