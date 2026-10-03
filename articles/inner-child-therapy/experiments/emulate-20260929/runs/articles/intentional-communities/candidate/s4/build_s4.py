"""Section 4 builds (2026-10-02). v1: an Emulate version for every flagged paragraph, with small logged fixes
for meaning; P8 to P10, P13 and P14 (Human in the published check) and P22 (a list) unchanged.
Writes final-vN.json (blocks), section-vN.md (Markdown) and rN/*.txt (plain text for Pangram)."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
O = json.load(open(HERE / 'original-blocks.json', encoding='utf-8'))
E = json.load(open(HERE / 'emu' / 'outputs.json', encoding='utf-8'))
L = {'reparent': 'https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided',
     'somatic': 'https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing',
     'romance': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents',
     'bruderhof': 'https://www.bruderhof.com/intentional-community',
     'twinoaks': 'https://www.twinoaks.org/about-twinoaks-community/about-income-sharing'}
ORDER = list(O)
V = {}
V[1] = dict(O)
V[1].update({
 'P1': "Communities tend to focus on the aspect of their project that was most interesting to the original founders, for example political types getting super into writing by-laws, or spiritual types just meditating all the time, or therapists processing each other, or people who like psychedelics discovering they’re all God together and never getting to the point of deciding who will put their name on the deed.",
 'P2': "I’ve broken the model I propose down into four parts. Obviously the details are complicated, and jealousy, children, money, land, God, and iboga don’t fit neatly into four boxes, but let’s go with it. I’ve written detailed guides on the first three already (free to read, not a sales pitch for a retreat or anything), but this article will be mostly about the fourth.",
 'P3': "In a nutshell, there's a difference between working together just to provide food/housing/logistics, etc., and working together to support each other in an internal practice. Why would we commit our whole lives to each other if the only thing we have is the need to take care of property? When we're all trying to help each other heal, to be less run by fear, etc, then the hard parts mean something, and it makes sense to bind our lives together. And when we take on the purpose of an outward *escuelita* and federation, then we have even more reason to do so, because we're not only protecting each other, but helping others build as well.",
 'P4': "Nothing suppressed, everything processed. Each of us is the authority on our own practice, and the community is the container. Things stay fluid and organic, and don't freeze into doctrine.",
 'P5': "These are just rough categories that bleed into one another. In practice, one move in a jealousy situation might also affect how the community governs itself, and how it shares resources can turn into a psychological issue. Or, the way a community uses medicine may create status, or the way it raises children may expose values the founders never talked about. I mostly break them out like this to help see what a community is missing, not because living in a community fits neatly into categories.",
 'P6': "Also, a note on agreements: a community needs some stable agreements that they're not constantly tweaking and revising. But these agreements need to stay open to lived experience.",
 'P7': "In more religious communities, these frozen agreements are called doctrine, but secular communities often make their own kind of doctrine, usually in the form of “the process.”",
 'P11': O['P11'].rsplit(' The child receives', 1)[0] + " The child gets love, protection and guidance, and enough freedom that s/he stays alive inside you.",
 'P12': "Then there’s [somatic regulation](%s), because you can make a great decision in your head and your body can still say no." % L['somatic'],
 'P15': "This means that the capacity to help people is in the community as a whole, not in a single professional, guru, or emotionally essential founder.",
 'P16': "But the people I go to for care shouldn’t, as a result of the care relationship, hold authority over the rest of my life: my membership, work, housing, children, medicine, or the evidence in a dispute about any of them. If they did, the relationship of care would become a relationship of authority, and the supposedly “horizontal” relationship of mutual assistance between peers would once again become vertical.",
 'P17': "On the flip side, there are some things that are not in the purview of peer competence. It’s important to know when to call for outside or expert help.",
 'P18': "It is best to deal with jealousy and conflict when it is still a peer thing, before it gets dragged up to the level of minutes and agendas, and the like.",
 'P19': "On a different note, there will be dyads… no matter if it is in the founding document or not, romance is gonna happen, and my [Romance Guide](%s) covers the basics." % L['romance'],
 'P20': "Doing serious plant medicines carefully with peer guidance without exalting any one person as a special shaman.",
 'P21': "This doesn't mean it can be done without structure and precautions. People still need to be screened, there should be sober sitters present, emergency plans, integration, boundaries, etc., all in place before the first ceremony. Yes, it would be pure to have a group of people all get altered and decide the rules together in that state, but I don't recommend it.",
 'P23': "I imagine that in the long run these communities would move to a situation with less and less money. I see three stages:",
 'P24': "First, no one buys from anyone else in the community to meet their basic needs (food, housing, care, tools, education, transport), but each person may work outside the community and bring in money. However, if they do work outside, they contribute an agreed upon amount of their income to the community. This is probably the most realistic way to get started.",
 'P25': "Later, all wages and other income earned by the members from work outside the community, or from business inside the community, will be paid into the common purse of the community. No member will be permitted to accumulate private wealth while a member of the community. Some version of this is how things have been done in the [Bruderhof](%s) community for generations, and my father lived there for 17 years. It is also done, in a somewhat different way, at [Twin Oaks](%s), and a number of other income-sharing communities. So a common purse isn’t just a theory." % (L['bruderhof'], L['twinoaks']),
 'P26': "Eventually, I'd like to see a point where even outside of the community, no money is used. People would meet their needs directly, or through exchange (be it trade, gift, work, obligation, or whatever). I don't know of any modern community that has gone this far, and in fact, it may be impossible because of government requirements like taxes on land. Perhaps the end point here is a community that is nearly entirely moneyless, but has a small collective cash boundary on the outside.",
 'P27': "None of this does away with scarcity or economic power. There are lots of areas where such power can be wielded: access to food storage, housing, tools, land, medicine, transportation, and the outside world’s currency, to name a few. Even in a moneyless community, someone can control what's scarce. What are the policies for distribution of these things? What are the expectations for members? What happens when someone wants to leave?",
 'P28': "These are less exciting topics to discuss spiritually. It’s rare that someone will come back from an ecstatic vision with news of how to revamp the community’s policies on provisional members, or how to divvy up assets with a departing member, or how to prevent one founder from having control over the land, or what to do when a child reports something serious.",
 'P29': "No amount of beautiful land can make up for one person having the final say over it. No amount of peer counseling can make up for letting people in faster than the group can support them. No amount of medicine can make up for an exit agreement that was never written.",
 'P30': "The first three parts are about the community’s inner life, and the container is the stable place where that work can happen.",
 'P31': "If one of them gets skipped, it will need to be dealt with eventually, usually at high stress, after the group has invested land, labor, and other resources and everyone has an opinion on how things should be.",
})
SRC1 = {'P1': 'e1-emuA', 'P2': 'e1-emuB', 'P3': 'e2-emuB', 'P4': 'e2-emuA + B (the principle\'s name kept)', 'P5': 'e3-emuB',
        'P6': 'e3-emuA', 'P7': 'e3-emuB', 'P11': 'published, last sentence new (both Emulate versions dropped it)',
        'P12': 'new (both Emulate versions made it a list item)', 'P15': 'e5-emuB', 'P16': 'e5-emuA', 'P17': 'e6-emuA',
        'P18': 'e6-emuB', 'P19': 'e6-emuB', 'P20': 'e7-emuA', 'P21': 'e7-emuA', 'P23': 'e8-emuA', 'P24': 'e8-emuA',
        'P25': 'e9-emuB', 'P26': 'e10-emuA + B', 'P27': 'e11-emuB', 'P28': 'e11-emuB', 'P29': 'e12-emuA',
        'P30': 'new (both Emulate versions reversed it)', 'P31': 'e12-emuB'}

V[2] = dict(V[1])
V[2].update({
 'P3': "In a nutshell, there's a difference between working together just to provide food/housing/logistics, etc., and working together to support each other in an internal practice. Why would we commit our whole lives to each other if the only thing we have is the need to take care of property? When we're all helping each other heal and be less run by fear, etc, then the hard parts mean something, and it makes sense to bind our lives together. And when we take on the purpose of an outward *escuelita* and federation, then we have even more reason to do so, because we're not only protecting each other, but helping others build as well.",
 'P4': "Nothing suppressed, everything processed. Each of us keeps authority over our own practice, and the community is the container. The answers stay fluid and organic, and don't freeze into doctrine.",
 'P5': "The four parts are just rough categories that bleed into one another. In practice, a jealousy situation can turn into a question of how the community governs itself. Who controls the shared resources can turn into a psychological issue. And the way a community uses plant medicine may create status, or the way it raises children may expose values the founders never talked about. I break them out like this to help see what a community has neglected, not because living in a community fits neatly into categories.",
 'P6': "Also, a note on agreements: a community needs some stable agreements that they're not tweaking and revising every time somebody has a revelation in breathwork. But these agreements need to stay open to lived experience.",
 'P7': "When agreements freeze, more religious communities may call that doctrine, but secular communities often make their own kind of doctrine too, usually in the form of “the process.”",
 'P12': "Then there’s [somatic regulation](%s), because you can make a great decision in your head while your body is still against it, and you may not even notice." % L['somatic'],
 'P16': "But the people I go to for care shouldn’t, as a result of the care relationship, hold authority over my membership, work, housing, children, medicine, or the evidence in a dispute about any of them. If they did, the relationship of care would become a relationship of authority, and the horizontal relationship of mutual assistance between peers would once again become vertical.",
 'P17': "Also, there are some things that are not in the purview of peer competence. It’s important to know when to call for outside or expert help.",
 'P18': "It is best to deal with jealousy and conflict while it's still between the people involved, before it gets minute-ized and agenda-ized to death.",
 'P19': "On a different note, there will be dyads… no matter if it is in the founding document or not, and even if everyone claims to be above it, romance is gonna happen, and my [Romance Guide](%s) covers it." % L['romance'],
 'P21': "This doesn't mean it can be done without structure and precautions. People still need to be screened, and there need to be sober sitters, emergency plans, integration and clear boundaries, all in place before the first ceremony. Yes, it would be pure collective learning to have several people get altered and decide the rules together in that state, but I don't recommend it.",
 'P23': "In the long run, I'd like to see communities like these use less and less money. I see three stages:",
 'P24': "First, no one buys from anyone else in the community to meet their basic needs (food, housing, care, tools, education, transport), but each person may work outside the community and keep what they earn. However, if they do work outside, they contribute an agreed upon amount of their income to the community. This is probably the most realistic way to get started.",
 'P25': "Later, all wages and other income earned by the members from work outside the community, or from business inside the community, will be paid into the common purse of the community. No member accumulates private wealth while a member of the community. Some version of this is how things have been done in the [Bruderhof](%s) community for generations, and my father lived there for 17 years. It is also done, in a somewhat different way, at [Twin Oaks](%s), and a number of other income-sharing communities. So a common purse isn’t just a theory." % (L['bruderhof'], L['twinoaks']),
 'P26': "Eventually, the community would also stop using money outside. People would meet their needs directly, or through exchange (be it trade, gift, work, obligation, or whatever). I don't know of any modern community that has gone this far, and in fact, it may be impossible because of government requirements like taxes on land. Perhaps the end point here is a community that is nearly entirely moneyless, but has a small collective cash boundary on the outside.",
 'P27': "None of this does away with scarcity or economic power. There are lots of areas where such power can be wielded: access to food storage, housing, tools, land, medicine, transportation, and the outside world’s currency, to name a few. Even in a moneyless community, someone can control what's scarce. What are the policies for distribution of these things? What do members owe one another? What happens when someone wants to leave?",
 'P28': "These are less exciting topics to discuss spiritually. Nobody will come back from an ecstatic vision with news of how to revamp the community’s policies on provisional members, or how to divvy up assets with a departing member, or how to prevent one founder from having control over the land, or what to do when a child reports something serious.",
})
SRC2 = dict(SRC1)

V[3] = dict(V[2])
V[3].update({
 'P3': V[2]['P3'].replace("And when we take on the purpose of an outward *escuelita* and federation, then we have even more reason to do so,", "And the outward *escuelita* and federation purpose gives us even more reason to do so,"),
 'P4': "Nothing suppressed, everything processed. Each of us keeps authority over our own practice, and the community is the container. Whatever answers we find stay fluid and organic, and don't freeze into doctrine.",
 'P5': V[2]['P5'].replace("The four parts are just rough categories that bleed into one another.", "The four parts are rough categories that bleed into one another almost right away."),
 'P6': V[2]['P6'].replace("a community needs some stable agreements", "a community does need some stable agreements"),
 'P7': V[2]['P7'].replace("more religious communities may call", "religious communities may call"),
 'P16': V[2]['P16'].replace("and the horizontal relationship of mutual assistance between peers would once again become vertical.", "and the horizontal relationship of mutual assistance between peers would turn into just another hierarchy."),
 'P19': "On a different note, there will be dyads… whether the founding document mentions romance or pretends everyone is above it, romance is gonna happen, and my [Romance Guide](%s) covers it." % L['romance'],
 'P21': "This doesn't mean it can be done without structure and precautions. People need to be screened, and sober sitters, emergency plans, integration and clear boundaries all need to be in place, before the first ceremony. Yes, it would be pure collective learning to work out the rules while several people are altered, but I don't recommend it.",
 'P24': V[2]['P24'].replace("an agreed upon amount of their income", "an agreed upon share of their income"),
 'P26': V[2]['P26'].replace("I don't know of any modern community that has gone this far,", "I couldn't find a well-documented modern community that has gone this far,").replace("Perhaps the end point here is", "So perhaps the practical end point here is"),
 'P27': V[2]['P27'].replace("What are the policies for distribution of these things?", "Who decides how these things are distributed?"),
 'P28': V[2]['P28'].replace("Nobody will come back from an ecstatic vision", "Nobody comes back from an ecstatic vision"),
 'P29': V[2]['P29'].replace("can make up for one person having the final say over it.", "can make up for ownership that gives one person the final say."),
 'P31': "If one of them gets skipped, it will need to be dealt with eventually, at high stress, usually after the group has invested land, labor, or other resources and everyone has an opinion on how things should be.",
})
for k in ('P3', 'P5', 'P6', 'P7', 'P16', 'P24', 'P26', 'P27', 'P28', 'P29'):
    assert V[3][k] != V[2][k], k
SRC3 = dict(SRC1)

V[4] = dict(V[3])
V[4].update({
 'P5': "I know that the four parts will often be interconnected. Two people get jealous, and suddenly it's a governance question. Somebody ends up controlling the shared land or tools, and now it's a psychological issue. The medicine work can make some people more important than others, and raising children brings out values the founders never talked about. So it all bleeds together, but I find it useful to compartmentalize to some extent, to make sure no area gets overlooked when I'm thinking about how a community might function.",
 'P11': O['P11'].rsplit(' The adult reparents.', 1)[0] + " It’s your inner adult that reparents your inner child, not the other way around, and the child gets love, protection, guidance, and enough freedom to stay alive inside you.",
 'P12': "Then there’s [somatic regulation](%s), for when you've made a great decision in your head and your nervous system still hasn't signed off on it." % L['somatic'],
 'P15': "This means that the capacity to help people is in the community as a whole, not in a single professional or guru, or a founder everybody leans on emotionally.",
 'P16': "But the people I go to for care shouldn’t, as a result of the care relationship, hold authority over my membership, work, housing, children, medicine, or the evidence in a dispute about any of them. If the listener gets that kind of power, it becomes just another step in the hierarchy, and stops being peer care.",
 'P17': "Also, some things are beyond what peers can handle, and it's important to know when to call in outside or expert help.",
 'P29': "You can have beautiful land and still be in trouble if the deed gives one person the final say. You can have great peer counseling and still get swamped if the group lets people in faster than it can support them. And no amount of medicine makes up for an exit agreement that was never written.",
})
SRC4 = dict(SRC1)
SRC4.update({'P5': 'e13-emuB, with the four examples back, one to a sentence', 'P11': 'published first sentence; then e15-emuA', 'P12': 'new', 'P15': 'e5-emuB', 'P16': 'e5-emuA, last sentence from e5-emuB', 'P17': 'new, from e6-emuA', 'P29': 'new (all four Emulate versions were a three-part "No amount of" or "It doesn\'t matter" run)'})
# a proposal for Joel, not in v4: P13's last sentence (his published text, Human in the baseline)
P13J = O['P13'].replace("A living community should relate to its own teachings the same way: devoted enough to practice them and secure enough to disagree.",
                        "A living community should treat its own teachings the same way, practicing them with devotion while still feeling secure enough to disagree.")
assert P13J != O['P13']

V[5] = dict(V[4])
V[5].update({
 'P5': "There is going to be bleed through between these four “categories” – e.g. how people deal with jealousy is going to be intertwined with how people run the community, how people use common things, how people parent, how people deal with medicine etc. But I do think they can be broken up like this for some degree of analysis so that people can see which “boxes” they are neglecting.",
 'P15': "The idea is that the capacity to be there for people when they need help isn’t located in one professional or guru, or the founder of the group that everyone emotionally depends on, but in the community as a whole.",
 'P16': "Another thing is that the person you’re working with shouldn’t get power, just from that, over whether or not you can be a member of the group, whether or not you can work for the group, whether or not you can live there, what happens with your children, whether or not you can take part in the medicine work, whether or not you’re believed in a dispute, etc. Giving someone the job of taking care of people emotionally and giving them administrative power is just creating a new hierarchy.",
 'P17': "Another thing is knowing what kinds of things to refer to outside or expert assistance for.",
 'P18': "And another is to deal with jealousy and conflict while it's still between the people involved, before it gets put on the agenda (generally at the bottom of the agenda).",
 'P19': "Also, read my [Romance Guide](%s), because no matter how much your founding document says that you’re all beyond romance, you’re still gonna have dyads." % L['romance'],
 'P29': "But no amount of gorgeous land will make up for the mess that is created when one person owns the land and has the final say about what will happen on it. And when members come on board faster than the group can support them, all the peer counseling in the world won't make up for it, any more than medicine makes up for the lack of a written exit agreement.",
 'P30': "The first three parts are the inside of the container, and this part is the container itself.",
})
SRC5 = dict(SRC4)
SRC5.update({'P5': 'e19-emuB', 'P15': 'e17-emuA', 'P16': 'e17-emuA (and e17-emuB\'s "believed")', 'P17': 'e17-emuA', 'P18': 'e17-emuA', 'P19': 'e17-emuA', 'P29': 'e20-emuA, its run broken', 'P30': 'e20-emuB'})
P29Y = "Gorgeous land doesn't help when one person owns it and has the final say. Peer counseling can't keep up when members come on board faster than the group can support them. And no ceremony is going to write the exit agreement nobody wrote."

# v6: Joel's edits of 2026-10-02 21:16 (his exact characters; the links put back on his link words)
V[6] = dict(V[5])
V[6].update({
 'P5': "These categories leak into one another almost immediately. Governance can end up slyly incorporating personal tensions like jealousy. Those who have positions with more control of shared resources will automatically be affected by that psychologically (power corrupts, as they say). Those who know medicine tend to have another type of god complex since they may make life or death decisions for people routinely. How folks choose to raise children can expose values the founders never discussed. And myriad other categories arise, of course.",
 'P6': "Also, a note on agreements: a community does need some stable agreements that they're not tweaking and revising every time somebody has a revelation in breathwork. But these agreements need to stay open to lived experience.",
 'P7': "When agreements get frozen, religious communities tend to call the frozen version doctrine. Secular communities on the other hand often call it “the process,” which can become just as sacred.",
 'P11': "[Inner-child reparenting](%s) means learning to identify as the best inner adult, which is comprised of the three inner adult roles: Nurturer, Protector, and Guide. The newly developed adult reparents their newly recognized inner child. The child receives all that love, protection, and guidance that you give it, and in this process actually gains more freedom to remain alive inside you." % L['reparent'],
 'P12': "And it's built on [somatic regulation](%s) first. Listening to the body's feelings before making a decision with the mind. And that actually symbolizes the adult/child relationship to me in some way as well." % L['somatic'],
 'P13': "My contemplative practice is grounded in the early [Buddhist suttas](https://suttacentral.net/), with a critical reading. Most are treasure, while some are obviously late additions (sometimes to the point of real absurdity). A living community should relate to its own teachings in that same critical manner while still devoted to following they've decided on so far.",
 'P26': "Eventually, the community would also stop using money outside. People would meet their needs directly, or through exchange (be it trade, gift, work, obligation, or whatever). I couldn't find a well-documented modern community that has gone this far, and in fact, it may be impractical in some locations because of government requirements like taxes on land. So perhaps the practical end point here is a community that is nearly entirely moneyless, but has a small collective cash boundary on the outside.",
 'P28': "These are less exciting topics to discuss spiritually. It's rare to see someone come back from an ecstatic vision with news of how to revamp the community’s policies on provisional members, or how to divvy up assets with a departing member, or how to prevent one founder from having control over the land, or what to do when a child reports something serious. And if they do, it's often still something that needs a sober thinking-through.",
 'P29': "But no amount of gorgeous land will make up for the mess that is created when one person owns the land or has the final say about what will happen on it. And when members come on board faster than the group can support them, all the peer counseling in the world won't make up for it, any more than medicine makes up for the lack of a written exit agreement.",
})
assert V[6]['P6'] == V[5]['P6']
SRC6 = dict(SRC5)
SRC6.update({k: "Joel's (2026-10-02 21:16)" for k in ('P5', 'P6', 'P7', 'P11', 'P12', 'P13', 'P26', 'P28', 'P29')})
P13W = V[6]['P13'].replace("while still devoted to following they've decided on so far.", "while still devoted to following what they've decided on so far.")
P5F = V[6]['P5'].replace("These categories leak", "These four categories leak")
assert P13W != V[6]['P13'] and P5F != V[6]['P5']

# v7: the run P21 to P24 from one Emulate call (e21), after the v6 section flagged P21's second sentence to P24's
# first; P16 and P17 fixed for the v6 stance check, trace and cold read
V[7] = dict(V[6])
V[7].update({
 'P16': "Another thing is that the person listening to you shouldn’t get power, just from that, over whether or not you can be a member of the group, whether or not you can work for the group, whether or not you can live there, what happens with your children, whether or not you can take part in the medicine work, whether or not you’re believed in a dispute, etc. Letting someone turn what they learned while caring for you into administrative power over you is just creating a new hierarchy.",
 'P17': "Another thing is knowing which problems are beyond what peers can handle and need outside or expert help.",
 'P21': "This doesn’t mean that a peer-led ceremony should be done without structure. Things like screening participants, making sure the sitters are sober, having a plan for dealing with emergencies, planning for integration, and other rules and boundaries need to be dealt with beforehand. While there may be some pure learning that could come from having several altered members figure out what rules and boundaries are needed on the spot, it’s not something I recommend.",
 'P22': "Membership, land, resources, governance, children, leaving, etc.",
 'P23': "I’m personally moving towards communities with less and less money involved. I think this will happen in three stages.",
 'P24': "First there will be no money exchanged between members for basic community functions like food, housing, care, tools, education, transport etc. Members might have outside jobs and bring their income in (some agreed share of it). This is probably a good place to start if someone wants to create a community now and have it be realistic.",
})
SRC7 = dict(SRC6)
SRC7.update({'P16': 'e17-emuA, its last sentence rebuilt', 'P17': 'e17-emuA, fixed', 'P21': 'e21-emuB (its subject from e21-emuA)', 'P22': 'e21 (both versions)', 'P23': 'e21-emuA', 'P24': 'e21-emuA, its last sentence from e21-emuB'})
P5FP = V[6]['P5'].replace("These categories leak", "These four categories leak").replace("Those who know medicine", "Those who know plant medicine")
P28S = V[6]['P28'].replace("And if they do, it's often still something", "And if they do, it's still something")
assert P5FP != V[6]['P5'] and P28S != V[6]['P28']

# v8: P23 and P24 fixed for the v7 trace and stance check (a direction, not a move or a forecast; the stage-one
# share is an obligation, as section 15 says)
V[8] = dict(V[7])
V[8].update({
 'P23': "Personally, I’m aiming for communities with less and less money involved. I think the path there has three stages.",
 'P24': "First there will be no money exchanged between members for basic community functions like food, housing, care, tools, education, transport etc. Members might have outside jobs, and they bring an agreed share of that income in. This is probably a good place to start if someone wants to create a community now and have it be realistic.",
})
SRC8 = dict(SRC7)

# v9: Joel's answers of 2026-10-02 23:49: "These four parts" (the four parts in the diagram under the heading),
# "staying devoted to following what they've decided on so far", and P28 without "often"; P21 stays (he finds
# Emulate's concession better); "plant medicine" declined ("plant medicine isn't the only kind of medicine")
V[9] = dict(V[8])
V[9].update({
 'P5': V[8]['P5'].replace("These categories leak", "These four parts leak"),
 'P13': V[8]['P13'].replace("while still devoted to following they've decided on so far.", "while staying devoted to following what they've decided on so far."),
 'P28': V[8]['P28'].replace("And if they do, it's often still something", "And if they do, it's still something"),
})
for k in ('P5', 'P13', 'P28'):
    assert V[9][k] != V[8][k], k
SRC9 = dict(SRC8)

def build(n, src):
    B = V[n]
    json.dump({'version': n, 'order': ORDER, 'blocks': B, 'source': src}, open(HERE / ('final-v%d.json' % n), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    md = '\n\n'.join(B[k] for k in ORDER) + '\n'
    (HERE / ('section-v%d.md' % n)).write_text(md, encoding='utf-8')
    plain = lambda ks: mdplain.plain('\n\n'.join(B[k] for k in ks if not k.startswith('IMG'))).strip() + '\n'
    return md, plain

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    md, plain = build(n, {1: SRC1, 2: SRC2, 3: SRC3, 4: SRC4, 5: SRC5, 6: SRC6, 7: SRC7, 8: SRC8, 9: SRC9}.get(n, SRC1))
    R = HERE / ('r%d' % n); R.mkdir(exist_ok=True)
    CHECKS = json.load(open(HERE / ('checks-v%d.json' % n))) if (HERE / ('checks-v%d.json' % n)).exists() else {}
    def text_for(ks):
        if isinstance(ks, dict):   # {"v": version, "keys": [...], "P13J": true}
            B = dict(V[ks['v']])
            if ks.get('P13J'): B['P13'] = P13J
            if ks.get('P29Y'): B['P29'] = P29Y
            if ks.get('P13W'): B['P13'] = P13W
            if ks.get('P5F'): B['P5'] = P5F
            if ks.get('P5FP'): B['P5'] = P5FP
            if ks.get('P28S'): B['P28'] = P28S
            return mdplain.plain('\n\n'.join(B[k] for k in ks['keys'] if not k.startswith('IMG'))).strip() + '\n'
        return plain(ks)
    for name, ks in CHECKS.items():
        t = text_for(ks)
        assert '\\n' not in t and '#' not in t, name
        (R / (name + '.txt')).write_text(t, encoding='utf-8'); print(name, len(t.split()))
    print('section words', len(plain(ORDER).split()))
