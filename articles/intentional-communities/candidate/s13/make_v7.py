"""Section 13 draft v7 (2026-10-15, Joel's 31 a): each paragraph that read AI, or never passed its records, rebuilt from
the closer Emulate version with the published meaning put back word by word. The four paragraphs that have read Human
stay as they are (H1-P3, H2-P2, H3-P2, H4-P1), copied from v6. Writes v7.md and v7-sources.json (each paragraph's
Emulate source and the word fixes made to it). Run from this folder: python3 make_v7.py

Emulate files: emu-b/out (round b, from v6), emu-c/out (round c, from v6), emu-d/out (round d, from the published text
and from v6). Characters stay as Emulate returned them (straight or curly), including in the words put back."""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
FARM = 'https://thefarmcommunity.com/'
CALT = ('https://library.uniteddiversity.coop/Ecovillages_and_Low_Impact_Development/'
        'Creating_a_Life_Together-Practical_Tools_to_Grow_Ecovillages_and_Intentional_Communities.pdf')
FAKER = 'http://sidney.u-dont-exist.com/'
RESEARCH = 'https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/'


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v6 = blocks((HERE / 'v6.md').read_text(encoding='utf-8'))
def v6p(start):
    hits = [b for b in v6 if b.startswith(start)]
    assert len(hits) == 1, start
    return hits[0]


P = []   # (heading or None, paragraph id, text, source, fixes)
def head(h):
    P.append((h, None, None, None, None))
def para(pid, text, source, fixes):
    P.append((None, pid, text, source, fixes))


head('# Your Little Forming Group Already Is the Community')
para('H1-P1', "Don't worry about getting land yet. If you've got a small handful of people who want to make a community "
     "but aren't sure yet, you are already a community. It sounds cheesy but it's true.",
     'emu-b e01-emuB (first paragraph)',
     ['dropped the "1." numbering', '"you are a community" -> "you are already a community" (U2: the first community)'])
para('H1-P2', "Don't combine ownership/major resources until the group has had at least one real conflict and dealt with "
     "it all the way through. Not \"dealt with it\" by writing a vision statement and shaking hands, or declaring a truce "
     "nobody believes, but really dealing with it. In other words, you need to do some real relational pl/ork where "
     "someone names what happened and each person gets time. What comes up in conflicts is always jealousy, humiliation, "
     "fear, or other old material, so find out which. Deal with it until the emotional pressure has changed enough for "
     "an agreement to mean something, and then you can make one.",
     'emu-b e01-emuB (second paragraph)',
     ['dropped the "2." numbering', '+"all the way through" (published)', '+"nobody believes" (published)',
      '"where someone says "what you did was wrong" and everyone takes the time to deal with it" -> "where someone names '
      'what happened and each person gets time" (published: name what happened, give each person time)',
      '"is always jealousy, humiliation, fear, and other stuff from the past" -> "is always jealousy, humiliation, fear, '
      'or other old material, so find out which" (published: find the ... or old material involved)',
      '"until the emotional pressure valve changes and then you can make an agreement" -> "until the emotional pressure '
      'has changed enough for an agreement to mean something, and then you can make one" (published condition)'])
para('H1-P3', v6p('Until that’s happened'), 'v6, unchanged (read Human alone, 287g)', [])
para('H1-P4', "Along with that, you'll also need to budget for the group's physical needs. That is, the things they can "
     "offer in the way of water, housing, food stores, health care, tools, seasonal labor, transportation, schooling, "
     "market access, etc. If there are outside debts to pay or cash reserves, how long will the cash last? What critical "
     "skills will the group need that they don't currently have? It's boring stuff but in the end, a group could be "
     "great on an emotional level but be dead in the water because the well fails, or because one exhausted person is "
     "the only one who knows where everything is and how it works.",
     'emu-c f01-emuA',
     ['"it would be a good idea to also budget" -> "you\'ll also need to budget" (published: an instruction)',
      '+"outside" before debts; "how long will they last?" -> "how long will the cash last?" (published: outside debts '
      'or cash runway)',
      '"be dead in the water physically due to a lack of foresight" -> "be dead in the water because the well fails, or '
      'because one exhausted person is the only one who knows where everything is and how it works" (published causes)'])

head('## Please Choose the Values Before Falling in Love With the View')
para('H2-P1', "Have you noticed people choose their community in the same way they would choose a vacation rental? "
     "“Wow! Look at this beautiful land! And a pond, with the sunset in it!! Who needs a beach?! And the people seem "
     "really nice, let’s get in here!” Fast forward two years. “Wait, there’s a vaccination policy?? And you need "
     "paperwork for it?!?!”",
     'emu-c f02-emuA',
     ['"Do you feel like you chose your community in the same way you would choose" -> "Have you noticed people choose '
      'their community in the same way they would choose" (published: people often choose; the reader hasn\'t chosen yet)',
      '"And a pond!!" -> "And a pond, with the sunset in it!!" (published: the pond reflects the sunset)',
      'cut "before someone else grabs it" (added haste)', '"2-years" -> "two years"',
      '"You want ME to get a shot for what??" -> "Wait, there’s a vaccination policy??" (published: the vaccination '
      'policy, either way; the shot took a side)'])
para('H2-P2', v6p('When you go to visit a community'), 'v6, unchanged (read Human inside 2P1P2, 288g)', [])
para('H2-P3', "Throw sexuality and gender onto that list. Is it ok to be openly part of the LGBTQ+ community? Is it okay "
     "to date and/or be in a relationship with whomever you choose? Will your community keep you fully protected if you "
     "are a member of the aforementioned community? Will your children be encouraged or discouraged to question their "
     "sexual identities at an early age? Should your children grow up to be gay or transgender, what happens then? Until "
     "your prospective community has answered these questions, its values on freedom and child-rearing are incomplete. "
     "Also make sure that your list declares whether or not you value experimenting, the folks next to you may think "
     "experimenting ended in 1978 and anything that came from it is doctrine now.",
     'emu-c f03-emuA',
     ['"Sexuality and Gender" -> lower case', '+"openly" (published: live openly)',
      '"look out for you" -> "keep you fully protected" (published: remain fully protected)',
      '"sexual make up" -> "sexual identities" (published)',
      '"will your community accept them?" -> "what happens then?" (published: what happens if)',
      '"Until you ask yourself and your prospective community these questions, your list of Values is incomplete." -> '
      '"Until your prospective community has answered these questions, its values on freedom and child-rearing are '
      'incomplete." (published: the group hasn\'t finished discussing freedom or child-rearing values)',
      '"includes" -> "declares" (published: has to be declared)',
      '"some folks think" -> "the folks next to you may think" (published: the person beside you may believe)',
      '"\'78" -> "1978"', '"should be considered doctrine" -> "is doctrine now" (published: the results are now doctrine)'])
para('H2-P4', "Once you’ve got a good sense of what is important to you, compare this to how the group actually "
     "functions (not just how they talk about functioning). How was a recent conflict handled? Who can block decisions, "
     "and how? How did it go for the last person who left the group? Who owns the land? It might be uncomfortable to "
     "have some of these conversations, but the view won’t go away after you’ve had them.",
     'emu-c f04-emuB',
     ['dropped the "5." numbering', '"How are conflicts handled?" -> "How was a recent conflict handled?" (published)',
      '"Who can make decisions and how?" -> "Who can block decisions, and how?" (published: who can block a decision)',
      '"How hard is it to leave the group?" -> "How did it go for the last person who left the group?" (published: what '
      'happened to the last person who left)', '"Who “owns” the land?" -> "Who owns the land?"',
      '"after you’ve seen it" -> "after you’ve had them" (published: after the uncomfortable conversation)'])

head('## Resources, Land, and Exit Terms')
para('H3-P1', "People tend to not take this into account enough. Whoever has the title to the land has a massive amount of "
     "power over the community. If the deed is in the founder's name, then they're really a landlord just with a "
     "philosophy. If it's in the name of three members out of twelve, then there's effectively two classes of members "
     "even if the literature says everyone's equal.",
     'emu-b e02-emuB',
     ['+"over the community" (published)', '"If it\'s in the founders name, then he\'s" -> "If the deed is in the '
      'founder\'s name, then they\'re" (published: the deed; no gender)', '"3 members" -> "three members out of twelve"'])
para('H3-P2', v6p('What legal form will hold the land'), 'v6, unchanged (read Human alone, 287g)', [])
para('H3-P3', "Visibility is important even in a money-free community. There are always scarce things and bottlenecks. "
     "It is important that people be able to know what the community owns or holds in common, what is set aside, what "
     "it owes to outsiders. Who has authority over distribution of major resources? Where are the conflicts of interest? "
     "Transfers of major resources (land, equipment, stores, outside cash, etc.) need to be recorded somewhere, and "
     "can't depend on one person's permission. It is also important to specify what rights people have to resources "
     "when they leave the community. If the community does not use money, it still needs to be able to provide people "
     "with resources when they leave (tools, transportation, temporary housing, stored goods, the right to keep using "
     "something, etc). Otherwise the \"right\" to leave is just something on paper that can only be exercised if there "
     "is money around.",
     'emu-b e03-emuB',
     ['"A description is important even in a non-money community." -> "Visibility is important even in a money-free '
      'community." (published: make the material system legible)', '"always bottlenecks" -> "always scarce things and '
      'bottlenecks" (published)', '"what the community has" -> "what the community owns or holds in common" (published)',
      '"(land, equipment, stored resources, outside money, etc.)" -> "(land, equipment, stores, outside cash, etc.)"; '
      '+"and can\'t depend on one person\'s permission" (published: not on one person\'s memory or permission)',
      '"stored resources, etc)" -> "stored goods, the right to keep using something, etc)" (published: continued use '
      'rights)'])
para('H3-P4', "Good people leave for good reasons, often due to a dying parent, love, work, health, exhaustion, or just "
     "a simple change of mind. Leaving should not require someone to leave everything they’ve put in, as that’s "
     "effectively coercing someone to stay. You should set the terms of letting someone leave when no one is leaving, "
     "and it’s just a theoretical discussion. Think of it as a pre-nup while you’re planning the wedding. It’s not "
     "that romantic, but it’s protective, and a lot easier than doing it when people are furious. For the whole "
     "sequence, see Diana Leafe Christian’s [*Creating a Life Together*](" + CALT + "): First you get the vision, then "
     "you get the members, then you pool the major resources, and lastly you get the land.",
     'emu-b e04-emuA',
     ['"It’s best to set" -> "You should set" (published: an instruction; round r4\'s stance check on "best written")',
      '"It’s not that romantic, but it’s a lot easier than doing it when people are angry." -> "It’s not that '
      'romantic, but it’s protective, and a lot easier than doing it when people are furious." (published: '
      'protective; furious)', 'link and italics back on Creating a Life Together',
      '"then you get the people" -> "then you get the members" (published: membership)'])

head('## From Visitor to Member—Slowly')
para('H4-P1', v6p('When [The Farm]'), 'v6, unchanged (read Human alone and with its heading, 288g)', [])
para('H4-P2', "There’s some correspondence first. Did they read the materials? Do they get the basic idea of why this "
     "community is here? Are they at least starting to do the practices? It’s better to just find out that way than "
     "after you spend six months together, right?",
     'emu-b e05-emuB (first paragraph)',
     ['cut "Usually" (published: correspond first, a step, not a custom)', '"the stuff" -> "the materials" (published)',
      '"why this is thing is here" -> "why this community is here"', '"do the thing" -> "do the practices" (published)',
      '"half a year" -> "six months" (published)'])
para('H4-P3', "The short visit: If you go for a week or two and just participate in normal life, well, most people can be "
     "charming for two weeks, so if that's all you do, congratulations, you've established that they can be charming "
     "for two weeks. \U0001F605",
     'emu-d g01-emuA (first paragraph; from the published short and long visit)',
     ['"The short version:" -> "The short visit:" (the published stage)'])
para('H4-P4', "The long visit: If you're not around long enough to actually experience any inconvenience or conflict with "
     "the person in question, then you're not going to learn very much about them. Watch how they react when tired, "
     "corrected, attracted, disappointed, bored, etc. Even [a professional faker](" + FAKER + ") may be able to pull off "
     "an act for a few months if they're really motivated, so time gets you more evidence, not certainty.",
     'emu-d g01-emuA (second paragraph) with the middle sentence from g01-emuB',
     ['"The long version: It depends on how long you stay. If" -> "The long visit: If" (the published stage)',
      'the five states from g01-emuB: "when inconvenienced, corrected, ..." -> "when tired, corrected, ..." (published)',
      'link back on "a professional faker"', '+", so time gets you more evidence, not certainty" (published)'])
para('H4-P5', "Have you thought about these questions: How long will a provisional membership be? What will a "
     "provisional member be responsible for and what are their rights? How will a provisional member's membership be "
     "reviewed? How might a person leave provisional membership? Who will make the decision about a person becoming a "
     "full member? (It shouldn't be the person who recruited them.) What rights will a full member have in terms of the "
     "land, other shared resources, and their voice within the group? What will a member be responsible for over the "
     "long term? (These should be addressed in the agreements you draw up when you are first starting your group.)",
     'emu-b e07-emuA',
     ['"(This should be addressed" -> "(These should be addressed" (published: all of full membership follows the '
      'founding agreements)'])
para('H4-P6', "How do you know? At each stage, always judge people based on their conduct. No matter how good it sounds "
     "when they talk about their spirituality or their therapy, don’t go by that. It’s too easy to go by vibes. "
     "It’s also easy to mistake people just doing what everyone else is doing for safety. Even giving it six months "
     "will not give you enough data to know if someone is a good person.",
     'emu-b e08-emuA (first paragraph)',
     ['"HOW DO YOU KNOW?" -> "How do you know?"', '"go by that." -> "go by vibes." (published: vibes)',
      '"to go by people just doing what everyone else is doing." -> "to mistake people just doing what everyone else is '
      'doing for safety." (published: mistaking conformity for safety)'])
para('H4-P7', "If someone will have a role in your group that has serious consequences, for example with kids, shared "
     "resources, medicine, vehicles or private records, you want to know how they handle that specific thing. You can do "
     "this by asking if you’ve seen them do this thing before, and asking for references if appropriate. Give people "
     "access to these things in stages and ensure there’s always some way for someone to appeal to a separate "
     "authority if needed.",
     'emu-b e08-emuB (second paragraph)',
     ['+"serious" (published: high-consequence)', '"private information" -> "private records" (published)',
      '"if they are good at that specific thing" -> "how they handle that specific thing" (published: conduct-specific '
      'evidence)', '"or asking for references" -> "and asking for references" (published: both)',
      '"gradually" -> "in stages" (published: staged access)'])
para('H4-P8', "Do stuff together prior to making them provisional members. Can you actually make a decision as a group? "
     "Can you actually work together to get something done (an ordinary work or shared-resource task will do)? Can you "
     "even process a small conflict afterwards? Do a trial run like that before people have to sell their houses to "
     "join. It won't show you anyone's soul, but it can show you whether your way of coordinating works.",
     'emu-b e09-emuA',
     ['"get some thing done (getting something done together to share can double duty as a test of this)" -> "get '
      'something done (an ordinary work or shared-resource task will do)" (published)', '"process what didn\'t go well '
      'afterwards" -> "process a small conflict afterwards" (published)', '+"like that"',
      '+"It won\'t show you anyone\'s soul, but it can show you whether your way of coordinating works." (published)'])
para('H4-P9', "Do visitors, volunteers, workers, renters and interns at a commune need some rights even if they're not "
     "\"in\" the commune politically? When decisions really affect their pay or use of resources, they need clear terms "
     "and a way to be heard, and those decisions have to be open to review. Also when decisions really affect their "
     "schedule, safety, housing, records, discipline, etc. Equality isn't just for members, or else there's a risk of "
     "creating servant classes from commune to commune.",
     'emu-d g03-emuA (first sentence) and g04-emuB (the rest)',
     ['g03-emuA: "visitors and people who volunteer to work or who work, rent, or intern at a commune" -> "visitors, '
      'volunteers, workers, renters and interns at a commune" (published)',
      'g04-emuB: "Unless somebody joining a commune is joining its political party, and wants to be part of its political '
      'process, visitors, volunteers, workers, renters, interns, etc. need some basic rights when decisions really '
      'affect their pay or use of resources." -> "When decisions really affect their pay or use of resources, they need '
      'clear terms and a way to be heard, and those decisions have to be open to review." (published remedy; round r4\'s '
      'trace: has to be open to review)', '"record," -> "records,"'])

head('## When Somebody Has to Go')
para('H5-P1', "Even in a safe community it’s ok to kick people out if they’re a serious or general danger. If "
     "someone won’t follow basic rules and boundaries, and won’t stop, and/or is just not someone people can live "
     "with, it’s okay to eject them. If the community feels like they can do restorative work with them in a "
     "reasonable amount of time that’s cool, but if they are a danger to the community, the community doesn’t have "
     "to provide them treatment.",
     'emu-b e11-emuA',
     ['"safe space community" -> "safe community" (published)', '"they’re serious" -> "they’re a serious"',
      '"restorative justice" -> "restorative work" (published)'])
para('H5-P2', "That said, the power to remove somebody is also one of the easiest powers to abuse. So work out the "
     "process before it's about anyone in particular. What constitutes a reason for immediate protective action, and "
     "who decides on temporary restrictions? How do you preserve the evidence and make sure that people who are involved "
     "in it aren’t participating in the decision? How does the person reply, and appeal the decision, without "
     "endangering others? How do people who are separated get housed, have their records and family connections "
     "protected, and still be able to use common resources or have access to outside funds? When do people reach for "
     "outside help?",
     'emu-b e12-emuA',
     ['"it’s also a lot easier to abuse" -> "the power to remove somebody is also one of the easiest powers to abuse" '
      '(published; his I4: name the power)', '"so coming up with a process ahead of time is probably a good idea." -> '
      'his line "So work out the process before it\'s about anyone in particular." (his answer 13, 2026-10-11)',
      '"What constitutes removing somebody for others’ safety?" -> "What constitutes a reason for immediate protective '
      'action, and who decides on temporary restrictions?" (published)', '"How do document what’s going on" -> "How do '
      'you preserve the evidence" (published)', '"How do people appeal the decision without threatening others?" -> "How '
      'does the person reply, and appeal the decision, without endangering others?" (published)'])
para('H5-P3', "'Outside' doesn't have to be a nation-state. (It's true that I've been kinda assuming that in "
     "[my research](" + RESEARCH + ").) All that's really needed is that there be a competent layer that isn't "
     "reviewing its own conduct. That can be another community, a federation, a professional, a court, a regulatory "
     "agency, an emergency service, or anything else. The Zapatistas have been very important in opening my eyes to the "
     "possibilities of autonomous regional institutions, which can review local power without becoming the state. But "
     "that doesn't mean that they can violate non-waivable individual rights, or that there can't be jurisdiction above "
     "them.",
     'emu-d g06-emuA',
     ['"The \'outside\' doesn\'t have to be a nation." -> "\'Outside\' doesn\'t have to be a nation-state." (published; and three paragraphs opening on "The" failed the linter, B13)', 'link back on "my research"',
      '"a competent layer above the one under review" -> "a competent layer that isn\'t reviewing its own conduct" '
      '(published; "above" put a layer over the community, which his 2026-10-07 position rules out)',
      '"a profession, or anything else" -> "a professional, a court, a regulatory agency, an emergency service, or '
      'anything else" (published list)', '"autonomous regional institutions, whether courts, regulatory agencies, '
      'emergency services, etc." -> "autonomous regional institutions, which can review local power without becoming '
      'the state" (published)'])
para('H5-P4', "Why should a mediator or ombud be chosen beforehand? Because if they are chosen in a crisis, and if the "
     "parties have not met this “neutral stranger” before, they are unlikely to trust them. And remember that "
     "although mediation can help restore good relations, it does not replace the need for evidence and safeguarding "
     "and, if necessary, a ruling. And it does not replace the finality of separation if one party no longer consents "
     "to staying.",
     'emu-b e14-emuA',
     ['"the Mediator or Ombud" -> "a mediator or ombud"', '"have not met them before" -> "have not met this “neutral '
      'stranger” before" (published)', '"if one party no longer wants to live with the other" -> "if one party no '
      'longer consents to staying" (published: when consent is gone; round r4\'s trace on "living together")'])

out, src = [], []
for h, pid, text, source, fixes in P:
    if h:
        out.append(h)
    else:
        out.append(text)
        src.append({'id': pid, 'source': source, 'fixes': fixes})
(HERE / 'v7.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v7-sources.json').write_text(json.dumps(src, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v7.md:', sum(1 for x in P if x[1]), 'paragraphs,', len(re.findall(r'\S+', '\n'.join(out))), 'words')
