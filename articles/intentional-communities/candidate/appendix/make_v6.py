"""The appendix, draft v6 (2026-10-17): v5 (Orlov o1, numbered inline: Human with Rubin in 334g, 0.22; o2 read Human too,
0.13, and o1 is the closer to the published) with the research paragraph in two more shapes, after four read AI alone (331g
0.84, 334g r1 0.79 and r2 0.89; the published, in G, 0.98). Both put the author in front, the way the rest of the article
talks ("I did a ton of research for this, by the way"; Emulate's call B: "If you're curious about how I came to these
conclusions"), and keep the published claims: a much larger source audit than fits in the article, the report's evidence
base, limits, counterexamples and what he still couldn't verify, and the report as the way to inspect the research without
a 200-row ledger in the article.
- r3: "I did a ton of research for this, by the way: ..." ending on the ledger, "Phew!" and an emoji (ending on the
  ledger and the emoji alone, the march found no break in either reading, review-r5);
- r4: "If you're curious how I got to all this, ..." ending on "Can you imagine?" and an emoji.
v6 is o1 with r3, v6x o1 with r4. Writes v6.md, v6x.md and v6-variants.json. Run from this folder: python3 make_v6.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v5.py')], check=True, capture_output=True)
t = (HERE / 'v5.md').read_text(encoding='utf-8')
RU = 'https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/'
R1 = json.loads((HERE / 'v5-variants.json').read_text(encoding='utf-8'))['variants']['r1']
assert t.count(R1) == 1
V = {
 'r3': ("I did a ton of research for this, by the way: a much bigger source audit than would comfortably fit in an article. The "
        "[public research report](%s) has the evidence base and its limits, the counterexamples, and what I still couldn't "
        "verify. That way you can check my work, and this article doesn't turn into a 200-row ledger. Phew! 😅" % RU),
 'r4': ("If you're curious how I got to all this, the research behind it was a much bigger source audit than would comfortably "
        "fit in an article. It's all in the [public research report](%s), with the evidence base and its limits, the "
        "counterexamples, and what I still couldn't verify. So you can check it yourself, and this article doesn't have to be a "
        "200-row ledger. Can you imagine? 😂" % RU),
}
(HERE / 'v6.md').write_text(t.replace(R1, V['r3']), encoding='utf-8')
(HERE / 'v6x.md').write_text(t.replace(R1, V['r4']), encoding='utf-8')
(HERE / 'v6-variants.json').write_text(json.dumps({'old': R1, 'variants': V, 'v6': 'r3', 'v6x': 'r4'}, ensure_ascii=False,
                                                  indent=1) + '\n', encoding='utf-8')
print('wrote v6.md (r3) and v6x.md (r4)')
