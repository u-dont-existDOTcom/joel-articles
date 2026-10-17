"""Section 16 draft v19 (2026-10-17): v18 erk (H3-P5 ending on Emulate's "Check their requirements first.") with H3-P6 in three
more shapes. With H3-P5's end changed alone, the subsection read Mostly Human, its one AI window H3-P6's first sentence (362g,
37 words: "By visiting some communities, you'll get a better idea of things no manifesto can tell you, like how much togetherness you
enjoy, what kind of privacy you need, and what kind of labor system irritates you.", my restoration around Emulate's list,
https://www.pangram.com/history/5e1f916b-37b9-49e0-92df-c9726dddad08). Emulate's whole run-on list (v18's b) read worse (363g to
365g). The shapes, each with the published items (how much togetherness you enjoy, what kind of privacy you need, the labor
system that irritates you, showers liberating or the studio apartment) and "no manifesto":
- d: v18's sentence without "things no manifesto can tell you, like", the list split two and one ("how much togetherness you
  enjoy and what kind of privacy you need, and what kind of labor system irritates you"), its showers sentence, and the
  manifesto after them ("No manifesto is going to tell you any of that.");
- g: round i's call C (`emu-i/out/i01-emuC.txt`: "When you do that you will get a much better idea of ..."), its studio-apartment
  joke kept ("you'd rather spend all your money on a studio apartment"), the published items in it, and the manifesto after it;
- h: round i's call A (`emu-i/out/i01-emuA.txt`: "These visits will help you find out what you like and don't like about ..."),
  with "etc." kept, the published items in it, and the manifesto after it ("You're not going to find that stuff in any
  manifesto!"; the shorter "No manifesto can tell you that stuff!" made half of H3's paragraphs end on a short line);
- r: v18's.
Writes v19.md and v19-variants.json. Run from this folder: python3 make_v19.py P6 P3 (for example: d h)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
p6 = sys.argv[1] if len(sys.argv) > 1 else 'd'
p3 = sys.argv[2] if len(sys.argv) > 2 else 'h'
subprocess.run([sys.executable, str(HERE / 'make_v18.py'), 'erk', p3], check=True, capture_output=True)
t = (HERE / 'v18.md').read_text(encoding='utf-8')
V18 = json.loads((HERE / 'v18-variants.json').read_text(encoding='utf-8'))
OLD = V18['P6'][0]
P6 = {
 'd': ("By visiting some communities, you'll get a better idea of how much togetherness you enjoy and what kind of privacy you "
       "need, and what kind of labor system irritates you. And whether communal showers feel liberating, or you'll start looking "
       "at studio apartments for rent right after the first communal shower you take! No manifesto is going to tell you any of "
       "that."),
 'g': ("When you do that, you'll get a much better idea of how much togetherness you really enjoy, what kind of privacy you need, "
       "what kind of labor system irritates you, and whether communal showers feel liberating or you'd rather spend all your money "
       "on a studio apartment. No manifesto is going to tell you any of that!"),
 'h': ("These visits will help you find out what you like and don't like about togetherness, what kind of privacy you need, "
       "which labor systems irritate you, whether communal showers feel liberating or make you start pricing studio apartments, "
       "etc. You're not going to find that stuff in any manifesto!"),
 'r': OLD,
}
assert t.count(OLD) == 1
t = t.replace(OLD, P6[p6])
(HERE / 'v19.md').write_text(t, encoding='utf-8')
(HERE / 'v19-variants.json').write_text(json.dumps({'old': OLD, 'H3-P6': P6, 'shape': [p6, p3]}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v19.md in shape', p6, p3)
