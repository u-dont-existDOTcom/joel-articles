#!/usr/bin/env python3
"""tells_lint.py - run the written tells audit mechanically before any Pangram check.

Usage:
  python3 tells_lint.py DRAFT [--source SOURCE] [--owner OWNER] [--installed ARTICLE] [--quiet]

DRAFT, SOURCE and OWNER are plain-text or markdown files.
  --source  the AI source section. Enables a review note (D9) when my paragraphs
            walk through the source's points in the source's order. That's not a
            failure by itself: organization is fine when the prose notices things.
  --owner   the owner's own lines, one per line (a line can be a whole paragraph). They're
            excluded from the sentence checks (they're his, not mine) but still counted in the metrics.
  --installed  the article as installed. Its sentences already passed, so they get no flags
            either (a section check holds them), and only the new text can fail.
There is deliberately no check against phrases from failed drafts (Joel, 2026-09-26):
an old phrase is judged like any other, on whether it looks AI. Swapping phrases
between rounds while the structure stays is what humanizer bots do.
Exit code: 2 = FAIL, 1 = REVIEW, 0 = CLEAR.
A CLEAR only means no mechanical tells were found. The judgment checks
(D2 disparity, A1 meaning and safety, referents) still have to be written by hand.
R1 only catches the "did it" kind of referent; no reviewer caught that one either (2026-09-30).
E125 (2026-10-03): a list of three or more is a REVIEW, and two in one paragraph are a FAIL.
E126 (2026-10-03 01:06): the fix is to drop the item that matters least, or split the list when every item is needed.
O8/O9 (2026-10-03 20:51): "smuggled into one sentence here" fails; a "not Y" tail on a finished claim is a REVIEW.
H1 and O10 (2026-10-06): headings are text. An x-not-y heading ("The Medicine Part, Without Pretending It Isn't There")
fails, and so does an opener that points at nothing ("Key here is that…"); a pointer word opening the first paragraph
under a heading ("This", "It", "The other") is a REVIEW. Markdown headings only (lines starting with #).
O1 (2026-10-07 15:44): the "doesn't get to decide" family fails only when its subject isn't a person ("the weather doesn't
get to decide"); with a person ("your dad doesn't get to decide") it isn't flagged, and an unclear subject is a REVIEW.
O14, O15 and O16 (Joel, 2026-10-07 01:43; numbered after the Inner Child lane's O11 to O13): Emulate's "and ... and ... and" list fails (two repeated "and"s or "or"s in
one stretch without punctuation are a REVIEW, three a FAIL); an unusual spelling or hyphenation is a REVIEW, his lines
included ("unusual spellings should help pass pangram, but that's also cheating"); a paragraph that closes by summing
itself up ("These are all questions that…") is a REVIEW ("it was way overcompleting itself").
O17 (Joel, 2026-10-07 15:05, and 16:46 in the Inner Child lane: "may have X and still Y"): "may be X and still Y" is a tell ("Humans don't use that as much"): a modal clause tied to
its consequence by "and still" is a REVIEW.
O12 includes "quietly" since 2026-10-10 (Joel: "using quietly all the time like that is a huge AI tell"; AGENTS.md lists boring, quietly
and ordinary together). O20 (2026-10-10): "I want / I don't want" opening a stance, a REVIEW. O21 (2026-10-10): a stock comparison
quip ("with a nicer logo", "with extra steps"), a REVIEW.
O18 (2026-10-07; O14 in the Inner Child lane until the 2026-10-09 merge, renumbered after main's O14 to O17): "not X, but still Y" in one sentence or two, a REVIEW (Joel: "there are other X Y rules, like 'Not x,
but still y.'"). O19 (2026-10-07; was the lane's O15): a bulleted or numbered list, a REVIEW (Joel: "lists in general are overused by AI").
Its word lists and patterns are for exact things (a fixed phrase Joel banned, a count, a list's length). A flag
about meaning is a candidate for a model to judge, never a verdict, and a meaning check is never fixed by adding words
to a list (AGENTS.md, "Checks that judge text"; UDA's pattern-matching fit check, Joel 2026-10-07).
O6 reads the grammar when spaCy (en_core_web_sm) and NLTK's WordNet are installed (Joel, 2026-10-07 23:22: a list of
abstract nouns "sounds brittle... abstract nouns are a real vast open-ended list"); otherwise it falls back to its word
list and says so in the report.

2026-10-11, the tells coverage audit (tools/humanization/TELLS-COVERAGE-20261011.md). Joel: "you mention that boring and
quietly were in the tells list, but never checked? why is that? can we debug that? any time something is not executing as
intended it should be debugged." The five documents (AGENTS.md, SKILL.md, docs/HUMANIZATION-GATE.md and the two lists in
tools/humanization/) name 131 tells, 82 of them mechanical; this file checked 51. Every tell now has an entry in
tells_registry.json, and tests/test_tells_registry.py runs each mechanical one's example through this file.
Matcher fixes:
- Curly quotes. The rules match a copy of each sentence with ’ ‘ made ' and “ ” made " (straight()); a flag still quotes
  the sentence as written. B2, B5, E41 and E138 had missed "That’s where…", "isn’t … it’s", "You’ll want…" and "I’d be
  tempted to…" (AGENTS.md writes "That’s where X matters to me" with the curly one first).
- B11's "That's not X. It's Y." looked inside one sentence, where the split had already cut it in two, so it never matched.
  It reads each sentence with the next one now, with the cousins "Not a hobby. It's a job." and "The point is not X. The
  point is Y." (reviewer/owner_bans.txt: "the "That's not X. It's Y." construction"; JOEL-FIXES-CATALOGUE, "What he cuts"
  2: ""Not X. It's Y." and its cousins").
- O2 fails "Fine." or "Sure." as a sentence of its own and "…, sure. But" across the split (owner_bans.txt: "as a clause or
  a sentence of their own"; the gate's 2026-10-10 prediction review: "sure. But").
- O37 is the chat-acronym flag, which had no ID: it reads any case now, and "lol" fails (gate step 9: ""lol" is wry, so
  it's out"; JOEL-FIXES-CATALOGUE: "lol is different from hehe, it's more wry.").
- E125 counts a list whose items start with "who is" (JOEL-FIXES-CATALOGUE: "The parallel "who is … who is … or who is"
  list became a looser one").
- O20's "I'd like" branch wanted a space after "I", so it never matched.
New rules (REVIEW unless the document bans the thing):
- O22 first-person staging: "I care about", "I'd want to see", "that tells me", "That's where X matters to me", "This is one
  reason I want", "The version I want is", "What matters to me is" (AGENTS.md: "Treat significance-staging constructions
  ... as AI-shaped in Joel-byline prose"; SKILL.md: "Phrases such as `I care about...`, `I want...`, `I don't want...`,
  `I'd want to see...`, `that tells me...`, and close variants are AI-shaped"). "I want" opening a sentence stays O20's.
  Words in double quotes are left out of O22, O23, O24 and O34: they're someone's speech (AGENTS.md: "Quotation or
  literal discussion of the construction is exempt").
- O23 research notes told as narration: "I had heard", "I checked", "I looked it up", "the check I did", "I wasn't sure what
  the term was", and "I thought" in a paragraph that narrates a check (AGENTS.md: "Do not automatically convert research
  notes such as `I thought X`, `I had heard Y`, `I checked it` ... into article narration"; "not as a diary of `I thought →
  I checked → I learned`").
- O24 stock lines: "I see the need to", "It's also important to", "One thing to notice about" (the gate's prediction review:
  "speech markers laid over AI shapes ... and stock lines like "I see the need to", "It's also important to", "One thing to
  notice about"").
- O25 "even" and "actually", with the count (TELLS-FROM-PANGRAM-DATA-20261007.md: "They're words I add to sound casual, and
  they don't help."). "Even if" and "even though" are B1's, and an "Even" that opens a sentence went with the passing drafts
  (same file), so they aren't counted.
- O26 emoji, all FAIL: a pointer (👇 👉 👆 👈 ☝️), 😉, or anything off the allowlist in EMOJI-LIST.md, read from that file
  (gate step 9: "everything else counts as banned until Joel says yes. Never a pointer (👇 👉 👆 👈 ☝️) or 😉: "those look
  super ai, only after seen them from ai slop, don't ever use those."").
- O27 rough edges in my text: two spaces in a row, or a paragraph that ends with no end mark (JOEL-FIXES-CATALOGUE: "Rough
  edges he leaves: typos, double spaces, missing periods. These come from typing. They aren't something for me to
  imitate."). Never on --owner or --installed lines.
- O28 "It's one thing to X. It's another to Y" (JOEL-FIXES-CATALOGUE: Emulate's "one thing ... another thing" "is not quite
  showing that the truth was Y not X"; "A contrast has to say which side is true.").
- O29 a run of three or more questions, once per run (gate step 7: "a few shared AI micro-patterns (question runs, triads,
  "isn't X, it's Y")").
- O30 a phrase said three or more times in one paragraph, his occurrences counted with mine (gate, 2026-10-07 20:21: "My "a
  commitment they make as adults", which he OK'd, gave P22 its fourth "as adults""; JOEL-FIXES-CATALOGUE: "yes fix p222
  take out second adults that's obvious"). A phrase is two to four words with a content word in it, not opening with
  "the", "a" or a possessive or always coming right after one (a thing named again, "the community" or "your little
  one", is ordinary), and not opening a sentence (a run of parallel questions is O29's).
- O31 two parallel "When…, don't…" lines in a paragraph, O32 "is a kind of X, but it's not the whole thing"
  (JOEL-FIXES-CATALOGUE, Minimal-fix lesson 1: the flagged window held "two parallel "When…, don't…" lines" and "an "is a
  kind of love, … but it's not the whole thing" line").
- O33 "Nope." and "Aww, buddy." (gate, "Repairing a failed draft": "The stock casual moves a model reaches for when told to
  sound casual ("Nope.", "Aww, buddy.", a goofy exclamation, a punchy closer) came back 100% AI, high, in eight versions").
- O34 "I wouldn't call that X" (JOEL-FIXES-CATALOGUE, his words: "Ai stuff overuses 'i wouldn't call that X'").
- O35 "with or without X" (gate step 2: Joel: "with or without X is not quite guidance". Say what X is good for).
- O36 a "but also" pair (the gate's prediction review: "P34m passed with "the boring problem", the "nicer logo" quip, a "but
  also" pair and a list; without the one word "connect," it read 100% AI").
"""
import os, re, sys, argparse, math
from statistics import mean, pstdev

def clean(t):
    # A comment between two spaces leaves one space, not two, so O27 doesn't read the gap as a double space (2026-10-11).
    t = re.sub(r'([ \t]*)<!--.*?-->([ \t]*)', lambda m: ' ' if (m.group(1) or m.group(2)) else '', t, flags=re.S)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    t = re.sub(r'^#+\s.*$', '', t, flags=re.M)          # drop headings
    t = t.replace('*', '')
    return t.strip()

def paragraphs(t):
    ps = [p.strip() for p in re.split(r'\n\s*\n', t) if p.strip()]
    # drop heading-like lines: short and without sentence punctuation at the end
    return [p for p in ps if not (len(p.split()) <= 12 and not p.rstrip().endswith(('.', '?', '!', '"', '”', ':')))]

ABBREVIATIONS = ('Mr.', 'Mrs.', 'Ms.', 'Dr.', 'St.', 'vs.', 'e.g.', 'i.e.')

def sentences(p):
    p = re.sub(r'\s+', ' ', p)
    parts = re.split(r'(?<=[.!?])["”]?\s+(?=["“]?[A-Z0-9])', p)
    # Rejoin splits after an abbreviation: "Mr. Rogers" was read as two sentences,
    # which produced false short-landing and announcing flags (2026-09-26).
    out = []
    for s in (x.strip() for x in parts if x.strip()):
        if out and out[-1].endswith(ABBREVIATIONS):
            out[-1] = out[-1] + ' ' + s
        else:
            out.append(s)
    return out

def words(s): return re.findall(r"[A-Za-z']+", s)

# Curly quotes (2026-10-11 audit): the rules below spell apostrophes and quotes straight, and B2, B5, E41 and E138 missed
# every curly one ("That’s where…" came back CLEAR where "That's where…" got B5). So the rules match against straight(s),
# a copy of the sentence with ’ ‘ made ' and “ ” made ". It's one character for one, so positions in the copy are positions
# in the original, and a flag still quotes the sentence as written: Joel's characters stay his (gate, 2026-10-02).
STRAIGHT = str.maketrans({chr(0x2019): "'", chr(0x2018): "'", chr(0x201C): '"', chr(0x201D): '"'})   # ’ ‘ “ ”

def straight(t): return t.translate(STRAIGHT)

TICS = [r"doing some work", r"load-bearing", r"tells on itself", r"metaboli[sz]", r"\bdigest", r"\bclean\b",
        r"does its work"]
# B11 across two sentences (2026-10-11): "That's not X. It's Y." was the last TICS pattern, tested one sentence at a time.
# The sentence split cuts it in two first, so it could never match. Now each sentence is read with the next one. The
# negated frame opens its clause ("It's not a hobby.", "…, that is not just bad sleep hygiene."), or the sentence is a
# "Not a…" fragment of a few words ("Not a hobby."; "Not a single member came to the meeting that night." is a sentence,
# not a fragment); the next sentence opens with the same kind of frame, not negated. "It was not until…" is a cleft, not
# a contrast. The cousin "The point is not X. The point is Y." repeats its own noun (JOEL-FIXES-CATALOGUE, "What he cuts" 2).
_B11_FRAME = r"(?:it|that|this)(?:'s|\s+is|\s+was)"
# The negated clause runs to its sentence's end with no comma: "that isn't a failure, though checking it off doesn't prove
# it helped either. That's the … question again." goes on past its "not" and isn't the swap (calibration, 2026-10-11).
B11_NOT_ITS = re.compile(r"(?:(?:^|[,;:]\s*|\b(?:and|but|so|because)\s+)(?:" + _B11_FRAME + r"\s+not|(?:it|that|this)\s+(?:isn't|wasn't))\b"
                         r"(?!\s+until\b)[^.?!,;:]{1,80}"
                         r"|^not\s+(?:a|an|the|just|only|really|about|because|for|some|my|your|our|their)\b(?:\s+[\w'-]+){1,5})"
                         r"[.?!]['\"]?\s+" + _B11_FRAME + r"\b(?!\s+not\b)", re.I)
B11_POINT_IS = re.compile(r"^the\s+(\w+)\s+(?:is|was)(?:\s+not|n't)\b[^.?!,;:]{1,80}[.?!]['\"]?\s+the\s+\1\s+(?:is|was)\b(?!\s+not\b)", re.I)
CONTRAST = [r"\b(isn't|is not|wasn't|aren't|not)\b[^.?!]{0,50}\b(it's|it is|they're|but)\b",
            r"\brather than\b", r"\binstead of\b", r"doesn't mean[^.?!]*\bmeans?\b", r"\bIt's tempting\b",
            r"\bnot the same as\b", r"\bis still a long way from\b", r"\bthe difference between\b"]
THESIS = [r"\band (still|yet)\b", r"\beven if\b", r"\beven though\b", r"\benough to\b[^.?!]*\b(but|not)\b",
          r"\bnot necessarily\b", r"\bstill counts\b", r"\banyway[.!]", r"\bonly gets you\b",
          r"^(Most|Nobody|Everyone|Everybody|People|Kids|Children|No one|Plenty of|Anybody who)\b"]
COACH = [r"\byou can\b(?!['’]t)", r"\byou might\b", r"\byou'll (want|need|probably)\b", r"\bat some point\b",
         r"\bthat's (fine|okay|ok|normal|all right)\b", r"\bit helps( to)?\b", r"\bstart (by|with)\b",
         r"\bthe next step\b", r"\bdon't be surprised\b", r"\bit's tempting\b", r"\byou don't (have|need) to\b",
         r"\bkeep in mind\b", r"\bremember (that|to)\b", r"\bgive yourself\b", r"\bit's okay to\b",
         r"\bthe goal is\b", r"\bthe point is\b", r"\bin other words\b", r"\bgo easy\b"]
ANNOUNCE = [r"^(Or maybe|For [a-z]+,|Here's|That's where|The next step|Now,|First,|Second,|Finally,|So the next)",
            r"^[A-Z][a-z]+ (is|are|can be|works like) [^.]{0,30}\.$"]
IMPER = set("""think picture imagine ask try put start leave borrow skip write take let keep stop find notice make give go
use pick tell say be do don't dont notice consider remember breathe turn stay come look call eat sleep sit""".split())
STOP = set("""a an the and or but if so to of in on at for with by from as is are was were be been being it its it's this that
these those you your yours i me my we our they them their he she his her not no do does did done have has had can could
would should will just about into than then there here what which who whom when where why how all any some more most very
up out over under again also too even still yet only own same such own each few other get got""".split())

def content(s): return [w.lower() for w in words(s) if w.lower() not in STOP and len(w) > 2]

def cos(a, b):
    from collections import Counter
    A, B = Counter(a), Counter(b)
    num = sum(A[k]*B[k] for k in A)
    den = math.sqrt(sum(v*v for v in A.values()))*math.sqrt(sum(v*v for v in B.values()))
    return num/den if den else 0.0

ACRONYMS = r"\b(IMO|IMHO|TBH|FWIW|IIRC|AFAIK|NGL|IRL|ICYMI|TL;?DR|BTW|OMG|LOL|SMH|YMMV)\b"

# O7: the balanced "X enough to A and Y enough to B" pair (Joel, 2026-10-02 21:16, on "devoted enough to practice them
# and secure enough to disagree": "looks super highly polished. surprised emulate let that in. and surprised pangram passed it").
ENOUGH_PAIR = r"\b\w+ enough to \w+[^.?!;]{0,60}?\b(?:and|but|yet|while)\b[^.?!;]{0,30}?\b\w+ enough to\b"

# O8: smuggling talk (Joel, 2026-10-03 20:51, on community section 5 P23's "My reasons are in those articles, not smuggled
# into one sentence here": "ai is always saying something like 'not smuggle in' or something about smuggling in"). The
# figurative kind fails (smuggled in or into something, or not/rather than/without smuggling); goods smuggled across a
# border are a REVIEW, for the ledger to clear.
SMUGGLE_FIG = (r"\b(?:not|never|rather than|instead of|without|no)\s+(?:\w+\s+){0,2}?smuggl\w*"
               r"|\bsmuggl\w*\s+(?:\w+\s+){0,4}?(?:in|into)\b(?!\s+(?:the\s+)?(?:country|border|port|prison|jail))")
SMUGGLE = r"\bsmuggl\w*"
# O9: a "not Y" tail on a finished claim (Joel, same message: "And it always wants to add a 'not Y' part"). REVIEW: say
# the claim or the reason plainly; keep a contrast only when the paragraph needs the other side said. Four words or more
# must come before the comma or dash, so "No, not today." stays out.
NOT_TAIL = re.compile(r"^(?P<head>.*\w.*?)(?:,|\s[—–]|\s--)\s+(?:and\s+)?(?:not|rather than|instead of)\s+(?:just\s+|only\s+|merely\s+|simply\s+)?[^,;:.!?]{2,90}[.!?\"”’)]*\s*$", re.I)

# O1 (Joel, 2026-09-28; scoped 2026-10-07 15:44): "that was regarding abstract subjects. "the weather doesn't get to
# decide" for example, not "your dad doesn't get to decide"". So the subject decides: a feeling, urge, part, thought or
# thing fails; a person isn't flagged; an unclear one ("your little one", "they") is a REVIEW.
GETS_TO = re.compile(r"\b(?:doesn['’]t|does not|don['’]t|do not|never|won['’]t|shouldn['’]t|can['’]t|cannot)\s+gets?\s+to\b"
                     r"|\bgets?\s+to\s+(?:decide|choose|pick|vote|call|run|set|have the (?:last|final) (?:word|say))\b"
                     r"|\bgets?\s+(?:a|the|any|no)\s+(?:vote|say|veto)\b", re.I)
GT_PERSON = re.compile(r"\b(?:you|i|we|he|she|nobody|no one|somebody|someone|everybody|everyone|anybody|anyone|people|person|"
                       r"parents?|dad|mom|mum|mother|father|partner|friends?|kids?|child|children|therapist|doctor|boss|family|"
                       r"brother|sister|wife|husband|neighbou?r|teacher|guru|leader|members?|man|woman|guy|girl|boy|adults?)\b", re.I)
GT_THING = re.compile(r"\b(?:it|this|that|feelings?|urges?|thoughts?|parts?|fears?|anxiety|anger|shame|grief|critic|voice|"
                      r"weather|rules?|ideas?|mind|brain|body|story|mood|panic|worry|doubts?|pain|hurt|past|wound|habit|"
                      r"impulse|emotions?|craving|instinct|alarm|nervous system)\b", re.I)
GT_CLAUSE = re.compile(r"[,;:—–(]|\b(?:and|but|so|because|since|if|when|while|though|although|unless|until|which|who)\b", re.I)

def gets_to_subject(s, m):
    """'person', 'thing' or 'unclear' for the subject right before a "gets to" match."""
    head = s[:m.start()]
    cuts = [x.end() for x in GT_CLAUSE.finditer(head)]
    seg = head[cuts[-1]:] if cuts else head
    seg = re.sub(r"\b(?:part|parts|side|bit|piece) of (?:you|your|yourself|me|us|them|him|her)\b", 'part', seg, flags=re.I)
    seg = re.sub(r"\b(?:your|my|his|her|their|our|its)\b", '', seg, flags=re.I)
    person, thing = bool(GT_PERSON.search(seg)), bool(GT_THING.search(seg))
    return 'person' if person and not thing else 'thing' if thing and not person else 'unclear'

# O18 (Joel, 2026-10-07 15:44; the lane's O14 until 2026-10-09): "there are other X Y rules, like "Not x, but still y."" The x-not-y family is wider than the
# "not Y" tail (O9) and the heading (H1). REVIEW: say the claim plainly; keep the contrast only when the reader needs it.
NOT_BUT_STILL = re.compile(r"\b(?:isn['’]t|is not|aren['’]t|wasn['’]t|weren['’]t|not|doesn['’]t|don['’]t|didn['’]t|never|no)\b"
                           r"[^.?!;]{0,70}?\b(?:but|though|yet)\b[^.?!;]{0,40}?\bstill\b", re.I)
# "may X and still Y" (Joel, 2026-10-07 16:46) is O17 (main's STILL_TAIL, from his 15:05 note in the community lane).
NOT_SENT = re.compile(r"\b(?:isn['’]t|aren['’]t|wasn['’]t|is not|are not|(?:doesn['’]t|don['’]t|didn['’]t) (?:mean|make|prove|change|count|matter|fix)|not (?:proof|enough|the same|a sign|evidence))\b", re.I)
STILL_NEXT = re.compile(r"(?:But |And )?(?:it|that|this|they|you)(?:['’]s)? (?:still|can still)\b", re.I)
# O19 (Joel, 2026-10-07 15:44; the lane's O15 until 2026-10-09): "lists of 3 especially, and lists in general are overused by AI. try to avoid that unless
# it's really needed." A bulleted or numbered list in the draft is a REVIEW (lists in a sentence are E125).
LIST_LINE = re.compile(r"^\s*(?:[-*+•]|\d+[.)])\s+\S", re.M)

# O6: a feeling or an abstract idea doing what a person does (Joel, 2026-10-02 00:52: "the usage of abstract concepts
# or feelings as agents is one AI tell because it permits high efficiency of words"; he changed "so the anger goes
# there, trying to get some justice" to "so the angry communard goes there"). REVIEW only: an idiom can stay, and so
# can his own words. It catches the noun right before the verb, so a subject with a long clause after it slips by.
# 2026-10-07 20:21, on community section 8 P28's "goodwill doesn't answer those questions": "that AI tell again, in the
# linter. abstracts doing things." The check had missed it: "goodwill" wasn't in the list, a negation ("doesn't",
# "won't", "can't") stood between the noun and the verb, and "answer" wasn't a verb it knew. The sentence read AI in
# about 25 wordings, and almost every first sentence drafted for it kept goodwill as the one answering; the cut passed.
ABSTRACT_AGENT = (r"\b(anger|fear|grief|shame|hurt|pain|longing|loneliness|resentment|jealousy|envy|desire|rage|guilt|"
                  r"sadness|anxiety|panic|feelings?|emotions?|objection|vision|insight|truth|idea|wish|need|hope|love|trust|"
                  r"goodwill|good will|good intentions?|kindness|ideology)"
                  r"\s+(?:(?:\w+ly|alone|still|also|just|doesn['’]t|does not|didn['’]t|did not|won['’]t|will not|can['’]t|"
                  r"cannot|can not|never)\s+){0,2}"
                  r"(goes|went|comes|came|arrives|arrived|tries|tried|wants|wanted|seeks|sought|demands|"
                  r"demanded|decides|decided|chooses|chose|refuses|refused|pushes|pushed|waits|waited|hides|hid|insists|"
                  r"insisted|asks|asked|teaches|taught|shows up|showed up|returns|returned|travels|traveled|files|filed|"
                  r"knocks|knocked|creeps|crept|sneaks|snuck|wanders|wandered|votes|voted|speaks|spoke|whispers|whispered|"
                  r"looks for|looked for|leaks|leaked|settles in|settled in|takes over|took over|wins|won|"
                  r"answers?|answered|settles?|settled|solves?|solved|fix|fixes|fixed|protects?|protected|saves?|saved|"
                  r"heals?|healed|handles?|handled|knows?|knew|decide|choose|refuse|want|try|ask|go|come)\b")

# O6, parsed (Joel, 2026-10-07 23:22, on the list above: "that sounds brittle... is that the best way to handle the
# abstracts doing things check? abstract nouns are a real vast open-ended list in my mind"). He's right: no list covers
# an open class. When spaCy (en_core_web_sm) and NLTK's WordNet are installed, the check reads each sentence's grammar
# instead. It finds each clause's subject, and asks WordNet what kind of thing that noun mostly names: a feeling, an
# idea, a quality, a state or a motive (abstract), or a person, an animal or a group (who may do anything). For the
# verb it asks whether WordNet's sentence frames give it only "Somebody" as a subject (answer, decide, refuse, vote)
# or also "Something" (destroy, prevent, need). A few verbs that also take things but read as a person's act after
# an idea are added by hand (SEED_PERSON_VERBS). It follows the verb into an infinitive or a participle with no subject
# of its own ("doesn't get to decide", "goes there, trying to"). It skips everyday phrasal verbs ("wears off", "comes
# up"), light verbs (do, give, take, make, have, get) and "is going to". On the community article as installed (15,460
# words, 926 sentences) it flags 13 sentences, most of them real cases ("Modern life trains us", "Nobody's status buys
# silence", "The vaccination policy arrives two years later carrying documents"), with four misparses; on the Inner
# Child article, 6, among them "Guilt may keep shouting at you". The word list found one sentence in both articles.
# Without those libraries the word list above is the fallback, and the report says so.
# Joel, 23:50, on "Modern life trains us": "actually very human to say ... so common it's almost cliche, it's not a witty
# AI quip ... isn't that what LLMs are great at?" The grammar finds candidates; only a reader can judge them. So an O6 flag
# is a candidate, and abstract_agents_prompt.py has a fresh agent sort them (everyday, in between, quip) against his ratings.
SEED_PERSON_VERBS = set("""arrive try want seek demand decide choose refuse push wait hide insist ask teach return travel
file knock creep sneak wander vote speak whisper settle win answer solve fix protect save heal handle know buy
train""".split())
LIGHT_VERBS = set('be do give take make have get keep put let become seem remain stay mean'.split())
_ABSTRACT_LEX = {'noun.feeling', 'noun.cognition', 'noun.attribute', 'noun.state', 'noun.motive'}
_ANIMATE_LEX = {'noun.person', 'noun.animal', 'noun.group'}
_PARSER = None

def parser():
    """(spaCy pipeline, WordNet) when both are installed, else False."""
    global _PARSER
    if _PARSER is None and os.environ.get('TELLS_LINT_PARSE', '1') == '0':
        _PARSER = False  # turned off: the tests do this, since loading spaCy costs a second or two per run
    if _PARSER is None:
        try:
            import spacy
            from nltk.corpus import wordnet as wn
            wn.synsets('fear')  # LookupError when the corpus isn't downloaded
            _PARSER = (spacy.load('en_core_web_sm'), wn)
        except Exception:
            _PARSER = False
    return _PARSER

def _noun_mostly_abstract(wn, name):
    ss = wn.synsets(name, 'n')
    if not ss:
        return None
    w = {'animate': 0.0, 'abstract': 0.0, 'other': 0.0}
    for s in ss:  # each sense weighted by how often it's used (SemCor counts), plus one
        c = sum(l.count() for l in s.lemmas() if l.name().lower() == name.lower()) + 1
        w['animate' if s.lexname() in _ANIMATE_LEX else 'abstract' if s.lexname() in _ABSTRACT_LEX else 'other'] += c
    return w['abstract'] >= 0.5 * sum(w.values())

def _person_verb(wn, lemma):
    if lemma in LIGHT_VERBS:
        return False
    if lemma in SEED_PERSON_VERBS:
        return True
    p = t = 0.0
    for s in wn.synsets(lemma, 'v'):
        c = sum(l.count() for l in s.lemmas() if l.name().lower() == lemma.lower()) + 1
        frames = [f for l in s.lemmas() if l.name().lower() == lemma.lower() for f in l.frame_strings()]
        if frames and not any(f.startswith(('Something', 'It ')) for f in frames):
            p += c
        t += c
    return t > 0 and p / t >= 0.6

def _light_verb_act(wn, verb_tok):
    """For a light verb, the person's act its object names: "makes the decision" (decide), "gives an answer"."""
    for o in (c for c in verb_tok.children if c.dep_ == 'dobj'):
        for s in wn.synsets(o.lemma_, 'n')[:2]:
            for l in s.lemmas():
                for d in l.derivationally_related_forms():
                    n = d.name()
                    if d.synset().pos() == 'v' and n not in LIGHT_VERBS and _person_verb(wn, n):
                        return n
    return None

def abstract_agents(sentence):
    """[(noun, verb)] for each clause whose subject is mostly an abstraction doing what a person does; None without
    the parser."""
    pw = parser()
    if not pw:
        return None
    nlp, wn = pw
    out = []
    for tok in nlp(sentence):
        if tok.dep_ != 'nsubj' or tok.pos_ != 'NOUN':
            continue
        mods = [c for c in tok.children if c.dep_ in ('compound', 'amod')]
        kinds = [_noun_mostly_abstract(wn, m.lemma_ + '_' + tok.lemma_) for m in mods]
        kind = next((k for k in kinds if k is not None), None)
        if kind is None:
            kind = _noun_mostly_abstract(wn, tok.lemma_)
        v = tok.head
        if not kind or v.pos_ not in ('VERB', 'AUX'):
            continue
        if any(c.dep_ == 'prt' for c in v.children):
            continue  # "the euphoria wears off", "anger comes up": everyday phrasal verbs
        if v.lemma_ == 'go' and any(c.dep_ == 'xcomp' for c in v.children):
            continue  # "is going to": the future
        chain = [v] + [c for c in v.children if c.dep_ in ('xcomp', 'advcl') and c.pos_ == 'VERB'
                       and not any(g.dep_ in ('nsubj', 'nsubjpass', 'expl') for g in c.children)]
        for x in chain:
            if x.pos_ != 'VERB':
                continue
            act = x.lemma_ if _person_verb(wn, x.lemma_) else _light_verb_act(wn, x) if x.lemma_ in LIGHT_VERBS else None
            if act:  # "Fear makes the decision before you've even noticed it" (Joel's ratings, 2026-10-02: 4 of 5)
                out.append((tok.text, act))
                break
    return out

# E125: lists of three. Joel, 2026-10-03 00:00 UTC, on Start With Whatever Showed Up P1 (66% AI): "P! failed b ecause
# it has 2 lists of 3. I did a minimal fix and now it's human med conf"; 00:01: "lists of 3 in general are an ai pattern".
# His fix kept two items in each and gave the rest its own sentence ("Maybe it just has something to say.").
# On the calibration corpus (2026-10-03), single paragraphs: one list or more in 45% of the 77 that failed and 28% of the
# 96 that passed; two or more in one paragraph, 16% (12) against 5% (5). Back to back or not made no difference.
# So one list is a REVIEW, and two in one paragraph are a FAIL. The detector is regex, not grammar: coordinate
# adjectives ("non-forced, slower exhales and a little self-massage") can still read as a list, and a list inside an
# opening if-clause with long items is skipped on purpose.
LEAD = set("""but so because since though although if when whenever while as once until unless which that who whom whose
where why how then than like even just before after""".split())
PRON = set("i you he she it we they there this that these those".split())
NOT_OR = re.compile(r"\bor\s+(not|so|less|more|else|other|two|three|whatever)\b", re.I)
QUOTED = re.compile(r'"[^"]*"|“[^”]*”')
WHO_ITEM = re.compile(r"who(?:'s|\s+(?:is|are|was|were))\b", re.I)

def _segments(s):
    out, pos = [], 0
    for part in s.split(','):
        out.append((pos, part)); pos += len(part) + 1
    return out

def _w0(seg):
    """The segment's first word, past a leading And/But/So/Or, without a contraction ending."""
    ws = seg.split()
    while ws and ws[0].lower() in ('and', 'but', 'so', 'or'):
        ws = ws[1:]
    return re.sub(r"['’](s|ll|re|d|ve|m)$", '', ws[0].lower()) if ws else ''

def _find(s):
    hits = []
    # 1. the same conjunction twice after commas: "A, or B, or C" / "A, and B, and C"
    for m in re.finditer(r",\s+(or|and)\s+[^,.;:!?]+?,\s+\1\b", s, re.I):
        hits.append(('repeated ' + m.group(1).lower(), m.start(), m.end()))
    # 2. "A or B or C" with no commas, items of up to five words
    for m in re.finditer(r"\bor\s+(?:[^\s,.;:!?]+\s+){1,5}?or\b", s, re.I):
        if NOT_OR.match(s, m.end() - 2): continue
        hits.append(('repeated or', m.start(), m.end()))
    seg = _segments(s)
    # 3. the serial list "A, B, and C" / "A, B, or C": an and/or segment after two comma segments
    for k in range(2, len(seg)):
        last = seg[k][1].strip(); mid = seg[k-1][1].strip(); first = seg[k-2][1].strip()
        if not re.match(r"(and|or)\s+\S", last, re.I): continue
        if re.match(r"(and|or)\b", mid, re.I): continue          # rule 1 has it
        if re.search(r"\b(and|or)\b", mid, re.I): continue       # "Nurturer, Protector and Guide are all you, and": rule 4
        mw = mid.split()
        # Items that each start with "who is" are a list, long items too (2026-10-11 audit, W63; JOEL-FIXES-CATALOGUE:
        # "The parallel "who is … who is … or who is" list became a looser one"). "who" is in LEAD, which had skipped them.
        who_list = WHO_ITEM.match(mid) and re.match(r"(?:and|or)\s+" + WHO_ITEM.pattern, last, re.I)
        if who_list:
            if len(mw) > 14: continue
        elif not (1 <= len(mw) <= 6) or mw[0].lower() in LEAD | {'not'}: continue
        if k - 2 == 0:
            fw = first.split()
            if len(fw) <= 1: continue                             # "Honestly, I think so, and he agreed"
            # an opening clause ("If the room itself triggers your spidey sense, leave, or lock the door"),
            # unless the items are short ("If you're stuck, tired, or bored")
            if _w0(first) in LEAD and not (len(mw) <= 2 and len(last.split()) <= 3): continue
        a = seg[k-2][0] + len(seg[k-2][1].rstrip()) - len(' '.join(first.split()[-5:]))
        b = seg[k][0] + len(seg[k][1]) - len(seg[k][1].lstrip()) + len(' '.join(last.split()[:5]))
        hits.append(('serial', a, b))
    # 4. the serial list without its last comma: "A, B and C" (a short "B and C" segment after a comma)
    for k in range(1, len(seg)):
        part = seg[k][1].strip()
        m = re.match(r"[^\s]+(?:\s+[^\s]+)?\s+(and|or)\s+([^\s]+)(?:\s+[^\s]+){0,3}[.!?\"”)]*$", part, re.I)
        if not m: continue
        if _w0(part) in LEAD | PRON | {'not'} or re.match(r"(and|or)\b", part, re.I) or NOT_OR.search(part): continue
        if _w0(m.group(2)) in PRON or part.startswith('"'): continue  # "“No, that's not right for me,” and they call it": a clause
        prev = seg[k-1][1].strip()
        if not prev or (k - 1 == 0 and (len(prev.split()) <= 1 or _w0(prev) in LEAD)): continue   # "If words are there, speak or write them"
        # "Or something does come, a voice or a hunch, and": the pair says what came (an aside), it isn't a third item
        if re.match(r"(a|an|the|some)\s", part, re.I) and re.search(r"\b(does|do|did|is|are|was|were|can|could|will|would|might|may|has|have|had|comes?|came)\b", prev, re.I):
            continue
        a = seg[k-1][0] + len(seg[k-1][1].rstrip()) - len(' '.join(prev.split()[-4:]))
        hits.append(('serial, no last comma', a, seg[k][0] + len(seg[k][1])))
    # one long list can match twice, or by two rules: count it once
    hits.sort(key=lambda h: h[1]); out = []
    for kind, a, b in hits:
        same = [i for i, o in enumerate(out) if (o[0] == kind and (kind.startswith('repeated') or a <= o[2] + 3))
                or (o[0].startswith('serial') and kind.startswith('serial') and a < o[2] and b > o[1])]
        if same:
            i = same[-1]; out[i] = (out[i][0], out[i][1], max(b, out[i][2])); continue
        out.append((kind, a, b))
    return out

def triads(s):
    """[(kind, excerpt, quoted)] for each list of three or more in sentence s. Quoted words (a prayer, a line
    someone says) are read on their own, so their commas don't split the sentence, and their lists are marked."""
    s = re.sub(r'\s+', ' ', s).strip()
    n = straight(s)   # matched with straight quotes; one character for one, so the excerpts come from s as written
    masked = QUOTED.sub(lambda m: '"' + 'Q' * (len(m.group(0)) - 2) + '"', n)
    res = [(k, s[a:b].strip(' ,'), False) for k, a, b in _find(masked)]
    for m in QUOTED.finditer(n):
        inner = s[m.start() + 1:m.end() - 1]
        res += [(k, inner[a:b].strip(' ,'), True) for k, a, b in _find(straight(inner))]
    return res


# H1 (Joel, 2026-10-06): "oh yeah that heading looks way ai for sure. always trying to do an x not y statement, isn't that
# on your tells list? humans don't do x not y as much." The published "The Medicine Part, Without Pretending It Isn't There"
# read AI with the paragraph after it in Pangram's web app, while that paragraph passed alone; his "The Medicine Part - Yes,
# I'm Naming It" passed. The linter dropped headings until then, so no rule ever saw one.
HEAD_XNOTY = re.compile(r"(?:,|\s[-—–:])\s*(?:without|not|never|no)\b|^(?:not|never)\b[^,]*,|\b(?:without pretending|not just|not only)\b", re.I)
HEAD_NEG = re.compile(r"\b(?:isn['’]t|aren['’]t|wasn['’]t|doesn['’]t|don['’]t|not|without)\b", re.I)
# O10 (Joel, 2026-10-06): "'Key here' can't be how you open a section. that's referring to something. Key where? what?"
# A trace had flagged its "here" as unanchored; the finding was kept and he caught it.
POINTER_FAIL = re.compile(r"^(?:the\s+)?key\s+(?:here|thing here|point here)\b|^here['’]?s the (?:thing|deal|key)\b|^here is the (?:thing|deal|key)\b", re.I)

# O14 (Joel, 2026-10-07 01:43, on section 7 P3): "you replaced commas and even 'or' with 'and and and and' that looks like
# emulate trying to cheat, and it wasn't needed. still passes pangram with normal syntax". Emulate's sentence was "It's not
# like calling something by a certain name dissolves the childhood panic and the comparison and the terror of abandonment
# and the desire to control another person." His: "...dissolves the childhood panic, the comparison, the terror of
# abandonment, or the desire to control another person." So a list keeps commas and its own "or". Counted per stretch of
# a sentence between punctuation marks: two repeats of the same "and" or "or" are a REVIEW, three a FAIL.
POLY_SPLIT = re.compile(r"[,;:()\[\]—–]|\s-\s|\s--\s")
def polysyndeton(s):
    """The longest chain of one conjunction repeated with short items between (six words or fewer; a pair counts only
    when the item between is three words or fewer), within a stretch between punctuation marks. "and who would notice
    and act" is a pair; "a relationship secret from the child's mother or another" is not a chain."""
    worst = 0
    for seg in POLY_SPLIT.split(QUOTED.sub(' ', s)):
        toks = re.findall(r"[\w'’]+", seg.lower())
        for conj in ('and', 'or'):
            idx = [i for i, t in enumerate(toks) if t == conj]
            run = 1; best = 1 if idx else 0
            for a, b in zip(idx, idx[1:]):
                gap = b - a - 1
                run = run + 1 if 1 <= gap <= 6 else 1
                best = max(best, run)
            if best == 2:
                pairs = [b - a - 1 for a, b in zip(idx, idx[1:])]
                if not any(1 <= g <= 3 for g in pairs):
                    best = 1
            worst = max(worst, best)
    return worst

# O15 (Joel, same message): "section 5 unusual spellings should help pass pangram, but that's also cheating i'd say, so
# you can fix them." His "priveleged", "contageous", "re-incarnation" and the like. A REVIEW, for his lines too: a coinage
# ("pl/ork", "technosphere") or a rare word stays; a misspelling or an odd hyphenation gets fixed, without a Pangram recheck
# (20:38: "no need to recheck pangram to fix a typo"). Needs pyspellchecker; without it the check is skipped and says so.
try:
    from spellchecker import SpellChecker
    _SPELL = SpellChecker()
except Exception:
    _SPELL = None
# prefixes whose closed form is the usual one ("re-incarnation", "pre-requisite", "contra-indications"); a compound like
# "grown-up" is left alone
HYPHEN_PREFIXES = {'re', 'pre', 'contra', 'co', 'non', 'anti', 'counter', 'inter', 'multi', 'semi', 'sub', 'super', 'un', 'over', 'under'}
def odd_spellings(s):
    if _SPELL is None:
        return []
    out = []
    for tok in re.findall(r"[A-Za-z][A-Za-z'’-]*[A-Za-z]", QUOTED.sub(' ', s)):
        if any(c.isupper() for c in tok) or '/' in tok:
            continue   # names, and coinages written with a slash
        t = re.sub(r"['’](s|t|re|ve|ll|d|m)$", '', tok.lower())
        if t.endswith("n") and tok.lower().endswith(("n't", "n’t")):
            continue
        if '-' in t:
            joined = t.replace('-', '')
            if t.split('-')[0] in HYPHEN_PREFIXES and _SPELL.known([joined]):
                out.append(tok + ' (the closed form "%s" is standard)' % joined)
            continue
        if len(t) > 3 and not _SPELL.known([t]):
            out.append(tok)
    return out

# O16 (Joel, same message, on section 6 P8 and P9): "i fixed p8p9, it was way overcompleting itself, now it passes pangram
# together". He cut the closing "These are all questions that a community should consider in advance." and a five-item
# list of protections. A REVIEW on a paragraph's last sentence when it sums the paragraph up. Cutting is his call: propose
# the cut with the passage quoted, don't make it.
SUMMARY_CLOSE = re.compile(r"^(?:these|those|all (?:of )?(?:these|those|this)|this|that)(?:\s+\w+){0,2}\s+(?:are|is|were)\s+all\b"
                           r"|^(?:all (?:of )?(?:these|those|this)|this is (?:all )?why|that['’]?s (?:all )?why|in short|in the end|"
                           r"ultimately|taken together|in sum|to sum up)\b", re.I)
# O17 (Joel, 2026-10-07 15:05, on community section 8 P18's "A scared or confused kid may get mixed up telling it and
# still need protection"): "Another AI tell is 'may be X and still Y' make sure that's in the shared tells list. Humans
# don't use that as much." The same section's P14 had "Fear like that can destroy that gift and still not prevent
# abuse". A REVIEW: say the two things plainly and keep the original's modal over both halves ("can destroy that gift,
# and it might not even prevent abuse" passed Pangram in the whole section and kept the possibility).
STILL_TAIL = re.compile(r"\b(?:may|might|can|could|will|would|should|must)\b[^.!?;:]{1,80}?\band\s+still\b", re.I)
POINTER_HEAD = re.compile(r"^(?:this|that|these|those|it|here|there|the other|another|such)\b(?!\s+(?:is a|are)\b)", re.I)

def heading_checks(raw):
    """Flags (severity, rule, text) for each markdown heading and the opener of the paragraph under it."""
    raw = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    blocks = []
    for b in (x.strip() for x in re.split(r'\n\s*\n', raw) if x.strip()):
        ls = b.split('\n')
        if len(ls) > 1 and re.match(r'^#+\s', ls[0]):      # a heading line with its paragraph right under it
            blocks += [ls[0], '\n'.join(ls[1:]).strip()]
        else:
            blocks.append(b)
    out = []
    for i, b in enumerate(blocks):
        m = re.match(r'^#+\s+(.*)$', b)
        if not m:
            continue
        h = m.group(1).strip()
        hn = straight(h)
        if HEAD_XNOTY.search(hn):
            out.append(('FAIL', 'H1 x-not-y heading (Joel 2026-10-06: "always trying to do an x not y statement ... humans don\'t do x not y as much"; 2026-10-07: "should be fully banned"); name the thing, as his "The Medicine Part - Yes, I\'m Naming It"', h))
        elif HEAD_NEG.search(hn):
            out.append(('REVIEW', 'H1 a negation in a heading: check it isn\'t an x-not-y frame (Joel 2026-10-06)', h))
        for sev, rule in emoji_flags(h):   # O26: a heading's emoji is on the allowlist too
            out.append((sev, rule, h))
        for nb in blocks[i + 1:]:
            if re.match(r'^#+\s', nb):
                break
            t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', nb).replace('*', '').strip()
            if not t or t.startswith('![') or re.match(r'^image \d+$', t, re.I) or (len(t.split()) <= 3 and not t.endswith(('.', '?', '!'))):
                continue
            first = sentences(t)[0] if sentences(t) else t
            if POINTER_HEAD.match(straight(first)) and not POINTER_FAIL.match(straight(first)):
                out.append(('REVIEW', 'O10 the first sentence under a heading opens with a pointer: say what it points at, since nothing above it in the section does (Joel 2026-10-06, on "Key here": "that\'s referring to something. Key where? what?")', first))
            break
    return out


# ---- 2026-10-11: the tells the linter didn't check (TELLS-COVERAGE-20261011.md, table 1). Each is in tells_registry.json
# with its source and an example, and the module docstring says where each comes from. All match straight(sentence).
# O22: first-person staging (AGENTS.md "Code review rules"; SKILL.md "Fake personal stake"). "I want" at a sentence's
# start is O20's; these are the other forms the two files name.
STAGING = re.compile(r"\bI care about\b|\bI(?:'d| would) want to see\b|\bthat tells me\b"
                     r"|\bthat(?:'s| is) where\b[^.?!]{1,60}?\bmatters? (?:to|for) me\b"
                     r"|\b(?:this|that|it) is (?:one|another|the) reason (?:why )?I want\b"
                     r"|\bthe version I want is\b|\bwhat matters (?:most )?to me is\b", re.I)
# O23: research notes told as narration (AGENTS.md, "Research-process compression gate"). "I thought" alone is too common
# to flag; it's flagged in a paragraph that also narrates the check, where it starts the diary.
RESEARCH_NOTE = re.compile(r"\bI(?:'d| had) heard\b|\bI (?:double-)?checked\b|\bI looked (?:it|this|that) up\b"
                           r"|\bthe check I did\b|\bI wasn't sure what the (?:term|word|name)\b", re.I)
RESEARCH_THOUGHT = re.compile(r"\bI (?:had )?thought\b", re.I)

def without_quotes(n):
    """n (straight quotes) with the words in double quotes taken out, for the first-person rules. sentences() drops a
    closing quote at the end of a sentence, so an odd last quote runs to the end."""
    return QUOTED.sub('""', n + '"' if n.count('"') % 2 else n)

# O24: stock lines (the gate's 2026-10-10 prediction review). "sure. But", from the same list, is O2's.
STOCK_LINE = re.compile(r"\bI see the need (?:to|for)\b|\bit(?:'s| is) also important to\b|\bone thing to (?:notice|note) about\b", re.I)
# O25: "even" and "actually" (TELLS-FROM-PANGRAM-DATA-20261007.md, finding 3). Not "even if"/"even though" (B1), and not
# an "Even" that opens a sentence (finding 4: it went with the passing drafts).
EVEN_ACTUALLY = re.compile(r"\bactually\b|\beven\b(?!\s+(?:if|though)\b)", re.I)
# O28: "It's one thing to X. It's another to Y", in one sentence or across two (JOEL-FIXES-CATALOGUE, Joel's fixes of
# 2026-10-02, community section 3 P6: "A contrast has to say which side is true.").
ONE_THING = re.compile(r"\bit(?:'s| is) one thing to\b[^.?!;]{1,150}?[.?!;,]['\"]?\s+(?:but\s+)?(?:it|that)(?:'s| is) "
                       r"(?:quite )?(?:another|a different (?:thing|matter|story)|something else)\b", re.I)
# O29: a question ends with "?", a closing quote or bracket allowed after it.
QUESTION_END = re.compile(r"\?[\"')\]]*$")
# O31 and O32: from the window Pangram flagged in Minimal-fix lesson 1 (JOEL-FIXES-CATALOGUE).
WHEN_DONT = re.compile(r"^(?:(?:and|but|so|or)\s+)?when\b[^.?!]{1,120}?,\s*(?:don't|do not|never)\b", re.I)
KIND_OF_WHOLE = re.compile(r"\b(?:a|one) kind of\b[^?!]{1,60}?\bbut\b[^.?!]{0,30}?\bnot the whole\b", re.I)
# O33: the stock casual moves (gate, "Repairing a failed draft").
STOCK_CASUAL = re.compile(r"^(?:nope[.!]+$|aww+[,.!]?\s+buddy\b)", re.I)
# O34, O35, O36: fixed phrases (JOEL-FIXES-CATALOGUE "In his words"; gate step 2; the gate's prediction review).
WOULDNT_CALL = re.compile(r"\bI (?:wouldn't|would not) call (?:that|this|it)\b", re.I)
WITH_OR_WITHOUT = re.compile(r"\bwith or without\b", re.I)
BUT_ALSO = re.compile(r"\bbut also\b", re.I)

# O26: emoji (gate step 9, "Joel's bans and the allowlist"; tools/humanization/EMOJI-LIST.md). An emoji is a pictograph
# (U+1F000 to U+1FAFF), a symbol drawn as an emoji (followed by U+FE0F or a skin tone), or one of the symbols that are
# emoji by default (⚡ ✨ ✅ ❌ ⭐ and the like), with its skin tone and any zero-width-joined parts (🧘🏿‍♀️ is one).
_EMOJI_BASE = (r'[\U0001F000-\U0001FAFF]'
               r'|[\U000000A9\U000000AE\U00002000-\U00002BFF\U00003030\U0000303D\U00003297\U00003299](?=\U0000FE0F|[\U0001F3FB-\U0001F3FF])'
               r'|[\U0000231A\U0000231B\U000023E9-\U000023EC\U000023F0\U000023F3\U000025FD\U000025FE\U00002614\U00002615\U0000261D'
               r'\U00002648-\U00002653\U0000267F\U00002693\U000026A1\U000026AA\U000026AB\U000026BD\U000026BE\U000026C4\U000026C5'
               r'\U000026CE\U000026D4\U000026EA\U000026F2\U000026F3\U000026F5\U000026FA\U000026FD\U00002705\U0000270A\U0000270B'
               r'\U00002728\U0000274C\U0000274E\U00002753-\U00002755\U00002757\U00002795-\U00002797\U000027B0\U000027BF'
               r'\U00002B1B\U00002B1C\U00002B50\U00002B55]')
_EMOJI_PART = r'(?:' + _EMOJI_BASE + r')\U0000FE0F?[\U0001F3FB-\U0001F3FF]?[\U000E0020-\U000E007F]*'
EMOJI = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}|' + _EMOJI_PART +
                   r'(?:\U0000200D[\U0001F000-\U0001FAFF\U00002000-\U00002BFF]\U0000FE0F?[\U0001F3FB-\U0001F3FF]?)*')
POINTER_EMOJI = set('\U0001F447\U0001F449\U0001F446\U0001F448\U0000261D')   # 👇 👉 👆 👈 ☝
EMOJI_LIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'EMOJI-LIST.md')
_ALLOWED = None

def _emoji_key(e):
    return e.replace(chr(0xFE0F), '').replace(chr(0xFE0E), '')   # the variation selectors: ❤️ and ❤ are one emoji

def emoji_allowlist():
    """The emoji in EMOJI-LIST.md's "## Allowlist" section: his list, his own placements and each later yes, read from the
    file so a yes he gives there counts at once. A line that tells of a wrong guess is skipped (the 🫩 bullet). None
    when the file isn't there; then only the pointers and 😉 are checked."""
    global _ALLOWED
    if _ALLOWED is None:
        try:
            md = open(EMOJI_LIST, encoding='utf-8').read()
        except OSError:
            _ALLOWED = False
        else:
            m = re.search(r'^## Allowlist.*?(?=^## |\Z)', md, re.S | re.M)
            _ALLOWED = {_emoji_key(e) for line in (m.group(0) if m else '').split('\n') if 'guessed' not in line
                        for e in EMOJI.findall(line)}
    return _ALLOWED or None

def emoji_flags(s):
    """[(severity, rule)] for the emoji in s: a pointer, 😉, or one off the allowlist; one flag of each kind."""
    out, allowed = [], emoji_allowlist()
    for e in EMOJI.findall(s):
        k = _emoji_key(e)
        if k[0] in POINTER_EMOJI:
            f = ('FAIL', 'O26 owner ban: a pointer emoji (👇 👉 👆 👈 ☝️; Joel 2026-10-01: "i don\'t want those pointer emojis those look super ai, only after seen them from ai slop, don\'t ever use those")')
        elif k == '\U0001F609':
            f = ('FAIL', 'O26 owner ban: 😉 (Joel 2026-10-01: "that one also looks like mainly used by AI (or by scammers)")')
        elif allowed is not None and k not in allowed:
            f = ('FAIL', 'O26 an emoji off the allowlist in tools/humanization/EMOJI-LIST.md (gate step 9: "everything else counts as banned until Joel says yes"); take it out, or ask him about that one')
        else:
            continue
        if f not in out:
            out.append(f)
    return out

# O27: rough edges in my text (JOEL-FIXES-CATALOGUE "What he adds" 9). An end mark is . ! ? … : or ;, before any closing
# quotes or brackets; an emoji or an ASCII face can end a paragraph too.
DOUBLE_SPACE = re.compile(r'(?<=\S) {2,}(?=\S)')
END_MARK = re.compile(r'(?:[.!?…:;]|[:;]-?[()DPp]|' + _EMOJI_PART + r')[\s"\')\]*_]*$')

def sentence_spans(p, ss):
    """(start, end) of each sentence of paragraph p in p with its whitespace collapsed, the text sentences() splits."""
    cp, spans, cur = re.sub(r'\s+', ' ', p), [], 0
    for s in ss:
        k = cp.find(s, cur)
        k = cur if k < 0 else k
        spans.append((k, k + len(s)))
        cur = k + len(s)
    return spans

# O30: a phrase said three or more times in one paragraph (gate, 2026-10-07 20:21; JOEL-FIXES-CATALOGUE, P22). A phrase is
# two to four words with a content word in it; a hyphenated word is one word. Left out: a phrase that opens with "the",
# "a" or a possessive, or always comes right after one, since that's a thing named again ("the community"; "your little
# one", the Inner Child article's word for the reader's inner child, was 38 of the first 43 hits on the calibration texts),
# and an occurrence that opens a sentence (a run of parallel questions is O29's). "ability to" four times in a list of
# rights, twice as "the ability to", still counts.
PHRASE_SKIP_FIRST = set('the a an this that these those my your his her its our their'.split())

def repeated_phrases(ss, mine):
    """[(phrase, count, [sentence indexes])] for each phrase said three or more times in a paragraph's sentences ss, at
    least once in a sentence of mine; the longest form of each, not its parts."""
    toks = [re.findall(r"[a-z]+(?:['-][a-z]+)*", straight(s).lower()) for s in ss]
    found = {}
    for n in (4, 3, 2):
        counts = {}
        for i, t in enumerate(toks):
            for j in range(1, len(t) - n + 1):   # j = 0 opens the sentence
                g = tuple(t[j:j + n])
                if g[0] in PHRASE_SKIP_FIRST or not any(w not in STOP and len(w) > 2 for w in g):
                    continue
                counts.setdefault(g, []).append((i, t[j - 1] in PHRASE_SKIP_FIRST))
        for g, occ in counts.items():
            where = [i for i, _ in occ]
            if len(where) >= 3 and not all(named for _, named in occ) and any(mine[i] for i in where):
                phrase = ' '.join(g)
                # "them as adults" three times holds "as adults" three times: report the longer one only, unless the
                # shorter one is said more often
                if not any(' ' + phrase + ' ' in ' ' + longer + ' ' and len(where) <= c for longer, (c, _) in found.items()):
                    found[phrase] = (len(where), sorted(set(where)))
    return [(ph, c, w) for ph, (c, w) in found.items()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('draft'); ap.add_argument('--source')
    ap.add_argument('--owner'); ap.add_argument('--quiet', action='store_true')
    ap.add_argument('--installed', help='the article as installed: its sentences passed already and get no flags')
    a = ap.parse_args()
    raw = open(a.draft, encoding='utf-8').read()
    text = clean(raw)
    owner = set()
    if a.owner:
        owner = {re.sub(r'\s+', ' ', l.strip()) for l in open(a.owner, encoding='utf-8') if l.strip()}
    # --installed (2026-10-03): a section check holds paragraphs that already passed alone and in their sections,
    # some with two lists of three (the When the Adult Voice Feels Fake opening, Love Doesn't Wait P12). Their sentences
    # are treated like the owner's: counted in the metrics, never flagged, so only the new text can fail.
    old = set()
    if a.installed:
        old = {re.sub(r'\s+', ' ', x) for q in paragraphs(clean(open(a.installed, encoding='utf-8').read())) for x in sentences(q)}
    known = owner | old
    def is_known(x):
        # An owner file can hold whole paragraphs, one per line (the calibration .owner files do); until
        # 2026-10-03 only a sentence that was a whole line matched, so his multi-sentence paragraphs were
        # flagged as mine. A sentence of three words or more inside one of his lines is his.
        n = re.sub(r'\s+', ' ', x)
        return n in known or (len(n.split()) >= 3 and any(n in l for l in owner))
    # chat acronyms the source or the owner lines already use are the article's own register (Joel, 2026-10-01 18:19);
    # read in any case since 2026-10-11 (O37: "lol" got through in lower case)
    src_acronyms = set()
    for extra in ([open(a.source, encoding='utf-8').read()] if a.source else []) + list(owner):
        src_acronyms |= {x.upper() for x in re.findall(ACRONYMS, extra, re.I)}
    ps = paragraphs(text)
    allw = words(straight(text)); nw = len(allw) or 1
    flags = []   # (severity, rule, sentence)
    def flag(sev, rule, s): flags.append((sev, rule, s))
    # H1 and O10 (2026-10-06): headings and the opener under each, from the raw markdown. A heading or opener the owner
    # wrote, or one already installed, isn't flagged.
    installed_raw = open(a.installed, encoding='utf-8').read() if a.installed else ''
    for sev, rule, x in heading_checks(raw):
        if x in installed_raw or is_known(x):
            continue
        flag(sev, rule, x)
    # O19 (2026-10-07): a bulleted or numbered list in the draft, once per list; a list the owner wrote or that's installed isn't flagged
    body = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    in_list = False
    for line in body.split('\n'):
        if LIST_LINE.match(line):
            item = re.sub(r'^\s*(?:[-*+•]|\d+[.)])\s+', '', line).strip()
            if not in_list and not (item in installed_raw or is_known(item)):
                flag('REVIEW', 'O19 a list (Joel 2026-10-07: "lists of 3 especially, and lists in general are overused by AI. try to avoid that unless it\'s really needed"): keep it only if the meaning really needs it', item)
            in_list = True
        elif line.strip():
            in_list = False
    mine_words = 0; coach_hits = 0; you_hits = 0
    para_final_short = 0; imper_heavy = 0
    openers = []
    sent_lens = []
    casual = []   # O25: (sentence, count) of "even" and "actually" in my sentences, flagged once the draft's count is known
    for p in ps:
        ss = sentences(p)
        # The rules match nss, the sentences with straight quotes; the flags quote ss, as written (2026-10-11).
        nss = [straight(x) for x in ss]
        mine_s = [not is_known(x) for x in ss]
        openers.append(' '.join(words(nss[0])[:1]).lower() if ss else '')
        imps = 0
        plists = []   # (mine, excerpt) for each list of three outside a quote (E125)
        checked = any(m and RESEARCH_NOTE.search(without_quotes(x)) for x, m in zip(nss, mine_s))   # O23: the paragraph narrates a check
        for i, s in enumerate(ss):
            n = nss[i]
            nxt = nss[i + 1] if i + 1 < len(ss) else None
            pair = n if nxt is None else n + ' ' + nxt   # for the rules that read a sentence with the next one
            def spans_next(mt):
                """For a match on pair: None if it doesn't start in this sentence, else what to quote (this sentence, or
                both when it runs into the next one); False when the next one is his."""
                if not mt or mt.start() >= len(n):
                    return None
                if mt.end() <= len(n):
                    return s
                return s + ' ' + ss[i + 1] if mine_s[i + 1] else False
            for o in odd_spellings(s):
                flag('REVIEW', 'O15 unusual spelling or hyphenation, his lines included (Joel 2026-10-07: "unusual spellings should help pass pangram, but that\'s also cheating"); a coinage or a rare word stays, a misspelling gets fixed: ' + o, s)
            mine = mine_s[i]
            w = words(n); sent_lens.append(len(w))
            tri = triads(s)
            plists += [(mine, x) for k, x, q in tri if not q]
            if not mine: continue
            for k, x, q in tri:
                flag('REVIEW', 'E125 list of three' + (' inside a quote (someone else\'s words can keep theirs)' if q else '') +
                     ': an AI pattern in general (Joel 2026-10-03: "lists of 3 in general are an ai pattern"; 2026-10-07: "lists in general are overused by AI. try to avoid that unless it\'s really needed"). If the meaning doesn\'t need '
                     'all three, drop the one that matters least; if it does, split them into sentences, the way he fixed P1 ("Maybe it just '
                     'has something to say."). Joel, 01:06: "when there\'s no actual need for 3 items you can remove one of them"', x)
            mine_words += len(w)
            for r in TICS:
                if re.search(r, n, re.I): flag('FAIL', 'B11 tic', s)
            q11 = spans_next(B11_NOT_ITS.search(pair) or B11_POINT_IS.search(pair))
            if q11:
                flag('FAIL', 'B11 tic: "That\'s not X. It\'s Y." and its cousins across two sentences (owner_bans.txt, Joel\'s Claude tics; JOEL-FIXES-CATALOGUE "What he cuts" 2: "The point is not perfect measurement. The point is pattern recognition." became "You won\'t measure stuff perfectly, but this way you might start seeing some important patterns jump out."); say what it is', q11)
            for mg in GETS_TO.finditer(n):
                subj = gets_to_subject(n, mg)
                if subj == 'thing':
                    flag('FAIL', 'O1 owner ban: "doesn\'t get to decide" family with a subject that isn\'t a person (Joel 2026-09-28: "humans just rarely use [it] for non-humans"; 2026-10-07: "\'the weather doesn\'t get to decide\' for example, not \'your dad doesn\'t get to decide\'")', s)
                elif subj == 'unclear':
                    flag('REVIEW', 'O1 "gets to" with an unclear subject: a person can stay, a feeling, part, thought or thing can\'t (Joel 2026-10-07)', s)
                break
            # O2: "Fine," as a clause, "Fine." or "Sure." as a sentence of its own (owner_bans.txt), and "…, sure. But" across the
            # split (2026-10-11; the gate's prediction review: "sure. But"). The split had cut "Sure. But" and "Fine. They're…" apart.
            o2 = None
            if re.search(r"(^|[.!?]\s+)(Fine|Good|Great|Sure|Okay|OK|Fair enough)[,.!]\s", n) or re.fullmatch(r"(?:Fine|Good|Great|Sure|Okay|OK|Fair enough)[.!]+", n.strip()):
                o2 = s
            elif nxt is not None and re.search(r",\s*(?:sure|fine)[.!]$", n, re.I) and re.match(r"But\b", nxt):
                o2 = s + ' ' + ss[i + 1]
            if o2:
                flag('FAIL', 'O2 owner ban: "Fine," "Good," "Great," "Sure" as a clause or a sentence of its own, and "sure. But" (Joel 2026-09-28: "i told you to stop saying \'Fine, Good, Great\' as clauses before"; the gate\'s 2026-10-10 prediction review: "sure. But")', o2)
            # E139 (2026-10-07): SKILL.md's "Synthetic specificity and fake concreteness" rule was never loaded here (O11 to O13; main's O8 to O10 came first).
            if re.search(r"\b(Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)days?\b", n):
                flag('FAIL', 'O11 owner ban: a weekday put in to sound concrete (Joel 2026-10-07: "AI is always saying Tuesday, on Tuesday, '
                     'or some specific day like this. on a regular Tuesday is the worst"; SKILL.md "Synthetic specificity"). Keep one only '
                     'when it is a real fact from the source and matters to the thought', s)
            if re.search(r"\b(ordinary|regular|boring|everyday|mundane|quietly)\b", n, re.I):
                flag('REVIEW', 'O12 "ordinary/regular/boring/quietly": overused by AI, not a sure tell (Joel 2026-10-07 03:24: "boring, regular etc are not '
                     'for sure AI tells, almost nothing is a for sure AI tell, but they are way overused by AI"; 2026-10-10 12:22, on "shouldn\'t quietly turn into": "using quietly all the time like that is a huge AI tell"); keep one that says something, judge published wording like new wording', s)
            # O20 (Joel 2026-10-10 12:22): "I want / I don't want" as the opener of a stance. SKILL.md has the rule; his 2026-10-02 exception for the
            # community article (his own wish to live in one) stands, "but there's just too much of this". A list fits: the opener is a fixed form.
            # "I'd like" (2026-10-11): the branch was "I 'd like", with a space no one types, so it never matched.
            if re.search(r"(^|[.!?]\s+)I(?: (?:don't |do not )?(?:want|wish|would like)|'d like)\b", n):
                flag('REVIEW', 'O20 "I want / I don\'t want" opening a stance (SKILL.md; Joel 2026-10-10: "i want/don\'t want which is in the tells list ... you can use i want sometimes when it makes real sense because i actually do want to find a commune to live in, but there\'s just too much of this"): keep it only where his own wish is the subject, else state the judgment', s)
            # O21 (Joel 2026-10-10 12:22, on "I don't want one super-commune with a nicer logo": "an AI-tell quip"). Stock comparison quips only;
            # whether some other line is a quip is a reader's call, not this list's.
            if re.search(r"\bwith (a |an )?(nicer|better|fancier|shinier|prettier|new) (logo|name|label|branding|font|website|mission statement)\b|\bwith extra steps\b", n, re.I):
                flag('REVIEW', 'O21 a stock comparison quip ("X with a nicer logo", "X with extra steps"; Joel 2026-10-10: "an AI-tell quip"): say what it claims plainly, or cut it if the point is carried elsewhere', s)
            if re.search(r"\b\d+\s*(%|percent)|\b(one|two|three|four|five|ten|twenty|fifty)\s+percent\b|\bo['’]clock\b|\b\d{1,2}(:\d\d)?\s?(am|pm)\b|"
                         r"\bby (lunch|dinner|noon|bedtime|lunchtime)\b|\b(a|one|this|that) (morning|afternoon|evening) of\b", n, re.I):
                flag('REVIEW', 'O13 a made-up number or clock time (Joel 2026-10-07, on "five percent is enough": "AI wants to put concrete '
                     'numbers on stuff all the time, then people are wondering how much is 5%?"; SKILL.md: no invented clock-time details)', s)
            if re.search(r"\b(my first (guess|thought|instinct|reaction)|I'd probably want to|I'd be tempted to|my instinct would be)\b", n, re.I):
                flag('REVIEW', 'E138 the writer\'s own impulse: check the next sentence doesn\'t take it back (Joel 2026-10-07, on "I\'d probably '
                     'want to fix it by saying sweeter and sweeter things, which won\'t work": "this part is contradictory"; his fix gave '
                     'the move to "some people")', s)
            ag = abstract_agents(n)  # None without the parser: then the word list decides
            if (ag if ag is not None else re.search(ABSTRACT_AGENT, n, re.I)):
                flag('REVIEW', 'O6 a candidate, to judge, not a finding: a feeling or idea doing what a person does. A neat, quotable line is the tell ("Grief doesn\'t keep a schedule"); a phrase people say all the time is not (Joel 2026-10-07 23:50: "Modern life trains us" is "so common it\'s almost cliche, it\'s not a witty AI quip"). Judge each with abstract_agents_prompt.py or by his ratings; fix only a quip, giving the action to a person with as few words changed as possible', s)
            if re.search(ENOUGH_PAIR, n, re.I):
                flag('REVIEW', 'O7 polished "X enough to… Y enough to…" pair (Joel 2026-10-02: "devoted enough to practice them and secure enough to disagree" "looks super highly polished")', s)
            if re.search(SMUGGLE_FIG, n, re.I):
                flag('FAIL', 'O8 owner ban: smuggling talk (Joel 2026-10-03: "ai is always saying something like \'not smuggle in\' or something about smuggling in"; 2026-10-07: "should be fully banned"); say the plain reason, as his "My reasons are given in those articles, respectively, since they need more space."', s)
            elif re.search(SMUGGLE, n, re.I):
                flag('REVIEW', 'O8 "smuggle": literal smuggling can stay; the figurative kind is an owner ban (Joel 2026-10-03)', s)
            if i == 0 and POINTER_FAIL.match(n.strip()):
                flag('FAIL', 'O10 an opener that points at nothing (Joel 2026-10-06: "\'Key here\' can\'t be how you open a section. that\'s referring to something. Key where? what?"): start with the claim itself, as his "Most of the writing on communities hasn\'t caught up with psychedelics."', s)
            m9 = NOT_TAIL.match(n.strip())
            if m9 and len(words(m9.group('head'))) >= 4:
                flag('REVIEW', 'O9 a "not Y" tail on a finished claim (Joel 2026-10-03: "it always wants to add a \'not Y\' part"): say the claim or the reason plainly; keep the contrast only when the paragraph needs the other side said', s)
            if NOT_BUT_STILL.search(n):
                flag('REVIEW', 'O18 "not X, but still Y" (Joel 2026-10-07: "there are other X Y rules, like \'Not x, but still y.\'"): say the claim plainly; keep the contrast only when the reader needs the other side said', s)
            elif nxt is not None and NOT_SENT.search(n) and STILL_NEXT.match(nxt.strip()) and mine_s[i + 1]:
                flag('REVIEW', 'O18 "not X. It still Y" across two sentences (Joel 2026-10-07: "there are other X Y rules, like \'Not x, but still y.\'")', s + ' ' + ss[i + 1])
            for r in CONTRAST:
                if re.search(r, n, re.I): flag('REVIEW', 'B2 contrast', s); break
            for r in THESIS:
                if re.search(r, n, re.I if not r.startswith('^') else 0): flag('REVIEW', 'B1 finished principle', s); break
            for r in ANNOUNCE:
                if re.search(r, n): flag('REVIEW', 'B5 announces the paragraph', s); break
            hits = sum(len(re.findall(r, n, re.I)) for r in COACH)
            coach_hits += hits
            if hits: flag('REVIEW', 'E41 coach phrase', s)
            you_hits += len(re.findall(r"\byou(r|'re|'ll|'d|'ve)?\b", n, re.I))
            if re.search(r"\bthe kid\b|\bkids?\b", n, re.I): flag('REVIEW', 'E1 kid', s)
            # O37 (the chat-acronym flag, numbered 2026-10-11): any case, so "lol" is caught; "lol" itself is banned, the rest
            # are a REVIEW where the source doesn't use them.
            acrs = re.findall(ACRONYMS, n, re.I)
            if any(x.lower() == 'lol' for x in acrs):
                flag('FAIL', 'O37 owner ban: "lol" (gate step 9: ""lol" is wry, so it\'s out"; Joel 2026-10-01: "lol is different from hehe, it\'s more wry."); "(hehe)" is fine', s)
            if any(x.lower() != 'lol' and x.upper() not in src_acronyms for x in acrs):
                flag('REVIEW', 'O37 chat acronym the source doesn\'t use: say it in words, unless the author asked for an informal internet style (Joel 2026-10-01: "for articles where the acronyms are used, you\'d use those, but for other articles where they aren\'t used, you wouldn\'t put them in")', s)
            first = (w[0].lower() if w else '')
            if first in IMPER: imps += 1
            if n.count(',') >= 3 or len(re.findall(r'\b(or|and)\b', n)) >= 3:
                flag('REVIEW', 'B4/E15 list or packed sentence', s)
            ps_n = polysyndeton(n)
            if ps_n >= 3:
                flag('FAIL', 'O14 owner ban: an "and ... and ... and" list (Joel 2026-10-07: "that looks like emulate trying to cheat, and it wasn\'t needed. still passes pangram with normal syntax"); use commas and keep the list\'s own "or"', s)
            elif ps_n == 2:
                flag('REVIEW', 'O14 two repeated "and"s or "or"s in one stretch: fine in speech ("bread and butter and jam"), Emulate\'s trick in a list (Joel 2026-10-07)', s)
            if i == len(ss) - 1 and len(ss) >= 3 and SUMMARY_CLOSE.match(n.strip()):
                flag('REVIEW', 'O16 a closing line that sums the paragraph up (Joel 2026-10-07: "it was way overcompleting itself"): propose the cut to him, quoted, with your opinion; don\'t cut it yourself', s)
            if STILL_TAIL.search(n):
                flag('REVIEW', 'O17 "may be X and still Y" (Joel 2026-10-07 15:05: "Another AI tell is \'may be X and still Y\' ... Humans don\'t use that as much"): say both things plainly and keep the modal over both halves', s)
            if i < 2 and re.search(r"\b(did|do|does|doing|done|didn't|don't|tried|try|skip|skipped|finish|finished|start|started)\s+it\b", ' '.join(n.split()[:8]), re.I):
                flag('REVIEW', 'R1 action "it" near a paragraph start: name the thing (Joel 2026-09-30, on "If you did it": "the first it is unclear referent")', s)
            if i > 0 and len(w) <= 6 and len(words(nss[i-1])) >= 12 and re.match(r"(But|That|It|So|And|Which|They)\b", n):
                flag('REVIEW', 'B3 short knock-down', s)
            # ---- 2026-10-11: the tells the linter didn't check (TELLS-COVERAGE-20261011.md, table 1)
            unquoted = without_quotes(n)   # quoted words are someone's speech: AGENTS.md exempts "Quotation or literal discussion"
            if STAGING.search(unquoted):
                flag('REVIEW', 'O22 first-person staging (AGENTS.md: "Treat significance-staging constructions such as `That\'s where X matters to me` ... as AI-shaped in Joel-byline prose"; SKILL.md: "`I care about...`, `I\'d want to see...`, `that tells me...`, and close variants are AI-shaped"): state the consequence or the judgment itself, unless his own wish is the subject', s)
            if RESEARCH_NOTE.search(unquoted) or (checked and RESEARCH_THOUGHT.search(unquoted)):
                flag('REVIEW', 'O23 research notes told as narration (AGENTS.md: "Do not automatically convert research notes such as `I thought X`, `I had heard Y`, `I checked it` ... into article narration"): give the result, unless the checking itself does a job for the reader', s)
            if STOCK_LINE.search(unquoted):
                flag('REVIEW', 'O24 a stock line (the gate\'s 2026-10-10 prediction review: "stock lines like "I see the need to", "It\'s also important to", "One thing to notice about""): say the thing itself', s)
            k_casual = sum(1 for m in EVEN_ACTUALLY.finditer(n) if not (m.group(0).lower() == 'even' and not n[:m.start()].strip(' "\'([')))
            if k_casual:
                casual.append((s, k_casual))
            for sev, rule in emoji_flags(n):
                flag(sev, rule, s)
            q28 = spans_next(ONE_THING.search(pair))
            if q28:
                flag('REVIEW', 'O28 "It\'s one thing to X. It\'s another to Y" (JOEL-FIXES-CATALOGUE: Emulate\'s "one thing ... another thing" "is not quite showing that the truth was Y not X"; "A contrast has to say which side is true."): say what was really going on', q28)
            q32 = spans_next(KIND_OF_WHOLE.search(pair))
            if q32:
                flag('REVIEW', 'O32 "is a kind of X, but it\'s not the whole thing" (JOEL-FIXES-CATALOGUE, Minimal-fix lesson 1: one of the lines in the window Pangram flagged)', q32)
            if STOCK_CASUAL.match(n.strip()):
                flag('REVIEW', 'O33 a stock casual move (gate: "The stock casual moves a model reaches for when told to sound casual ("Nope.", "Aww, buddy.", a goofy exclamation, a punchy closer) came back 100% AI, high, in eight versions")', s)
            if WOULDNT_CALL.search(unquoted):
                flag('REVIEW', 'O34 "I wouldn\'t call that X" (Joel 2026-09-26: "Ai stuff overuses \'i wouldn\'t call that X\'"): say what it is', s)
            if WITH_OR_WITHOUT.search(n):
                flag('REVIEW', 'O35 "with or without X" (Joel 2026-10-02: "with or without X is not quite guidance"): say what X is good for', s)
            if BUT_ALSO.search(n):
                flag('REVIEW', 'O36 a "but also" pair (the gate\'s 2026-10-10 prediction review: one of the tells a fragile pass carried, with "the boring problem" and the "nicer logo" quip)', s)
        if len(plists) >= 2 and any(m for m, _ in plists):
            flag('FAIL', 'E125 two lists of three in one paragraph (Joel 2026-10-03, on P1 at 66% AI: "P! failed b ecause it has 2 lists of 3"); '
                 'fix one first: drop the item that matters least, or if every item is needed, split it into sentences the way he did', ' / '.join(x for _, x in plists))
        if ss and len(words(nss[-1])) <= 9 and mine_s[-1]:
            para_final_short += 1; flag('REVIEW', 'B7 short landing at paragraph end', ss[-1])
        if imps >= 2: imper_heavy += 1; flag('REVIEW', 'E23 paragraph of instructions', p[:90] + '...')
        # O27: rough edges in my text, never in his lines or installed ones (JOEL-FIXES-CATALOGUE: "Rough edges he leaves:
        # typos, double spaces, missing periods. These come from typing. They aren't something for me to imitate.")
        spans, seen = sentence_spans(p, ss), set()
        for m in DOUBLE_SPACE.finditer(p):
            pos = len(re.sub(r'\s+', ' ', p[:m.start()]))   # where the gap is in the collapsed paragraph the spans index
            at = tuple(j for j, (a0, b0) in enumerate(spans) if a0 <= pos < b0) or \
                tuple([j for j, (a0, b0) in enumerate(spans) if b0 <= pos][-1:] + [j for j, (a0, b0) in enumerate(spans) if a0 > pos][:1])
            if at and at not in seen and all(mine_s[j] for j in at):
                seen.add(at)
                flag('REVIEW', 'O27 a rough edge in my text: two spaces in a row (JOEL-FIXES-CATALOGUE: "Rough edges he leaves: typos, double spaces, missing periods. ... They aren\'t something for me to imitate.")', ' '.join(ss[j] for j in at))
        if ss and mine_s[-1] and not LIST_LINE.search(p) and not re.match(r'(?:\||>|```)', p) \
                and not re.search(r'https?://\S+$', p.rstrip()) and not END_MARK.search(straight(p.rstrip())):
            flag('REVIEW', 'O27 a rough edge in my text: the paragraph ends with no period (JOEL-FIXES-CATALOGUE: "Rough edges he leaves: typos, double spaces, missing periods. ... They aren\'t something for me to imitate.")', ss[-1])
        # O29: three or more questions in a row (gate step 7: "a few shared AI micro-patterns (question runs, triads, "isn't X,
        # it's Y")"), once per run.
        run = []
        for j in range(len(ss) + 1):
            if j < len(ss) and QUESTION_END.search(nss[j].rstrip()):
                run.append(j)
                continue
            if len(run) >= 3 and any(mine_s[k] for k in run):
                flag('REVIEW', 'O29 a run of three or more questions (gate step 7: "a few shared AI micro-patterns (question runs, triads, "isn\'t X, it\'s Y")"; its prediction review: "questions the text answers itself"): keep the ones a reader would ask', '%d questions: %s' % (len(run), ' '.join(ss[k] for k in run)))
            run = []
        # O30: a phrase said three or more times in one paragraph, his and mine together (gate 2026-10-07 20:21: my "a commitment
        # they make as adults" "gave P22 its fourth "as adults"")
        for phrase, c, at in repeated_phrases(ss, mine_s):
            flag('REVIEW', 'O30 a phrase said three or more times in one paragraph (gate, 2026-10-07: my "a commitment they make as adults" "gave P22 its fourth "as adults""; Joel: "take out second adults that\'s obvious"): keep it only where the repeat does a job', '"%s" %d times: %s' % (phrase, c, ' / '.join(ss[k] for k in at)))
        # O31: two parallel "When…, don't…" lines in a paragraph (JOEL-FIXES-CATALOGUE, Minimal-fix lesson 1)
        wd = [j for j in range(len(ss)) if WHEN_DONT.match(nss[j].strip())]
        if len(wd) >= 2 and any(mine_s[j] for j in wd):
            flag('REVIEW', 'O31 parallel "When…, don\'t…" lines (JOEL-FIXES-CATALOGUE, Minimal-fix lesson 1: the window Pangram flagged held "two parallel "When…, don\'t…" lines"): break the pattern, or keep one', ' / '.join(ss[j] for j in wd))
    # O25 (2026-10-11): "even" and "actually", with the draft's count (TELLS-FROM-PANGRAM-DATA-20261007.md, finding 3)
    if casual:
        o25 = ('O25 "even" or "actually", %d in my text (TELLS-FROM-PANGRAM-DATA-20261007.md: they go with the failing paragraphs; '
               '"They\'re words I add to sound casual, and they don\'t help"): keep one only where it says something' % sum(k for _, k in casual))
        for s, _ in casual:
            flag('REVIEW', o25, s)
    # paragraph-level metrics
    plen = [len(words(straight(p))) for p in ps]
    cv_p = (pstdev(plen)/mean(plen)) if len(plen) > 1 and mean(plen) else 1
    cv_s = (pstdev(sent_lens)/mean(sent_lens)) if len(sent_lens) > 1 else 1
    coach_density = 100*coach_hits/max(mine_words, 1)
    you_density = 100*you_hits/max(mine_words, 1)
    landing_rate = para_final_short/max(len(ps), 1)
    from collections import Counter
    oc = Counter(o for o in openers if o)
    rep_openers = {k: v for k, v in oc.items() if v >= 3}
    metrics = dict(words=nw, my_words=mine_words, paragraphs=len(ps), coach_per_100=round(coach_density, 2),
                   you_per_100=round(you_density, 1), landing_rate=round(landing_rate, 2),
                   instruction_paragraphs=imper_heavy, para_len_cv=round(cv_p, 2), sent_len_cv=round(cv_s, 2),
                   repeated_openers=rep_openers)
    hard = []
    if coach_density > 2.0: hard.append(f'E41 coach register: {coach_density:.1f} coach phrases per 100 of my words (limit 2.0)')
    if landing_rate >= 0.5 and len(ps) >= 3: hard.append(f'B7/B13 landings: {para_final_short}/{len(ps)} paragraphs end on a short line')
    if imper_heavy >= 2: hard.append(f'E23 listicle: {imper_heavy} paragraphs are strings of instructions')
    if rep_openers: hard.append(f'B13 repeated paragraph openers: {rep_openers}')
    # Review note only since 2026-09-26: second-person density doesn't separate Pangram
    # results. The Guide paragraph passed at 13.4 per 100, and two failing P5 attempts
    # sat at 4.7 and 6.1. Check what the "you" sentences are doing instead (coach register).
    if you_density > 6.0:
        flag('REVIEW', 'E36/E41 heavy second person', f'{you_density:.1f} "you" per 100 of my words')
    # AI marching order: do my paragraphs walk through the source's points in the source's order?
    if a.source:
        src = clean(open(a.source, encoding='utf-8').read())
        spts = [q for q in re.split(r'\n\s*\n|\n- ', src) if len(q.split()) >= 8]
        mapping = []
        for p in ps:
            sims = [cos(content(straight(p)), content(straight(q))) for q in spts]
            j = max(range(len(sims)), key=lambda k: sims[k]) if sims else -1
            mapping.append((j, round(sims[j], 2) if j >= 0 else 0))
        matched = [j for j, s in mapping if s >= 0.15]
        inversions = sum(1 for x in range(len(matched)) for y in range(x+1, len(matched)) if matched[x] > matched[y])
        pairs = len(matched)*(len(matched)-1)/2 or 1
        order = 1 - inversions/pairs
        coverage = len(matched)/max(len(ps), 1)
        metrics['source_map'] = mapping; metrics['source_order_agreement'] = round(order, 2)
        metrics['paragraphs_mapped_to_source'] = round(coverage, 2)
        if coverage >= 0.6 and order >= 0.8 and len(set(matched)) >= 0.6*len(matched):
            # Review note, not a hard fail (Joel, 2026-09-26): following the source's order is fine when the
            # sentences notice things along the way. The tell is nothing noticed (inventory T13) or equal weight (T09).
            flag('REVIEW', 'D9 follows the source order',
                 f"{len(matched)}/{len(ps)} paragraphs follow the source's points in its order (agreement {order:.2f}); "
                 f"fine if each part notices something; check T13 and T09 in the tell ledger")
    fails = [f for f in flags if f[0] == 'FAIL']
    verdict = 'FAIL' if (hard or fails) else ('REVIEW' if flags else 'CLEAR')
    print(f'== tells_lint: {a.draft}')
    if _SPELL is None:
        print('note: O15 (spelling) skipped, pyspellchecker is not installed (pip install pyspellchecker)')
    if not parser():
        print('note: the check for an idea doing what a person does used its short word list, which misses most abstract nouns'
              + (' (TELLS_LINT_PARSE=0)' if os.environ.get('TELLS_LINT_PARSE') == '0' else '') + '; '
              'for the parsed check: pip install spacy nltk; python -m spacy download en_core_web_sm; '
              'python -c "import nltk; nltk.download(\'wordnet\')"')
    print('verdict:', verdict)
    for h in hard: print('  HARD:', h)
    print('metrics:', metrics)
    if not a.quiet:
        from collections import defaultdict
        by = defaultdict(list)
        for sev, rule, s in flags: by[rule].append(s)
        for rule in sorted(by):
            print(f'-- {rule} ({len(by[rule])})')
            for s in by[rule]: print('   *', s[:160])
    sys.exit(2 if verdict == 'FAIL' else 1 if verdict == 'REVIEW' else 0)

if __name__ == '__main__':
    main()
