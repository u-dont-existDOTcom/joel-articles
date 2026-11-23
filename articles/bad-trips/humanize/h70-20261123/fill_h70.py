#!/usr/bin/env python3
"""fill_h70.py - the making-sense receipts of turn 62's texts, written from his round-51 answers (2026-11-23 23:35 UTC):
step 6 (salty potato chips, magnesium on the skin, Epsom salt is magnesium sulfate, high potassium and vomiting), step 8
(DMSO first, then niacin, then Syrian rue oil as a last resort, the magnesium moved to step 6), and his MDMA paragraph
(B119: no dancing, why plain water lowers sodium, how much salt). One round of the three fresh reads came first, on
version one (reads/*-a1-ss.txt on TEST-a1-ss.txt, the whole list; reads/*-a1-mdma.txt on TEST-a1-mdma.txt); version two
answers their marks.

  python3 fill_h70.py a2-ss6 a2-ss8 a2-mdma
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

CFG = {
    'a2-ss6': dict(read='a1-ss', section='Act Now on SS', his=('HIS-ss6.txt', 'his own: his step 6 of round 48, its first sentence as he wrote it'),
                   place='step 6 of the eight steps under "Act Now on SS" (B136)',
                   why='it tells the friend what to give for salt, potassium and magnesium, and how'),
    'a2-ss8': dict(read='a1-ss', section='Act Now on SS', his=None,
                   place='step 8 of the eight steps under "Act Now on SS" (B136), the last',
                   why='it tells the friend which of this guide\'s remedies to use, which to leave out, and which to keep for a last resort'),
    'a2-call': dict(read='a1-call', section='Call Medics For:', his=None,
                    place='the Call Medics For list (B94), the first part of When to Get Outside Help',
                    why='it tells the friend which signs mean calling medics now'),
    'a2-mdma': dict(read='a1-mdma', section='MDMA: Magnesium Alarm',
                    his=('HIS-mdma.txt', 'his own: his MDMA: Magnesium Alarm paragraph (B119, round 42, MED-MDMA)'),
                    place='his MDMA: Magnesium Alarm paragraph (B119)',
                    why='it tells the friend what to do once the jaw tenses, why plain water is a risk, and when to call medics'),
}
READER = {'a1-call': ('a friend with someone who took something a few hours ago and is getting worse, reading the list to '
                       'decide whether to call an ambulance'),
          'a1-ss': ('a friend sitting with someone who took MDMA on top of their antidepressant and now has twitching muscles, '
                    'sweating and a racing heart; they have called an ambulance and read what to do while they wait'),
          'a1-mdma': ('a friend at a festival with someone who took MDMA a few hours ago and has been dancing, whose jaw is '
                      'tight and who has been drinking a lot of water, reading what to do')}
PAY = {
    "If they still show the signs": ('they know when the friend needs more than a drink', 'the drink just named', 'If they still show'),
    "Salty potato chips give the salt": ('they give salty chips, as many as wanted', 'the salt and potassium just named', 'Salty'),
    "That's the only way I'd give potassium": ('they give potassium only in food', 'the chips just named', "That's"),
    "Their potassium could be running high": ('they know potassium can go either way', 'the potassium just named', 'Their potassium'),
    "High potassium also brings on": ('they stop the chips if vomiting or diarrhea starts', 'the high potassium just named', 'High potassium also'),
    "Magnesium also runs low": ('they know to give magnesium too', 'the salt and potassium just named', 'Magnesium also'),
    "Magnesium chloride tastes too bad": ('they put it on the skin instead of making them drink it', 'the magnesium just named', 'Magnesium chloride'),
    "If you don't have the flakes": ('they use Epsom salt the same way', 'the flakes just named', "If you don't have"),
    "If they can stand the taste": ('they can give it by mouth too, with the amounts', 'the taste just named', 'If they can stand the taste'),
    "Magnesium Alarm](": ('the link\'s second half', 'the sentence it is in', ''),
    "Since a seizure is one of the main dangers": ('they use DMSO and know how', 'the seizure in step 7', 'Since a seizure'),
    "You might also think of": ('they leave niacin out', 'DMSO just named', 'also'),
    "The other remedy I'd keep": ('they keep Syrian rue oil for a last resort', 'niacin just named', 'The other remedy'),
    "The oil isn't the Syrian rue brew": ('they know step 1 meant the brew, and that the oil is unstudied with MDMA', 'the oil just named', 'The oil'),
    "While it's natural to want to dance": ('they keep their friend from dancing', 'the slowing down just named', "While it's natural"),
    "Plain water is the risk because": ('they know why plain water lowers sodium', 'the plain water just named', 'Plain water'),
    "The following indicators would justify calling medics": ('they know the signs that call for medics and what to give meanwhile', 'the risk just named', 'The following indicators'),
    "If their confusion or headache worsens": ('they know the signs that call for medics and what to give meanwhile', 'the lead-in just before', 'If their confusion'),
    "That has to be a lot of salt": ('they know how much salt', 'the salty food just named', 'That'),
}
SRC = {
    'a2-ss6': [
        {'point': 'salty potato chips give salt and potassium with nothing to cook, as many as they want',
         'found': 'his QUIZ-3 answer of 2026-11-23 23:35 UTC: "i\'d have a bag of salty potato chips on hand that, has salt and potassium, no need to cook anything. and i\'d eat as much of those as they want to"',
         'still_needed': 'yes: they give salt and potassium without cooking', 'fate': 'kept'},
        {'point': 'high potassium brings on vomiting and diarrhea, which then drain it',
         'found': 'his QUIZ-3 answer: "with high potassium they are more likely to have vomiting and diarrhea (which then causes hypokalemia as it removes potassium)"; round 50: "nausea and diarrhea are more indicative of hyper"',
         'still_needed': 'yes: they stop the chips if those start', 'fate': 'kept'},
        {'point': 'magnesium chloride tastes terrible and the skin absorbs it from a handful of flakes in a little water; Epsom salt is magnesium sulfate and gets through the skin less well',
         'found': 'his QUIZ-3 answer: "magnesium chloride tastes terrible ... make sure we are mentioning it\'s absorbed thru the skin when dissolved in a little water"; "just put like a handful of mag chloride flakes in water and then rub that on their skin"; "epsom salt is magnesium sulfate (many people think it\'s more like table salt because it\'s salt)"; round 50: "epsom salts also absorb thru the skin, just not as well"',
         'still_needed': 'yes: they give magnesium a way the friend will take', 'fate': 'kept'},
        {'point': 'many people with serotonin syndrome run low on magnesium',
         'found': 'the nursing review he sent on round 49 (doi.org/10.1097/01.NME.0000432871.59839.f3)',
         'still_needed': 'yes: they give magnesium as well as salt and potassium', 'fate': 'kept'}],
    'a2-ss8': [
        {'point': 'DMSO seems to help prevent seizures, by people\'s reports; start low, since some people react more strongly',
         'found': 'his SS-ASKED-2 answer (c) of round 50 ("definitely seems to prevent seizures", from "the forum signal"); his QUIZ-3 answer: "I\'d just say that some people are more sensitive than others ... start low go slow"',
         'still_needed': 'yes: they know how to start DMSO and how fast to add more', 'fate': 'kept'},
        {'point': 'niacin at trip-ending doses can cause flushing and low blood pressure',
         'found': 'NIH Office of Dietary Supplements, Niacin fact sheet (ods.od.nih.gov/factsheets/Niacin-Consumer)',
         'still_needed': 'yes: they leave niacin out while they wait', 'fate': 'kept'},
        {'point': 'Syrian rue oil does not block MAO, unlike the brew, makes trips much less intense, and is unstudied with MDMA: a last resort if nothing helps and no medics come',
         'found': 'his SS-OIL answer of 2026-11-23 23:35 UTC ("it doesn\'t inhibit MAO, which is what normally makes syrian rue tea dangerous with MDMA"; "it makes trips (including ayahuasca) much less intense"; "a last resort for SS if nothing else is helping and no medics are coming"; "there is just no research on this"); his section Syrian Rue Oil: Gentler',
         'still_needed': 'yes: they know when the oil is worth trying', 'fate': 'kept'}],
    'a2-call': [
        {'point': 'every sign of the list as it stood, said as what the friend sees: slow, shallow breathing; blue or gray lips; the seizure rules; collapse, not waking, getting harder to wake; dangerously hot; rigid muscles, fever with clonus; no sleep for days; one-sided weakness, losing speech, not walking normally, wetting or soiling; the brain feeling damaged with the checks failing; the chest pain cases; serious injury; vomiting that won\'t stop, blood, dehydration, stomach pain; an MAOI with something that raises serotonin',
         'found': 'the list as the guide had it (B94, from his post, with "No sleep for days" from his round-50 answer); fidelity keys R50 PASS on the guide with this list in it',
         'still_needed': 'yes: they call medics for each sign the list had before', 'fate': 'kept'}],
    'a2-mdma': [
        {'point': 'dancing makes heat and sweat that drain salt; he would tell everyone not to dance on MDMA',
         'found': 'his MDMA-SODIUM answer of 2026-11-23 23:35 UTC: "i\'d also just blanket warn people not to dance on mdma"',
         'still_needed': 'yes: they keep their friend from dancing', 'fate': 'kept'},
        {'point': 'MDMA makes the body hold on to water, so plain water lowers sodium',
         'found': 'Baggott et al. 2016 (PMC4923534): "MDMA potentiated the ability of water to lower serum sodium"; MDMA hyponatremia is thought to combine inappropriate antidiuretic hormone with hypotonic fluid intake',
         'still_needed': 'yes: they know why plain water is the risk', 'fate': 'kept'},
        {'point': 'the field amount of salt by mouth: three or four bouillon cubes in half a cup of water',
         'found': 'AAFP summary of the Wilderness Medical Society guidelines on exercise-associated hyponatremia: "three to four bouillon cubes or three ramen seasoning packets per 125 mL of water"; severe cases get 100 mL IV boluses of hypertonic saline, up to three',
         'still_needed': 'yes: they know a snack is too little', 'fate': 'kept'}],
}
Q = {
    'Q1': 'PASS: each sentence opens on why it is there',
    'Q2': 'PASS: every instruction is something the friend does or leaves out, with why',
    'Q3': 'PASS: what to give, how, and when to stop',
    'Q4': 'PASS: terms come with their plain words (Epsom salt is magnesium sulfate)',
    'Q5': 'PASS: each sentence ties to the one before at its start',
    'Q6': 'PASS: what to do first, then what not to do, then the last resort',
    'Q7': 'PASS: every fact is one he gave or a source says',
    'Q8': 'PASS: one point a sentence',
    'Q9': 'PASS: the payoff first',
}


def first(s, body=''):
    for k in PAY:
        if s.startswith(k):
            return k
    for sent in re.split(r'(?<=[.!?])\s+', body):
        if s in sent and not sent.startswith(s):
            return first(sent)
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
    body = ' '.join(s['s'] for s in d['sentences'])
    for s in d['sentences']:
        if s.get('his'):
            continue
        k = first(s['s'], body)
        if not k and key == 'a2-call':
            s['payoff'], s['follows'] = 'they call medics when they see this sign', 'the heading, Call Medics For'
            if 'link' in s:
                s['link'] = 'none: a new item of the call list, which finishes its heading'
            continue
        if not k:
            print(key, 'no PAY for:', s['s'][:80]); return 1
        pay, fol, link = PAY[k]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link
    d['checked'] = SRC[key]
    d['placement'] = c['place']
    d['opens']['why_reading'] = c['why']
    d['same_point'] = ('none: read the section from its heading to the next; magnesium is now said once in the steps '
                       '(step 6), with its amounts in MDMA: Magnesium Alarm, which step 6 points to')
    rs = M.sentences((HERE / ('TEST-%s.txt' % ('a1-ss' if read == 'a1-ss' else 'a1-mdma'))).read_text(encoding='utf-8').strip())
    his, fit = marks(read, rs)
    mine = [s['s'] for s in d['sentences'] if not s.get('his')]
    hiss = [s['s'] for s in d['sentences'] if s.get('his')]

    def kept_for(lst):
        o = {}
        for x in lst:
            if x in hiss:
                o[x] = 'his own words, kept as he wrote them; what the read found is said in the turn\'s report'
            elif x in mine:
                o[x] = 'kept in version two: the mark is answered in the sentences around it'
        return o
    d['needed'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md (reads/need-%s.txt), '
                              'on version one' % read), 'unneeded': [], 'kept': {}}
    hm = [m for m in his if m['s'] in mine or m['s'] in hiss]
    fm = [m for m in fit if m['s'] in mine or m['s'] in hiss]
    d['his_fixes'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its twenty-six ways '
                                 '(reads/his-%s.txt), on version one' % read), 'marked': hm, 'kept': kept_for([m['s'] for m in hm])}
    d['fit'] = {'reader': ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md (reads/fit-%s.txt), on '
                           'version one' % read), 'marked': fm, 'kept': kept_for([m['s'] for m in fm])}
    d['questions'] = Q
    if key == 'a2-mdma':
        d['late_ok'] = {'Plain water': ('his sentence before it first says plain water is the risk and stays as he wrote it; the why comes right after it, where he asked "how does too much water relate to lack of salt?"')}
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1500:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in (sys.argv[1:] or list(CFG))))
