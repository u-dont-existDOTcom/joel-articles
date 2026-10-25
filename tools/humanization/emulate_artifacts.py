#!/usr/bin/env python3
"""The strict Emulate check: what a rewriting pass (Emulate, a model, a merge) brought into an article that isn't in the
author's own texts, from typos to thrown-in sentences.

Joel, 2026-10-25 19:42 UTC, on the hypnosis guide's review page: "i didn' tmake these typos, did you?" (spaces before
full stops and commas), "it looks like you must have forgotten to fix all kinds of errors you got from emulate? ... that
means we should also check the community article i guess?", "why was inner child in quotes? ... looks like more crap from
emulate you forgot to check. make those emulate checks more strict pls for future also", "i feel this was prob some
emulate nonsense thrown in" (a sentence in none of his texts) and "make sure all the citations and stuff are not messed
up in the emulate-infused articles". None of the spaces were in his texts; the earlier checks compared Emulate's output
with our draft, not with his words, and read meaning, not marks.

    python3 tools/humanization/emulate_artifacts.py audit ARTICLE --source FILE [--source FILE ...] [--allowed FILE ...]
        --out DIR          # AUDIT.json, AUDIT.md, PAIRS.json and PAIRS-<n>.txt (for the meaning read) in DIR
    python3 tools/humanization/emulate_artifacts.py fix ARTICLE DIR/AUDIT.json OUT   # the mechanical fixes only

ARTICLE and each file are Markdown, Substack editor HTML or plain text. A source is the author's own text (his published
post, his editor HTML, his drafts), most trusted first; an allowed file is text he approved from elsewhere (the new
sentences of suggestions he approved, a guide of his the article quotes). A paragraph of ARTICLE that is word for word
in one of them is his and is skipped. Every other paragraph is lined up, sentence by sentence, with the closest sentence
in his texts and checked:

  mechanical (never meant, so `fix` corrects them; a pattern his own texts have is left alone):
    space-before-punct  a space before , . ; : ! ? or inside ( )
    doubled-word        "the the", for the small words that are never doubled on purpose
  for a decision (each with his version beside it, for the marking page):
    confusable          it's/its, you're/your, they're/their/there, then/than, who's/whose, lose/loose, affect/effect
                        where his sentence has the other one; a contraction where his sentence has none, to be read
    quote-marks         quoted words his texts have without quote marks (scare quotes), or quoted words in none of them
    citation            a sentence with a year, page or chapter whose names, year, pages, italics or links differ from his
                        line, or which none of his texts has
    number              a number his line doesn't have, or his line's number gone
    link                a link in none of his texts, or a link his paragraph has that this one lost
    parenthetical       words in brackets in none of his texts
    doubled-word        any other doubled word
    spelling            a British spelling where his texts spell the word the American way, or a word neither his
                        texts nor the dictionary know (pyspellchecker, when it's installed)
    new-sentence        a sentence with no line of his close to it (claims, asides, softeners, warnings thrown in)

Code finds the marks; meaning goes to a reader (the method-fit rule in AGENTS.md). PAIRS-<n>.txt holds every changed
paragraph with his closest paragraphs, for a fresh reader who lists what the new version adds or loses
(docs/EMULATE-FALLBACK.md section 4, step 6).
"""
import argparse
import collections
import difflib
import html
import json
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import html_text_edit  # noqa: E402
import suggestion_review as sr  # noqa: E402

VERSION = 'emulate_artifacts.py 1.0 (2026-10-25)'
QUOTE_TR = str.maketrans({'‘': "'", '’': "'", '‚': "'", '‛': "'", '′': "'", '“': '"', '”': '"', '„': '"', '‟': '"',
                          '″': '"', '–': '-', '—': '-', '‐': '-', '‑': '-', '−': '-', ' ': ' ', '​': ''})
ALIGNED, CLOSE, NEW = 0.6, 0.45, 0.45
SMALL_WORDS = {'a', 'an', 'the', 'to', 'of', 'in', 'on', 'at', 'for', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
               'it', 'i', 'you', 'we', 'they', 'he', 'she', 'with', 'from', 'by', 'as', 'be', 'this', 'your', 'my', 'if'}
CONFUSABLE = {"its": {"it's"}, "it's": {"its"}, "your": {"you're"}, "you're": {"your"}, "their": {"they're", "there"},
              "they're": {"their", "there"}, "there": {"their", "they're"}, "then": {"than"}, "than": {"then"},
              "whose": {"who's"}, "who's": {"whose"}, "lose": {"loose"}, "loose": {"lose"}, "affect": {"effect"},
              "effect": {"affect"}, "affects": {"effects"}, "effects": {"affects"}}
CONTRACTIONS = {"it's", "you're", "they're", "who's"}
SPACE_PUNCT = re.compile(r'(?<=[^\s(\[])( +)([,;:!?]|\.(?!\.))(?=\s|$|["”’)\]*])|(?<=\()( +)(?=\S)|(?<=\S)( +)(?=\))')
DOUBLED = re.compile(r'\b([A-Za-z]+)\s+\1\b', re.I)
PAREN = re.compile(r'\(([^()]{3,400})\)')
QUOTED = re.compile(r'“([^”]{1,300})”|(?<![\w"])"([^"\n]{1,300})"(?![\w])|(?<![\w‘])‘([^’]{1,120})’(?![A-Za-z])')
YEAR = re.compile(r'\b(1[6-9]\d\d|20\d\d)\b')
PAGES = re.compile(r'\b(?:pp?\.?|pages?|ch(?:apters?|s)?\.?)\s*\d', re.I)
NUMBER = re.compile(r'(?<!\d)(?<!\d[.,])\d+(?:[.,]\d+)*(?!\d)')
SENT_END = re.compile(r'(?<=[.!?…])["”’)\]]*\s+(?=["“‘(\[]?[A-Z0-9])')


def norm(s):
    s = unicodedata.normalize('NFKC', s).translate(QUOTE_TR)
    return re.sub(r'\s+', ' ', s).strip()


def low(s):
    return norm(s).lower()


def words(s):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", low(s))


# ---------------------------------------------------------------- reading the files as blocks

class HtmlInline:
    """Segments ({t, href, em}) of a piece of inline HTML."""

    def __init__(self, inner):
        self.segs, href, em = [], [], 0
        for m in re.finditer(r'<(/?)(\w+)([^>]*)>|([^<]+)', inner):
            if m.group(4) is not None:
                t = html.unescape(m.group(4))
                if t:
                    self.segs.append({'t': t, 'href': href[-1] if href else None, 'em': em > 0})
                continue
            close, tag = m.group(1), m.group(2).lower()
            if tag == 'br':
                self.segs.append({'t': ' ', 'href': None, 'em': False})
            elif tag == 'a':
                if close:
                    href and href.pop()
                else:
                    h = re.search(r'href="([^"]*)"', m.group(3))
                    href.append(html.unescape(h.group(1)) if h else '')
            elif tag in ('em', 'i'):
                em += -1 if close else 1


HTML_BLOCK = re.compile(r'<(p|h[1-6])\b[^>]*>(.*?)</\1>', re.S | re.I)


def html_blocks(doc):
    """[(start, end, inner_start, inner_end, kind)] for each <p> and <h1>..<h6> in DOC."""
    return [(m.start(), m.end(), m.start(2), m.end(2), m.group(1).lower()) for m in HTML_BLOCK.finditer(doc)]


def load(path):
    """The file's blocks: [{i, kind, where, segs, text}] (headings included, native objects left out)."""
    path = pathlib.Path(path)
    data = path.read_text(encoding='utf-8')
    out = []
    if path.suffix.lower() in ('.html', '.htm'):
        heading, n = '', 0
        for k, (_s, _e, a, z, kind) in enumerate(html_blocks(data)):
            segs = HtmlInline(data[a:z]).segs
            text = re.sub(r'\s+', ' ', ''.join(x['t'] for x in segs)).strip()
            if not text:
                continue
            if kind.startswith('h'):
                heading, n = text, 0
                where = 'the heading "%s"' % text
            else:
                n += 1
                where = '%s, P%d' % (heading or 'the opening', n)
            out.append({'i': k, 'kind': kind, 'where': where, 'segs': segs, 'text': text})
    elif path.suffix.lower() == '.md':
        bl = sr.blocks(data)
        for b in bl:
            if b['native'] or not b['text'].strip():
                continue
            out.append({'i': b['i'], 'kind': b['kind'], 'where': sr.where(bl, b['i']), 'segs': b['segs'], 'text': b['text']})
    else:
        for k, para in enumerate(re.split(r'\n\s*\n', data)):
            t = re.sub(r'\s+', ' ', para).strip()
            if t:
                out.append({'i': k, 'kind': 'p', 'where': 'paragraph %d' % (k + 1), 'segs': [{'t': t, 'href': None, 'em': False}],
                            'text': t})
    return out


def sentences(text):
    """[(start, end)] of each sentence of TEXT."""
    out, pos = [], 0
    for m in SENT_END.finditer(text):
        out.append((pos, m.start()))
        pos = m.end()
    out.append((pos, len(text)))
    return [(a, z) for a, z in out if text[a:z].strip()]


def seg_spans(segs):
    """[(start, end, seg)] of each segment in the block's plain text."""
    out, pos = [], 0
    for s in segs:
        out.append((pos, pos + len(s['t']), s))
        pos += len(s['t'])
    return out


# ---------------------------------------------------------------- his texts, indexed

class Corpus:
    def __init__(self, files):
        self.docs, self.sents, self.grams, self.joined = [], [], collections.defaultdict(set), []
        self.quoted, self.urls, self.paras, self.parens, self.vocab = set(), set(), set(), [], set()
        for rank, f in enumerate(files):
            bl = load(f)
            name = pathlib.Path(f).name
            self.docs.append((name, bl))
            parts = []
            for b in bl:
                t = b['text']
                self.paras.add(low(t))
                parts.append(low(t))
                for s in b['segs']:
                    if s['href']:
                        self.urls.add(s['href'])
                for m in QUOTED.finditer(norm(t)):
                    self.quoted.add(low(next(g for g in m.groups() if g is not None)))
                for m in PAREN.finditer(t):
                    self.parens.append(words(m.group(1)))
                self.vocab.update(words(t))
                for a, z in sentences(t):
                    w = words(t[a:z])
                    k = len(self.sents)
                    self.sents.append({'doc': name, 'rank': rank, 'block': b, 'start': a, 'end': z, 'text': t[a:z].strip(),
                                       'words': w})
                    for g in grams(w):
                        self.grams[g].add(k)
            self.joined.append(' \n '.join(parts))

    def has(self, s):
        s = low(s)
        return bool(s) and any(s in j for j in self.joined)

    def best(self, text, n=1):
        """The closest sentences of his to TEXT: [(ratio, sentence)], best first."""
        w = words(text)
        if not w:
            return []
        hits = collections.Counter()
        for g in grams(w):
            for k in self.grams.get(g, ()):
                hits[k] += 1
        out = []
        for k, _c in hits.most_common(30):
            s = self.sents[k]
            out.append((difflib.SequenceMatcher(None, w, s['words'], autojunk=False).ratio(), -s['rank'], k))
        out.sort(reverse=True)
        return [(r, self.sents[k]) for r, _rk, k in out[:n]]


def grams(w):
    if len(w) < 3:
        return [tuple(w)] if w else []
    return [tuple(w[i:i + 3]) for i in range(len(w) - 2)]


# ---------------------------------------------------------------- the checks

def finding(kind, b, text, start, end, note, theirs=None, fix=None, auto=False, strength='check'):
    return {'kind': kind, 'block': b['i'], 'where': b['where'], 'start': start, 'end': end, 'text': text[start:end],
            'context': text[max(0, start - 60):end + 60], 'note': note, 'his': theirs, 'fix': fix, 'auto': auto,
            'strength': strength}


def audit_block(b, corpus, allowed):
    text, out = b['text'], []
    sents = []
    for a, z in sentences(text):
        best = corpus.best(text[a:z])
        al = allowed.best(text[a:z]) if allowed.sents else []
        sents.append({'start': a, 'end': z, 'best': best[0] if best else (0.0, None), 'allowed': al[0] if al else (0.0, None)})

    def his_line(pos):
        for s in sents:
            if s['start'] <= pos < s['end'] + 1:
                return s
        return sents[-1] if sents else None

    # space before punctuation
    for m in SPACE_PUNCT.finditer(text):
        sp = next(i for i in (1, 3, 4) if m.group(i) is not None)
        a, z = m.start(sp), m.end(sp)
        prev = re.findall(r'\S+$', text[:a])
        nxt = text[z:z + 1]
        mine = low((prev[0] if prev else '') + ' ' + nxt)
        if corpus.has(mine) or allowed.has(mine):
            continue
        if nxt == '.' and text[a - 1:a] == '…':   # "else… ." : the ellipsis ends the sentence, as in his texts
            fix_ = ('delete', a, z + 1)
        else:
            fix_ = ('delete', a, z)
        out.append(finding('space-before-punct', b, text, max(0, a - 12), min(len(text), z + 2),
                           'a space before "%s" his texts never have here' % nxt, fix=fix_, auto=True,
                           strength='mechanical'))
    # doubled words
    for m in DOUBLED.finditer(text):
        w = m.group(1).lower()
        if corpus.has(m.group(0)) or allowed.has(m.group(0)):
            continue
        small = w in SMALL_WORDS and w not in ('that', 'had', 'is')
        out.append(finding('doubled-word', b, text, m.start(), m.end(), '"%s" twice' % m.group(1),
                           fix=('delete', m.start(1) + len(m.group(1)), m.end()) if small else None, auto=small,
                           strength='mechanical' if small else 'check'))
    # sentence by sentence against his line
    for s in sents:
        a, z = s['start'], s['end']
        st = text[a:z]
        ratio, his = s['best']
        aratio, _ = s['allowed']
        sw = words(st)
        if his is not None and ratio >= ALIGNED:
            hw = his['words']
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, hw, sw, autojunk=False).get_opcodes():
                if op == 'replace' and i2 - i1 == 1 and j2 - j1 == 1 and sw[j1] in CONFUSABLE.get(hw[i1], ()):
                    k = word_pos(st, sw, j1)
                    out.append(finding('confusable', b, text, a + k, a + k + len(sw[j1]),
                                       '"%s" where his line has "%s"' % (sw[j1], hw[i1]), theirs=his['text'],
                                       strength='likely'))
            hn, sn = NUMBER.findall(his['text']), NUMBER.findall(st)
            if collections.Counter(hn) != collections.Counter(sn) and aratio < 0.8:
                out.append(finding('number', b, text, a, z, 'numbers %s, his line %s' % (sn, hn), theirs=his['text'],
                                   strength='likely'))
        else:
            for j, w in enumerate(sw):
                if w in CONTRACTIONS and aratio < 0.8:
                    k = word_pos(st, sw, j)
                    nxt = sw[j + 1] if j + 1 < len(sw) else ''
                    if his is not None and (w + ' ' + nxt) in ' '.join(his['words']):
                        continue
                    if not looks_possessive(st, sw, j):
                        continue
                    out.append(finding('confusable', b, text, a + k, a + k + len(w),
                                       '"%s %s": read it for "%s"' % (w, nxt, '/'.join(sorted(CONFUSABLE[w]))),
                                       theirs=his['text'] if his is not None and ratio >= CLOSE else None))
        if (his is None or ratio < NEW) and aratio < 0.8 and len(sw) >= 4:
            out.append(finding('new-sentence', b, text, a, z, 'no line of his close to it (closest %.2f)' % ratio,
                               theirs=his['text'] if his is not None and ratio >= 0.3 else None))
        # citations
        if (YEAR.search(st) or PAGES.search(st) or ' et al' in st) and aratio < 0.95:
            out += cite_check(b, text, a, z, corpus)
    # quote marks
    for m in QUOTED.finditer(text):
        g = next(i for i in (1, 2, 3) if m.group(i) is not None)
        q = low(m.group(g))
        if q in corpus.quoted or q in allowed.quoted or len(q) < 2:
            continue
        line = his_line(m.start())
        r, h = line['best'] if line else (0.0, None)
        if h is not None and r >= CLOSE and q in low(h['text']):
            note, strength = 'quote marks his line doesn\'t have around these words', 'likely'
        elif allowed.has(q) and not corpus.has(q):
            continue
        elif corpus.has(q):
            note, strength = 'quote marks his texts never put around these words', 'check'
        else:
            note, strength = 'quoted words in none of his texts', 'check'
        out.append(finding('quote-marks', b, text, m.start(), m.end(), note, strength=strength,
                           fix=('unquote', m.start(), m.end()) if strength == 'likely' else None))
    # parentheticals
    for m in PAREN.finditer(text):
        inner = m.group(1)
        if corpus.has(inner) or allowed.has(inner) or len(words(inner)) < 2:
            continue
        if YEAR.fullmatch(inner.strip()) or re.fullmatch(r'[^()]*\b(1[6-9]\d\d|20\d\d)\b[^()]*', inner) and len(words(inner)) <= 6:
            continue   # (Author 2024): the citation check reads these
        close = max((difflib.SequenceMatcher(None, words(inner), w, autojunk=False).ratio() for w in corpus.parens), default=0)
        if close >= 0.5:
            continue   # his own bracket, reworded: the meaning read sees it with its paragraph
        best = corpus.best(inner)
        out.append(finding('parenthetical', b, text, m.start(), m.end(),
                           'words in brackets in none of his texts (closest bracket of his %.2f)' % close,
                           theirs=best[0][1]['text'] if best and best[0][0] >= CLOSE else None))
    # links
    for start, end, sg in seg_spans(b['segs']):
        if sg['href'] and sg['href'] not in corpus.urls and sg['href'] not in allowed.urls:
            out.append(finding('link', b, text, start, end, 'a link in none of his texts: %s' % sg['href'], strength='likely'))
    for m in re.finditer(r"[A-Za-z]+(?:['’][A-Za-z]+)*", text):
        w = m.group(0).lower().replace('’', "'")
        if w in corpus.vocab or w in allowed.vocab or len(w) < 4:
            continue
        us = american(w)
        if us and us in corpus.vocab:
            out.append(finding('spelling', b, text, m.start(), m.end(), 'British spelling; his texts have "%s"' % us,
                               fix=('replace', m.start(), m.end(), match_case(m.group(0), us)), auto=True,
                               strength='mechanical'))
        elif SPELL is not None and "'" not in w and not SPELL.known([w]) and not m.group(0)[0].isupper():
            out.append(finding('spelling', b, text, m.start(), m.end(), 'a word neither his texts nor the dictionary know'))
    his_blocks = {}
    for s in sents:
        r, h = s['best']
        if h is not None and r >= ALIGNED:
            his_blocks[id(h['block'])] = h['block']
    have = {sg['href'] for sg in b['segs'] if sg['href']}
    his_edit = any(x['allowed'][0] >= 0.8 for x in sents)   # he rewrote part of it himself later
    for hb in his_blocks.values():
        for start, end, sg in seg_spans(hb['segs']):
            if his_edit and low(sg['t']) not in low(text):
                continue   # the linked words went in his own later edit
            if sg['href'] and sg['href'] not in have and sg['href'] not in allowed.urls:
                out.append(finding('link', b, text, 0, 0, 'his paragraph links "%s" to %s; this one doesn\'t'
                                   % (sg['t'], sg['href']), theirs=hb['text'], strength='likely'))
    return out, sents


def word_pos(st, sw, j):
    """Where word J of SW (the words of ST) starts in ST."""
    k = 0
    for i, m in enumerate(re.finditer(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)?", st)):
        if i == j:
            return m.start()
        k = m.end()
    return k


try:
    from spellchecker import SpellChecker
    SPELL = SpellChecker()
except Exception:   # optional: without it, only the British spellings are checked
    SPELL = None
try:
    import spacy
    NLP = spacy.load('en_core_web_sm', disable=['parser', 'ner', 'lemmatizer'])
except Exception:   # optional: without it, every contraction in a changed sentence is listed
    NLP = None
BRITISH = [(r'isation$', 'ization'), (r'isations$', 'izations'), (r'ise$', 'ize'), (r'ised$', 'ized'), (r'ises$', 'izes'),
           (r'ising$', 'izing'), (r'yse$', 'yze'), (r'ysed$', 'yzed'), (r'ysing$', 'yzing'), (r'our$', 'or'),
           (r'ours$', 'ors'), (r'oured$', 'ored'), (r'ouring$', 'oring'), (r'ourite$', 'orite'), (r'tre$', 'ter'),
           (r'tres$', 'ters'), (r'lled$', 'led'), (r'lling$', 'ling'), (r'ogue$', 'og'), (r'ence$', 'ense')]


def american(w):
    for pat, rep in BRITISH:
        if re.search(pat, w):
            return re.sub(pat, rep, w)
    return None


def match_case(old, new):
    return new.capitalize() if old[:1].isupper() else new


def looks_possessive(st, sw, j):
    """Whether contraction J of ST's words is followed by what a possessive would be (a noun, or "own")."""
    nxt = sw[j + 1] if j + 1 < len(sw) else ''
    if nxt in ('own', 'self'):
        return True
    if NLP is None:
        return True
    k = word_pos(st, sw, j) + len(sw[j])
    doc = NLP(st[k:k + 60])
    toks = [t for t in doc if not t.is_space and not t.is_punct]
    return bool(toks) and toks[0].tag_ in ('NN', 'NNS', 'NNP', 'NNPS') and toks[0].text.lower() == nxt


def names(s):
    return {w for w in re.findall(r"\b[A-Z][a-z]+(?:-[A-Z][a-z]+)?\b", s)} - {
        'The', 'A', 'An', 'In', 'On', 'See', 'And', 'For', 'This', 'These', 'That', 'It', 'I', 'If', 'As', 'Also', 'From',
        'Some', 'Note', 'NOTE', 'Of', 'To', 'With', 'By', 'But', 'Or'}


def em_texts(block, a, z):
    return [low(sg['t']) for s, e, sg in seg_spans(block['segs']) if sg['em'] and s < z and e > a and words(sg['t'])]


def cite_check(b, text, a, z, corpus):
    st = text[a:z]
    years = set(YEAR.findall(st))
    cands = []
    for k, s in enumerate(corpus.sents):
        if years and not years & set(YEAR.findall(s['text'])):
            continue
        if not years and not PAGES.search(s['text']):
            continue
        r = difflib.SequenceMatcher(None, words(st), s['words'], autojunk=False).ratio()
        cands.append((r, -s['rank'], k))
    if not cands:
        return [finding('citation', b, text, a, z, 'a reference none of his texts has (year %s)' % ', '.join(sorted(years)),
                        strength='likely')]
    cands.sort(reverse=True)
    r, _rk, k = cands[0]
    his = corpus.sents[k]
    if r < 0.3:
        return [finding('citation', b, text, a, z, 'a reference his texts have only far from this (closest %.2f)' % r,
                        theirs=his['text'], strength='likely')]
    diffs = []
    if names(st) != names(his['text']):
        gone, extra = names(his['text']) - names(st), names(st) - names(his['text'])
        diffs.append('names: %s' % '; '.join(x for x in (gone and 'his has ' + ', '.join(sorted(gone)),
                                                          extra and 'this has ' + ', '.join(sorted(extra))) if x))
    hn, sn = collections.Counter(NUMBER.findall(his['text'])), collections.Counter(NUMBER.findall(st))
    if hn != sn:
        diffs.append('numbers: his %s, this %s' % (sorted(hn.elements()), sorted(sn.elements())))
    he, se = em_texts(his['block'], his['start'], his['end']), em_texts(b, a, z)
    for t in he:
        if t not in se and t in low(st):
            diffs.append('italics: his "%s" is in italics' % t)
    if re.search(r'\s[,.;:]|\(\d{4}\)\s*pp?\b|,\s*\(', st) and not re.search(r'\s[,.;:]', his['text']):
        diffs.append('punctuation')
    if not diffs:
        return []
    return [finding('citation', b, text, a, z, '; '.join(diffs), theirs=his['text'], strength='likely')]


# ---------------------------------------------------------------- audit and fix

STOP = set("""a an the and or but if then than so to of in on at for from by with as is are was were be been being it its
it's this that these those there their they them you your you're i me my we our he she his her him not no do does did done
have has had can could will would should may might must just also very more most less some any all each every one what
which who whom whose when where why how about into over under up down out off again here own same such only too don't
can't it'll you'll i'm i've that's what's there's let's etc""".split())


def content(text):
    return {w for w in words(text) if w not in STOP and len(w) > 2}


def align_blocks(art, src):
    """For each block of ART, the indexes of the blocks of SRC it was rewritten from: an order-keeping alignment that
    shares the most content words (Jaccard), then, for a block it leaves out (a moved one), the best match anywhere."""
    A, S = [content(b['text']) for b in art], [content(b['text']) for b in src]
    index = collections.defaultdict(set)
    for j, w in enumerate(S):
        for x in w:
            index[x].add(j)

    def sims(i):
        out = {}
        for j in set().union(*(index[x] for x in A[i])) if A[i] else ():
            u = len(A[i] | S[j])
            out[j] = len(A[i] & S[j]) / u if u else 0.0
        return out
    table = [sims(i) for i in range(len(A))]
    n, m = len(A), len(S)
    best = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        row, prev, t = best[i], best[i - 1], table[i - 1]
        for j in range(1, m + 1):
            v = prev[j] if prev[j] > row[j - 1] else row[j - 1]
            x = t.get(j - 1, 0.0)
            if x >= 0.1 and prev[j - 1] + x > v:
                v = prev[j - 1] + x
            row[j] = v
    match, i, j = {}, n, m
    while i > 0 and j > 0:
        x = table[i - 1].get(j - 1, 0.0)
        if x >= 0.1 and abs(best[i][j] - (best[i - 1][j - 1] + x)) < 1e-12:
            match[i - 1] = j - 1
            i, j = i - 1, j - 1
        elif best[i][j] == best[i - 1][j]:
            i -= 1
        else:
            j -= 1
    used = set(match.values())
    out = {}
    for i in range(n):
        t = table[i]
        if i in match:
            js = [match[i]]
        else:
            k = max(t, key=t.get, default=None)
            js = [k] if k is not None and t[k] >= 0.25 else []
        for j in list(js):
            for nb in (j - 1, j + 1):
                if 0 <= nb < m and nb not in used and t.get(nb, 0.0) >= 0.12 and nb not in js:
                    js.append(nb)
        out[i] = sorted(js)
    return out


def audit(article, sources, allowed_files, out_dir, parts=6):
    corpus = Corpus(sources)
    allowed = Corpus(allowed_files) if allowed_files else Corpus([])
    blocks = load(article)
    main_name, main_blocks = corpus.docs[0]
    aligned = align_blocks(blocks, main_blocks)
    findings, pairs, skipped = [], [], 0
    for n, b in enumerate(blocks):
        t = low(b['text'])
        if t in corpus.paras or corpus.has(b['text']) or t in allowed.paras:
            skipped += 1
            continue
        f, sents = audit_block(b, corpus, allowed)
        findings += f
        if b['kind'].startswith('h'):
            continue
        his = [{'doc': main_name, 'where': main_blocks[j]['where'], 'text': main_blocks[j]['text']} for j in aligned[n]]
        for s in sents:
            r, h = s['best']
            if h is not None and r >= CLOSE and h['block']['text'] not in [x['text'] for x in his]:
                his.append({'doc': h['doc'], 'where': h['block']['where'], 'text': h['block']['text']})
        marked = b['text']
        for s in sorted(sents, key=lambda x: -x['start']):
            if s['allowed'][0] >= 0.8:
                marked = marked[:s['start']] + '⟦' + marked[s['start']:s['end']] + '⟧' + marked[s['end']:]
        new = [b['text'][s['start']:s['end']].strip() for s in sents
               if s['best'][0] < NEW and s['allowed'][0] < 0.8 and len(words(b['text'][s['start']:s['end']])) >= 4]
        pairs.append({'block': b['i'], 'where': b['where'], 'text': b['text'], 'marked': marked, 'his': his[:4],
                      'new_sentences': new})
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    counts = collections.Counter(f['kind'] for f in findings)
    record = {'tool': VERSION, 'article': str(article), 'sources': [str(x) for x in sources],
              'allowed': [str(x) for x in allowed_files], 'blocks': len(blocks), 'his_word_for_word': skipped,
              'checked': len(blocks) - skipped, 'counts': dict(sorted(counts.items())),
              'auto_fixes': sum(1 for f in findings if f['auto']), 'findings': findings}
    (out_dir / 'AUDIT.json').write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out_dir / 'PAIRS.json').write_text(json.dumps(pairs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for old in out_dir.glob('PAIRS-*.txt'):
        old.unlink()
    size = -(-len(pairs) // parts) if pairs else 0
    for n in range(parts):
        chunk = pairs[n * size:(n + 1) * size]
        if not chunk:
            continue
        lines = []
        for p in chunk:
            lines.append('=== %s [block %d]' % (p['where'], p['block']))
            lines.append('NEW: ' + p['marked'])
            if p['his']:
                for h in p['his']:
                    lines.append('HIS (%s, %s): %s' % (h['doc'], h['where'], h['text']))
            else:
                lines.append('HIS: (no paragraph of his close to this one)')
            lines.append('')
        (out_dir / ('PAIRS-%d.txt' % (n + 1))).write_text('\n'.join(lines), encoding='utf-8')
    md = ['# Emulate check: %s' % pathlib.Path(article).name, '',
          'Made by `%s` against %s%s. %d blocks, %d of them his word for word; %d checked.' % (
              VERSION, ', '.join('`%s`' % pathlib.Path(x).name for x in sources),
              (' (allowed: %s)' % ', '.join('`%s`' % pathlib.Path(x).name for x in allowed_files)) if allowed_files else '',
              len(blocks), skipped, len(blocks) - skipped), '',
          '| Kind | Found | Fixed by `fix` |', '|---|---|---|']
    for k, n in sorted(counts.items()):
        md.append('| %s | %d | %d |' % (k, n, sum(1 for f in findings if f['kind'] == k and f['auto'])))
    md.append('')
    for k in sorted(counts):
        md += ['## %s' % k, '']
        for f in findings:
            if f['kind'] == k:
                md.append('- **%s**: "%s" (%s)%s' % (f['where'], f['text'].strip()[:200], f['note'],
                                                     ('; his: "%s"' % f['his'][:240]) if f['his'] else ''))
        md.append('')
    (out_dir / 'AUDIT.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    return record


def fixed_text(text, fixes):
    for f in sorted(fixes, key=lambda x: -x[1]):
        kind, a, z = f[:3]
        if kind == 'delete':
            text = text[:a] + text[z:]
        elif kind == 'unquote':
            text = text[:a] + text[a + 1:z - 1] + text[z:]
        elif kind == 'replace':
            text = text[:a] + f[3] + text[z:]
    return text


def fix(article, audit_path, out_path, kinds=None):
    """ARTICLE with every auto fix in AUDIT_PATH made (or those of KINDS), its links and italics kept; returns the count."""
    record = json.loads(pathlib.Path(audit_path).read_text(encoding='utf-8'))
    by_block = collections.defaultdict(list)
    for f in record['findings']:
        if f['fix'] and (f['auto'] if kinds is None else f['kind'] in kinds):
            by_block[f['block']].append(tuple(f['fix']))
    path = pathlib.Path(article)
    data = path.read_text(encoding='utf-8')
    blocks = {b['i']: b for b in load(path)}
    n = 0
    if path.suffix.lower() in ('.html', '.htm'):
        spans = html_blocks(data)
        for i in sorted(by_block, reverse=True):
            _s, _e, a, z, _k = spans[i]
            inner = data[a:z]
            plain = ''.join(x['t'] for x in HtmlInline(inner).segs)
            if re.sub(r'\s+', ' ', plain).strip() != blocks[i]['text'] or plain != blocks[i]['text']:
                raise SystemExit('block %d: its text has spaces the audit folded; fix it by hand' % i)
            new_inner, dropped, _moved = html_text_edit.set_text(inner, fixed_text(plain, by_block[i]))
            assert not dropped, (i, dropped)
            data = data[:a] + new_inner + data[z:]
            n += len(by_block[i])
    else:
        raw = re.split(r'(\n\s*\n)', data)
        texts = raw[0::2]
        bl = sr.blocks(data)
        if len(texts) != len(bl):
            raise SystemExit('the Markdown has a split post card; fix it by hand')
        for i, fixes in by_block.items():
            core = texts[i].rstrip()
            tail = texts[i][len(core):]
            prefix, body = split_md(core)
            if ''.join(x['t'] for x in sr.segments(body)) != bl[i]['text']:
                raise SystemExit('block %d spans lines or has a split link; fix it by hand' % i)
            new_inner, dropped, _moved = html_text_edit.set_text(md_to_html(body), fixed_text(bl[i]['text'], fixes))
            assert not dropped, (i, dropped)
            texts[i] = prefix + html_to_md(new_inner) + tail
            n += len(fixes)
        raw[0::2] = texts
        data = ''.join(raw)
    pathlib.Path(out_path).write_text(data, encoding='utf-8')
    return n


MD_PREFIX = re.compile(r'^(#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s?)')


def split_md(raw):
    m = MD_PREFIX.match(raw)
    return (m.group(0), raw[m.end():]) if m else ('', raw)


def md_to_html(body):
    out = []
    for s in sr.segments(body):
        t = html.escape(s['t'], quote=False)
        if s['em']:
            t = '<em>%s</em>' % t
        if s['href']:
            t = '<a href="%s">%s</a>' % (html.escape(s['href'], quote=True), t)
        out.append(t)
    return ''.join(out)


def html_to_md(h):
    out, stack = [], []
    for m in re.finditer(r'<(/?)(a|em)(?:\s+href="([^"]*)")?>|([^<]+)', h):
        if m.group(4) is not None:
            out.append(html.unescape(m.group(4)))
        elif m.group(2) == 'em':
            out.append('*')
        elif not m.group(1):
            stack.append(html.unescape(m.group(3)))
            out.append('[')
        else:
            out.append('](%s)' % stack.pop())
    return ''.join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('audit')
    a.add_argument('article')
    a.add_argument('--source', action='append', required=True)
    a.add_argument('--allowed', action='append', default=[])
    a.add_argument('--out', required=True)
    a.add_argument('--parts', type=int, default=6)
    f = sub.add_parser('fix')
    f.add_argument('article')
    f.add_argument('audit')
    f.add_argument('out')
    f.add_argument('--kinds', nargs='*')
    args = ap.parse_args(argv)
    if args.cmd == 'audit':
        r = audit(args.article, args.source, args.allowed, args.out, args.parts)
        print(json.dumps({'blocks': r['blocks'], 'his_word_for_word': r['his_word_for_word'], 'checked': r['checked'],
                          'counts': r['counts'], 'auto_fixes': r['auto_fixes']}))
    else:
        print(fix(args.article, args.audit, args.out, args.kinds), 'fixes made')


if __name__ == '__main__':
    main()
