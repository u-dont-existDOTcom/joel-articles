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


def build(n, src):
    B = V[n]
    json.dump({'version': n, 'order': ORDER, 'blocks': B, 'source': src}, open(HERE / ('final-v%d.json' % n), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    md = '\n\n'.join(B[k] for k in ORDER) + '\n'
    (HERE / ('section-v%d.md' % n)).write_text(md, encoding='utf-8')
    plain = lambda ks: mdplain.plain('\n\n'.join(B[k] for k in ks if not k.startswith('IMG'))).strip() + '\n'
    return md, plain


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    md, plain = build(n, {1: SRC1, 2: SRC2, 3: SRC3, 4: SRC4, 5: SRC5, 6: SRC6, 7: SRC7}.get(n, SRC7))
    WHY = {k: WHY1.get(k, []) + (WHY2.get(k, []) if n >= 2 else []) + (WHY3.get(k, []) if n >= 3 else []) + (WHY4.get(k, []) if n >= 4 else []) + (WHY5.get(k, []) if n >= 5 else []) + (WHY6.get(k, []) if n >= 6 else []) + (WHY7.get(k, []) if n >= 7 else []) for k in ORDER}
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
