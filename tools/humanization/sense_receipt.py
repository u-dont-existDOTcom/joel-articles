#!/usr/bin/env python3
"""sense_receipt.py - the making-sense read's receipt: the record, sentence by sentence, that a paragraph I wrote or
changed was read for sense before it goes to Pangram or onto Joel's marking page (gate E365, which enforces E362).

Joel, 2026-11-05 15:14 UTC, on round 6 of the bad trips guide, where my card had kept the 7-OH-CBD point after checking it
had taken away its reason for being there, and had brought in a trial of focal seizures for a reader facing a seizure
from MDMA or a psychedelic overdose, which are generalized: "i already told you to stop putting stuff in that is wasting
reader's time ... READ what you wrote, it literally is a whole big waste of time to talk about this, there's NO PAYOFF
... why did i have to tell you this twice? fix the way you work because i'm not telling you the same stuff over and
over." The making-sense read (docs/MAKING-SENSE.md) already asked "does this fact help this reader now?" (E360). Nothing
made me answer it for each sentence before the card went out, so it wasn't answered. UDA's
patterns/task-time-lesson-activation.md: when the owner catches a violation of a rule he already stated, repair the
enforcement, not only the candidate. This is the enforcement: tools/humanization/pangram_ledger.py predict refuses a text
of mine without a receipt that passes here, and tools/humanization/suggestion_review.py refuses a card that adds or
changes words without one (reviews built from 2026-11-05).

The judging is mine (a model reads meaning; nothing here judges it): the receipt makes me write, for every sentence, what
this section's reader does or understands differently because of it, and why it comes where it does. The code checks
only what code can: the receipt is for this exact text (SHA-256), it covers every sentence in order, nothing is left
blank or marked as having no payoff, a point whose checking took away its reason for being there is cut, the placement
is said, and each of the read's nine questions is answered PASS (or N/A with a reason).

  python3 tools/humanization/sense_receipt.py make TEXT --section "Active Seizure" --reader "who reads it, facing what
          exactly" [--his HIS.txt] --out RECEIPT.json
  python3 tools/humanization/sense_receipt.py check TEXT RECEIPT.json

make writes the receipt to fill: every sentence of TEXT with an empty payoff and follows (a sentence found word for word
in HIS.txt, Joel's own text, is marked his and needs neither), the nine questions, placement and checked. Fill it by
editing the JSON, then check it. A sentence whose payoff you can't write goes from the text; make the receipt again.

The fields:
  reader     who reads this section and what exactly they face: the case, not the topic ("someone with a person having
             a seizure from MDMA or a psychedelic overdose, which is generalized", not "someone interested in seizures").
             Every payoff is judged against it.
  sentences  [{"s": the sentence, "his": true for Joel's words, "payoff": what this reader does or understands
             differently because of it, "follows": why it comes after the sentence before (what it continues, answers
             or turns on); for the first sentence, why it follows the paragraph or heading before it}]
  checked    [{"point", "found": what the source says, "still_needed": "yes: ..." or "no: ..." (does the reason this
             point is here survive what the check found?), "fate": "kept", "changed" or "cut"}]   every point I checked
             against a source; "no" must be "cut" (the 7-OH-CBD case: it was there because it might be more active; the
             check found it about as active as CBD, so nothing was missed and the point had no payoff left)
  placement  where the paragraph sits and why there: next to what it continues; same-topic paragraphs together, a
             different topic before or after the group, never inside it; and what its first "also", "this" or "as for"
             now points to (Joel, 2026-11-05: "the problem was simply that you had the ideas out of their natural
             order"; "we should move the non-cannabis para above all the cannabis info ... isn't that obvious?")
  questions  Q1 to Q9, docs/MAKING-SENSE.md's questions: "PASS: the evidence in the text" or "N/A: why it can't apply";
             "FAIL" blocks.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

SCHEMA = 'SENSE_RECEIPT_V1'
QUESTIONS = {
    'Q1': 'Why am I reading this sentence, and do I know it before I have to work through it? (the point first; a study '
          'after the question it answers)',
    'Q2': 'What is each instruction for, said in the reader\'s terms, and is it something the helper does ("have someone '
          'go with them"), not a rule stated as a fact ("someone goes with them")?',
    'Q3': 'Which thing exactly? (pools of water, not water; any substance, not anything)',
    'Q4': 'What does each word act on, or mean here? (adjunct remedy; known-genuine)',
    'Q5': 'Why does each sentence follow from the one before? (every but, so, because and this has what it turns on)',
    'Q6': 'Is this the order the reader is thinking in, and does each idea sit next to what it continues?',
    'Q7': 'Does each fact help this reader now, in their case (the same kind of thing they face, not just the same topic)?',
    'Q8': 'Does each item belong in the group it is put in?',
    'Q9': 'Is anything compressed? (one step a sentence, the small words that carry the relation, no space before mg)',
}
NO_PAYOFF = re.compile(r'^\s*(none|nothing|no payoff|n/?a|-+|\?|tbd|todo)\b', re.I)


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


ABBREV = {'dr', 'mr', 'mrs', 'ms', 'st', 'vs', 'etc', 'e.g', 'i.e', 'cf', 'al', 'approx', 'no', 'fig'}


def sentences(text):
    """The text's sentences, in order: a break after . ! ? (and any closing quote or bracket) before a space and a
    capital, a digit or an opening quote, but not after an abbreviation such as "Dr." or "e.g."; and at line breaks.
    Exact and repeatable, so a receipt's sentences can be compared with the text's."""
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        start = 0
        for m in re.finditer(r'[.!?]["”’)\]]*(\s+)(?=["“‘(\[]?[A-Z0-9])', line):
            word = re.search(r'([\w.]+)$', line[start:m.start() + 1])
            if word and line[m.start()] == '.' and word.group(1).rstrip('.').lower() in ABBREV:
                continue
            out.append(line[start:m.start(1)].strip())
            start = m.end(1)
        rest = line[start:].strip()
        if rest:
            out.append(rest)
    return [x for x in out if x]


def make(text, section='', reader='', his_text=''):
    his = his_text or ''
    return {
        'schema': SCHEMA,
        'text_sha256': sha256(text),
        'text': text,
        'section': section,
        'reader': reader,
        'sentences': [dict({'s': s}, **({'his': True} if his and s in his else {'payoff': '', 'follows': ''}))
                      for s in sentences(text)],
        'checked': [],
        'placement': '',
        'questions': {q: '' for q in QUESTIONS},
        'question_text': QUESTIONS,
    }


def check(text, receipt):
    """Problems with RECEIPT for TEXT: [message]. Empty means it passes."""
    p = []
    if receipt.get('schema') != SCHEMA:
        p.append('not a %s receipt' % SCHEMA)
    if receipt.get('text_sha256') != sha256(text):
        p.append('the receipt is for another text (its SHA-256 %s, this text\'s %s): a changed text needs its read again'
                 % ((receipt.get('text_sha256') or '?')[:12], sha256(text)[:12]))
    if len((receipt.get('reader') or '').strip()) < 40:
        p.append('reader: say who reads this section and what exactly they face (the case, not the topic), in a sentence')
    want = sentences(text)
    got = [x.get('s', '') for x in receipt.get('sentences', [])]
    if got != want:
        missing = [s for s in want if s not in got]
        extra = [s for s in got if s not in want]
        p.append('sentences: the receipt must list the text\'s sentences in order (make writes them)%s%s' % (
            '; missing: ' + ' | '.join(m[:60] for m in missing[:3]) if missing else '',
            '; not in the text: ' + ' | '.join(e[:60] for e in extra[:3]) if extra else ''))
    mine = 0
    for x in receipt.get('sentences', []):
        if x.get('his'):
            continue
        mine += 1
        s = x.get('s', '')[:60]
        pay = (x.get('payoff') or '').strip()
        if len(pay) < 12 or NO_PAYOFF.match(pay):
            p.append('payoff missing for "%s": what does this reader do or understand differently because of it? If '
                     'nothing, it goes (Joel, 2026-11-05: "there\'s NO PAYOFF")' % s)
        if len((x.get('follows') or '').strip()) < 8:
            p.append('follows missing for "%s": why does it come after the sentence before?' % s)
    for c in receipt.get('checked', []):
        for k in ('point', 'found', 'still_needed', 'fate'):
            if not (c.get(k) or '').strip():
                p.append('checked: "%s" has no %s' % ((c.get('point') or '?')[:50], k))
        if (c.get('still_needed') or '').strip().lower().startswith('no') and c.get('fate') != 'cut':
            p.append('checked: "%s" lost its reason for being here when it was checked, so it goes (fate "cut"); '
                     'a corrected point with no payoff still wastes the reader\'s time (the 7-OH-CBD case, E362)'
                     % (c.get('point') or '?')[:50])
        if c.get('fate') not in (None, '', 'kept', 'changed', 'cut'):
            p.append('checked: fate must be "kept", "changed" or "cut"')
    if mine and len((receipt.get('placement') or '').strip()) < 20:
        p.append('placement: say where the paragraph sits and why there, and what its first "also", "this" or "as for" '
                 'points to')
    qs = receipt.get('questions') or {}
    for q in QUESTIONS:
        a = (qs.get(q) or '').strip()
        if a.upper().startswith('FAIL'):
            p.append('%s fails: %s' % (q, a[:120]))
        elif not (a.upper().startswith('PASS') and len(a) > 10) and not (a.upper().startswith('N/A') and len(a) > 10):
            p.append('%s: answer "PASS: the evidence" or "N/A: why", for: %s' % (q, QUESTIONS[q]))
    return p


def check_files(text_path, receipt_path):
    text = pathlib.Path(text_path).read_text(encoding='utf-8').rstrip('\n')
    receipt = json.loads(pathlib.Path(receipt_path).read_text(encoding='utf-8'))
    return check(text, receipt)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('text')
    m.add_argument('--section', default='')
    m.add_argument('--reader', default='')
    m.add_argument('--his', help='a file of Joel\'s own text: its sentences in TEXT are marked his')
    m.add_argument('--out', required=True)
    c = sub.add_parser('check')
    c.add_argument('text')
    c.add_argument('receipt')
    a = ap.parse_args(argv)
    if a.cmd == 'make':
        text = pathlib.Path(a.text).read_text(encoding='utf-8').rstrip('\n')
        his = pathlib.Path(a.his).read_text(encoding='utf-8') if a.his else ''
        pathlib.Path(a.out).write_text(json.dumps(make(text, a.section, a.reader, his), ensure_ascii=False, indent=1)
                                       + '\n', encoding='utf-8')
        print('receipt to fill: %s (%d sentences)' % (a.out, len(sentences(text))))
        return 0
    probs = check_files(a.text, a.receipt)
    if probs:
        print('FAIL\n  ' + '\n  '.join(probs))
        return 1
    print('PASS: the making-sense receipt covers every sentence of this text')
    return 0


if __name__ == '__main__':
    sys.exit(main())
