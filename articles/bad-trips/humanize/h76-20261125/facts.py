#!/usr/bin/env python3
"""facts.py - (copied from h75, turn 68: his round-57 kidney paragraph says 'muscle breakdown' and 'gram-per-minute', and 'injure the kidneys' carries the study's link) the MDMA: Magnesium Alarm section's doses, products and events, which a rewrite keeps word for word (turn
65): the R50 fidelity keys hold only digits and a few terms, and these are spelled out. Run on a guide (or a copy):

  python3 facts.py GUIDE.md
"""
import re, sys

FACTS = ['Dead Sea magnesium chloride hexahydrate flakes', 'one gram per minute', 'twenty minutes', 'twenty grams',
         'forty grams', 'second wife', 'severe convulsions', 'IV potassium was the only treatment',
         'gram-per-minute magnesium chloride dosing approach', 'muscle breakdown', 'injure the kidneys', 'PMC10509448', '27917269', 'impaired kidneys',
         'taken to a hospital ASAP',   # (turn 68) his round-57 version: 'one-gram-per-minute', 'rhabdomyolysis' and 'acute kidney injury' are his changes (FIDELITY-KEYS-R57.json)
         'earliest warning', 'absorbs faster and better than any other form', "what I know works best"]   # (turn 67) 'far better than magnesium oxide' and '11794633' out: his CHLORIDE-CLAIM answer of round 56 ("remove the source then if there's no source")
# (turn 66) 'meaningful' and 'essentially zero' out: his round-55 versions cut them (KEEP-AS-IS C15, C16)


def plain(s):
    return re.sub(r'\s+', ' ', re.sub(r'\[([^\]]*)\]\(([^)]*)\)', r'\1 \2', s).replace('**', ''))


t = plain(open(sys.argv[1], encoding='utf-8').read())
lost = [f for f in FACTS if f.lower() not in t.lower()]   # a term at the start of a sentence is the same term
print('facts: %d of %d kept%s' % (len(FACTS) - len(lost), len(FACTS), ('; LOST: ' + '; '.join(lost)) if lost else ''))
sys.exit(1 if lost else 0)
