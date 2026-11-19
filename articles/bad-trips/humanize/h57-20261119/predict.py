#!/usr/bin/env python3
"""predict.py - turn 49's predictions (pangram_ledger.py predict), written before each batch's checks.

  python3 predict.py h57a          every baseline unit of build_baseline.py, checked as the guide has it (--unchanged)
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
DET = "Pangram web app (his account, Pangram Professional), in the desktop app's browser pane"
DEC_A = ("whether it needs a lesson-19b fix: below High by itself, it is the near miss the next try starts from; Human High "
         "in every window by itself, it stays as it is")
sys.path.insert(0, str(HERE))
import build_baseline as BB  # noqa: E402

# key: (call, chance, tells, human tells, h42 or later windows below High that put it on the list)
A = {
    'a01-brain-protocol': ('AI', 0.25, ['Do not manufacture reassurance from missing information.',
                                        'At this point safety matters more than preserving the experience.'],
                           ['take a 5mg lick of it'],
                           'h42-06 (4076db14): "DMSO immediately." Human Medium, "Ask what the symptoms ..." Human Medium, '
                           '"If this is a psychedelic ..." Human Low, among AI windows; never checked by itself'),
    'a02-coffee-cherry': ('Human', 0.6, ['It may also extend the trip.'], ['Eating a couple of coffee cherries helps my nausea.'],
                          'h43 (d00c127c): "It may also extend the trip." Human Medium; the rest High'),
    'a03-bmg-mdma': ('Human', 0.5, ['centered on magnesium, temperature, sodium, potassium, hydration, serotonin toxicity'],
                     ['I was rushing to help and may have given more than I would now.'],
                     'h42-25 (523d93cd): B178\'s second sentence Human Medium, a run of category words (his fixes, way 1)'),
    'a04-shungite': ('Human', 0.5, ['Shungite should not be drunk unless it has been properly washed of heavy metals.'],
                     ['which can cost around $20 on Amazon'],
                     'h42-23 (dbfabf7b): both halves Human Low'),
    'a05-dmso-overlap': ('Human', 0.6, ['has what I consider a perfect safety profile'], ['I don\'t yet know why.'],
                         'h42-19 (793cb8f9): the last sentence Human Low'),
    'a06-dmso-side': ('Human', 0.5, ['Sensitivity varies.', 'DMSO can also burn dry mouth tissue, so the mouth should be moist first.'],
                      ['I don\'t smell when I put it into milk.'],
                      'h42-19 (793cb8f9): the mouth and nausea lines Human Medium, the better-sleep and body-odor lines Human Low, '
                      'the milk line Human Medium; his round-39 sleep text since in the Reduced sleep item, never checked here'),
    'a07-niacin-side': ('Human', 0.5, ['This is normal, although some people find it intolerable and others enjoy it.'],
                        ['itchy sunburn-like heat'],
                        'h42-25 (523d93cd): the flush line and heartburn Human Medium, drowsiness and the risk line Human Low'),
    'a08-niacin-forms': ('Human', 0.5, ['Avoid sustained-release niacin and the useless non-flush hexanicotinate form.'],
                         ['the useless non-flush hexanicotinate form'],
                         'h43 (60f2bff5): B215\'s last sentence Human Medium; the list as in a07'),
    'a09-humic-caution': ('Human', 0.6, ['I wouldn\'t use it casually during a bad trip.'],
                          ['can produce a hyperintelligent state for me'],
                          'h42-14 (495edcec): the heading and first sentence Human Low'),
    'a10-anchor-lead': ('Human', 0.55, ['One person can only handle so much, though.'], ['to back them up'],
                        'h43 (3a3fd073): its first two sentences Human Medium'),
    'a11-music': ('Human', 0.5, ['Use familiar music when possible.'], ['like that of Chantress Seba and others on my music page'],
                  'h43 (7fd43eaf): "Music" and its first line Human Medium'),
    'a12-move-list': ('Human', 0.55, ['The same goes after a stimulant or an unknown mixture, or with any medical concern.'],
                      ['with nothing high to fall from'],
                      'h43 (7fd43eaf): the exercise line\'s second sentence Human Medium'),
    'a13-shadow-def': ('Human', 0.65, ['is central.'], ['Shadow work to me is neither BDSM nor "feeding your demons."'],
                       'h42-36 (236a3091): "Inner-child reparenting is central." Human Medium'),
    'a14-redefining': ('Human', 0.6, ['Samsara offers no shortage of difficult experiences to process.'],
                       ['that explanation might have come too late'],
                       'h42-42 (4972cd65): two of his sentences and B357 Human Medium'),
    'a15-sorrow': ('Human', 0.7, [], ['it took me months of daily loveyhuasca after my ex-wife Bee left to understand it'],
                   'h42-37 (8d71284e): "Missing hurts." and his Bee line Human Medium'),
    'a16-shadow-thoughts': ('Human', 0.5, ['Shadow thoughts and feelings are not inherently a problem.'],
                            ['I also notice them after excessive focus.'],
                            'h42-41 (a9528123): the heading with both paragraphs Human Low (65, 7 and 19 words)'),
    'a17-opposites': ('Human', 0.55, ['In the subconscious world of concepts, however, two sides are often considered together.'],
                      ['A hated baby does not feel love'],
                      'h43 (79d1ab12): B414\'s last sentence Human Medium'),
    'a18-aftermath': ('Human', 0.55, ['may obviate the need for one'], ['which solves nothing'],
                      'h42-46 (78353445): the heading alone Human Medium'),
    'a19-appendix': ('Human', 0.6, [], ['The monk Ajahn Jayasaro gives useful guidance'],
                     'h42-50 (eeba7d60): "U.C." alone Human Medium (2 words)'),
    'a20-aura': ('Human', 0.65, [], ['although that\'s just a hunch based on the effects I notice so far'],
                 'h42-07 (6280b126): the heading and his first two sentences Human Medium (44 words)'),
    'a21-cbd-topical': ('Human', 0.6, [], ['Generalized are the type people usually have with MDMA & psychedelic overdoses'],
                        'h43 (5f6a6b57): "As for topical CBD, it hasn\'t been well-studied." Human Medium'),
    'a22-cbd-dmso': ('Human', 0.55, ['and we know it has several neuroprotective mechanisms'], ['I\'d still consider DMSO alongside it'],
                     'h43 (83f4caef): its last sentence Human Medium (21 words)'),
    'a23-ss-recognize': ('Human', 0.55, [], ['We can use the same Hunter criteria that clinicians use'],
                         'h46 (0dfe5d10), his round-36 version in place: the heading and first sentence Human Medium (17 words)'),
    'a24-first-five': ('Human', 0.7, [], ['or pools of water for that matter'],
                       'h42-27 (71e9dd23): "And if they want to leave, have someone go with them." Human Medium (11 words)'),
    'a25-after-storm': ('Human', 0.55, ['To prevent your mind from giving spirituality a negative connotation'],
                        ['not the 20 chaotic people who are still coming down'],
                        'h42-45 (53464de3): its last two sentences Human Low'),
    'a26-mh-support': ('AI', 0.35, ['The trauma material is bigger than the room can hold'], ['(that yin yoga again!)'],
                       'never checked: 38 words, under the web app\'s minimum, so it goes with the item before it (his)'),
}


def predict_a(key):
    call, chance, tells, human, why = A[key]
    ids, scope, what = BB.UNITS[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h57)' % what, '--scope', scope,
         '--text', 'articles/bad-trips/humanize/h57-20261119/TEST-%s.txt' % key, '--key', key, '--batch', 'h57a',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_A,
         '--diagnosis', 'on the list from %s. Checked by itself as the guide has it, before any change (lesson 19b: the near '
                        'miss to start from)' % why,
         '--unchanged', what]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1] if out else r.returncode)
    if r.returncode:
        print(out)


if __name__ == '__main__':
    if sys.argv[1:2] == ['h57a']:
        for k in sys.argv[2:] or list(A):
            predict_a(k)


# ---- batch h57b: the lesson-19b tries from each near miss (build_tries.py) ----
import build_tries as BT  # noqa: E402
B = {
    'b05-dmso-overlap': ('Human', 0.6, ['has what I consider a perfect safety profile'], ['but I don\'t yet know why'],
                         'payoff: none moved, the comparison leads; join: the two semicolon pairs and "I don\'t yet know '
                         'why" joined to what it answers; plain: "in my experience" said once'),
    'b06-dmso-side': ('Human', 0.6, ['Nausea: when drinking DMSO, dilute it in water, juice, or milk and sip gradually.'],
                      ['I don\'t smell when I put it into milk.'],
                      'payoff: the rat finding after its limit; join: none; plain: "less deep" for "lighter", "the skin" and '
                      '"the DMSO" for two "it"s, "crenate" explained, "wet your mouth first"'),
    'b07-niacin-side': ('Human', 0.6, ['especially with liver problems, alcohol, or medications'], ['itchy sunburn-like heat'],
                        'payoff: the risk said as what it is (liver damage); join: none; plain: "The flush" for "This", '
                        '"sensitive physiology" out'),
    'b08-niacin-forms': ('Human', 0.5, ['Niacinamide sometimes relaxes people and sometimes creates hyperfocus'],
                         ['the useless "no-flush" kind'],
                         'payoff: the risk said as what it is; join: none; plain: "than niacin" said, the no-flush form '
                         'named as a label has it, "The flush" for "This"'),
    'b10-anchor-lead': ('Human', 0.55, ['bring in one more calm adult or a crisis professional'], ['to back them up'],
                        'payoff: none moved; join: none; plain: "the anchor" for "them", "keeping everyone from getting '
                        'hurt" for "safe", "get that help" for "do it"'),
    'b12-move-list': ('Human', 0.6, ['Avoid strenuous exercise if you\'re overheating or have chest pain'],
                      ['with nothing high to fall from'],
                      'payoff: what to skip said first ("Skip exercise too"); join: none; plain: "if you\'ve taken" for '
                      '"after", "have any other" for "with any"'),
    'b13-shadow-def': ('Human', 0.6, ['aren\'t some error in your philosophy'], ['Shadow work to me is neither BDSM'],
                       'payoff: none moved; join: none; plain: "this work" for an "it" that could point two ways, the '
                       'term explained where it is used'),
    'b17-opposites': ('Human', 0.6, ['I am not repeating the simplistic Hermetic claim'], ['A hated baby does not feel love'],
                      'payoff: none moved; join: none; plain: "the mind" who keeps them, "both" for "the two sides"'),
    'b19-appendix': ('Human', 0.75, [], ['The monk Ajahn Jayasaro gives useful guidance'],
                     'payoff: none moved; join: none; plain: UC for "U.C.", which read as a sentence of its own'),
}
H = 'https://www.pangram.com/history/'


def predict_b(key):
    call, chance, tells, human, first = B[key]
    base, edits, why = BT.TRIES[key]
    ids, scope, what = BB.UNITS[base]
    r = json.loads((HERE / 'RESULTS-h57a.json').read_text(encoding='utf-8'))[base]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h57)' % what, '--scope', scope,
         '--text', 'articles/bad-trips/humanize/h57-20261119/TEST-%s.txt' % key, '--key', key, '--batch', 'h57b',
         '--call', call, '--chance', str(chance), '--detector', DET,
         '--decides', 'whether it goes into the guide: only Human High in every window by itself (gate bad-trips-2026-11-12l)',
         '--diagnosis', ('%s, as the guide has it, read %s (%s%s): the near miss. This try changes %s. Better: Human High in '
                         'every window' % (base, r[0], H, r[5].strip('/'), why)),
         '--receipt', 'articles/bad-trips/humanize/h57-20261119/TEST-%s.receipt.json' % key,
         '--humanized', 'lesson 19b: from the near miss, only the words its windows below High hold that a reader could take '
                        'two ways, a word or two each (%s)' % why,
         '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    out = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    o = (out.stdout + out.stderr).strip()
    print(key, '|', o.splitlines()[-1] if o else out.returncode)
    if out.returncode:
        print(o)


if __name__ == '__main__' and sys.argv[1:2] == ['h57b']:
    for k in sys.argv[2:] or list(B):
        predict_b(k)


# ---- batch h57c: the next try from each near miss still below High after h57b ----
C = {
    'c05-dmso-overlap': ('Human', 0.55, ['has what I consider a perfect safety profile'], ['calms a trip better'],
                         'payoff: none moved; join: the first semicolon pair; plain: "the charcoal water" for "the water", '
                         '"calms a trip better" for "works better"',
                         'b05 (137ef380) read the same as a05 with both joins: the window on this sentence holds its '
                         'two-way words, "the water" and "works better"'),
    'c08-niacin-forms': ('Human', 0.55, ['Avoid sustained-release niacin'], ['relaxes some people, but it can make others hyperfocused'],
                         'payoff: none moved; join: the pair built two ways with "but"; plain: "the state the person is in"',
                         'b08 (a5c2e9d1) read Human, Medium 61 over B215: its "sometimes ... and sometimes" and "their state"'),
    'c13-shadow-def': ('Human', 0.55, ['aren\'t some error in your philosophy'], ['Shadow work to me is neither BDSM'],
                       'payoff: none moved; join: none; plain: "central to shadow work" for "central"',
                       'b13 (6f1ae0bf) read worse than a13, its three sentences one Medium window: the explanation I added; '
                       'this try from a13 names only what it is central to'),
    'c17-opposites': ('Human', 0.55, ['I am not repeating the simplistic Hermetic claim'], ['A hated baby does not feel love'],
                      'payoff: what happens to a concept said; join: "though" for "however"; plain: "each idea often comes '
                      'paired with its opposite"',
                      'b17 (a4b0fea1) read the same as a17, Medium 13 on this sentence: "the mind ... both" left what '
                      'happens unsaid'),
}


def predict_c(key):
    call, chance, tells, human, first, diag = C[key]
    base, edits, why = BT.TRIES_C[key]
    ids, scope, what = BB.UNITS[base]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h57)' % what, '--scope', scope,
         '--text', 'articles/bad-trips/humanize/h57-20261119/TEST-%s.txt' % key, '--key', key, '--batch', 'h57c',
         '--call', call, '--chance', str(chance), '--detector', DET,
         '--decides', 'whether it goes into the guide: only Human High in every window by itself (gate bad-trips-2026-11-12l)',
         '--diagnosis', '%s. This try changes %s. Better: Human High in every window' % (diag, why),
         '--receipt', 'articles/bad-trips/humanize/h57-20261119/TEST-%s.receipt.json' % key,
         '--humanized', 'lesson 19b: from the near miss, a word or two a reader could take two ways (%s)' % why,
         '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    out = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    o = (out.stdout + out.stderr).strip()
    print(key, '|', o.splitlines()[-1] if o else out.returncode)
    if out.returncode:
        print(o)


if __name__ == '__main__' and sys.argv[1:2] == ['h57c']:
    for k in sys.argv[2:] or list(C):
        predict_c(k)
