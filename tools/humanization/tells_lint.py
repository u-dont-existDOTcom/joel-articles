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
O14, O15 and O16 (Joel, 2026-10-07 01:43; numbered after the Inner Child lane's O11 to O13): Emulate's "and ... and ... and" list fails (two repeated "and"s or "or"s in
one stretch without punctuation are a REVIEW, three a FAIL); an unusual spelling or hyphenation is a REVIEW, his lines
included ("unusual spellings should help pass pangram, but that's also cheating"); a paragraph that closes by summing
itself up ("These are all questions that…") is a REVIEW ("it was way overcompleting itself").
O17 (Joel, 2026-10-07 15:05): "may be X and still Y" is a tell ("Humans don't use that as much"): a modal clause tied to
its consequence by "and still" is a REVIEW.
O6 reads the grammar when spaCy (en_core_web_sm) and NLTK's WordNet are installed (Joel, 2026-10-07 23:22: a list of
abstract nouns "sounds brittle... abstract nouns are a real vast open-ended list"); otherwise it falls back to its word
list and says so in the report.
"""
import os, re, sys, argparse, math
from statistics import mean, pstdev

def clean(t):
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
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

TICS = [r"doing some work", r"load-bearing", r"tells on itself", r"metaboli[sz]", r"\bdigest", r"\bclean\b",
        r"does its work", r"\b(That's|It's|This is) not [^.?!]{1,60}[.?!] (It's|That's|This is)\b"]
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
            if x.pos_ == 'VERB' and _person_verb(wn, x.lemma_):
                out.append((tok.text, x.lemma_))
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
        if not (1 <= len(mw) <= 6) or mw[0].lower() in LEAD | {'not'}: continue
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
    masked = QUOTED.sub(lambda m: '"' + 'Q' * (len(m.group(0)) - 2) + '"', s)
    res = [(k, s[a:b].strip(' ,'), False) for k, a, b in _find(masked)]
    for m in QUOTED.finditer(s):
        inner = m.group(0)[1:-1]
        res += [(k, inner[a:b].strip(' ,'), True) for k, a, b in _find(inner)]
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
        if HEAD_XNOTY.search(h):
            out.append(('FAIL', 'H1 x-not-y heading (Joel 2026-10-06: "always trying to do an x not y statement ... humans don\'t do x not y as much"); name the thing, as his "The Medicine Part - Yes, I\'m Naming It"', h))
        elif HEAD_NEG.search(h):
            out.append(('REVIEW', 'H1 a negation in a heading: check it isn\'t an x-not-y frame (Joel 2026-10-06)', h))
        for nb in blocks[i + 1:]:
            if re.match(r'^#+\s', nb):
                break
            t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', nb).replace('*', '').strip()
            if not t or t.startswith('![') or re.match(r'^image \d+$', t, re.I) or (len(t.split()) <= 3 and not t.endswith(('.', '?', '!'))):
                continue
            first = sentences(t)[0] if sentences(t) else t
            if POINTER_HEAD.match(first) and not POINTER_FAIL.match(first):
                out.append(('REVIEW', 'O10 the first sentence under a heading opens with a pointer: say what it points at, since nothing above it in the section does (Joel 2026-10-06, on "Key here": "that\'s referring to something. Key where? what?")', first))
            break
    return out


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
    # chat acronyms the source or the owner lines already use are the article's own register (Joel, 2026-10-01 18:19)
    src_acronyms = set()
    for extra in ([open(a.source, encoding='utf-8').read()] if a.source else []) + list(owner):
        src_acronyms |= {x.upper() for x in re.findall(ACRONYMS, extra)}
    ps = paragraphs(text)
    allw = words(text); nw = len(allw) or 1
    flags = []   # (severity, rule, sentence)
    def flag(sev, rule, s): flags.append((sev, rule, s))
    # H1 and O10 (2026-10-06): headings and the opener under each, from the raw markdown. A heading or opener the owner
    # wrote, or one already installed, isn't flagged.
    installed_raw = open(a.installed, encoding='utf-8').read() if a.installed else ''
    for sev, rule, x in heading_checks(raw):
        if x in installed_raw or is_known(x):
            continue
        flag(sev, rule, x)
    mine_words = 0; coach_hits = 0; you_hits = 0
    para_final_short = 0; imper_heavy = 0
    openers = []
    sent_lens = []
    for p in ps:
        ss = sentences(p)
        openers.append(' '.join(words(ss[0])[:1]).lower() if ss else '')
        imps = 0
        plists = []   # (mine, excerpt) for each list of three outside a quote (E125)
        for i, s in enumerate(ss):
            for o in odd_spellings(s):
                flag('REVIEW', 'O15 unusual spelling or hyphenation, his lines included (Joel 2026-10-07: "unusual spellings should help pass pangram, but that\'s also cheating"); a coinage or a rare word stays, a misspelling gets fixed: ' + o, s)
            mine = not is_known(s)
            w = words(s); sent_lens.append(len(w))
            tri = triads(s)
            plists += [(mine, x) for k, x, q in tri if not q]
            if not mine: continue
            for k, x, q in tri:
                flag('REVIEW', 'E125 list of three' + (' inside a quote (someone else\'s words can keep theirs)' if q else '') +
                     ': an AI pattern in general (Joel 2026-10-03: "lists of 3 in general are an ai pattern"). If the meaning doesn\'t need '
                     'all three, drop the one that matters least; if it does, split them into sentences, the way he fixed P1 ("Maybe it just '
                     'has something to say."). Joel, 01:06: "when there\'s no actual need for 3 items you can remove one of them"', x)
            mine_words += len(w)
            for r in TICS:
                if re.search(r, s, re.I): flag('FAIL', 'B11 tic', s)
            if re.search(r"\b(doesn['’]t|does not|don['’]t|do not|never) gets? to (decide|choose|pick|vote|call)|\bgets? (a|the) (vote|say)\b|\bgets? to (decide|choose)\b", s, re.I):
                flag('FAIL', 'O1 owner ban: "doesn\'t get to decide" family (Joel 2026-09-28)', s)
            if re.search(r"(^|[.!?]\s+)(Fine|Good|Great|Sure|Okay|OK|Fair enough)[,.!]\s", s):
                flag('FAIL', 'O2 owner ban: Fine/Good/Great as a clause (Joel 2026-09-28)', s)
            # E139 (2026-10-07): SKILL.md's "Synthetic specificity and fake concreteness" rule was never loaded here (O11 to O13; main's O8 to O10 came first).
            if re.search(r"\b(Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)days?\b", s):
                flag('FAIL', 'O11 owner ban: a weekday put in to sound concrete (Joel 2026-10-07: "AI is always saying Tuesday, on Tuesday, '
                     'or some specific day like this. on a regular Tuesday is the worst"; SKILL.md "Synthetic specificity"). Keep one only '
                     'when it is a real fact from the source and matters to the thought', s)
            if re.search(r"\b(ordinary|regular|boring|everyday|mundane)\b", s, re.I):
                flag('REVIEW', 'O12 "ordinary/regular/boring": overused by AI, not a sure tell (Joel 2026-10-07 03:24: "boring, regular etc are not '
                     'for sure AI tells, almost nothing is a for sure AI tell, but they are way overused by AI"); keep one that says something', s)
            if re.search(r"\b\d+\s*(%|percent)|\b(one|two|three|four|five|ten|twenty|fifty)\s+percent\b|\bo['’]clock\b|\b\d{1,2}(:\d\d)?\s?(am|pm)\b|"
                         r"\bby (lunch|dinner|noon|bedtime|lunchtime)\b|\b(a|one|this|that) (morning|afternoon|evening) of\b", s, re.I):
                flag('REVIEW', 'O13 a made-up number or clock time (Joel 2026-10-07, on "five percent is enough": "AI wants to put concrete '
                     'numbers on stuff all the time, then people are wondering how much is 5%?"; SKILL.md: no invented clock-time details)', s)
            if re.search(r"\b(my first (guess|thought|instinct|reaction)|I'd probably want to|I'd be tempted to|my instinct would be)\b", s, re.I):
                flag('REVIEW', 'E138 the writer\'s own impulse: check the next sentence doesn\'t take it back (Joel 2026-10-07, on "I\'d probably '
                     'want to fix it by saying sweeter and sweeter things, which won\'t work": "this part is contradictory"; his fix gave '
                     'the move to "some people")', s)
            ag = abstract_agents(s)  # None without the parser: then the word list decides
            if (ag if ag is not None else re.search(ABSTRACT_AGENT, s, re.I)):
                flag('REVIEW', 'O6 a feeling or idea doing what a person does: one of the top tells, not a ban, worst when polished or overused; give the action to a person, changing as few words as possible (Joel 2026-10-02: "so the anger goes there" became "so the angry communard goes there")', s)
            if re.search(ENOUGH_PAIR, s, re.I):
                flag('REVIEW', 'O7 polished "X enough to… Y enough to…" pair (Joel 2026-10-02: "devoted enough to practice them and secure enough to disagree" "looks super highly polished")', s)
            if re.search(SMUGGLE_FIG, s, re.I):
                flag('FAIL', 'O8 owner ban: smuggling talk (Joel 2026-10-03: "ai is always saying something like \'not smuggle in\' or something about smuggling in"); say the plain reason, as his "My reasons are given in those articles, respectively, since they need more space."', s)
            elif re.search(SMUGGLE, s, re.I):
                flag('REVIEW', 'O8 "smuggle": literal smuggling can stay; the figurative kind is an owner ban (Joel 2026-10-03)', s)
            if i == 0 and POINTER_FAIL.match(s.strip()):
                flag('FAIL', 'O10 an opener that points at nothing (Joel 2026-10-06: "\'Key here\' can\'t be how you open a section. that\'s referring to something. Key where? what?"): start with the claim itself, as his "Most of the writing on communities hasn\'t caught up with psychedelics."', s)
            m9 = NOT_TAIL.match(s.strip())
            if m9 and len(words(m9.group('head'))) >= 4:
                flag('REVIEW', 'O9 a "not Y" tail on a finished claim (Joel 2026-10-03: "it always wants to add a \'not Y\' part"): say the claim or the reason plainly; keep the contrast only when the paragraph needs the other side said', s)
            for r in CONTRAST:
                if re.search(r, s, re.I): flag('REVIEW', 'B2 contrast', s); break
            for r in THESIS:
                if re.search(r, s, re.I if not r.startswith('^') else 0): flag('REVIEW', 'B1 finished principle', s); break
            for r in ANNOUNCE:
                if re.search(r, s): flag('REVIEW', 'B5 announces the paragraph', s); break
            hits = sum(len(re.findall(r, s, re.I)) for r in COACH)
            coach_hits += hits
            if hits: flag('REVIEW', 'E41 coach phrase', s)
            you_hits += len(re.findall(r"\byou(r|'re|'ll|'d|'ve)?\b", s, re.I))
            if re.search(r"\bthe kid\b|\bkids?\b", s, re.I): flag('REVIEW', 'E1 kid', s)
            for acr in re.findall(ACRONYMS, s):
                if acr.upper() not in src_acronyms:
                    flag('REVIEW', 'chat acronym the source doesn\'t use: say it in words, unless the author asked for an informal internet style (Joel 2026-10-01: "for articles where the acronyms are used, you\'d use those, but for other articles where they aren\'t used, you wouldn\'t put them in")', s)
                    break
            first = (w[0].lower() if w else '')
            if first in IMPER: imps += 1
            if s.count(',') >= 3 or len(re.findall(r'\b(or|and)\b', s)) >= 3:
                flag('REVIEW', 'B4/E15 list or packed sentence', s)
            ps_n = polysyndeton(s)
            if ps_n >= 3:
                flag('FAIL', 'O14 owner ban: an "and ... and ... and" list (Joel 2026-10-07: "that looks like emulate trying to cheat, and it wasn\'t needed. still passes pangram with normal syntax"); use commas and keep the list\'s own "or"', s)
            elif ps_n == 2:
                flag('REVIEW', 'O14 two repeated "and"s or "or"s in one stretch: fine in speech ("bread and butter and jam"), Emulate\'s trick in a list (Joel 2026-10-07)', s)
            if i == len(ss) - 1 and len(ss) >= 3 and SUMMARY_CLOSE.match(s.strip()):
                flag('REVIEW', 'O16 a closing line that sums the paragraph up (Joel 2026-10-07: "it was way overcompleting itself"): propose the cut to him, quoted, with your opinion; don\'t cut it yourself', s)
            if STILL_TAIL.search(s):
                flag('REVIEW', 'O17 "may be X and still Y" (Joel 2026-10-07 15:05: "Another AI tell is \'may be X and still Y\' ... Humans don\'t use that as much"): say both things plainly and keep the modal over both halves', s)
            if i < 2 and re.search(r"\b(did|do|does|doing|done|didn't|don't|tried|try|skip|skipped|finish|finished|start|started)\s+it\b", ' '.join(s.split()[:8]), re.I):
                flag('REVIEW', 'R1 action "it" near a paragraph start: name the thing (Joel 2026-09-30, on "If you did it": "the first it is unclear referent")', s)
            if i > 0 and len(w) <= 6 and len(words(ss[i-1])) >= 12 and re.match(r"(But|That|It|So|And|Which|They)\b", s):
                flag('REVIEW', 'B3 short knock-down', s)
        if len(plists) >= 2 and any(m for m, _ in plists):
            flag('FAIL', 'E125 two lists of three in one paragraph (Joel 2026-10-03, on P1 at 66% AI: "P! failed b ecause it has 2 lists of 3"); '
                 'fix one first: drop the item that matters least, or if every item is needed, split it into sentences the way he did', ' / '.join(x for _, x in plists))
        if ss and len(words(ss[-1])) <= 9 and not is_known(ss[-1]):
            para_final_short += 1; flag('REVIEW', 'B7 short landing at paragraph end', ss[-1])
        if imps >= 2: imper_heavy += 1; flag('REVIEW', 'E23 paragraph of instructions', p[:90] + '...')
    # paragraph-level metrics
    plen = [len(words(p)) for p in ps]
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
            sims = [cos(content(p), content(q)) for q in spts]
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
