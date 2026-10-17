"""The appendix, draft v3 (2026-10-17): v2 with a break in each run that batch 331g would screen. The march (review-r1, two
readings, one paragraph per run) found a break only in the Orlov and Rubin run and in the research paragraph, both readings
(the Liedloff run in one): a reading list marches, one fact after another. The gate blocks a screen without a break in every
reading (E131), so each break below is a question, a reaction or an aside that claims nothing new or carries the published
meaning in a reacting form. Joel decides whether a reading list should need them (questions page).
Writes v3.md and v3-breaks.json. Run from this folder: python3 make_v3.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v2.md').read_text(encoding='utf-8')
FIX = [
 ("For this article, the view of the grown children is essential.",
  "Why this one? For this article, the view of the grown children is essential.",
  'a question that claims nothing, before the published "essential"'),
 ("takes you on a tour of a bunch of ecovillages in Europe, and shows how many different arrangements hide under that one label.",
  "takes you on a tour of a bunch of ecovillages in Europe. How many different arrangements can hide under that one label? A "
  "lot, it turns out!",
  'the published "showing how many different arrangements hide under one label" as a question and its answer'),
 ("The Bruderhof also has a pretty extensive [YouTube channel]",
  "Oh, and the Bruderhof has a pretty extensive [YouTube channel]",
  'an aside ("Oh, and ... too"); the same fact'),
 ("](https://www.youtube.com/channel/UCr6Df5XndlMFVB43NodfUsQ).", "](https://www.youtube.com/channel/UCr6Df5XndlMFVB43NodfUsQ) too.",
  'the aside\'s "too"'),
 ("It's provocative observation, so take it with a grain of salt as anthropology.",
  "Is it settled anthropology? No, it's provocative observation, so take it with a grain of salt.",
  'the published "Read it as provocative observation rather than settled anthropology" as a question and its answer'),
 ("And for a whole-systems guide to intentional community, there's ",
  "Want a guide to intentional community that covers the whole system? There's ",
  'the published "a whole-systems guide to intentional community" as a question'),
 ("is a paper that asks whether longevity alone is a meaningful measure, when a community may keep going without its members "
  "flourishing.",
  "is a paper with this question: is longevity alone a meaningful measure, when a community may keep going without its members "
  "flourishing?", 'the paper\'s question asked directly; the same question'),
 ("(1970) is the classic essay arguing that a hidden hierarchy can be harder to challenge than explicit authority.",
  "(1970) is the classic essay on hidden hierarchy. Can it be harder to challenge than explicit authority? She argues it can.",
  'the published "the classic argument that hidden hierarchy can be harder to challenge than explicit authority" as a '
  'question and her answer'),
 ("Then there's the Zapatistas' own archive, [Enlace Zapatista]",
  "Want it straight from the Zapatistas? Their own archive is [Enlace Zapatista]",
  'a question that claims nothing; the published "The Zapatistas\' own Enlace Zapatista archive"'),
 ("), especially their 2023 explanations of the new autonomy.",
  "), and look especially for their 2023 explanations of the new autonomy.",
  'the published "especially" as what to look for there'),
]
log = []
for old, new, why in FIX:
    assert t.count(old) == 1, old[:60]
    t = t.replace(old, new)
    log.append({'old': old, 'new': new, 'why': why})
(HERE / 'v3.md').write_text(t, encoding='utf-8')
(HERE / 'v3-breaks.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v3.md,', len(log), 'changes')
