#!/usr/bin/env python3
"""predict.py - turn 59's predictions (pangram_ledger.py predict) for my serotonin steps 1, 3, 4, 7 and 8, each by itself,
written his way after his round-48 steps 5 and 6, and checked only after four rounds of fresh reads (lesson
bad-trips-2026-11-21d: sense first, Pangram after). Written before the checks.

  python3 predict.py [KEY...]
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h67-20261121/'
DET = "Pangram web app (his account), in the desktop app's browser pane"
BATCH = 'h67a'
LIN = ('bad-trips Suspected Serotonin Syndrome step %d by itself: B136, "Do this immediately when serotonin toxicity is '
       'reasonably suspected:" (h62 c1-ss-steps-1, as it stood)')
FIRST = ('payoff: each step opens on why the reader is reading it, his way ("Overstimulating also dehydrates them, but we '
         'can\'t give fluids unless ..."): too much serotonin, the call the line before asked for, the heat the muscles '
         'make, the wait, the remedies they may reach for; join: the reason and the act in one sentence, the second '
         'sentence saying how it follows ("of course, but also", "so", "also", "Then", "though"); plain: the drugs named '
         'with what they are (the painkiller tramadol, the antibiotic linezolid), the antidepressant kinds with brand '
         'names, harmala as Syrian rue, no hospital line the reader can\'t act on')
BIG = ('his round-48 fix of steps 5 and 6 showed that the old steps\' trouble was sense, not wording: a step that doesn\'t '
       'say why it\'s there, a don\'t with no reason or nothing to do instead, a line said twice, advice that isn\'t right '
       'here; small fixes of the old wording keep all four, so each step is written again his way (lesson '
       'bad-trips-2026-11-21d), not in a new form for the detector')
HUM = ('written his way from his round-48 steps 5 and 6, then through four rounds of the three fresh reads, every mark changed or kept with why: each step opens on why the reader is reading it, the reason joined to the act; the impulse named before the don\'t (driving them yourself, the cold bath, a fever reducer, the guide\'s other remedies); terms explained where first used (serotonergic, the antidepressant kinds with brand names, the painkiller tramadol, the antibiotic linezolid, harmala as Syrian rue); his first person where it is his judgment (I\'d stop, I\'d hold off, I\'d call them only once, I\'d gather, I would consider); the hospital line the reader can\'t act on out')
DECIDES = ('whether step %d goes in as I wrote it his way: Human High in every window by itself; if not, the window says '
           'which sentence still doesn\'t read right, and the next change is that sentence\'s sense, in the same direction')
P = {
    1: ('AI', 0.4, ['No more MDMA or other stimulants, of course, but also no DXM cough syrup, the painkiller tramadol or the antibiotic linezolid.',
                    'whether it\'s an SSRI like Prozac or Zoloft, Effexor or another SNRI, or an MAOI'],
        ['Serotonin syndrome comes from too much serotonin, so I\'d stop anything', 'And don\'t forget the supplements people don\'t think of as drugs']),
    3: ('Human', 0.55, ['You can also call poison control to figure out which mix of drugs did this'],
        ['so don\'t drive them yourself, even if it seems faster']),
    4: ('AI', 0.45, ['So while you wait for the ambulance, move them somewhere cool, take off extra clothes, and use a fan and cool damp cloths.'],
        ['A cold bath would cool them faster, but', 'seem like the obvious thing for someone this hot']),
    7: ('Human', 0.5, ['Then I\'d write down how much of each they took and when, including any recreational drugs and supplements.'],
        ['so the doctors can see whether the person is getting better or worse']),
    8: ('AI', 0.45, ['like niacin for ending a trip or DMSO for brain injuries, seizures and chest pain'],
        ['While you wait, you might think of this guide\'s other remedies']),
}
OLD = {1, 4, 8}   # lineages with a try before (h65's g3a, g3d, g3h)
DIAG = {
    1: ('what changed: the step opens on why (serotonin syndrome comes from too much serotonin), and the drugs go from the '
        'obvious ones to the ones people don\'t think of, each named with what it is, ending on the supplements in the '
        'reader\'s own cupboard, where the last try was a lead line over a bare list of categories; why it should help: '
        'his fixes read Human where each sentence says why the reader is reading it (way 13) and a list ends on the '
        'reader\'s own life (lesson 07j); better: Human in every window, at High'),
    4: ('what changed: the step opens on the heat the muscles make, which is why cooling comes first; the bath and the '
        'fever reducer say why someone would reach for them before why not, and the ice packs say why those places; why '
        'it should help: his step 5 ("While it\'s natural ..., the problem is ...") and his step 6, which opens on why '
        'fluids come up at all, read Human High where my flat rules read AI; better: Human in every window, at High'),
    8: ('what changed: the hospital line the reader can\'t act on is out (two needed reads), and the step opens on the '
        'reader\'s moment, the remedies of this guide they may reach for while they wait, before saying not to use them; '
        'why it should help: his fixes open on what calls for a step (way 13) and name the impulse first (way 14); '
        'better: Human in every window, at High'),
}


def run(n):
    call, chance, tells, human = P[n]
    key = 'v6-ss%d' % n
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', LIN % n, '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', call, '--chance', str(chance),
         '--detector', DET, '--decides', DECIDES % n, '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--first-fix', FIRST, '--humanized', HUM]
    if n in OLD:
        a += ['--big-change', BIG, '--diagnosis', DIAG[n]]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:1200] if r.returncode else out.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    ks = [int(k) for k in sys.argv[1:]] or list(P)
    sys.exit(max(run(n) for n in ks))
