"""The guide's references put back to his published post's facts and formatting where Emulate changed them mechanically.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/fix_citations.py

Emulate's run HG40-fxw1 (fix-20261018/emu-r/) rewrote Appendix K, and its output went in with the book titles in plain
type, "Healing the Divided Self , ... (1995) pp" and commas between a link and its verb; the EFT paragraph's
"randomized controlled trials" became "randomized control trials". His published post (source/published-20260928.md)
has the titles in italics and the term right. Only those marks and that word change here; the changes of meaning the
check found (who wrote the ISH article, "several" studies become "a few", the topic of Trauma and Memory's chapter 7)
are on the marking page for his decision.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
GUIDE = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
FIXES = [
    ('found 7 randomized control trials', 'found 7 randomized controlled trials'),
    ('Healing the Divided Self, Maggie Phillips and Claire Frederick, (1995) pp 24-27, 45-50, 83-90, covers',
     '*Healing the Divided Self*, Maggie Phillips and Claire Frederick (1995), pp 24-27, 45-50, 83-90, covers'),
    ('see Healing the Divided Self, Phillips and Frederick, 1995, pp 53 - 57, 96 - 100, as well as',
     'see *Healing the Divided Self*, Phillips and Frederick, 1995, pp 53-57, 96-100, as well as'),
    ('comes from In an Unspoken Voice, Peter Levine, 2010, especially ch 5 and 7, as well as ch 3 and 4 of Freedom from Pain, '
     'Levine and Maggie Phillips 2012, and ch 4 of Healing Trauma, by Levine.',
     'comes from *In an Unspoken Voice*, Peter Levine, 2010, especially ch 5 and 7, as well as ch 3 and 4 of *Freedom from '
     'Pain*, Levine and Maggie Phillips, 2012, and ch 4 of *Healing Trauma*, by Levine.'),
    ('taken from Healing the Divided Self, Phillips and Frederick, 1995, pp 148-153, 171-174,',
     'taken from *Healing the Divided Self*, Phillips and Frederick, 1995, pp 148-153, 171-174,'),
    ("see Trauma Through a Child's Eyes, Levine and Maggie Kline,", "see *Trauma Through a Child's Eyes*, Levine and Maggie Kline,"),
    ('Chapter 7 of Trauma and Memory, by Peter Levine, 2015,', 'Chapter 7 of *Trauma and Memory*, by Peter Levine, 2015,'),
    ('](https://www.va.gov/WHOLEHEALTHLIBRARY/tools/hypnosis.asp), contains', '](https://www.va.gov/WHOLEHEALTHLIBRARY/tools/hypnosis.asp) contains'),
    ('](https://asch.net/what-is-certification/), contains', '](https://asch.net/what-is-certification/) contains'),
]
text = GUIDE.read_text(encoding='utf-8')
for old, new in FIXES:
    assert text.count(old) == 1, old
    text = text.replace(old, new)
GUIDE.write_text(text, encoding='utf-8')
print(len(FIXES), 'fixes')
