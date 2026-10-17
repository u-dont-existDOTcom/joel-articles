"""The fixes from the whole-article faithfulness pass (Joel's 45 of 2026-10-17 17:16 UTC: "we should do a final pass to make
sure it's faithful to the original"), with the published words wherever they fit (his rule: what got lost gets the published
words back). Only candidate sections change; findings in his own text and in the accepted sections 13 and 14 go to him as
questions (fix-20261017b/faithful/TRIAGE.md has every finding and what happened to it).
- Section 2 v3.3, P2: "starvin'" back to the published "starving". The dropped g was Emulate's, kept by me because he writes
  "poppin'" there; his rule for section 5 (2026-10-07): "unusual spellings should help pass pangram, but that's also cheating
  i'd say, so you can fix them". REPORT-A.md.
- Section 9 v17, the Escuelita evidence paragraph: the published limit back, as its own sentence: "I'm not claiming the
  Zapatistas already proved my whole model." (published: "I'm borrowing a pedagogy and a replication ambition, not claiming the
  Zapatistas already proved my whole model."). REPORT-C.md.
- Section 15 (on top of v14's exclamations): "All is not well in paradise" P3, the published judgment back in place of "It's
  interesting to see that ... whether you're allowed": "Being in community isn't automatically liberating. It all depends on
  who is allowed to belong without pretending." (published: "Community itself isn't automatically liberating. Everything
  depends on who is permitted to belong without pretending."). The Black Tax P1: "whatever prosperity came through you later"
  for "whatever you made of yourself later" (published: "whatever prosperity later came through you"; "made of yourself" is
  the self-made view the paragraph argues against). REPORT-D.md. And "No, not that either." for "No, not that either!": the
  answer opens the section on the anti-gay law, prison and mob violence, and the whole-article reader found the bluntness
  softened at the article's gravest point (REPORT-FOREST.md [12]; the published: "I don't want to turn this into Sénégal as a
  surviving communal paradise either."); his 43 swaps the mark where the sentence reads right with a period, and this one
  needs the period.
- Section 16 (on top of v29's exclamations): "If You Can't Move", the published "change how people survive" for "make a
  difference when people are going through" (published: "It can still change how people survive divorce, illness, grief,
  parenting, and ordinary loneliness."). The reader's other half, "already contains a real piece of community", stays out:
  the overnight dedup cut it under his 02:07 rule because section 13 opens with it, and he saw that listed. REPORT-D.md. And
  "rather than by declaring "money is impure!"" for "rather than because "money is impure!"": the published mocked a
  declaration made while somebody else pays ("not from declaring money impure while somebody else quietly pays the tax
  bill"), and the rewrite mocked the belief, which section 4 gives as his own ("money is antagonistic to the spirit of
  community"); his "(That sounds kind of weird when somebody else is paying the tax bill.)" follows the declaration.
  REPORT-FOREST.md [2].
- Not changed, though a reader asked: the appendix's "sequencing" (his 23:38 of 2026-10-16: "no we should not lean on
  Christian's book order if it contradicts my own order"), and section 13's book order and dedup cuts (his decisions; section
  13 is accepted). TRIAGE.md has each.
Writes s2-v3.3.md, s9-v17.md here, s15/v14.md and s16/v29.md again (make_excl.py first), and
article-with-drafts.md: HUMANIZED-SO-FAR.md with all of them in. Run from candidate/: python3 fix-20261017b/make_faithful.py"""
import pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
subprocess.run([sys.executable, str(HERE / 'make_excl.py')], check=True, capture_output=True)
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')


def bounds(md, h1):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return a, (a + 3 + m.start()) if m else len(md.rstrip('\n'))   # the appendix runs to the end


def sec(md, h1):
    a, b = bounds(md, h1)
    return md[a:b].strip()


FIXES = {
    '# Communes Are Hot Again': (HERE / 's2-v3.3.md', None, [
        ('something about the current arrangement is starvin’ them.', 'something about the current arrangement is starving them.')]),
    '# The Best Model I’ve Seen: Zapatistas': (HERE / 's9-v17.md', None, [
        ("I'm borrowing the Zapatistas' teaching method and their ambition to replicate.",
         "I'm borrowing the Zapatistas' teaching method and their ambition to replicate. I'm not claiming the Zapatistas already "
         "proved my whole model.")]),
    '# What This Looks Like From Sénégal': (C / 's15' / 'v14.md', C / 's15' / 'v14.md', [
        ("It's interesting to see that being in community isn't necessarily liberating for everyone, it all depends on whether "
         "you're allowed to belong without pretending.",
         "Being in community isn't automatically liberating. It all depends on who is allowed to belong without pretending."),
        ('had a real claim on whatever you made of yourself later.', 'had a real claim on whatever prosperity came through you later.'),
        ("that's kept its communal paradise? No, not that either! The warmth", "that's kept its communal paradise? No, not that either. The warmth")]),
    '# Practice Comes Before Property': (C / 's16' / 'v29.md', C / 's16' / 'v29.md', [
        ('It can still make a difference when people are going through a divorce, an illness or grief.',
         'It can still change how people survive a divorce, an illness or grief.'),
        ('rather than because "money is impure!"', 'rather than by declaring "money is impure!"')]),
}
out = art
for h1, (dst, src, pairs) in FIXES.items():
    text = src.read_text(encoding='utf-8').strip() if src else sec(art, h1)
    for old, new in pairs:
        assert text.count(old) == 1, (h1, old)
        text = text.replace(old, new)
    dst.write_text(text + '\n', encoding='utf-8')
    a, b = bounds(out, h1)
    out = out[:a] + text + '\n' + out[b:]
(HERE / 'article-with-drafts.md').write_text(out, encoding='utf-8')
print('wrote', ', '.join(d.name for d, _, _ in FIXES.values()), 'and article-with-drafts.md')
