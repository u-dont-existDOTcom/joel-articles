"""Section 13 v35 (2026-10-17, after Joel's message of 19:14 UTC, joel-20261017/joel-20261017-1914-message.txt): "i agree with
your excl 13 14 ideas", the exclamations list sent with question 48 (fix-20261017b/excl-13-14.md), his 43 applied to section 13
one exclamation at a time. Section 14 keeps all of its own (the list), so it doesn't change.
The list covered 22 of section 13's exclamations; two more were missed because each has an emoji after its mark (the
visitor-to-member subsection's "Not exactly a high bar! 😅" and "(Hint: not the person who recruited them! 😜)"). The first gets
the list's own treatment for a deadpan line whose feeling is carried by something else (row 7: the mark only), the emoji staying;
the message says so, so he can keep it. The second stays as it is (HELD, below).
Taken back after the march reads (HELD): the cuts of "Very important!" and "Lots of decisions to make!", each its paragraph's
only break in both readings; those two paragraphs go to him.
Kept, as the list says: "That's okay!", "(And who owns the land!)", "Being open to everybody felt so spiritual!", "(Hopefully not
all at once!)", and the quoted visitor's own ("Wow! Look at this beautiful land! ...").
Writes s13/v35.md from s13/v34.md (the installed text) and fix-20261017c/excl-changes-13.json.
Run from candidate/: python3 fix-20261017c/make_s13_v35.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
# (where, kind, old, new, why); "where" is the subsection and the paragraph under it, as the list names them
CHANGES = [
    ('Opening P3', 'cut', 'That’s okay! There’s lots you can do!', 'That’s okay!',
     'list row 1: keep "That\'s okay!" (reassurance; with a period it reads curt); the phrase "There\'s lots you can do!" goes, '
     'since the next sentence says what'),
    ('Opening P4', 'period', 'This is the boring stuff!', 'This is the boring stuff.', 'list row 2: wry, reads right either way'),
    ('Values P2', 'period', 'Bring your values with you when you go to visit a community!',
     'Bring your values with you when you go to visit a community.', 'list row 3: advice'),
    ('Values P2', 'period', 'It’s a long list, I know!', 'It’s a long list, I know.',
     'list row 4: it answers the list just given'),
    ('Values P4', 'period', 'That’s a real value too!', 'That’s a real value too.', 'list row 5'),
    ('Values P5', 'period', 'but the view isn’t going anywhere!', 'but the view isn’t going anywhere.', 'list row 7: deadpan works'),
    ('Resources P3', 'period', 'There will be bottlenecks, sorry!', 'There will be bottlenecks, sorry.', 'list row 10'),
    ('Resources P4', 'period', "You don't want them to lose everything they've put in!",
     "You don't want them to lose everything they've put in.", 'list row 11'),
    ('Resources P4', 'period', 'happens to have spare money!', 'happens to have spare money.', 'list row 12'),
    ('Resources P4', 'period', 'Not romantic, but protective!', 'Not romantic, but protective.', 'list row 13'),
    ('Visitor to Member P2', 'period', '(Not everyone does!)', '(Not everyone does.)', 'list row 15'),
    ('Visitor to Member P3', 'period', 'Not exactly a high bar! 😅', 'Not exactly a high bar. 😅',
     'missed by the list (the emoji after the mark): deadpan, the 😅 carries the feeling, as in row 7'),
    ('Visitor to Member P4', 'period', 'pull off an act for months!', 'pull off an act for months.', 'list row 17'),
    ('Visitor to Member P7', 'period', 'just because they’re great with kids!', 'just because they’re great with kids.', 'list row 18'),
    ('Visitor to Member P8', 'period', "(Sorry, hanging out doesn't count! I know, it's the fun part.)",
     "(Sorry, hanging out doesn't count. I know, it's the fun part.)", 'list row 19'),
    ('Visitor to Member P9', 'period', '(yes, even interns!)', '(yes, even interns)', 'list row 20: the mark only'),
    ('When Somebody Has to Go P3', 'period', "The key is that it's not the same people!", "The key is that it's not the same people.",
     'list row 21'),
]
# Taken back after the march (fix-20261017c/march-r1, both readers): each was its paragraph's only break, so the cut leaves a
# run of steps (E173; his 43: "give me the paragraph and i'll help"); the two phrases go to him (the questions page), and the
# hint, one the list missed, stays as it is (one reader found no break in that paragraph before or after, the other one in both).
HELD = [
    ('Resources P1', 'cut', 'Who will have title to the land? Very important! Whoever',
     'Who will have title to the land? Whoever', 'list row 8: "Very important!" goes; the next sentence says why'),
    ('Resources P2', 'cut', 'wants to leave the community. Lots of decisions to make!', 'wants to leave the community.',
     'list row 9: the phrase goes'),
    ('Visitor to Member P5', 'period', '(Hint: not the person who recruited them! 😜)', '(Hint: not the person who recruited them 😜)',
     'missed by the list (the emoji after the mark): the mark only, the 😜 stays (his 33 a), as in row 20'),
]

# Kept, as the list says (and the two quoted voices, which keep all of theirs)
KEPT = ['That’s okay!', '(And who owns the land!)', 'Being open to everybody felt so spiritual!', '(Hopefully not all at once!)']
QUOTES = [r'“Wow!.*?”', r'“Wait, there’s a vaccination policy.*?”']


def accounted(md):
    """Every "!" in the section outside the two quoted voices is in a change, a held change or a kept line: the list he agreed to
    missed two (each with an emoji after the mark), and a count in code would have caught it."""
    import re
    spans = [m.span() for q in QUOTES for m in re.finditer(q, md, flags=re.S)]
    for o in [c[2] for c in CHANGES + HELD] + KEPT:
        spans += [m.span() for m in re.finditer(re.escape(o), md)]
    loose = [i for i, ch in enumerate(md) if ch == '!' and not any(a <= i < b for a, b in spans)]
    return loose


if __name__ == '__main__':
    md = (C / 's13' / 'v34.md').read_text(encoding='utf-8')
    loose = accounted(md)
    assert not loose, ['...' + md[max(0, i - 50):i + 5] for i in loose]
    before = md.count('!')
    for where, kind, old, new, why in CHANGES:
        assert md.count(old) == 1, (where, old)
        md = md.replace(old, new)
    (C / 's13' / 'v35.md').write_text(md, encoding='utf-8')
    (HERE / 'excl-changes-13.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('s13/v35.md written:', len(CHANGES), 'changes;', before, '->', md.count('!'), 'exclamation marks in the file')
