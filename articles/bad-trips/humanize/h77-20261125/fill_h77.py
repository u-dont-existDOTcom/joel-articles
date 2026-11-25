#!/usr/bin/env python3
"""fill_h77.py - the making-sense receipts of turn 69's texts of mine (the method and the fields are fill_h76.py's):

- b2-b128: his round-58 poison control paragraph with one clause of his replaced by two sentences of mine, offered to him
  on round 59's card (his own paragraph is what is in the guide);
- a2-b139-open: the first three paragraphs of My Acute Rescue Remedies with three words changed in the one sentence that
  read Human Low (the near miss's small fix, lesson bad-trips-2026-11-19b);
- a1-b141: the gut-driven paragraph of the same section, one try from his post's text.

  python3 fill_h77.py b2-b128 a2-b139-open a1-b141
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
POST = 'his post as of 2026-11-03 (original.md), the paragraph as it stood in the guide before this turn'
HIS58 = 'his round-58 answer (review/r58/ANSWERS-R58-20261125-1742.json, CHARCOAL-HOUR)'
CFG = {
    'b128': dict(
        section='Swallowed Too Much?',
        reader=('the friend of someone who swallowed too much of a plant medicine a few hours ago, with activated charcoal in '
                'their bag and a phone, deciding what to do next'),
        place='the last paragraph of Swallowed Too Much? (B128), after his charcoal paragraph and before Serotonin Syndrome (SS)?',
        why='it tells the friend what AI and Poison Control are good for here, and what not to ask them',
        same='none: read the section from its heading to the next; who to ask, and about what, is said only here',
        readkey='b1-swallowed-sec', draft='TEST-b1-b128.txt in TEST-b1-swallowed-sec.txt',
        note=('the three fresh reads of my first draft of the new sentence (reads/*-b1-swallowed-sec.txt) marked it for four '
              'ideas in one sentence, for "them" and "they" that could be AI, Poison Control or the person, and for saying the '
              'limit twice; the checked text names Poison Control, is two sentences, and says the limit once, with the link on it. '
              'The other three sentences are his, word for word')),
    'b139': dict(
        section='My Acute Rescue Remedies',
        reader=('somebody sitting with a friend on a psychedelic who has diarrhea and nausea and says their mind is going crazy, '
                'deciding whether to talk them through it or to treat it'),
        place='the first three paragraphs of My Acute Rescue Remedies (B139, his answer N-AN-Q1, B86), before B87',
        why='it tells the reader what the remedies that follow are for, and that a body feeling awful gets read as a spiritual crisis',
        same=('none new: read the section from its heading to the next. B87 after it says what the body may need; this says what '
              'gets misread. Only three words of one sentence change'),
        readkey='asis-rescue-sec', draft='the text as it stands, TEST-asis-rescue-sec.txt',
        note=('the three fresh reads of the section as it stands (reads/*-asis-rescue-sec.txt) marked most of its sentences, but '
              'by themselves these three paragraphs read Human High 56 and Human Low 14 (d9dea7a8): only the list sentence fell '
              'short, so only it changes, by three words, as a near miss is fixed (lesson bad-trips-2026-11-19b). The read against '
              'his fixes called "become spiritual content" a label for what happens; the sentence before says who does it (the '
              'altered mind), so the things "get read as" it. Every other sentence stays as it reads High')),
    'b141': dict(
        section='My Acute Rescue Remedies',
        reader=('somebody sitting with a friend on a psychedelic who has diarrhea and nausea and says their mind is going crazy, '
                'deciding whether to talk them through it or to treat it'),
        place='the last paragraph of the opening of My Acute Rescue Remedies (B141), before the list of remedies',
        why='it tells the reader which trips the remedies below are for, as against a mainly emotional crisis',
        same=('none: read the section from its heading to the next; B86 says the body gets read as a spiritual crisis, and this '
              'says which signs point to the gut or the brain and which part of the guide to use'),
        readkey='a1-rescue-sec', draft='TEST-a1-b141.txt in TEST-a1-rescue-sec.txt',
        note=None),   # set below, once the reads of the first draft are in
}
PAY = {
    "If you're unsure about the interactions": ('they know what to ask AI and Poison Control: how the drugs taken interact', 'his charcoal paragraph before it', None),
    'They might have important info': ('they know the call is most useful when the drugs are well-known', 'AI and Poison Control, just named', 'They might'),
    'They can also help you': ('they know Poison Control can also talk them through standard first aid', 'what they might know, just said', 'They can also'),
    "But I wouldn't ask Poison Control": ('they know not to ask Poison Control whether to give charcoal', 'what Poison Control is good for, just said', "But I wouldn't ask Poison Control"),
    'Someone I know did': ('they know what happens if they ask: they are told Poison Control cannot say to take it, and are left confused', 'asking about charcoal, just said', 'Someone I know did'),
    'This hierarchy is for acute': ('they know the remedies are for acute trouble, emergencies included', 'the section\'s heading', None),
    "In general it's good to try": ('they know to try each remedy in small, rising amounts before a crisis', 'the remedies the heading names', 'none: his answer N-AN-Q1, word for word; a new step, how to get ready'),
    "Sometimes the mind isn't": ('they know a crisis is not always about the mind', 'the acute situations just named', 'the mind'),
    'The body feels awful': ('they know the altered mind explains a body that feels awful as cosmic horror', 'the mind, just named', 'The body'),
    'Nausea, heat, exhaustion': ('they know which body states get read as spiritual', 'the body feeling awful, just said', 'Nausea'),
}
SRC = {
    'b128': [
        {'point': 'AI and Poison Control are worth checking with about the interactions between the drugs taken, most when the drugs are well-known, and can give standard first aid instructions',
         'found': HIS58 + ': his three sentences, kept word for word',
         'still_needed': 'yes: they know who to ask about the mix, and for first aid', 'fate': 'kept'},
        {'point': 'Poison Control often can\'t give actionable advice, for liability reasons',
         'found': (HIS58 + ': "i know someone who did, and poison control said they aren\'t allowed to tell them to take charcoal, so it left '
                   'them very confused". That is one case, about charcoal, and his next sentence says they do give first aid instructions. '
                   'Poison Control\'s own page (the National Capital Poison Center, https://www.poison.org/articles/2017-jun/activated-charcoal, '
                   'read 2026-11-25): "It is not recommended to use these products at home to treat a poisoning". So the two sentences say '
                   'what happened and nothing wider; "for liability reasons" is his reading of why, and is not in them'),
         'still_needed': 'yes: they know not to ask Poison Control about charcoal, and what they will hear if they do', 'fate': 'changed'},
    ],
    'b139': [
        {'point': 'nausea, heat, exhaustion, dehydration, overstimulation and sleep loss all become spiritual content very quickly',
         'found': POST + '; all six stay; "become" is "get read as", after the sentence that says the altered mind does the reading',
         'still_needed': 'yes: they check the body before they take a horrible thought as a message', 'fate': 'changed'},
        {'point': 'the hierarchy is for acute situations; try the remedies in very low, increasing doses beforehand (his answer); a body that feels awful is explained by the altered mind as cosmic horror',
         'found': POST + ' and his answer N-AN-Q1; unchanged, Human High 56 by themselves (d9dea7a8)',
         'still_needed': 'yes: they know what the list is for and how to get ready for it', 'fate': 'kept'},
    ],
    'b141': [],   # set below
}
UNNEEDED = {'b128': {}, 'b139': {}, 'b141': {}}
try:   # the gut-driven paragraph's own sentences, sources and kept marks, written after its first draft was read
    from fill_h77_b141 import PAY141, SRC141, NOTE141, UNNEEDED141
    PAY.update(PAY141); SRC['b141'] = SRC141; CFG['b141']['note'] = NOTE141; UNNEEDED['b141'] = UNNEEDED141
except ImportError:
    pass


def first(s):
    for k in PAY:
        if s.startswith(k):
            return k
    return None


def fill(key):
    block = key.split('-')[1]
    c = CFG[block]
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
                        '--section', c['section'], '--reader', c['reader']], capture_output=True, text=True)
    if r.returncode:
        print(key, 'make:', (r.stdout + r.stderr)[-600:]); return 1
    d = json.loads(out.read_text(encoding='utf-8'))
    for s in d['sentences']:
        k = first(s['s'])
        if not k:
            print(key, 'no PAY for:', s['s'][:80]); return 1
        pay, fol, link = PAY[k]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link
    d['checked'] = SRC[block]
    d['placement'] = c['place']
    d['opens']['why_reading'] = c['why']
    d['same_point'] = c['same']
    who = 'a fresh agent (Sonnet) given tools/humanization/%s (reads/%s-' + c['readkey'] + '.txt), on ' + c['draft'] + '; the checked text answers its marks'
    d['needed'] = {'reader': who % ('needed_read_brief.md', 'need'), 'unneeded': list(UNNEEDED[block]), 'kept': UNNEEDED[block]}
    d['his_fixes'] = {'reader': who % ('his_fixes_brief.md', 'his'), 'marked': [], 'kept': {}}
    d['fit'] = {'reader': who % ('fit_read_brief.md', 'fit'), 'marked': [], 'kept': {}}
    q = 'PASS: ' + c['note']
    d['questions'] = {k: q for k in d['questions']}
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1500:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.path.insert(0, str(HERE))
    sys.exit(max(fill(k) for k in sys.argv[1:]))
