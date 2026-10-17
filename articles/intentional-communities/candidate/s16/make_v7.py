"""Section 16 draft v7 (2026-10-17): v6 with H1-P2 as in v5 and two stretches rebuilt from Emulate round c (emu-c/out/, each
stretch sent whole), the published meaning put back inside Emulate's sentences.
- H1 (round c's c01): call B turns the wrong order into the mistaken plan's own voice, a numbered list of exclamations ("1. Get
  the land! 2. Ok, now write that vision thing down! ..."), and the better order the same way; call A does the first list as
  plain exclamations ("Get the land first! Put the vision in writing!"). Two shapes of H1:
  n: H1-P1 and H1-P2 numbered, in call B's voice, with every published step and Joel's own words for his order ("decide
     ownership and exit", which the key check holds; B: "How do you want to own it? How will you get out ...?"; wrong order,
     not B's "reverse";
     the money deciding ownership, which both calls lost; "clarify values" and "test membership", for B's "write down some
     values" and "do you want to be members"; "consider land", for B's "get some land");
  e: H1-P1 as call A's exclamations, with the published four (A lost the money), and H1-P2 as in v5 (it read Human with H1-P3,
     328g, 0.34).
  H1-P3 in both: call B's "don't try to fly straight there!" with the published conditions and the impure-money contrast inside
  the sentence (its end read AI inside H1 in every version since v4); "the tax bill" (B: "your tax bill"), and none of B's
  "IF YOU WANT TO" (an added choice).
- H3-P4 (c03, call B): the possible places as questions ("Are there any unprogrammed Quaker meetings or restorative-practice
  groups near you? ..."), the person back from a long retreat kinder, "rather than more impressed with themselves", the last.
Writes v7.md and v7-variants.json. Run from this folder: python3 make_v7.py [n|e]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
choice = sys.argv[1] if len(sys.argv) > 1 else 'n'
subprocess.run([sys.executable, str(HERE / 'make_v6.py')], check=True, capture_output=True)
t = (HERE / 'v6.md').read_text(encoding='utf-8')
fx = json.loads((HERE / 'v6-fixes.json').read_text(encoding='utf-8'))
P2_V5_FIRST, P2_V6_FIRST = fx[0]['old'], fx[0]['new']
P1 = ("Most people building community go about it in the wrong order. They get the land first, then write the vision down in a "
      "document, then let whoever had the money end up owning it. And the emotional preparation? That gets put off until later, "
      "when everyone has more time.")
P2 = P2_V6_FIRST + " I know, it wouldn't make much of a movie!"
P3 = ("Likewise, the economic side should go in stages. You shouldn't try to fly straight to the economic destination! Only after "
      "the group has proven it can reliably provide for everybody, and fairly decide who gets what from the common, should it move "
      "to a common purse. And cutting back on outside money, or getting rid of it, should come from what the group has shown it "
      "can do. (\"Money is impure!\" is a weird thing to say while somebody else is quietly paying the tax bill.)")
P4 = ("Where might you find them? Maybe among unprogrammed Quakers, restorative-practice groups, open-hearted congregations, mature "
      "recovery groups or meditation groups. Or people who came back from a long retreat kinder, rather than more impressed with "
      "themselves.")
for x in (P1, P2, P3, P4):
    assert t.count(x) == 1, x[:50]
NEW_P3 = ("The money side should go in stages too: don't try to fly straight to the economic destination! Only once the group can "
          "reliably provide for everybody, and fairly decide who gets what from the common, should it move to a common purse. And "
          "cutting back on outside money, or getting rid of it, should come from what the group has shown it can do, rather than "
          "from deciding that \"money is impure!\" (which sounds weird while somebody else is quietly paying the tax bill).")
V = {
 'n': {
  'H1-P1': ("Most people building community do it in the wrong order: 1) Get the land! 2) Write the vision down in a document! "
            "3) Let whoever had the money end up owning it. 4) And all the emotional preparation? Let's get around to that "
            "later, when everyone has more time!"),
  'H1-P2': ("The better order is less cinematic: 1) Practice together! 2) Process a real conflict! 3) Get clear on your values. "
            "4) Test membership. 5) Decide ownership and exit. 6) Only then, start thinking about "
            "land. I know, it wouldn't make much of a movie!"),
  'H1-P3': NEW_P3,
 },
 'e': {
  'H1-P1': ("Most people building community do it in the wrong order. Get the land first! Put the vision in a document! Let "
            "whoever had the money end up owning it! And the emotional preparation? That can wait until later, when everyone has more time."),
  'H1-P2': P2_V5_FIRST + " I know, it wouldn't make much of a movie!",
  'H1-P3': NEW_P3,
 },
}
NEW_P4 = ("Where do you find them? Are there any unprogrammed Quaker meetings or restorative-practice groups near you? Any "
          "open-hearted congregations? Maybe a mature recovery group, or a meditation group? Or someone who came back from a long "
          "retreat kinder, rather than more impressed with themselves?")
v = V[choice]
t = t.replace(P1, v['H1-P1']).replace(P2, v['H1-P2']).replace(P3, v['H1-P3']).replace(P4, NEW_P4)
(HERE / 'v7.md').write_text(t, encoding='utf-8')
(HERE / 'v7-variants.json').write_text(json.dumps({'H1': V, 'H3-P4': NEW_P4, 'chosen': choice}, ensure_ascii=False, indent=1) + '\n',
                                       encoding='utf-8')
print('wrote v7.md with H1', choice)
