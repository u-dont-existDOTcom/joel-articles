#!/usr/bin/env python3
"""fill_h75.py - the making-sense receipts of turn 67's texts of mine in MDMA: Magnesium Alarm: B115 with his round-56
answer on why magnesium chloride (the source out, his claim said as what he knows works best), and the kidney paragraph
(B120). The three fresh reads are turn 66's, on the whole section (../h74-20261124/reads/*-a1-sec.txt): B115 changes one
clause from the text they read, to his own words; B120's tries answer their marks and the tell panel's (panel-b120/).

  python3 fill_h75.py a1-b115 [a1-b120 ...]
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H74 = HERE.parent / 'h74-20261124'
REPO = HERE.parents[3]
sys.path.insert(0, str(H74))
import make_reads as M  # noqa: E402

SECTION = 'MDMA: Magnesium Alarm'
READER = ('a friend at a festival with someone who took MDMA a few hours ago, whose jaw has started to clench and grind, '
          'with magnesium chloride flakes in their bag, reading what to do')
POST = 'his post as of 2026-11-03 (original.md), the paragraph as it stood in the guide before this turn'
CFG = {
    'b115': dict(place='the second paragraph of MDMA: Magnesium Alarm (B115), after his paragraph on what the jaw tension means',
                 why='it tells the friend how much magnesium chloride the writer takes, how much his gut tolerates, and why that kind'),
    'b120': dict(place='the last paragraph of MDMA: Magnesium Alarm (B120), after the dance paragraph and before Chest Pain and Injury',
                 why='it tells the friend what changes when someone has impaired kidneys'),
}
PAY = {
    "A token dose may not be enough": ('they know a little magnesium may not release the jaw', 'his jaw-release claim just made', 'A token dose'),
    "More than once, I've dissolved": ('they know how much magnesium chloride the writer takes, and how', 'the token dose just named', 'More than once'),
    "Around twenty grams is fine for my gut": ('they know how much the writer takes before diarrhea', 'the dose just named', 'Around twenty grams'),
    "And magnesium chloride is": ('they know this kind is gentler on the gut than others', 'his diarrhea, just named', 'And'),
    "I use it mostly because": ('they know why the writer uses this kind, as what he knows works best, and how soon to expect it to help', 'magnesium chloride, just named', 'I use it mostly because'),
    # the kidney paragraph, try a1 (small fixes from his post's text) and try w1 (the second writer's, from the tell panel)
    "**People with impaired kidneys do need": ('they know magnesium needs more care when the kidneys are impaired, and why', 'the section\'s magnesium doses', 'none: his bold lead opens a new case, the people whose kidneys are impaired, after the dance paragraph'),
    "But they should be far more worried": ('they know the MDMA is the bigger danger to those kidneys, and what it can cause', 'the magnesium caution just given', 'But they'),
    "That makes kidney impairment": ('they know impaired kidneys are a reason not to take MDMA, and that worsening jaw tension still gets treated once it is taken', 'what MDMA can cause, just listed', 'That makes kidney impairment'),
    "I just wouldn't tell somebody": ('they know the writer\'s one-gram-per-minute amounts are not for serious kidney impairment as they stand, and that help comes sooner', 'the jaw tension that still gets treated, just said', 'I just wouldn\'t'),
    "**Someone with impaired kidneys does need": ('they know magnesium needs more care when the kidneys are impaired, and why', 'the section\'s magnesium doses', 'none: the bold lead opens a new case, someone whose kidneys are impaired, after the dance paragraph'),
    "But the MDMA should worry them": ('they know the MDMA is the bigger danger', 'the magnesium caution just given', 'But the MDMA'),
    "It can cause overheating and rhabdomyolysis": ('they know what the MDMA can cause', 'the MDMA, just named', 'It can cause'),
    "Kidney impairment is a strong reason to skip": ('they know impaired kidneys are a reason not to take MDMA', 'what MDMA can cause, just listed', 'Kidney impairment'),
    "Once someone has taken it and their jaw tension": ('they know worsening jaw tension still gets treated once the MDMA is taken', 'not taking MDMA, just said', 'Once someone has taken it'),
    "Someone with serious kidney impairment should not": ('they know the writer\'s one-gram-per-minute amounts are not for serious kidney impairment as they stand', 'the jaw tension that still gets treated, just said', 'Someone with serious kidney impairment'),
    "Treat the situation as higher-risk": ('they know to get help sooner in that case', 'serious kidney impairment, just named', 'Treat the situation'),
}
SRC = {
    'b115': [{'point': 'why magnesium chloride: it is what he knows works best; it absorbs faster and better than any other form, and you can see it helping usually within a minute',
              'found': ('his TEACH-JAW comment of round 55 ("it absorbs faster and better than any other form, so you can see how it\'s '
                        'helping usually within a minute") and his CHLORIDE-CLAIM answer of round 56 (2026-11-24 21:26 UTC): "remove the '
                        'source then if there\'s no source, but i definitely can\'t recommend using anything other than what i know works '
                        'best". Round 56\'s card had told him what the study shows (Firoz and Graber 2001: oxide poorly absorbed; chloride, '
                        'lactate and aspartate about equal) and that no study compares speed; the claim stays as his, said as what he knows, '
                        'and the link is out, as he said'),
              'still_needed': 'yes: they know why this kind, and when to expect it to start working', 'fate': 'changed'},
             {'point': 'his amounts and his gut: about one gram per minute by mouth for around twenty minutes; twenty grams without diarrhea, diarrhea only above about forty',
              'found': POST + '; facts.py holds each',
              'still_needed': 'yes: they know a token dose may not release the jaw, and what the writer takes', 'fate': 'kept'}],
    'b120': [{'point': 'people with impaired kidneys need to be more cautious with large, rapid magnesium doses, since they may not clear magnesium normally, and should be far more worried about the MDMA',
              'found': POST + ' (his bold lead); fidelity key W027 and facts.py hold its words',
              'still_needed': 'yes: they know magnesium needs more care with impaired kidneys, and that the MDMA is the bigger danger', 'fate': 'kept'},
             {'point': 'MDMA can cause overheating, rhabdomyolysis, dangerous electrolyte shifts and acute kidney injury',
              'found': POST + ', with its link to the acute kidney injury study (PubMed 27917269); fidelity key W028 and facts.py hold each term',
              'still_needed': 'yes: they know why the MDMA is the bigger danger to someone whose kidneys are impaired', 'fate': 'changed'},
             {'point': 'kidney impairment is a strong reason not to take MDMA, and after taking it no reason to sit there with worsening jaw tension',
              'found': POST + ', where it is one sentence with a dash aside ("--not a reason to sit there ...")',
              'still_needed': 'yes: they know not to leave worsening jaw tension alone because of the kidneys', 'fate': 'changed'},
             {'point': 'with serious kidney impairment he would not have them copy his one-gram-per-minute approach blindly: the situation is higher-risk and help comes sooner',
              'found': POST + ', where it is a mirrored pair ("I would not tell ...; I would tell them ..."); fidelity key W029 holds one-gram-per-minute and higher-risk',
              'still_needed': 'yes: they know his amounts are not for serious kidney impairment as they stand, and to get help sooner', 'fate': 'changed'}],
}
# what a fresh reader marked in a sentence the kidney paragraph keeps, and why it stays
KEPT = {'b120': {'his': 'kept: his bold lead, word for word from his post; it names who the paragraph is for, and the amount it means comes with his one-gram-per-minute approach in the last sentence',
                 'fit': 'kept: his sentence; whether someone\'s kidneys are impaired is theirs to know and say, and the paragraph is for those who do'}}
SAME = {'b120': ('none: read the section from its heading to the next; the caution for impaired kidneys is said only here, and '
                 'overheating and the electrolytes are named here for what the MDMA does to those kidneys')}
QB = {'b120': ('PASS: read against turn 66\'s three fresh reads of this paragraph (humanize/h74-20261124/reads) and the tell panel on '
               'his post\'s text (panel-b120/PANEL.md); the try answers their marks and adds no dose, reason or advice')}
Q = {q: 'PASS: as turn 66 read it (humanize/h74-20261124), one clause changed to his own words' for q in
     ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9')}


def first(s):
    for k in PAY:
        if s.startswith(k):
            return k
    return None


def marks(rs):
    his, fit = [], []
    for line in (H74 / 'reads' / 'his-a1-sec.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+)(?:-S?(\d+))?[^:]*:\s*([\d, ]+)\s*[—-]', line)
        if m:
            for n in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
                if n - 1 < len(rs):
                    his.append({'s': rs[n - 1], 'difference': m.group(3).strip()})
    for line in (H74 / 'reads' / 'fit-a1-sec.txt').read_text(encoding='utf-8').splitlines():
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
    d['same_point'] = SAME.get(block) or ('none: read the section from its heading to the next; why magnesium chloride is said once, here, with '
                       'the amounts; overheating and the electrolytes are said in his paragraph on what to do and in the '
                       'kidney paragraph, each for its own reader')
    rs = M.sentences((H74 / 'TEST-a1-sec.txt').read_text(encoding='utf-8').strip())
    his, fit = marks(rs)
    now = [s['s'] for s in d['sentences']]

    def kept_for(lst, who=None):
        if block in KEPT:
            return {x: KEPT[block][who] for x in lst}
        return {x: 'kept: it read High in its window last turn, and the words carry a dose or an event of his post that stays' for x in lst}
    d['needed'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md '
                              '(../h74-20261124/reads/need-a1-sec.txt), on turn 66\'s version one of the whole section'), 'unneeded': [], 'kept': {}}
    hm = [m for m in his if m['s'] in now]
    fm = [m for m in fit if m['s'] in now]
    d['his_fixes'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md '
                                 '(../h74-20261124/reads/his-a1-sec.txt), on turn 66\'s version one of the whole section'),
                      'marked': hm, 'kept': kept_for([m['s'] for m in hm], 'his')}
    d['fit'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md '
                           '(../h74-20261124/reads/fit-a1-sec.txt), on turn 66\'s version one of the whole section'),
                'marked': fm, 'kept': kept_for([m['s'] for m in fm], 'fit')}
    d['questions'] = {q: QB[block] for q in Q} if block in QB else Q
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1800:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in sys.argv[1:]))
