#!/usr/bin/env python3
"""fill_receipt.py - the making-sense receipt of the two medical fixes to his round-41 MDMA version (TEST-mdma-hisfix.txt)."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
p = HERE / 'TEST-mdma-hisfix.receipt.json'
r = json.loads(p.read_text())
S = [x['s'] for x in r['sentences']]
import sys
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import sense_receipt
read = sense_receipt.sentences((HERE / 'reads' / 'read-text-mdma-hisfix.txt').read_text().strip())
HIS = 'his line (his round-41 version, c45651d9)'
pay = [
 ("they make the jaw tension the last dose and get their friend to slow down and cool off", "his paragraph opens", None),
 ("they have their friend sip an electrolyte drink when thirsty, not drink a lot of plain water", HIS, 'none: ' + HIS),
 ("they call medics when confusion or a headache gets worse or vomiting won't stop, and from then on give no more to "
  "drink, since by then even an electrolyte drink can't fix the sodium", "his first call-medics signs, with what his "
  "parenthesis meant said plainly: his question was whether to keep giving electrolytes", "sodium might be too low by then"),
 ("they call medics when muscles keep weakening or palpitations keep getting stronger", HIS, 'none: ' + HIS),
 ("they know a seizure or collapse can come from low sodium as well as potassium, overheating or MDMA toxicity",
  "his last call-medics sign, low sodium added: it is the electrolyte most often behind MDMA seizures", "low sodium or potassium")]
for s, (a, b, c) in zip(r['sentences'], pay):
    s['payoff'], s['follows'] = a, b
    if 'link' in s:
        s['link'] = c if c and (c.startswith('none:') or c in s['s']) else 'none: %s' % b
r['checked'] = [
 {'point': 'whether to keep giving electrolyte drinks once low-sodium signs show (his question)',
  'found': ('the Wilderness Medical Society guidelines (2019 update, in American Family Physician 2021): overdrinking water or '
            'sports drinks, both hypotonic, is the usual cause; fluids are restricted once low sodium is suspected; severe '
            'cases get hypertonic saline; MDMA cases in hospital the same (Merck Manual: fluid restriction or hypertonic IV '
            'fluids)'),
  'still_needed': 'yes: they stop giving drinks once those signs show and leave the fix to the hospital', 'fate': 'changed'},
 {'point': 'what a seizure or collapse can come from',
  'found': ('low sodium is the electrolyte most often behind MDMA seizures (the case reports and reviews the search found; '
            'hypertonic saline given for them); severe low potassium brings weakness and heart rhythm trouble'),
  'still_needed': 'yes: they know low sodium can bring a seizure too, not only low potassium', 'fate': 'changed'}]
r['placement'] = "MDMA: Jaw Tension Is the Magnesium Alarm, after his second wife's story (B118), before the kidney paragraph (B120)"
r['opens']['why_reading'] = "it tells someone whose friend's jaw has tensed on MDMA what to do now and which signs mean medics"
r['same_point'] = ("none: read the MDMA section from its heading to the next for drinking and the call-medics signs: only this "
                   "paragraph says them; B120 names acute kidney injury with its review")
r['questions'] = {
 'Q1': 'PASS: his order kept; the parenthesis now says what "too late for an easy fix" meant',
 'Q2': 'PASS: "don\'t give them any more to drink": the helper\'s act',
 'Q3': 'PASS: "even an electrolyte drink", "low sodium or potassium"',
 'Q4': 'PASS: no new term',
 'Q5': 'PASS: "by then" ties the stop to the signs before it, which keeps it apart from his sipping line',
 'Q6': 'PASS: his order',
 'Q7': 'PASS: each bears on a friend on MDMA',
 'Q8': 'PASS: his signs, grouped as he grouped them',
 'Q9': 'PASS: his sentences'}
NEED = 'a fresh agent given tools/humanization/needed_read_brief.md with only the text, its heading and what it is for (reads/need.txt), of reads/read-text-mdma-hisfix.txt'
HISF = 'a fresh agent given tools/humanization/his_fixes_brief.md with the text, one sentence a line (reads/his.txt), of reads/read-text-mdma-hisfix.txt'
FIT = 'a fresh agent given tools/humanization/fit_read_brief.md, the universal version (reads/fit.txt), of reads/read-text-mdma-hisfix.txt'
his = 'they know %s; his sentence, his to change: what the read found goes to him on round 42\'s card'
r['needed'] = {'reader': NEED, 'unneeded': [S[4]], 'kept': {S[4]: ('they know what a seizure or collapse can come from; his '
               'sentence with "low sodium or" added; the read\'s point, that it says no action, goes to him on the card, the '
               'sentence sitting under his "The following indicators would justify calling medics:"')}}
r['his_fixes'] = {'reader': HISF, 'marked': [
    {'s': read[2], 'difference': '1, 5', 'draft': 'mdma-hisfix as read'}, {'s': S[3], 'difference': '7', 'draft': 'mdma-hisfix'},
    {'s': S[4], 'difference': '1, 7', 'draft': 'mdma-hisfix'}],
    'kept': {S[3]: his % 'weakening muscles and stronger palpitations mean medics',
             S[4]: his % 'what a seizure or collapse can come from (low sodium added)'}}
r['fit'] = {'reader': FIT, 'marked': [{'s': read[2], 'found': "ANYWAY, CAN'T TELL, MISREAD"}, {'s': S[3], 'found': "ANYWAY, CAN'T TELL"}],
            'kept': {S[3]: his % 'weakening muscles and stronger palpitations mean medics'}}
p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
print('filled')
