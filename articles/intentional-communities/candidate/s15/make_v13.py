"""Section 15 draft v13 (2026-10-17 13:11 UTC): v12 (in the article since the overnight run) with Joel's corrections of 13:11
(joel-20261017/joel-20261017-1311-message.txt), each in his words:
- "All is not well in paradise" P2: "the french word apology should have been translated as "advocacy" and it doesn't need to be
  in quotes. and then we can remove the ", along with certain financing or support meant to promote it." as that sounds
  redundant." (The published text quoted the law's French term, "apologie", as "apology".)
- "Lessons from the Black Tax" P4 (the page counts the video as P2): "you replaced "this is " with "it's"... "this" is not the
  same as "it"..." The published sentence opens "This is also the boundary problem ...".
- P6: "for p6 at the end you added "i like that." why? I actually don't know that i like that ... I'd rather say that... i
  understand the motivation to negotiate like that but i think it's not a full solution either." His sentence in place of
  "I like that.", with capital I's and a comma before "but".
Writes v13.md. Run from this folder: python3 make_v13.py"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v12.md').read_text(encoding='utf-8')
CH = [
    ('and it also made public "apology" for homosexuality a crime, along with certain financing or support meant to promote it.',
     'and it also made public advocacy for homosexuality a crime.'),
    ("It's also the thorny boundary issue of living without money inside a money-based society.",
     "This is also the thorny boundary issue of living without money inside a money-based society."),
    ("but at least now it's something they can name and negotiate. I like that.",
     "but at least now it's something they can name and negotiate. I understand the motivation to negotiate like that, but I "
     "think it's not a full solution either."),
]
for old, new in CH:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
(HERE / 'v13.md').write_text(t, encoding='utf-8')
print('wrote v13.md')
