#!/usr/bin/env python3
"""preservation_keys.py - check that a draft still has the words each preserved meaning rests on.

Joel, 2026-10-12 05:33 UTC, on community section 12: "p3 got broken because you changed "good enough" for community to
"good enough" and i'm not understand anymore what they are good enough for. then you broke p7 by reducing it to "but
it's not infinite" ? what? p16 also broke the meaning ... you can't just remove "remains" and keep the same meaning ...
revert those to guide exactly. debug the error so it doesn't happen again."

Each of those breaks dropped a word that the section's stance ledger (its preservation units) had named: "infinitely
absorbent", "this language of capacity", "Pretending capacity is unlimited", "remains". Two or three meaning traces called
each one EQUIVALENT, and the ledger itself had shortened "good enough" for community to "good enough". A trace is a
judgment; this check is not. Every unit lists its key words, and a draft that has lost one fails until the unit's words
are back or Joel has authorized the change.

Usage:
  python3 tools/humanization/preservation_keys.py KEYS.json DRAFT.md [--json]

KEYS.json: {"section": "...", "units": [{"id": "U7", "what": "...", "keys": [["for community"], ["good enough"]]}, ...]}
A key is a list of alternatives. A unit passes when one paragraph of the draft has every key (at least one alternative
of each); a unit whose meaning spans paragraphs says so with "span": 2 (or more), and then any run of that many
paragraphs will do. Matching against one paragraph, not the whole draft, matters: "free resource" appears all through
section 12, so a whole-draft match would pass a paragraph that had lost it. Matching ignores case, straightens curly
quotes and apostrophes, and collapses spaces; HTML comments, Markdown link targets and emphasis marks are dropped first.
Exit 1 when a unit is missing a key.

"section_terms" (optional, 2026-10-12): the section's own words for its subject, such as "absorb" in "The Math of
Absorption". A unit whose meaning ("what") uses one must list it as a key: trace r6 found "tolerate" where the published
P13 says "absorb disruption", and the unit had never listed "absorb". The check fails the key file itself when a unit
leaves its section term out.

"elsewhere" (2026-10-17, Joel's standing dedup rule of 02:07 UTC: "you can only cut if it isn't losing important meaning
or there's no good way to merge"): a unit a dedup cut leaves to another section names that section and the words it
rests on there, {"section": "# Dissolution and Exit", "words": ["foundation", "film"], "why": "..."}. It passes only when
--article is given and that section of the article has every one of the words; otherwise it is missing like any other.
A key file can't use this to drop a point: the other section has to carry it, word for word.
"""
import argparse, json, re, sys

QUOTES = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"', '–': '-', '—': '-'})


def normalize(text):
    text = re.sub(r'<!--.*?-->', ' ', text, flags=re.S)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = text.replace('*', '').translate(QUOTES)
    return re.sub(r'\s+', ' ', text).lower()


def incomplete_units(keys_doc):
    """Units whose meaning uses a section term that none of their keys requires."""
    out = []
    for term in keys_doc.get('section_terms', []):
        t = normalize(term)
        for unit in keys_doc['units']:
            if t in normalize(unit.get('what', '')) and not any(t in normalize(a) for alts in unit['keys'] for a in alts):
                out.append({'id': unit['id'], 'what': unit.get('what', ''), 'term': term})
    return out


def section_of(article, heading):
    """The text of the section under the heading (to the next heading of its level or higher), or None."""
    lines = article.split('\n')
    level = len(heading) - len(heading.lstrip('#'))
    out, inside = [], False
    for line in lines:
        if line.strip() == heading.strip():
            inside = True
            continue
        if inside and line.startswith('#') and len(line) - len(line.lstrip('#')) <= level:
            break
        if inside:
            out.append(line)
    return '\n'.join(out) if inside else None


def carried(unit, article):
    """True when the unit's "elsewhere" section of the article has every word it names."""
    e = unit.get('elsewhere')
    if not e or article is None:
        return False
    sec = section_of(article, e['section'])
    return sec is not None and all(normalize(w) in normalize(sec) for w in e['words'])


def check(keys_doc, draft, article=None, carried_out=None):
    paras = [normalize(b) for b in re.split(r'\n\s*\n', draft) if normalize(b).strip()]
    missing = []
    for unit in keys_doc['units']:
        span = max(1, int(unit.get('span', 1)))
        windows = [' '.join(paras[i:i + span]) for i in range(max(1, len(paras) - span + 1))]
        best = None
        for w in windows:
            lost = [alts for alts in unit['keys'] if not any(normalize(a) in w for a in alts)]
            if best is None or len(lost) < len(best):
                best = lost
            if not lost:
                break
        if best and carried(unit, article):
            if carried_out is not None:
                carried_out.append({'id': unit['id'], 'what': unit.get('what', ''), 'section': unit['elsewhere']['section'],
                                    'why': unit['elsewhere'].get('why', '')})
        elif best:
            missing.append({'id': unit['id'], 'what': unit.get('what', ''), 'missing': best})
    return missing


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('keys')
    ap.add_argument('draft')
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--article', help='the article with the other sections, for units a dedup left "elsewhere"')
    a = ap.parse_args(argv)
    keys_doc = json.load(open(a.keys, encoding='utf-8'))
    art = open(a.article, encoding='utf-8').read() if a.article else None
    moved = []
    missing = check(keys_doc, open(a.draft, encoding='utf-8').read(), art, moved)
    gaps = incomplete_units(keys_doc)
    if a.json:
        print(json.dumps({'units': len(keys_doc['units']), 'missing': missing, 'carried_elsewhere': moved, 'key_file_gaps': gaps},
                         ensure_ascii=False, indent=1))
    else:
        print('== preservation_keys: %s, %d units' % (a.draft, len(keys_doc['units'])))
        for g in gaps:
            print('KEY FILE %s (%s): its meaning uses the section\'s term %r, but no key requires it' % (g['id'], g['what'], g['term']))
        for m in moved:
            print('CARRIED ELSEWHERE %s (%s): in %s (%s)' % (m['id'], m['what'], m['section'], m['why']))
        for m in missing:
            print('MISSING %s (%s): %s' % (m['id'], m['what'], ' | '.join(' or '.join(repr(x) for x in alts) for alts in m['missing'])))
        print('verdict: %s' % ('FAIL' if missing or gaps else 'PASS'))
    return 1 if missing or gaps else 0


if __name__ == '__main__':
    sys.exit(main())
