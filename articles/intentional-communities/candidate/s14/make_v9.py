"""Section 14 draft v9 (2026-10-17): v8 with P2 as Joel wrote it in his message of 02:07 UTC (question 38 b: "simple i just
deleted the 2nd one and it's still human on pangram"), his characters kept. His P2 drops the question about bridging
"people's food, housing and care, and any outside cash or benefits, if relevant": the repeat question 38 asked about, with
the outside cash or benefits it carried. Joel accepted sections 13 and 14 in the same message ("accept 13 and 14."), so v9
is the accepted section. Writes v9.md. Run from this folder: python3 make_v9.py"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v8.md').read_text(encoding='utf-8')
JOEL = ('If the community dissolves, what happens to the land and any outside debts? What about its buildings, equipment, '
        'common stores or funds? What happens to each member’s agreed rights? More immediately, who is responsible for '
        'ensuring that everyone has a place to live and food to eat? Who takes responsibility for making sure people get their '
        'medications and the other care they need? Who keeps childcare going, and makes sure the kids’ schooling carries on? '
        'Who takes responsibility for transportation, for the records, for family contact, for the animals, for making sure '
        'land obligations are met, and for any unresolved claims? That’s a lot of loose ends!')
msg = (HERE.parent / 'joel-20261017' / 'joel-20261017-0207-message.txt').read_text(encoding='utf-8')
assert JOEL in msg, 'his P2 must be his exact words'
old = [b for b in re.split(r'\n\s*\n', t) if b.startswith('If the community dissolves')]
assert len(old) == 1
t = t.replace(old[0], JOEL)
(HERE / 'v9.md').write_text(t, encoding='utf-8')
print('wrote v9.md')
