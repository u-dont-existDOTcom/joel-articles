"""Section 16 draft v17 (2026-10-17): v16 hhhk (H3-P4 to H3-P6 from Emulate round h, which read Human in every run of three over
H3-P3 to H3-P7, 356g, 0.00 to 0.09) with H3-P3, and in one shape H3-P2, from Emulate too. Inside the whole section every v16
shape read AI from H3-P3's second sentence ("Call it that, not a commune!", mine since v13) to the section's end, and over
H2-P6's last sentence, the heading and H3-P2's question (354g to 358g); in v15 q the AI window started at the same sentence
(351g). The Emulate sentences keep their loose shape, with the published meaning put back:
- H3-P3 h, round h's call B (`emu-h/out/h02-emuB.txt`): "two or three" people (Emulate's "who are interested in the same things
  you are" cut, an addition), "handling one disagreement" (Emulate: "disagreeing"), "keeping your commitments" (Emulate:
  "committing"), and "a shared future" (Emulate: "forming a community") later, after all of it;
- H3-P3 b, round i's call B (`emu-i/out/i01-emuB.txt`, sent the whole published subsection): "Call it a practice group", the four
  skills and the shared future after them put back (Emulate kept only "Just get together regularly");
- H3-P3 j: v16's (mine);
- H3-P2 q: v15's question opening (mine); H3-P2 b: round i's call B ("Work on the inside stuff. Start the pl/ork. ..."), with the
  published "free", "and" (Emulate: "or"), "you already trust" and the audience put back ("No audience yet, though!").
The march found no break in H3-P3 h, H3-P3 b or H3-P2 b in one of its two readings (review-r32), so both H3-P3 shapes get
"One disagreement is enough!" (a break in v15's H3-P3, review-r24), and H3-P2 b waits (H3-P2 q has its break).
Writes v17.md and v17-variants.json. Run from this folder: python3 make_v17.py P3 P2 (for example: h q, h b, b q)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
p3 = sys.argv[1] if len(sys.argv) > 1 else 'h'
p2 = sys.argv[2] if len(sys.argv) > 2 else 'q'
subprocess.run([sys.executable, str(HERE / 'make_v16.py'), 'hhhk'], check=True, capture_output=True)
t = (HERE / 'v16.md').read_text(encoding='utf-8')
V16 = json.loads((HERE / 'v16-variants.json').read_text(encoding='utf-8'))
V15 = json.loads((HERE / 'v15-variants.json').read_text(encoding='utf-8'))
RG = '[reparenting guide](https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided)'
HM = '[Hearthwork manual](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)'
OLD = {'H3-P2': V15['H3-P2']['q'], 'H3-P3': V16['H3-P3']}
P3 = {
 'h': ("Find two or three other people and meet regularly. This is not quite the same thing as forming a commune. Call it a "
       "practice group. Practice the skills you need to practice: listening, switching roles, handling one disagreement, keeping "
       "your commitments, etc. One disagreement is enough! You can talk about a shared future later."),
 'b': ("Get a few people together, two or three, and start practicing together. Don't call it a commune, and you don't have to "
       "actually be a commune. Call it a practice group. Just get together regularly, and learn to listen, switch roles, handle "
       "one disagreement and keep your commitments. One disagreement is enough! You can talk about a shared future after that."),
 'j': OLD['H3-P3'],
}
P2 = {
 'q': OLD['H3-P2'],
 'b': ("Work on the inside stuff. Start the inner pl/ork. Read the free %s and %s, or something else equally serious that you "
       "already trust, and start practicing. No audience yet, though!" % (RG, HM)),
}
for k in OLD:
    assert t.count(OLD[k]) == 1, k
t = t.replace(OLD['H3-P3'], P3[p3]).replace(OLD['H3-P2'], P2[p2])
(HERE / 'v17.md').write_text(t, encoding='utf-8')
(HERE / 'v17-variants.json').write_text(json.dumps({'old': OLD, 'H3-P3': P3, 'H3-P2': P2, 'shape': [p3, p2]}, ensure_ascii=False,
                                                   indent=1) + '\n', encoding='utf-8')
print('wrote v17.md in shape', p3, p2)
