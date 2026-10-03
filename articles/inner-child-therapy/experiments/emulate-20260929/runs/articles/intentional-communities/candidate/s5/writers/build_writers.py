"""Writer prompts for the section 5 paragraphs that still read AI (2026-10-03, after API batches 1-3). Emulate's key
returned HTTP 403 at 04:30, so the gate's own route for new wording is used: fresh writers, three variants each, then
the linter, Pangram (API), and the trace and stance check on the picks."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
B = json.load(open(HERE.parent / 'final-v11.json', encoding='utf-8'))['blocks']
O = json.load(open(HERE.parent / 'original-blocks.json', encoding='utf-8'))
S4 = json.load(open(HERE.parent.parent / 's4' / 'final-v9.json', encoding='utf-8'))['blocks']
P = lambda k: mdplain.plain(B[k]).strip()
PO = lambda k: mdplain.plain(O[k]).strip()
bans = open('/home/claude/s3rules/tools/humanization/reviewer/owner_bans.txt', encoding='utf-8').read().strip()
voice = '\n\n'.join(mdplain.plain(S4[k]).strip() for k in ('P5', 'P7', 'P28', 'P29'))
HEAD = """You're rewriting part of one section of a long essay by Joel about intentional communities (communes), published on his Substack. The section is "The Medicine Part, Without Pretending It Isn't There": why psychedelic medicine belongs in his community model, its risks, his ceremony principles, and the "calling" people feel after big experiences. The essay is first person, plain, a bit blunt and sometimes goofy; it argues for things. Joel coined "pl/ork" (play + work) earlier in the essay; keep it where it appears.

The paragraph(s) you rewrite read as AI-generated on Pangram, an AI-text detector, in the version shown below. Your job is a version that says the same things at the same strength and reads like a person wrote it. Meaning comes first: every point listed under "What it has to say" must be there, no stronger or weaker, and nothing new about Joel, his life or the world may be added.

"""
LESSONS = """What the detector has shown on this section (not a checklist, and nothing here needs to be shown off):
- Versions that failed kept the published sentence shapes: a topic sentence, then a list, then a verdict; a list of three or more strung through one sentence; parallel runs ("may be X, or may be Y", "who..., who..., who..."); balanced lines ("Being X is different from Y"); a closing maxim ("Omnipotence is a terrible founding document"; "insight does not wash dishes"); a closing "The question is whether...".
- Versions that passed sounded spoken and a little loose: a question put to the reader ("do you trust them?"), a fragment or two, an "And" or "Yeah" at the start of a sentence, a number in digits, a parenthetical aside, Joel's own plain bluntness. Don't pile these on; one real one beats three decorative ones.
- Joel's own paragraphs from the section before, which read as human (his register to aim at):

""" + voice + """

The author's bans and tells:
""" + bans + """

"""
def task(name, keys, says, notes=''):
    before_k, after_k = TASKS_CTX[name]
    before = '\n\n'.join(P(k) if not k.startswith('H') else re.sub(r'^#+\s*', '', B[k]) for k in before_k)
    after = '\n\n'.join(P(k) if not k.startswith('H') else re.sub(r'^#+\s*', '', B[k]) for k in after_k)
    current = '\n\n'.join(P(k) for k in keys)
    published = '\n\n'.join(PO(k) for k in keys)
    n = len(keys)
    out = (HEAD + "What it has to say (in this order unless a different order reads more naturally inside the paragraph; keep the paragraph breaks"
           + (" between the %d paragraphs" % n if n > 1 else "") + "):\n" + says + "\n\n" + (notes + "\n\n" if notes else '')
           + "The published version (AI-assisted; its meaning is the reference, its wording isn't):\n" + published + "\n\n"
           + "The latest rewrite, which read as AI (don't reuse its shapes):\n" + current + "\n\n"
           + "The text just before (final; don't change it):\n" + before + "\n\n"
           + "The text just after (final; don't change it):\n" + after + "\n\n" + LESSONS
           + "Write three variants, A, B and C, each different in how it's built (not just reworded). Each variant is the whole rewrite"
           + (" (all %d paragraphs, blank line between them)" % n if n > 1 else "") + ", plain text, no headings, no emojis unless the published version has one there. "
           + "Where a link must sit, wrap the words that carry it in double square brackets, [[like this]]. Keep roughly the published length (within about 20%).\n\n"
           + "Output exactly:\nVARIANT A\n<text>\n\nVARIANT B\n<text>\n\nVARIANT C\n<text>\n\n"
           + "Don't use any tools except reading this one file: don't open, list or search anything else, don't run commands, and don't use the web.\n")
    (HERE / (name + '.txt')).write_text(out, encoding='utf-8')
    print(name, len(out.split()), 'words')
TASKS_CTX = {'W1': (['H1'], ['P2']), 'W2': (['P6'], ['H2a', 'P9']), 'W3': (['P11'], ['P15']), 'W4': (['P16'], ['H2b', 'P18']),
             'W5': (['P17', 'H2b'], ['P19']), 'W6': (['P19'], ['P21']), 'W7': (['P20'], ['P28']), 'W8': (['P30'], ['P32'])}
task('W1', ['P1'], """- Psychedelics have moved from taboo toward regulated use, much faster than most writing about communities has caught up with (acknowledged).
- Oregon's licensed psilocybin service centers began opening in 2023. Link on the words for Oregon's licensed psilocybin service centers.
- Colorado created a regulated natural-medicine system and began licensing in 2025.
- New Mexico enacted a Medical Psilocybin Act in 2025. Link on "Medical Psilocybin Act".
- In Australia, authorized psychiatrists have had limited access to psilocybin and MDMA for specified conditions since 2023. Link on the words for the psychiatrists' access.
Every fact stays exact: the places, the years, "licensed", "regulated", "enacted", "authorized", "limited", "specified conditions". Add no fact, number or name.""")
task('W2', ['P7', 'P8'], """Paragraph 1:
- These medicines also attract people who love revelation and hate the follow-through.
- Someone can collect lots of ceremonies and origin stories (the published also has "a new sacred name"; optional) and still be unable to apologize to a housemate.
- A community organized mainly around the peak experience will find out sooner or later that insight doesn't do the practical work of living together: it doesn't wash the dishes or calm a frightened child.
Paragraph 2:
- In Joel's own experience, the case for using these medicines communally is also real ("in my experience" stays first person).
- Psychedelics can loosen the defenses that otherwise dominate every serious conversation.
- They can create powerful bonds when people sit through difficult nights together.
- They can also produce confusion, grandiosity, dependency, and a mess between people (all four stay; don't string them through one sentence).
- The open question at the end: whether the community around them is mature enough to tell those apart. It stays a question; don't answer it.""",
     "Notes: the published paragraph 1 says insight does not \"revise agreements\" either; leave that out (Joel has seen people come back from visions with practical ideas).")
task('W3', ['P12', 'P13', 'P14'], """Paragraph 1:
- In a community, your sober sitter may be someone who has known you for years.
- Being watched and being held feel different.
- That matters especially with long, medically risky experiences such as iboga, where screening beforehand and continuous observation are essential.
Paragraph 2:
- Peers can also reality-check the "downloads" (what people bring back from a trip).
- Psychedelics produce genuine insight and convincing nonsense, and the two look alike (the published quip: "with identical lighting"; optional).
- Friends who know your history may notice which parts look like a new understanding and which look like your mother (keep "may": they notice, they don't rule).
Paragraph 3:
- Community creates rhythm.
- Many traditional medicine systems put ceremonies on communal timing rather than individual appetite.
- A shared calendar can reduce compulsive repetition and give integration time to happen.
The community doesn't permit or forbid anyone's use; authority over a person's practice stays with them.""")
task('W4', ['P17'], """- Joel won't idealize psychedelics (first person).
- Some people should avoid them, and some communities shouldn't use them.
- Enthusiasm will create casualties wherever competence lags behind access.
- A community that chooses this path needs the humility to say no, to pause, to refer someone out to outside or expert help, and to admit it when an experience caused harm. All four stay; don't string them through one sentence.""",
     "Notes: with the paragraph before it, the latest rewrite read as human; alone it read AI. It has to read human alone.")
task('W5', ['P18'], """- The principle: no special shamans.
- Traditional lineages usually disagree with Joel here.
- Many ayahuasca and Bwiti communities believe medicine should stay under trained lineage authority.
- Joel respects what those traditions have preserved, and he has learned from them (first person, his).""",
     "Notes: this is the first of Joel's ceremony principles, right under the heading \"My Ceremony Principles\". The next paragraph (final) explains his objection, so this one doesn't need to.")
task('W6', ['P20'], """- Joel doesn't yet know how a peer-led medicine culture keeps an informal shaman from emerging anyway: the person everybody trusts and gradually stops questioning, even though nobody gave them the title (the published also has "consults"; one of those can go).
- Rotating roles and public accountability may help.
- He doesn't think either of them solves it completely.""")
task('W7', ['P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27'], """Seven short paragraphs, the rest of Joel's ceremony principles. Keep each paragraph's content in its own paragraph.
1. Joel wants people to learn to guide themselves and to care for each other, while respecting the limits of their competence ("I want" is fine here: it's the community he wants). He has written more about [[peer-held ceremonies]] and about [[the best psychopath shaman I ever met]] (two links; keep "psychopath").
2. Peer-led never means casual. Screening for medical and psychiatric contraindications; reviewing medications and combinations; an appropriate sober sitter; and deciding, before anybody takes anything, what calls for professional or emergency care. Distributed authority raises the bar of competence; it doesn't lower it. (All of these stay; don't string three or more through one sentence.)
3. Joel is especially cautious about medicines and protocols he considers more destabilizing or medically burdensome, including some uses of [[ketamine and MDMA]] and [[bufo]] (two links; "some uses of" and "I consider" stay). The reasons are in the linked articles rather than smuggled into one sentence here.
4. The medicine stays behind the other pl/ork. Reparenting, somatic capacity, and peer counseling come first. Medicine can deepen a practice that already exists; it can't create months of honest relationship (the published quip: "by pharmacological decree"; optional).
5. This prerequisite also filters out experience collectors. Someone unwilling to spend six months learning to listen without fixing is unlikely to become more relationally mature because the visions were especially geometric (keep "unlikely"; the joke is optional).
6. Integration is ordinary life. Ceremony opens something; the weeks after show whether anything changed: in relationships, daily behavior, sleep, decisions, and the ability to tolerate frustration without declaring a new spiritual emergency (carry as much of that list as reads naturally, never three or more in one sentence).
7. Supports matter: preparation, nutrition, interaction screening, dose discipline and emergency planning matter more than aesthetic ceremony details (never three or more in one sentence). Joel keeps his current safety material in [[Altered States Triage]] (a link).""")
task('W8', ['P31'], """- The call may be real (a concession: the urge people feel after a big experience).
- But omnipotence, the feeling that your love can heal anyone, is a terrible thing to found a community on (the published: "Omnipotence is a terrible founding document"). The point is about what a community is founded on, not when.""",
     "Notes: three versions of this as a one-line maxim read AI next to the paragraph after it, which reads human alone. Try something other than a maxim; it can be one or two sentences.")
