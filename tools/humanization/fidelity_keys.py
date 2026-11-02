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


def check(keys, draft):
    text = plain(draft)
    have = collections.Counter(numbers(text))
    want = collections.Counter(keys['numbers'])
    lost_numbers = sorted((want - have).elements())
    new_numbers = sorted((have - want).elements())
    lost_terms = sorted(set(keys['terms']) - terms(text))
    draft_paras = '\n\n'.join(plain(b) for b in re.split(r'\n\s*\n', draft))
    lost_warnings = pk.check({'units': keys['units']}, draft_paras)
    return {'numbers_lost': lost_numbers, 'numbers_new': new_numbers, 'terms_lost': lost_terms,
            'warnings_lost': lost_warnings,
            'pass': not (lost_numbers or new_numbers or lost_terms or lost_warnings)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    e = sub.add_parser('extract'); e.add_argument('master'); e.add_argument('out')
    c = sub.add_parser('check'); c.add_argument('keys'); c.add_argument('draft'); c.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    if a.cmd == 'extract':
        k = extract(pathlib.Path(a.master).read_text(encoding='utf-8'))
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
        print('verdict:', 'PASS' if r['pass'] else 'FAIL')
    return 0 if r['pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
