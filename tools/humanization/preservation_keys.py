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
"""
import argparse, json, re, sys

QUOTES = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"', '–': '-', '—': '-'})


def normalize(text):
    text = re.sub(r'<!--.*?-->', ' ', text, flags=re.S)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = text.replace('*', '').translate(QUOTES)
    return re.sub(r'\s+', ' ', text).lower()


def check(keys_doc, draft):
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
        if best:
            missing.append({'id': unit['id'], 'what': unit.get('what', ''), 'missing': best})
    return missing


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('keys')
    ap.add_argument('draft')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    keys_doc = json.load(open(a.keys, encoding='utf-8'))
    missing = check(keys_doc, open(a.draft, encoding='utf-8').read())
    if a.json:
        print(json.dumps({'units': len(keys_doc['units']), 'missing': missing}, ensure_ascii=False, indent=1))
    else:
        print('== preservation_keys: %s, %d units' % (a.draft, len(keys_doc['units'])))
        for m in missing:
            print('MISSING %s (%s): %s' % (m['id'], m['what'], ' | '.join(' or '.join(repr(x) for x in alts) for alts in m['missing'])))
        print('verdict: %s' % ('FAIL' if missing else 'PASS'))
    return 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main())
