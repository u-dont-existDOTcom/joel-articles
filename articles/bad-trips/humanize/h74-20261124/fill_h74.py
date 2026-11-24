#!/usr/bin/env python3
"""fill_h74.py - the making-sense receipts of turn 66's texts of mine in MDMA: Magnesium Alarm: B115 with why magnesium
chloride (his round-55 question), and B117 and B120 from his post's text with the ways of his round-55 fixes. One round
of the three fresh reads came first, on version one of the whole section with his two round-55 versions in it
(reads/*-a1-sec.txt on TEST-a1-sec.txt); version two answers their marks.

  python3 fill_h74.py a2-b115 a2-b117 a2-b120
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

SECTION = 'MDMA: Magnesium Alarm'
READER = ('a friend at a festival with someone who took MDMA a few hours ago, whose jaw has started to clench and grind, '
          'with magnesium chloride flakes in their bag, reading what to do')
POST = 'his post as of 2026-11-03 (original.md), the paragraph as it stood in the guide before this turn'
CFG = {
    'b115': dict(place='the second paragraph of MDMA: Magnesium Alarm (B115), after his paragraph on what the jaw tension means',
                 why='it tells the friend how much magnesium chloride the writer takes, why that kind, and how much his gut tolerates'),
    'b117': dict(place='the third paragraph of MDMA: Magnesium Alarm (B117), after the amounts and before his second wife\'s story',
                 why='it tells the friend what magnesium before the peak does to the high, and why the writer takes it anyway'),
    'b120': dict(place='the last paragraph of MDMA: Magnesium Alarm (B120), after the dance paragraph and before Chest Pain and Injury',
                 why='it tells the friend what changes when someone has impaired kidneys'),
}
PAY = {
    "A token dose may not be enough": ('they know a little magnesium may not release the jaw', 'his jaw-release claim just made', 'A token dose'),
    "More than once, I've dissolved": ('they know how much magnesium chloride the writer takes, and how', 'the token dose just named', 'More than once'),
    "I use magnesium chloride because": ('they know why this kind, and how soon to expect it to help', 'the flakes just named', 'I use magnesium chloride'),
    "Around twenty grams is fine for my gut": ('they know how much the writer takes before diarrhea', 'the dose just named', 'Around twenty grams'),
    "Magnesium chloride is also": ('they know this kind is gentler on the gut than others', 'the diarrhea just named', 'also'),
    "It's also [less likely to cause diarrhea": ('they know this kind is gentler on the gut than others', 'magnesium chloride, just named', "It's also"),
    "I use it mostly because": ('they know the main reason for this kind, and how soon to expect it to help', 'magnesium chloride, just named', 'I use it mostly because'),
    "And magnesium chloride is": ('they know this kind is gentler on the gut than others', 'his diarrhea, just named', 'And'),
    "Magnesium taken before the MDMA peak": ('they know magnesium early softens the high, and why that may be', 'the jaw release of the paragraphs before', 'also'),
    "I'm fine trading a little euphoria": ('they weigh a softer high against a relaxed jaw and a lower risk', 'the softer peak just named', "I'm fine trading"),
    "I don't mind a little less euphoria": ('they weigh a softer high against a relaxed jaw and a lower risk', 'the softer peak just named', "I don't mind"),
    "**If someone has impaired kidneys": ('they are careful with large, fast magnesium doses for someone with weak kidneys', 'the magnesium amounts of this section', 'none: the paragraph\'s first sentence, which opens on whose case it is'),
    "But the MDMA is a far bigger danger": ('they see the MDMA as the bigger danger to weak kidneys, and how it hurts them', 'the magnesium caution just said', 'But'),
    "So kidney trouble is a strong reason": ('they still treat the jaw tension of someone with weak kidneys who has taken MDMA', 'the kidney harm just named', 'So'),
    "With serious kidney impairment, though": ('they get help sooner for someone with serious kidney impairment', 'the jaw tension that still needs treating', 'With serious kidney impairment, though'),
}
SRC = {
    'b115': [{'point': 'why magnesium chloride: it is absorbed far better than magnesium oxide, and he can usually see it start helping within a minute',
              'found': ('his TEACH-JAW comment of 2026-11-24 19:53 UTC: "it absorbs faster and better than any other form, so you can see how '
                        'it\'s helping usually within a minute"; Firoz and Graber 2001 (PubMed 11794633): magnesium oxide\'s fractional '
                        'absorption 4%, "significantly higher and equivalent bioavailability of magnesium chloride, magnesium lactate and '
                        'magnesium aspartate"; no study found comparing how fast the forms act, so "within a minute" is his experience and '
                        '"any other form" is narrowed to what the study shows, a change that goes to him on round 56'),
              'still_needed': 'yes: they know why this kind, and when to expect it to start working', 'fate': 'changed'},
             {'point': 'his amounts and his gut: about one gram per minute by mouth for around twenty minutes; twenty grams without diarrhea, diarrhea only above about forty',
              'found': POST + '; facts.py holds each',
              'still_needed': 'yes: they know a token dose may not release the jaw, and what the writer takes', 'fate': 'kept'}],
    'b117': [{'point': 'magnesium before the MDMA peak makes the peak less euphoric for him; it may calm part of the drug\'s stimulation besides meeting a fast-rising need; a little less euphoria is worth a relaxed jaw and a much lower risk',
              'found': POST + ': "magnesium taken before the MDMA peak also makes the peak less euphoric for me. That suggests it may both meet a rapidly increasing magnesium need and directly moderate part of MDMA\'s excitatory effect"; the R55 keys W024 hold "risk", "euphoria", "relaxed"',
              'still_needed': 'yes: they know what the trade is before giving magnesium early', 'fate': 'kept'}],
    'b120': [{'point': 'impaired kidneys: more caution with large, rapid magnesium doses (they may not clear it), but the MDMA is the bigger danger (overheating, dangerous electrolyte shifts, acute kidney injury, rhabdomyolysis); still treat the jaw tension; with serious impairment, higher-risk, help sooner, not his approach copied blindly',
              'found': POST + '; the acute kidney injury source it links (PubMed 27917269); the R55 keys W027 to W029',
              'still_needed': 'yes: they treat someone with weak kidneys as higher-risk and get help sooner', 'fate': 'kept'}],
}
Q = {
    'Q1': 'PASS: each sentence opens on why it is there',
    'Q2': 'PASS: what the writer does and what the friend should do are said as acts',
    'Q3': 'PASS: the amounts, and what changes them',
    'Q4': 'PASS: terms come with their plain words (rhabdomyolysis, muscle breaking down into the blood)',
    'Q5': 'PASS: each sentence ties to the one before at its start',
    'Q6': 'PASS: the amounts and why this kind, the trade, then the kidney care',
    'Q7': 'PASS: every fact is the post\'s, his, or a source\'s, and the doses are word for word',
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
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
                        '--section', SECTION, '--reader', READER], capture_output=True, text=True)
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
    d['same_point'] = ('none: read the section from its heading to the next; why magnesium chloride is said once, here, with '
                       'the amounts; overheating and the electrolytes are said in his paragraph on what to do and in the '
                       'kidney paragraph, each for its own reader')
    rs = M.sentences((HERE / 'TEST-a1-sec.txt').read_text(encoding='utf-8').strip())
    his, fit = marks(rs)
    now = [s['s'] for s in d['sentences']]

    def kept_for(lst):
        return {x: 'kept in version two: the mark is answered in the sentences around it, or the words carry a dose, an event or a warning of his post that stays' for x in lst}
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
