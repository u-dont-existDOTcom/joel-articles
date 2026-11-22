#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of batch h57b's tries (tools/humanization/sense_receipt.py), with the three
fresh reads (reads/: each read the draft kept as reads/read-text-KEY.txt, the try before the reads' fixes) and each marked
line's fate.

  python3 fill_receipts.py [KEY...]      then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with only the text, its heading and what it is '
        'for (reads/need-%s.txt; the draft it read: reads/read-text-%s.txt)')
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, the ten ways, with the text one sentence a line '
        '(reads/his-%s.txt; the draft it read: reads/read-text-%s.txt)')
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version (reads/fit-%s.txt; the '
       'draft it read: reads/read-text-%s.txt)')


def read_sents(key):
    return M.sentences((HERE / 'reads' / ('read-text-%s.txt' % key)).read_text(encoding='utf-8').strip())


def parse(key):
    rs = read_sents(key)
    S = lambda n: rs[n - 1]
    his = []
    for line in (HERE / 'reads' / ('his-%s.txt' % key)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*([\d, ]+)\s*[—-]', line)
        if m:
            his.append({'s': S(int(m.group(1))), 'difference': m.group(2).strip(), 'n': int(m.group(1))})
    fit = []
    for line in (HERE / 'reads' / ('fit-%s.txt' % key)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            fit.append({'s': S(int(m.group(1))), 'found': ', '.join(found), 'n': int(m.group(1))})
    need = []
    t = (HERE / 'reads' / ('need-%s.txt' % key)).read_text(encoding='utf-8')
    for line in t.split('UNNEEDED:', 1)[-1].splitlines():
        m = re.match(r'\s*-\s*S(\d+):', line)
        if m:
            need.append((int(m.group(1)), S(int(m.group(1)))))
    return his, fit, need


R = {}
R['b05-dmso-overlap'] = dict(
    section="DMSO (Mental Stabilizers That Don't Abort the Trip)",
    reader=("someone sitting with a friend whose psychedelic trip has become too intense, with DMSO and aged ozonated-charcoal "
            "water at hand, deciding which to give"),
    pay=[("they know DMSO and the water do a similar job, so either can be tried, and that one may help where the other "
          "doesn't", "his paragraph before says what DMSO does for him in a bad trip; this sets it beside the water", None),
         ("they know either may work better on a given trip, so they try one and switch to the other if it doesn't help",
          "says how unequally the two work", "Sometimes DMSO works better"),
         ("they know nobody can tell in advance which will help, so they don't wait to pick the right one",
          "says why they can't choose in advance", "why"),
         ("they can give both, one after the other or mixed together, without worrying, when one alone isn't enough",
          "what to do when you can't tell which will help: give both", "taking both"),
         ("they know both are low-risk in his experience, the water the lowest, so they can start with either",
          "the reason no harm comes from giving both", "what I consider")],
    placement=("the DMSO section of Mental Stabilizers That Don't Abort the Trip, after his paragraph on what DMSO does for him "
               "(R39B-DMSO-1), before his evidence paragraphs; its \"It\" is DMSO, named in that paragraph"),
    why_reading="it tells someone choosing between DMSO and the water that the two do a similar job, but not always equally",
    same_point=("B197, in the charcoal-water section, says the two address different kinds of overload, from his ozone story; "
                "this paragraph says what to do about it (try one, switch, or give both), so both stay"),
    keep_need={3: ("they know nobody can tell them in advance which will work, so they try one and switch rather than "
                   "wait to pick"),
               5: ("they know both are low-risk in his experience, the water lowest, so they start with either or give both "
                   "without fear; his judgment, which the guide keeps where it bears on what the reader does (his rule of "
                   "2026-11-08)")},
    keep_his={1: ("\"It\" is DMSO, named in the paragraph before it in the guide; \"equally\" is said by the next sentence, "
                  "which works better when; W060's fidelity keys hold \"overlaps\", \"don't\" and \"equally\""),
              2: "the semicolon pair joined with \"and\", his way 8; what to do with it (try the other) the reader takes from it",
              3: ("a short sentence of his voice; joining it to the one before (the his-fixes read's suggestion) is the next "
                  "try's, the near miss's 20% being spent"),
              4: ("\"them\" is the two just named, and \"taking both or mixing them\" says both ways of giving both; what counts "
                  "as harm is the next sentence's"),
              5: ("his judgment of the two, which tells the reader both are low-risk; \"safety profile\" is the next try's "
                  "one change if this window stays Medium (lesson 19b: one change a window a check)")},
    keep_fit={1: "\"It\" is DMSO, named in the paragraph before it in the guide (the check reads it alone)",
              2: "nobody can tell in advance which will work, and the next sentence says so (\"I don't yet know why\")",
              4: "his experience, said as his (\"In my experience\"); it tells them they may give both",
              5: ("his judgment, said as his (\"what I consider\"); \"safety profile\" is the next try's one change if this "
                  "window stays Medium")},
    questions={'Q1': 'PASS: the comparison first, then what it means for the reader (try one, switch, or give both)',
               'Q2': 'N/A: no instruction; what they may do (give both) is said as his experience',
               'Q3': 'PASS: DMSO and aged ozonated-charcoal water named; "both" is the two',
               'Q4': 'N/A: no term a high-school graduate wouldn\'t know that the section hasn\'t explained',
               'Q5': 'PASS: "but", "Sometimes ... but I don\'t yet know why", "In my experience", the ranking as the reason',
               'Q6': 'PASS: how they compare, that you can\'t predict, that both is fine, why',
               'Q7': 'PASS: each bears on which to give a friend whose trip is too intense',
               'Q8': 'N/A: no list',
               'Q9': 'PASS: the semicolon pairs said as joined clauses'})
R['b06-dmso-side'] = dict(
    section="DMSO: Side effects (Mental Stabilizers That Don't Abort the Trip)",
    reader=("someone about to give a friend DMSO during a hard trip, or take it themselves, checking what side effects to "
            "expect and how to avoid them"),
    pay=[("they know the list that follows is DMSO's side effects", "the label under the DMSO section, after its uses", None),
         ("they know undiluted DMSO usually irritates the skin on the upper body", "the first side effect", "Astringency:"),
         ("they know what to do when it itches: dilute it with water or pure aloe juice", "what to do about the irritation",
          "When the skin itches"),
         ("they know not to leave 100% DMSO on the skin, which can shrivel it for a week", "what leaving it on does",
          "Leaving 100% DMSO on the skin"),
         ("they wet the mouth before taking it by mouth, since it can burn dry mouth tissue", "the mouth, the other place it "
          "burns", "can also"),
         ("they dilute it and sip it slowly when drinking it, so it doesn't nauseate", "the second side effect, nausea",
          "Nausea:"),
         ("they know too much, too late, or too many days of it cuts his sleep", "the third side effect, sleep",
          "Reduced sleep:"),
         ("they take it in the morning and lower the dose if they sleep less, because it builds up", "what to do about the "
          "sleep, his advice", "so it's best taken in the morning"),
         ("they know a study backs his experience (in rats, higher doses made sleep less deep), so the morning advice is worth "
          "following", "the evidence for the sleep effect, with where it was found first (lesson 19a)", "In rats"),
         ("they know some people sleep better on it, when it relieves what kept them awake, so they don't skip it for fear of "
          "insomnia", "the other side of the sleep effect", "Some people sleep better"),
         ("they know a high dose can make them smell of sulfur", "the fourth side effect", "Body odor:"),
         ("they can avoid the smell by taking it in milk, as he does", "what to do about the smell, his experience",
          "when I put it into milk")],
    checked=[{'point': 'the sleep study the line links (Cavas et al. 2005, Toxicology Letters; round 3\'s card W-SLEEP)',
              'found': ('20 rats given one injection at the start of their sleep period, the next 3 hours recorded: the two '
                        'higher doses made sleep lighter, with more light sleep and less deep sleep'),
              'still_needed': 'yes: they know a study backs the sleep effect his line reports, so they take it in the morning',
              'fate': 'changed'}],
    placement=("the DMSO section's side effects list, after the section's uses and evidence and before its interactions; every "
               "item names what it is about first"),
    why_reading="it tells someone about to use DMSO that what follows is what can go wrong, item by item",
    same_point=("none: read the DMSO section from its heading to the next for side effects: only this list gives them; the "
                "section's reduced-sleep advice is said here once (round 39b)"),
    keep_need={1: "they know the list is side effects: the guide's own label, under a heading that names DMSO, not side effects",
               12: ("they know a study backs his sleep line, which is the evidence his advice to take it in the morning "
                    "rests on; the study is the link, which goes with it (gate E380: a citation isn't cut without him)"),
               13: ("they know DMSO can help some people sleep (when it eases what kept them awake), so they don't skip it "
                    "for fear of insomnia")},
    keep_his={10: ("his own experience, in his words (round 39b put his sleep advice here); each of the three causes is short "
                   "and the next sentence says what to do"),
              11: ("his advice from round 39b in his words; \"It\" is DMSO, the item's subject; the threshold is why the "
                   "morning helps"),
              12: "the finding comes after \"In rats\", the limit, first; it backs his advice (morning doses), which is the use",
              13: "they know it can help some people sleep; what kept them awake is whatever it was for that person",
              14: ("the dose differs between people, as the sleep item says of its threshold; the next sentence says what "
                   "to do (milk)"),
              15: "his experience, said as his; it tells them how to avoid the smell"},
    keep_fit={10: ("his experience of DMSO in general, not of a trip; the list is DMSO's side effects whenever it's used, "
                   "and says how to avoid each"),
              11: "his advice (morning doses, less if sleep shortens) holds whenever DMSO is used, a trip or not",
              14: "the dose differs between people; the next sentence says how to avoid the smell"},
    questions={'Q1': 'PASS: each item opens on the side effect it is about, then says what to do',
               'Q2': 'PASS: dilute it, wet your mouth first, sip gradually, take it in the morning, lower the dose: the reader\'s acts',
               'Q3': 'PASS: "the skin", "the DMSO", "your mouth" named where an "it" could have pointed two ways',
               'Q4': 'PASS: "crenate" explained where it is used ("shrivel"); "astringency" is the label the item explains',
               'Q5': 'PASS: "When", "so", "because", "In rats" carry each turn',
               'Q6': 'PASS: skin, mouth, stomach, sleep, smell: the order of the list, each with its fix',
               'Q7': 'PASS: each item bears on using DMSO without harm',
               'Q8': 'PASS: each item is a side effect of DMSO',
               'Q9': 'PASS: one step a sentence; "Sensitivity varies" cut'})
NIACIN_CHECKED = [{'point': 'what the risk of higher or repeated niacin doses is',
                   'found': ('NIH ODS (consumer fact sheet): long-term treatment, especially with extended-release forms of '
                             'nicotinic acid, can cause liver problems; LiverTox (NBK548176): high doses and certain '
                             'formulations linked to acute liver injury, which can be severe; MSD Manual: high-dose niacin can '
                             'cause complications in people with a liver disorder, and hepatotoxicity may be more common with '
                             'sustained-release forms'),
                   'still_needed': 'yes: they know the risk is to the liver, so they don\'t take more or keep taking it, '
                                   'especially if they drink or have liver trouble',
                   'fate': 'changed'}]
NIACIN_PAY = [("they know the flush they'll feel: itchy heat like sunburn", "the first side effect, the one everyone gets",
               "Niacin flush:"),
              ("they know the flush is expected, not an emergency, and that some hate it and some enjoy it",
               "says what the flush means", "The flush is normal"),
              ("they know heartburn can come, with a sensitive stomach or too much at once", "the second side effect",
               "Heartburn"),
              ("they know it can make them drowsy, with poor sleep", "the third side effect", "Drowsiness"),
              ("they don't take higher or repeated doses, which risk liver damage, least of all with liver problems, alcohol "
               "or medications", "the risk after the side effects", "Higher or repeated doses")]
R['b07-niacin-side'] = dict(
    section="A Final Trip Killer: Niacin (a Form of Vitamin B3): Side effects",
    reader=("someone whose friend's trip has to end, without beach morning glory, reading niacin's side effects before giving "
            "it"),
    pay=[("they know the list that follows is niacin's side effects", "the label after the section's dosing paragraph",
          None)] + NIACIN_PAY,
    checked=NIACIN_CHECKED,
    placement=("Niacin's section, after the paragraph on why he includes it and its literature, before the other forms of "
               "vitamin B3"),
    why_reading="it tells someone about to give niacin what it will feel like and when it becomes risky",
    same_point="none: read Niacin's section from its heading to the next for its side effects: only this list gives them",
    keep_need={1: "they know the list is side effects: the guide's own label, under a heading that names niacin"},
    keep_his={2: "a list item's label, which the next sentence explains (\"The flush is normal\")",
              4: "a list item, built as the list's items are; who gets it (a sensitive stomach, too much at once) is said",
              5: "a list item; drowsiness and the poor sleep with it are the two things to expect"},
    keep_fit={4: "how much is too much at once the dose the section gives says; the item says heartburn can come with more",
              5: "the dose the section gives is the measure for higher; what they know of their friend's liver, drinking and medications is theirs"},
    questions={'Q1': 'PASS: each item opens on the side effect it is about',
               'Q2': 'N/A: no instruction but the last, said as the risk',
               'Q3': 'PASS: "the flush" named where "This" could have meant the flush or the heat; the risk named (liver damage)',
               'Q4': 'PASS: "niacin flush" explained in its item ("itchy sunburn-like heat")',
               'Q5': 'PASS: a list; each item its own side effect; "although", "especially with"',
               'Q6': 'PASS: the side effect everyone gets first, the risk last',
               'Q7': 'PASS: each bears on giving niacin to end a trip',
               'Q8': 'PASS: each item is a side effect or risk of niacin',
               'Q9': 'PASS: "sensitive physiology", which no reader can check, out'})
R['b08-niacin-forms'] = dict(
    section="A Final Trip Killer: Niacin (a Form of Vitamin B3): its side effects, then the other forms of vitamin B3",
    reader=("someone whose friend's trip has to end, without beach morning glory, reading about niacin before buying or "
            "giving it"),
    pay=NIACIN_PAY + [
        ("they know other forms of B3 relax people less reliably than niacin, so they get niacin", "after niacin's own "
         "effects, the other forms", "Other forms of vitamin B3"),
        ("they know niacinamide can relax, or can make someone hyperfocused, so it's a gamble during a trip",
         "the first other form", "Niacinamide"),
        ("they don't buy sustained-release niacin or the \"no-flush\" kind, which is useless here", "the forms to avoid",
         "Avoid")],
    checked=NIACIN_CHECKED,
    placement=("Niacin's section: its side effects list, then the paragraph on the other forms of vitamin B3, which closes "
               "the section"),
    why_reading="it tells someone about to give niacin what it will feel like and when it becomes risky",
    same_point="none: read Niacin's section from its heading to the next for the forms of B3: only this paragraph names them",
    keep_need={},
    keep_his={1: "a list item's label, which the next sentence explains (\"The flush is normal\")",
              3: "a list item, built as the list's items are; who gets it (a sensitive stomach, too much at once) is said",
              4: "a list item; drowsiness and the poor sleep with it are the two things to expect",
              6: "now says less reliable than what (than niacin)",
              7: ("which states give which isn't known; the sentence says it can go either way, which is what the reader "
                  "needs to know before giving it during a trip"),
              8: ("the forms to avoid, each named the way a label names it; why sustained-release is avoided (the liver) "
                  "is the next try's change if this window stays below High, within the 20% of a near miss")},
    keep_fit={3: "how much is too much at once the section's dose says; the item says heartburn can come with more",
              4: "drowsiness is what helps end a trip; the item says to expect it with poor sleep after",
              5: "the dose the section gives is the measure for higher; what they know of their friend's liver, drinking and medications is theirs",
              7: "nobody can say in advance which a person will get; the sentence says it can go either way"},
    questions={'Q1': 'PASS: each item opens on the side effect it is about; the paragraph opens on the other forms',
               'Q2': 'PASS: "Avoid" names the forms not to buy',
               'Q3': 'PASS: "the flush" named; "than niacin" said; the forms to avoid named',
               'Q4': 'PASS: the "no-flush" kind named the way a label has it',
               'Q5': 'PASS: "although", "especially with", "than niacin", "depending on"',
               'Q6': 'PASS: niacin\'s effects, then the other forms, then which to avoid',
               'Q7': 'PASS: each bears on giving niacin to end a trip',
               'Q8': 'PASS: side effects in the list, forms in the paragraph',
               'Q9': 'PASS: "sensitive physiology" out; one form a clause'})
R['b10-anchor-lead'] = dict(
    section="Get One Human Anchor",
    reader=("one of a few people with someone having a bad trip, working out who takes the lead and when to call in more "
            "help"),
    pay=[("they pick one calm person to lead", "the paragraph before says why one calm person helps more than a crowd", None),
         ("they know one person's limits, which the next sentence turns into when to add help", "the limit of the one "
          "anchor", "though"),
         ("they bring in a second calm adult or a crisis professional when the anchor is worn out, overwhelmed, or can't keep "
          "everyone from getting hurt, and do it right away if anyone might be violent or hurt themselves",
          "when the limit is reached, and what to do", "If fatigue or logistics")],
    placement=("Get One Human Anchor, after its first paragraph (alone is bad, a crowd is bad) and before the scripts; "
               "\"So\" turns on that paragraph"),
    why_reading="it tells a group with someone in a bad trip to pick one calm person to lead",
    same_point="none: read Get One Human Anchor from its heading to the next for the lead and backup: only this paragraph",
    keep_need={2: ("they know why a second person may be needed, which the next sentence says when; his approved wording "
                   "(OWNER-EDITS r13-anchor-backup)")},
    keep_his={2: ("his approved wording (OWNER-EDITS r13-anchor-backup, round 13); what the anchor can handle only so much "
                  "of is the next sentence's fatigue, logistics and keeping everyone from getting hurt"),
              3: ("each condition is short, and they share one action, bringing in help; \"them\" is now the anchor, named; "
                  "\"get that help\" says what to do right away; W079's keys hold fatigue, logistics and risk")},
    keep_fit={},
    questions={'Q1': 'PASS: who leads first, then when to add help',
               'Q2': 'PASS: have one person lead, bring in one more, get that help right away: the group\'s acts',
               'Q3': 'PASS: "the anchor", "one more calm adult or a crisis professional", "that help" named',
               'Q4': 'N/A: no term a high-school graduate wouldn\'t know',
               'Q5': 'PASS: "So", "though", "If", "and get that help right away if"',
               'Q6': 'PASS: who leads, the limit, when to add help',
               'Q7': 'PASS: each bears on who leads and when to call more help',
               'Q8': 'N/A: no list',
               'Q9': 'PASS: "safe" said as what it means (keeping everyone from getting hurt)'})
R['b12-move-list'] = dict(
    section="Grounding Menu: Choose One or Two Things (Ordinary world)",
    reader="someone with a friend in a hard trip that's starting to ease, looking for one simple grounding thing for them to do",
    pay=[("they offer simple food, like fruit, when the friend can eat", "the first thing from the ordinary world", None),
         ("they go for a slow walk with someone clear-headed, somewhere safe", "the second thing", "none: a new item of the list, which the reader expects after the one before"),
         ("they take the friend outside if it's quiet, with nothing high to fall from, away from roads and water",
          "the third thing", "too"),
         ("they skip hard exercise if the friend is overheating, has chest pain, feels faint or is badly confused",
          "the limit on moving", "none: a new item of the list, which the reader expects after the one before"),
         ("they skip exercise too after a stimulant or an unknown mixture, or with any other medical concern",
          "more cases for the same limit", "Skip exercise too")],
    placement="the Grounding Menu's Ordinary world list, after its Smell and Music parts",
    why_reading="it gives someone with a friend coming down something simple to do: eat",
    same_point="none: read the Grounding Menu from its heading to the next for food, walking and exercise: only this list",
    keep_need={},
    keep_his={2: "the walk's place is said in the next item, with what to avoid; a list item each",
              3: ("each condition is short and says what to avoid; \"water\" here is rivers, lakes and pools outdoors, read "
                  "with roads and heights"),
              4: "each sign is short and the action is one: skip strenuous exercise",
              5: "changed: \"The same goes\" now says what to skip (exercise), and whose concern"},
    keep_fit={4: ("hard exercise is what it limits, not the walk above it; \"badly confused\" is beyond the trip's usual "
                  "confusion, which the word \"badly\" says"),
              5: "changed: \"The same goes\" now says what to skip; an unknown mixture is when they don't know what was taken"},
    questions={'Q1': 'PASS: each item opens on the thing to do or skip',
               'Q2': 'PASS: eat, walk, go outside, skip exercise: the reader\'s acts',
               'Q3': 'PASS: "exercise" named where "The same goes" pointed two ways',
               'Q4': 'N/A: no term a high-school graduate wouldn\'t know',
               'Q5': 'PASS: a list; "too", "if", "Skip exercise too if"',
               'Q6': 'PASS: food, walking, outside, then the limit on exercise',
               'Q7': 'PASS: each bears on what to do with a friend coming down',
               'Q8': 'PASS: each item is an ordinary-world thing to do or skip',
               'Q9': 'PASS: one condition set a sentence'})
R['b13-shadow-def'] = dict(
    section="Shadow Work",
    reader="someone whose trip brought up frightening parts of their mind, starting the guide's shadow work part to understand what happened",
    pay=[("they know shadow work here isn't a sexual practice or indulging dark urges", "the part opens on what it means by "
          "shadow work", None),
         ("they know what it is: bringing loving awareness to the parts of the mind formed in fear, pain and rejection",
          "the definition after what it isn't", "It means"),
         ("they know the main method is inner-child reparenting, giving yourself the parenting you missed", "how it's done",
          "this work"),
         ("they see a negative mind-state as a young part of them waiting for love and protection, not a flaw in their thinking",
          "what reparenting is for", "young parts of you")],
    placement="the first paragraph under the Shadow Work part's heading (round 32's SHADOW-START b)",
    why_reading="it tells someone whose trip brought up frightening parts of their mind what this guide means by shadow work",
    same_point="none: read Shadow Work from its heading to the next for what shadow work is: only this paragraph defines it",
    keep_need={},
    keep_his={1: "his round-32 opening of the part (SHADOW-START), which says what the reader may think it is; his words stay",
              2: "the definition; each word names a feeling the parts were formed in, which the reader may recognize",
              3: "changed: \"it\" now \"this work\", and the term explained where it is used",
              4: ("what reparenting does with those parts; the contrast answers a worry the reader really has (that "
                  "something is wrong with their thinking)")},
    keep_fit={1: "his opening of the part, which names two ideas a reader may have heard (round 32)",
              2: "how to bring loving awareness is what the sections after it teach; this paragraph says what it is",
              3: "changed: the term explained where it is used (giving yourself the parenting you missed)",
              4: "what the parts are waiting for (love, protection, permission) says how to treat them; the sections after it say how"},
    questions={'Q1': 'PASS: what it isn\'t, what it is, how, what for',
               'Q2': 'N/A: a definition, no instruction',
               'Q3': 'PASS: "this work" names what "it" pointed to two ways',
               'Q4': 'PASS: "inner-child reparenting" explained where it is used',
               'Q5': 'PASS: "It means", "is central to this work", "Most negative mind-states"',
               'Q6': 'PASS: what it is first, then how, then what for',
               'Q7': 'PASS: each bears on understanding what happened in their mind',
               'Q8': 'N/A: no list',
               'Q9': 'PASS: one idea a sentence'})
R['b17-opposites'] = dict(
    section="Dealing With Shadow Thoughts",
    reader=("someone who, during or after a trip, keeps having dark thoughts that are the opposite of what they want to feel, "
            "reading this to understand them"),
    pay=[("they have a way to meet the thoughts: let go of the sense of a separate self", "the paragraph before says what "
          "to do with shadow thoughts (notice them, don't attach)", None),
         ("they know where to read more on it, his pamphlet", "a pointer for the practice just named", "this"),
         ("they know he isn't saying you need an opposite to understand anything", "turns to why opposites come up",
          "I am not repeating"),
         ("they know a feeling, lived, doesn't come with its opposite", "the example that shows the claim is wrong",
          "A hated baby"),
         ("they know the mind keeps a concept's two sides together, which is why the opposite thought shows up, and nothing "
          "is wrong with them", "turns on the example with however", "however")],
    placement="Dealing With Shadow Thoughts, after the paragraph on noticing shadow thoughts and before the during-a-trip lines",
    why_reading="it tells someone with frightening opposite thoughts a way to meet them, which the paragraph before began",
    same_point=("B411 and B412, above it, say the opposite becomes visible when we purify the mind; this pair says why (the "
                "mind keeps both sides together), so both stay"),
    keep_need={1: ("they have his practice for meeting the thoughts (let the separate self go), from his own teaching; his "
                   "words, and the pair read High in its check but for the last sentence"),
               2: "they know where to read more on that practice: his pamphlet, his pointer",
               3: "they know what he isn't claiming, so the example after it reads right; his stance, in his words"},
    keep_his={1: "his practice, in his words; the pair read Human High but for the last sentence, which is what changes",
              2: "his pointer to his pamphlet; \"this\" is the practice just named",
              3: "his stance, which answers a worry a reader with frightening opposites may have (that they need the dark to know the light)",
              4: "his example, which shows the claim is wrong in lived feeling",
              5: "changed: \"the two sides\" now \"both\", the love and hate just named, and who keeps them (the mind)"},
    keep_fit={1: "his practice, in his words; how to do it is in his pamphlet, which the next sentence names",
              2: "his pointer to where the practice is taught",
              3: "his stance; it says plainly the claim is one he isn't repeating",
              4: "his example; the next sentence says what it shows"},
    questions={'Q1': 'PASS: the practice, then the claim he isn\'t making, then why opposites come',
               'Q2': 'PASS: relax, unwind, unbind and unweave: his practice',
               'Q3': 'PASS: "both" is the love and hate just named',
               'Q4': 'N/A: his terms (identity illusion, Hermetic) are his teaching\'s, his pamphlet the place they are explained',
               'Q5': 'PASS: "this", "I am not repeating", "however"',
               'Q6': 'PASS: the practice, then why the opposites come',
               'Q7': 'PASS: each bears on understanding the opposite thoughts',
               'Q8': 'N/A: no list',
               'Q9': 'PASS: one idea a sentence'})
R['b19-appendix'] = dict(
    section="Appendix: Additional Resources",
    reader="someone whose crisis is over, looking for more help and learning for themselves or a friend",
    pay=[("they can find other kinds of help than standard mental-health care, at the site named", "the appendix's list, "
          "after its note that the triage app comes first", None),
         ("they can take a free class on learning to be happy and helping others be happy, by its link", "a second resource",
          "none: a new item of the list, which the reader expects after the one before"),
         ("they can watch a monk's guidance on shadow work, in the video below", "a third resource", "none: a new item of the list, which the reader expects after the one before")],
    placement="the Appendix's list, after its note that the triage app comes first in trouble",
    why_reading="it gives someone past the crisis a place to find other kinds of help",
    same_point="none: read the Appendix from its heading to the next for these resources: only this list",
    keep_need={},
    keep_his={1: "the site's own name for what it lists; the link takes them there",
              2: "the class is the link on \"free class\"; what it is about the sentence says",
              3: "the video is right below the list; shadow work is the guide's own subject, defined in its Shadow Work part"},
    keep_fit={},
    questions={'Q1': 'PASS: each item names the resource first',
               'Q2': 'N/A: resources, no instruction',
               'Q3': 'PASS: each resource named',
               'Q4': 'N/A: shadow work is defined in the guide\'s Shadow Work part',
               'Q5': 'PASS: a list; each item its own resource',
               'Q6': 'PASS: help, then learning, then the video below it',
               'Q7': 'PASS: each bears on finding more help after the crisis',
               'Q8': 'PASS: each item is a resource',
               'Q9': 'PASS: "U.C." spelt UC, which Pangram read as a sentence of its own'})


# ---- batch h57c ----
import copy
R['c05-dmso-overlap'] = copy.deepcopy(R['b05-dmso-overlap'])
R['c05-dmso-overlap']['pay'][1] = ("they know either may calm the trip better, so they try one and switch to the charcoal water, "
                                   "or to DMSO, if it doesn't help", "says how unequally the two work",
                                   "Sometimes DMSO calms a trip better")
R['c05-dmso-overlap']['keep_his'] = {
    1: ("\"It\" is DMSO, named in the paragraph before it in the guide; what they overlap in, calming a trip, the next "
        "sentence now says; W060's fidelity keys hold \"overlaps\", \"don't\" and \"equally\""),
    2: "what to do with it (try the other) the reader takes from it; it now says what each does better, calm a trip",
    3: "they know nobody can tell in advance which will work, so they try one and switch",
    4: ("\"them\" is the two just named, and \"taking both or mixing them\" says both ways of giving both; what counts "
        "as harm is the next sentence's"),
    5: ("his judgment of the two, as the guide has it, which tells the reader both are low-risk; its window is the next "
        "try's one change if it stays Medium (lesson 19b)")}
R['c05-dmso-overlap']['keep_fit'] = {
    1: "\"It\" is DMSO, named in the paragraph before it in the guide (the check reads it alone)",
    2: "nobody can tell in advance which will work, and the next sentence says so (\"I don't yet know why\")",
    4: "his experience, said as his (\"In my experience\"); it tells them they may give both",
    5: "his judgment, said as his (\"what I consider\"), as the guide has it; this try changes only the window before it"}
R['c05-dmso-overlap']['keep_need'] = {3: R['b05-dmso-overlap']['keep_need'][3]}
R['c05-dmso-overlap']['questions']['Q3'] = 'PASS: "the charcoal water" named where "the water" could have been plain water'
R['c05-dmso-overlap']['questions']['Q9'] = 'PASS: the first semicolon pair said as joined clauses; the last as the guide has it'

R['c08-niacin-forms'] = copy.deepcopy(R['b08-niacin-forms'])
R['c08-niacin-forms']['pay'][6] = ("they know niacinamide relaxes some people but can make others hyperfocused, depending on "
                                   "the state the person is in, so it's a gamble during a trip", "the first other form",
                                   "Niacinamide")
R['c08-niacin-forms']['keep_need'] = {6: ("they know to get niacin itself rather than another form of B3, which is what the "
                                          "sentence is for; the next two say which forms and why")}
R['c08-niacin-forms']['keep_his'] = {
    1: "a list item's label, which the next sentence explains (\"The flush is normal\"); it read High in its own check (b07)",
    3: "a list item, built as the list's items are; who gets it (a sensitive stomach, too much at once) is said; High in b07",
    4: "a list item; drowsiness and the poor sleep with it are the two things to expect; High in b07",
    5: "the list's risk line as it went in (b07, Human High 57 with its label)",
    6: "now says less reliable than what (than niacin); which forms the next two sentences name",
    7: ("\"they\" is now \"the person\"; which states give which isn't known, and the sentence says it can go either way, "
        "which is what the reader needs before giving it during a trip"),
    8: ("the forms to avoid, each named the way a label names it; why sustained-release is avoided (the liver) is the next "
        "try's change if this window stays below High")}
R['c08-niacin-forms']['keep_fit'] = {
    3: "how much is too much at once the section's dose says; the item says heartburn can come with more",
    4: "poor sleep later is what to expect; the item says so, which is all it needs to",
    5: "the dose the section gives is the measure for higher; what they know of their friend's liver, drinking and medications is theirs",
    7: "nobody can say in advance which a person will get; the sentence says it can go either way",
    8: "the parenthesis names the form meant (inositol hexanicotinate), so niacinamide, named just before, isn't it"}

R['c13-shadow-def'] = copy.deepcopy(R['b13-shadow-def'])
R['c13-shadow-def']['pay'][2] = ("they know the main method of shadow work here is inner-child reparenting, which the guide's "
                                 "link explains", "how it's done", "shadow work")
R['c13-shadow-def']['keep_his'] = {
    1: "his round-32 opening of the part (SHADOW-START), which says what the reader may think it is; it stays as the guide has it",
    2: "the definition; each word names a feeling the parts were formed in, which the reader may recognize",
    3: ("the term is his guide's name, linked to it; explaining it here (b13, \"giving yourself the parenting you missed\") "
        "read worse, its three sentences one Medium window, so this try names only what it is central to"),
    4: ("what reparenting does with those parts; the contrast answers a worry the reader really has (that something is wrong "
        "with their thinking)")}
R['c13-shadow-def']['keep_fit'] = {
    4: ("the young parts are what the sections after it work with; \"most\" says not every one, and the guide's call list "
        "and mental-health support list say when it needs real help")}
R['c13-shadow-def']['questions']['Q3'] = 'PASS: "shadow work" named where "it" could have pointed two ways'
R['c13-shadow-def']['questions']['Q4'] = ('PASS: "inner-child reparenting" is the name of his guide, linked where it is used; '
                                          'explaining it here read worse in b13')

R['c17-opposites'] = copy.deepcopy(R['b17-opposites'])
R['c17-opposites']['pay'][4] = ("they know each idea in the subconscious often comes paired with its opposite, which is why the "
                                "opposite thought shows up, and nothing is wrong with them", "turns on the example with though",
                                "though")
R['c17-opposites']['keep_need'][4] = ("they know a lived feeling doesn't come with its opposite, which the next sentence turns "
                                      "on; his example, in his words")
R['c17-opposites']['keep_his'][5] = ("changed: \"each one\" now \"each idea\", and what happens said: it comes paired with its "
                                     "opposite")
R['c17-opposites']['questions']['Q3'] = 'PASS: "each idea" named where "each one" could have pointed at the babies or the thoughts'


def fill(key):
    r = R[key]
    p = HERE / ('TEST-%s.receipt.json' % key)
    d = json.loads(p.read_text(encoding='utf-8'))
    d['section'], d['reader'] = r['section'], r['reader']
    assert len(d['sentences']) == len(r['pay']), (key, len(d['sentences']), len(r['pay']))
    for s, (pay, fol, link) in zip(d['sentences'], r['pay']):
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link or 'none: a new item of the list, which the reader expects after the one before'
    d['checked'] = r.get('checked', [])
    d['placement'] = r['placement']
    d['opens']['why_reading'] = r['why_reading']
    d['same_point'] = r['same_point']
    his, fit, need = parse(key)
    d['needed'] = {'reader': NEED % (key, key), 'unneeded': [s for n, s in need],
                   'kept': {s: r['keep_need'][n] for n, s in need if n in r['keep_need']}}
    d['his_fixes'] = {'reader': HISF % (key, key), 'marked': [{'s': m['s'], 'difference': m['difference']} for m in his],
                      'kept': {m['s']: r['keep_his'][m['n']] for m in his if m['n'] in r['keep_his']}}
    d['fit'] = {'reader': FIT % (key, key), 'marked': [{'s': m['s'], 'found': m['found']} for m in fit],
                'kept': {m['s']: r['keep_fit'][m['n']] for m in fit if m['n'] in r['keep_fit']}}
    d['questions'] = r['questions']
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
        print('filled', k)
