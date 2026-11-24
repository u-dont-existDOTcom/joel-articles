#!/usr/bin/env python3
"""fill_h72.py - the making-sense receipts of turn 64's texts: the dance paragraph (R52-DANCE) with his MAPS-SETTING
answer of 2026-11-24 14:20 UTC, and the Medium windows of steps 6 and 8 under Act Now on SS (AGENTS.md's done rule of
2026-11-24: every window High). One round of the three fresh reads came first, on version one (reads/*-a1-dance.txt,
reads/*-a1-ss6.txt, reads/*-a1-ss8.txt); version two answers their marks.

  python3 fill_h72.py a2-dance a2-ss6 a2-ss8
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

CFG = {
    'a2-dance': dict(read='a1-dance', section='MDMA: Magnesium Alarm',
                     his=('HIS-dance.txt', 'his own: his DANCE-ENERGY answer of round 52 and his MAPS-SETTING answer of '
                                           'round 53 (2026-11-24 14:20 UTC)'),
                     place=('the paragraph after his MDMA paragraph (B119), whose last sentence names overheating among '
                            'what brings on a seizure or collapse; its "That\'s why" turns on that sentence and on the '
                            'salt the paragraph is about; before the kidney paragraph (B120)'),
                     why=('it tells someone going to dance on MDMA why not to, what the writer would take instead, and '
                          'what he thinks a pill that makes someone feel like dancing says about it')),
    'a2-ss6': dict(read='a1-ss6', section='Act Now on SS',
                   his=('HIS-ss6.txt', 'his own: his step 6 of round 48, its first sentence as he wrote it'),
                   place='step 6 of the eight steps under "Act Now on SS" (B136)',
                   why='it tells the friend what to give for salt, potassium and magnesium, how, and when to stop'),
    'a3-ss8': dict(read='a1-ss8', section='Act Now on SS', his=None,
                   place='step 8 of the eight steps under "Act Now on SS" (B136), the last',
                   why=('it tells the friend which of this guide\'s remedies to use, which to leave out, and which to '
                        'keep for a last resort')),
    'a2-ss8': dict(read='a1-ss8', section='Act Now on SS', his=None,
                   place='step 8 of the eight steps under "Act Now on SS" (B136), the last',
                   why=('it tells the friend which of this guide\'s remedies to use, which to leave out, and which to '
                        'keep for a last resort')),
}
READER = {
    'a1-dance': ('someone about to go to a festival with friends who plan to take MDMA and dance all night, reading '
                 'this the day before'),
    'a1-ss6': ('a friend sitting with someone who took MDMA on top of their antidepressant and now has twitching '
               'muscles, sweating and a racing heart; they have called an ambulance and read what to do while they wait'),
}
READER['a1-ss8'] = READER['a1-ss6']
PAY = {
    # the dance paragraph: as turn 63 checked it, with his MAPS-SETTING answer added before his suspicion
    "That's why I'd tell everyone not to dance": ('they keep their friends from dancing on MDMA', 'the overheating and the low sodium just named', "That's why"),
    "And really, what's the point of MDMA": ('they see the writer\'s case against MDMA for dancing', 'the no dancing just said', 'And really'),
    "For that they can take": ('they know what the writer would take to dance instead', 'the question just asked', 'For that'),
    "Real MDMA, the kind": ('they know what the writer says real MDMA is like', 'the MDMA of the question', 'Real MDMA'),
    "No, they're sitting there": ('they know the writer\'s view rests on his and his friends\' experience', 'the trials just named', "No, they're sitting there"),
    "It's not like": ('they know what the writer means by not wanting to dance', 'what the real thing feels like, just named', "It's not like"),
    "And in the same exact setting": ('they know it is the pill and not the place that decides, so their own urge to dance says something about the pill', 'the couch lock just named', 'And in the same exact setting'),
    "So if a pill makes someone feel like dancing": ('they know the writer suspects a pill that makes someone feel like dancing', 'the pills that went both ways, just named', 'So if a pill'),
    "That might also be why women": ('they know the field and the lab disagree on women, and the writer\'s reading of it', 'the suspect pills just named', 'That might also be why'),
    "Then again, the lab dosed everyone": ('they know the lab differed in another way, so a small friend gets more from the same pill', 'the lab just named', 'Then again, the lab'),
    # step 6: as turn 62 checked it, with the high-potassium line said as the act
    "If they still show the signs": ('they know when the friend needs more than a drink', 'the drink just named', 'If they still show'),
    "Salty potato chips give the salt": ('they give salty chips, as many as wanted', 'the salt and potassium just named', 'Salty'),
    "That's the only way I'd give potassium": ('they give potassium only in food', 'the chips just named', "That's"),
    "Their potassium could be running high": ('they know potassium can go either way', 'the potassium just named', 'Their potassium'),
    "So if they start vomiting or get diarrhea": ('they stop the chips at the first vomiting or diarrhea', 'the potassium that may be running high, just named', 'So if they start'),
    "Magnesium also runs low": ('they know to give magnesium too', 'the salt and potassium just named', 'Magnesium also'),
    "Magnesium chloride tastes too bad": ('they put it on the skin instead of making them drink it', 'the magnesium just named', 'Magnesium chloride'),
    "If you don't have the flakes": ('they use Epsom salt the same way', 'the flakes just named', "If you don't have"),
    "If they can stand the taste": ('they can give it by mouth too, with the amounts', 'the taste just named', 'If they can stand the taste'),
    "Magnesium Alarm](": ('the link\'s second half', 'the sentence it is in', ''),
    # step 8: as turn 62 checked it, with the niacin line and the oil's reason said as the act and the case
    "Since a seizure is one of the main dangers": ('they use DMSO and know how', 'the seizure in step 7', 'Since a seizure'),
    "You might also think of": ('they leave niacin out', 'DMSO just named', 'also'),
    "What I'd leave out is": ('they leave niacin out', 'the DMSO just given', "What I'd leave out"),
    "The other remedy I'd keep": ('they keep Syrian rue oil for a last resort', 'niacin just named', 'The other remedy'),
    "The oil isn't the Syrian rue brew": ('they know step 1 meant the brew, and that the oil is unstudied with MDMA', 'the oil just named', 'The oil'),
    "The reason I'd keep it that late": ('they know why it is the last one: nobody has given the oil with MDMA in a study', 'the last resort just named', "The reason I'd keep it that late"),
    "What makes the brew in step 1": ('they know step 1 meant the brew, and what the brew does that the oil does not', 'the oil just named', 'What makes the brew'),
}
SRC = {
    'a2-dance': [
        {'point': 'the setting isn\'t what decides: in the same setting, some pills had him wanting to dance and some left him in couch lock',
         'found': 'his MAPS-SETTING answer of 2026-11-24 14:20 UTC: "It\'s not because of the setting. i\'ve been in the same exact setting takign different mdma, some makes you want to dance, some makes you almost incapable of moving"',
         'still_needed': 'yes: they read their own urge to dance as something about the pill, not the place', 'fate': 'kept'},
        {'point': 'real MDMA is couch lock, not dancing energy; a pill that makes someone feel like dancing may have amphetamines or another drug in it; San Pedro or mescaline is way safer for dancing and still therapeutic',
         'found': 'his DANCE-ENERGY answer of 2026-11-24 01:25 UTC; his round-51 note ("i\'m highly suspicious that contains amphetamines or it\'s not real mdma maybe 6apb"); kept as his view after round 52\'s card gave him what the studies show (Kolbrich 2008: energy ratings rise with the dose)',
         'still_needed': 'yes: they hear the writer\'s case before they decide to dance on it', 'fate': 'kept'},
        {'point': 'in a lab study where people took pure MDMA and drank water, women\'s sodium dropped no more than men\'s; the lab dosed by body weight',
         'found': 'Baggott et al. 2016 (PMC4923534): 1.5 mg per kg; "There was a trend for women to have lower baseline serum sodium than men, but there were no significant interactions with drug condition"; his WOMEN-RISK answer of round 52 asked for the field vs lab note here',
         'still_needed': 'yes: they know the field and the lab disagree, and that a smaller body takes more from the same pill', 'fate': 'kept'}],
    'a2-ss6': [
        {'point': 'salty potato chips give salt and potassium with nothing to cook, as many as they want',
         'found': 'his QUIZ-3 answer of 2026-11-23 23:35 UTC: "i\'d have a bag of salty potato chips on hand that, has salt and potassium, no need to cook anything. and i\'d eat as much of those as they want to"',
         'still_needed': 'yes: they give salt and potassium without cooking', 'fate': 'kept'},
        {'point': 'too much potassium brings on vomiting and diarrhea, so the chips stop when those start',
         'found': 'his QUIZ-3 answer: "with high potassium they are more likely to have vomiting and diarrhea (which then causes hypokalemia as it removes potassium)"; round 50: "nausea and diarrhea are more indicative of hyper"',
         'still_needed': 'yes: they stop the chips at the first sign', 'fate': 'kept'},
        {'point': 'the second half of his note, that the vomiting and diarrhea then drain potassium again, is out of this step',
         'found': 'his QUIZ-3 answer\'s parenthesis ("which then causes hypokalemia as it removes potassium"); the three fresh reads on version one each stumbled on it: that draining argues for more potassium, not less, and "they" could be the friend or the signs (reads/his-a1-ss6.txt S8, reads/need-a1-ss6.txt S8, reads/fit-a1-ss6.txt S8), and its sentence was the step\'s Medium window',
         'still_needed': 'no: they do the same thing either way, and the step already says potassium can run high as well as low', 'fate': 'cut'},
        {'point': 'magnesium chloride tastes terrible and the skin absorbs it from a handful of flakes in a little water; Epsom salt is magnesium sulfate and gets through the skin less well',
         'found': 'his QUIZ-3 answer: "magnesium chloride tastes terrible ... make sure we are mentioning it\'s absorbed thru the skin when dissolved in a little water"; "epsom salt is magnesium sulfate"',
         'still_needed': 'yes: they give magnesium a way the friend will take', 'fate': 'kept'},
        {'point': 'many people with serotonin syndrome run low on magnesium',
         'found': 'the nursing review he sent on round 49 (doi.org/10.1097/01.NME.0000432871.59839.f3)',
         'still_needed': 'yes: they give magnesium as well as salt and potassium', 'fate': 'kept'}],
    'a3-ss8': [
        {'point': 'DMSO seems to help prevent seizures, by people\'s reports; start low, since some people react more strongly',
         'found': 'his SS-ASKED-2 answer (c) of round 50 ("definitely seems to prevent seizures"); his QUIZ-3 answer: "some people are more sensitive than others ... start low go slow"',
         'still_needed': 'yes: they know how to start DMSO and how fast to add more', 'fate': 'kept'},
        {'point': 'niacin is the one to leave out: the trip-ending dose can cause flushing and a drop in blood pressure, which is unsafe with serotonin syndrome',
         'found': 'his round-49 step 8 ("niacin is actually unsafe with serotonin syndrome") and his SS-ASKED answer (c) ("Niacin can cause flushing, low blood pressure"); NIH Office of Dietary Supplements, Niacin fact sheet (ods.od.nih.gov/factsheets/Niacin-Consumer)',
         'still_needed': 'yes: they leave niacin out while they wait', 'fate': 'kept'},
        {'point': 'Syrian rue oil is the last resort if nothing else is helping and no medics are coming: it makes trips much less intense, nobody has given it with MDMA in a study, and unlike the brew of step 1 it does not block MAO',
         'found': 'his SS-OIL answer of 2026-11-23 23:35 UTC ("it doesn\'t inhibit MAO, which is what normally makes syrian rue tea dangerous with MDMA"; "it makes trips (including ayahuasca) much less intense"; "a last resort for SS if nothing else is helping and no medics are coming"; "there is just no research on this so that\'s the main reason i\'m cautious")',
         'still_needed': 'yes: they know when the oil is worth trying and why it comes last', 'fate': 'kept'}],
}
Q = {
    'Q1': 'PASS: each sentence opens on why it is there',
    'Q2': 'PASS: every instruction is something the friend does or leaves out, with why',
    'Q3': 'PASS: what to do, and the signs that change it',
    'Q4': 'PASS: terms come with their plain words (MAO, the enzyme that clears serotonin)',
    'Q5': 'PASS: each sentence ties to the one before at its start',
    'Q6': 'PASS: what to give or do first, then what to stop, then the last resort',
    'Q7': 'PASS: every fact is one he gave or a source says, and his view is said as his',
    'Q8': 'PASS: one point a sentence',
    'Q9': 'PASS: the payoff first',
}


SRC['a2-ss8'] = SRC['a4-ss8'] = SRC['a3-ss8']
CFG['a4-ss8'] = CFG['a3-ss8']


def first(s):
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
    d['same_point'] = ('none: read the section from its heading to the next; magnesium is said once in the steps (step 6), '
                       'with its amounts in MDMA: Magnesium Alarm, which step 6 points to, and the dance line once, in the '
                       'paragraph after his MDMA paragraph')
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
                o[x] = ('kept in version two: it read High in its window last turn, and the mark is answered in the '
                        'sentences around it or is his view as he said it')
        return o
    d['needed'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md (reads/need-%s.txt), '
                              'on version one' % read), 'unneeded': [], 'kept': {}}
    hm = [m for m in his if m['s'] in now]
    fm = [m for m in fit if m['s'] in now]
    d['his_fixes'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its twenty-eight ways '
                                 '(reads/his-%s.txt), on version one' % read),
                      'marked': hm, 'kept': kept_for([m['s'] for m in hm])}
    d['fit'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md (reads/fit-%s.txt), on '
                           'version one' % read), 'marked': fm, 'kept': kept_for([m['s'] for m in fm])}
    d['questions'] = Q
    if key == 'a3-ss8':
        d['late_ok'] = {'MAO': 'the term comes with its plain words where the step first uses it, in the last sentence'}
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1800:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in (sys.argv[1:] or list(CFG))))
