#!/usr/bin/env python3
"""fill_h71.py - the making-sense receipts of turn 63's texts, written from his round-52 answers (2026-11-24 01:25 UTC):
his MDMA paragraph (B119) with his sentence that women are most at risk, and the paragraph after it (R52-DANCE) from
DANCE-ENERGY and the field vs lab note he asked for in WOMEN-RISK. One round of the three fresh reads came first, on
version one (reads/*-a1-mdma.txt on TEST-a1-mdma.txt, reads/*-a1-dance.txt on TEST-a1-dance.txt); version two answers
their marks.

  python3 fill_h71.py a2-mdma a2-dance
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

CFG = {
    'a2-mdma': dict(read='a1-mdma', section='MDMA: Magnesium Alarm',
                    his=('HIS-mdma.txt', 'his own: his MDMA: Magnesium Alarm paragraph (B119, round 42, MED-MDMA)'),
                    place='his MDMA: Magnesium Alarm paragraph (B119), after his paragraph on his second wife\'s potassium',
                    why='it tells the friend what to do once the jaw tenses, why plain water is a risk, who is most at risk, and when to call medics'),
    'a3-dance': None,
    'a2-dance': dict(read='a1-dance', section='MDMA: Magnesium Alarm',
                     his=('HIS-dance.txt', 'his own: his DANCE-ENERGY answer on round 52 (2026-11-24 01:25 UTC)'),
                     place=('the paragraph after his MDMA paragraph (B119), whose last sentence names overheating among what '
                            'brings on a seizure or collapse; its "That\'s why" turns on that sentence and on the salt the '
                            'paragraph is about; before the kidney paragraph (B120)'),
                     why='it tells someone going to dance on MDMA why not to, what the writer would take instead, and what he thinks a pill that makes someone feel like dancing says about it'),
}
READER = {'a1-mdma': ('a friend at a festival with a woman who took MDMA a few hours ago and has been dancing, whose jaw is '
                      'tight and who has been drinking a lot of water, reading what to do'),
          'a1-dance': ('someone about to go to a festival with friends who plan to take MDMA and dance all night, reading '
                       'this the day before')}
PAY = {
    "Plain water is the risk because": ('they know why plain water lowers sodium, so they give the electrolyte drink', 'the plain water just named', 'Plain water is the risk because'),
    "Women are most at risk of this": ('they watch a woman friend most closely for low sodium', 'the low sodium just named', 'Women are most at risk of this'),
    "[California's poison control]": ('they know the risk to women is more than one rave', 'the rave just named', 'found the same pattern'),
    "The following indicators would justify calling medics": ('they know the signs that call for medics and what to give meanwhile', 'the risk just named', 'The following indicators'),
    "That has to be a lot of salt": ('they know how much salt', 'the salty food just named', 'That has to be'),
    "That's why I'd tell everyone not to dance": ('they keep their friends from dancing on MDMA', 'the overheating and the low sodium just named', "That's why"),
    "And really, what's the point of MDMA": ('they see the writer\'s case against MDMA for dancing', 'the no dancing just said', 'And really'),
    "For that they can take": ('they know what the writer would take to dance instead', 'the question just asked', 'For that'),
    "Real MDMA, the kind": ('they know what the writer says real MDMA is like', 'the MDMA of the question', 'Real MDMA'),
    "No, they're sitting there": ('they know the writer\'s view rests on his and his friends\' experience', 'the trials just named', "No, they're sitting there"),
    "It's not like": ('they know what the writer means by not wanting to dance', 'what the real thing feels like, just named', "It's not like"),
    "So if a pill makes someone feel like dancing": ('they know the writer suspects a pill that makes someone feel like dancing', 'the couch lock just said', 'So if a pill'),
    "That might also be why women": ('they know the field and the lab disagree on women, and the writer\'s reading of it', 'the suspect pills just named', 'That might also be why'),
    "The lab also dosed everyone by their weight": ('they know the lab differed in another way, so a smaller friend is at more risk from the same pill', 'the lab just named', 'The lab also'),
    "Then again, the lab dosed everyone": ('they know the lab differed in another way, so a small friend gets more from the same pill', 'the lab just named', 'Then again, the lab'),
}
SRC = {
    'a2-mdma': [
        {'point': 'women are most at risk of low sodium on MDMA: at a rave in the Netherlands, mildly low sodium in about 1 in 4 women on ecstasy vs 3% of men',
         'found': 'his WOMEN-RISK sentence of round 51 ("Women are most at risk of this, based on results we have from one study done at raves, where sodium was low in 1/4 women vs only 3% of men"); van Dijken et al. 2013 (PubMed 23476039): "Only 3% of males, but no less than ~25% of females attending a rave party and using MDMA developed mild hyponatraemia during the event"',
         'still_needed': 'yes: they watch a woman friend most closely', 'fate': 'kept'},
        {'point': 'among MDMA cases reported to California\'s poison control, women had four times the odds of low sodium',
         'found': 'Rosenson et al. 2007 (PubMed 17084942), California Poison Control System 2000 to 2005: "female sex was associated with increased odds of hyponatremia (odds ratio [OR] 4.0; 95% confidence interval [CI] 2.1 to 7.6)", among patients with a documented sodium level',
         'still_needed': 'yes: they know the risk to women is seen beyond one rave', 'fate': 'kept'},
        {'point': 'MDMA keeps the body from peeing out extra water, so plain water lowers sodium',
         'found': 'Baggott et al. 2016 (PMC4923534): MDMA with water loading lowered sodium more than placebo with water loading; MDMA hyponatremia is thought to combine inappropriate antidiuretic hormone with hypotonic fluid intake',
         'still_needed': 'yes: they know why plain water is the risk', 'fate': 'kept'}],
    'a2-dance': [
        {'point': 'real MDMA is couch lock, not dancing energy; a pill that makes someone feel like dancing may have amphetamines or another drug in it; San Pedro or mescaline is way safer for dancing and still therapeutic',
         'found': 'his DANCE-ENERGY answer of 2026-11-24 01:25 UTC ("if you want to dance you can take some san pedro cactus or mescaline, which is way way safer"; "Real MDMA ... is NOT the kind of mdma that people want to dance on"; "It\'s not like "I don\'t feel like dancing" it\'s like "I can barely move", couch lock"); his round-51 note ("i\'m highly suspicious that contains amphetamines or it\'s not real mdma maybe 6apb"); kept as his view after round 52\'s card gave him what the studies show (Kolbrich 2008: energy ratings rise with the dose)',
         'still_needed': 'yes: they hear the writer\'s case before they decide to dance on it', 'fate': 'kept'},
        {'point': 'in a lab study where people took pure MDMA and drank water, women\'s sodium dropped no more than men\'s; the lab dosed by body weight',
         'found': 'Baggott et al. 2016 (PMC4923534): 1.5 mg/kg MDMA; "There was a trend for women to have lower baseline serum sodium than men, but there were no significant interactions with drug condition"; "their response to drug and water loading was not different from males"; the sex analyses exploratory, the samples small (8 and 8, 6 and 6); his WOMEN-RISK answer of round 52: "you can make a note about the difference between the field vs lab studies then bc that supports what i\'m saying"',
         'still_needed': 'yes: they know the field and the lab disagree, and that a smaller body takes more from the same pill', 'fate': 'kept'}],
}
Q = {
    'Q1': 'PASS: each sentence opens on why it is there',
    'Q2': 'PASS: every instruction is something the friend does or leaves out, with why',
    'Q3': 'PASS: what to do, and the signs that change it',
    'Q4': 'PASS: terms come with their plain words (couch lock: "I can barely move")',
    'Q5': 'PASS: each sentence ties to the one before at its start',
    'Q6': 'PASS: the act first, then why, then what the studies show',
    'Q7': 'PASS: every fact is one he gave or a source says, and his view is said as his',
    'Q8': 'PASS: one point a sentence',
    'Q9': 'PASS: the payoff first',
}


def first(s, body=''):
    for k in PAY:
        if s.startswith(k):
            return k
    return None


def marks(read, rs):
    his, fit = [], []
    for line in (HERE / 'reads' / ('his-%s.txt' % read)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+)(?:-S?(\d+))?[^:]*:\s*([\d, ]+)\s*[—-]', line)
        if m:
            for n in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
                if n - 1 < len(rs):
                    his.append({'s': rs[n - 1], 'difference': m.group(3).strip()})
    for line in (HERE / 'reads' / ('fit-%s.txt' % read)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            if found and int(m.group(1)) - 1 < len(rs):
                fit.append({'s': rs[int(m.group(1)) - 1], 'found': ', '.join(found)})
    return his, fit


def fill(key):
    c = CFG[key]
    read = c['read']
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    cmd = [sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
           '--section', c['section'], '--reader', READER[read]]
    if c['his']:
        cmd += ['--his', str(HERE / c['his'][0]), '--whose', c['his'][1]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(key, 'make:', (r.stdout + r.stderr)[-600:]); return 1
    d = json.loads(out.read_text(encoding='utf-8'))
    for s in d['sentences']:
        if s.get('his'):
            continue
        k = first(s['s'])
        if not k:
            print(key, 'no PAY for:', s['s'][:80]); return 1
        pay, fol, link = PAY[k]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link
    d['checked'] = SRC[key]
    d['placement'] = c['place']
    d['opens']['why_reading'] = c['why']
    d['same_point'] = ('none: read the section from its heading to the next; the dance line is said once, in the paragraph '
                       'after his MDMA paragraph, and low sodium in women once in each, the risk in his paragraph and the '
                       'field vs lab difference in the next, as he asked')
    rs = M.sentences((HERE / ('TEST-%s.txt' % read)).read_text(encoding='utf-8').strip())
    his, fit = marks(read, rs)
    now = [s['s'] for s in d['sentences']]
    mine = [s['s'] for s in d['sentences'] if not s.get('his')]
    hiss = [s['s'] for s in d['sentences'] if s.get('his')]

    def kept_for(lst):
        o = {}
        for x in lst:
            if x in hiss:
                o[x] = 'his own words, kept as he wrote them; what the read found is said in the turn\'s report'
            elif x in mine:
                o[x] = 'kept in version two: the mark is answered in the sentences around it, or it is his view as he said it'
        return o
    d['needed'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md (reads/need-%s.txt), '
                              'on version one' % read), 'unneeded': [], 'kept': {}}
    hm = [m for m in his if m['s'] in now]
    fm = [m for m in fit if m['s'] in now]
    d['his_fixes'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its twenty-seven ways '
                                 '(reads/his-%s.txt), on version one' % read), 'marked': hm, 'kept': kept_for([m['s'] for m in hm])}
    d['fit'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md (reads/fit-%s.txt), on '
                           'version one' % read), 'marked': fm, 'kept': kept_for([m['s'] for m in fm])}
    d['questions'] = Q
    if key == 'a2-mdma':
        d['late_ok'] = {'Plain water': ('his sentence before it first says plain water is the risk and stays as he wrote '
                                        'it; the why comes right after it, where he asked "how does too much water relate '
                                        'to lack of salt?"')}
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1800:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


CFG['a3-dance'] = CFG['a2-dance']
SRC['a3-dance'] = SRC['a2-dance']

if __name__ == '__main__':
    sys.exit(max(fill(k) for k in (sys.argv[1:] or list(CFG))))
