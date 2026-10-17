"""The appendix, draft v5 (2026-10-17): v4 with the two entries that read AI in 331g in two shapes each. Both carry a list of
four, and Joel's way with a list is to split it into sentences (2026-10-07) or, in his own section 4, to number it inline
("1) inner pl/ork (reparenting), 2) relational pl/ork ..., and 4) the practical logistical foundation").
- Orlov (with Rubin, 0.25 AI; Rubin with Kanter read Human): o1 numbers the four things long-lasting communities often rely
  on, inline; o2 splits them over two sentences, the second an exclamation.
- The research paragraph (0.84 AI alone): r1 numbers what the report shows; r2 splits it over two sentences.
v5 is o1 with r1, v5x o2 with r2. Writes v5.md, v5x.md and v5-variants.json. Run from this folder: python3 make_v5.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v4.md').read_text(encoding='utf-8')
OU = 'https://philebersole.wordpress.com/2014/06/23/dmitry-orlov-on-communities-that-abide/'
RU = 'https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/'
OLD_O = ("[***Communities That Abide***](%s) by Dmitry Orlov makes an uncomfortable argument that long-lasting communities often "
         "rely on communal property, separation, boundaries and a binding ideology. From a distance, cohesion and capture can look "
         "a lot alike." % OU)
OLD_R = ("If you're curious, I did a much bigger source audit than would comfortably fit in this article. The [public research "
         "report](%s) shows the evidence base, the limits, the counterexamples and what I still couldn't verify. That way you can "
         "check the research yourself, and this article doesn't have to turn into a 200-row ledger. Can you imagine?" % RU)
V = {
 'o1': ("[***Communities That Abide***](%s) by Dmitry Orlov makes an uncomfortable argument: the communities that last a long "
        "time often rely on 1) communal property, 2) separation, 3) boundaries and 4) a binding ideology. From a distance, "
        "cohesion and capture can look a lot alike." % OU),
 'o2': ("[***Communities That Abide***](%s) by Dmitry Orlov is uncomfortable reading. The communities that last a long time, he "
        "argues, often rely on communal property and separation. And on boundaries, and a binding ideology! From a distance, "
        "cohesion and capture can look a lot alike." % OU),
 'r1': ("If you're curious, I did a much bigger source audit than would comfortably fit in this article. The [public research "
        "report](%s) has 1) the evidence base, 2) the limits, 3) the counterexamples and 4) what I still couldn't verify. That "
        "way you can check the research yourself, and this article doesn't have to turn into a 200-row ledger. Can you "
        "imagine?" % RU),
 'r2': ("If you're curious, I did a much bigger source audit than would comfortably fit in this article. It's all in the "
        "[public research report](%s). The evidence base is there, and the limits. So are the counterexamples, and what I still "
        "couldn't verify. That way you can check the research yourself, and this article doesn't have to turn into a 200-row "
        "ledger. Can you imagine?" % RU),
}
assert t.count(OLD_O) == 1 and t.count(OLD_R) == 1
(HERE / 'v5.md').write_text(t.replace(OLD_O, V['o1']).replace(OLD_R, V['r1']), encoding='utf-8')
(HERE / 'v5x.md').write_text(t.replace(OLD_O, V['o2']).replace(OLD_R, V['r2']), encoding='utf-8')
(HERE / 'v5-variants.json').write_text(json.dumps({'old': {'orlov': OLD_O, 'research': OLD_R}, 'variants': V,
                                                   'v5': ['o1', 'r1'], 'v5x': ['o2', 'r2']}, ensure_ascii=False, indent=1) + '\n',
                                       encoding='utf-8')
print('wrote v5.md (o1, r1) and v5x.md (o2, r2)')
