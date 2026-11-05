#!/usr/bin/env python3
"""fidelity_keys.py - hold a protocol article's doses, units, timings, compounds and warnings to the text as it went in.

The queue's rule for the neuro de-armoring article (articles/inner-child-therapy/experiments/emulate-20260929/ARTICLES.md,
Joel's queue of 2026-09-28): "Supplement protocol. Every compound, dose, unit, timing and warning must come out exactly as
it went in." Emulate's rewrites of it broke that rule in 14 of 40 captures (a lost "below 90 BPM", a "150-300 mg" range
reworded, "Cycle off NAC" made optional; QUALITY-neuro-de-armoring.md on the emulate branch), and a meaning read is a
judgment. This check is not:

- every number as written, with its unit ("300-600 mg/day", "~925 mg", "<20g/day", "Weeks 3-5", "90 BPM") is in the
  draft as often as in the master, and the draft has no number the master doesn't;
- every compound or term the master names (5-HTP, D-Serine, NAC, DMSO, agmatine, ayahuasca, ...) is still named;
- every warning sentence (do not, never, stop, avoid, cap at, without clinician review, ...) still has, in one paragraph,
  its warning word, every term and every number it had (preservation_keys.py's paragraph match).

  python3 tools/humanization/fidelity_keys.py extract MASTER.md KEYS.json
  python3 tools/humanization/fidelity_keys.py check KEYS.json DRAFT.md [--json]

Dashes are made one kind and spaces are collapsed before matching, so "300–600 mg" and "300-600 mg" are the same number;
"300 to 600 mg" is not, and a draft that writes it so fails until the master is read again. Exit 1 when anything is lost.

The owner's own wording. When Joel rewrites a paragraph himself, his words are the protocol: "3 to 7 days" for "3–7 days",
"Don't" for "Do not", "a physician competent to consider ..." for "clinician review". KEYS.json's "owner_wording" records
each one, with where he wrote it, and the check reads his words as the master's: {"his": his words, "for": the master's
words, "by": his answers file and card, "unit": a warning's id}. With "unit", his words are one more way to meet that
warning's key "for" (and only that warning's); without it, they stand for a number or term anywhere in the draft ("Omega-3's"
for "omega-3s"). An entry with no "by", or whose "for" is no key of its unit, is an error, so a slip in the file can't
quietly pass a draft. `extract` keeps an existing file's owner_wording. "Don't" is read as "Do not" in any draft: they are
the same words.

What his own version leaves out. When a version of his drops a compound or a warning, it goes back to him as a question,
never put back over his words. Until he answers, KEYS.json's "owner_open" holds it ({"term" or "unit", "by": where he
wrote the version, "question": the question that asks him}): the check doesn't count it lost, lists it as open with him,
and still fails on anything else lost.

When a warning's words may change. With "warning_words": {"rule": "meaning", "by": ...} in KEYS.json (Joel's answer 8a,
2026-11-04 18:10 UTC: "8a not sure why you had to ask that, the whole point is rewording stuff here"), each warning keeps
only its warning word, its compounds and terms, and its numbers; the other words it was held to (the sentence's rarest
words) are free to change, and the comparative read beside his post checks the meaning.

What his approved cards change. When he approves a card that changes the protocol itself (a warning cut, a dose the
studies support), KEYS.json's "owner_changes" records what that card took out and put in ({"by": his answers file and the
card, "numbers_lost", "numbers_new", "terms_lost": [...], "keys_lost": {a warning's id: [its keys the card took out]}}):
the check reads those as his and still fails on anything else. The script that puts his answers in writes each entry from
the check's own difference before and after that card, so nothing goes in that the card didn't change.
"""
import argparse
import collections
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import preservation_keys as pk  # noqa: E402

DASHES = str.maketrans({'–': '-', '—': '-', '‑': '-', '’': "'", '‘': "'", '“': '"', '”': '"', ' ': ' '})
UNIT = (r"(?:mg/kg|mg/day|g/day|mg/100g|mcg|µg|mg|ml|mL|g|kg|BPM|bpm|%|seconds?|minutes?|Minutes?|min|hours?|days?|"
        r"nights?|weeks?|Weeks?|months?|years?|times|cups?|sprays?|spray|filet|fillet|a\.m\.|point|th)")
NUM = r"\d+(?:[.,]\d+)*"
# a number, with "~", "≈", "<" or ">" before it, a range or ratio after it ("300-600", "1/24th", "D2/D3" is a term), and
# its unit; "Weeks 1-2" and "Week 8+" keep their word in front
NUMBER = re.compile(r"(?:\b(?:Weeks?|Day|Days|Step|Part|Scenario)\s+)?(?:[~≈<>]\s*)?(?<![\w.])" + NUM +
                    r"(?:\s*" + UNIT + r"\b)?(?:\s*(?:-|to|/)\s*(?:[~≈]\s*)?" + NUM + r")?(?:\s*" + UNIT + r"\b)?\+?")
# a word that mixes letters and digits ("5-HTP", "D2/D3", "Nrf2", "PDE-5", "Val158Met"), all capitals ("NAC", "SSRIs"),
# or a capital inside ("DeltaFosB", "GluD"); a number glued to its unit ("400mg", "200g") is a number, not a term
TERM = re.compile(r"\b(?:[A-Za-z]*\d[\w-]*[A-Za-z][\w-]*|\d+-[A-Za-z][\w-]*|[A-Z][A-Za-z]*[A-Z][\w-]*|[A-Z]{2,}s?)"
                  r"(?:/[A-Za-z0-9-]+)?\b")
GLUED = re.compile(r"^" + NUM + r"(?:" + UNIT + r")?(?:-" + NUM + r")?" + UNIT + r"$")
# words in capitals that are words, not compounds ("THE SCIENCE", "DO NOT", "EAT FAT"): a heading or emphasis may be
# written differently without losing anything the rule protects
CAPS_WORDS = {'THE', 'TO', 'OR', 'DO', 'NOT', 'EAT', 'FAT', 'AM', 'PM', 'CRITICAL', 'MEDICAL', 'DISCLAIMER', 'DECISION',
              'SCIENCE', 'SHIELD', 'JAMMER', 'TIMELINE', 'SATIETY', 'KETONE', 'AND', 'IF', 'NO', 'ON', 'IN', 'OF', 'ALL',
              'WARNING', 'IMPORTANT', 'NOTE', 'STOP', 'NEVER', 'ONLY', 'YOU', 'YOUR', 'IS', 'IT', 'A', 'AN', 'BE'}
# compounds and drugs written in lower case, or only capitalized at a sentence start
NAMES = ['agmatine', 'phosphatidylcholine', 'phosphatidylserine', 'uridine', 'magnesium', 'zinc', 'leucine', 'l-serine',
         'd-serine', 'd-cycloserine', 'potassium', 'sodium', 'sulforaphane', 'myrosinase', 'cordyceps', 'choline',
         'cdp-choline', 'ketones', 'ketone', 'iboga', 'ibogaine', 'noribogaine', 'psilocybin', 'shrooms', 'ayahuasca',
         'harmalas', 'harmala', 'kratom', 'clonidine', 'guanfacine', 'nitrates', 'opioids', 'lithium', 'linezolid',
         'tramadol', 'methadone', 'fentanyl', 'ketamine', 'pramipexole', 'ropinirole', 'prozac', 'glutamate', 'dopamine',
         'serotonin', 'cortisol', 'dynorphin', 'oxytocin', 'adrenaline', 'tryptophan', 'l-tryptophan', 'cystine',
         "st. john's wort", 'sam-e', 'fish oil', 'broccoli sprouts', 'mackerel', 'herring', 'tuna', 'potatoes', 'potato',
         'beet greens', 'salmon', 'avocado', 'coconut water', 'eggs', 'hillbilly', 'mazatapec', 'glycinate', 'sulfate',
         'electrolytes', 'mercury']
CUES = re.compile(r"\b(?:do not|don't|never(?! know| had)|stop|stops|avoid|cap at|caution|cautious|careful|warning|without clinician "
                  r"review|consult|must|not for|only if|unless|dangerous|danger|risk|toxicity|exceed|no hot|drop it|"
                  r"poor fit|interaction|interact|conflict)\b", re.I)


def norm(t):
    return re.sub(r'\s+', ' ', t.translate(DASHES))


def plain(md):
    """The article's words: links' text kept, their targets, images and HTML comments dropped."""
    md = re.sub(r'<!--.*?-->', ' ', md, flags=re.S)
    md = re.sub(r'\[image \d+\]\([^)]*\)', ' ', md)
    md = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md)
    return norm(md.replace('*', ''))


def numbers(text, spaced=False):
    """The numbers in the text, spaces taken out ("300-600mg/day") for counting, or kept as written for a paragraph match."""
    out = []
    masked = TERM.sub(lambda m: m.group(0) if GLUED.match(m.group(0)) else ' ' * len(m.group(0)), text)
    for m in NUMBER.finditer(masked):
        out.append(m.group(0).strip() if spaced else re.sub(r'\s+', '', m.group(0)))
    return out


def terms(text):
    # his two hyphens join words ("tuna daily--mercury"; E353 (Inner Child)): a term after them is still a word of its own
    text = text.replace('--', ' -- ')
    found = {m.group(0) for m in TERM.finditer(text) if not GLUED.match(m.group(0)) and m.group(0) not in CAPS_WORDS}
    low = text.lower()
    found |= {n for n in NAMES if re.search(r'(?<![\w-])' + re.escape(n) + r'(?![\w-])', low)}
    return found


def sentences(paragraph):
    return [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"(⚠*])', paragraph) if s.strip()]


STOP = set("""about after again also although always another because been before being both cannot could does doing down
during each even every from have having here into just like little make many more most much must only other over same
should since some such than that their them then there these they this those through very want what when where which while
will with without would your yours you're it's isn't don't""".split())


def anchors(sentence, freq, taken, n=2):
    """The sentence's n rarest words in the article, so a warning that only says "do not" is held to its own words."""
    ws = [w for w in re.findall(r"[a-z][a-z'-]{3,}", sentence.lower()) if w not in STOP and w not in taken]
    return sorted(set(ws), key=lambda w: (freq[w], -len(w), w))[:n]


def extract(master):
    paras = [plain(b) for b in re.split(r'\n\s*\n', master) if plain(b).strip()]
    text = '\n\n'.join(paras)
    freq = collections.Counter(re.findall(r"[a-z][a-z'-]{3,}", text.lower()))
    units = []
    for pi, p in enumerate(paras):
        if p.lstrip().startswith('#'):
            continue
        for s in sentences(p):
            cues = sorted({m.group(0).lower() for m in CUES.finditer(s)})
            if not cues:
                continue
            keys = [[c] for c in cues] + [[t] for t in sorted(terms(s))] + [[n] for n in numbers(s, spaced=True)]
            taken = {x.lower() for k in keys for x in k}
            keys += [[w] for w in anchors(s, freq, taken | set(cues))]
            units.append({'id': 'W%03d' % (len(units) + 1), 'what': s.strip()[:400], 'paragraph': pi, 'keys': keys})
    return {'about': 'fidelity_keys.py extract: the numbers, terms and warnings of the master, which a draft must keep',
            'numbers': dict(sorted(collections.Counter(numbers(text)).items())),
            'terms': sorted(terms(text)), 'units': units}


def owner_wording(keys):
    """(substitutions, units): his words for a number or term, each (his, the master's) to put in the draft's text before
    counting, and the warning units with his words added to the keys they meet. Raises ValueError on an entry that
    names no source or no key of its unit."""
    subs, units = [], [dict(u, keys=[list(k) for k in u['keys']]) for u in keys['units']]
    by_id = {u['id']: u for u in units}
    for w in keys.get('owner_wording', []):
        if not str(w.get('by', '')).strip() or not w.get('his') or not w.get('for'):
            raise ValueError('owner_wording entry without his words, the master\'s or where he wrote them: %r' % (w,))
        if not w.get('unit'):
            subs.append((norm(w['his']), norm(w['for'])))
            continue
        u = by_id.get(w['unit'])
        hit = [k for k in (u['keys'] if u else []) if pk.normalize(w['for']) in {pk.normalize(x) for x in k}]
        if not hit:
            raise ValueError('owner_wording: %r is no key of %s' % (w['for'], w['unit']))
        hit[0].append(w['his'])
    return subs, units


def check(keys, draft):
    subs, units = owner_wording(keys)
    # "don't" is "do not", for the warning words and everything else (the same words, contracted)
    subs.append(("don't", 'do not'))
    subs.append(("Don't", 'Do not'))
    for u in units:
        u['keys'] = [[('do not' if pk.normalize(x) == "don't" else x) for x in k] for k in u['keys']]

    def his(t):
        for a, b in subs:
            t = t.replace(a, b)
        return t
    # a limit said in words matched the post's sign: "under 20g/day" for its "<20g/day" (the neuro de-armoring lane,
    # 2026-11-05, Strategy B: the same limit, which a sentence can't say with "<")
    signed = {n for n in keys['numbers'] if n.startswith('<')}

    def limit(t):
        def one(m):
            n = '<' + re.sub(r'\s+', '', m.group(1))
            return n if n in signed else m.group(0)
        return re.sub(r'\b(?:under|less than|below) (\d[^\s,;)]*[^\s,;).])', one, t)
    text = limit(his(plain(draft)))
    have = collections.Counter(numbers(text))
    want = collections.Counter(keys['numbers'])
    lost_numbers = sorted((want - have).elements())
    new_numbers = sorted((have - want).elements())
    lost_terms = sorted(set(keys['terms']) - terms(text))
    # a dash matched whatever its spaces and length: the typographic swap (E337 (gut)) made the post's "numb—living" "numb –
    # living", and since 2026-11-04 makes it his "numb--living" (E353 (Inner Child))
    def dash(t):
        return re.sub(r'[ \t]*-+[ \t]*', '-', t)

    # a number and its unit matched with or without the space between them: his "50mg" for the post's "50 mg" (Joel,
    # 2026-11-04 18:09 UTC, on the 5-HTP trial: "then i just removed spaces before "mg" and that helped a bit ... don't think
    # i've seen humans put spaces there"); the count above already takes the spaces out
    def glue(t):
        return re.sub(r'(\d)[ \t]+(?=(?:mg|mcg|µg|g|kg|ml|mL)\b)', r'\1', t)
    draft_paras = glue(dash('\n\n'.join(limit(his(plain(b))) for b in re.split(r'\n\s*\n', draft))))
    meaning = (keys.get('warning_words') or {}).get('rule') == 'meaning'
    term_set = {pk.normalize(t) for t in keys['terms']}

    def same(k):
        return tuple(sorted(pk.normalize(glue(dash(norm(x)))) for x in k))
    # the keys his approved cards took out (keys['owner_changes'] below) leave their units before the paragraph match, so a
    # unit with few keys left can't be matched to the wrong paragraph
    taken = collections.defaultdict(set)
    for c in keys.get('owner_changes', []):
        for uid, ks in (c.get('keys_lost') or {}).items():
            taken[uid] |= {same(k) for k in ks}
    for u in units:
        u['keys'] = [[glue(dash(norm(x))) for x in k] for k in u['keys'] if same(k) not in taken[u['id']]]
        if meaning:
            # his answer 8a: a warning's words may change when its meaning stays. The check keeps what a reader acts on, the
            # warning word ("do not", "stop", "avoid" ...), every compound or term and every number; the other words of the
            # sentence are left to the comparative read beside his post (E284, E294). A warning that names no compound and no
            # number ("Do not push through.") keeps its own words too, since they are what its warning word applies to
            named = [k for k in u['keys'] if any(NUMBER.search(x) or TERM.search(x) or pk.normalize(x) in term_set for x in k)]
            if named:
                u['keys'] = [k for k in u['keys'] if k in named or any(CUES.search(x) for x in k)]
    lost_warnings = pk.check({'units': units}, draft_paras)
    # what his approved cards changed (keys['owner_changes']): his, neither lost nor new
    changes = []
    for c in keys.get('owner_changes', []):
        if not str(c.get('by', '')).strip():
            raise ValueError('owner_changes entry without the answers file and card that approved it: %r' % (c,))
        for n in c.get('numbers_lost', []):
            if n in lost_numbers:
                lost_numbers.remove(n)
        for n in c.get('numbers_new', []):
            if n in new_numbers:
                new_numbers.remove(n)
        for t in c.get('terms_lost', []):
            if t in lost_terms:
                lost_terms.remove(t)
        for uid, ks in (c.get('keys_lost') or {}).items():
            out = {same(k) for k in ks}
            for u in lost_warnings:
                if u['id'] == uid:
                    u['missing'] = [k for k in u['missing'] if same(k) not in out]
        lost_warnings = [u for u in lost_warnings if u['missing']]
        changes.append(c.get('by'))
    # what his own version left out, held open until he answers (keys['owner_open']): not lost, not passed either
    open_ = []
    for o in keys.get('owner_open', []):
        if not str(o.get('by', '')).strip() or not str(o.get('question', '')).strip() or not (o.get('term') or o.get('unit')):
            raise ValueError('owner_open entry without the term or unit, where he left it out, or the question: %r' % (o,))
        hit = False
        if o.get('term') in lost_terms:
            lost_terms.remove(o['term'])
            hit = True
        if o.get('term'):
            # a warning that misses only the open term isn't lost either
            for u in lost_warnings:
                u['missing'] = [k for k in u['missing'] if pk.normalize(o['term']) not in {pk.normalize(x) for x in k}]
            kept = [u for u in lost_warnings if u['missing']]
            hit = hit or len(kept) < len(lost_warnings)
            lost_warnings = kept
        if o.get('unit') and any(u['id'] == o['unit'] for u in lost_warnings):
            lost_warnings = [u for u in lost_warnings if u['id'] != o['unit']]
            hit = True
        if hit:
            open_.append(o)
    return {'numbers_lost': lost_numbers, 'numbers_new': new_numbers, 'terms_lost': lost_terms,
            'warnings_lost': lost_warnings, 'open_with_owner': open_, 'owner_changes': changes,
            'pass': not (lost_numbers or new_numbers or lost_terms or lost_warnings)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    e = sub.add_parser('extract'); e.add_argument('master'); e.add_argument('out')
    c = sub.add_parser('check'); c.add_argument('keys'); c.add_argument('draft'); c.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    if a.cmd == 'extract':
        k = extract(pathlib.Path(a.master).read_text(encoding='utf-8'))
        old = pathlib.Path(a.out)
        if old.exists() and json.loads(old.read_text(encoding='utf-8')).get('owner_wording'):
            k['owner_wording'] = json.loads(old.read_text(encoding='utf-8'))['owner_wording']
        pathlib.Path(a.out).write_text(json.dumps(k, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('numbers %d (%d distinct), terms %d, warning sentences %d' % (
            sum(k['numbers'].values()), len(k['numbers']), len(k['terms']), len(k['units'])))
        return 0
    r = check(json.loads(pathlib.Path(a.keys).read_text(encoding='utf-8')), pathlib.Path(a.draft).read_text(encoding='utf-8'))
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        for k in ('numbers_lost', 'numbers_new', 'terms_lost'):
            for x in r[k]:
                print('%s: %s' % (k, x))
        for u in r['warnings_lost']:
            print('warning lost: %s | missing %s' % (u['what'][:160], u['missing']))
        for o in r['open_with_owner']:
            print('open with him: %s (%s)' % (o.get('term') or o.get('unit'), o['question']))
        print('verdict:', ('PASS' if r['pass'] else 'FAIL') + (' (%d open with him)' % len(r['open_with_owner'])
                                                              if r['open_with_owner'] else ''))
    return 0 if r['pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
