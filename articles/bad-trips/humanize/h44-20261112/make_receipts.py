#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's tests (gate E365), as in ../h43-20261111/make_receipts.py.
His own sentences (his round-34 version, HIS-LINES.txt) are marked his and need no payoff of mine.

  python3 make_receipts.py KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8')) if (HERE / 'NEEDED.json').exists() else {}
HIS_WHOSE = ('his own: his round-34 version of Risk of Harm\'s first paragraph, from his Pangram check aa15e193 '
             '(experiments/t34-answers/JOEL-VERSION-TEACH-HARM-aa15e193.md)')
R = {
 'harm-s1': {
  'section': "Risk of Harm: When Peer Support Isn't Enough",
  'reader': 'someone sitting with a person in a hard trip, deciding whether to get urgent help now, and which number to call',
  'his': True,
  'mine': [
   ('they know this part is when to get urgent help', 'the heading', 'none: the section heading itself'),
   ("they call 911 for immediate danger, a medical emergency, a weapon or a crime in progress", 'after his reasons, which number',
    'In the United States, call 911'),
   ("they call 988 for a mental-health crisis with nobody in physical danger, for help calming it and finding local help",
    'the other number, and when', "If it's a mental-health crisis"),
   ('they find their local emergency and crisis numbers ahead of time outside the United States', 'the rest of the world', 'Anywhere else'),
  ],
  'placement': "Risk of Harm, after his two paragraphs of when to get urgent help: which number, said once",
  'why_reading': 'it tells a sitter to get urgent help the moment they think someone might get hurt',
  'same_point': "the 911 line's old reasons (violence underway, a situation you cannot safely contain) and its second 'immediate "
                "danger' and 'medical emergency' are cut: his paragraph says the reasons once (his round-34 comment, 'make sure "
                "this is only said once')",
  'questions': {
   'Q1': 'PASS: his paragraphs open on the bar; the number paragraph opens on where it applies',
   'Q2': "PASS: each instruction is the sitter's own act (call, look up)",
   'Q3': 'PASS: "911", "988", "your local emergency services number and a crisis line" say which',
   'Q4': 'PASS: "de-escalation" said as calming things down',
   'Q5': 'PASS: "and also", "If", "Anywhere else" say each relation',
   'Q6': 'PASS: when to get help, then which number',
   'Q7': 'PASS: each line bears on calling now',
   'Q8': 'PASS: every line is about getting urgent help',
   'Q9': 'PASS: the reasons said once; one number a sentence',
  }},
 'oral-s1': {
  'section': 'Recent Oral Toxic Ingestion',
  'reader': 'someone with a person who swallowed too much of something recently, deciding what to do first: what to find out, whether to give activated charcoal, whether to call poison control',
  'his': False,
  'mine': [
   ('they know this part is for something swallowed recently', 'the heading', 'none: the section heading itself'),
   ('they find out what was swallowed, how much and when before picking a remedy', 'it opens the section under its heading',
    'none: the first sentence under its heading'),
   ('they look at what the body is doing', 'the next thing to find out', 'Then'),
   ('they tell slow breathing from a stimulant high, serotonin toxicity, a seizure or overheating, since each needs its own remedy',
    'what the body might be doing, and why it matters', 'so each gets its own remedy'),
   ('they give activated charcoal only for something it binds, swallowed recently, if the person can swallow safely', 'the first remedy for this',
    'Activated charcoal can help'),
   ("they know it won't bind everything and can soak up needed medicine", 'its limits', 'It won\'t'),
   ("they don't give it to someone vomiting, sedated, seizing or unable to protect their airway, who could breathe it in", 'its danger',
    'And if they'),
   ('they can read the clinical review behind it', 'its source', 'none: the source link for the paragraph'),
   ('they call poison control when they are unsure what the substance does, whether there is a delayed risk, or whether charcoal is worth it',
    'the next help', 'Poison control can be useful'),
   ("they know he doesn't treat calling as a must, since it varies by country and by who answers", 'his view of it', 'though'),
   ('they know poison control helps them decide and the first aid is theirs', 'what it is for', "They're there to help you decide"),
  ],
  'placement': 'Recent Oral Toxic Ingestion, in the medical part after the acute intro',
  'why_reading': 'it tells someone facing an "overdose" to find out what was swallowed before picking a remedy',
  'same_point': 'none: read the section to the next heading; charcoal is said here and in the gut tools as a different use',
  'questions': {
   'Q1': 'PASS: each paragraph opens on its point (what to find out, when charcoal helps, when poison control helps)',
   'Q2': "PASS: each instruction is the reader's own act",
   'Q3': 'PASS: "activated charcoal", "poison control" say which',
   'Q4': 'PASS: "respiratory depression" and "aspiration" explained where they are used',
   'Q5': 'PASS: "because", "Then", "so", "as long as", "And if", "though" say each relation',
   'Q6': 'PASS: what to find out, what charcoal can and can\'t do, then poison control',
   'Q7': 'PASS: each fact bears on what they do now',
   'Q8': 'PASS: all three paragraphs are about something swallowed',
   'Q9': 'PASS: one step a sentence',
  }},
}


# Paragraph tests: their unit's entries for the same sentences; the needed read is the unit's, which read them in place
PARA = {'harm-p911': ('harm-s1', 'it tells a sitter which number to call in the United States'),
        'oral-p1': ('oral-s1', 'it tells someone facing an "overdose" to find out what was swallowed before picking a remedy'),
        'oral-p2': ('oral-s1', 'it tells someone thinking of activated charcoal when it can help'),
        'oral-p3': ('oral-s1', 'it tells someone when poison control is worth calling')}


def para_entry(key):
    unit, why = PARA[key]
    d = R[unit]
    tmp = HERE / ('.%s.json' % key)
    subprocess.run([sys.executable, str(SR), 'make', str(HERE / ('TEST-%s.txt' % key)), '--section', d['section'], '--reader',
                    d['reader'], '--out', str(tmp)], check=True, capture_output=True)
    sents = [x['s'] for x in json.loads(tmp.read_text(encoding='utf-8'))['sentences']]
    tmp.unlink()
    usk = HERE / ('.%s-unit.json' % key)
    subprocess.run([sys.executable, str(SR), 'make', str(HERE / ('TEST-%s.txt' % unit)), '--section', d['section'], '--reader',
                    d['reader'], '--out', str(usk)], check=True, capture_output=True)
    usents = [x['s'] for x in json.loads(usk.read_text(encoding='utf-8'))['sentences']]
    usk.unlink()
    mine = iter(d['mine'])
    his = [l.strip() for l in (HERE / 'HIS-LINES.txt').read_text(encoding='utf-8').splitlines() if l.strip()] if d['his'] else []
    entries = {}
    for x in usents:
        if any(x in h for h in his):
            continue
        entries[x] = next(mine)
    e = dict(d)
    e['his'] = False
    e['mine'] = [entries[x] for x in sents]
    e['why_reading'] = why
    e['placement'] = d['placement'] + ' (checked here by itself first, E343)'
    n = NEEDED.get(unit)
    if n:
        NEEDED[key] = {'reader': n['reader'] + '; this paragraph is part of that test, read there in place',
                       'unneeded': [x for x in n['unneeded'] if x in sents],
                       'kept': {k: v for k, v in n['kept'].items() if k in sents}}
    return e


for _k in PARA:
    if (HERE / ('TEST-%s.txt' % _k)).exists():
        R[_k] = para_entry(_k)


def fill(key):
    text = HERE / ('TEST-%s.txt' % key)
    out = HERE / ('TEST-%s.receipt.json' % key)
    d = R[key]
    cmd = [sys.executable, str(SR), 'make', str(text), '--section', d['section'], '--reader', d['reader'], '--out', str(out)]
    if d['his']:
        cmd += ['--his', str(HERE / 'HIS-LINES.txt'), '--whose', HIS_WHOSE]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); return
    rc = json.loads(out.read_text(encoding='utf-8'))
    mine = iter(d['mine'])
    first = True
    for s in rc['sentences']:
        if s.get('his'):
            first = False
            continue
        payoff, follows, link = next(mine)
        s['payoff'], s['follows'] = payoff, follows
        if not first:
            s['link'] = link
        first = False
    rc['placement'], rc['same_point'], rc['questions'] = d['placement'], d['same_point'], d['questions']
    rc['opens']['why_reading'] = d['why_reading']
    if key in NEEDED:
        rc['needed'] = NEEDED[key]
    out.write_text(json.dumps(rc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    o = (c.stdout + c.stderr).strip()
    print(key, o.splitlines()[-1] if o else c.returncode)
    if c.returncode:
        print(o)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
