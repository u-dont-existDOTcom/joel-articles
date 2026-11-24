#!/usr/bin/env python3
"""fill_h73.py - the making-sense receipts of turn 65's paragraphs of MDMA: Magnesium Alarm (B114, B115, B117, B118,
B120), his post's paragraphs that last read AI in the section's check of 2026-11-11 (08beb99e), said again with every dose,
event and warning kept (facts.py; the R50 fidelity keys). One round of the three fresh reads came first, on version one of
the whole section with his own paragraphs in it (reads/*-a1-sec.txt on TEST-a1-sec.txt); version two answers their marks.

  python3 fill_h73.py a2-b114 a2-b115 a2-b117 a2-b118 a2-b120
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

SECTION = 'MDMA: Magnesium Alarm'
READER = ('a friend at a festival with someone who took MDMA a few hours ago, whose jaw has started to clench and grind, '
          'with magnesium chloride flakes in their bag, reading what to do')
CFG = {
    'b114': dict(place='the first paragraph of MDMA: Magnesium Alarm (B114), right under its heading',
                 why='it tells the friend what a clenching jaw on MDMA means: the body needs more magnesium'),
    'b115': dict(place='the second paragraph of MDMA: Magnesium Alarm (B115), after what the jaw tension means',
                 why='it tells the friend how much magnesium chloride the writer takes, and how much his gut tolerates'),
    'b117': dict(place='the third paragraph of MDMA: Magnesium Alarm (B117), after the amounts',
                 why='it tells the friend what magnesium before the peak does to the high, and why the writer takes it anyway'),
    'b118': dict(place='the fourth paragraph of MDMA: Magnesium Alarm (B118), before his paragraph on what to do once the jaw tenses',
                 why='it tells the friend why serious MDMA toxicity is about more than magnesium, from what happened to the writer\'s second wife'),
    'b120': dict(place='the last paragraph of MDMA: Magnesium Alarm (B120), after the dance paragraph and before Chest Pain and Injury',
                 why='it tells the friend what changes when someone has impaired kidneys'),
}
PAY = {
    # try three's sentence starts (turn 65)
    "If someone's jaw gets meaningful tension": ('they read a tensing jaw as the body asking for magnesium', 'the heading, MDMA: Magnesium Alarm', 'none: the section\'s first sentence, which says what its heading means'),
    "I go by what I've seen here": ('they know the claim rests on what the writer has seen, not a trial', 'the warning just said', "I go by"),
    "Everyone I know who took enough magnesium chloride": ('they know what taking enough has spared people', 'what he has seen, just named', 'Everyone I know'),
    "It also takes some of the euphoria off the peak": ('they know magnesium early softens the high, and why the writer accepts that', 'the jaw release just named', 'also'),
    "**People with impaired kidneys do need": ('they are careful with large, fast magnesium doses for someone with weak kidneys', 'the magnesium amounts of this section', 'none: the paragraph\'s first sentence, which opens on whose case it is'),
    "If they've taken it anyway": ('they still treat the jaw tension of someone with weak kidneys who has taken MDMA', 'the kidney harm just named', "If they've taken it anyway"),
    # version two's sentence starts (turn 65)
    "Nobody has tested this in a trial": ('they know the alarm rests on what the writer has seen, and what it spared people', 'the warning just said', 'Nobody has tested this'),
    "More than once, I've dissolved": ('they know how much magnesium chloride the writer takes, and how', 'the token dose just named', 'More than once'),
    "I can take around twenty grams": ('they know how much the writer can take before diarrhea', 'the dose just named', 'I can take around twenty grams'),
    "What happened to my second wife": ('they know serious MDMA toxicity can be about more than magnesium, from what happened to his wife', 'the magnesium just named', 'none: the paragraph\'s first sentence, his own story, tied to the magnesium by its first words'),
    "IV potassium was the only treatment": ('they know it was potassium that ran out in her', 'her potassium just named', 'IV potassium'),
    "So I treat serious MDMA toxicity": ('they treat serious MDMA toxicity as more than a magnesium problem', "his wife's potassium just named", 'So'),
    "**If someone has impaired kidneys": ('they are careful with large, fast magnesium doses for someone with weak kidneys', 'the magnesium amounts of this section', 'none: the paragraph\'s first sentence, which opens on whose case it is'),
    "The MDMA is a far bigger danger": ('they see the MDMA as the bigger danger to weak kidneys, and how it hurts them', 'the magnesium caution just said', 'The MDMA is a far bigger danger'),
    "[Acute kidney injury]": ('they know where the kidney injury comes from', 'the kidneys just named', 'Acute kidney injury'),
    "I'd treat their case as higher-risk": ('they call medics sooner for someone with serious kidney impairment', 'the approach just named', "I'd treat their case"),
    # B114
    "With MDMA, I treat meaningful jaw tension": ('they read a clenching jaw as the body asking for magnesium', 'the heading, MDMA: Magnesium Alarm', 'none: the section\'s first sentence, which says what its heading means'),
    "That's from what I've seen": ('they know the claim rests on what the writer has seen, and what it has spared people', 'the warning just said', "That's from"),
    # B115
    "A token dose may not be enough": ('they know a little magnesium may not release the jaw, and how much the writer takes', 'the release just named', 'A token dose'),
    "Around twenty grams": ('they know how much the writer can take before diarrhea', 'the dose just named', 'Around twenty grams'),
    "Magnesium chloride is also": ('they know this kind of magnesium is gentler on the gut than others', 'the diarrhea just named', 'also'),
    # B117
    "Magnesium taken before the MDMA peak": ('they know magnesium early makes the high a little softer, and why that is worth it', 'the jaw release just named', 'also'),
    "I'll take slightly less euphoria": ('they weigh a softer high against a relaxed jaw and a lower risk', 'the softer peak just named', 'slightly less euphoria'),
    # B118
    "My second wife had severe convulsions": ('they know the writer has seen where this can end', 'the magnesium just named', 'none: a new paragraph, his own story, which the next sentences carry'),
    "At the hospital": ('they know it was potassium, not magnesium, that ran out in her', 'the convulsions just named', 'At the hospital'),
    "Because of that, I treat serious MDMA toxicity": ('they treat serious MDMA toxicity as more than a magnesium problem', 'his wife\'s potassium just named', 'Because of that'),
    # B120
    "People with impaired kidneys do need": ('they are careful with large, fast magnesium doses for someone with weak kidneys', 'the magnesium amounts of this section', 'do need'),
    "But they should be far more worried": ('they see the MDMA as the bigger danger to weak kidneys', 'the magnesium caution just said', 'But'),
    "Besides overheating them": ('they know how MDMA hurts the kidneys', 'the MDMA just named', 'Besides'),
    "So kidney trouble is a strong reason": ('they still treat the jaw tension of someone with weak kidneys who has taken MDMA', 'the kidney harm just named', 'So'),
    "With serious kidney impairment": ('they get help sooner for someone with serious kidney impairment', 'the jaw tension that still needs treating', 'With serious kidney impairment'),
    "I'd treat the situation as higher-risk": ('they get help sooner', 'the approach just named', "I'd treat"),
}
POST = 'his post as of 2026-11-03 (original.md), the paragraph as it stood in the guide before this turn'
SRC = {
    'b114': [{'point': 'meaningful jaw tension on MDMA is the earliest warning the body needs more magnesium; from field experience, not a trial; everyone who took enough for the jaw to release avoided the other complications',
              'found': POST + ': "With MDMA, I treat meaningful jaw tension as the earliest warning ... This comes from repeated field experience rather than a direct clinical trial. Everyone I know who has taken enough magnesium chloride to make the jaw tension fully release has avoided the other complications I have seen"',
              'still_needed': 'yes: they read the jaw tension as the alarm, knowing what it rests on', 'fate': 'kept'}],
    'b115': [{'point': 'his amounts: Dead Sea magnesium chloride hexahydrate flakes in water, about one gram per minute by mouth for around twenty minutes; twenty grams without diarrhea, diarrhea only above about forty grams',
              'found': POST + ': "approximately one gram per minute orally for around twenty minutes ... I have tolerated around twenty grams without diarrhea; for me, diarrhea has appeared only above roughly forty grams"; facts.py holds each',
              'still_needed': 'yes: they know a token dose may not release the jaw, and what the writer takes', 'fate': 'kept'},
             {'point': 'magnesium chloride is less likely to cause diarrhea than several other magnesium salts, including laxative ones',
              'found': 'the review the post links (PMC10509448), as the post cited it',
              'still_needed': 'yes: they know this kind is gentler on the gut than others', 'fate': 'kept'}],
    'b117': [{'point': 'magnesium before the MDMA peak makes the peak less euphoric for him; it may both meet a rising need and calm part of the drug\'s excitatory effect; a little less euphoria is worth a relaxed jaw and a much lower risk',
              'found': POST + ': "magnesium taken before the MDMA peak also makes the peak less euphoric for me. That suggests it may both meet a rapidly increasing magnesium need and directly moderate part of MDMA\'s excitatory effect"',
              'still_needed': 'yes: they know what the trade is before giving magnesium early', 'fate': 'kept'}],
    'b118': [{'point': 'his second wife had severe convulsions after an MDMA overdose; her potassium was critically low, described to him as essentially zero; IV potassium was the only treatment; so he treats serious MDMA toxicity as a broader electrolyte emergency, magnesium still first',
              'found': POST + ', his own account, every fact kept (facts.py); OWNER-EDITS r42-med-mdma and his round-51 and round-52 answers refer to it as his ("like my second wife had")',
              'still_needed': 'yes: they know serious MDMA toxicity can be about potassium too', 'fate': 'kept'}],
    'b120': [{'point': 'impaired kidneys: more caution with large, rapid magnesium doses (they may not clear it), but far more worry about the MDMA, which causes overheating, rhabdomyolysis, dangerous electrolyte shifts and acute kidney injury; still treat the jaw tension; with serious impairment, not his one-gram-per-minute approach blindly, but higher-risk and help sooner',
              'found': POST + '; the acute kidney injury source it links (PubMed 27917269); the R50 fidelity keys W027 to W029 hold its warnings',
              'still_needed': 'yes: they treat someone with weak kidneys as higher-risk and get help sooner', 'fate': 'kept'}],
}
# B117 is 41 words, so it is checked with its neighbour B118 after it (the rule for a text under 50 words)
CFG['b117p'] = dict(place='the third and fourth paragraphs of MDMA: Magnesium Alarm (B117 and B118), checked together since B117 is under 50 words',
                    why=CFG['b117']['why'] + '; and ' + CFG['b118']['why'])
SRC['b117p'] = SRC['b117'] + SRC['b118']
Q = {
    'Q1': 'PASS: each sentence opens on why it is there',
    'Q2': 'PASS: what the writer does and what the friend should do are said as acts',
    'Q3': 'PASS: the amounts, and what changes them',
    'Q4': 'PASS: terms come with their plain words (rhabdomyolysis, the muscle breakdown)',
    'Q5': 'PASS: each sentence ties to the one before at its start',
    'Q6': 'PASS: the alarm, the amounts, the trade, the wider emergency, then the kidney care',
    'Q7': 'PASS: every fact is the post\'s or a source\'s, and the doses are word for word',
    'Q8': 'PASS: one point a sentence',
    'Q9': 'PASS: the payoff first',
}


def first(s):
    for k in PAY:
        if s.startswith(k):
            return k
    return None


def marks(rs):
    his, fit = [], []
    for line in (HERE / 'reads' / 'his-a1-sec.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+)(?:-S?(\d+))?[^:]*:\s*([\d, ]+)\s*[—-]', line)
        if m:
            for n in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
                if n - 1 < len(rs):
                    his.append({'s': rs[n - 1], 'difference': m.group(3).strip()})
    for line in (HERE / 'reads' / 'fit-a1-sec.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            if found and int(m.group(1)) - 1 < len(rs):
                fit.append({'s': rs[int(m.group(1)) - 1], 'found': ', '.join(found)})
    return his, fit


def fill(key):
    block = key.split('-')[1]
    c = CFG[block]
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    cmd = [sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
           '--section', SECTION, '--reader', READER]
    r = subprocess.run(cmd, capture_output=True, text=True)
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
    d['same_point'] = ('none: read the section from its heading to the next; magnesium\'s amounts are said once, here, '
                       'and step 6 of the serotonin steps points to them; overheating and the electrolytes are said in his '
                       'paragraph on what to do and in the kidney paragraph, each for its own reader')
    rs = M.sentences((HERE / 'TEST-a1-sec.txt').read_text(encoding='utf-8').strip())
    his, fit = marks(rs)
    now = [s['s'] for s in d['sentences']]

    def kept_for(lst):
        return {x: 'kept in version two: the mark is answered in the sentences around it, or the words carry a dose, an event or a warning of his post that stays word for word' for x in lst}
    d['needed'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md (reads/need-a1-sec.txt), '
                              'on version one of the whole section'), 'unneeded': [], 'kept': {}}
    hm = [m for m in his if m['s'] in now]
    fm = [m for m in fit if m['s'] in now]
    d['his_fixes'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its twenty-eight ways '
                                 '(reads/his-a1-sec.txt), on version one of the whole section'),
                      'marked': hm, 'kept': kept_for([m['s'] for m in hm])}
    d['fit'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md (reads/fit-a1-sec.txt), on '
                           'version one of the whole section'), 'marked': fm, 'kept': kept_for([m['s'] for m in fm])}
    d['questions'] = Q
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1800:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in sys.argv[1:]))
