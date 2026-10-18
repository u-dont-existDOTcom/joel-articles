"""The questions page after Joel's message of 2026-10-17 21:37 UTC (45 to 51): his answers in Decided with what was done and the
checks (batches 421g to 424g), and the new questions 52 to 54. Built from the page as published at 08ca113a (version 13), so a
second run doesn't add the new items twice. Run from candidate/: python3 fix-20261017d/make_questions.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import section  # noqa: E402

R = {}
for b in ('b421', 'b422', 'b423', 'b424'):
    f = HERE / b / ('%s-results.json' % b)
    if f.exists():
        r = json.loads(f.read_text(encoding='utf-8'))
        al = HERE / b / 'aliases.json'
        for k, v in (json.loads(al.read_text()) if al.exists() else {}).items():
            r.setdefault(k, r[v])
        R.update(r)
L = lambda k: '[check](https://www.pangram.com/history%s)' % R[k][5]
human = lambda k: R[k][0].startswith('Human') and R[k][3].startswith('Human') and '; AI' not in R[k][3]
for k in ('S16v30', 'S15v15', 'S8v31', 'S13v36', 'S13v37b', 'S15v17'):
    assert human(k), k
for k in ('S2v34', 'S2v34a', 'S2v34b', 'S16v31', 'S13v37', 'S13v37a'):
    assert not human(k), k
page = subprocess.run(['git', 'show', '08ca113a:articles/intentional-communities/candidate/OWNER-QUESTIONS.md'], cwd=C,
                      capture_output=True, text=True, check=True).stdout
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
s13_words = len(section(art, '# Your Little Forming Group Already Is the Community').split())
s13_before = len(section((C / 's13' / 'v35.md').read_text(encoding='utf-8'), '# Your Little Forming Group Already Is the Community').split())
S15_DONE = (C / 's15' / 'v18.md').exists() and (C / 's15' / 'v18.md').read_text(encoding='utf-8').strip() in art
S15_TRIED = 'S15v18' in R

OLD_HEAD = re.search(r'Last updated 2026-10-17 in the evening, after your message of 19:14.*?what\'s coming up next\.\n', page, flags=re.S).group(0)
NEW_HEAD = ('Last updated 2026-10-17 at night, after your message of 21:37 (your answers to 45 to 51): they\'re done (Decided, below), '
            'except your section 2 paragraph and the anomie paragraph, which wait on section 2\'s first paragraph (question 52), and '
            'the master, which waits on those. **Open questions: 3** (52 to 54). Every question is here at the top, numbered, with '
            'its options; nothing further down needs an answer. To answer, reply in chat with the number and the letter (for '
            'example "52 a"), or in your own words. Below the questions: what\'s for you to do, what you decided and what I did '
            'about it, and what\'s coming up next.\n')
assert page.count(OLD_HEAD) == 1
page = page.replace(OLD_HEAD, NEW_HEAD)

a = page.index('## Open questions')
b = page.index('## For you to do')
OPEN = ('## Open questions\n\n'
        '> [!IMPORTANT]\n'
        '> Three questions. Each quotes its passage; the section 8 page sent with this message shows question 54\'s in place.\n\n'
        '**🟣 52. Section 2: your paragraph and the anomie paragraph wait on the first paragraph.** Your fixed paragraph reads Human '
        'alone (%s) and with the paragraph after it (%s), and the anomie paragraph reads Human alone (%s) and with the one after it '
        '(%s). But with your paragraph in, Pangram splits off the section\'s first paragraph, which didn\'t change, and reads it '
        'AI (section 2 Mostly Human, 0.31, %s):\n\n'
        '> Suddenly the longing behind my father’s movie is everywhere again, and in 2023 the U.S. Surgeon General even put out an '
        'advisory about it. Or about the loneliness under it, at least. The advisory said roughly half of American adults experience '
        'loneliness, and it treated social connection as a public-health issue.\n\n'
        'With the anomie paragraph after yours as well, the AI window runs from the heading into the paragraph after the Google Trends one '
        '(0.36, %s), and with your screenshot and caption too there are three AI windows (0.36, %s). So your 46 a ("once section 2 '
        'reads 100%% Human with it") and your new paragraph aren\'t in yet: section 2 is as it was, "starvin\'" and all, and the '
        'screenshot is still in section 12. That first paragraph is my rewrite of your published "The longing that shaped my '
        'father\'s film is suddenly everywhere again. ..."\n'
        '- a) Your words for it; I check it alone and in the section, with your paragraph, then with the anomie paragraph and the '
        'screenshot. **My pick**: your rewrites have read Human every time today.\n'
        '- b) I rework it myself, through the checks, and bring it back.\n'
        '- c) Leave section 2 as it is for now (the master then goes ahead without your new paragraph).\n\n'
        'If you don\'t answer, b.\n\n'
        % (L('S2v34-P2'), L('S2v34a-P2+next'), L('S2v34-A46'), L('S2v34-A46+next'), L('S2v34a'), L('S2v34b'), L('S2v34')) +
        '**🟣 53. Section 2, your aside: the rule isn\'t the Geneva Convention.** "(it\'s literally classified as torture by the UN\'s '
        'Geneva Convention)": the Geneva Conventions are the laws of war. The UN rules you mean are the Nelson Mandela Rules, its '
        'rules for prisoners: rule 43 bans prolonged solitary confinement, which rule 44 defines as 22 hours a day or more without '
        'meaningful human contact for more than 15 days in a row, among punishments that may never "amount to torture" or other '
        'cruel treatment ([rules 43 and 44](https://www.solitaryconfinement.org/un-nelson-mandela-rules)). The aside goes in with '
        'your paragraph (question 52).\n'
        '- a) "(it\'s literally classified as torture in the UN\'s rules for prisoners)", with that link on "the UN\'s rules for '
        'prisoners". **My pick**: your words, with only the name changed.\n'
        '- b) "(the UN\'s Mandela Rules literally ban it, along with torture)".\n'
        '- c) Your words.\n\n'
        'If you don\'t answer, a.\n\n'
        '**🟣 54. Section 8, your 49: a report from a kid who lies a lot.** You kept "Make sure kids understand what they say will be '
        'taken seriously if they are known to be honest." on purpose ("dishonesty is a reason to dismiss the report"). This one is '
        'my own concern, not the reader\'s: when a kid reports that someone is hurting them, child-protection practice is to look '
        'into it every time, even when the kid lies a lot, because people who abuse kids often pick the ones who won\'t be believed. '
        '"Dismiss" can read as "don\'t check".\n'
        '- a) Keep it as you wrote it.\n'
        '- b) A sentence after it, in your words, something like "That doesn\'t mean ignoring a kid who says someone\'s hurting '
        'them. You still check." **My pick.**\n'
        '- c) Your words, some other way.\n\n'
        'If you don\'t answer, a.\n\n')
page = page[:a] + OPEN + page[b:]

OLD_DO = re.search(r'- 🟠 Merge when you\'ve looked at the pages:.*\n', page).group(0)
NEW_DO = ('- 🟠 Merge when you\'ve looked at the pages: `gh pr merge 189 -R u-dont-existDOTcom/joel-articles --merge` ([the pull '
          'request](https://github.com/u-dont-existDOTcom/joel-articles/pull/189)). It has the evening\'s and tonight\'s changes, from '
          'your 17:16, 19:14 and 21:37 messages; the overnight run and the afternoon\'s are in already (you merged them at 15:49 UTC).\n')
page = page.replace(OLD_DO, NEW_DO)

s15 = ('"Kind of the opposite problem." (the tag "isn\'t it?" out) and "Can you believe it?" out after your "they won\'t let me '
       'pay rent!"')
if S15_DONE:
    s15 += ', and "So which is it? Well, in a way, it\'s both." out, since your new first paragraph already answers it'
held = ('Two rewordings stay as they are, because each took out its paragraph\'s only break, and that check still holds a rewording: '
        '"Why bother?" (section 13) and "So what about the families?" (section 15).' if S15_DONE else
        ('Two rewordings stay as they are, because each took out its paragraph\'s only break, and that check still holds a rewording: '
         '"Why bother?" (section 13) and "So what about the families?" (section 15). And "So which is it? Well, in a way, it\'s '
         'both." stays, though your new first paragraph already answers it: cut, the paragraph read AI with your law paragraph before '
         'it (0.95, %s), though Human with the one after (%s) and the section 100%% Human (%s). By your borderline rule (a paragraph that '
         'passes only beside a strong neighbor has to pass without it), it stays. A line of yours in its place would do it, if you\'d '
         'like it gone.' % (L('S15v18-p3+prev'), L('S15v18-p3+next'), L('S15v18'))) if S15_TRIED else
        'Three rewordings stay as they are, because each took out its paragraph\'s only break, and that check still holds a '
        'rewording: "Why bother?" (section 13), "So what about the families?" and "So which is it? Well, in a way, it\'s both." '
        '(section 15). The last asks again what your new first paragraph answers, so I\'m checking it cut (Coming up).')
DEC = (
    '- 🟢 2026-10-17 21:37 UTC, your answers to 45 to 51:\n'
    '  - 45 a, "Accept it all (sections 1 to 16 and the appendix) once 46 to 51 are settled": the master file and the record of the '
    'change are ready, and they go in once section 2 is settled (question 52). Until then your published text stays the master.\n'
    '  - 46 a: not in yet. Section 2 doesn\'t read 100%% Human with the anomie paragraph (question 52).\n'
    '  - 47, point 1, "remove one is enough": done. Section 16\'s practice paragraph now says "Get through at least one disagreement '
    'too, and keep your commitments. You can talk about a shared future later." It reads Human with the paragraph before it (%s), '
    'and the section 100%% Human (%s). With the paragraph after it, Pangram read that paragraph\'s list of groups AI (%s); that '
    'paragraph, unchanged, reads Human with its own next one, so every paragraph there passes with a neighbor.\n'
    '  - Point 2, "Really, go!": kept. Point 3, "use the version that passed": kept as it is.\n'
    '  - Point 4, your rewrite of "All is not well in paradise": in as you wrote it, with "No, not quite." given its period, '
    '"favort" spelled "favor", and the law link kept after "March 2026". Your first paragraph with your second reads Human (%s), your '
    'second alone (%s), and section 15 100%% Human (%s). You\'re right that the "!" made it blunter, not softer: the reader had it '
    'backwards.\n'
    '  - Point 5, your section 2 paragraph: waits on questions 52 and 53. On "starvin\'": the dropped g came from Emulate, the '
    'kind of thing your section 5 rule calls cheating, and your version doesn\'t need it. What I meant by "didn\'t have a turn": '
    'none of my rewordings had a break in the thought, a sentence where the writer reacts, jokes or steps aside instead of making '
    'the next point, so the check I run before Pangram stopped them.\n'
    '  - "Trust me on this one.": stays.\n'
    '  - 48 a: done in section 13, each change checked alone and in the section:\n'
    '    - the conflict paragraph has two of its three "dealt with it" out and no capitals: "and really dealt with it. Not by writing out a '
    'vision statement and shaking hands ..." and "Dealing with it for real includes the relational pl/ork ...";\n'
    '    - "And how will you handle the visibility of what the community has? A money-free community still has scarce things and '
    'bottlenecks, sorry." (your published "A money-free community still has scarce things and bottlenecks." back, with the "sorry" the line had);\n'
    '    - the provisional-membership questions folded together: "Write down your answers: How long is a provisional membership, and '
    'what are a provisional member\'s rights and responsibilities? How is it reviewed, and how does someone leave it? ...";\n'
    '    - the repeat of your section 9 out ("But when power had crept up in their own system over the years, it took them a long '
    'review to push it back down.");\n'
    '    - and three lines the whole-article reader called padding: "Honestly?" before the book line, "Why wouldn\'t they be?", and '
    '"Yeah, it\'s tough. It\'s also true."\n'
    '    - "Very important!" and "Lots of decisions to make!" stay, as you said. So do "It may sound cheesy, but it\'s true all the '
    'same." and "Until then, what\'s it worth?": with those two out as well, Pangram read three windows of the section AI (%s), and '
    'with the other cuts only, 100%% Human (%s).\n'
    '    - Your test of those two exclamation cuts showed the check I run before Pangram was wrong about cuts: it had held both because '
    'each was its paragraph\'s only break, and you found it made no difference. So a cut now goes to Pangram whatever that check '
    'says (it\'s in the shared rules), which is how the three padding cuts got in.\n'
    '    - Section 13 is %s words now, from %s before this pass (the published has 1,327).\n'
    '  - 49: points 2 and 3 done in section 8: "If it can\'t, it can still avoid punishing departure." is back after the '
    'transition help, and "Amish young people, from about age 16, go through a period of freedom from parental control called '
    'Rumspringa." The Rumspringa paragraph reads Human (%s), the skills paragraph alone (%s) and with the one after it (%s), and '
    'section 8 100%% Human (%s). Points 1 and 4 stay as you wrote them (question 54 has one thing of mine on point 1).\n'
    '  - 50 a: kept yours. The gate line was my wrong guess; your point is already in section 11: "In general, people can have their '
    'own private practices, of course. But some practices go too far against the communal spirit. If someone starts worshipping '
    'Satan, say, they get booted."\n'
    '  - 51 a: done with 48 in section 13, and in section 15: %s. Section 15 reads 100%% Human (%s). "PLUS goats" stays. Section '
    '16\'s "CAN" stays: with "can", Pangram read a window about 300 words further on AI (%s), and the section reads 100%% Human '
    'with "CAN". %s\n'
    % (L('S16v30-H3P2+prev'), L('S16v30'), L('S16v30-H3P2+next'), L('S15v15-H2P1+next'), L('S15v15-H2P2'), L('S15v15'),
       L('S13v37'), L('S13v37b'), format(s13_words, ','), format(s13_before, ','), L('S8v31-rumspringa'), L('S8v31-skills'), L('S8v31-skills+next'),
       L('S8v31'), s15, L('S15v18' if S15_DONE else 'S15v17'), L('S16v31'), held))
d = page.index('> Answered, with what I did.')
d = page.index('\n', d) + 1
page = page[:d] + '\n' + DEC + page[d:].lstrip('\n')

OLD_UP = '- 🔵 When you accept (question 45): the humanized article becomes the registered master, with a record of the change.\n'
assert page.count(OLD_UP) == 1
NEW_UP = ('- 🔵 Section 2, once question 52 is settled: your paragraph (with question 53\'s aside), then the anomie paragraph and your '
          'screenshot (46 a), each checked alone and in the section.\n'
          '- 🔵 Then your 45 a: the humanized article becomes the registered master, with a record of the change.\n')
if not S15_DONE and not S15_TRIED:
    NEW_UP += ('- 🔵 Section 15: "So which is it? Well, in a way, it\'s both." cut, since your new first paragraph answers it; '
               'the meaning checks first, then Pangram, alone and in the section.\n')
page = page.replace(OLD_UP, NEW_UP)
(C / 'OWNER-QUESTIONS.md').write_text(page, encoding='utf-8')
print('wrote OWNER-QUESTIONS.md', len(page), 'chars; section 13:', s13_words, 'words; section 15 cut done:', S15_DONE)
