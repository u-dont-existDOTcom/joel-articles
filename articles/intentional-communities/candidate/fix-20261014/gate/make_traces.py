"""make_traces.py - the meaning-trace pairs and prompts for this turn's fixes (trace brief, at most four pairs a run).
Each pair: the published sentence(s) for the changed spot, and the rewrite's sentence(s), with context from the candidate.
Run from fix-20261014/gate/."""
import json, pathlib, re

G = pathlib.Path(__file__).resolve().parent
ROOT = G.parents[4]
brief = (ROOT / 'tools/humanization/reviewer/trace_brief.md').read_text(encoding='utf-8')
brief = re.sub(r'<!--.*?-->\n*', '', brief, flags=re.S)

GLOSS = ('(The rewrite explains a name at its first mention on purpose: the author\'s rule is to explain an unfamiliar name '
         'where it first appears. Check that the explanation doesn\'t change what the sentence claims, and list it under ADDED.)')
P = [
 ('S3P4f',
  'Meeting procedure isn’t going to solve every problem, no matter how sophisticated the system of labor and money and decision making may be in a community of the Federation of Egalitarian Communities or any other income-sharing community.',
  'Yet a meeting procedure can’t make two people stop hating each other. It can only determine whose turn it is to speak about the hatred and whether the motion requires a second.',
  'It can’t make it so that two people don’t hate each other. It can only decide whose turn it is to talk about the hatred, and whether a motion about it needs somebody to second it.',
  'Eventually, when people are together long enough, politics will become a way of carrying emotional material that people can’t name.', ''),
 ('S3P10f',
  'Spiritual groups attempt to address the inner life, but because it\'s the inner world being shaped by the outer as a condition of membership, we tend to find both real-world and spiritual power concentrating around whoever defines the path.',
  'The deeper failure is that authority earned in one role can be spent in every other role. A founder may be a gifted teacher. A therapist may genuinely help people. A farmer or business manager may carry much of the economy.',
  'The deeper problem is that somebody who\'s earned authority in one role can use it in all their other roles. The founder who is a good teacher, the therapist who really helps people, the farmer or business manager that actually carries a lot of the economy.',
  'The danger starts when one person has the ability to define the problem, control the information related to the problem, define what the solution is, and make it hard for people to leave or express disagreement.', ''),
 ('S6P8f',
  'How accurate are the fears about the future? I don\'t know exactly. Maybe AI will improve the lot of humanity enormously. Maybe millions of people will lose their jobs to AI. Maybe AI will become the administrative layer between us and nearly everything.',
  'I’d rather build more human independence than wait for certainty. I’d rather have community and discover I didn’t need an exit than need an exit after spending ten years optimizing my feed.',
  'Ok, so on a personal level, it makes more sense to me to focus on cultivating more independence from the technosphere, all the machines and systems modern life runs on, than to wait for certainty. It\'s better to have community and find out I didn\'t need a way out of it than to need one after spending ten years optimizing my social media feed, right?',
  'What connections to the technosphere do you keep, and which do you limit, when you\'re designing a community?',
  GLOSS + ' The section is called "Which Connections to the Technosphere Do You Keep?", and readers had asked "independence from what?" and "an exit from what?".'),
 ('S7P6f',
  'Whatever forms people choose, I do think that housing, security for kids, membership and access to common necessities should not be contingent on a person staying in some agreement with the people they\'re romantically involved with.',
  'ZEGG and Tamera have spent decades experimenting with relationships inside community.',
  'ZEGG, a community near Berlin, and Tamera, another in Portugal, have spent decades experimenting with relationships inside community.',
  'Their answers are not a set of commandments that everyone must follow.', GLOSS),
 ('S8P10f',
  'A friend who reviewed this draft grew up in a Christian commune in Colorado where her father was a pastor. She calls her childhood "a treasure and a burden."',
  'That sentence is more useful than another promotional video of smiling children carrying vegetables.',
  'What she said is more useful than the usual promo video showing kids smiling and carrying vegetables.',
  'Communal Parenting Adds On (the next heading)', '(Earlier in the section the author shares a video his son made; it isn\'t a promotional video.)'),
 ('S8P12f',
  'One of the biggest reasons I think community matters for kids is Jean Liedloff\'s The Continuum Concept.',
  'Her Ye’kuana account is one outsider’s interpretation and may idealize what she saw, but the picture remains powerful:',
  'It\'s one outsider\'s interpretation of the Ye\'kuana, an Indigenous people of the Venezuelan rainforest she lived with, and she may have idealized what she saw, but it\'s still a powerful picture:',
  'the babies are carried along in ordinary adult life, the kids are surrounded by people of several ages and learn by taking part', GLOSS),
 ('S8P20f',
  'I also reject the suburban panic that treats every warm relationship between a child and an unrelated adult as suspicious.',
  'Children benefit from many adults who know them, enjoy them, notice changes, and will act when something is wrong. Fear can destroy that gift without actually preventing abuse.',
  'It\'s good for kids to have a whole bunch of grownups who know them and enjoy them, who would notice when something changes, and who would act when something\'s wrong. When adults panic like that, kids can lose all those grownups, and the panic might not even prevent abuse.',
  'There are several parts to this protection:', ''),
 ('S8P23f',
  'Create a no-secrets rule. No grownup has a right to ask a kid to keep a secret from their mom or another trusted adult, whether it\'s about a gift, a game, a touch, a conversation or a relationship.',
  'Surprises have an ending date. Secrets designed to isolate the child are forbidden.',
  'A surprise isn\'t a secret, because it has an end date. But secrets meant to isolate a kid aren\'t allowed.',
  'Protecting children is the duty of adults, but it requires children to help also.', ''),
 ('S8F10',
  'Make sure kids understand what they say will be taken seriously if they are known to be honest. Don\'t let the teaching turn into interrogation or punishment when they\'re not sure.',
  'A frightened or confused child may tell a story imperfectly and still need protection.',
  'A scared or confused kid may get mixed up telling what happened and still need protection.',
  'Hear the child even when the accused is someone people love.', ''),
 ('S8P26f',
  'Make sure there\'s at least one trusted adult, advocate or reporting route they can reach without going through the community\'s leadership.',
  'In 1984, Vermont authorities seized 112 children during the Island Pond raid, and the court returned them after rejecting the state’s blanket request. State intervention can fail spectacularly.',
  'In 1984, Vermont authorities raided a religious commune in Island Pond and took 112 kids into custody over suspected abuse. A judge sent them all home the same day, because the state couldn\'t name a single specific case. State intervention can fail spectacularly,',
  'and enclosing kids completely in a community can fail too. Kids need more than one world.',
  '(Readers had asked whose children, why they were seized, and what the state asked. The facts come from the sources: the Northeast Kingdom Community Church in Island Pond, Vermont, 22 June 1984; 112 children taken into custody amid allegations of child abuse; Judge Frank Mahady, noting the state\'s inability to name individual cases, ruled the raid unconstitutional, and the children went home that day. List the added facts under ADDED.)'),
 ('S9P2f',
  'The Best Model I’ve Seen: Zapatistas (the heading)',
  'In 2005, a few college friends and I visited Oventik, one of the Zapatista caracoles in Chiapas.',
  'In 2005, a few college buddies and I went down to Oventik, one of the Zapatista caracoles ("snails"), the regional centers that tie their villages together in Chiapas.',
  'We almost died several times getting there.', GLOSS),
 ('S9P18f',
  '(Four paragraphs earlier, in the author\'s own words: "Now, the Zapatistas also don\'t prove my whole money-free economy goal.") In this paragraph: I couldn\'t find a clear chain of somebody having been to the Escuelita, then a new communal institution being set up, and then evidence about how its members and their children actually did over time. Zapatista influence was already spreading abroad before the Escuelita, so if some institution resembles a Zapatista one later, that alone doesn\'t prove the Escuelita was responsible.',
  'I’m borrowing the Zapatistas’ teaching method and replication ambition, not claiming they have already proven my whole model.',
  'I\'m borrowing the Zapatistas\' teaching method and their ambition to replicate.',
  'Sociocracy has a very different history, yet some similar features have emerged there as well:',
  '(The rewrite cuts the closing disclaimer on purpose, because the section already says the Zapatistas don\'t prove the author\'s model. Judge whether a reader of the section still comes away knowing the author isn\'t claiming they proved his model.)'),
 ('S10P9f',
  'Solidarity doesn\'t mean every community is liable for whatever the others owe, and it doesn\'t mean anyone has an unlimited claim on another community\'s labor and stores, or its land and tools.',
  'And when two principles collide, don’t preserve only the final rule. Keep the hard case:',
  'Limits like those come from two principles colliding, solidarity and each community\'s claim on its own labor and stores. Whenever you create or apply a rule where principles collide, don\'t only store the rule. Store the hard case too:',
  'what happened, the principles that actually conflicted, your first judgments, and your final decision and rationale.',
  '(Readers had found "a collision of two principles" abrupt, with no principles named. The new first sentence names the pair in the paragraph before as an example; the advice still covers any collision.)'),
 ('S11P2f',
  'Founderism: The Four Questions (the heading). In every community there was somebody who took the initiative to get it started. Somebody found the land, wrote the first documents, taught the method, recruited the first members, or kept things going when everybody else lost interest.',
  'That contribution creates real influence. Pretending it doesn’t exist only makes the influence harder to examine.',
  'That person ends up with real influence, and pretending they don\'t just makes that influence harder to look at. When that influence goes unchecked, I call it founderism.',
  'I know this personally. Many of the methods discussed in this article were my doing, and I wrote the materials, so it would be very easy for me to become the person who decides whether or not everyone else “understood” them correctly.',
  '(Readers had found the heading\'s word "Founderism" never defined. Later in the section the author writes: "While founderism is a problem in every community, it\'s especially so in communities which form naturally over time". List the definition under ADDED and say whether it fits that later use.)'),
 ('S11P4f',
  'A few things help keep that in check. One is to judge the method by results people can actually see. Are the members flourishing, and are they safe? Can conflicts get resolved? Can people disagree, leave, and later tell a different story about it? Are the kids doing well once they grow up?',
  'does the community remain materially viable; can it correct a bad prediction; can it replace the founder; and, if it is meant to spread, do later projects actually emerge and last?',
  'Is the community still materially viable? When the method gets a prediction wrong, can the community say so and change course? And if it\'s meant to spread, do new projects actually start up and last?',
  'How long a community has lasted, how full it is, whether it reaches consensus and how many members stay aren\'t enough on their own.',
  '(Readers had asked whose prediction. "Can it replace the founder?" is cut here on purpose because three paragraphs later the section asks "Can the community replace the role of the founder?"; judge whether a reader of the section still gets that test.)'),
 ('S11P6f',
  'Allow for parallel implementations. Fork the method. If the community finds a way to alter Hearthwork and get better results, they\'ve taught me something. If every change they make still needs the founder\'s “blessing”, then it\'s not really running in parallel, is it?',
  'Here are the four questions:',
  'The questions so far have been about the method. These four are about the founder:',
  'Can the community respectfully override the founder? Can the community replace the role of the founder? Can the community alter the vision of the founder? Can the community exist without the founder?', ''),
 ('S11P8f',
  'Then follow the practical power. Whose name is on the deed? Who\'s in charge of the housing and the food stores, the vehicles and tools, and any bank account outside the community?',
  'Who keeps the records, sets admissions, chooses reviewers, decides access to children or medicine, and can make a complaint disappear?',
  'Who keeps the records? Who decides who gets admitted, and who picks the people who review the founder? Who controls access to the kids, or to medicine, and who can make a complaint go away?',
  'Remember, it\'s not an override unless it can actually work on the person in question. If the founder selects the person to review the founder, holds the records, has title to the land, and can kick out complainers, then there\'s no way for the community to override the founder,', ''),
 ('S11P9f',
  'Remember, it\'s not an override unless it can actually work on the person in question.',
  'If the founder chooses the reviewer, holds the records, owns the land, and can remove the complainant, the community cannot meaningfully override the founder no matter how many circles it holds.',
  'If the founder selects the person to review the founder, holds the records, has title to the land, and can kick out complainers, then there\'s no way for the community to override the founder, no matter how many meetings it holds.',
  'Also watch for the daily signs of founderism.', '(Readers had found "circles" unexplained in this section.)'),
 ('S11P10f',
  'If the founder selects the person to review the founder, holds the records, has title to the land, and can kick out complainers, then there\'s no way for the community to override the founder, no matter how many meetings it holds.',
  'Also watch the daily signs: the founder becomes more central over time; disagreement is treated as failure;',
  'Also watch for the daily signs of founderism. Increasing focus on the founder over time. Sense that disagreement is failure.',
  'Every bad result is blamed on lack of good implementation.', '(Readers had asked "signs of what?". "Founderism" is defined at the start of the section.)'),
]
runs = [P[i:i + 4] for i in range(0, len(P), 4)]
for n, run in enumerate(runs, 1):
    pairs = ['# Pairs: published sentences and rewrite\n']
    for key, before, pub, new, after, note in run:
        pairs.append('## %s → %sx\n\nCONTEXT BEFORE: %s\n\nPUBLISHED %s:\n%s\n\nREWRITE %sx:\n%s\n\nCONTEXT AFTER: %s\n%s' % (
            key, key, before, key, pub, key, new, after, ('\nNOTE: ' + note + '\n') if note else ''))
    inp = G / ('trace-pairs-T%d.md' % n)
    inp.write_text('\n'.join(pairs), encoding='utf-8')
    prompt = (brief.replace('{what}', 'this turn\'s fixes, run %d' % n).replace('{input}', str(inp))
              .replace('{report}', str(G / ('TRACE-T%d.md' % n))).replace('{words}', '900'))
    (G / ('PROMPT-trace-T%d.txt' % n)).write_text(prompt, encoding='utf-8')
    print('T%d' % n, [p[0] for p in run])
