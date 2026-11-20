#!/usr/bin/env python3
"""predict.py - turn 50's predictions (pangram_ledger.py predict), written before each batch's checks.

  python3 predict.py a [KEY...]      units checked as the guide has them (--unchanged)
  python3 predict.py b [KEY...]      tries (build.py TRIES), each with its receipt
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h58-20261120/'
DET = "Pangram web app (his account, Pangram Professional), in the desktop app's browser pane"
DEC_A = ("whether it needs a lesson-19b fix: below High by itself, it is the near miss the next try starts from; Human High "
         "in every window by itself, it stays as it is")
DEC_B = 'whether it goes into the guide: only Human High in every window by itself (gate bad-trips-2026-11-12l)'
H = 'https://www.pangram.com/history/'
sys.path.insert(0, str(HERE))
import build as BD  # noqa: E402

BATCH = {}  # key: batch, for keys checked in a batch other than the first
# key: (call, chance, tells, human tells, why it is on the list)
A = {
    'a01-trip-shadow': ('AI', 0.3, ["During a trip, don't identify with every shadow thought, suppress it, confess it to everybody, "
                                    "or convert it into a permanent diagnosis."],
                        ['Then return to room, body, human, time, and love.'],
                        'h42-41 (a9528123): its sentences AI-Generated Low (23 and 20 words) in the section check; h43\'s fix '
                        'with the paragraph before (79d1ab12) read AI Low and AI Medium; never checked by itself. He left it '
                        'to fix: "you can try to fix p5" (2026-11-20 00:01 UTC), after his rewrite of the section before it'),
}

# key: (call, chance, tells, human tells, first fix, diagnosis)
B = {
    'b01-dmso-side': ('Human', 0.6, ['Sensitivity varies, so try less at first.'], ["I don't smell when I put it into milk."],
                      'payoff: what to do about varying sensitivity said with it ("so try a small amount at first"); join: '
                      'his line joined to what to do; plain: "less" (less than what?) said as "a small amount"',
                      'b06 (21a95b3c) read Human High 179 with "Sensitivity varies." cut; he wants it kept, with what to do '
                      'about it'),
    'b02-niacin-side': ('Human', 0.6, ['especially with liver problems, alcohol, or medications'], ['itchy sunburn-like heat'],
                        'payoff: what carries the risk named first (sustained-release niacin, repeated doses through the '
                        'day); join: none; plain: "Higher" out',
                        'b07 (7ef96156) read Human High 57 with "Higher or repeated doses can create a real risk of liver '
                        'damage"; he says the risk is extended-release, or regular niacin taken through the day'),
}

B.update({
    'c01-dmso-side': ('Human', 0.6, ['Sensitivity to DMSO varies, so start with less than you planned.'],
                      ["I don't smell when I put it into milk."],
                      'payoff: his reason, then what to do ("so start with less than you planned"); join: none, his line '
                      'stays its own sentence; plain: "a small amount" said as less than you planned, his "less"',
                      'b01 (fb34d3fb) read Human with two Medium windows, his new line (9 words) and the rats line (8)'),
    'c02-dmso-side': ('Human', 0.6, ['starting with less than you planned, since sensitivity varies'],
                      ["I don't smell when I put it into milk."],
                      'payoff: the act first, his reason last; join: his line joined into the nausea sentence it belongs to; '
                      'plain: "less than you planned" for "a small amount"',
                      'b01 (fb34d3fb) read Human with two Medium windows, his new line (9 words) on its own and the rats '
                      'line (8)'),
    'd01-trip-shadow': ('AI', 0.4, ['Just notice what\'s there: "A thought is here.'],
                        ['maybe hold off on confessing it to everybody else'],
                        'payoff: what to do with the thought first, each reason after it; join: the four don\'ts of one '
                        'sentence into three sentences with their reasons; plain: "identify with" said as taking it as the '
                        'truth about you, "suppress" as pushing the thought away, "convert it into" as deciding',
                        'a01 (ee4961ce) read AI High in one window over the whole paragraph (100%)'),
    'd02-trip-shadow': ('AI', 0.4, ['Just notice what\'s there: "A thought is here.'],
                        ['since a trip is about the worst time to decide something is permanently wrong with you'],
                        'payoff: what to do with the thought first, each reason after it; join: the four don\'ts of one '
                        'sentence into three sentences with their reasons; plain: "identify with" said as taking it as the '
                        'truth about you, "suppress" as pushing it away, "convert it into a permanent diagnosis" as deciding '
                        'something is permanently wrong with you',
                        'a01 (ee4961ce) read AI High in one window over the whole paragraph (100%)'),
})
BATCH.update({k: 'h58b' for k in ('c01-dmso-side', 'c02-dmso-side', 'd01-trip-shadow')})
BATCH['d02-trip-shadow'] = 'h58c'
BIG = {k: ('a01 read AI High in one window over the whole paragraph (ee4961ce, 100%), so there is no Human window to start '
           'from and no word-level fix it can show; the four don\'ts in one sentence are the list his fifth fix takes apart, '
           'and his round-43 rewrite of the section before it unpacked a compressed line into reasons and examples, the way '
           'this try does') for k in ('d01-trip-shadow', 'd02-trip-shadow')}


def run(a, key):
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1] if out else r.returncode)
    if r.returncode:
        print(out)


def predict_a(key, batch='h58a'):
    call, chance, tells, human, why = A[key]
    ids, scope, what = BD.UNITS[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h58)' % what, '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH.get(key, batch),
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_A,
         '--diagnosis', 'on the list from %s. Checked by itself as the guide has it, before any change (lesson 19b: the near '
                        'miss to start from)' % why,
         '--unchanged', what]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    run(a, key)


def lineage(base):
    ids, scope, what = BD.UNITS[base]
    return ('bad-trips %s (h57)' % what) if base in BD.BB.UNITS else ('bad-trips %s (h58)' % what), scope


def predict_b(key, batch='h58a'):
    call, chance, tells, human, first, diag = B[key]
    base, edits, why = BD.TRIES[key]
    lin, scope = lineage(base)
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', lin, '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH.get(key, batch),
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_B,
         '--diagnosis', '%s. This try changes %s. Better: Human High in every window' % (diag, why),
         '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--humanized', 'lesson 19b: from the near miss, only what he asked for, a word or two (%s)' % why,
         '--first-fix', first]
    if key in BIG:
        a += ['--big-change', BIG[key]]
    if key in globals().get('PANEL', {}):
        a += ['--panel', PANEL[key]]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    run(a, key)


if __name__ == '__main__':
    kind, keys = sys.argv[1], sys.argv[2:]
    if kind == 'a':
        for k in keys or list(A):
            predict_a(k)
    elif kind == 'b':
        for k in keys or list(B):
            predict_b(k)

BIG['d02-trip-shadow'] = ('d01 (1eac3d57) read AI High over the whole paragraph, its script and the room line in the AI windows '
                          '("A feeling is here." AI Medium on its own): no Human window to start from, and d01 had kept the '
                          'two parts that read AI; this try says the script in one breath and the room line as the things to '
                          'come back to')
B['d02-trip-shadow'] = ('AI', 0.4, ['tends to make it come back stronger'], ['OK, there\'s a thought, and there\'s a feeling'],
                        'payoff: what to do with the thought first, each reason after it; join: the script\'s three lines '
                        'joined into one breath; plain: "human" said as the person with you, "time" as what time it is, '
                        '"suppress" as pushing it away',
                        'd01 (1eac3d57) read AI High over the whole paragraph (100%), the script and the room line in its '
                        'windows')
if __name__ == '__main__' and sys.argv[1:2] == ['c']:
    for k in sys.argv[2:] or ['d02-trip-shadow']:
        predict_b(k)

# ---- batch h58d (B415's third try, after the tell panel) and h58e (his four, a word or two each) ----
PANEL = {'d03-trip-shadow': REL + 'panel-d03/PANEL.md'}
B.update({
    'd03-trip-shadow': ('AI', 0.35, ["Just notice the thought and the feeling that came with it."],
                        ["don't go texting your whole family about it at 3 a.m."],
                        'payoff: what a shadow thought looks like first, with two examples; join: none, sentences of '
                        'different lengths, as the panel asked; plain: "shove the thought down", "a lifelong disorder", '
                        '"texting your whole family at 3 a.m."',
                        'd02 (the tell panel, panel-d02/PANEL.md: S2 to S5 agreed, and the whole read as an even sequence '
                        'with no specific detail) and d01 (1eac3d57, AI High 100%)'),
    'e01-aftermath': ('Human', 0.55, ['Try to find the underlying psychological or physical patterns driving the symptoms:'],
                      ['which solves nothing'],
                      'payoff: none moved, his order; join: none; plain: "or physical" for "and/or physiological", '
                      '"after a trip" says which symptoms',
                      'a18 (522cc1a4) read his heading with his first sentence Human Medium (23) and his last Human Medium '
                      '(13)'),
    'e02-ss-recognize': ('Human', 0.6, ['One or more of these patterns makes the diagnosis more likely:'],
                         ['would be counted as one pattern altogether'],
                         'payoff: none moved; join: none; plain: "the Hunter criteria, the same checklist clinicians use", '
                         'the term explained where first used',
                         'a23 (67e584da) read the heading with his first sentence Human Medium (17)'),
    'e03-first-five': ('Human', 0.65, ['Put any weapons away and keep the person away from crowds and strangers.'],
                       ['or pools of water for that matter'],
                       'payoff: none moved; join: none; plain: "until tomorrow" says how long the confrontation waits',
                       'a24 (189231bd) read his confront line Human Medium (10)'),
    'e04-redefining': ('AI', 0.45, ['offers no shortage of difficult experiences to process'],
                       ['that explanation might have come too late'],
                       'payoff: none moved; join: none; plain: "Samsara" explained where first used, "present-moment '
                       'trauma" said as the trauma the trip itself is causing, "the blockage" as what\'s blocking it',
                       'a14 (3b646eb8) read AI Detected 44%: his "Samsara" sentence AI Low, his last sentence AI Medium, '
                       'my line after it AI Low'),
})
BATCH.update({'d03-trip-shadow': 'h58d', 'e01-aftermath': 'h58e', 'e02-ss-recognize': 'h58e', 'e03-first-five': 'h58e',
              'e04-redefining': 'h58e'})
BIG['d03-trip-shadow'] = ('d01 and d02 read AI High in every window with my words in his frame; the tell panel on d02 agreed on '
                          'four of its five sentences and on the whole (an even run of sentences with no specific detail), '
                          'so this try rebuilds it around what a shadow thought looks like on a trip')
if __name__ == '__main__' and sys.argv[1:2] == ['d']:
    for k in sys.argv[2:]:
        predict_b(k)
