#!/usr/bin/env python3
"""fill_sodium.py - the making-sense receipt of the two sodium sentences in his MDMA: Magnesium Alarm paragraph (B119),
from his QUIZ-2 note of 2026-11-23 ("check this out: https://onlinelibrary.wiley.com/doi/10.1111/add.70255 this is
important because it shows that MDMA can cause dangerous hyponatremia in something like 1/4 of people at a festival").
One round of the three fresh reads came first (reads/*-a6-sodium.txt) on version one (TEST-a6-sodium-v1.txt); version
two (TEST-a7-sodium.txt) answers their marks: "That happened" named ("Low sodium"), the study said as what it means for
the helper (who is most at risk), the reassuring ending out, and the sign said with what to do ("stop the water and give
them something salty"), the sign that can tell (bloated, not thirsty) rather than one already true (they've drunk a lot).

  python3 fill_sodium.py a7-sodium
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

READ = 'a6-sodium'
READER = ('a friend at a festival with someone who took MDMA a few hours ago, whose jaw is tight and who has been drinking '
          'a lot of water, reading what to do')
NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with the whole paragraph, its heading and what '
        'it is for (reads/need-%s.txt), on version one (TEST-a6-sodium-v1.txt)' % READ)
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its twenty-three ways (twenty-six from 2026-11-23), with the paragraph one '
        'sentence a line (reads/his-%s.txt), on version one' % READ)
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version, with the paragraph '
       '(reads/fit-%s.txt), on version one' % READ)
PAY = {
    "Low sodium seems to hit women hardest": ('they watch a woman\'s water more closely', 'the sodium drop just named',
                                              'Low sodium'),
    "If they've drunk a lot and feel bloated": ('they stop the water and give something salty when the water is the '
                                                'likely problem', 'the water and the sodium just named',
                                                "If they've drunk a lot"),
    "Magnesium Alarm](": ('the link\'s second half', 'the sentence it is in', ''),
}
CHECKED = [
    {'point': 'at one rave about one in four women who took MDMA had a mild case of low sodium, against 3% of men',
     'found': ('van Dijken et al. 2013, PubMed 23476039: mild hyponatraemia in 14.3% of the ravers who took MDMA, about a '
               'quarter of the women and 3% of the men'),
     'still_needed': 'yes: they watch a woman\'s water more closely', 'fate': 'kept'},
    {'point': ('after a lot of water, feeling bloated and not thirsty points to too much water; the field treatment is to '
               'stop the water and give salt'),
     'found': ('AAFP summary of the Wilderness Medical Society guidelines on exercise-associated hyponatremia (2021): mild '
               'EAH "often manifests as bloating, weight gain"; its table lists "Bloated feeling" and "No thirst"; "Fluid '
               'restriction is the primary treatment"; salt by oral hypertonic solutions (bouillon cubes) "or by '
               'consumption of salty foods"'),
     'still_needed': 'yes: they know what to do when the water is the problem', 'fate': 'kept'},
]
KEPT = {}
Q = {
    'Q1': 'PASS: each new sentence opens on why it is there: who is most at risk, the sign that tells',
    'Q2': 'PASS: the second says what to do when the sign is there',
    'Q3': 'PASS: the sign is one a friend can ask about (bloated, not thirsty)',
    'Q4': 'PASS: no term a reader needs explained',
    'Q5': 'PASS: each ties to the one before at its start (Low sodium, If they\'ve drunk a lot)',
    'Q6': 'PASS: before the signs that call for medics, as the milder stage',
    'Q7': 'PASS: every fact is one a source says, linked',
    'Q8': 'PASS: one point a sentence',
    'Q9': 'PASS: the payoff first',
}
HIS = ('HIS-sodium.txt', 'his own: his MDMA: Magnesium Alarm paragraph (B119, round 42), with the review he sent on '
       'round 50 linked on "sodium dropping too low"')


def first(s, body=''):
    for k in PAY:
        if s.startswith(k):
            return k
    for sent in re.split(r'(?<=[.!?])\s+', body):
        if s in sent and not sent.startswith(s):
            return first(sent)
    return None


def marks(rs):
    his, fit = [], []
    for line in (HERE / 'reads' / ('his-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+)(?:/S?(\d+))?[^:]*:\s*([\d, ]+)\s*[—-]', line)
        if m:
            for n in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
                his.append({'s': rs[n - 1], 'difference': m.group(3).strip()})
    for line in (HERE / 'reads' / ('fit-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            if found:
                fit.append({'s': rs[int(m.group(1)) - 1], 'found': ', '.join(found)})
    return his, fit


def fill(key):
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    cmd = [sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
           '--section', 'MDMA: Magnesium Alarm', '--reader', READER, '--his', str(HERE / HIS[0]), '--whose', HIS[1]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(key, 'make:', (r.stdout + r.stderr)[-600:]); return 1
    d = json.loads(out.read_text(encoding='utf-8'))
    body = ' '.join(s['s'] for s in d['sentences'])
    for s in d['sentences']:
        if s.get('his'):
            continue
        k = first(s['s'], body)
        if not k:
            print(key, 'no PAY for:', s['s'][:80]); return 1
        pay, fol, link = PAY[k]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link
    d['checked'] = CHECKED
    d['placement'] = 'his MDMA: Magnesium Alarm paragraph (B119), after his sentence on plain water and sodium'
    d['opens']['why_reading'] = 'it tells the friend who is most at risk of low sodium and how to tell when the water is the problem'
    d['same_point'] = ('none: read the section from its heading to the next (MDMA: Magnesium Alarm to Chest Pain and Injury); '
                       'step 6 of Act Now on SS points to these signs, not says them again')
    rs = M.sentences((HERE / ('TEST-%s-v1.txt' % READ)).read_text(encoding='utf-8').strip())
    his, fit = marks(rs)
    mine = [s['s'] for s in d['sentences'] if not s.get('his')]
    hiss = [s['s'] for s in d['sentences'] if s.get('his')]

    def kept_for(lst):
        out = {}
        for x in lst:
            if x in hiss:
                out[x] = 'his own words, kept as he wrote them; what the read found is on the card with my best fix'
            elif x in mine:
                out[x] = KEPT.get(first(x, body)) or 'changed in version two'
        return out
    d['needed'] = {'reader': NEED, 'unneeded': [], 'kept': {}}
    hm = [m for m in his if m['s'] in mine or m['s'] in hiss]
    fm = [m for m in fit if m['s'] in mine or m['s'] in hiss]
    d['his_fixes'] = {'reader': HISF, 'marked': hm, 'kept': kept_for([m['s'] for m in hm])}
    d['fit'] = {'reader': FIT, 'marked': fm, 'kept': kept_for([m['s'] for m in fm])}
    d['questions'] = Q
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1500:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in (sys.argv[1:] or ['a7-sodium'])))
