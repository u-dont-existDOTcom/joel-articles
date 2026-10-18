"""Joel's 48 a and 51 a of 2026-10-17 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt):
- 48 a: section 13's repeat cut (the Zapatistas' power creep, which section 9 says, his) and a tightening pass on its padding
  (the whole-article reader's list, fix-20261017b/faithful/REPORT-FOREST.md [9]), with the bottlenecks anchor back (the cold
  reader's "Bottlenecks in what?", fix-20261017c/DISPOSITIONS-COLD.md; the published "A money-free community still has scarce
  things and bottlenecks."). "Very important!" and "Lots of decisions to make!" stay ("leave those in actually, they are ok").
- 51 a: Emulate's question-answer pairs and stress capitals in sections 13, 15 and 16, "make sure it reads well": the real ones stay
  (questions a reader would ask, checklists, jokes, quotes, his own lines, "PLUS goats", which he likes), the stock ones go or are
  reworked. Every question and capital in the three sections is listed in fix-20261017d/qa-caps-inventory.json, and this script
  stops unless each one is either changed here or kept with a reason (KEPT).
Writes s13/v36.md (from v35), s15/v16.md (from v15), s16/v31.md (from v30) and fix-20261017d/tighten-changes.json.
Run from candidate/: python3 fix-20261017d/make_tighten.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
# (section, where, kind, old, new, why)
CHANGES = [
    ('s13', 'Opening P2', 'tighten', 'and REALLY dealt with it. Not dealt with it by writing out', 'and really dealt with it. Not by writing out',
     '48 and 51: the capitals go (stress the sentence already carries), and the second "dealt with it" of four'),
    ('s13', 'Opening P2', 'cut', ' But really, truly dealt with it. This includes the relational pl/ork', ' Dealing with it for real '
     'includes the relational pl/ork', '48: the third "dealt with it", saying the first again; the next sentence names what "this" was '
     '(the tone check, TONE-tighten.md change 2: "This" would point at the truce)'),
    ('s13', 'Resources P3', 'rework', 'And how will you handle the VISIBILITY of what the community has? There will be bottlenecks, sorry.',
     'And how will you handle the visibility of what the community has? A money-free community still has scarce things and '
     'bottlenecks, sorry.',
     '51: the capitals go; 48: the published anchor back ("A money-free community still has scarce things and bottlenecks."), '
     'for the cold reader\'s "Bottlenecks in what?"'),
    ('s13', 'Visitor to Member P5', 'tighten',
     'Write down your answers to these questions: How long will a provisional membership be? What will a provisional member be '
     'responsible for and what are their rights? How will a provisional member\'s membership be reviewed? How might a person leave '
     'provisional membership? Who will make the decision about a person becoming a full member? (Hint: not the person who recruited '
     'them! 😜) What rights will a full member have in terms of the land, other shared resources, and their voice within the group? '
     'What will a member be responsible for over the long term? (A full member\'s rights and responsibilities should be addressed in '
     'your founding agreements.)',
     'Write down your answers: How long is a provisional membership, and what are a provisional member\'s rights and '
     'responsibilities? How is it reviewed, and how does someone leave it? Who decides on full membership? (Hint: not the person who '
     'recruited them! 😜) And what rights does a full member have to the land, the shared resources and a voice in the group, and '
     'what do they owe over the long term? (Those go in your founding agreements.)',
     '48: the whole-article reader\'s padding (the published\'s 32 words became 105, seven questions); every point the published '
     'and v35 make is still here (the period, rights, responsibilities, review, exit, who decides, his hint, the full member\'s '
     'land, resources, voice and long-term obligations, the founding agreements)'),
    ('s13', 'When Somebody Has to Go P3', 'cut',
     ' But when power had crept up in their own system over the years, it took them a long review to push it back down.', '',
     '48: the repeat of his section 9 ("it had crept up and consolidated itself at higher levels over time")'),
    ('s15', 'Lessons from the Black Tax P7', 'cut', 'Kind of the opposite problem, isn\'t it?', 'Kind of the opposite problem.',
     '51: the tag question; the whole-article reader\'s padding'),
    ('s16', 'Opening P3', 'rework', 'what the group has shown it CAN do', 'what the group has shown it can do',
     '51: the capitals go; "rather than by declaring" already makes the contrast'),
]
# Held back after the march (fix-20261017d/march-r1 and -r2, two readers): each was its paragraph's only break, so the change would
# leave a run of steps (E173). They stay as they are; Joel found them fine on his quick pass ("it looked ok"). The conflict
# paragraph keeps its last question ("Until then, what's it worth?") for the same reason, with the rest of its tightening.
HELD = [
    ('s13', 'Opening P1', 'cut', ' It may sound cheesy, but it\'s true all the same.', '',
     '48: padding the whole-article reader named; a hedge before the point, which the sentence before already makes'),
    ('s13', 'Opening P2', 'cut', ' Until then, what\'s it worth?', '',
     '48 and 51: a question that restates the sentence before it ("until ... whatever agreement you come up with means anything")'),
    ('s13', 'Resources P5', 'cut', 'Honestly? For the nuts and bolts', 'For the nuts and bolts', '51: a stock opener, not a question'),
    ('s13', 'Visitor to Member P9', 'cut', ' Why wouldn\'t they be?', '', '48 and 51: the reader\'s padding; a question the sentence before answers'),
    ('s13', 'When Somebody Has to Go P1', 'cut', ' Yeah, it’s tough. It’s also true.', '', '48: the reader\'s padding'),
    ('s13', 'When Somebody Has to Go P4', 'rework',
     'Also decide on a mediator or ombudsperson in advance. Why bother? People often won\'t trust someone they haven\'t already met, '
     'who comes in during a crisis as a "neutral stranger."',
     'Also decide on a mediator or ombudsperson in advance, because people often won\'t trust someone they haven\'t already met, who '
     'comes in during a crisis as a "neutral stranger."',
     '51: a stock question-answer; the reason now follows the advice, as published ("before the crisis. People who have never met '
     'the neutral stranger ... often do not trust them")'),
    ('s15', 'All is not well in paradise P3', 'rework', 'So which is it? Well, in a way, it\'s both.', 'Both things are true.',
     '51: after his new "No, not quite." the question is already answered; the published words'),
    ('s15', 'All is not well in paradise P7', 'rework',
     '(some of the men even make the dangerous journey by sea to Europe). So what about the families? The ones that used to share '
     'almost everything are now',
     '(some of the men even make the dangerous journey by sea to Europe). And the families that used to share almost everything are '
     'now', '51: a stock question-answer'),
    ('s15', 'Lessons from the Black Tax P9', 'cut', ' Can you believe it?', '',
     '51: a stock question after his own "they won\'t let me pay rent!", which carries the surprise'),
]
# every other question or capital in the three sections, kept, and why
KEPT = {
    's13': {
        'Do you have outside debts to pay?': 'the budget checklist (published: "outside debts or cash runway")',
        'How long will your cash reserves last': 'the checklist, with his "if the community uses them"',
        'What critical skills will you need?': 'the checklist (published: "the few skills whose absence can stop everything")',
        'Have you noticed people often choose': 'a real question to the reader, opening the vacation-rental joke',
        'Who needs a beach?!': 'the quoted visitor', '“Wait, there’s a vaccination policy??': 'the quoted visitor',
        'And you need paperwork for it?!?!”': 'the quoted visitor',
        'Would LGBTQ+ people be able': 'published questions', 'Should children be taught': 'published questions',
        'Are you willing to experiment?': 'reads well, the published value as a question to the reader',
        'how did they handle it?': 'published ("Ask how a recent conflict was handled")',
        'Does that match your values?': 'published ("compare your values")',
        'Who will have title to the land?': 'his "Very important!" answers it; he keeps it',
        'What kind of legal entity': 'a planning question (published: "Choose the legal form")',
        'And how will you handle the visibility': 'a planning question',
        'Did they read the materials?': 'published questions', 'Do they get the basic idea': 'published questions',
        'Are they at least starting': 'published questions', 'right?': 'a tag that reads naturally',
        'Write down your answers': 'the tightened checklist', 'How is it reviewed': 'the tightened checklist',
        'Who decides on full membership?': 'the tightened checklist', 'And what rights does a full member have': 'the tightened checklist',
        'What do they actually do?': 'a real question',
        'Can you actually make a decision as a group?': 'the published tasks as questions to the reader',
        'Can you actually work together': 'the same', 'Can you even process a small conflict': 'the same',
        'What counts as cause for immediate protective action?': 'published, the process checklist',
        'Who decides to put temporary restrictions': 'published', 'Who will make sure all the evidence': 'published',
        'Who will recuse themselves?': 'published', 'How will the person be able to reply': 'published',
        'What protections will there be': 'published', 'When is it time to bring in outside help?': 'published',
        'they HAVE to stay': 'a real stress, the coercion point; reads like speech',
        'Until then, what\'s it worth?': 'held: the conflict paragraph\'s only turn without it (march r1, r2)',
        'Honestly?': 'held: the book line\'s only turn (march r1)',
        'Why wouldn\'t they be?': 'held: the paragraph\'s only turn (march r1)',
        'Why bother?': 'held: the paragraph\'s only turn (march r1)',
    },
    's15': {
        "Don't human beings already do that?": 'a quote', 'But knowing why twelve people': 'a joke ("That\'s graduate school.")',
        'Who needs a workshop called': 'a joke', 'But does this mean I think Sénégal': 'his own line (21:37)',
        'Who stole the sheep?': 'a joke that is the example', 'So why not share in return?': 'the turn of the argument; reads well',
        'How can they get ahead': 'a real question', "Who's that going to be?": 'the question the paragraph poses (his 43 kept it)',
        "And you can't exactly leave all that at the door, can you?": 'reads naturally; the paragraph\'s turn',
        'Would you like people coming to your house': 'a real question to the reader',
        'So which is it?': 'held: the paragraph\'s only turn (march r1); after his rewrite it still recaps the two sides',
        'So what about the families?': 'held: the paragraph\'s only turn (march r1)',
        'Can you believe it?': 'held: the paragraph\'s only turn (march r1)',
    },
    's16': {
        '"First let\'s get land!"': 'quoted founders',
        'PLUS goats': 'he likes it ("i liked "PLUS goats" lol")',
        'etc etc?': 'his kind of "etc etc"; the list\'s turn',
        'So what?': 'the version that passed (his 47.3: "use the version that passed")',
        'So what do you actually do this month?': 'opens the subsection; reads well',
        'Where do you find these people?': 'a real question',
    },
}
SRC = {'s13': (C / 's13' / 'v35.md', C / 's13' / 'v36.md'), 's15': (C / 's15' / 'v15.md', C / 's15' / 'v16.md'),
       's16': (C / 's16' / 'v30.md', C / 's16' / 'v31.md')}

if __name__ == '__main__':
    inv = json.loads((HERE / 'qa-caps-inventory.json').read_text(encoding='utf-8'))
    for s, (src, dst) in SRC.items():
        md = src.read_text(encoding='utf-8')
        for sec, where, kind, old, new, why in CHANGES:
            if sec == s:
                assert md.count(old) == 1, (s, where, old[:60], md.count(old))
                md = md.replace(old, new)
        dst.write_text(md, encoding='utf-8')
        # every inventoried question or capital is changed here or kept with a reason
        loose = []
        plain_new = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', md)
        for r in inv[s]:
            t = r['text']
            changed = t not in plain_new   # the sentence as inventoried is no longer in the section
            kept = any(k in t for k in KEPT[s])
            if not changed and not kept:
                loose.append(t[:90])
        assert not loose, (s, loose)
        print(dst.name, 'written; every question and capital accounted for:', len(inv[s]))
    (HERE / 'tighten-changes.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
