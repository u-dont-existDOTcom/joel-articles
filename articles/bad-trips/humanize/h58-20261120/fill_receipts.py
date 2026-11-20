#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 50's tries (tools/humanization/sense_receipt.py), with the three
fresh reads (reads/: each read the draft kept as reads/read-text-KEY.txt, the try before the reads' fixes) and each marked
line's fate. Built as h57's fill_receipts.py builds them.

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
R['b01-dmso-side'] = dict(
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
         ("they start with a small amount, since how easily DMSO turns the stomach differs between people",
          "what to do when sipping slowly may not be enough for them", "Sensitivity varies"),
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
    checked=[],
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
    keep_his={8: "changed: \"try less\" (less than what?) now \"try a small amount\", his \"at first\" kept",
              10: ("his own experience, in his words (round 39b put his sleep advice here); each of the three causes is short "
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
               'Q2': ("PASS: dilute it, wet your mouth first, sip gradually, try a small amount at first, take it in the "
                      "morning, lower the dose: the reader's acts"),
               'Q3': 'PASS: "the skin", "the DMSO", "your mouth" named where an "it" could have pointed two ways',
               'Q4': 'PASS: "crenate" explained where it is used ("shrivel"); "astringency" is the label the item explains',
               'Q5': 'PASS: "When", "so", "because", "In rats" carry each turn',
               'Q6': 'PASS: skin, mouth, stomach, sleep, smell: the order of the list, each with its fix',
               'Q7': 'PASS: each item bears on using DMSO without harm',
               'Q8': 'PASS: each item is a side effect of DMSO',
               'Q9': 'PASS: one step a sentence; "Sensitivity varies" said with what to do about it, as he asked'})

R['b02-niacin-side'] = dict(
    section="A Final Trip Killer: Niacin (a Form of Vitamin B3): Side effects",
    reader=("someone whose friend's trip has to end, without beach morning glory, reading niacin's side effects before giving "
            "it"),
    pay=[("they know the list that follows is niacin's side effects", "the label after the section's opening paragraphs",
          None),
         ("they know the flush they'll feel: itchy heat like sunburn", "the first side effect, the one everyone gets",
          "Niacin flush:"),
         ("they know the flush is expected, not an emergency, and that some hate it and some enjoy it",
          "says what the flush means", "The flush is normal"),
         ("they know heartburn can come, with a sensitive stomach or too much at once", "the second side effect",
          "Heartburn"),
         ("they know it can make them drowsy, with poor sleep", "the third side effect", "Drowsiness"),
         ("they don't use sustained-release niacin or keep taking regular niacin through the day, which risk liver damage, "
          "least of all with liver problems, alcohol or medications", "the risk after the side effects",
          "Sustained-release niacin")],
    checked=[{'point': 'where niacin\'s liver risk is: sustained-release niacin, or regular niacin taken through the day',
              'found': ('McKenney et al. 1994, JAMA (PubMed 8309029), randomized and double-blind, the two forms at 500 to '
                        '3,000 mg a day: hepatotoxic effects in 12 of 23 on sustained-release, none on immediate-release. A '
                        '1992 FDA review (in the New York State drug information response on nicotinic acid, 2018) found 6 '
                        'case reports of liver injury on immediate-release niacin, all at 3 g a day or more. Slow release '
                        'sends more niacin down the amidation pathway, whose metabolites are linked to liver toxicity; fast '
                        'release saturates it (the same response) - which is why regular niacin spread through the day can '
                        'act like sustained-release, as he says'),
              'still_needed': ('yes: they know which niacin, and which way of taking it, risks the liver, so they use '
                               'regular niacin, taken at once'),
              'fate': 'changed'}],
    placement=("Niacin's section, after the paragraph on why he includes it and its literature, before the other forms of "
               "vitamin B3"),
    why_reading="it tells someone about to give niacin what it will feel like and when it becomes risky",
    same_point=("B215 says to avoid sustained-release niacin, among the other forms of B3; this line says why (the liver), "
                "and adds regular niacin spread through the day, so both stay"),
    keep_need={1: "they know the list is side effects: the guide's own label, under a heading that names niacin"},
    keep_his={2: "a list item's label, which the next sentence explains (\"The flush is normal\")",
              4: "a list item, built as the list's items are; who gets it (a sensitive stomach, too much at once) is said",
              5: "a list item; drowsiness and the poor sleep with it are the two things to expect",
              6: ("his line (his guide's \"Higher or repeated doses ... especially with liver problems, alcohol, "
                  "medications\") with the risk said where he says it is; naming each medicine and the signs of liver "
                  "trouble is more than he asked, and a near miss's next change is a word or two (lesson 19b)")},
    keep_fit={4: ("the guide gives no niacin dose; the item says heartburn comes with more at once, so they give less at a "
                  "time"),
              5: ("they expect drowsiness without good sleep, during or after; his line, Human High in its check (7ef96156)"),
              6: ("they ask their friend whether they drink, take medicines or have liver trouble, and hold off if so; the "
                  "line names what raises the risk")},
    questions={'Q1': 'PASS: each item opens on the side effect it is about; the last on what carries the risk',
               'Q2': 'N/A: no instruction; the risk said as what carries it',
               'Q3': 'PASS: what carries the risk named: sustained-release niacin, repeated doses through the day',
               'Q4': 'PASS: "niacin flush" explained in its item ("itchy sunburn-like heat"); "sustained-release" as labels say it',
               'Q5': 'PASS: a list; each item its own side effect; "although", "especially with"',
               'Q6': 'PASS: the side effect everyone gets first, the risk last',
               'Q7': 'PASS: each bears on giving niacin to end a trip',
               'Q8': 'PASS: each item is a side effect or risk of niacin',
               'Q9': 'PASS: "Higher" out: regular niacin taken at once is not where the liver risk is'})


# ---- batch h58b ----
def dmso(nausea_pay, keep_his_extra, keep_need, keep_fit, q9, joined=False):
    r = json.loads(json.dumps(R['b01-dmso-side'], ensure_ascii=False))
    pay = r['pay']
    if joined:
        pay[5] = nausea_pay[0]
        del pay[6]
    else:
        pay[6] = nausea_pay[0]
    r['keep_his'] = keep_his_extra
    r['keep_need'] = keep_need
    r['keep_fit'] = keep_fit
    r['questions'] = dict(r['questions'], Q9=q9)
    return r

KEEP_HIS_LINES = {  # the lines of his list as they read Human High in b06 (21a95b3c), by the reads' numbering
    'S10': ("his own experience, in his words (round 39b put his sleep advice here); each of the three causes is short and "
            "the next sentence says what to do"),
    'S11': "his advice from round 39b in his words; \"It\" is DMSO, the item's subject; the threshold is why the morning helps",
    'S12': ("the finding comes after \"In rats\", the limit, first; it backs his advice (morning doses), which is the use; "
            "its link is the study (gate E380)"),
    'S13': "they know it can help some people sleep; what kept them awake is whatever it was for that person",
    'S14': "the dose differs between people, as the sleep item says of its threshold; the next sentence says what to do (milk)",
    'S15': "his experience, said as his; it tells them how to avoid the smell",
}
def renum(d, shift):
    return {int(k[1:]) + shift: v for k, v in d.items()}

R['c01-dmso-side'] = dmso(
    [("they start with less than they planned, since how easily DMSO turns the stomach differs between people",
      "what to do when sipping slowly may not be enough for them, his reason first", "Sensitivity to DMSO varies")],
    {**renum(KEEP_HIS_LINES, 0),
        6: ("\"dry mouth tissue\" is the tissue of a dry mouth, which the same sentence's fix says (\"so wet your mouth "
            "first\"); Human High in b06"),
        7: ("his item as it read Human High in b06; the amounts are the drink's, and the next sentence says how much DMSO to "
            "start with"),
        8: "changed: \"Sensitivity\" said as sensitivity to DMSO, and \"a small amount\" as less than you planned, his \"less\""},
    {1: "they know the list is side effects: the guide's own label, under a heading that names DMSO, not side effects",
     12: ("they know a study backs his sleep line, which is the evidence his advice to take it in the morning rests on; the "
          "study is the link, which goes with it (gate E380: a citation isn't cut without him)"),
     13: ("they know DMSO can help some people sleep (when it eases what kept them awake), so they don't skip it for fear of "
          "insomnia")},
    {8: "changed: \"a small amount\" (no measure) said as less than you planned, the measure they have",
     10: "his experience of DMSO in general, not of a trip; the list says how to avoid each side effect whenever it's used",
     11: "his advice (morning doses, less if sleep shortens) holds whenever DMSO is used, a trip or not",
     14: "the dose differs between people; the next sentence says how to avoid the smell"},
    'PASS: one step a sentence; his "Sensitivity varies" said with what it is to (DMSO) and what to do about it')

R['c02-dmso-side'] = dmso(
    [("they dilute it, sip it slowly and start with less than they planned, since sensitivity varies, so it doesn't "
      "nauseate", "the second side effect, nausea, with his reason last", "Nausea:")],
    {**renum({k: v for k, v in KEEP_HIS_LINES.items() if k != 'S10'}, -1),
        7: ("the join is this try's point: b01's separate short line read Human Medium on its own (fb34d3fb), and his "
            "round-43 versions joined such lines into the sentence they belong to; one act to a clause, with his reason "
            "last"),
        10: ("his advice from round 39b in his words; \"It\" is DMSO, the item's subject; the threshold is why the morning "
             "helps")},
    {1: "they know the list is side effects: the guide's own label, under a heading that names DMSO, not side effects",
     11: ("they know a study backs his sleep line, which is the evidence his advice to take it in the morning rests on; the "
          "study is the link, which goes with it (gate E380: a citation isn't cut without him)"),
     12: ("they know DMSO can help some people sleep (when it eases what kept them awake), so they don't skip it for fear of "
          "insomnia")},
    {9: "his experience of DMSO in general, not of a trip; the list says how to avoid each side effect whenever it's used",
     10: "his advice (morning doses, less if sleep shortens) holds whenever DMSO is used, a trip or not",
     13: "the dose differs between people; the next sentence says how to avoid the smell"},
    'PASS: his line joined to the act it belongs to, its reason last ("since sensitivity varies")', joined=True)

SHADOW_COMMON = dict(
    section="Dealing With Shadow Thoughts",
    reader=("someone tripping who just had a dark thought or feeling about themselves come up, or the friend sitting with "
            "them, reading what to do with it right now"),
    checked=[],
    placement=("the last paragraph of Dealing With Shadow Thoughts, after his six paragraphs on why the opposite shows up "
               "and his \"So relax ...\", before The Joker Poem: the general advice before it, what to do in the moment here"),
    why_reading="it tells someone tripping what to do with a dark thought about themselves, right now",
    same_point=("none: read Dealing With Shadow Thoughts from its heading to the next for what to do during a trip: only this "
                "paragraph says it; his \"So relax ...\" is the general advice, this the steps in the moment"),
    keep_need={},
)
SCRIPT_KEEP = ("the script the guide gives the reader to say, a line each, built the same way on purpose so it can be "
               "repeated; \"It\" is the thought and the feeling it has just named")
ROOM_KEEP = ("his decision on the grounding order (OWNER-EDITS q5-room-first, round 5's Q-5 (a): room before body), word for "
             "word; each word is a heading of the Grounding Menu earlier in the guide, which says what to do with it")
QS = {'Q1': 'PASS: what to do with the thought first, each don\'t with its reason after it',
      'Q2': ('PASS: each instruction is something the reader does (take it as true or not, let it be there, tell the person '
             'sitting with you, notice), with what it\'s for in their terms'),
      'Q3': 'PASS: "the person sitting with you" and "everybody else" told apart; "the thought" named where "it" could point two ways',
      'Q4': ('PASS: "shadow thought" said as a dark thought that comes up; "the flip side of whatever you\'ve been focusing '
             'on" in place of "the other half of a pair"'),
      'Q5': 'PASS: "since", "so", "but", "Then" carry each turn',
      'Q6': 'PASS: what the thought is, what not to do, who to tell, what to do instead, then grounding: the order of the moment',
      'Q7': 'PASS: each line is for someone with a dark thought during a trip',
      'Q8': 'PASS: the don\'ts are what not to do with the thought; the script is what to say',
      'Q9': 'PASS: the four don\'ts of one sentence unpacked, each with its reason'}

R['d01-trip-shadow'] = dict(SHADOW_COMMON,
    pay=[("they don't believe a dark thought about themselves just because it came up, knowing it's often the flip side of "
          "what they've been focusing on", "his paragraphs before it, on why the opposite shows up; this says what to do with "
          "it during a trip", None),
         ("they don't fight the thought, since that makes it come back stronger, and let it be there", "the second thing not "
          "to do, from his \"ignoring problems only makes them worse\"", "Pushing the thought away"),
         ("they can tell the person sitting with them, but don't announce it to everyone or take it as a verdict on themselves",
          "who to tell, and what not to decide yet", "You can tell"),
         ("they name what's happening: a thought is here", "what to do instead of those", "Just notice what's there"),
         ("they name the feeling too", "the script's second line", "none: the script's next line, which the reader says "
          "after the one before"),
         ("they hold it as intense but not all of them", "the script's last line, what the noticing is for", "It is intense"),
         ("they go back to grounding in the Grounding Menu's order: the room, the body, a calm person, the time, love",
          "what to do after noticing", "Then")],
    keep_his={4: SCRIPT_KEEP, 5: SCRIPT_KEEP, 6: SCRIPT_KEEP, 7: ROOM_KEEP},
    keep_fit={7: ROOM_KEEP},
    questions=QS)

R['d02-trip-shadow'] = dict(SHADOW_COMMON,
    pay=[("they don't believe a dark thought about themselves just because it came up", "his paragraphs before it, on why "
          "the opposite shows up; this says what to do with it during a trip", None),
         ("they know it's often the flip side of what they've been focusing on, and that pushing it away makes it come back "
          "stronger", "why not to believe it, and the second thing not to do", "It's often"),
         ("they can tell the person sitting with them, but don't announce it to everyone, since a trip is the worst time to "
          "decide something is permanently wrong with them", "who to tell, and what not to decide yet", "You can tell"),
         ("they notice the thought and the feeling, saying to themselves that it's intense but not all of them",
          "what to do instead of those, in the words they can say", "Just notice what's there"),
         ("they come back to the room, their body, the person with them, the time, and love, in the Grounding Menu's order",
          "what to do after noticing", "Then come back")],
    keep_his={5: "changed: the script's three lines, built the same way, said as one breath a person says to themselves",
              6: "changed: the script's three lines, built the same way, said as one breath a person says to themselves",
              7: "changed: \"It is intense, but it is not the whole of me\" said as the person says it (\"it's not all of me\")",
              8: ("changed: the five category words said as the five things to come back to; room still before body, his "
                  "round-5 decision (OWNER-EDITS q5-room-first)")},
    keep_fit={8: ("changed: the five words said as things to come back to (\"the person with you\" for \"human\", \"what time "
                  "it is\" for \"time\"); love stays, the guide's word for it")},
    questions=dict(QS, Q9='PASS: the four don\'ts of one sentence unpacked, each with its reason; the script said in one breath'))


# ---- batch h58d: B415's third try (after the tell panel on d02) ----
R['d03-trip-shadow'] = dict(SHADOW_COMMON,
    pay=[("they recognize a shadow thought when it comes, from the two examples, and that it can feel like the plain truth",
          "his paragraphs before it, on why the opposite shows up; this is what it looks like during a trip", None),
         ("they know it usually isn't the truth, just the opposite of what they were trying to feel", "why not to believe it",
          "It's usually not the truth"),
         ("they don't push the thought down, since it comes back louder", "the second thing not to do", "Don't shove"),
         ("they can tell their sitter, but don't text everyone at 3 a.m. or decide they have a lifelong disorder",
          "who to tell, and what not to decide yet", "Tell the person sitting with you"),
         ("they notice the thought and the feeling that came with it", "what to do instead of those", "Just notice"),
         ("they hold it as intense but not all of them", "what the noticing is for", "They're intense"),
         ("they come back to the room, their body, the person with them, the time, and love when they can, in the Grounding "
          "Menu's order", "what to do after noticing", "Then come back")],
    keep_his={2: ("changed: \"whatever you were working so hard on\" said as \"whatever you were trying so hard to feel\", "
                  "what the reader is doing on a trip"),
              3: "changed: said as the instruction it is (\"Don't shove the thought down, because ...\"), \"it\" named",
              6: ("the script's point, that the thought is intense but not all of them, said as the person says it; the "
                  "contrast is the meaning"),
              7: ("changed: \"when you can, love\" (a term of address?) said as \"when you can, to love\"; the four things "
                  "are the Grounding Menu's, room before body (his Q-5 decision)")},
    keep_fit={2: ("the section's point, his: the opposite shows up where you focus; \"usually\" leaves room for the rare "
                  "thought that is worth taking to someone after the trip"),
              7: ("the Grounding Menu says how to come back to each; \"the person with you\" is the guide's one calm "
                  "person, and Alone at 3 a.m. is for when there's no one")},
    questions=dict(QS, Q3=('PASS: what a shadow thought is, shown (hating someone you love, being sure you\'re a fraud); the '
                           'sitter told apart from the whole family'),
                   Q9='PASS: the four don\'ts of one sentence unpacked, each with its reason, in sentences of different lengths'))

# ---- batch h58e: his own paragraphs, a word or two each (round 44's cards) ----
HIS_KEEP = "his words, unchanged; the card puts this read's point to him, since the words are his"
R['e01-aftermath'] = dict(
    section="After the Storm: What Kind of Aftermath Is This?",
    reader="someone still having symptoms days after a bad trip, working out what's going on before deciding whether to get help",
    pay=[("they know the section sorts what kind of aftermath this is", "the heading's question", None),
         ("they don't lump every lingering symptom into \"I'm broken\", which solves nothing", "why to sort it at all",
          "When symptoms linger after a trip"),
         ("they know a professional can help at any point, and that working it out themselves may be enough",
          "who can help, before the reader starts", "While a professional"),
         ("they look for the psychological or physical pattern behind their symptoms, in the list that follows",
          "the task, which leads into his list", "Try to find")],
    checked=[], placement="the first paragraph under What Kind of Aftermath Is This?, before his list of patterns",
    why_reading="it tells someone with lingering symptoms to sort out what kind of problem it is",
    same_point="none: read After the Storm for what to do with lingering symptoms: only this paragraph and its list say it",
    keep_need={1: "they know the section sorts what kind of aftermath this is: the guide's heading",
               3: ("they know a professional can help at any point, and that sorting it out themselves may be enough: his "
                   "sentence, which the card puts to him with the fit read's point (\"obviate\", read fast, reassures)")},
    keep_his={2: HIS_KEEP + " (changed: \"after a trip\" says which symptoms)", 3: HIS_KEEP,
              4: HIS_KEEP + " (changed: \"psychological or physical\", the plain word for \"and/or physiological\")"},
    keep_fit={3: HIS_KEEP, 4: HIS_KEEP},
    questions={'Q1': 'PASS: what goes wrong first (the "I\'m broken" bucket), then who helps, then the task',
               'Q2': 'PASS: "Try to find" is the reader\'s act, and the list that follows says how',
               'Q3': 'PASS: "symptoms" said as symptoms after a trip',
               'Q4': 'PASS: "physical" for "physiological"; "obviate" his word, put to him',
               'Q5': 'PASS: "which", "While", the colon into his list',
               'Q6': 'PASS: the problem, the help, the task, in the reader\'s order',
               'Q7': 'PASS: each bears on lingering symptoms after a trip',
               'Q8': 'N/A: no list here; his list follows',
               'Q9': 'PASS: his sentences as he wrote them, two words changed'})
R['e02-ss-recognize'] = dict(
    section="Suspected Serotonin Syndrome (SS): Recognizing serotonin toxicity",
    reader="someone whose friend took MDMA or another drug that raises serotonin and is shaking and sweating, checking for serotonin syndrome",
    pay=[("they know this part is how to recognize serotonin toxicity", "the heading", None),
         ("they know the checklist is the one clinicians use, the Hunter criteria, so they can trust it", "what the patterns "
          "below come from", "We can use the Hunter criteria"),
         ("they know any one of the patterns makes it more likely", "how to use the list", "One or more of these patterns"),
         ("they check for spontaneous clonus, spasms with nothing setting them off", "the first pattern", "Spontaneous clonus:"),
         ("they check for spasms set off by stretching or flexing, with agitation or sweating", "the second pattern",
          "Inducible clonus"),
         ("they check for rapid eye movements with agitation or sweating", "the third pattern", "Ocular clonus"),
         ("they check for shaking with very brisk reflexes", "the fourth pattern", "Another is"),
         ("they check for rigid muscles with a fever over 38°C and eye or inducible clonus", "the last pattern", "Lastly")],
    checked=[], placement="Suspected Serotonin Syndrome's recognition part, his round-36 version, before what to do immediately",
    why_reading="it tells someone checking a friend which patterns point to serotonin syndrome",
    same_point="none: read Suspected Serotonin Syndrome for how to recognize it: only this list gives the patterns",
    keep_need={6: ("they check for rapid eye movements with agitation or sweating: his list item; its ending (\"another pattern "
                   "together\") goes to him on the card, the needed read's point")},
    keep_his={3: HIS_KEEP, 8: HIS_KEEP},
    keep_fit={2: HIS_KEEP + " (changed: \"the same checklist clinicians use\" explains the Hunter criteria where first used)",
              5: HIS_KEEP, 6: HIS_KEEP, 7: HIS_KEEP, 8: HIS_KEEP},
    questions={'Q1': 'PASS: what the list is for first, then how to use it, then the patterns',
               'Q2': 'N/A: no instruction; a checklist the reader goes through',
               'Q3': 'PASS: the Hunter criteria named and said as the checklist clinicians use',
               'Q4': 'PASS: every clinical term explained in its item (clonus, hyperreflexia, hypertonia), his round-36 version',
               'Q5': 'PASS: "One or more", "Another", "Lastly"',
               'Q6': 'PASS: the Hunter criteria\'s order',
               'Q7': 'PASS: each pattern is what to check in a friend after a serotonergic drug',
               'Q8': 'PASS: each item is one pattern of the criteria',
               'Q9': 'PASS: his items as he wrote them; one sentence of his changed'})
R['e03-first-five'] = dict(
    section="Psychological First Aid: The First Five Minutes",
    reader="someone with a friend in a bad trip right now, making the next five minutes safe",
    pay=[("they remove what could hurt them in the next five minutes: keys, stove, roads, balconies, water", "the section's "
          "first job", None),
         ("they let them move and pace, but stop them taking more of anything", "what to allow and the one thing to stop",
          "Letting them move around"),
         ("they put off a confrontation until tomorrow", "the next risk: going after someone", "If they want to go confront"),
         ("they send someone with them if they want to leave", "the risk of leaving alone", "And if they want to leave"),
         ("they put weapons away and keep them from crowds and strangers", "the risk from things and people around",
          "Put any weapons away"),
         ("they take the phone if they want to post a revelation or message an ex", "the last rash act, his",
          "If they want to post")],
    checked=[], placement="Psychological First Aid: The First Five Minutes, his dangers paragraph, before the next step",
    why_reading="it tells a helper what to make safe first, in the first five minutes",
    same_point="none: read The First Five Minutes for what to make safe: only this paragraph says it",
    keep_need={6: ("they take the phone before a post or message the person will regret: his line, one of the rash actions "
                   "the guide says to put off until morning")},
    keep_his={3: HIS_KEEP + " (changed: \"until tomorrow\" says how long it waits)", 4: HIS_KEEP, 5: HIS_KEEP, 6: HIS_KEEP},
    keep_fit={},
    questions={'Q1': 'PASS: what takes priority first, then each risk with what to do',
               'Q2': 'PASS: each instruction is the helper\'s act (get the keys, keep them from more, take the phone)',
               'Q3': 'PASS: the keys, the stove, roads, balconies, pools of water named',
               'Q4': 'N/A: no term a high-school graduate wouldn\'t know',
               'Q5': 'PASS: "so", "but", "And if"',
               'Q6': 'PASS: the most dangerous first',
               'Q7': 'PASS: each bears on the next five minutes',
               'Q8': 'PASS: each is a risk and what to do about it',
               'Q9': 'PASS: his sentences, two words added'})
R['e04-redefining'] = dict(
    section="(Re)defining \"Bad Trip\"",
    reader="someone who just had a rough trip, or whose friend did, reading whether it was shadow work or something to get through",
    pay=[("they know the claim that there's no bad trip, only shadow work", "what the section pushes against", None),
         ("they know that explanation doesn't help someone who never meant to do shadow work", "why the claim falls short",
          "But if you had no intention"),
         ("they know some bad trips aren't about shadow work, though any can lead into it", "the other kind",
          "Other bad trips"),
         ("they know life brings plenty of hard experiences to work through anyway", "why there's no need to seek more",
          "Samsara"),
         ("they reduce the trauma the trip itself is causing, so the old material can be dealt with", "what follows for a bad "
          "trip: reduce it", "It still makes sense"),
         ("they know focusing on what they want can show what's blocking it, which the picture after it shows",
          "my line into the picture after his paragraph", "Sometimes focusing")],
    checked=[], placement="(Re)defining \"Bad Trip\", his third paragraph (B330c) with my line before the picture (B357)",
    why_reading="it tells someone after a rough trip that reducing a bad trip is still worth doing",
    same_point="none: read (Re)defining \"Bad Trip\" for whether a bad trip is worth reducing: only this paragraph says it",
    keep_need={3: "they know some bad trips aren't shadow work, though any can lead into it: his sentence, his distinction",
               4: ("they know life brings plenty of hard experiences anyway, so there's no need to welcome a bad trip for "
                   "them: his sentence, its term now explained")},
    keep_his={1: HIS_KEEP, 2: HIS_KEEP, 3: HIS_KEEP,
              4: HIS_KEEP + " (changed: \"Samsara\" explained where it is first used)",
              5: "changed: \"present-moment trauma\" said as the trauma the trip itself is causing",
              6: "changed: \"the blockage\" said as what's blocking it; what we want is the picture's, which follows"},
    keep_fit={2: HIS_KEEP, 3: HIS_KEEP,
              5: "changed: \"the trauma happening now\" (read fast, it calls the reader's trip trauma) said as the trip's own"},
    questions={'Q1': 'PASS: the claim first, then why it falls short, then what follows',
               'Q2': 'N/A: no instruction but "it still makes sense", said with its reason',
               'Q3': 'PASS: "the trauma the trip itself is causing" for "present-moment trauma"',
               'Q4': 'PASS: "Samsara" explained where it is first used',
               'Q5': 'PASS: "because", "But", "although", "still", "so"',
               'Q6': 'PASS: the claim, its limit, the other kind, what follows',
               'Q7': 'PASS: each bears on whether a bad trip is worth reducing',
               'Q8': 'N/A: no list',
               'Q9': 'PASS: his sentences, a few words changed'})


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
