"""The appendix, draft v2 (2026-10-17): v1 (../make_v1.py) with every entry rebuilt from Emulate round a (emu-a/out/, calls A
and B) and the published meaning put back inside Emulate's sentences. Emulate's shapes: the title first, then "by" and the
author, then what the work is, in a plain spoken sentence ("is about", "follows", "compares"), without the published
"Author, Title — descriptor" form. Kept from the published: every heading, title, author, year, link and emphasis, and every
claim of each entry (the "why" of each entry says what came back). Emulate's B call ran several entries together into
paragraphs and dropped the headings; the appendix stays a list, one entry per paragraph.
Two entries put the author first ("Ludwig and Gimnig's", "Jo Freeman's"): four of
the entries opened with a title that starts with "The", and the linter's B13 counts repeated paragraph openers.
Writes v2.md and v2-entries.json. Run from this folder: python3 make_v2.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v1.md').read_text(encoding='utf-8')
LINK = re.compile(r'\]\(([^)\s]+)\)')
# (start of the v1 entry, the v2 entry with {1}, {2} for the entry's links in order, why)
NEW = [
 ('[***Where’s Utopia?***]', "[***Where’s Utopia?***]({1}) (1988) is a documentary by my father, made with Jerry Mintz.",
  'B: "is a documentary by my dad, with Jerry Mintz"; "my father", as the article says it everywhere else'),
 ('[***A Place Called Chiapas***]', "[***A Place Called Chiapas***]({1}) (1998) is about the early days of the Zapatistas.",
  'B word for word; "the early days" for "their early years"'),
 ('[***American Commune***]', "[***American Commune***]({1}) (2013) is about The Farm, seen through the eyes of two sisters "
  "who grew up there. For this article, the view of the grown children is essential.",
  'B\'s "is about The Farm"; the published "through the eyes of" (B\'s "narrated by" said more) and "essential" (B: "important")'),
 ('[***Commune***]', "[***Commune***]({1}) (2005) is about Black Bear Ranch, and what radical freedom did to the relationships "
  "there.", 'B\'s "is about Black Bear Ranch, and the relationship implications of radical freedom", said plainly'),
 ('[***A New We***]', "[***A New We***]({1}) takes you on a tour of a bunch of ecovillages in Europe, and shows how many "
  "different arrangements hide under that one label.",
  'B\'s "takes us on a tour of a bunch of different ecovillages in Europe"; the published "how many different arrangements '
  'hide under one label" back (both calls dropped it)'),
 ('[***Within Reach***]', "[***Within Reach***]({1}) follows a couple as they bike 6,500 miles, visiting a hundred or so "
  "communities.", 'B word for word, with the published "6,500"'),
 ('[***Seeking the Good Life in America***]', "[***Seeking the Good Life in America***]({1}) compares Twin Oaks, Acorn and "
  "Light Morning.", 'B word for word (A\'s "three nearby communities" added a claim)'),
 ('[***Voices of Cohousing***]', "[***Voices of Cohousing***]({1}) shows the partial-community option, where you get high "
  "neighborliness and more private autonomy.",
  'B\'s "the partial-community option, with high neighborliness and more private autonomy", without its "a good introduction" '
  '(an added verdict)'),
 ('[***Inside the Bruderhof***]', "[***Inside the Bruderhof***]({1}) is about a high-commitment religious community, including "
  "the autonomy it requires members to give up. The Bruderhof also has a pretty extensive [YouTube channel]({2}).",
  'A\'s "is a film about a high-commitment religious community" and "pretty extensive YouTube channel"; the published "the '
  'autonomy it requires members to surrender" (A: "the tradeoffs they make") and "The Bruderhof" named (A, B: "they")'),
 ('[***Living in the Future: Lammas***]', "[***Living in the Future: Lammas***]({1}) is about what happens when "
  "community-building meets land use and planning law.",
  'the published "community-building meets land use and planning law" inside the "is about" of both calls (A\'s "messiness" '
  'and B\'s "a good picture" added verdicts)'),
 ('[Jean Liedloff, *The Continuum Concept***]', "[***The Continuum Concept***]({1}) by Jean Liedloff (1975) is a foundational "
  "natural-child-rearing book, based on her time with the Ye’kuana. It's provocative observation, so take it with a grain of "
  "salt as anthropology.",
  'A\'s title first and "take it with a grain of salt from an anthropological perspective"; the published "a foundational" '
  '(A, B: "the classic", "the foundational") and "provocative observation"; A\'s "an important book to read" added a verdict'),
 ('[Michaeleen Doucleff, *Hunt, Gather, Parent***]', "[***Hunt, Gather, Parent***]({1}) by Michaeleen Doucleff (2021) is a "
  "practical, accessible book about kids taking part in family life, in a way that gives them autonomy and spreads out the "
  "work of caring for them.",
  'A\'s "in a way that allows them autonomy and that distributes the work of caring for children"; the published "practical, '
  'accessible" (A: "a really good book", B: "more practical") and "participating" (kids taking part)'),
 ('Diana Leafe Christian, [***Creating a Life Together***]', "[***Creating a Life Together***]({1}) by Diana Leafe Christian is "
  "the place to start, for the nuts and bolts of membership, money, land and agreements.",
  'B\'s "starting with" and "nuts and bolts stuff about membership, money, land, agreements"; "start here" kept as "the place '
  'to start", without B\'s "etc."'),
 ('Yana Ludwig, [***Building Belonging***]', "And for a whole-systems guide to intentional community, there's "
  "[***Building Belonging***]({1}) by Yana Ludwig.", 'B\'s "For a guide to doing it all in a whole-systems way, check out"; '
  'the published "a whole-systems guide to intentional community"'),
 ('Rau and Koch-Gonzalez, [***Many Voices One Song***]', "[***Many Voices One Song***]({1}) by Rau and Koch-Gonzalez is a "
  "practical manual for doing sociocracy.", 'A\'s "a practical manual for how to use sociocracy"'),
 ('Schaub and colleagues, [***Building United Judgment***]', "[***Building United Judgment***]({1}) by Schaub and colleagues "
  "is about consensus decision-making.", 'B\'s "is about consensus", with the published "consensus decision-making"'),
 ('Ludwig and Gimnig, [***The Cooperative Culture Handbook***]', "Ludwig and Gimnig's [***The Cooperative Culture Handbook***]({1}) "
  "has a bunch of exercises for being more cooperative, dealing with conflict and building group culture.",
  'B\'s "has a bunch of useful exercises on how to be more cooperative, deal with conflict, build group culture", without '
  '"useful" (an added verdict) and "etc."'),
 ('Dmitry Orlov, [***Communities That Abide***]', "[***Communities That Abide***]({1}) by Dmitry Orlov makes an uncomfortable "
  "argument that long-lasting communities often rely on communal property, separation, boundaries and a binding ideology. "
  "From a distance, cohesion and capture can look a lot alike.",
  'B\'s "makes a fairly uncomfortable argument that communities ...", with the published "often rely on" (B: "survive longer '
  'if", A: "most ... had") and the published last sentence in plain words (A gave it to Orlov, B made it "have a lot in '
  'common")'),
 ('Rubin, Willis, and Ludwig, [“Measuring Success', "[“Measuring Success in Intentional Communities”]({1}) by Rubin, Willis "
  "and Ludwig is a paper that asks whether longevity alone is a meaningful measure, when a community may keep going without "
  "its members flourishing.",
  'A\'s "is a paper that asks whether longevity is an appropriate measure ... when communities may last without their members '
  'flourishing", with the published "alone" and "meaningful measure" back (B made the question a claim)'),
 ('Rosabeth Moss Kanter, [***Commitment and Community***]', "[***Commitment and Community***]({1}) by Rosabeth Moss Kanter is "
  "a classic. It compares a bunch of nineteenth-century communes, and the practices that built commitment in them.",
  'B\'s "is a classic that compared a bunch of 19th century communes", with the published "the practices that built '
  'commitment" (B: "some key ingredients")'),
 ('Benjamin Zablocki, [***Alienation and Charisma***]', "[***Alienation and Charisma***]({1}) by Benjamin Zablocki is field "
  "research on communes, and on the role charisma plays in them.",
  'A\'s "a book based on his field research of communes", with the published "the role of charisma" (A: "their use of '
  'charisma", B: "underscores the importance of charisma")'),
 ('Jo Freeman, [“The Tyranny of Structurelessness”]', "Jo Freeman's [“The Tyranny of Structurelessness”]({1}) (1970) is the "
  "classic essay arguing that a hidden hierarchy can be harder to challenge than explicit authority.",
  'A\'s "is a classic essay on why ...", with the published "can be harder to challenge than explicit authority" (A, B: '
  '"worse than an explicit one")'),
 ('Gloria Muñoz Ramírez and Subcomandante Marcos, [***The Fire and the Word***]', "[***The Fire and the Word***]({1}) by Gloria "
  "Muñoz Ramírez and Subcomandante Marcos is about how the Zapatista movement came about, its practice-before-theory "
  "approach, how it built autonomous institutions, and the original Good Government Boards.",
  'B\'s "on how the Zapatista movement came about, their practice-before-theory approach, how they built autonomous '
  'institutions, and the original Good Government Boards", without "a really helpful primer" (an added verdict)'),
 ('The Zapatistas’ own [Enlace Zapatista]', "Then there's the Zapatistas' own archive, [Enlace Zapatista]({1}), especially "
  "their 2023 explanations of the new autonomy.",
  'B\'s "The Zapatistas have an excellent archive, Enlace Zapatista", without "excellent", and the published "especially" '
  '(A, B: "including")'),
 ('I did a much larger source audit', "If you're curious, I did a much bigger source audit than would comfortably fit in this "
  "article. The [public research report]({1}) shows the evidence base, the limits, the counterexamples and what I still "
  "couldn't verify. That way you can check the research yourself, and this article doesn't have to turn into a 200-row "
  "ledger!",
  'B\'s "If you\'re curious ..., I did a lot more research than made it into this article", with the published audit, the four '
  'things the report shows and the ledger back (A and B kept only "see my research report")'),
]
blocks = re.split(r'(\n\s*\n)', t)
log, used = [], set()
for start, new, why in NEW:
    idx = [i for i, b in enumerate(blocks) if b.startswith(start)]
    assert len(idx) == 1, (start, idx)
    old = blocks[idx[0]]
    urls = LINK.findall(old)
    text = new
    for n, u in enumerate(urls, start=1):
        assert '{%d}' % n in text, (start, n)
        text = text.replace('{%d}' % n, u)
    assert '{' not in text, start
    text += old[len(old.rstrip()):]  # the entry's trailing newline, if any
    blocks[idx[0]] = text
    used.add(idx[0])
    log.append({'start': start, 'old': old, 'new': text, 'why': why})
paras = [i for i, b in enumerate(blocks) if b.strip() and not b.strip().startswith('#') and not re.fullmatch(r'\n\s*\n', b)]
assert set(paras) == used, sorted(set(paras) - used)
(HERE / 'v2.md').write_text(''.join(blocks), encoding='utf-8')
(HERE / 'v2-entries.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v2.md,', len(log), 'entries')
