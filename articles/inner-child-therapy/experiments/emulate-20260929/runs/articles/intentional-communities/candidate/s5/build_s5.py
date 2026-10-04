"""Section 5 builds (2026-10-03). v1: for every paragraph an Emulate version (emu/outputs.json), with small logged
fixes for meaning: the facts and links as published, Joel's first person only where the published text has it, the
hedges and quantifiers the stance ledger marks (STANCE-LEDGER-s5.md), and the specific pairings put back where
Emulate blurred them. P10's two middle sentences, Human in the baseline, stay as published.
Writes final-vN.json (blocks), section-vN.md (Markdown), fixlog-s5.json and rN/*.txt (plain text for Pangram)."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
O = json.load(open(HERE / 'original-blocks.json', encoding='utf-8'))
E = json.load(open(HERE / 'emu' / 'outputs.json', encoding='utf-8'))
LINKS = {}
for k, t in O.items():
    for a, u in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', t):
        LINKS[a] = u
L = lambda anchor: LINKS[anchor]
ORDER = list(O)
V = {}
V[1] = dict(O)
V[1].update({
 'P1': "Psychedelics have been moving from taboo toward regulated use, and a lot of those changes haven’t made it into most of the literature on communities yet. In the US, [Oregon’s licensed psilocybin service centers](%s) started opening in 2023. Colorado has created a regulated natural medicine system and started licensing in 2025. New Mexico passed a [Medical Psilocybin Act](%s) in 2025. In Australia, [authorized psychiatrists have been able to use psilocybin and MDMA](%s) (for a limited set of conditions) since 2023." % (L('Oregon’s licensed psilocybin service centers'), L('Medical Psilocybin Act'), L('authorized psychiatrists have had limited access to psilocybin and MDMA')),
 'P2': "It's not all roses, either, and none of it is inevitable. In 2024, the FDA issued a [Complete Response Letter](%s) for the submitted MDMA-assisted therapy application, declining to approve it and asking for more evidence. Portugal often gets described, lazily, as a place where \"they've legalized everything\" -- which is false! They've [decriminalized small amounts of all drugs for personal possession and use](%s), but trafficking is still criminal." % (L('Complete Response Letter'), L('decriminalized possession of small amounts for personal use')),
 'P3': E['e2-emuA'].split('\n\n')[0],
 'P4': "Most communities that are using psychedelics don't advertise that fact, because even where the law allows some use there may be issues with parents worried about their kids, or neighbors imagining chaos, or insurance disappearing, or local authorities who may not understand any of the distinctions.",
 'P5': "I'm talking about it here because not to talk about it would be to falsify my model. Many of the people who read this article are already familiar with my [writing about psychedelics](%s), including my [loveyhuasca/Haoma material](%s). If this article is going to be honest, it has to talk about both the value and the risk." % (L('psychedelic writing'), L('loveyhuasca/Haoma material')),
 'P6': "Consider the case against building medicine into a community first, because it's serious: the [Global Ayahuasca Survey](%s) found that physical and mental adverse effects are common with ayahuasca use. Severe adverse effects are far less common, and context matters. And these medicines can open things up faster than people (or communities) are able to support them." % L('Global Ayahuasca Survey'),
 'P7': "On top of that, these medicines attract people who want to experience revelation more than they want to do the work that follows. While this isn’t true of everyone, there are certainly plenty of people who will happily go to a dozen ceremonies and learn six different origin stories, while never dealing with simple issues like apologizing to a housemate. If a community is set up mainly around the peak experience, it will find out eventually that insight doesn’t wash the dishes, revise the agreements, or calm a frightened child.",
 'P8': "On the other hand, from my own experience, the communal aspect of using these medicines has real value. Psychedelics can be used to let go of the defenses that dominate every serious conversation, and can create powerful bonds between people who sit through difficult nights together. They can also be confusing, lead to grandiosity, create dependency, and lead to messy interactions with other people. The question is whether the community that’s supporting their use is mature enough to tell those apart.",
 'P9': "A lot of it is about integration. When you gain insight and clarity about your life, you wake up and you’re still in the same environment you were in before it happened, with all the old cues still waiting, and no one knows what happened to you. This is where it can be super helpful to have gone through the experience in a community, where the people who were there for you can also notice what happens to you in the months after.",
 'P10': "The deeper you go, the more alienated you can feel. " + O['P10'].split('. ', 1)[1].rsplit(' That helped produce', 1)[0] + " That isolation helped give me a God complex, a Savior complex, or both, and then I attracted exactly the right people to show me my limits. 😂",
 'P11': "And the people you’re relying on to support you, do you trust them? The alternative is often to pay people you don’t know to support you for a night. They may be great, but there’s also the possibility that the person stroking a feather over you has only known you for 4 hours and already has a cosmology they’re using to explain everything you say.",
 'P12': "If you’re working within a community, your sober sitter may be someone who has known you for a long time. There’s a difference between being held and simply being watched—this is especially relevant when you’re working with medicines like iboga that require screening and watching for the duration of a long and medically risky experience.",
 'P13': "Your peers can also help you reality-check your downloads. Psychedelics can be an incredible source of insight, but they can also be an incredible source of nonsense. It can be hard to tell the difference between the two since the lighting is the same. It helps to have friends who know you and your history well enough to offer a perspective on which parts of what you’re bringing back are insight and which are simply more of the same stuff you got from your mother.",
 'P14': "Community also helps provide a rhythm for medicine work. Many medicine traditions use community timing for their ceremonies, rather than allowing people to take medicine when they want. This can be helpful for avoiding compulsive medicine-taking and for allowing integration time to happen.",
 'P15': "It will be easier to deal with logistics when there’s more of you. Having somebody that the collective trusts to watch the kids. Not having to drive away from the ceremony. Having people that can bring water, be close by and sit quietly with somebody as they come back to normal consciousness.",
 'P16': "There will be people to play with! Raves often let people skip to that part of intimacy where they feel close enough to do wild things together before they know enough about each other to truly trust each other. Imagine doing ecstatic music and dance with people in a community that you do know… 💃🕺",
 'P17': "Yeah, I won’t idealize psychedelics. They’re not for everybody. There will be people that shouldn’t do them. There will be communities that shouldn’t be doing them. And with a lot of people hella stoked on psychedelics, there will be casualties wherever people get access before they’re competent to work with these powerful substances. If a community is going to dive into this it needs to do so in a humble way. Knowing that sometimes the answer will be no, or not now, or go work with so-and-so, or we messed that one up and someone got hurt.",
 'P18': "No special shamans. In this, I know I disagree with many of the traditional lineages (particularly in ayahuasca and Bwiti), which believe medicine should stay under trained lineage authority. I respect what those traditions have preserved, and I’ve learned from them.",
 'P19': "My issue is with placing one charismatic person above everyone else’s direct experience. The facilitator on the retreat circuit may be wise. They may also be someone who hasn’t been vetted by anybody, who may or may not be a sexual predator, who is financially dependent on people coming back to them specifically, who has little to be accountable to, or who is simply wrong. When one is opening so deeply, not knowing which you’re getting is a major concern.",
 'P20': "One of the things I’m not sure how to navigate yet, though, in this peer-led way of working with medicine is how to avoid someone becoming a de facto shaman anyway: the person everybody consults, trusts, and gradually stops questioning, even though nobody gave them the title. I suspect rotating roles and public accountability can help, but that neither one is enough.",
 'P21': "I do, however, advocate for people to learn how to guide themselves, take care of each other, and know when something is beyond their competence. I talk a bit more about this in the piece on [peer-held ceremonies](%s) and in the one on [the best psychopath shaman I’ve ever met](%s)." % (L('peer-held ceremonies'), L('the best psychopath shaman I ever met')),
 'P22': "There’s a difference, though, between peer led and doing it casually. There needs to be screening for medical and psychiatric contraindications, a review of medications and medication combinations, an appropriate sober sitter present, and a clear idea, before anybody takes anything, of when to bring in professional help or go to the ER. When authority is distributed, the bar of required competence actually goes up.",
 'P23': "In addition, I am especially cautious about medicines and protocols which I consider to be more destabilizing or medically burdensome, including some uses of [ketamine and MDMA](%s) and [bufo](%s). See the linked articles for more explanation." % (L('ketamine and MDMA'), L('bufo')),
 'P24': "Medicine will come after the other pl/ork. If a person hasn’t done the reparenting, somatic capacity, peer counseling, etc. before the ceremony, the medicine can’t do that work for them. It can deepen a practice that’s already there, but it can’t create months of honest relationship.",
 'P25': "Also, this helps weed out the ‘experience collectors’. If someone is unwilling to spend six months learning to listen without fixing, why would they suddenly become more relationally mature because the visions were especially geometric?",
 'P26': "Integration is a part of day to day life. Ceremony opens something up, but the weeks that follow are where you see whether anything changed for the person. How are their relationships? How are they living their life now? Sleep? Decisions? Can they tolerate frustration without declaring a new spiritual emergency?",
 'P27': "Practical safety and support matter more than how the ceremony looks: preparing for it, nutrition, screening for interactions, dose discipline, and what to do in case of emergency, etc. A lot of this is covered in [Altered States Triage](%s), where I keep my current safety material." % L('Altered States Triage'),
 'P28': "Legal issues differ greatly, and are sometimes not well defined, but some basic understanding of what is or is not allowed in a given community, what needs to be private, what might be insurable or require legal review, etc. should be put in writing. “I don’t think anybody here has ever heard of that” is information, but it’s not the same as a legal opinion.",
 'P29': "One of the most common impulses that people feel following a deep psychedelic or mystical experience is the urge to find one’s tribe, to form a village, to help others access the experience.",
 'P30': "I know this call. I also know that it can come with an inflated sense of self. You come back from this experience and you believe you can fix everyone with your love and soon find that there are people who don’t want to be fixed and those who sincerely want to but yet live lives contrary to that change and those that need more help than you imagined.",
 'P31': "Even if the call is real, building a village on a foundation of omnipotence is a bad idea.",
 'P32': "A group that begins in a kind of collective spiritual euphoria can start recruiting immediately and promise too much, not realizing how quickly things can get out of hand arithmetically until several people already depend on it. The sections on capacity and on membership, later on in this article, are partly there to protect the original generosity from that first rush.",
 'P33': "Once the initial flush of euphoria has passed, the call may still prove useful. A community can be a training ground where people learn the practices, care for one another, and sometimes move on to start a new experiment. This answers the reasonable objection that forming a commune is just a privileged way of escaping from society.",
})
assert V[1]['P10'].count('26') == 1 and 'Buddhist monasteries despite all the preaching' in V[1]['P10']
SRC1 = {'P1': 'e1-emuA', 'P2': 'e1-emuA', 'P3': 'e2-emuA', 'P4': 'e2-emuB', 'P5': 'e2-emuB', 'P6': 'e3-emuA',
        'P7': 'e3-emuA', 'P8': 'e3-emuA', 'P9': 'e4-emuA', 'P10': 'published, first sentence from e4-emuB, last sentence new',
        'P11': 'e4-emuA', 'P12': 'e5-emuA', 'P13': 'e5-emuA', 'P14': 'e5-emuA', 'P15': 'e6-emuA', 'P16': 'e6-emuA',
        'P17': 'e6-emuA', 'P18': 'e7-emuA, rebuilt', 'P19': 'e7-emuA, rebuilt', 'P20': 'e7-emuB', 'P21': 'e8-emuB',
        'P22': 'e8-emuB', 'P23': 'e8-emuA', 'P24': 'e9-emuA and e9-emuB', 'P25': 'e9-emuA', 'P26': 'e9-emuA',
        'P27': 'e10-emuA, rebuilt', 'P28': 'e10-emuA', 'P29': 'e11-emuB', 'P30': 'e11-emuA', 'P31': 'e11-emuB',
        'P32': 'e12-emuA, rebuilt', 'P33': 'e12-emuB'}
# why each fix, for fixlog-s5.json and the side-by-side page (what Emulate had, and what the published text says)
WHY1 = {
 'P1': ['Emulate A, with the facts put back: it had Oregon "set to start opening licensed psilocybin service centers in 2023", Colorado "set to begin licensing in 2025", New Mexico\'s Act "set to take effect in 2025" (the published says the centers began opening in 2023, licensing began in 2025, and the Act was enacted in 2025), and psychiatrists without "authorized".',
        'Its first sentence ("There has been a lot of changes in the legality and regulations of psychedelics") lost "from taboo toward regulated use"; that came back. "Enacted" became "passed".'],
 'P2': ['Emulate A. "It\'s not all roses" lost "nor inevitable", so "none of it is inevitable" went back in; "asking for more evidence in order to be considered for approval" became "declining to approve it and asking for more evidence", and the application is "MDMA-assisted therapy" again.',
        '"Lazily" back, beside Emulate\'s "which is false!". Emulate added "of all drugs" (true of Portugal\'s 2001 law; the linked policy profile says so).'],
 'P3': ['Emulate A as it came. The published quip "not a friend who once read a thread" is gone; "actual legal advice" carries its point, and P28 makes it again ("is information, not a legal opinion").'],
 'P4': ['Emulate B. Both versions blurred the four reasons: A had "for fear of scaring off potential parents, neighbors, insurance, official types"; B had parents "of children that they want to welcome to the community", bare "other neighbors" and "insurance". Each is back with its own reason: parents worried about their kids, neighbors imagining chaos, insurance disappearing, officials who may not understand the distinctions.',
        '"Even where the law might be on their side" is "even where the law allows some use" again.'],
 'P5': ['Emulate B. "Likely already familiar" lost its "likely"; the two links are apart again (the psychedelic writing, and the loveyhuasca/Haoma material; B had put all of it "on loveyhuasca or Haoma").',
        'B\'s last sentence opened with "I want to be able to write an honest article", the "I want" opener Joel calls AI for his opinion; it says what the published says without it.'],
 'P6': ['Emulate A. Out: its opener "It sounds like a lot to ask", "suggest" (the survey "found"), "context is everything" (published: "context mattered") and "The fundamental problem is that these medicines open" (published: they "can open"). "Serious" back, in Emulate\'s "consider the negative case first".'],
 'P7': ['Emulate A. "Seem to attract" is "attract" again, and "apologizing when they\'re wrong" is "apologizing to a housemate".',
        'Its last sentence ("this problem is only going to be exacerbated") replaced the published claim; the claim is back: a community set up mainly around the peak experience finds out that insight doesn\'t wash the dishes, revise the agreements, or calm a frightened child. "A new sacred name" is gone from the list.'],
 'P8': ['Emulate A. "Incredibly valuable" is "has real value" (published: "real"); "the patterns that dominate most conversations" is "the defenses that dominate every serious conversation"; the bonds come from sitting "through difficult nights together" again.',
        'Its last sentence ("Whether they do or not, in my experience, comes down to the maturity of the community") answered the published question and added a second "in my experience"; the question is back.'],
 'P9': ['Emulate A. Its opener "It\'s also about integration" had no "also" to point to under the new heading; "every old cue is waiting" is back; the people who were there "can also notice" what happens (A: "help you notice").'],
 'P10': ['The two middle sentences are the published ones (Human in the baseline). The first is Emulate B\'s. Both versions changed the rest: A had people "who had been there physically" and a generic "you may feel a God/Savior complex"; B had "my first couple of ego deaths", "IRL" and "I had both" (the published says "or both").',
         'The last sentence is new: the isolation "helped" (as published), the same three possibilities, and the 😂.'],
 'P11': ['Emulate A. "Finally," out (it isn\'t the last point); "often" back; "only knows your for 4 hours" fixed.'],
 'P12': ['Emulate A. "For one," out; "potentially medically risky" is "medically risky" again.'],
 'P13': ['Emulate A. "Second," out; friends sort "which parts" are insight and which are your mother (A: "whether what you\'re bringing back is insight or").'],
 'P14': ['Emulate A. "Third," out; "extremely helpful" is "helpful" (published: a shared calendar "can reduce").'],
 'P15': ['Emulate A. "More of ya" is "more of you"; "re-integrate back into normal consiousness" is "come back to normal consciousness" (integration means the weeks after, in this section).'],
 'P16': ['Emulate A. "Raves are great because they allow" is "Raves often let" (published: raves "often create sudden intimacy", with no verdict on raves); "ya" is "you".'],
 'P17': ['Emulate A. "I won\'t idealize psychedelics" back. Its casualties sentence ("Just like there are a lot of people that are hella stoked on psychedelics there will be casualties when people are not competent enough") lost the access half; now casualties come "wherever people get access before they\'re competent".',
         '"Or I fucked that one up" is "or we messed that one up and someone got hurt" (published: "admit when an experience caused harm"). "Hella stoked" is Emulate\'s.'],
 'P18': ['Rebuilt on Emulate A. Both versions dropped "I respect what those traditions have preserved and have learned from them" and the lineages\' reason (medicine under "trained lineage authority"); A also had "One of the things I want to make clear is that", "I don\'t advocate for shaman, per se" (no "special") and "the traditional lineages I have worked with", which the published doesn\'t say.'],
 'P19': ['Rebuilt on Emulate A. A turned the objection into a description of shamans ("often the shaman in these settings is a charismatic individual on the retreat circuit") and dropped "may be wise" and "simply wrong"; B was worse ("shitwomping").',
         'Now: the objection as published, the facilitator who "may be wise", and A\'s list under one "may"; "Deep openness magnifies the cost of that uncertainty" is "When one is opening so deeply, not knowing which you\'re getting is a major concern."'],
 'P20': ['Emulate B. "Yet" back; the informal shaman is described again ("the person everybody consults, trusts, and gradually stops questioning, even though nobody gave them the title"); "a deep commitment to holding one another accountable are good" is "public accountability can help"; "not enough" kept for "I don\'t think either solves it completely", as "neither one is enough".'],
 'P21': ['Emulate B. "Guide each other" is "guide themselves" (published: "self-guidance"); the links are on their words again. A had "I am teaching people", which the published doesn\'t say.'],
 'P22': ['Emulate B. A had "the ceremonies I lead". "Awareness of" and "knowledge of" are "screening for" and "a review of" again; "before anybody takes anything" back; "does not lower the bar of required competence" is "the bar of required competence actually goes up" (published: distributed authority "raises the competence requirement; it doesn\'t lower it").'],
 'P23': ['Emulate A. "Especially" back; "destabilizing and medically burdensome" is "or" again; the links on their words; "See the above articles" is "See the linked articles".'],
 'P24': ['Emulate A and B. A\'s "For now," made the rule provisional; out. B\'s "if a person doesn\'t do the reparenting … prior to the ceremony the medicine cannot do this work for them" carries "come first"; "deepen a practice" and "months of honest relationship" are back. "Etc." is Emulate\'s: image 7\'s pillars name more than three practices.'],
 'P25': ['Emulate A. "Invest the time in relationship building (6months is not that long)" is "spend six months learning to listen without fixing" again ("not that long" was Emulate\'s verdict); "especially geometric" back.'],
 'P26': ['Emulate A. "Lastly," out. "The weeks that follow are where the real work is done" is "where you see whether anything changed" (published: the weeks "reveal"); "Decisions?" and the frustration line back, for its "Etc.".'],
 'P27': ['Rebuilt on Emulate A, whose list was garbled ("screening for appropriate interaction") and had lost "more than aesthetic ceremony details"; B had screening for "the entity". "The Altered States Triage material I\'m currently using" is "where I keep my current safety material" again.'],
 'P28': ['Emulate A. "Often are not well defined" is "sometimes" again; "is valuable to have in writing" is "should be put in writing"; the quote "is information" again (A: only "not the same as a legal opinion"). B reversed the point.'],
 'P29': ['Emulate B, with "One of the great impulses" as "One of the most common impulses" (published: "Many people").'],
 'P30': ['Emulate A, with "know" for its "understand" twice (published: "I know that call. I also know the inflation") and "sincerely" back.'],
 'P31': ['Emulate B, with "The call is real" as "Even if the call is real" (published: "The call may be real").'],
 'P32': ['Rebuilt on Emulate A, which turned "can recruit" into a history ("many groups have begun … and immediately begun recruiting") and dropped "promise too much", the people already dependent, "partly" and the generosity the sections protect.'],
 'P33': ['Emulate B. "A training ground for people to move on from" lost what people learn there and made leaving the point; "learn the practices, care for one another, and sometimes" are back. "Partly answers" is "answers" again (published), "reasonable" and "just" (published: "merely") back.'],
}
assert set(WHY1) == {k for k in ORDER if k.startswith('P') and V[1][k] != O[k]}, set(WHY1) ^ {k for k in ORDER if k.startswith('P') and V[1][k] != O[k]}

# v2: what the v1 gate found (TRACE-v1-A to D, SENSE-v1, GROUNDING-v1, STANCE-v1), fixed before any Pangram call
V[2] = dict(V[1])
V[2].update({
 'P1': "Psychedelics have been moving from taboo toward regulated use much faster than most of the literature on communities has caught up with. In the US, [Oregon’s licensed psilocybin service centers](%s) started opening in 2023. Colorado has created a regulated natural medicine system and started licensing in 2025. New Mexico signed a [Medical Psilocybin Act](%s) into law in 2025. In Australia, [authorized psychiatrists have had limited access to psilocybin and MDMA](%s) (for specified conditions) since 2023." % (L('Oregon’s licensed psilocybin service centers'), L('Medical Psilocybin Act'), L('authorized psychiatrists have had limited access to psilocybin and MDMA')),
 'P2': "It hasn't been a smooth ride, either, and it isn't inevitable. In 2024, the US Food and Drug Administration issued a [Complete Response Letter](%s) for the submitted MDMA-assisted therapy application, declining to approve it and asking for more evidence. Portugal often gets described, lazily, as a place where \"they've legalized everything\" -- which is false! They've [decriminalized possessing small amounts for personal use](%s), but trafficking is still criminal." % (L('Complete Response Letter'), L('decriminalized possession of small amounts for personal use')),
 'P3': "To be sure, the legality of this varies depending on country, state, substance, religious status, what exactly one does, and so on, and if medicine is going to be part of a community at all, that community should definitely get actual local legal advice.",
 'P4': "Most intentional communities that are using psychedelics still don't say so publicly, because even where the law allows some use there may be issues with parents worried about the children, or neighbors imagining chaos, or insurance disappearing, or a local official who doesn't understand any of the distinctions.",
 'P6': "First, consider the case against building medicine into a community, because it's serious: the [Global Ayahuasca Survey](%s) found that physical and mental adverse effects were common with ayahuasca use, though severe ones were far less common, and context mattered. These medicines can open things up faster than a person (or a group) can support them." % L('Global Ayahuasca Survey'),
 'P7': "On top of that, these medicines attract people who want the revelation and hate the work that follows. Someone can collect a dozen ceremonies and six different origin stories, and still be unable to apologize to a housemate. If a community is set up mainly around the peak experience, it will find out eventually that insight doesn’t wash the dishes, revise the agreements, or calm a frightened child.",
 'P8': "On the other hand, from my own experience, the communal aspect of using these medicines has real value. Psychedelics can loosen the defenses that otherwise dominate every serious conversation, and can create powerful bonds between people who sit through difficult nights together. They can also produce confusion, grandiosity, dependency, and messy interactions with other people. The question is whether the community around them is mature enough to tell those apart.",
 'P9': "A lot of it is about integration, because an insight needs somewhere to land. When you gain insight and clarity about your life, you wake up and you’re still in the same environment you were in before it happened, with all the old cues still waiting, and no one knows what happened to you. This is where it can be super helpful to have gone through the experience in a community, where the people who held you through it can also notice what happens to you in the months after.",
 'P10': V[1]['P10'].replace("and then I attracted exactly the right people", "and then attracted exactly the right people"),
 'P11': "And the people you’re relying on to support you, do you trust them? The commercial alternative is often to pay people you don’t know to support you for a night. Sometimes they’re great, but sometimes the person stroking a feather over you has only known you for 4 hours and already has a cosmology they’re using to explain everything you say.",
 'P12': "If you’re working within a community, your sober sitter may be someone who has known you for years. There’s a difference between being held and being watched—this is especially relevant when you’re working with medicines like iboga, where you need screening first and someone watching over you for the whole of a long and medically risky experience.",
 'P13': "Your peers can also reality-check your downloads. Psychedelics produce real insight, but they also produce convincing nonsense, and it can be hard to tell the difference between the two since the lighting is the same. It helps to have friends who know you and your history well enough to see which parts of what you’re bringing back are insight and which parts look a lot like your mother.",
 'P14': "Community also gives medicine work a rhythm. Many medicine traditions use community timing for their ceremonies, rather than whenever each person feels like taking medicine. A shared calendar like that can be helpful for avoiding compulsive medicine-taking and for giving integration time to happen.",
 'P15': "Logistics get easier in a community. Having somebody that the collective trusts to watch the kids. Not having to drive away from the ceremony. Having people that can bring water, be close by, or sit quietly with somebody as they come back to normal consciousness.",
 'P16': "There will be people to play with! Raves often let people skip to that part of intimacy where they feel close before they know enough about each other to truly trust each other. Imagine doing ecstatic music and dance with people in a community that you do know, inconvenient habits and all… 💃🕺",
 'P17': "Yeah, I won’t idealize psychedelics. There will be people that shouldn’t do them. There will be communities that shouldn’t be doing them. And with a lot of people hella stoked on psychedelics, that enthusiasm will create casualties wherever people get access before they’re competent to work with these powerful substances. If a community is going to dive into this it needs to do so in a humble way. Knowing that sometimes the answer will be no, or not now, or go see someone outside who knows more, and admitting it when an experience caused harm.",
 'P18': "No special shamans. In this, I know I disagree with most traditional lineages. Many ayahuasca and Bwiti communities believe medicine should stay under trained lineage authority. I respect what those traditions have preserved, and I’ve learned from them.",
 'P19': "My issue is with placing one charismatic person above everyone else’s direct experience. The facilitator on the retreat circuit may be wise. They may also be someone who hasn’t been vetted by anybody, who isn’t accountable to anyone, who is a sexual predator, who is financially dependent on people coming back to them specifically, or who is simply wrong. And the more deeply someone is opening up, the more it costs not to know which one you’re getting.",
 'P20': "What I’m not sure how to navigate yet, though, in this peer-led way of working with medicine, is how to avoid someone becoming a de facto shaman anyway: the person everybody consults, trusts, and gradually stops questioning, even though nobody gave them the title. I suspect rotating roles and public accountability may help, but that neither one solves it completely.",
 'P21': "I do, however, want people to learn how to guide themselves and take care of each other, while respecting the limits of their competence. There’s more in my pieces on [peer-held ceremonies](%s) and on [the best psychopath shaman I’ve ever met](%s)." % (L('peer-held ceremonies'), L('the best psychopath shaman I ever met')),
 'P22': "But peer led never means casual. There needs to be screening for medical and psychiatric contraindications, a review of medications and combinations, an appropriate sober sitter present, and a clear idea, before anybody takes anything, of when to bring in professional or emergency care. When authority is distributed, the bar of required competence actually goes up.",
 'P23': V[1]['P23'].replace("See the linked articles for more explanation.", "The reasons are in the linked articles, rather than squeezed into one sentence here."),
 'P24': "Medicine comes after the other pl/ork. Reparenting, somatic capacity, peer counseling, etc. come first, and pharmacology can’t replace them. The medicine can deepen a practice that’s already there, but it can’t create months of honest relationship.",
 'P25': "Also, this prerequisite weeds out the ‘experience collectors’. If someone is unwilling to spend six months learning to listen without fixing, how likely are they to suddenly become more relationally mature because the visions were especially geometric?",
 'P26': "Integration is day to day life. Ceremony opens something up, and the weeks that follow show whether anything changed in the person. How are their relationships? How are they acting now? Sleep? Decisions? Can they tolerate frustration without declaring a new spiritual emergency?",
 'P27': "Supports matter, and the practical safety stuff matters more than how the ceremony looks: preparation, nutrition, screening for interactions, dose discipline, and what to do in case of emergency. I keep my current safety material in [Altered States Triage](%s)." % L('Altered States Triage'),
 'P28': "Legal issues differ greatly, and are sometimes not well defined, but a community should still write down where it stands: what’s allowed and what’s prohibited, what’s private, what’s insured, and what’s been legally reviewed. “I don’t think anybody here has ever heard of that” is information, but it’s not the same as a legal opinion.",
 'P29': "Plenty of people feel the same urge following a deep psychedelic or mystical experience: to find one’s tribe, to form a village, to help others get to whatever just opened up.",
 'P30': "I know this call. I also know the inflated sense of self that can come with it. You come back from this experience believing your love can heal anyone, and then you meet people who don’t want to change, and those who sincerely want to change but keep choosing the opposite, and those whose crisis is more than you can hold, however enthusiastic you are.",
 'P31': "Maybe the call is real, but building a village on a foundation of omnipotence is a terrible idea.",
 'P32': "A group that begins in collective spiritual euphoria can recruit too quickly and promise too much, and only do the math on how much need it can absorb once several people already depend on it. The sections on capacity and on membership, later on in this article, are partly there to protect the original generosity from that first rush.",
 'P33': "Once the initial flush of euphoria has passed and the call sobers up, it can become useful. A community can be a training ground where people learn the practices, care for one another, and sometimes move on to start a new experiment. This answers the reasonable objection that communes are just privileged escape pods.",
})
SRC2 = dict(SRC1)
WHY2 = {
 'P1': ['v2 (trace): the pace is back ("much faster than most of the literature … has caught up with"); New Mexico "signed … into law" (v1\'s "passed" read as not yet law); Australia\'s "limited access" back (v1\'s "able to use" read as unrestricted, or as psychiatrists taking the drugs).'],
 'P2': ['v2 (trace, grounding): "not all roses" read as "not wholly good", so "It hasn\'t been a smooth ride"; the FDA named in full for readers outside the US; Portugal back to the published scope (v1 had Emulate\'s "all drugs" and "use").'],
 'P3': ['v2 (grounding MUST, trace, cold read): "if one is going to build a community around this" could tell a community with occasional, gated ceremonies that the advice isn\'t for it; now "if medicine is going to be part of a community at all". "Local" back.'],
 'P4': ['v2 (trace): "intentional communities", "still" and "don\'t say so publicly" back; one local official, as published.'],
 'P6': ['v2 (trace, cold read): the survey\'s three findings are the survey\'s again, in the past tense; "First, consider" (v1\'s "first" could attach to building medicine in first).'],
 'P7': ['v2 (trace): "hate the work" (v1: wanting revelation "more than" the work), one person who "can collect" (v1: "plenty of people who will happily"), "unable to apologize"; the hedge "While this isn\'t true of everyone" out.'],
 'P8': ['v2 (trace): medicines "can loosen" defenses (v1: "can be used to let go of"), "otherwise" back, "produce confusion", "the community around them" (v1\'s "supporting their use" read as backing it).'],
 'P9': ['v2 (trace): the need is back ("an insight needs somewhere to land"); the people "who held you through it".'],
 'P10': ['v2 (trace): "That isolation" attracts the people again, as "That" did (v1: "I attracted").'],
 'P11': ['v2 (trace): "Sometimes they\'re great, but sometimes…" (v1 made both guesses); "The commercial alternative".'],
 'P12': ['v2 (cold read): "simply" out, and "someone watching over you", so the held/watched difference and iboga\'s long observation connect; "for years" back.'],
 'P13': ['v2 (trace): peers reality-check the downloads themselves; psychedelics "produce" real insight and "convincing" nonsense; parts that "look a lot like your mother" (v1: "stuff you got from your mother", an origin, not a likeness).'],
 'P14': ['v2 (stance, trace): v1\'s "rather than allowing people to take medicine when they want" made the community the one who permits, against "authority stays with the practitioner"; now the timing is against individual appetite, and "a shared calendar" is back.'],
 'P15': ['v2 (trace): logistics get easier "in a community" (v1: "when there\'s more of you"); "or sit quietly".'],
 'P16': ['v2 (trace): "wild things" out (not in the published); "inconvenient habits and all" brings back the point that in community you know each other\'s flaws.'],
 'P17': ['v2 (stance, trace, grounding): "They\'re not for everybody" out (it repeated the next sentence); "that enthusiasm will create casualties" (the cause, as published); v1\'s "go work with so-and-so, or we messed that one up and someone got hurt" narrowed referring out and admitting harm; now "go see someone outside who knows more, and admitting it when an experience caused harm".'],
 'P18': ['v2 (trace): lineages "most" (published: "usually"); the belief is the ayahuasca and Bwiti communities\' again.'],
 'P19': ['v2 (trace): "isn\'t accountable to anyone" (v1: "has little to be accountable to"); one "may" over the list (v1 hedged only the predator twice); the cost grows with the depth of opening again.'],
 'P20': ['v2 (trace): "One of the things" implied other unsolved problems; "may help"; "neither one solves it completely" (published: "I don\'t think either solves it completely").'],
 'P21': ['v2 (trace): "I want" back (Joel, 2026-10-02: it fits this article, about the community he wants); "while respecting the limits of their competence"; the two pieces are about their own subjects again.'],
 'P22': ['v2 (trace): "never" back ("peer led never means casual"); "combinations" and "emergency care" as published.'],
 'P23': ['v2 (trace): "See the linked articles for more explanation" implied a partial explanation here; now "The reasons are in the linked articles, rather than squeezed into one sentence here".'],
 'P24': ['v2 (stance): v1\'s "If a person hasn\'t done … the medicine can\'t do that work for them" read as advice someone could skip and still sit in ceremony; now the gate: the other pl/ork comes first. "Can\'t replace them" is Emulate A\'s.'],
 'P25': ['v2 (trace): "weeds out" (v1: "helps weed out"); "how likely are they…" (v1\'s "why would they…" read as near-certain; published: "unlikely").'],
 'P26': ['v2 (trace): "Integration is day to day life" (published: "is ordinary life"; v1: "a part of"); the weeks "show whether anything changed in the person".'],
 'P27': ['v2 (trace): "Supports matter" back; v1\'s new claim that Altered States Triage covers "a lot of this" out.'],
 'P28': ['v2 (stance, grounding, trace): v1\'s "some basic understanding … what might be insurable or require legal review" was a record of guesses; now the community writes down where it stands: allowed and prohibited, private, insured, legally reviewed.'],
 'P29': ['v2 (trace): "Plenty of people feel the same urge" (published: "Many people"; v1: "one of the most common impulses", a ranking); "whatever just opened up" back.'],
 'P30': ['v2 (stance, grounding, trace, cold read): "I also know the inflated sense of self" (first-hand); "your love can heal anyone"; the three groups as published, the third a limit on what you can hold (v1\'s "need more help than you imagined" could read as a cue to give more).'],
 'P31': ['v2 (trace): "Maybe the call is real" (a concession, as published; v1\'s "Even if" made it hypothetical); "terrible".'],
 'P32': ['v2 (trace, cold read): "recruit too quickly" back; the late discovery is the math of how much need it can absorb (v1: "how quickly things can get out of hand arithmetically", which a cold reader couldn\'t place).'],
 'P33': ['v2 (trace): sobering up makes the call useful again; "communes are just privileged escape pods".'],
}


# v3: what the v2 gate found (TRACE-v2-A to D, SENSE-v2, STANCE-v2), fixed before any Pangram call on these paragraphs
V[3] = dict(V[2])
V[3].update({
 'P1': V[2]['P1'].replace("New Mexico signed a [Medical Psilocybin Act](%s) into law in 2025." % L('Medical Psilocybin Act'), "New Mexico enacted a [Medical Psilocybin Act](%s) in 2025." % L('Medical Psilocybin Act')),
 'P3': V[2]['P3'].replace("the legality of this varies", "the legality of psychedelics varies"),
 'P8': V[2]['P8'].replace("the communal aspect of using these medicines has real value.", "the case for using these medicines communally is real too."),
 'P9': "Part of it is integration: an insight needs somewhere to land. When you gain insight and clarity about your life, you come back to the same environment you were in before, with all the old cues still waiting, and no one knows what happened to you. This is where it can be super helpful to have gone through the experience in a community, where the people who held you through it can also notice what happens to you in the months after.",
 'P10': V[2]['P10'].replace("That isolation helped give me a God complex, a Savior complex, or both, and then attracted exactly the right people", "That helped give me a God complex, a Savior complex, or both, which then attracted exactly the right people"),
 'P11': V[2]['P11'].replace("The commercial alternative is often to pay people you don’t know to support you for a night.", "That’s different from the commercial alternative, which is often to pay people you don’t know to support you for a night."),
 'P12': "If you’re working within a community, your sober sitter may be someone who has known you for years. Being held is different from just being watched, and that matters especially with long, medically risky experiences like iboga, where you need screening first and someone has to watch you the whole time.",
 'P13': "Your peers can also reality-check your downloads. Psychedelics produce real insight, but they also produce convincing nonsense, and it can be hard to tell the difference between the two since the lighting is the same. It helps to have friends who know you and your history, who may notice which parts of what you’re bringing back look like a new understanding and which parts look a lot like your mother.",
 'P15': V[2]['P15'].replace("Having somebody that the collective trusts to watch the kids.", "Arranging childcare together, with somebody everyone trusts to watch the kids."),
 'P16': "There will be people to play with! Raves often let strangers skip to that part of intimacy where they feel close before there’s any trust between them. Imagine doing ecstatic music and dance with people in a community who already know each other, inconvenient habits and all… 💃🕺",
 'P17': "Yeah, I won’t idealize psychedelics. There will be people that shouldn’t do them. There will be communities that shouldn’t be doing them. And enthusiasm will create casualties wherever people get access before they’re competent to work with them. If a community is going to dive into this it needs to do so in a humble way: being willing to say no, or not now, or go see someone outside who knows more, and to admit it when an experience caused harm.",
 'P20': "What I don’t know yet, though, is how a peer-led way of working with medicine keeps someone from becoming a de facto shaman anyway: the person everybody consults, trusts, and gradually stops questioning, even though nobody gave them the title. Rotating roles and public accountability may help, but I don’t think either one solves it completely.",
 'P23': V[2]['P23'].replace("rather than squeezed into one sentence here.", "rather than smuggled into one sentence here."),
 'P24': "Medicine comes after the other pl/ork. Reparenting, somatic capacity, and peer counseling come first. The medicine can deepen a practice that’s already there, but it can’t create months of honest relationship out of thin air.",
 'P25': V[2]['P25'].replace("how likely are they to suddenly become more relationally mature", "how likely are they to become more relationally mature"),
 'P27': "Supports matter more than how the ceremony looks. That means preparation, nutrition, screening for interactions, dose discipline, and knowing what to do in an emergency. I keep my current safety material in [Altered States Triage](%s)." % L('Altered States Triage'),
 'P28': V[2]['P28'].replace("are sometimes not well defined, but a community should still write down where it stands:", "are sometimes not well defined, so a community should write down where it stands:"),
 'P30': V[2]['P30'].replace("believing your love can heal anyone", "believing love can heal anyone"),
})
for k in ('P1', 'P3', 'P8', 'P10', 'P11', 'P23', 'P25', 'P28', 'P30'):
    assert V[3][k] != V[2][k], k
SRC3 = dict(SRC2)
SRC3['P24'] = 'e9-emuA, rebuilt'
WHY3 = {
 'P1': ['v3 (trace): "enacted" again ("signed … into law" asserted a signing step).'],
 'P3': ['v3 (trace): "the legality of psychedelics" ("of this" could point to trafficking, just before). The widening "if medicine is going to be part of a community at all" stays: it was the grounding review\'s one MUST (a community with occasional, gated ceremonies could think the advice isn\'t for it); the published says "Anyone building around medicine".'],
 'P8': ['v3 (trace): "the case for using these medicines communally is real too" (the published "case for", and its "also").'],
 'P9': ['v3 (trace): "you come back to the same environment" (v2\'s "wake up … still in" said you never left); "Part of it is integration" (v2\'s "A lot of it" weighted it).'],
 'P10': ['v3 (cold read, trace): "That" as published, and the complex is what attracts the people ("which then attracted"): the cold read couldn\'t see how isolation attracts anyone.'],
 'P11': ['v3 (trace): the difference is said ("That\'s different from the commercial alternative"), not only asked.'],
 'P12': ['v3 (cold read, trace): the held/watched difference matters with iboga because someone has to watch you the whole time; "long, medically risky experiences like iboga" as published.'],
 'P13': ['v3 (stance): friends "may notice" which parts "look like a new understanding" (v2\'s "see which parts … are insight" made them judges of your experience, against "authority stays with the practitioner").'],
 'P15': ['v3 (trace): childcare arranged together, with somebody everyone trusts (published: "Trusted childcare can be arranged collectively").'],
 'P16': ['v3 (trace): strangers, before there\'s any trust; people "who already know each other".'],
 'P17': ['v3 (trace): "a lot of people hella stoked" and "powerful" were new claims, out; the community does the four things again ("being willing to say no, or not now, or go see someone outside who knows more, and to admit it…").'],
 'P20': ['v3 (trace): "What I don\'t know yet" (published: "I don\'t yet know"); "a peer-led way of working with medicine", not his own approach; "I don\'t think either one solves it completely" out from under "I suspect".'],
 'P23': ['v3 (trace): "smuggled" back (v2\'s "squeezed" made it about space; published: candor about unargued judgments).'],
 'P24': ['v3 (trace): the closed list of three again (v2\'s "etc."), and v2\'s new claim "pharmacology can\'t replace them" out; "out of thin air" for "by pharmacological decree".'],
 'P25': ['v3 (trace): "suddenly" out (it limited the doubt to quick change).'],
 'P27': ['v3 (trace, cold read): v2\'s list after "how the ceremony looks:" could read as what the ceremony looks like; now the supports are named after "That means".'],
 'P28': ['v3 (trace): "so a community should write down" (the law\'s variation is the reason to write, as published; v2\'s "but … still" made it an obstacle).'],
 'P30': ['v3 (trace): "believing love can heal anyone" (v2: "your love").'],
}


# v4: what the v3 gate found (TRACE-v3-A and B, SENSE-v3, STANCE-v3)
V[4] = dict(V[3])
V[4].update({
 'P11': V[3]['P11'].replace("do you trust them? That’s different from the commercial alternative, which is often to pay people you don’t know to support you for a night.", "do you trust them? Being supported by people you trust is different from the commercial alternative, which is often to pay people you don’t know to look after you for a night."),
 'P17': "Yeah, I won’t idealize psychedelics. There will be people that shouldn’t do them. There will be communities that shouldn’t be doing them. And enthusiasm will create casualties wherever the competence hasn’t caught up with the access. If a community is going to dive into this it needs to do so in a humble way: being willing to say no, or to pause, or to send someone to an outside expert, and to admit it when an experience caused harm.",
 'P22': V[3]['P22'].replace("and a clear idea, before anybody takes anything, of when to bring in professional or emergency care.", "and a decision, made before anybody takes anything, about what calls for professional or emergency care."),
 'P24': V[3]['P24'].replace("Medicine comes after the other pl/ork.", "Medicine stays behind the other pl/ork."),
 'P27': V[3]['P27'].replace("dose discipline, and knowing what to do in an emergency.", "dose discipline, and an emergency plan."),
 'P30': V[3]['P30'].replace("and those whose crisis is more than you can hold, however enthusiastic you are.", "and those whose crisis needs more than enthusiasm."),
})
for k in ('P11', 'P22', 'P24', 'P27', 'P30'):
    assert V[4][k] != V[3][k], k
SRC4 = dict(SRC3)
WHY4 = {
 'P11': ['v4 (cold read): "That\'s different" had nothing to point to; now "Being supported by people you trust is different from the commercial alternative".'],
 'P17': ['v4 (trace): casualties come "wherever the competence hasn\'t caught up with the access" (v3 named the users\' competence); "or to pause, or to send someone to an outside expert" (published: "pause, refer out"; v3\'s "go see someone outside" could read as the community going itself).'],
 'P22': ['v4 (stance): "a decision, made before anybody takes anything, about what calls for professional or emergency care" (published: "Decide what requires professional or emergency care before anybody takes anything"; v3\'s "a clear idea" was weaker, against section 4\'s plans that "have to exist before the first ceremony").'],
 'P24': ['v4 (trace): "stays behind" (published), not "comes after".'],
 'P27': ['v4 (stance): "an emergency plan" (published: "emergency planning"; v3\'s "knowing what to do in an emergency" was know-how, not a plan made beforehand).'],
 'P30': ['v4 (trace): the limit is enthusiasm\'s again ("whose crisis needs more than enthusiasm"; published: "exceeds anything your enthusiasm can hold"), without the abstract agent.'],
}


# v5: after round 1 of Pangram (P6, P7, P18 with its heading, P31 and P33 100% AI; P2, P4P5, P5, P19 and P32 Human),
# Emulate round 2 on the runs around them (emu/outputs2.json, inputs from v4's text), with small fixes; and the v4
# gate's two findings (P11's feather, P15's childcare)
E2 = json.load(open(HERE / 'emu' / 'outputs2.json', encoding='utf-8'))
V[5] = dict(V[4])
V[5].update({
 'P6': "There’s a serious case against having medicine as part of a community. Physical and psychological negative effects of ayahuasca were common in the [Global Ayahuasca Survey](%s), although severe effects were far less common and context mattered. And the medicine can open people up faster than they (or their group) can deal with it." % L('Global Ayahuasca Survey'),
 'P7': "These medicines also attract people who love the revelatory side of the medicine but hate doing the work. Some will collect as many ceremonies and origin stories as they can and still can’t say sorry to a housemate. If a community is set up mainly around the peak experience, it’s going to find out that insight alone won’t get the dishes done, or the agreements revised, or a frightened child calmed down.",
 'P11': V[4]['P11'].replace("the person stroking a feather over you", "the person with the feather"),
 'P15': V[4]['P15'].replace("Arranging childcare together, with somebody everyone trusts to watch the kids.", "Having the group arrange childcare it can trust."),
 'P18': "I don’t believe in “special” shamans, which puts me in opposition to most lineages, especially in ayahuasca and Bwiti, where many communities believe medicine should stay under trained lineage authority. I still respect what those traditions have preserved, and I’ve learned from them.",
 'P29': "Quite a few people have a desire to form a village after some deep psychedelic or mystical experiences. There’s a strong urge to find “your people”, and to help others get to where you have.",
 'P30': "I know this urge. And I know the omnipotent tendency to grandiosity that can go along with it: “Love can heal anyone.” And then you run into the people who don’t want to change. And you run into the people who sincerely want to change, but who regularly choose the opposite. And you run into the people who need more help than you are capable of giving.",
 'P31': "It’s possible that the call is real, but it’s a terrible idea to form a village while you’re in that state.",
 'P21': V[4]['P21'].replace("I do, however, want people to learn", "Still, I want people to learn"),
 'P33': "After the euphoria wears off, and the “call” matures a bit, it can become useful. One of the functions of a place like this is to give people a place to learn the practices and care for one another, and sometimes to go off and start another experiment. That also deals with a reasonable objection to this whole idea: that people are just forming privileged little communities to get away from the world.",
})
for k in ('P11', 'P15'):
    assert V[5][k] != V[4][k], k
assert 'I don’t believe in “special” shaman' in E2['f2-emuB'] and 'It’s possible that the call is real' in E2['f3-emuB']
SRC5 = dict(SRC4)
SRC5.update({'P6': 'f1-emuB (round 2), rebuilt', 'P7': 'f1-emuB (round 2), rebuilt', 'P18': 'f2-emuB (round 2)', 'P29': 'f3-emuB (round 2)',
             'P30': 'f3-emuB (round 2)', 'P31': 'f3-emuB (round 2)', 'P33': 'f3-emuB (round 2)'})
WHY5 = {
 'P6': ['v5: v4\'s P6 read 100% AI alone. Rebuilt on round 2\'s f1-emuB ("One of the reasons not to have medicine as part of a community, as many of the physical and psychological negative effects of ayahuasca (found in the global ayahuasca survey) are quite common…"), with "serious" back, the findings the survey\'s, "context mattered" for its "highly contextualised", and no "In other words" (the outpacing isn\'t what the survey found).'],
 'P7': ['v5: v4\'s P7 read 100% AI alone. From round 2\'s f1-emuB ("like the revelatory aspects of the medicine but don\'t want to do the work"; "collect as many ceremonies and stories … as they can, but still struggle to say sorry to their housemate when they\'ve fucked up"; "then it\'s gonna be a bit shit"), with "love" and "hate" (published), "can\'t say sorry", no swearing, and the claim back: insight alone won\'t get the dishes done, the agreements revised, or a frightened child calmed down (the published triad, said plainly; "insight does not wash dishes" is a phrase AI has colonized).'],
 'P11': ['v5 (trace, three times): "the person with the feather", as published (v1 to v4 had Emulate\'s "stroking a feather over you", an action the original never gives them).'],
 'P15': ['v5 (stance): "Having the group arrange childcare it can trust" (published: "Trusted childcare can be arranged collectively"). v4\'s "somebody everyone trusts to watch the kids" made being trusted by everyone the qualification, which the essay names as how communities fail with children ("the adult may be … everybody\'s friend").'],
 'P18': ['v5: v4\'s P18 read 100% AI with its heading and P19 (P19 passes alone). From round 2\'s f2-emuB ("Note: I don\'t believe in “special” shaman, which is in opposition to most lineages, especially in ayahuasca and Bwiti."), with the lineages\' reason and Joel\'s respect back.'],
 'P29': ['v5: round 2\'s f3-emuB, with "find" for its "get to know" (published: "find the tribe"), for one voice across the subsection.'],
 'P30': ['v5: round 2\'s f3-emuB. Out: its "or don\'t even know they need to change" (new); in: "sincerely" and the published belief, "Love can heal anyone" (its quote was "I can help anybody with love"). Its third group keeps the limit as the seeker\'s capacity ("need more help than you are capable of giving").'],
 'P31': ['v5: v4\'s P31 read 100% AI with P32 (P32 passes alone). Round 2\'s f3-emuB, with "a terrible idea" (published: "terrible") for its "a bad idea"; "that state" is the grandiosity in P30.'],
 'P21': ['v5 (linter B13: three paragraphs opened with "I"): "Still, I want…" for "I do, however, want…".'],
 'P33': ['v5: v4\'s P33 read 100% AI alone. Round 2\'s f3-emuB, with "it can become useful" (its "it can be a great thing" hyped it), what people do there back ("learn the practices and care for one another, and sometimes …", published), "a reasonable objection" (its "one of the common objections") and "privileged" back.'],
}


# v6: what the v5 gate found (TRACE-v5-A and B, SENSE-v5; STANCE-v5 found no conflict)
V[6] = dict(V[5])
V[6].update({
 'P6': V[5]['P6'].replace("And the medicine can open people up faster than they (or their group) can deal with it.", "And these medicines can open things up faster than a person (or their group) can deal with."),
 'P7': "These medicines also attract people who love the revelatory side of the medicine but hate doing the work. Someone can collect as many ceremonies and origin stories as they like and still not be able to say sorry to a housemate. If a community is set up mainly around the peak experience, it’s going to find out that insight doesn’t get the dishes done, or the agreements revised, or a frightened child calmed down.",
 'P18': "No special shamans. That puts me at odds with most traditional lineages, including many ayahuasca and Bwiti communities, which believe medicine should stay under trained lineage authority. I still respect what those traditions have preserved, and I’ve learned from them.",
 'P29': V[5]['P29'].replace("and to help others get to where you have.", "and to help others get to whatever just opened up for you."),
 'P30': "I know this urge. And I know the omnipotent tendency to grandiosity that can go along with it: you come back believing love can heal anyone. And then you run into the people who don’t want to change. And you run into the people who sincerely want to change, but who regularly choose the opposite. And you run into the people whose crisis is more than your enthusiasm can hold.",
 'P33': "After the euphoria wears off and the call sobers up, it can become useful. A community like this can give people a place to learn the practices and care for one another, and sometimes to go off and start another experiment. That also deals with a reasonable objection to this whole idea: that people are just forming privileged little communities to get away from the world.",
})
for k in ('P6', 'P29'):
    assert V[6][k] != V[5][k], k
SRC6 = dict(SRC5)
WHY6 = {
 'P6': ['v6 (trace): "these medicines can open things up" (v5\'s "the medicine can open people up" read as about ayahuasca alone, and as opening the people rather than the material).'],
 'P7': ['v6 (trace): "Someone can collect…" (a possibility, as published; v5\'s "Some will" was a prediction); "insight doesn\'t get the dishes done" (v5\'s "insight alone won\'t" implied it does part of the work).'],
 'P18': ['v6 (trace): "No special shamans" back as the rule; "at odds with most traditional lineages, including many ayahuasca and Bwiti communities" (v5\'s scare-quoted "special", "opposition" and "especially" each changed the claim a little).'],
 'P29': ['v6 (trace): "whatever just opened up for you" (published: "whatever just opened"; v5\'s "where you have" made it a place reached).'],
 'P30': ['v6 (trace): the belief is the returning seeker\'s again ("you come back believing love can heal anyone"); the third group\'s crisis is "more than your enthusiasm can hold" (published), not a general need for help.'],
 'P33': ['v6 (trace, cold read): "the call sobers up" (published; v5\'s scare-quoted "call" that "matures a bit"); "A community like this can give people…" (v5\'s "a place like this" had nothing to point to, and "One of the functions … is" made a possibility a fact).'],
}


# v7: what the v6 gate found (TRACE-v6-A; STANCE-v6 on P31), and P31 after v6's P31P32 read 100% AI
V[7] = dict(V[6])
V[7].update({
 'P18': "No special shamans. That puts me at odds with most traditional lineages. Many ayahuasca and Bwiti communities, for instance, believe medicine should stay under trained lineage authority. I still respect what those traditions have preserved, and I’ve learned from them.",
 'P29': "Quite a few people feel a strong urge to form a village after some deep psychedelic or mystical experiences. They want to find their people, and to help others get to whatever just opened up for them.",
 'P30': "I know this urge. And I know the grandiosity that can go along with it: you come back believing love can heal anyone. And then you run into the people who don’t want to change. And you run into the people who sincerely want to change, but who keep choosing the opposite. And you run into the people whose crisis is more than your enthusiasm can hold.",
 'P31': "The call might be real, but omnipotence is a terrible thing to build a village on.",
 'P33': "After the euphoria wears off and the call sobers up, it can become useful. A community can give people a place to learn the practices and care for one another, and sometimes to go off and start another experiment. That also deals with a reasonable objection: that communes are just privileged little escapes from the world.",
})
SRC7 = dict(SRC6)
SRC7['P31'] = 'new (both versions so far read AI with P32: v4\'s and round 2\'s)'
WHY7 = {
 'P18': ['v7 (trace): "Many ayahuasca and Bwiti communities, for instance, believe…" (v6\'s "which believe" could attach to most traditional lineages).'],
 'P29': ['v7 (trace): one strong urge again, the village included; no quotation marks around "your people".'],
 'P30': ['v7 (trace): "the grandiosity" (v6\'s "omnipotent tendency to grandiosity" said more than "inflation"); "keep choosing the opposite" (published).'],
 'P31': ['v7 (stance, Pangram): round 2\'s "a terrible idea to form a village while you\'re in that state" made it a rule about timing, where the published says omnipotence is a bad premise for any community ("Omnipotence is a terrible founding document"), and with P32 it read 100% AI, as v4\'s "building a village on a foundation of omnipotence is a terrible idea" had. New: "The call might be real, but omnipotence is a terrible thing to build a village on." Not yet checked.'],
 'P33': ['v7 (trace): "A community can give people…" (v6\'s "A community like this" pointed at a kind of community the text never names); the objection is about communes again.'],
}


# v8: Joel's answers of 2026-10-03 04:03: the first-person lines are his, the ego deaths were at 25, "psychedelic
# medicine" in P3's widened advice, and P33 says the step he meant ("if people are training to spread the communal
# system then it's not an escape from society it's building a genuine alternative")
V[8] = dict(V[7])
V[8].update({
 'P3': V[7]['P3'].replace("if medicine is going to be part of a community at all", "if psychedelic medicine is going to be part of a community at all"),
 'P10': V[7]['P10'].replace("ego deaths at 26,", "ego deaths at 25,"),
 'P33': "After the euphoria wears off and the call sobers up, it can become useful. A community can be a training ground where people learn the practices, care for one another, and sometimes go off to start another one. If people are training there to spread the communal system, they’re building a genuine alternative to society instead of escaping it. That answers the reasonable objection that communes are just privileged escape pods.",
})
for k in ('P3', 'P10'):
    assert V[8][k] != V[7][k], k
SRC8 = dict(SRC7)
WHY8 = {
 'P3': ['v8 (Joel, 04:03): "wider version is good but i\'d say \'psychedelic medicine\' since medicine is too general".'],
 'P10': ['v8 (Joel, 04:03): the first-person lines are his, and the age was 25: "i found out it was age 25 not age 26".'],
 'P33': ['v8 (Joel, 04:03): the paragraph now says his step: "if people are training to spread the communal system then it\'s not an escape from society it\'s building a genuine alternative". Section 1 makes the same point ("some eventually leave to start the next one. Otherwise, we\'ve built a lovely refuge for whoever got there first"), but nothing may lean on a point sections back, so P33 says it itself. "Sometimes go off to start another one" (published: "sometimes leave to begin another experiment").'],
}


# v9: lists of three (E125/E126, Joel 2026-10-03 00:00-01:06, in the shared gate since main's turn 20-21): "lists of 3 in
# general are an ai pattern"; "when there's no actual need for 3 items you can remove one of them, the one that matters
# the least. when you need all 3 items to be there for meaning, then split it up". The linter failed v8's P3 (two lists)
# and flagged single lists in P7, P8, P15, P17, P20, P22, P27, P28 and P33, none of them checked on Pangram yet (P2's
# and P4's flags stay: both pass on Pangram; P16's is a false hit on "music and dance … habits and all").
V[9] = dict(V[8])
V[9].update({
 'P3': "To be sure, the legality of psychedelics varies by country and by state. It varies by substance, too. And it can depend on a group’s religious status and on what exactly it does. So if psychedelic medicine is going to be part of a community at all, that community should definitely get actual local legal advice.",
 'P7': V[8]['P7'].replace("insight doesn’t get the dishes done, or the agreements revised, or a frightened child calmed down.", "insight doesn’t get the dishes done or calm down a frightened child."),
 'P8': V[8]['P8'].replace("They can also produce confusion, grandiosity, dependency, and messy interactions with other people.", "They can also produce confusion and grandiosity. People can get dependent on them, and things between people can get messy."),
 'P15': V[8]['P15'].replace("Having people that can bring water, be close by, or sit quietly with somebody", "Having people that can bring water, or sit quietly with somebody"),
 'P17': "Yeah, I won’t idealize psychedelics. There will be people that shouldn’t do them. There will be communities that shouldn’t be doing them. And enthusiasm will create casualties wherever the competence hasn’t caught up with the access. If a community is going to dive into this it needs to do so in a humble way. Sometimes the answer has to be no, or not yet. Sometimes it means sending someone to an outside expert. And when an experience caused harm, the community has to admit it.",
 'P20': V[8]['P20'].replace("the person everybody consults, trusts, and gradually stops questioning", "the person everybody trusts and gradually stops questioning"),
 'P22': "But peer led never means casual. It means screening for medical and psychiatric contraindications and going over everyone’s medications and combinations. There has to be an appropriate sober sitter. And before anybody takes anything, the group decides what calls for professional or emergency care. When authority is distributed, the bar of required competence actually goes up.",
 'P27': "Supports matter more than how the ceremony looks. That means preparation and nutrition. It means screening for interactions and dose discipline, too. And there has to be an emergency plan. I keep my current safety material in [Altered States Triage](%s)." % L('Altered States Triage'),
 'P28': "Legal issues differ greatly, and are sometimes not well defined, so a community should write down where it stands: what’s allowed and what’s prohibited. It should write down what it keeps private and what’s actually insured. And it should note which activities have had a legal review. “I don’t think anybody here has ever heard of that” is information, but it’s not the same as a legal opinion.",
 'P33': V[8]['P33'].replace("where people learn the practices, care for one another, and sometimes go off to start another one.", "where people learn the practices and sometimes go off to start another one."),
})
for k in ('P7', 'P8', 'P15', 'P20', 'P33'):
    assert V[9][k] != V[8][k], k
SRC9 = dict(SRC8)
WHY9 = {
 'P3': ['v9 (E125): v8 had two lists in one sentence ("country, state, substance, religious status, what exactly one does, and so on"); all five axes are the published claim, so they\'re split, two to a sentence; Emulate\'s "and so on" out.'],
 'P7': ['v9 (E125): "or the agreements revised" out, the item that matters least, which also takes away the clash with Joel\'s section 4 correction that people do come back from visions with practical ideas (stance ledger D1).'],
 'P8': ['v9 (E125): the four harms kept, split: "confusion and grandiosity", then dependency and the mess between people.'],
 'P15': ['v9 (E125): "be close by" out (the person sitting with you is close by).'],
 'P17': ['v9 (E125): the four things kept, split into sentences: no or not yet, an outside expert, admitting harm.'],
 'P20': ['v9 (E125): "consults" out; the person everybody "trusts and gradually stops questioning" carries the danger.'],
 'P22': ['v9 (E125): the four requirements kept, split; "the group decides" for the published imperative "Decide … before anybody takes anything".'],
 'P27': ['v9 (E125): the five supports kept, two to a sentence and the emergency plan alone.'],
 'P28': ['v9 (E125): the five things to write down kept, split two, two and one; "actually insured" (the grounding review: a record of real coverage).'],
 'P33': ['v9 (E125): "care for one another" out: the paragraph\'s argument is about training people who go off to start another one.'],
}


# v10: what the v9 gate found (TRACE-v9-A and B, STANCE-v9; its finding on "25" is Joel's own correction)
V[10] = dict(V[9])
V[10].update({
 'P8': V[9]['P8'].replace("People can get dependent on them, and things between people can get messy.", "They can produce dependency, too, and things between people can get messy."),
 'P17': V[9]['P17'].replace("Sometimes the answer has to be no, or not yet.", "Sometimes the answer has to be no, or a pause."),
 'P28': V[9]['P28'].replace("It should write down what it keeps private and what’s actually insured.", "It should write down which activities are private and what’s actually insured."),
 'P33': "After the euphoria wears off and the call sobers up, it can become useful. A community can be a training ground where people learn the practices and sometimes go off to start another experiment. If people are training there to spread communal living, they’re building a genuine alternative to society, not just escaping it. That answers the reasonable objection that communes are just privileged escape pods.",
})
for k in ('P8', 'P17', 'P28'):
    assert V[10][k] != V[9][k], k
SRC10 = dict(SRC9)
WHY10 = {
 'P8': ['v10 (trace): "dependency" unspecified again (v9\'s "People can get dependent on them" made it dependence on the medicines).'],
 'P17': ['v10 (trace): "or a pause" (published: "pause"; v9\'s "not yet" only deferred).'],
 'P28': ['v10 (trace): "which activities are private" (v9\'s "what it keeps private" read as recording what it hides).'],
 'P33': ['v10 (stance, trace): "spread communal living" (v9\'s "the communal system" read as one system to copy, where the essay says the transmission needs no "one official version"); "start another experiment" (published); "not just escaping it" (the published objection is "merely" escape pods, and the essay elsewhere values community as an exit too: "I\'d rather have community and discover I didn\'t need an exit").'],
}


# v11: what the v10 gate found in P33 (STANCE-v10: "spread communal living" and "a genuine alternative to society"
# read as a rival society, where the essay's outward purpose is to "help other people build"); "a genuine
# alternative" stays: it is Joel's own framing (04:03), and goes to him as information
V[11] = dict(V[10])
V[11].update({
 'P33': V[10]['P33'].replace("If people are training there to spread communal living, they’re building a genuine alternative to society, not just escaping it.", "If people are training there so they can help others build communities like it, they’re building a genuine alternative, not just escaping society."),
})
assert V[11]['P33'] != V[10]['P33']
SRC11 = dict(SRC10)
WHY11 = {'P33': ['v11 (stance): "so they can help others build communities like it" (the essay\'s outward purpose: "to help other people build"; v10\'s "spread communal living" read as a rival society). "A genuine alternative, not just escaping society" keeps Joel\'s framing of 04:03.']}



# v12: the paragraphs still reading AI after API batches 1 to 3, rebuilt by fresh writers (Emulate's key returned 403
# from 04:30): eight Opus writers, one brief each (writers/W1-W8.txt, built by writers/build_writers.py), three
# variants each (writers/outputs-raw.md, exact). Picked on meaning, with the earlier gates' findings applied (fixlog);
# apostrophes made the article's. v13 is the alternate set, gated with v12 so a paragraph that still reads AI has a
# gated replacement ready.
WL = lambda t: re.sub(r"\[\[(.+?)\]\]", lambda m: '[%s](%s)' % (m.group(1), WRITER_LINKS[m.group(1)]), t).replace("'", "’")
WRITER_LINKS = {
 "Oregon's licensed psilocybin service centers": L('Oregon’s licensed psilocybin service centers'),
 'limited access to psilocybin and MDMA': L('authorized psychiatrists have had limited access to psilocybin and MDMA'),
 'authorized psychiatrists limited access to psilocybin and MDMA': L('authorized psychiatrists have had limited access to psilocybin and MDMA'),
 'Medical Psilocybin Act': L('Medical Psilocybin Act'),
 'peer-held ceremonies': L('peer-held ceremonies'),
 'the best psychopath shaman I ever met': L('the best psychopath shaman I ever met'),
 'ketamine and MDMA': L('ketamine and MDMA'),
 'bufo': L('bufo'),
 'Altered States Triage': L('Altered States Triage'),
}
V[12] = dict(V[11])
V[12].update({
 'P1': WL("If you went by most of what's written about communities, you'd badly underestimate how quickly psychedelics have moved from taboo toward regulated use. Australia's authorized psychiatrists have had [[limited access to psilocybin and MDMA]] for specified conditions since 2023, and [[Oregon's licensed psilocybin service centers]] began opening that year. In 2025, New Mexico enacted a [[Medical Psilocybin Act]] and Colorado started licensing under a regulated natural-medicine system it created."),
 'P7': WL("They also attract people who love revelation but can't stand the follow-through. You can meet someone with 12 ceremonies and a pile of origin stories who still can't apologize to a housemate. Eventually, a community organized mainly around the peak experience learns that the practical work of living together is still there after the insight (somebody has to wash dishes and calm a frightened child)."),
 'P8': WL("From what I've seen, the case for communal use is real too. Psychedelics can loosen the defenses that otherwise take over every serious conversation. People who sit through difficult nights together can end up powerfully bonded. But psychedelics can also leave people confused or grandiose. Some end up dependent. And then there's the mess between people. Is the community around them mature enough to tell the difference?"),
 'P12': WL("In a community, though, your sober sitter may be someone who's known you for years, and you feel the difference between being watched and being held. That matters even more with iboga and other long, medically risky experiences, which require screening beforehand and continuous observation."),
 'P13': WL("Peers can reality-check the downloads too, since psychedelics produce genuine insight and convincing nonsense, and the two look alike (same lighting and everything). Friends who know your history may notice which parts look like a new understanding and which look like your mother."),
 'P14': WL("And people living together fall into a rhythm. Many traditional medicine systems hold ceremonies on communal timing, not one person's appetite. With a shared calendar, folks can cut down on compulsive repetition and leave time for integration."),
 'P17': WL("But I won't idealize psychedelics. Some people and communities should avoid them. Where access is ahead of know-how, people will become casualties of somebody's enthusiasm. Is your community humble enough to say no, or pause? Using the medicine takes that. It also takes humility to refer people out, and admit when an experience did harm."),
 'P18': WL("No special shamans, which traditional lineages usually disagree with me on. Many ayahuasca and Bwiti communities believe the medicine should stay under the authority of whoever's trained in the lineage. And I've learned from those traditions myself. I respect what they've preserved."),
 'P20': WL("In a peer-led medicine culture, how do you keep an informal shaman from showing up anyway? That's the person everybody trusts and slowly stops questioning, even though nobody gave them the title. I don't know yet. Rotating roles might help, and so might public accountability. I don't think either one fixes it all the way."),
 'P21': WL("Still, I want people to learn to guide themselves and care for each other, within the limits of their competence. I've written more about [[peer-held ceremonies]], and about [[the best psychopath shaman I ever met]]."),
 'P22': WL("Peer-led never means casual. When authority is spread across a group, people need more competence, not less. So there's screening for medical and psychiatric contraindications, plus a review of medications and combinations. You need an appropriate sober sitter. And before anybody takes anything, it's already settled what calls for professional or emergency care."),
 'P23': WL("Also, I'm especially cautious about medicines and protocols I consider more destabilizing or more of a medical burden. That includes some uses of [[ketamine and MDMA]] and [[bufo]]. My reasons are in those articles, not smuggled into one sentence here."),
 'P24': WL("The medicine stays behind the other pl/ork. Reparenting and somatic capacity come first. Peer counseling does too. Nobody gets months of honest relationship by pharmacological decree, but if a practice is already there, medicine can deepen it."),
 'P25': WL("Making that a prerequisite also keeps out experience collectors. If someone won't spend 6 months learning to listen without fixing, they're unlikely to become more relationally mature because the visions were especially geometric."),
 'P26': WL("Integration is just regular life. The ceremony opens something, and you find out in the weeks after whether anything changed. Changes show up in relationships and daily behavior. You'll see them in sleep and decisions too. Another sign is whether the person can tolerate frustration without declaring a new spiritual emergency."),
 'P27': WL("Supports matter. By supports I mean preparation and nutrition. I also mean interaction screening and dose discipline. Plus an emergency plan, worked out ahead of time. That all matters more than ceremony aesthetics. My current safety material is in [[Altered States Triage]]."),
 'P31': WL("Yeah, the call may be real. A community founded on omnipotence is a terrible idea."),
})
for k in ('P1', 'P7', 'P8', 'P12', 'P13', 'P14', 'P17', 'P18', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P31'):
    assert V[12][k] != V[11][k] and "'" not in V[12][k] and '[[' not in V[12][k], k
SRC12 = dict(SRC11)
SRC12.update({'P1': 'writer W1 C', 'P7': 'writer W2 A', 'P8': 'writer W2 A', 'P12': 'writer W3 A', 'P13': 'writer W3 A', 'P14': 'writer W3 A',
              'P17': 'writer W4 C', 'P18': 'writer W5 A', 'P20': 'writer W6 A', 'P21': 'writer W7 A', 'P22': 'writer W7 B', 'P23': 'writer W7 A',
              'P24': 'writer W7 A', 'P25': 'writer W7 A', 'P26': 'writer W7 A', 'P27': 'writer W7 C', 'P31': 'writer W8 A'})
WHY12 = {
 'P1': ['v12: v11 read 100% AI (try 1, batch 1). Writer W1 C, exact: the five facts as published (enacted, authorized, limited access, specified conditions), the pace as "you\'d badly underestimate how quickly" (published: "much faster than most community literature has acknowledged"), grouped by year.'],
 'P7': ['v12: v11 read 100% AI (try 3). Writer W2 A, exact: "12 ceremonies" is the published "twelve ceremonies"; "can\'t stand" for "hate"; insight doesn\'t do the practical work (dishes, a frightened child; "revise agreements" stays out, v9).'],
 'P8': ['v12: v11 read 100% AI (try 1, batch 3). Writer W2 A, with "From what I\'ve seen, … real too" for its "I\'ve also found … is real" (linter B13: six paragraphs opened with "I"), and "Some end up dependent" for its "Some folks get dependent on them" (dependency unspecified, as v10\'s trace asked); the question stays a question.'],
 'P12': ['v12: v11 read 100% AI (try 1, batch 1). Writer W3 A, with "you feel" for its "you can feel" (linter E41: one "you can" in 47 words is coach density 2.1): "though" answers P11\'s four-hour stranger; the held/watched difference matters more with iboga, which requires screening and continuous observation.'],
 'P13': ['v12: v11 read 100% AI alone and with P14 (try 1). Writer W3 A, with "(same lighting and everything)" added: the writers dropped the published quip "with identical lighting", and a joke stays unless Joel cuts it.'],
 'P14': ['v12: P13P14 read 100% AI. Writer W3 A, exact: folks cut down on repetition with a shared calendar (the community doesn\'t permit, v2 stance).'],
 'P17': ['v12: v11 read 100% AI alone (try 1). Writer W4 C, with "But" first (B13; writer W4 A\'s opener, after P16\'s rave): "where access is ahead of know-how" leaves whose competence open (v4 trace: naming the users\' competence was a shift); the four duties as two and two.'],
 'P18': ['v12: H2bP18P19 read 100% AI (try 2). Writer W5 A, exact: the rule opens the paragraph; "usually"; the lineages\' belief is the ayahuasca and Bwiti communities\'.'],
 'P20': ['v12: v11 read 100% AI (try 1). Writer W6 A, exact: Joel\'s open question asked as a question, then "I don\'t know yet"; "might help"; "I don\'t think either one fixes it all the way".'],
 'P21': ['v12: the P21 to P27 run read AI in every window. Writer W7 A, with "Still," first (B13, as v5): "I want" (Joel\'s community), within the limits of their competence, both links on their words.'],
 'P22': ['v12: v11 read 100% AI (try 1) and 57% AI with P21. Writer W7 B, exact: the reason first (spread authority, more competence), then the four requirements; the emergency decision settled "before anybody takes anything".'],
 'P23': ['v12: writer W7 A, with "Also," first (B13): "some uses of" both links, "I consider", "smuggled".'],
 'P24': ['v12: writer W7 A, exact: "stays behind", the three practices first (two and one), "by pharmacological decree" back.'],
 'P25': ['v12: writer W7 A, exact: "unlikely" (published) for v11\'s question; "6 months".'],
 'P26': ['v12: writer W7 A, exact: all five places a change shows, two, two and one.'],
 'P27': ['v12: writer W7 C, exact: the five supports, two, two and one; an emergency plan worked out ahead of time; "more than ceremony aesthetics".'],
 'P31': ['v12: three versions read AI with P32 (try 3 in batch 1). Writer W8 A, exact: the concession, then omnipotence as a bad basis for any community (not timing, v7 stance). To be checked with P30, which passes alone.'],
}

# v13: the alternates (gated with v12; each replaces its v12 paragraph only if v12's reads AI)
V[13] = dict(V[12])
V[13].update({
 'P1': WL("Most people writing about communities are way behind on how fast psychedelics have moved from taboo toward regulated use. [[Oregon's licensed psilocybin service centers]] started opening in 2023, and Colorado, which created a regulated natural-medicine system, began licensing in 2025. New Mexico enacted a [[Medical Psilocybin Act]] that same year. And since 2023, Australia has given [[authorized psychiatrists limited access to psilocybin and MDMA]] for specified conditions."),
 'P7': WL("They're also a magnet for people who are all about revelation and hate the follow-through. Some have done lots of ceremonies and have plenty of origin stories, and still can't apologize to a housemate. Organize a community mainly around the peak experience and you'll eventually find that living together still takes practical work after the insight, like washing dishes or calming a frightened child."),
 'P8': WL("My experience is that the case for communal use is real too, since on psychedelics the defenses that usually dominate every serious conversation can loosen, and people who sit through hard nights together can form a powerful bond. Psychedelics can also leave people confused. Or grandiose. And some end up dependent, or in a mess with each other. Does the community around them have the maturity to tell those apart?"),
 'P12': WL("In a community, your sober sitter may be somebody who's known you for years. Being held by a person like that feels different from being watched, which counts for even more with something long and medically risky like iboga (screening beforehand and continuous observation are essential there)."),
 'P13': WL("Your peers can reality-check the downloads, too. Psychedelics produce convincing nonsense alongside genuine insight, and the two look alike, right down to the lighting. Friends who know your history may notice which parts look like a new understanding. And which parts look like your mother."),
 'P14': WL("Communities also run on a rhythm. In many traditional medicine systems, ceremonies happen on communal timing rather than individual appetite, and sharing a calendar that way can mean less compulsive repetition and more time for integration."),
 'P17': WL("But I won't idealize psychedelics. Some people should avoid them, and some communities shouldn't use them. Wherever access gets ahead of skill, eager folks will cause casualties. A community on this path needs the humility to say no or hit pause. Same goes for referring people out, and owning up when an experience did harm."),
 'P18': WL("No special shamans. Traditional lineages tend to disagree with me, and many ayahuasca and Bwiti communities will tell you the medicine should stay in the hands of trained lineage holders. These are traditions I've learned from, and I respect what they've preserved."),
 'P20': WL("Even a peer-led medicine culture can end up with an informal shaman (the person everybody trusts and gradually stops questioning, though nobody gave them the title). I don't know yet how to prevent that, other than maybe rotating roles and public accountability. And I don't think either one is a complete fix."),
 'P21': WL("Still, I want people to learn to guide themselves and to care for each other. And I want them to respect the limits of their competence. (I've written more about [[peer-held ceremonies]] and [[the best psychopath shaman I ever met]].)"),
 'P22': WL("Peer-led never means casual. Before anybody takes anything, the group decides what calls for professional or emergency care. People get screened for medical and psychiatric contraindications. Somebody reviews their medications, combinations included. The sober sitter has to be appropriate. Spread authority around and the bar for competence goes up, not down."),
 'P23': WL("Also, I consider some medicines and protocols more destabilizing or medically burdensome, and I'm especially cautious with those. Some uses of [[ketamine and MDMA]] and [[bufo]] fall into that category. The linked articles explain why. I'm not smuggling that into one sentence here."),
 'P24': WL("The medicine stays behind the rest of the pl/ork. First comes reparenting, along with somatic capacity. So does peer counseling. Medicine can deepen a practice that's already there. Months of honest relationship, though? You can't create those by pharmacological decree."),
 'P25': WL("This prerequisite also filters out experience collectors, since someone who won't spend six months learning to listen without fixing is unlikely to become more relationally mature just because the visions were especially geometric."),
 'P27': WL("Supports matter more than the aesthetic details of the ceremony. Preparation and nutrition are supports. So are interaction screening and dose discipline. And somebody plans for emergencies in advance. My current safety material is in [[Altered States Triage]]."),
 'P31': WL("Maybe the call itself is real. I'm not saying it isn't. But that feeling of omnipotence makes a terrible foundation for a community."),
})
for k in ('P1', 'P7', 'P8', 'P12', 'P13', 'P14', 'P17', 'P18', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P27', 'P31'):
    assert V[13][k] != V[12][k] and "'" not in V[13][k] and '[[' not in V[13][k], k
SRC13 = dict(SRC12)
SRC13.update({'P1': 'writer W1 B', 'P7': 'writer W2 C', 'P8': 'writer W2 C', 'P12': 'writer W3 C', 'P13': 'writer W3 C', 'P14': 'writer W3 C',
              'P17': 'writer W4 A, edited', 'P18': 'writer W5 C', 'P20': 'writer W6 C', 'P21': 'writer W7 B, edited', 'P22': 'writer W7 A', 'P23': 'writer W7 C',
              'P24': 'writer W7 B', 'P25': 'writer W7 B', 'P27': 'writer W7 A', 'P31': 'new (mine)'})
WHY13 = {
 'P1': ['v13 (alternate): writer W1 B, exact.'],
 'P7': ['v13 (alternate): writer W2 C, exact.'],
 'P8': ['v13 (alternate): writer W2 C, exact ("some end up dependent": dependency unspecified).'],
 'P12': ['v13 (alternate): writer W3 C, exact.'],
 'P13': ['v13 (alternate): writer W3 C, with ", right down to the lighting" (the published quip, kept), and "Your peers can" for its "You can have your peers" (linter E41).'],
 'P14': ['v13 (alternate): writer W3 C, exact.'],
 'P17': ['v13 (alternate): writer W4 A, with "Wherever access gets ahead of skill, eager folks will cause casualties" for its "Eager folks with more access than skill will cause casualties" (whose competence stays open, v4 trace).'],
 'P18': ['v13 (alternate): writer W5 C, exact (W5 B opened with "I", B13).'],
 'P20': ['v13 (alternate): writer W6 C, exact.'],
 'P21': ['v13 (alternate): writer W7 B, with "Still," first (B13) and "to respect" for its "respecting".'],
 'P22': ['v13 (alternate): writer W7 A, exact.'],
 'P23': ['v13 (alternate): writer W7 C, with "Also," first (B13).'],
 'P24': ['v13 (alternate): writer W7 B, exact.'],
 'P25': ['v13 (alternate): writer W7 B, exact.'],
 'P27': ['v13 (alternate): writer W7 A, exact.'],
 'P31': ['v13 (alternate): mine ("Maybe", not "The", first: B13): the concession said aloud ("I\'m not saying it isn\'t"), and "that feeling of omnipotence" ties the word to P30\'s grandiosity.'],
}



# v14: v12 with what its gate found (TRACE-v12-A and B, STANCE-v12, SENSE-v12, GROUNDING-v12); v15: v13 (the
# alternates) with what its gate found (TRACE-v13-A and B, STANCE-v13, SENSE-v13, GROUNDING-v13). Both stance checks
# found Joel's "25" (his own correction, information only); STANCE-v13 also found P33's "communities like it" (mine).
def fix(d, k, a, b):
    assert d[k].count(a) == 1, (k, a)
    d[k] = d[k].replace(a, b)
V[14] = dict(V[12])
fix(V[14], 'P2', "It hasn't been a smooth ride, either, and it isn't inevitable.", "It hasn't been a smooth ride, though, and it isn't inevitable.")
fix(V[14], 'P7', "You can meet someone with 12 ceremonies and a pile of origin stories who still can’t apologize to a housemate. Eventually, a community organized mainly around the peak experience learns that", "You can meet someone who’s collected 12 ceremonies and 6 origin stories and still can’t apologize to a housemate. Any community organized mainly around the peak experience will eventually learn that")
fix(V[14], 'P8', "From what I’ve seen, the case for communal use is real too. Psychedelics can loosen the defenses that otherwise take over every serious conversation. People who sit through difficult nights together can end up powerfully bonded. But psychedelics can also leave people confused or grandiose. Some end up dependent. And then there’s the mess between people. Is the community around them mature enough to tell the difference?",
    "But in my experience, the case for communal use is real too. Psychedelics can loosen the defenses that otherwise take over every serious conversation. People who sit through difficult nights on them together can end up powerfully bonded. Psychedelics can also leave people confused or grandiose. Some can end up dependent. And then there’s the mess between people. Is the community around them mature enough to tell the good from the bad?")
fix(V[14], 'P14', "And people living together fall into a rhythm.", "And community creates a rhythm.")
fix(V[14], 'P17', "Where access is ahead of know-how, people will become casualties of somebody’s enthusiasm.", "Where access is ahead of competence, people will become casualties of enthusiasm.")
fix(V[14], 'P18', "believe the medicine should stay under the authority of whoever’s trained in the lineage.", "believe the medicine should stay under the authority of trained lineage holders.")
fix(V[14], 'P22', "So there’s screening for medical and psychiatric contraindications, plus a review of medications and combinations. You need an appropriate sober sitter. And before anybody takes anything, it’s already settled what calls for professional or emergency care.",
    "So there has to be screening for medical and psychiatric contraindications, plus a review of medications and combinations. You need an appropriate sober sitter. And before anybody takes anything, the group has to settle what calls for professional or emergency care.")
fix(V[14], 'P26', "Changes show up in relationships and daily behavior. You’ll see them in sleep and decisions too.", "Any change would show up in relationships and daily behavior. You’d see it in sleep and decisions too.")
fix(V[14], 'P33', "so they can help others build communities like it,", "so they can help others build communities of their own,")
SRC14 = dict(SRC12)
WHY14 = {
 'P2': ['v14 (cold read, both runs; SENSE-v3 too): "though" for "either" (the paragraph before is all progress, so "either" had no negative to pair with).'],
 'P7': ['v14 (trace): "who’s collected" (the published "collect", which sets up P25’s "experience collectors"); "12 ceremonies and 6 origin stories" (the published counts; "a pile" implied more); "Any community … will eventually learn" (the published prediction about every such community). "A new sacred name" stays out: the third item of the published list of three, the one that matters least (E125, Joel 2026-10-03).'],
 'P8': ['v14 (trace, B13): "But in my experience" (published; "From what I’ve seen" narrowed it to watching others; "But" turns from the case against, and keeps the openers varied); the bonds come from difficult nights "on them" (psychedelics create the bonds, as published); "Some can end up dependent" (published: "can produce"); (cold read, both runs) "tell the good from the bad" (published: "tell those apart", the good effects from the harms).'],
 'P14': ['v14 (trace): "community creates a rhythm" (published: "Community creates rhythm"; "people living together fall into" made it something that happens to them).'],
 'P17': ['v14 (trace): "casualties of enthusiasm" (published: "enthusiasm will create casualties"; "somebody’s" pinned it on one person); "competence" (published) for "know-how".'],
 'P18': ['v14 (trace): "trained lineage holders" (published: "trained lineage authority"; "whoever’s trained" was any trained individual).'],
 'P22': ['v14 (trace): the requirements are requirements again ("has to be screening", "the group has to settle"; "there’s screening" and "it’s already settled" read as a description).'],
 'P26': ['v14 (trace): "Any change would show up … You’d see it" (the weeks show whether anything changed; "Changes show up" said they will).'],
 'P33': ['v14 (STANCE-v13): "communities of their own" (mine, v11’s "communities like it", read as copies of this one; the essay wants daughter communities free to differ, "with different values"). Joel’s "spread the communal system" (04:03) is about communal living, not this community’s model.'],
}
V[15] = dict(V[13])
for k in ('P2', 'P14', 'P26', 'P33'):
    V[15][k] = V[14][k]   # P14 too: v13's P14 had no finding, but v14's fix is the published claim; P26 has no alternate
V[15]['P14'] = V[13]['P14']
fix(V[15], 'P1', "Most people writing about communities are way behind on how fast", "Most of what’s been written about communities is way behind on how fast")
fix(V[15], 'P7', "Some have done lots of ceremonies and have plenty of origin stories, and still can’t apologize to a housemate.", "Someone can collect 12 ceremonies and 6 origin stories and still not be able to apologize to a housemate.")
fix(V[15], 'P8', "and people who sit through hard nights together can form a powerful bond.", "and people who sit through hard nights on them together can form a powerful bond.")
fix(V[15], 'P8', "And some end up dependent, or in a mess with each other. Does the community around them have the maturity to tell those apart?", "And some can end up dependent, or in a mess with each other. Does the community around them have the maturity to tell the good from the bad?")
fix(V[15], 'P12', "Being held by a person like that feels different from being watched, which counts for even more with something", "Being held by a person like that feels different from being watched. That counts for even more with something")
fix(V[15], 'P17', "Wherever access gets ahead of skill, eager folks will cause casualties.", "Wherever access gets ahead of competence, enthusiasm is going to leave casualties.")
fix(V[15], 'P18', "Traditional lineages tend to disagree with me, and many", "Traditional lineages tend to disagree with me on this, and many")
fix(V[15], 'P20', "I don’t know yet how to prevent that, other than maybe rotating roles and public accountability.", "I don’t know yet how to prevent that. Rotating roles and public accountability might help.")
fix(V[15], 'P21', "to care for each other. And I want them to respect the limits of their competence.", "to care for each other, while respecting the limits of their competence.")
fix(V[15], 'P22', "Before anybody takes anything, the group decides what calls for professional or emergency care. People get screened for medical and psychiatric contraindications. Somebody reviews their medications, combinations included. The sober sitter has to be appropriate.",
    "Before anybody takes anything, the group has to decide what calls for professional or emergency care. People need screening for medical and psychiatric contraindications. Their medications need reviewing, combinations included. There has to be an appropriate sober sitter.")
fix(V[15], 'P24', "First comes reparenting, along with somatic capacity. So does peer counseling.", "Reparenting and somatic capacity come first. So does peer counseling.")
fix(V[15], 'P25', "This prerequisite also filters out experience collectors, since someone who won’t", "This prerequisite also filters out experience collectors. Someone who won’t")
fix(V[15], 'P27', "So are interaction screening and dose discipline. And somebody plans for emergencies in advance.", "So are interaction screening and dose discipline. An emergency plan made in advance is one too.")
fix(V[15], 'P31', "Maybe the call itself is real. I’m not saying it isn’t. But that feeling", "Maybe the call itself is real. But that feeling")
SRC15 = dict(SRC13)
WHY15 = {
 'P1': ['v15 (trace): "Most of what’s been written" (published: the literature; "people writing" faulted the writers).'],
 'P7': ['v15 (trace): "Someone can collect 12 ceremonies and 6 origin stories" (published: a possibility, the "collect" that sets up P25, the counts; "Some have done" asserted such people exist).'],
 'P8': ['v15 (trace): bonds from hard nights "on them"; "some can end up dependent" (published: "can produce"); (cold read) "the good from the bad".'],
 'P12': ['v15 (trace, grounding): "That counts for even more" (v13’s "which" could attach to "being watched").'],
 'P17': ['v15 (trace, stance close call): "enthusiasm is going to leave casualties" (published: "enthusiasm will create casualties"; "eager folks will cause" made people the perpetrators); "competence" (published).'],
 'P18': ['v15 (trace): "disagree with me on this" (published: "here"; without it the disagreement wasn’t limited to this point).'],
 'P20': ['v15 (trace): "Rotating roles and public accountability might help" (published: "may help"; "other than maybe" made them the only ideas).'],
 'P21': ['v15 (trace): "while respecting the limits of their competence" (published; "And I want them to respect" made it a separate want).'],
 'P22': ['v15 (trace, stance close call): the requirements are requirements ("has to decide", "need screening", "need reviewing", "There has to be"); no new "Somebody".'],
 'P24': ['v15 (trace): "Reparenting and somatic capacity come first. So does peer counseling." (v13’s "First comes reparenting, along with somatic capacity" ranked them).'],
 'P25': ['v15 (trace): two sentences, as published ("since" made one the reason for the other).'],
 'P27': ['v15 (trace): "An emergency plan made in advance is one too" (a support, as published; "somebody plans" added a person).'],
 'P31': ['v15 (trace): "I’m not saying it isn’t" out (it strengthened the concession).'],
}



# v16: the candidate after API batch 4a (05:52 UTC). P12, P21, P23, P27 and P31 (with P30) pass; P1, P13, P20, P24 and
# P25 read AI, so their gated alternates (v15) go in as the next try; and what the round-2 gate found (TRACE-v14-A,
# TRACE-v15-A and B, STANCE-v14 and v15, SENSE-v14 and v15) in P8 and P22. v17: the alternate set with the same fixes.
V[16] = dict(V[14])
for k in ('P1', 'P13', 'P20', 'P24', 'P25'):
    V[16][k] = V[15][k]
fix(V[16], 'P8', "People who sit through difficult nights on them together can end up powerfully bonded. Psychedelics can also leave people confused or grandiose. Some can end up dependent. And then there’s the mess between people.",
    "And sitting through a difficult medicine night together can bond people powerfully. Then again, psychedelics can also leave people confused or grandiose. They can leave some people dependent, too. And then there’s the mess they can make between people.")
fix(V[16], 'P8', "They can leave some people dependent, too.", "They can leave people dependent, too.")
fix(V[16], 'P22', "And before anybody takes anything, the group has to settle what calls for professional or emergency care.", "And what calls for professional or emergency care has to be settled before anybody takes anything.")
SRC16 = dict(SRC14)
SRC16.update({k: SRC15[k] for k in ('P1', 'P13', 'P20', 'P24', 'P25')})
WHY16 = {
 'P1': ['v16: v14’s P1 (writer W1 C) read 100% AI (batch 4a); the gated alternate (v15, writer W1 B) is the next try.'],
 'P13': ['v16: v14’s P13 read 100% AI alone and with P12, which passes alone (batch 4a); the gated alternate (v15, writer W3 C) is the next try.'],
 'P20': ['v16: v14’s P20 (writer W6 A) read 100% AI (batch 4a); the gated alternate (v15, writer W6 C) is the next try.'],
 'P24': ['v16: v14’s P24 read 100% AI alone and with P23 and P25 (batch 4a); the gated alternate (v15, writer W7 B) is the next try.'],
 'P25': ['v16: v14’s P25 read 100% AI alone and with P24 (batch 4a); the gated alternate (v15, writer W7 B) is the next try.'],
 'P8': ['v16 (TRACE-v14 and v15): "sitting through a difficult medicine night together can bond people powerfully" (published: psychedelics create the bonds when people sit through difficult nights; "on them" put everyone in the bond on the drug); "They can leave some people dependent, too", "the mess they can make" (published: psychedelics produce both; the dependency stays unspecified, v10); (SENSE-v14) "Then again" marks the swing back to the harms; (TRACE-v16-A) "leave people dependent", not "some people" (published: dependency at the same strength as the other harms).'],
 'P22': ['v16 (TRACE-v15-B): "what calls for professional or emergency care has to be settled before anybody takes anything" (published: an instruction that names no decider; "the group" named one).'],
}
V[17] = dict(V[15])
fix(V[17], 'P8', "My experience is that the case for communal use is real too, since on psychedelics the defenses that usually dominate every serious conversation can loosen, and people who sit through hard nights on them together can form a powerful bond.",
    "My experience is that the case for communal use is real too. On psychedelics, the defenses that usually dominate every serious conversation can loosen. And sitting through a hard medicine night together can form a powerful bond.")
fix(V[17], 'P18', "many ayahuasca and Bwiti communities will tell you the medicine should stay in the hands of trained lineage holders.", "many ayahuasca and Bwiti communities believe the medicine should stay in the hands of trained lineage holders.")
fix(V[17], 'P22', "Their medications need reviewing, combinations included.", "Medications and combinations need reviewing.")
fix(V[17], 'P22', "Before anybody takes anything, the group has to decide what calls for professional or emergency care.", "What calls for professional or emergency care has to be decided before anybody takes anything.")
SRC17 = dict(SRC15)
WHY17 = {
 'P8': ['v17 (TRACE-v15-A): the benefits are general claims again, not the reasons inside "My experience is that" ("since" out); the bond from "a hard medicine night" sat through together (not everyone "on them").'],
 'P18': ['v17 (TRACE-v15-A): "believe" (published; "will tell you" distanced it).'],
 'P22': ['v17 (TRACE-v15-B): "Medications and combinations need reviewing" (published: "Review medications and combinations"; "their medications, combinations included" narrowed it to each person’s own); no decider named.'],
}



# v18: Emulate round 4 (2026-10-03 06:25 to 06:33 UTC, emu/outputs4.json; inputs emu-in4/, v16's gated text) for the
# eleven paragraphs whose writer versions read AI (batches 4a to 4c), with the meaning put back by the smallest fixes
# (WHY18). Each paragraph keeps Emulate's own sentences where they carry the meaning, and Emulate's characters
# (straight apostrophes in g2, g5 and g6's paragraphs, as it returned them; curly where it used curly).
V[18] = dict(V[16])
V[18].update({
 'P1': "Most of the writing about communities feels outdated when it comes to psychedelics, primarily because they’ve gone from taboo toward regulated use so fast. [Licensed psilocybin service centers started opening in Oregon](%s) in 2023. Colorado created a regulated system for natural medicines and began licensing in 2025, and New Mexico enacted a [Medical Psilocybin Act](%s) also in 2025. In Australia, since 2023, [authorized psychiatrists have had limited access to psilocybin and MDMA](%s) for a specific list of conditions." % (L('Oregon’s licensed psilocybin service centers'), L('Medical Psilocybin Act'), L('authorized psychiatrists have had limited access to psilocybin and MDMA')),
 'P7': "They do also attract people who are all for revelation and hate the follow-through, people who can collect 12 ceremonies and 6 origin stories and still can't say sorry to their housemate. When you're running a community based mainly around the peak experience, you'll find out the insight doesn't do the practical work for you. Sometimes the dishes need doing and a scared kid needs comforting.",
 'P8': "My own experience shows there are real reasons for the communal use of psychedelics, too. One being that they lower the defenses that otherwise dominate every serious conversation, and the other that they can build a strong bond between a group of people going through the harder nights together. But there are negative aspects that can come from taking psychedelics, among them confusion and grandiosity. They can also bring dependency, and they can foul up the dynamics between people. The question is, are you mature enough as a community to pick through the good and the bad?",
 'P13': "Also your peers can help reality check any downloads you may have had. Psychedelics can create nonsense as well as genuine insight, and on the spot the two often feel very similar. Having a few friends that know your history can help you sort out what’s actually a new understanding from what’s just… mom showing up again.",
 'P14': "They can also help you time your ceremonies, since community creates a rhythm. A lot of traditional medicine systems rely on the community to time ceremonies rather than on individual appetite, and a shared calendar like that can help keep people out of a compulsive cycle of taking the medicine. It leaves more time for integrating, too.",
 'P18': "No special shamans here. This statement is usually contested by traditional lineages, and many ayahuasca and Bwiti communities believe the medicine should stay under trained lineage authority. I respect what these traditions have preserved, and I’ve learned from them.",
 'P20': "Even in a culture of peer medicine, there could still be an informal \"shaman\", someone everyone trusts and gradually stops questioning, even though nobody gave them the title. I don't know yet how to avoid this. Things that might help would be to have rotation of roles, and to make everyone publicly accountable for what they do. Though neither of these seem like a complete solution.",
 'P22': "This doesn't mean that peer led is ever casual. It means more competence is required, since the authority is spread around. Screening for medical or psychiatric contraindications and reviewing medications and combinations is a must. An appropriate sober sitter is required. In addition, before anybody takes anything, it will be necessary to decide what should be dealt with by seeking professional help or emergency care.",
 'P24': "The medicine stays behind the other pl/ork. It’s a secondary thing, which comes after the most basic things: reparenting and somatic capacity, and also working with your peers (the counseling thing). It can improve upon something you already have. But you can’t, by decree (and what the medicine does is essentially a decree), grant someone months of honest relationship they haven’t had.",
 'P25': "This also keeps out the experience collectors. What’s the likelihood that someone who won’t spend six months learning to listen without fixing is going to become more relationally mature because the visions were especially geometric?",
 'P26': "Another thing is that your integration is, well, your life. Ceremony opens something, and if it had any effect on you, it’ll show up in the weeks after, in your relationships and your daily behavior. In your sleep and your decisions, too. It’s also in how well you tolerate frustration without declaring a new spiritual emergency.",
})
SRC18 = dict(SRC16)
SRC18.update({'P1': 'g1-emuA (round 4)', 'P7': 'g2-emuA (round 4)', 'P8': 'g2-emuA (round 4)', 'P13': 'g3-emuA (round 4)', 'P14': 'g3-emuA (round 4)',
              'P18': 'g4-emuA (round 4)', 'P20': 'g5-emuA (round 4)', 'P22': 'g6-emuA (round 4)', 'P24': 'g7-emuA (round 4)', 'P25': 'g7-emuA (round 4)', 'P26': 'g7-emuA (round 4)'})
WHY18 = {
 'P1': ['v18: Emulate g1 A, with its heading-like first words ("Limitations of Existing Online Resources on Psychedelics") out; "writing about communities" (it had "writing online about psychedelics"); "taboo toward regulated use so fast" (it had "being regulated now in so many places"); "started opening" (published: "began opening"; it had "opened"); Colorado "created" the system and began licensing in 2025 (its "In 2025, Colorado implemented" dated the creation); "enacted" (gate v3; it had "passed"); "authorized psychiatrists have had limited access" (published; it had "psychiatrists working in certain settings have been able to access"). B had the 2025 dates in the future tense and "retail" services.'],
 'P7': ['v18: Emulate g2 A, with "revelation" and "you’re" spelled right; "They" (the medicines, P6) for its "It"; "hate the follow-through" (published: "hate"; it had "not so much for working"); "people who can collect 12 ceremonies and 6 origin stories" (published: a possibility, "collect", the counts; it had "having 12 revelutions and 6 stories of where you come from"); "their housemate" (it had "your"); "you’ll find out the insight doesn’t do the practical work for you" (published: the community discovers insight doesn’t do it; it had "these things will come up and need to be dealt with"); "based mainly around the peak experience" (it had "revelution"). B dropped the ceremonies.'],
 'P8': ['v18: Emulate g2 A, with "My own experience shows" (published: "in my experience"; it had "tends to show"); "real reasons" (published: the case is "real"; it had "some good reasons"); "the defenses that otherwise dominate every serious conversation" (it had "lower defences"); "they can build a strong bond between a group of people going through the harder nights together" (published: psychedelics create bonds when people sit through difficult nights; it had "a great way of building a strong bond … by experiencing some of the harder times"); "As you point out though" out (a chat artifact); the four harms two and two (E125; dependency unspecified, v10); "pick through the good and the bad" is Emulate’s. B opened "you make a very good point".'],
 'P13': ['v18: Emulate g3 A, with "nonsense as well as genuine insight" (it had "a lot of nonsense"); "the two" for "they"; "a new understanding" (published; it had "actually useful"); "mom showing up again" is Emulate’s for the mother joke, and "on the spot the two often feel very similar" carries the lighting quip’s point.'],
 'P14': ['v18: Emulate g3 A, with "since community creates a rhythm" (published claim); "traditional medicine systems" (it had "traditional medicines"); "rather than on individual appetite" (published); "a shared calendar like that" (published; v2 stance); "can help keep people out of a compulsive cycle" (published: "can reduce"; it had "a great help to get off of the compulsive cycle").'],
 'P18': ['v18: Emulate g4 A, with "No special shamans here." for its "There are no special shamans." (linter B13: P6 and P16 open with "There"; and "here" makes it a principle of his ceremonies, not a claim that no shaman is special anywhere); "usually" (published; it had "often"); the communities believe the medicine should stay "under trained lineage authority" (published; it had lineages that "point out" communities "revere the authority of particular lineages to be the only ones fit to dispense these medicines"); "I respect what these traditions have preserved" back; "I’ve learned from them" (published; it had "I must concede that there is much I have learned"). B invented his use of Bwiti.'],
 'P20': ['v18: Emulate g5 A, with "I agree that" out (a chat artifact); "could still be" (published: the risk; it had "would still be"); "gradually stops questioning, even though nobody gave them the title" (published; it had "isn’t questioned"); "I don’t know yet how to avoid this" (published: "I don’t yet know how"; it had "if it would be possible"). B added "or needs to be avoided".'],
 'P22': ['v18: Emulate g6 A, with "ever" (published: "never means casual"); "since the authority is spread around" (published: distributed authority raises the requirement; it had "to lead the group"); "before anybody takes anything" back; "professional help or emergency care" (published; it had "professional medical or psychiatric help or going to the emergency room"). B strung four requirements through one sentence.'],
 'P24': ['v18: Emulate g7 A, with "The medicine stays behind the other pl/ork." (published; it had "The reason is that medicine is a secondary thing"); "reparenting and somatic capacity, and also working with your peers (the counseling thing)" (three practices, not "reparenting/somatic capacity"); "It can improve upon" (published: "can deepen"; it had "is meant to"); "honest relationship" (published; it had "real"). "By decree (and what the medicine does is essentially a decree)" is Emulate’s, for "pharmacological decree".'],
 'P25': ['v18: Emulate g7 A, with "keeps out the experience collectors" (published: "filters out"; it had "prevents … from getting into the way"); "spend six months learning to listen without fixing" and "become more relationally mature because the visions were especially geometric" back (published; it had "this kind of relationship work" and "magically do it after having some visions"). The question is Emulate’s, for "unlikely".'],
 'P26': ['v18: Emulate g7 A, with "Ceremony opens something" and "in the weeks after" back (published); "if it had any effect on you, it’ll show up" (published: the weeks reveal whether anything changed); "daily behavior", "sleep" and "decisions" back, two and two; "without declaring a new spiritual emergency" back; "It’s also in how well you tolerate frustration" (it had two "You can look").'],
}



# v19: what the v18 gate found (TRACE-v18-A and B, STANCE-v18, SENSE-v18, GROUNDING-v18), fixed in Emulate's
# sentences; P13 takes the lighting quip from round 5 (emu/outputs5.json, g3-emuB: "with the same bright shining light").
V[19] = dict(V[18])
fix(V[19], 'P1', "Most of the writing about communities feels outdated when it comes to psychedelics, primarily because they’ve gone", "Most of the writing about communities is outdated when it comes to psychedelics, because they’ve gone")
fix(V[19], 'P7', "When you're running a community based mainly around the peak experience, you'll find out the insight doesn't do the practical work for you.", "Any community based mainly around the peak experience is going to find out sooner or later that the insight doesn't do the practical work for it.")
fix(V[19], 'P8', "My own experience shows there are real reasons for the communal use of psychedelics, too. One being that they lower the defenses that otherwise dominate every serious conversation, and the other that they can build", "In my own experience there are real reasons for the communal use of psychedelics, too. One being that they can lower the defenses that otherwise dominate every serious conversation, and another that they can build")
V[19]['P13'] = "Also your peers can reality check any downloads you may have had. Psychedelics can give you genuine insight, and they can also give you convincing nonsense with the same bright shining light. A few friends that know your history may notice which parts look like a new understanding and which look like… mom."
V[19]['P14'] = "Community also creates a rhythm. A lot of traditional medicine systems rely on the community to time ceremonies rather than on individual appetite, and a shared calendar like that can help cut down on compulsive repetition. It can leave more time for integrating, too."
fix(V[19], 'P18', "This statement is usually contested by traditional lineages, and many", "Traditional lineages usually disagree with me on this, and many")
fix(V[19], 'P20', "Things that might help would be to have rotation of roles, and to make everyone publicly accountable for what they do.", "Things that might help would be to have rotation of roles, and public accountability.")
fix(V[19], 'P22', "This doesn't mean that peer led is ever casual.", "This doesn't mean that peer-led ceremonies are ever casual.")
V[19]['P24'] = "The medicine stays behind the other pl/ork. It’s a secondary thing, which comes after reparenting and somatic capacity, and after peer counseling too. It can deepen a practice you already have. But no pharmacological decree is going to give someone months of honest relationship they haven’t had."
V[19]['P25'] = "This also keeps out the experience collectors. Someone who won’t spend six months learning to listen without fixing probably isn’t going to become more relationally mature because the visions were especially geometric."
SRC19 = dict(SRC18)
SRC19['P13'] = 'g3-emuA (round 4), with round 5 g3-emuB’s "with the same bright shining light"'
WHY19 = {
 'P1': ['v19 (TRACE-v18-A): "is outdated … because" (published: a flat claim about the literature; "feels outdated, primarily because" made it an impression with other causes).'],
 'P7': ['v19 (TRACE-v18-A): "Any community … is going to find out sooner or later" (published: "Any community … will eventually discover"; "When you’re running a community, you’ll find out" made an organizer the one who learns).'],
 'P8': ['v19 (TRACE-v18-A, STANCE-v18, GROUNDING-v18): "In my own experience" (published: a limit, not proof); "they can lower" (published: "can loosen"); "another" for "the other" (two of the reasons, not the only two).'],
 'P13': ['v19 (TRACE-v18-A, STANCE-v18, GROUNDING-v18): peers "reality check" (published; "help" left the sorting to the reader); "convincing nonsense … with the same bright shining light" (published: "with identical lighting"; round 5’s words; "on the spot … often feel very similar" made them alike only sometimes and only in the moment); friends "may notice which parts look like a new understanding and which look like… mom" (published: friends notice a likeness; "help you sort out what’s actually … from what’s just… mom showing up again" made it identification).'],
 'P14': ['v19 (TRACE-v18-A): "Community also creates a rhythm" (published; "They can also help you time your ceremonies" made it the friends’ job); "can help cut down on compulsive repetition" (published: "can reduce"; "keep people out of" was prevention); "It can leave more time" (published: "can give integration time").'],
 'P18': ['v19 (TRACE-v18-A): "Traditional lineages usually disagree with me on this" (published: they disagree with him; "This statement is usually contested" took him out of it).'],
 'P20': ['v19 (TRACE-v18-B, STANCE-v18): "public accountability" (published; "make everyone publicly accountable for what they do" made it a rule for every member, where the essay aims it at whoever gathers power and warns that group scrutiny slides into surveillance).'],
 'P22': ['v19 (SENSE-v18): "peer-led ceremonies" ("peer led" stood as a noun with nothing to describe).'],
 'P24': ['v19 (TRACE-v18-B, STANCE-v18, SENSE-v18): "after reparenting and somatic capacity, and after peer counseling too" (published: three named practices; "the most basic things" and "working with your peers (the counseling thing)" changed them); "It can deepen a practice you already have" (published; "improve upon something you already have" widened it); "no pharmacological decree is going to give someone months of honest relationship" (published: medicine can’t create it "by pharmacological decree"; Emulate’s "(and what the medicine does is essentially a decree)" said everything medicine does is a decree, and "you can’t … grant someone" put a person in the medicine’s place).'],
 'P25': ['v19 (TRACE-v18-B): "probably isn’t going to" (published: "is unlikely to"; "What’s the likelihood …?" read as a firmer dismissal).'],
}



# v20: v19 with the last two findings of its gate (TRACE-v19-A), in the trace's own terms; STANCE-v19 found only Joel's
# own "25" and his P33 step (information for him), SENSE-v19 nothing new, TRACE-v19-B nothing.
V[20] = dict(V[19])
fix(V[20], 'P1', "Most of the writing about communities is outdated when it comes to psychedelics, because they’ve gone from taboo toward regulated use so fast.", "Most of the writing about communities hasn’t caught up on psychedelics, which have gone from taboo toward regulated use really fast.")
fix(V[20], 'P14', "A lot of traditional medicine systems rely on the community to time ceremonies rather than on individual appetite,", "A lot of traditional medicine systems hold ceremonies on communal timing rather than individual appetite,")
SRC20 = dict(SRC19)
WHY20 = {
 'P1': ['v20 (TRACE-v19-A): "hasn’t caught up on psychedelics" (published: most community literature hasn’t acknowledged the pace; "is outdated" was broader and harsher), with no added cause.'],
 'P14': ['v20 (TRACE-v19-A): "hold ceremonies on communal timing" (published: the systems "place ceremonies inside communal timing"; "rely on the community to time ceremonies" made the community the scheduler).'],
}



# v21 and v22: after API batch 5 (07:05 UTC) P1, P7, P8, P13, P20, P22 and P26 pass alone; four short paragraphs still
# read AI with every neighbor that passes alone (P14, P18, P24, P25). Following the gate's E104 ("what would the
# narrator say aloud here"), mine in Joel's spoken register, two each: v21 the first, v22 the second.
V[21] = dict(V[20])
V[21].update({
 'P14': "Community gives the whole thing a rhythm, too. In a lot of traditional medicine systems, ceremonies happen on the group’s schedule, not whenever somebody’s in the mood. A shared calendar like that can cut down on people taking medicine over and over out of compulsion, and it can leave time for integration to actually happen.",
 'P18': "First one: no special shamans. I know, traditional lineages mostly disagree with me on that. A lot of ayahuasca and Bwiti communities believe the medicine should stay with people trained in the lineage, under their authority. And I respect what those traditions have kept alive. I’ve learned from them.",
 'P24': "The medicine stays behind the other pl/ork. Reparenting and somatic capacity come first, and so does peer counseling. Medicine can deepen a practice you’ve already got going. But it can’t hand you months of honest relationship by pharmacological decree.",
 'P25': "Bonus: this prerequisite filters out the experience collectors. If someone won’t put in six months learning to listen without fixing, I doubt they’ll come out more relationally mature just because the visions were especially geometric.",
})
SRC21 = dict(SRC20); SRC21.update({k: 'new (mine), after Emulate and writers read AI' for k in ('P14', 'P18', 'P24', 'P25')})
WHY21 = {
 'P14': ['v21: mine. v11, v14, v16 and v20 read AI (with P13 and with P15, which pass alone). The published claims in spoken order: community gives the medicine work a rhythm; traditional systems hold ceremonies on the group’s schedule, not individual appetite ("whenever somebody’s in the mood"); a shared calendar can cut down on compulsive repetition and leaves time for integration. The community schedules nothing for anyone (v2 stance).'],
 'P18': ['v21: mine. Six versions read AI (alone and with its heading and P19). "First one:" opens the list the heading promises; "mostly disagree" (published: "usually"); "stay with people trained in the lineage, under their authority" (published: "under trained lineage authority"); "kept alive" (published: "preserved").'],
 'P24': ['v21: mine. v14, v16 and v20 read AI. The published units, with "you’ve already got going" (published: "a practice that exists") and "hand you" (published: "create").'],
 'P25': ['v21: mine. v14, v16 and v20 read AI. "Bonus:" for "also"; "I doubt" (published: "is unlikely"; his own assessment); the geometric visions kept.'],
}
V[22] = dict(V[20])
V[22].update({
 'P14': "And there’s a rhythm to it when you do it as a community. A lot of traditional medicine systems run ceremonies on communal time, not on individual appetite. Having a shared calendar can cut down on compulsive repetition, and it can give integration time to happen.",
 'P18': "First principle: no special shamans. Traditional lineages usually disagree with me on this one. Lots of ayahuasca and Bwiti communities believe the medicine should stay under the authority of people trained in the lineage. I respect what those traditions have preserved, though, and I’ve learned from them.",
 'P24': "The medicine stays behind the other pl/ork, and that’s on purpose. Reparenting and somatic capacity come first, and peer counseling does too. If there’s already a practice going, medicine can deepen it. No pharmacological decree is going to create months of honest relationship, though.",
 'P25': "Plus, the prerequisite weeds out the experience collectors. Somebody who won’t spend six months learning to listen without fixing isn’t likely to get more relationally mature because the visions were especially geometric.",
})
SRC22 = dict(SRC20); SRC22.update({k: 'new (mine), alternate' for k in ('P14', 'P18', 'P24', 'P25')})
WHY22 = {k: ['v22 (alternate to v21): mine.'] for k in ('P14', 'P18', 'P24', 'P25')}
WHY21['P14'].append('v21 (TRACE-v21-A, SENSE-v21): "it can leave time" (published: "can … give integration time"); "taking medicine" ("taking it" had no noun to point to).')
WHY22['P14'].append('v22 (TRACE-v22-A): "compulsive repetition" (published; "repeat-dosing" narrowed it to doses); "it can give integration time to happen" (published).')
WHY22['P18'].append('v22 (TRACE-v22-A): "First principle:" ("My first principle" could read as his top one).')



# v23: Emulate round 6 (emu/outputs6.json). Its versions were checked raw first (EMULATE-FALLBACK section 4 step 1;
# batch 6b: ten of eleven Human), and the passing version closest in meaning gets only word-level fixes. P18 has no
# usable round-6 version (WHY23), so it stays v20's and goes to Joel.
V[23] = dict(V[20])
V[23].update({
 'P14': "A community can help ground your ceremonies in a schedule. Many traditional medicine systems only hold ceremonies at specific times for the whole group. This schedule can help you avoid compulsive overuse and give you time to integrate.",
 'P24': "The use of this medicine is secondary to all of the other pl/ork you should be doing first: reparenting and somatic capacity. And peer counseling. The medicine can enhance that. It will not replace months of honest relationship with any kind of pharmacological short cut.",
 'P25': "Another benefit of this pre-req – it weeds out those who only want to collect experiences. If they are unwilling to make a 6 month commitment to learning to listen without fixing, it is unlikely they will come out of a ceremony more relationally mature, regardless of how mindblowing the geometric shapes they saw were.",
})
SRC23 = dict(SRC20); SRC23.update({'P14': 'h1-emuB (round 6)', 'P24': 'h5-emuA (round 6)', 'P25': 'h5-emuB (round 6)'})
WHY23 = {
 'P14': ['v23: Emulate h1 B (raw: 100% Human, 41 words), with "It sounds cheesy but" out (an aside the published doesn’t have; kept as a proposal for Joel); "medicine systems" (published; it had "medicines"); "only hold ceremonies" (it had "only allow": the traditions don’t permit, they time; v2 stance). "Ground your ceremonies in a schedule" carries "Community creates rhythm"; "at specific times for the whole group" carries "communal timing rather than individual appetite".'],
 'P24': ['v23: Emulate h5 A (raw: 100% Human, 52 words), with "you should be doing first: reparenting and somatic capacity. And peer counseling." (published: the three come first, a closed list, split two and one as Joel split lists of three (E125); it had "to increase your capacity for reparenting, somatic capacity, and peer counseling, etc."); "can enhance" (published: "can deepen"; it had "will"); "months of honest relationship" (published; it had "those other kinds of relationships"). "Pharmacological short cut" is Emulate’s for "pharmacological decree".'],
 'P25': ['v23: Emulate h5 B (raw: 100% Human, 62 words), with "Another benefit of this pre-req –" (linter B13: P6 and P16 open with "There"; it had "There is another benefit to this pre-req –"); "learning to listen without fixing" (published; it had "learning how to counsel their peers"); "more relationally mature" (published; it had "having gained a lot of relational maturity"). "Regardless of how mindblowing the geometric shapes they saw were" is Emulate’s for "because the visions were especially geometric".'],
 'P18': ['v23: no round-6 version is usable: "there is no such thing as a shaman" (reverses him), "Mine was the first one I did" (invented), two stop mid-sentence, and one has "That is fine." (a banned standalone). v20’s stays; it has read AI seven times, alone and with its heading and P19, so it goes to Joel.'],
}



# v24: what the v23 gate found (TRACE-v23-A, STANCE-v23, SENSE-v23), at word level in Emulate's sentences.
V[24] = dict(V[23])
V[24].update({
 'P14': "A community grounds your ceremonies in a schedule. Many traditional medicine systems hold their ceremonies on communal timing, not individual appetite. This schedule can help cut down on compulsive repetition and give you time to integrate.",
 'P24': "The use of medicine is secondary to all of the other pl/ork that comes first: reparenting and somatic capacity. And peer counseling. The medicine can enhance that work once it's there. But no pharmacological short cut will create months of honest relationship.",
 'P25': "As a bonus, this pre-req weeds out the experience collectors. If someone is unwilling to make a 6 month commitment to learning to listen without fixing, it is unlikely they will come out of a ceremony more relationally mature, regardless of how mindblowing the geometric shapes they saw were.",
})
SRC24 = dict(SRC23)
WHY24 = {
 'P14': ['v24 (TRACE-v23-A, STANCE-v23): "grounds" (published: "creates"; "can help ground" hedged it); "hold their ceremonies on communal timing, not individual appetite" (published; "only … at specific times for the whole group" claimed fixed times only); "can help cut down on compulsive repetition" (published: "can reduce compulsive repetition"; "avoid compulsive overuse" was another concern).'],
 'P24': ['v24 (TRACE-v23-A, SENSE-v23): "The use of medicine" (in general; "this medicine" read as bufo, after P23); "that comes first" (the published rule; "you should be doing first" made it an instruction to the reader); "can enhance that work once it’s there" (published: "a practice that exists"); "no pharmacological short cut will create months of honest relationship" (published: medicine "cannot create" it; "It will not replace … with any kind of pharmacological short cut" tangled the medicine with the shortcut).'],
 'P25': ['v24 (TRACE-v23-A, SENSE-v23): "the experience collectors" and "If someone is unwilling" (published; "those who only want to collect experiences" and "they" narrowed both); "As a bonus" (Emulate h6 A’s words; "Another benefit" sent the reader looking for a first one).'],
}



# v25: the last word-level findings of TRACE-v24-A, made in the trace's terms (STANCE-v24 found only Joel's "25").
V[25] = dict(V[24])
fix(V[25], 'P14', "This schedule can help cut down on compulsive repetition", "This schedule can cut down on compulsive repetition")
fix(V[25], 'P24', "The medicine can enhance that work once it's there. But no pharmacological short cut will create months of honest relationship.", "The medicine can deepen a practice once it's there. But medicine can't be a pharmacological short cut to months of honest relationship.")
fix(V[25], 'P25', "If someone is unwilling to make a 6 month commitment to learning to listen without fixing,", "If someone is unwilling to put in 6 months learning to listen without fixing,")
SRC25 = dict(SRC24)
WHY25 = {
 'P14': ['v25 (TRACE-v24-A): "can cut down on" (published: "can reduce"; "can help cut down on" was weaker).'],
 'P24': ['v25 (TRACE-v24-A): "can deepen a practice once it’s there" (published: "can deepen a practice that exists"); "medicine can’t be a pharmacological short cut to months of honest relationship" (published: medicine "cannot create" it "by pharmacological decree"; "no pharmacological short cut will create" moved the limit off medicine and made it a prediction).'],
 'P25': ['v25 (TRACE-v24-A): "put in 6 months learning" (published: "spend six months learning"; "make a 6 month commitment" made it a pledge).'],
}



# v26: P14 from Emulate round 6's h2 B (raw: 100% Human, 41 words; the closest in meaning of the four raw P14s that
# passed), with two word-level fixes. v25's P14 (h1 B with the gate's fixes) read AI alone and with both neighbors.
V[26] = dict(V[25])
V[26]['P14'] = "One of the benefits of community is rhythm, and many traditional medicinal practices occur within ceremonies that have a schedule. The schedule of ceremonies, rather than people doing ceremonies when they want, can serve to limit compulsive use and provide for integration time."
SRC26 = dict(SRC25); SRC26['P14'] = 'h2-emuB (round 6)'
WHY26 = {'P14': ['v26: Emulate h2 B, with "is rhythm, and" for its "is that" (published: "Community creates rhythm"; it made the benefit of community that traditional practices are scheduled) and "can serve" for "serves" (published: "can reduce"). "Rather than people doing ceremonies when they want" carries "rather than individual appetite"; "limit compulsive use" carries "reduce compulsive repetition"; "provide for integration time", "give integration time".']}



# v27: TRACE-v26-A's finding on P14, in its own terms (STANCE-v26: only Joel's "25" and his P33 step).
V[27] = dict(V[26])
fix(V[27], 'P14', "occur within ceremonies that have a schedule. The schedule of ceremonies, rather than people doing ceremonies when they want,", "occur within ceremonies that have a communal schedule. The shared schedule of ceremonies, rather than each person doing ceremonies when they want,")
SRC27 = dict(SRC26)
WHY27 = {'P14': ['v27 (TRACE-v26-A): "a communal schedule", "The shared schedule", "each person" (published: "communal timing rather than individual appetite", "a shared calendar"; "a schedule" and "people doing ceremonies when they want" made it scheduled against on-demand).']}



# v28: Joel's message of 2026-10-03 20:51 UTC.
# - P10: "add that sentence to the end of it so it will lead correctly into P11" (the sentence proposed at 08:04).
# - P19: "P19 is a hard fail. Why didn't you see it flipped the logic from the original? OR is not ALSO." I wrote
#   "They may also be…" in v1; TRACE-v2-C marked "may be wise, or… → may also be" SAME-MEANING and I took it.
# - P23: his sentence for "My reasons are in those articles, not smuggled into one sentence here." ("ai is always
#   saying something like 'not smuggle in' … And it always wants to add a 'not Y' part").
# - P28: his parenthetical for "private", and "insured" out ("as if someone is insuring a ceremony, no").
# - P22: "medical and psychiatric" (published) for Emulate's "medical or psychiatric", from my own logic pass.
V[28] = dict(V[27])
fix(V[28], 'P10', "which then attracted exactly the right people to show me my limits. 😂", "which then attracted exactly the right people to show me my limits. 😂 In a community of people who’ve sat through the same nights, you aren’t the only one who’s been there, and someone can catch the God complex early.")
fix(V[28], 'P19', "The facilitator on the retreat circuit may be wise. They may also be someone who", "The facilitator on the retreat circuit may be wise. Or they may be someone who")
fix(V[28], 'P23', "My reasons are in those articles, not smuggled into one sentence here.", "My reasons are given in those articles, respectively, since they need more space.")
fix(V[28], 'P28', "It should write down which activities are private and what’s actually insured.", "It should write down which activities are private (to the individual, to a group in the community, or to the community vs the outside).")
fix(V[28], 'P22', "Screening for medical or psychiatric contraindications", "Screening for medical and psychiatric contraindications")
SRC28 = dict(SRC27)
WHY28 = {
 'P10': ['v28 (Joel, 20:51: "it was explained by P9, but yeah add that sentence to the end of it so it will lead correctly into P11"): the sentence proposed at 08:04, with "the God complex" for "the inflation" (the term in his sentence before) and "sat through" for "sat".'],
 'P19': ['v28 (Joel, 20:51: "P19 is a hard fail … OR is not ALSO"): "Or they may be someone who…" (published: "may be wise, or may be unvetted, …": one of these, which is why "not to know which one you’re getting" follows). I wrote "They may also be" in v1, which says the same facilitator may be wise and a predator at once; TRACE-v2-C marked the change SAME-MEANING and I accepted it without reading the logic myself.'],
 'P23': ['v28 (Joel, 20:51): his sentence, "My reasons are given in those articles, respectively, since they need more space.", for "My reasons are in those articles, not smuggled into one sentence here." ("ai is always saying something like \'not smuggle in\' … And it always wants to add a \'not Y\' part").'],
 'P28': ['v28 (Joel, 20:51): his parenthetical, "private (to the individual, to a group in the community, or to the community vs the outside)"; "and what’s actually insured" out ("that\'s actually the more weird part. as if someone is insuring a ceremony, no").'],
 'P22': ['v28 (my logic pass after Joel’s P19 ruling): "medical and psychiatric contraindications" (published: "Screen for medical and psychiatric contraindications"; Emulate’s "medical or psychiatric" could read as one kind or the other).'],
}


V[29] = dict(V[28])
fix(V[29], 'P18', "Traditional lineages usually disagree with me on this, and many ayahuasca and Bwiti communities believe the medicine should stay under trained lineage authority. I respect what these traditions have preserved, and I’ve learned from them.", "Traditional lineages usually disagree with me on this, though I’ve learned from them and respect what they’ve preserved. Many ayahuasca and Bwiti communities believe the medicine should stay under trained lineage authority.")
SRC29 = dict(SRC28)
WHY29 = {
 'P18': ['v29 (batch 9: the respect sentence alone trips Pangram; out, the heading, P18 and P19 read Human; in without the concession, AI): the respect and the debt moved up into the concession ("though I’ve learned from them and respect what they’ve preserved"; published: "I respect what those traditions have preserved and have learned from them"), so the paragraph no longer closes on a courtesy right before P19’s "My issue is with…". Same units; only their place and a "though" for the contrast the published leaves to juxtaposition. Joel asked what the stumbling block is: the sentence names a respect and a debt and fills in neither (what they preserved, what he learned), and that is his to say.'],
}

V[30] = dict(V[28])
fix(V[30], 'P18', "and many ayahuasca and Bwiti communities believe the medicine should stay under trained lineage authority. I respect what these traditions have preserved, and I’ve learned from them.", "and many ayahuasca and Bwiti communities believe the medicine should stay under trained lineage authority. I’ve learned from those traditions, though, and I respect what they’ve preserved.")
fix(V[30], 'P3', "To be sure, the legality of psychedelics varies", "All of which means the legality of psychedelics varies")
fix(V[30], 'P3', "And it can depend on a group’s religious status", "And it depends on a group’s religious status")
fix(V[30], 'P4', "parents worried about the children, or neighbors imagining chaos, or insurance disappearing, or a local official", "parents worried about the children, and neighbors imagining chaos, and insurance disappearing, and a local official")
fix(V[30], 'P17', "Is your community humble enough to say no, or pause?", "Is your community humble enough to say no? To pause?")
fix(V[30], 'P22', "it will be necessary to decide what should be dealt with by seeking professional help or emergency care.", "it will be necessary to decide what needs professional help or emergency care.")
fix(V[30], 'P24', "The medicine can deepen a practice once it's there.", "The medicine can deepen a practice that's already there.")
fix(V[30], 'P26', "in your relationships and your daily behavior. In your sleep and your decisions, too. It’s also in how well you tolerate frustration", "in your relationships or your daily behavior, in your sleep or your decisions. Or in how well you tolerate frustration")
fix(V[30], 'P28', "“I don’t think anybody here has ever heard of that”", "“I don’t think anybody around here has ever heard of that”")
SRC30 = dict(SRC28)
WHY30 = {
 'P18': ['v30 (TRACE-v29-A): v29 had moved the respect up into the concession; that widened whom Joel says he learned from ("them": traditional lineages in general, where the published "those traditions" follows the ayahuasca and Bwiti sentence) and left the paragraph ending on lineage authority, right before P19’s "My issue is with…", which reads as his verdict on those lineages. Back at the end, reworded and traced clean: "I’ve learned from those traditions, though, and I respect what they’ve preserved."'],
 'P3': ['v30 (LOGIC-v29 A and B): "All of which means" (published: "Communities therefore face…", a consequence of P1 and P2; Emulate’s "To be sure" reads as a concession); "it depends on" (published: real differences by all five; "it can depend" made the last two only sometimes).'],
 'P4': ['v30 (LOGIC-v29 A and B): "and … and … and" (published: "parents may worry …, neighbors may imagine chaos, insurers may disappear, and a local official may understand none": each may happen, several at once; Emulate’s "or" made them alternatives). Same shape, the connective back.'],
 'P17': ['v30 (LOGIC-v29 A and B, and my own pass): "humble enough to say no? To pause?" (published: "humility to say no, pause, refer out, and admit": all of them; "say no, or pause" let one stand in for the other).'],
 'P22': ['v30 (TRACE-v29-A): "decide what needs professional help or emergency care" (published: "what requires"; Emulate’s "what should be dealt with by seeking" weakened the necessity).'],
 'P24': ['v30 (LOGIC-v29 B): "a practice that’s already there" (published: "a practice that exists"; "once it’s there" could read as the medicine being there).'],
 'P26': ['v30 (LOGIC-v29 A): "in your relationships or your daily behavior, in your sleep or your decisions. Or in how well…" (published: the weeks reveal whether anything changed in any of these; "and … too … It’s also in" said every effect shows up in all five).'],
 'P28': ['v30 (TRACE-v29-A): "anybody around here" (published: "Nobody around here", the locality; "here" could mean the group).'],
}

V[31] = dict(V[30])
fix(V[31], 'P26', "it’ll show up in the weeks after, in your relationships or your daily behavior, in your sleep or your decisions. Or in how well", "it’ll show up in the weeks after, maybe in your relationships and your daily behavior. Maybe in your sleep and your decisions. Or in how well")
SRC31 = dict(SRC30)
WHY31 = {
 'P26': ['v31 (batch 10: v30’s "or … or … Or in" read 100% AI, where v20’s "and … too … It’s also in" had passed; the fix had changed the shape as well as the logic): v20’s three parts and sentence breaks back, with the logic carried by "maybe … Maybe … Or in" (published: the weeks reveal "whether anything changed" in these places, so one is enough).'],
}

V[32] = dict(V[31])
fix(V[32], 'P26', "Ceremony opens something, and if it had any effect on you, it’ll show up in the weeks after, maybe in your relationships and your daily behavior. Maybe in your sleep and your decisions. Or in how well", "Ceremony opens something, and the weeks after will tell you whether it had any effect on you, in your relationships and your daily behavior. In your sleep and your decisions, too. And in how well")
SRC32 = dict(SRC31)
WHY32 = {
 'P26': ['v32 (batch 11: "maybe … Maybe … Or in" and "or … maybe … Or in" both read AI; v20’s "and … too" passed): the published test back ("The following weeks reveal whether anything changed — in relationships, …": "the weeks after will tell you whether it had any effect on you, in …"), where the "and … too" list the places to look, as the published "and" does, so v20’s words can stay.'],
}

V[33] = dict(V[32])
fix(V[33], 'P26', "Ceremony opens something, and the weeks after will tell you whether it had any effect on you, in your relationships and your daily behavior. In your sleep and your decisions, too. And in how well", "Ceremony opens something, and if it had any effect on you, the weeks after will show it. Look at your relationships and your daily behavior. At your sleep and your decisions, too. And at how well")
SRC33 = dict(SRC32)
WHY33 = {
 'P26': ['v33 (TRACE-v32-A: "In your sleep and your decisions, too. And in how well…" sit outside "whether", so they still add places where it shows): v20’s conditional with the published "reveal" ("the weeks after will show it"), then the five as places to look ("Look at … At …, too. And at …"), so the "and … too" add places to look, not places it is.'],
}

V[34] = dict(V[33])
fix(V[34], 'P26', V[33]['P26'], "Another aspect is integration: your life. Ceremony opens something. Did anything change? Look at your life over the last few weeks. Look at your relationships, how you behave, how you sleep, how you make decisions, how you handle frustration without declaring a new spiritual emergency.")
SRC34 = dict(SRC33)
SRC34.update({'P26': 'i1-emuA (round 7)'})
WHY34 = {
 'P26': ['v34 (batch 12: v33 read AI; Emulate round 7 on v33, both raw versions Human): i1 A, with "Another" for its "The other" (one principle of several); the published "Ceremony opens something." and "Did anything change?" for its "Did the ceremony open you up to anything?", which merged the opening with the change (published: "Ceremony opens something. The following weeks reveal whether anything changed"); the published "without declaring a new spiritual emergency" back for its "etc, etc.", which also opened the published list of five. The five are places to look ("Look at …"), so a change in one is enough, as published.'],
}

V[35] = dict(V[34])
fix(V[35], 'P26', "Another aspect is integration: your life.", "Another aspect is integration: your everyday life.")
fix(V[35], 'P26', "Look at your life over the last few weeks.", "Look at your life in the weeks after.")
SRC35 = dict(SRC34)
WHY35 = {
 'P26': ['v35 (TRACE-v34-A): "your everyday life" (published: "Integration is ordinary life", everyday life as against ceremony; "your life" alone could read as your whole life); "in the weeks after" (published: "The following weeks", after the ceremony; "the last few weeks" counted back from the reading and capped the span).'],
}

V[36] = dict(V[35])
fix(V[36], 'P26', "how you handle frustration without declaring", "how well you handle frustration without declaring")
SRC36 = dict(SRC35)
WHY36 = {
 'P26': ['v36 (TRACE-v35-A, in its own terms): "how well you handle frustration" (published: "the person’s ability to tolerate frustration", a capacity; "how you handle" read as a manner, or as if you already get through it). TRACE-v35-A: the five read as places to look, one or more, as published; "the weeks after" keeps the published time. Kept, with reasons: the "you" voice, which the section uses throughout (v20’s P26 too); "Another aspect", which the heading places among the ceremony principles.'],
}

V[37] = dict(V[36])
fix(V[37], 'P26', "Another aspect is integration: your everyday life.", "The other aspect is integration: your life.")
SRC37 = dict(SRC36)
WHY37 = {
 'P26': ['v37 (batch 15, ablation): v36 read AI, and undoing any one of three fix groups made it Human; Emulate’s own first sentence back ("The other aspect is integration: your life."), the fix that carried the least meaning. Kept: the published opening apart from the change ("Ceremony opens something. Did anything change?"), the published quip, the closed list of five, "in the weeks after".'],
}

V[38] = dict(V[37])
fix(V[38], 'P18', "I’ve learned from those traditions, though, and I respect what they’ve preserved.", "I've learned what to do, and what not to do, from watching those traditions, though. A lot of people need the rituals, and the look and vibe to match, before they feel comfortable doing this kind of thing, even if I don't do them myself. The spirit realms are quite a mixed bag: you can have a shaman who heals people very well, and yet he also may take money to send evil spirits to kill someone. And people do very often decide they're ready to do ceremonies long before they're really trained and prepared. I'm sure I could still learn a lot from them, and they could still learn a lot from me.")
fix(V[38], 'P33', "they’re building a genuine alternative, not just escaping society.", "they’re building a genuine alternative.")
fix(V[38], 'P26', "The other aspect is integration: your life.", "Another aspect is integration: your life.")
SRC38 = dict(SRC37)
SRC38.update({'P18': 'g4-emuA (round 4) with Joel’s 01:18 answer'})
WHY38 = {
 'P18': ['v38 (Joel, 2026-10-04 01:18, asked what he learned from those lineages): the empty courtesy ("I’ve learned from those traditions, though, and I respect what they’ve preserved"; published: "I respect what those traditions have preserved and have learned from them") becomes his specifics, his words wherever they read in place, with his straight apostrophes: "I\'ve learned what to do, and what not to do, from watching those traditions" (his "i\'ve learned what to do, and what not to do, based on observing the various traditions"); the rituals and "the look and vibe to match" people need "before they feel comfortable doing this kind of thing", "even if I don\'t do them myself"; "the spirit realms are quite a mixed bag: you can have a shaman who heals people very well, and yet he also may take money to send evil spirits to kill someone"; "people do very often decide they\'re ready to do ceremonies long before they\'re really trained and prepared"; "I\'m sure I could still learn a lot from them, and they could still learn a lot from me."'],
 'P33': ['v38 (Joel, 01:18: "sure cut it"): ", not just escaping society" out, the "not Y" tail he named on 20:51; the next sentence answers the escape-pod objection.'],
 'P26': ['v38 (linter B13: v37 gave the section three paragraphs opening "The": P10, P24, P26): "Another aspect" (v36’s word, without its "everyday"; batch 15 left open which of the two tipped v36).'],
}

V[39] = dict(V[38])
fix(V[39], 'P18', V[38]['P18'], "No special shamans here. Traditional lineages usually disagree with me on this, and many ayahuasca and Bwiti communities believe the medicine should stay under trained lineage authority. I respect what those traditions have preserved, and I've learned what to do, and what not to do, from watching them. I see a lot of people need the rituals, and the look and vibe to match, before they feel comfortable doing this kind of thing, even if I don't do them myself. I've learned that the spirit realms are quite a mixed bag: you can have a shaman who heals people very well, and yet he also may take money to send evil spirits to kill someone. And that people do very often decide they're ready to do ceremonies long before they're really trained and prepared. I'm sure I could still learn a lot from those traditions, and they could still learn a lot from me.")
SRC39 = dict(SRC38)
WHY39 = {
 'P18': ['v39 (TRACE-v38-A, STANCE-v38, the v38 cold read): the published respect back ("I respect what those traditions have preserved"; v38 had dropped it, and his answer adds to it rather than replacing it), now with something it attaches to; his own framing kept on each lesson ("I see a lot of people need the rituals…", "I\'ve learned that the spirit realms are quite a mixed bag…", "And that people do very often decide…"), so the spirit realms and the readiness read as what he learned, not as claims from nowhere (cold read [63], [64]); "from those traditions" for "from them" in the last sentence ("them" read as the untrained people). Kept as he wrote it: "do ceremonies" (lead them or take part; asked).'],
}

V[40] = dict(V[39])
fix(V[40], 'P18', "I see a lot of people need the rituals, and the look and vibe to match,", "I see a lot of people need sacred rituals, and the look and vibe to match,")
fix(V[40], 'P18', "I've learned that the spirit realms are quite a mixed bag:", "I've also seen that the spirit realms are quite a mixed bag:")
fix(V[40], 'P18', "And that people do very often decide", "And people do very often decide")
SRC40 = dict(SRC39)
WHY40 = {
 'P18': ['v40 (TRACE-v39-A, the v39 cold read, in their terms): "sacred rituals" (his "sacred ritual practices"; "the rituals" had no antecedent); "I\'ve also seen that the spirit realms…" (his "based on observing"; three "I\'ve learned" in a row); "And people do very often decide…" as a sentence of its own (the cold read had to reread the "And that…" fragment). Kept as his: "what not to do", "from watching" (his "observing"), the shaman who heals and also may take money to send evil spirits to kill someone, the two-way learning at the end; "do ceremonies" (asked).'],
}

V[41] = dict(V[40])
fix(V[41], 'P26', "Another aspect is integration: your life.", "The other aspect is integration: your life.")
SRC41 = dict(SRC40)
WHY41 = {
 'P26': ['v41 (batch 17: "Another aspect" read AI): v37’s "The other aspect" back (it passes alone); the third "The" opener (B13, with P10 and P24) goes in the section pass, where P24 is in an AI window.'],
}

V[42] = dict(V[41])
V[42]['P22'] = 'This is not to say that peer led ceremonies are ever casual. In fact, since the authority is spread around, there needs to be more competence, and some things are a must: screening for contra-indications (both medical and psychiatric), reviewing medications (including medication combinations), having the right kind of sober sitter present, and knowing in advance what kind of situations would require professional help or going to the ER.'
V[42]['P23'] = 'Also, I am especially cautious about some medicines and protocols that I see as more destabilizing and/or presenting more of a medical burden. This includes some uses of [ketamine and MDMA](http://mdmaket.u-dont-exist.com/) and [bufo](http://bufo.u-dont-exist.com/). My reasons are given in those articles, respectively, since they need more space.'
V[42]['P24'] = "Using medicine is secondary to all of the other pl/ork that I list above: reparenting, developing somatic capacity, and learning to do peer counseling. The medicine can deepen an existing practice, but it can't be a pharmacological short cut to what takes several months of real relationship with other people."
V[42]['P25'] = 'This pre-requisite also takes care of another issue in one shot: experience collectors. If you’re not willing to spend six months developing the capacity to listen to another person without trying to “fix” them, you’re probably not going to come out of a ceremony any more relationally mature than you were before, no matter how many cool geometric shapes you see.'
V[42]['P26'] = 'The other aspect of this is integration: your life. Ceremony opens something. Did anything change? Look at your life in the weeks after a ceremony. Look at your relationships. Look at how you’re acting. Look at how you’re sleeping. Look at how you’re making decisions. Look at how you’re handling frustration without defining it as a new “spiritual emergency.”'
V[42]['P27'] = 'All of the “supports” are important: preparation, nutrition, screening for drug interactions, making sure the dose is appropriate, and having a plan for dealing with emergencies. They matter more than ceremony aesthetics. My current safety material is at [Altered States Triage](https://badtrips.u-dont-exist.com/).'
V[42]['P28'] = 'Finally, there are the legal issues. These vary a lot, and they are not always well-defined. As a community, you need to write down what is and isn’t allowed, which activities are private (to the individual, to a group in the community, or to the community vs the outside), and what kinds of activities have been reviewed from a legal standpoint. “I don’t think anybody around here has ever heard of that” is information, but it’s not the same thing as a legal opinion.'
V[42]['P29'] = 'It’s not uncommon for people to feel the urge to form a village after going through some serious psychedelic and/or mystical experiences. Finding a way to “find their people” and help others get where they’ve been is a powerful urge.'
V[42]['P30'] = 'I’ve felt that urge myself. The problem is that it can come with a degree of grandiosity. “My love can heal anyone” turns into a more realistic view once you realize that there are a lot of people who either don’t want to change, sincerely want to change but keep choosing the opposite, or are in such a crisis that their need for help is greater than someone’s ability to show up with nothing but enthusiasm.'
V[42]['P31'] = 'That urge may be real, but forming a community based on omnipotence is a terrible idea.'
V[42]['P32'] = 'Communities that are formed based on collective spiritual euphoria can take on more people than they can handle and promise too much, and only think through how much need they can absorb once several people already depend on them. Read the sections on capacity and membership, later in this article: they’re partly there to protect the original generosity from that first rush.'
V[42]['P33'] = 'Once the euphoria wears off and people have a more sober view of the call they feel, it can become useful. A community could be a place for people to train up in certain practices, and sometimes go off and start a new one. In fact, if people are living in a community in order to train up so they can help others build communities of their own, they’d be working towards forming a real alternative. That answers the reasonable objection that communes are just privileged escape pods.'
SRC42 = dict(SRC41)
SRC42.update({k: ('u7-emuA (round 8)' if k in ('P22','P23','P24','P25','P26','P27','P28') else ('u8-emuB (round 8)' if k == 'P32' else 'u8-emuA (round 8)')) for k in ['P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33']})
WHY42 = {k: ['v42 (section pass, Emulate round 8 over the last AI window as two runs; its raw runs read 100% Human, 411 and 294 words): rebuilt from the raw run with the meaning put back word by word; see emu/round8-u7u8-restored.json and the trace.'] for k in ['P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29', 'P30', 'P31', 'P32', 'P33']}

V[43] = dict(V[42])
V[43]['P1'] = "Key here is that most of the writing on communities hasn't caught up with psychedelics. They've gone from taboo toward regulated use really fast in a few jurisdictions ([licensed service centers for psilocybin started opening in Oregon](https://www.oregon.gov/oha/ph/preventionwellness/pages/oregon-psilocybin-services.aspx) in 2023, Colorado set up a system for regulating natural medicines and began licensing in 2025, and New Mexico enacted a [Medical Psilocybin Act](https://www.nmlegis.gov/Legislation/Legislation?Chamber=S&LegNo=219&LegType=B&year=25) in 2025), and Australia has allowed [limited access for a list of conditions via authorized psychiatrists](https://www.tga.gov.au/resources/explore-topic/mdma-and-psilocybine-hub) since 2023 for both psilocybin and MDMA."
V[43]['P2'] = 'That said, it\'s not a smooth ride or an inevitability. The US FDA issued a [Complete Response Letter](https://download.open.fda.gov/crl/CRL_NDA215455_20240808.pdf) to the MDMA-assisted therapy application in 2024, where they did not approve it and requested more evidence. And the thing with Portugal is that many people will lazily say "they\'ve legalized everything there" - but that\'s false, [they\'ve only decriminalized personal use of small quantities of drugs](https://www.euda.europa.eu/system/files/publications/642/PolicyProfile_Portugal_WEB_Final_289201.pdf). It\'s still a crime to traffic them.'
V[43]['P4'] = 'Even where the law allows some use, most intentional communities using psychedelics are not open about it, due to possible concerns from the parents of the children in the community, from neighbors imagining chaos, from insurance providers who might drop them, and from local officials who may not understand any of the distinctions.'
V[43]['P7'] = "They also attract people who love revelations but don’t want to do the work afterwards. You can have 12 ceremonies and 6 origin stories and still not be able to apologise to your housemate. Any community based mainly on peak experiences will find out sooner or later that insight doesn't do the dishes or comfort a scared kid."
V[43]['P8'] = 'In my experience there are real reasons to take psychedelics communally - eg lowering defensive barriers which otherwise dominate every serious conversation, and creating bonds between members of the community who have been through the harder nights together. But there are also negatives that can come from taking a psychedelic - confusion, grandiosity, dependency, fouling up dynamics between members. Are you mature enough as a community to separate the good from the bad?'
V[43]['P9'] = 'Part of it is integration: an insight needs somewhere to land. What happens when you come back from an amazing experience which gave you insight and clarity about your life, into the same old environment where nobody knows what you’ve been through and you’re faced with the same old cues? It can be super helpful to have gone through the experience in a community, with the people who held you through it there to notice what happens to you over the following months.'
V[43]['P11'] = "Do you trust the people you're relying on for support? It's very different from paying someone you don't know to look after you for a night. Sometimes they're great, but sometimes the person with the feather has only known you for 4 hours and already has a cosmology to explain everything you say."
V[43]['P12'] = "In a community, your sober sitter may be someone you've known for years, and you feel the difference between being watched and being held. This is especially true when doing iboga or other long and medically risky experiences. You need someone to properly screen you beforehand and watch you continuously."
V[43]['P13'] = 'Your peers can also help you reality check any downloads you may have had. Psychedelics can give you insight and they can give you convincing nonsense, all in the same bright shining light. A few friends who know your history can help you tell the difference between new understanding and mom.'
V[43]['P15'] = 'There are the obvious practical benefits: logistics are easier when it comes to things like having childcare arranged by the group that parents are comfortable leaving their kid(s) with, not needing to drive away from the ceremony, having someone bring water to someone or just sit with them while they come back to normal consciousness, etc.'
V[43]['P16'] = 'And then there will be people to play with! Raves often let strangers fast-track intimacy (getting to a level of intimacy that usually comes after building trust), but imagine doing ecstatic music & dance in a community that already knows each other (and has put up with each other’s bad habits). 💃🕺'
V[43]['P22'] = 'This is not to say that peer led ceremonies are ever casual. In fact, since the authority is spread around, there needs to be more competence. Some things are a must: screening for contra-indications (both medical and psychiatric), reviewing medications and combinations, having the right kind of sober sitter present, and deciding before anybody takes anything what kind of situations would require professional help or emergency care.'
V[43]['P23'] = 'Also, I am especially cautious about medicines and protocols that I see as more destabilizing and/or presenting more of a medical burden. This includes some uses of [ketamine and MDMA](http://mdmaket.u-dont-exist.com/) and [bufo](http://bufo.u-dont-exist.com/). My reasons are given in those articles, respectively, since they need more space.'
V[43]['P24'] = "Using medicine is secondary to all of the other pl/ork that comes first: reparenting, developing somatic capacity, and learning to do peer counseling. The medicine can deepen an existing practice, but it can't be a pharmacological short cut to what takes several months of honest relationship with other people."
V[43]['P25'] = 'This pre-requisite also takes care of another issue in one shot: it weeds out the experience collectors. If you’re not willing to spend six months developing the capacity to listen to another person without trying to “fix” them, you’re probably not going to come out of a ceremony any more relationally mature than you were before, no matter how many cool geometric shapes you see.'
V[43]['P27'] = 'All of the “supports” are important: preparation, nutrition, screening for drug interactions, being disciplined about the dose, and having a plan for dealing with emergencies. They matter more than ceremony aesthetics. My current safety material is at [Altered States Triage](https://badtrips.u-dont-exist.com/).'
V[43]['P29'] = 'It’s really common for people to feel the urge to form a village after going through some serious psychedelic and/or mystical experiences. Finding “their people” and helping others get to whatever just opened up for them is part of the same urge.'
V[43]['P30'] = 'I’ve felt that urge myself. The problem is that it can come with a degree of grandiosity, and I’ve felt that too. You come back believing love can heal anyone, and that turns into a more realistic view once you realize that there are people who either don’t want to change, sincerely want to change but keep choosing the opposite, or are in such a crisis that their need for help is more than your enthusiasm can hold.'
V[43]['P31'] = 'That call may be real, but forming a community based on omnipotence is a terrible idea.'
V[43]['P32'] = 'Communities that are formed during collective spiritual euphoria can take on too many people too fast and promise too much, and only think through how much need they can absorb once several people already depend on them. Read the sections on capacity and membership, later in this article: they’re partly there to protect the original generosity from that first rush.'
V[43]['P33'] = 'Once the euphoria wears off and people have a more sober view of the call they feel, it can become useful. A community can be a place for people to train up in the practices, and sometimes go off and start another experiment. In fact, if people are living in a community in order to train up so they can help others build communities of their own, they’d be working towards forming a real alternative. That answers the reasonable objection that communes are just privileged escape pods.'
SRC43 = dict(SRC42)
SRC43.update({k: v + ' (round 8)' for k, v in {'P1': 'u1-emuA', 'P2': 'u1-emuA', 'P4': 'u2-emuA', 'P7': 'u3-emuB', 'P8': 'u3-emuB', 'P9': 'u3-emuB', 'P11': 'u4-emuB', 'P12': 'u4-emuB', 'P13': 'u4-emuB', 'P15': 'u5-emuB', 'P16': 'u5-emuB'}.items()})
WHY43 = {k: ['v43: section pass, Emulate round 8 (the raw runs read 100% Human); rebuilt from the raw run with the meaning put back word by word (P1 to P16), or TRACE-v42-A/B’s findings made in their terms (P22 to P33); records in emu/round8-v43.json and the traces.'] for k in ['P1', 'P2', 'P4', 'P7', 'P8', 'P9', 'P11', 'P12', 'P13', 'P15', 'P16', 'P22', 'P23', 'P24', 'P25', 'P27', 'P29', 'P30', 'P31', 'P32', 'P33']}

V[44] = dict(V[43])
fix(V[44], 'P1', "They've gone from taboo toward regulated use really fast in a few jurisdictions (", "They've gone from taboo toward regulated use really fast (")
fix(V[44], 'P1', 'and Australia has allowed [limited access for a list of conditions via authorized psychiatrists](https://www.tga.gov.au/resources/explore-topic/mdma-and-psilocybine-hub) since 2023 for both psilocybin and MDMA.', 'and Australia has allowed [authorized psychiatrists limited access](https://www.tga.gov.au/resources/explore-topic/mdma-and-psilocybine-hub) for a list of conditions since 2023, for both psilocybin and MDMA.')
fix(V[44], 'P2', "[they've only decriminalized personal use of small quantities of drugs]", "[they've only decriminalized possessing small quantities for personal use]")
fix(V[44], 'P4', 'Even where the law allows some use, most intentional communities using psychedelics are not open about it, due to possible concerns from the parents of the children in the community, from neighbors', 'Most intentional communities using psychedelics are still not open about it. Even where the law allows some use, there are possible concerns from parents worried about children, from neighbors')
fix(V[44], 'P7', 'who love revelations but don’t want to do the work afterwards.', 'who love revelations but hate doing the work afterwards.')
fix(V[44], 'P8', 'there are real reasons to take psychedelics communally - eg lowering defensive barriers which otherwise dominate every serious conversation, and creating bonds between', 'there are real reasons to take psychedelics communally too - eg they can lower defensive barriers which otherwise dominate every serious conversation, and create strong bonds between')
fix(V[44], 'P8', 'to separate the good from the bad?', 'to tell the good from the bad?')
fix(V[44], 'P9', 'in a community, with the people who held you through it there to notice what happens to you over the following months.', 'in a community, where the people who held you through it can also notice what happens to you over the following months.')
fix(V[44], 'P11', "It's very different from paying someone you don't know to look after you for a night.", "Support from people you trust is very different from the commercial alternative, which is often paying someone you don't know to look after you for a night.")
fix(V[44], 'P12', "may be someone you've known for years,", "may be someone who's known you for years,")
fix(V[44], 'P12', 'This is especially true when doing iboga or other long and medically risky experiences. You need someone to properly screen you beforehand and watch you continuously.', 'This matters even more when doing iboga or other long and medically risky experiences. For those you need proper screening beforehand and someone watching you continuously.')
fix(V[44], 'P13', 'Your peers can also help you reality check', 'Your peers can also reality check')
fix(V[44], 'P13', 'Psychedelics can give you insight and', 'Psychedelics can give you genuine insight and')
fix(V[44], 'P13', 'A few friends who know your history can help you tell the difference between new understanding and mom.', 'A few friends who know your history can tell which parts look like a new understanding and which look like… mom.')
fix(V[44], 'P15', 'There are the obvious practical benefits:', 'There are the practical benefits:')
fix(V[44], 'P15', 'or just sit with them while they come back', 'or just sit quietly with them while they come back')
fix(V[44], 'P16', '(and has put up with each other’s bad habits)', '(and each other’s inconvenient habits)')
fix(V[44], 'P26', 'The other aspect of this is integration: your life.', "Then there's integration: your life.")
fix(V[44], 'P30', 'The problem is that it can come with a degree of grandiosity, and I’ve felt that too. You come back believing love can heal anyone, and that turns into a more realistic view once you realize that there are people who either don’t want to change, sincerely want to change but keep choosing the opposite, or are in such a crisis that their need for help is more than your enthusiasm can hold.', 'The problem is that it can come with grandiosity, and I’ve felt that too. You come back believing love can heal anyone, and then you meet people who don’t want to change, people who sincerely want to change but keep choosing the opposite, and people in such a crisis that their need for help is more than your enthusiasm can hold.')
fix(V[44], 'P32', 'can take on too many people too fast and promise too much, and only think through how much need they can absorb once several people already depend on them.', 'can recruit too fast and promise too much, and they can end up thinking through how much need they can absorb only once several people already depend on them.')
fix(V[44], 'P33', 'In fact, if people are living in a community in order to train up so they can help others build communities of their own,', 'In fact, if people are training there so they can help others build communities of their own,')
SRC44 = dict(SRC43)
WHY44 = {k: ['v44 (TRACE-v43-A to -D, LOGIC-v43-A and -B, STANCE-v43, the v43 cold read), word by word in their terms; the list of findings and what stays (Joel’s own changes, wording every gate since v20 accepted) is in PREDICTIONS-s5.md.'] for k in ['P1', 'P2', 'P4', 'P7', 'P8', 'P9', 'P11', 'P12', 'P13', 'P15', 'P16', 'P26', 'P30', 'P32', 'P33']}

V[45] = dict(V[44])
V[45]['P4'] = 'Even where the law allows some use, there are possible concerns from parents worried about children, from neighbors imagining chaos, from insurance providers who might drop them, and from local officials who may not understand any of the distinctions, so most intentional communities using psychedelics are still not open about it.'
V[45]['P11'] = "Do you trust the people you're relying on for support? It's very different from what often happens instead, paying someone you don't know to look after you for a night. Sometimes they're great, but sometimes the person with the feather has only known you for 4 hours and already has a cosmology ready to explain everything you say."
V[45]['P12'] = "Having someone who's known you for years as your sober sitter can make the difference between being watched and being held, and in a community you can. This matters even more when doing iboga or other long and medically risky experiences. For those you need proper screening beforehand and someone watching you continuously."
V[45]['P25'] = 'This pre-requisite also takes care of another issue in one shot: it weeds out the experience collectors. If someone is unwilling to put in 6 months learning to listen without fixing, it is unlikely they will come out of a ceremony more relationally mature, regardless of how mindblowing the geometric shapes they saw were.'
SRC45 = dict(SRC44)
WHY45 = {
 'P4': ['v45 (batch 21: v44’s second sentence read AI as its own window; batch 22: dA1 Human): the risks first, as Emulate’s opener had it, and the secrecy as their result ("…so most intentional communities using psychedelics are still not open about it"), which keeps the logic the v43 audits asked for: "even where the law allows some use" governs the risks, and the claim is about most communities.'],
 'P11': ['v45 (batch 21: P11’s last two sentences and P12’s first read AI as one window; batch 23: dC2 Human): Emulate’s B wording back with the meaning in it: "It’s very different from what often happens instead, paying someone you don’t know…" ("often", the alternative), "already has a cosmology ready to explain everything you say".'],
 'P12': ['v45 (same window): "Having someone who’s known you for years as your sober sitter can make the difference between being watched and being held, and in a community you can" (published: in community the sitter may be somebody who has known you for years; being watched and being held feel different).'],
 'P25': ['v45 (batch 21: Emulate A’s second sentence read AI as its own window three times; batch 22: v41’s wording Human): v41’s second sentence, traced since v24.'],
}

V[46] = dict(V[45])
V[46]['P4'] = 'Most intentional communities using psychedelics are not open about it, due to possible concerns (even where the law allows some use) from parents worried about children, from neighbors imagining chaos, from insurance providers who might drop them, and from local officials who may not understand any of the distinctions.'
V[46]['P11'] = "Do you trust the people you're relying on for support? It's very different from paying someone you don't know to look after you for a night. Sometimes they're great, but sometimes the person with the feather has only known you for 4 hours and already has a cosmology to explain everything you say."
V[46]['P12'] = "In a community, your sober sitter may be someone who's known you for years, and you feel the difference between being watched and being held. This is especially true when doing iboga or other long and medically risky experiences. For those you need someone to properly screen you beforehand and watch you continuously."
V[46]['P13'] = 'Your peers can also reality check any downloads you may have had. Psychedelics can give you insight and they can give you convincing nonsense, all in the same bright shining light. A few friends who know your history can tell the difference between new understanding and… mom.'
SRC46 = dict(SRC45)
WHY46 = {
 'P4': ['v46 (batch 25: with P3 and P5, v45’s P4 read AI and this one Human, 0.01): Emulate’s order back, with "(even where the law allows some use)" on the concerns, so the logic stays as the v43 audits asked.'],
 'P11': ['v46 (batch 25: P10 to P14 read 0.81 with v45’s P11 to P13, 0.32 with v43’s): v43’s P11 back. Kept with reasons: "It’s very different from paying someone you don’t know…" (the contrast is still with paid strangers; no claim that all paid care is strangers).'],
 'P12': ['v46: v43’s P12 with the two fixes that change what a reader believes: "someone who’s known you for years" (who knows whom) and "For those you need someone to…" (iboga-type experiences, not every ceremony). Kept: "This is especially true".'],
 'P13': ['v46: v43’s P13 without "help you" in either sentence (the peers check; the friends tell), and "… mom" as the punchline (the cold read couldn’t place "mom"). Kept: "insight" without "genuine" (the contrast with "convincing nonsense" carries it).'],
}

V[47] = dict(V[46])
fix(V[47], 'P4', "Most intentional communities using psychedelics are not open about it,", "Most intentional communities using psychedelics are still not open about it,")
fix(V[47], 'P12', "This is especially true when doing iboga", "This is especially important when doing iboga")
fix(V[47], 'P13', "A few friends who know your history can tell the difference between", "A few friends who know your history may notice the difference between")
SRC47 = dict(SRC46)
WHY47 = {
 'P4': ['v47 (TRACE-v46-A: "still" DROPPED; the v43 gate had asked for it and v46’s reorder lost it): "are still not open about it" (published: "still avoid saying so publicly", the secrecy goes on while the law moves).'],
 'P12': ['v47 (TRACE-v46-B, LOGIC-v46-A and -B: "This is especially true" reads as the felt difference being stronger on iboga; published "This matters especially"): "This is especially important" (Emulate A’s word in round 8, u4A).'],
 'P13': ['v47 (TRACE-v46-B, LOGIC-v46-A and -B, STANCE-v46: "can tell the difference" asserts an ability; published "may notice"): "may notice the difference between new understanding and… mom".'],
}

V[48] = dict(V[47])
fix(V[48], 'P4', "are still not open about it, due to possible concerns (even where the law allows some use) from", "are still not public about it, due to possible trouble (even where the law allows some use) from")
fix(V[48], 'P12', "For those you need someone to properly screen you beforehand and watch you continuously.", "For those you need to be properly screened beforehand and monitored continuously.")
V[49] = dict(V[48])
fix(V[49], 'P11', "It's very different from paying someone you don't know", "Support from people you trust is very different from paying someone you don't know")
SRC48 = dict(SRC47); SRC49 = dict(SRC48)
WHY48 = {
 'P4': ['v48 (TRACE-v47 and LOGIC-v47: "not open about it" can read as secrecy toward everyone, published "avoid saying so publicly"; "concerns from" insurers and officials gives them concerns the published doesn’t, where insurers "may disappear" and an official "may understand none of the distinctions"): "not public about it", "possible trouble … from".'],
 'P12': ['v48 (TRACE-v47 and LOGIC-v47: one "someone" to screen and watch reads as the sitter doing the medical screening, and the published names no one; TRACE-v46-B and the v47 cold read: "watch you" right after "being watched" makes you reread): "For those you need to be properly screened beforehand and monitored continuously" (published: "screening and continuous observation are essential").'],
}
WHY49 = {
 'P11': ['v49 (the v47 cold read: "It" has no referent until P12): "Support from people you trust is very different from paying someone you don’t know…" (published: "Trusted support is different from purchased support").'],
}

V[50] = dict(V[49])
fix(V[50], 'P11', "Support from people you trust is very different from paying someone you don't know to look after you for a night.", "Support from people you trust is different from paying people you don't know to look after you for a night.")
fix(V[50], 'P29', "helping others get to whatever just opened up for them is part", "helping others get to whatever just opened up is part")
V[51] = dict(V[50])
fix(V[51], 'P11', "to look after you for a night.", "to look after you for a night, which is often the alternative.")
SRC50 = dict(SRC49); SRC51 = dict(SRC50)
WHY50 = {
 'P11': ['v50 (LOGIC-v49-A: "very different" makes the gap large, published "is different from"; LOGIC-v49-A and TRACE-v49-A: "Sometimes they’re great" has three possible antecedents once S2 names "people you trust"): "very" out; "paying people you don’t know" (plural, as the published "paying strangers"), so "they" takes the nearest plural.'],
 'P29': ['v50 (LOGIC-v46-B and the v49 cold read: "them" first reads as the others): "whatever just opened up" (published: "whatever just opened").'],
}
WHY51 = {
 'P11': ['v51 (LOGIC-v43, LOGIC-v49-A: without "often" a reader takes paying strangers as what paid support is; published "The commercial alternative is often paying strangers for one night of care"): ", which is often the alternative".'],
}

V[52] = dict(V[51])
V[52]['P7'] = "They do also attract people who are all for revelation and hate the follow-through, people who can collect 12 ceremonies and 6 origin stories and still can't say sorry to their housemate. Any community based mainly around the peak experience is going to find out sooner or later that the insight doesn't do the practical work for it. Sometimes the dishes need doing and a scared kid needs comforting."
V[52]['P26'] = 'Integration is your life. The ceremony opens something up in you. Look at your life after the ceremony for a few weeks and see how things have changed, if at all. Look at your relationships, your behavior, your sleeping habits, your decision-making, and how well you can deal with frustration without declaring a new spiritual emergency.'
V[52]['P32'] = 'A group that begins in collective spiritual euphoria can recruit too quickly and promise too much, and only do the math on how much need it can absorb once several people already depend on it. The sections on capacity and on membership, later on in this article, are partly there to protect the original generosity from that first rush.'
SRC52 = dict(SRC51)
WHY52 = {
 'P7': ['v52 (batch 32: v43’s P7, rebuilt from Emulate round 8 for the section’s windows, reads 100% AI alone, 0.97): v20’s P7 back, which passed alone (batch 5, 0.0) and went through the v20 to v41 gates (traces, LOGIC-v29 A and B). It has the published "collect" (TRACE-v46-A: "have" had lost it, and P25’s "experience collectors" points back to it).'],
 'P26': ['v52 (batch 32: v43’s P26 reads 100% AI alone, 0.62; batches 33 and 34: v37’s body reads AI with every opener but "The other aspect is", which the v43 cold read couldn’t place): Emulate round 10 B (`emulate-runs/community-s5j`, raw 0.0) with the meaning put back word by word: the claims "Integration is your life." (published "Integration is ordinary life.") and "The ceremony opens something up in you." (B asked both as questions), "how things have changed, if at all" (B’s, the published "whether anything changed"), the five places, and the quip "without declaring a new spiritual emergency" (B had dropped it; the published wording, so no scare quotes).'],
 'P32': ['v52 (batch 32: v51’s P32 reads 100% AI alone, 0.86): v41’s P32 (the round-8 input), which passes alone (batch 33, 0.27): "can recruit too quickly and promise too much, and only do the math … once several people already depend on it" (published "can recruit too quickly, promise too much, and discover arithmetic only after several people are already dependent on it"; "can" over all three) and the sections’ purpose as published.'],
}

V[53] = dict(V[52])
fix(V[53], 'P11', "Support from people you trust is different from paying people you don't know to look after you for a night, which is often the alternative.", "Support from people you trust is different from paid support, which is often people you don't know looking after you for a night.")
fix(V[53], 'P26', "Integration is your life.", "Integration is everyday life.")
fix(V[53], 'P26', "Look at your life after the ceremony for a few weeks and see", "Look at your life in the weeks after the ceremony and see")
fix(V[53], 'P29', "It’s really common for people to feel the urge", "A lot of people feel the urge")
fix(V[53], 'P29', "Finding “their people” and", "Finding their people and")
SRC53 = dict(SRC52)
WHY53 = {
 'P11': ['v53 (LOGIC-v43, -v49-A and -v52-A, TRACE-v52-A: the contrast had narrowed from purchased support to paying strangers for a night, and "often" sat on the wrong thing; published "Trusted support is different from purchased support. The commercial alternative is often paying strangers for one night of care."): "different from paid support, which is often people you don’t know looking after you for a night". "They" in the next sentence now has one plural before it.'],
 'P26': ['v53 (LOGIC-v52-A: "Integration is your life" reads as the idiom "X is your life", everything to you; published "Integration is ordinary life"; and "for a few weeks" sets a number the published "The following weeks" doesn’t): "Integration is everyday life." ("ordinary" is on the AI-frequency list), "in the weeks after the ceremony".'],
 'P29': ['v53 (LOGIC-v52-A: "It’s really common" makes the urge the usual response, published "Many people"; TRACE-v52-A, and the v7 trace before it: the quotation marks around "their people" are added): "A lot of people feel the urge…", no quotation marks.'],
}

V[54] = dict(V[53])
fix(V[54], 'P11', "which is often people you don't know looking after you for a night.", "which is often paying people you don't know to look after you for a night.")
fix(V[54], 'P26', "in the weeks after the ceremony and see", "in the weeks that follow the ceremony and see")
fix(V[54], 'P29', "after going through some serious", "after they’ve gone through some serious")
fix(V[54], 'P29', "whatever just opened up is part", "whatever has just opened up is part")
SRC54 = dict(SRC53)
WHY54 = {
 'P11': ['v54 (batch 37: v53 read 5.0% AI with two windows downstream, P19 and P25/P26; v52, two words longer here, read 0%): "which is often paying people you don’t know to look after you for a night" (the published "paying strangers"), so P11 has v52’s length.'],
 'P26': ['v54 (the same): "in the weeks that follow the ceremony" (the published "the following weeks"), v52’s length.'],
 'P29': ['v54 (the same): "after they’ve gone through", "whatever has just opened up", v52’s length.'],
}

V[56] = dict(V[52])
V[56]['P11'] = V[54]['P11']
V[56]['P29'] = V[53]['P29']
SRC56 = dict(SRC54)
WHY56 = {
 'P11': ['v56 (batches 39 to 41: v54’s P11 doesn’t move the section’s windows): v54’s P11 on v52.'],
 'P26': ['v56 (batches 37 to 41: every change tried in P26’s third sentence, "in the weeks after the ceremony", "in the weeks that follow the ceremony", "for some weeks", brings AI windows back at P19 and P25 in the section, though each passes alone): v52’s P26. Left for Joel: "for a few weeks" (LOGIC-v52-A: "a few" sets a number the published "The following weeks" doesn’t) and "Integration is your life." (LOGIC-v52-A AMBIGUOUS: the idiom).'],
 'P29': ['v56: v53’s P29 on v52 (batch 40: the section reads 0% with it).'],
}

V[59] = dict(V[56])
fix(V[59], 'P2', "It's still a crime to traffic them.", "It's still a crime to traffic drugs.")
V[60] = dict(V[59])
V[60]['P26'] = V[53]['P26']
SRC59 = dict(SRC56); SRC60 = dict(SRC59)
WHY59 = {
 'P2': ['v59 (the v56 cold read and TRACE-v46-A: "traffic them" has nothing to point to, since v44’s link text dropped "drugs"): "It’s still a crime to traffic drugs." (published "trafficking remains criminal"). Batch 43: the section stays at 0%.'],
}
WHY60 = {
 'P26': ['v60 (LOGIC-v52-A and the v56 cold read: "Integration is your life." reads as the idiom at first; LOGIC-v52-A: "for a few weeks" sets a number): v53’s P26, "Integration is everyday life." (published "Integration is ordinary life") and "in the weeks after the ceremony" (published "The following weeks"); it passes alone (batch 37, 0.01). With it the section has two small AI windows elsewhere (batches 37, 38, 42); v59 keeps v52’s P26 at 0%. Meaning first: AGENTS.md, "Detector results are evidence, not editorial authority".'],
}

def build(n, src):
    B = V[n]
    json.dump({'version': n, 'order': ORDER, 'blocks': B, 'source': src}, open(HERE / ('final-v%d.json' % n), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    md = '\n\n'.join(B[k] for k in ORDER) + '\n'
    (HERE / ('section-v%d.md' % n)).write_text(md, encoding='utf-8')
    plain = lambda ks: mdplain.plain('\n\n'.join(B[k] for k in ks if not k.startswith('IMG'))).strip() + '\n'
    return md, plain


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    md, plain = build(n, {1: SRC1, 2: SRC2, 3: SRC3, 4: SRC4, 5: SRC5, 6: SRC6, 7: SRC7, 8: SRC8, 9: SRC9, 10: SRC10, 11: SRC11, 12: SRC12, 13: SRC13, 14: SRC14, 15: SRC15, 16: SRC16, 17: SRC17, 18: SRC18, 19: SRC19, 20: SRC20, 21: SRC21, 22: SRC22, 23: SRC23, 24: SRC24, 25: SRC25, 26: SRC26, 27: SRC27, 28: SRC28, 29: SRC29, 30: SRC30, 31: SRC31, 32: SRC32, 33: SRC33, 34: SRC34, 35: SRC35, 36: SRC36, 37: SRC37, 38: SRC38, 39: SRC39, 40: SRC40, 41: SRC41, 42: SRC42, 43: SRC43, 44: SRC44, 45: SRC45, 46: SRC46, 47: SRC47, 48: SRC48, 49: SRC49, 50: SRC50, 51: SRC51, 52: SRC52, 53: SRC53, 54: SRC54, 56: SRC56, 59: SRC59, 60: SRC60}.get(n, SRC60))
    WHY = {k: WHY1.get(k, []) + (WHY2.get(k, []) if n >= 2 else []) + (WHY3.get(k, []) if n >= 3 else []) + (WHY4.get(k, []) if n >= 4 else []) + (WHY5.get(k, []) if n >= 5 else []) + (WHY6.get(k, []) if n >= 6 else []) + (WHY7.get(k, []) if n >= 7 else []) + (WHY8.get(k, []) if n >= 8 else []) + (WHY9.get(k, []) if n >= 9 else []) + (WHY10.get(k, []) if n >= 10 else []) + (WHY11.get(k, []) if n >= 11 else []) + (WHY12.get(k, []) if n >= 12 else []) + (WHY13.get(k, []) if n >= 13 else []) + (WHY14.get(k, []) if n >= 14 else []) + (WHY15.get(k, []) if n >= 15 else []) + (WHY16.get(k, []) if n >= 16 else []) + (WHY17.get(k, []) if n >= 17 else []) + (WHY18.get(k, []) if n >= 18 else []) + (WHY19.get(k, []) if n >= 19 else []) + (WHY20.get(k, []) if n >= 20 else []) + (WHY21.get(k, []) if n == 21 else []) + (WHY22.get(k, []) if n == 22 else []) + (WHY23.get(k, []) if n >= 23 else []) + (WHY24.get(k, []) if n >= 24 else []) + (WHY25.get(k, []) if n >= 25 else []) + (WHY26.get(k, []) if n >= 26 else []) + (WHY27.get(k, []) if n >= 27 else []) + (WHY28.get(k, []) if n >= 28 else []) + (WHY29.get(k, []) if n == 29 else []) + (WHY30.get(k, []) if n >= 30 else []) + (WHY31.get(k, []) if n == 31 else []) + (WHY32.get(k, []) if n == 32 else []) + (WHY33.get(k, []) if n == 33 else []) + (WHY34.get(k, []) if n >= 34 else []) + (WHY35.get(k, []) if n >= 35 else []) + (WHY36.get(k, []) if n >= 36 else []) + (WHY37.get(k, []) if n >= 37 else []) + (WHY38.get(k, []) if n >= 38 else []) + (WHY39.get(k, []) if n >= 39 else []) + (WHY40.get(k, []) if n >= 40 else []) + (WHY41.get(k, []) if n >= 41 else []) + (WHY42.get(k, []) if n >= 42 else []) + (WHY43.get(k, []) if n >= 43 else []) + (WHY44.get(k, []) if n >= 44 else []) + (WHY45.get(k, []) if n >= 45 else []) + (WHY46.get(k, []) if n >= 46 else []) + (WHY47.get(k, []) if n >= 47 else []) + (WHY48.get(k, []) if n >= 48 else []) + (WHY49.get(k, []) if n >= 49 else []) + (WHY50.get(k, []) if n >= 50 else []) + (WHY51.get(k, []) if n >= 51 else []) + (WHY52.get(k, []) if n >= 52 else []) + (WHY53.get(k, []) if n >= 53 and not (n >= 56 and k == 'P26') else []) + (WHY54.get(k, []) if n >= 54 and not (n >= 56 and k in ('P26', 'P29')) else []) + (WHY56.get(k, []) if n >= 56 and not (n >= 60 and k == 'P26') else []) + (WHY59.get(k, []) if n >= 59 else []) + (WHY60.get(k, []) if n >= 60 else []) for k in ORDER}
    json.dump({'about': 'Section 5 v%d: each changed paragraph\'s published text, its Emulate source (exact outputs in emu/), the text, and why.' % n,
               'paragraphs': [{'p': k, 'published': O[k], 'from': SRC1.get(k), 'v%d' % n: V[n][k], 'why': WHY.get(k, [])}
                              for k in ORDER if k.startswith('P') and V[n][k] != O[k]]},
              open(HERE / 'fixlog-s5.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    R = HERE / ('r%d' % n); R.mkdir(exist_ok=True)
    CHECKS = json.load(open(HERE / ('checks-v%d.json' % n))) if (HERE / ('checks-v%d.json' % n)).exists() else {}
    for name, ks in CHECKS.items():
        t = plain(ks)
        assert '\\n' not in t and '#' not in t, name
        (R / (name + '.txt')).write_text(t, encoding='utf-8'); print(name, len(t.split()))
    for k in ORDER:
        if k.startswith('P'): print(k, len(plain([k]).split()), end='; ')
    print('\nsection words', len(plain(ORDER).split()))
