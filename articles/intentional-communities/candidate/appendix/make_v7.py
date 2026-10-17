"""The appendix, draft v7 (2026-10-17): v6x (Orlov o1, research paragraph r4: the whole appendix 100% Human, 336g, 0.15) with
two more shapes of the research paragraph, which reads AI alone in all seven so far (r4 the closest, 0.54). Both keep r4's
opening and ending and break up the list of what the report has (every shape so far kept it as one list of three or four):
- r5: the list stays in one sentence, as a run with "etc." at its end, and "(a lot bigger!)" as an aside;
- r6: the list over two sentences ("The evidence base is in there, and where it runs out. So are the counterexamples, and the
  stuff I still couldn't verify.").
Both carry trace T3's fix of Doucleff's entry (review-r7: the published three topics, not two results).
v7 is o1 with r5, v7x o1 with r6. Writes v7.md, v7x.md and v7-variants.json. Run from this folder: python3 make_v7.py"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v6.py')], check=True, capture_output=True)
t = (HERE / 'v6x.md').read_text(encoding='utf-8')
RU = 'https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/'
R4 = json.loads((HERE / 'v6-variants.json').read_text(encoding='utf-8'))['variants']['r4']
assert t.count(R4) == 1
V = {
 'r5': ("If you're curious how I got to all this, the research behind it was a much bigger source audit than would comfortably "
        "fit in an article (a lot bigger!). It's all in the [public research report](%s): the evidence base and its limits, the "
        "counterexamples, what I still couldn't verify, etc. So you can check it yourself, and this article doesn't have to be a "
        "200-row ledger. Can you imagine? 😂" % RU),
 'r6': ("If you're curious how I got to all this, the research behind it was a much bigger source audit than would comfortably "
        "fit in an article. It's all in the [public research report](%s). The evidence base is in there, and where it runs out. "
        "So are the counterexamples, and the stuff I still couldn't verify. So you can check it yourself, and this article "
        "doesn't have to be a 200-row ledger. Can you imagine? 😂" % RU),
}
# trace T3 of review-r7: Doucleff's entry made autonomy and shared care results of the kids taking part (SHIFT); the published
# lists them as three things the book is about
D_OLD = "about kids taking part in family life, in a way that gives them autonomy and spreads out the work of caring for them."
D_NEW = "about kids taking part in family life, autonomy, and spreading out the work of caring for them."
assert t.count(D_OLD) == 1
t = t.replace(D_OLD, D_NEW)
(HERE / 'v7.md').write_text(t.replace(R4, V['r5']), encoding='utf-8')
(HERE / 'v7x.md').write_text(t.replace(R4, V['r6']), encoding='utf-8')
(HERE / 'v7-variants.json').write_text(json.dumps({'old': R4, 'variants': V, 'v7': 'r5', 'v7x': 'r6'}, ensure_ascii=False,
                                                  indent=1) + '\n', encoding='utf-8')
print('wrote v7.md (r5) and v7x.md (r6)')
