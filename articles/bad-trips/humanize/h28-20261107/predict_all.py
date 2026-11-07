#!/usr/bin/env python3
"""predict_all.py - the predictions for this folder's tests (pangram_ledger.py predict), written before the checks."""
import subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
H = 'articles/bad-trips/humanize/h28-20261107'
DET = "Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane"
MOVE = ("his round-22 move carried: the denial said as how it feels ('it might feel like X'), then 'but more likely' or "
        "'but'; what happens said first and then named ('and we call that ...'); lists said as acts with verbs; contractions")
P = []
def add(key, lineage, name, call, chance, tells, human, diagnosis, decides, first, humanized=None, unchanged=None):
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lineage, '--scope', 'paragraph',
         '--text', '%s/TEST-base-%s.txt' % (H, name), '--key', key, '--call', call, '--chance', str(chance), '--detector', DET,
         '--diagnosis', diagnosis, '--decides', decides]
    for t in tells: a += ['--tells', t]
    for t in human: a += ['--human-tells', t]
    if unchanged:
        a += ['--unchanged', unchanged]
    else:
        a += ['--receipt', '%s/TEST-base-%s.receipt.json' % (H, name), '--humanized', humanized, '--first-fix', first]
    P.append(a)
WHY = ("his own two tries of the not-broken paragraph differ only in one sentence and a 'But': 'It's not that you're damaged "
       "for good, nor that ...' read AI 99.99% (14fa25d1), 'I might feel in the moment like you're damaged for good ... But "
       "more likely ...' read Human (68752b7e)")
add('bt-his-a0', 'bad-trips (Re)defining "Bad Trip", his version (round 22)', 'A0', 'Human', 0.8,
    ['none of the old denial left'], ["'I might feel in the moment like'", "'But more likely factors include'"],
    WHY + "; this checks his passing version exactly as he sent it, after the Human base, as the guide would have it",
    'whether his version reads Human where the guide puts it', None,
    unchanged="his version as he sent it on round 22's card (TEACH-NOT-BROKEN), from his Pangram history 68752b7e, after the Human base")
add('bt-his-a1', 'bad-trips (Re)defining "Bad Trip", his version with two typos fixed (round 22)', 'A1', 'Human', 0.7,
    ['the typos he made are gone'], ["'It might feel in the moment like'", "'But more likely factors include'"],
    WHY + "; this is his version with two typos fixed ('I might feel' to 'It might feel', 'no that' to 'or that') and a double space, to see whether the fixes cost the reading",
    'whether his typos can be fixed without a downside', "payoff: unchanged, his; join: unchanged, his; plain: two typos fixed, 'I might feel' to 'It might feel' and 'no that' to 'or that'",
    humanized="fixed two typos in his version ('I might feel' to 'It might feel', 'no that' to 'or that') and a double space; every other word his")
add('bt-move-sp', 'bad-trips Spiritual ≠, the bypassing and practice pair, his round-22 move', 'SP', 'AI', 0.45,
    ['the quoted views still a run of four'], ["'it can feel wise to reach for'", "'and we call that bypassing'", "'because pretending helps nobody'"],
    WHY + "; the pair read 71% after the Human base with 'Bypassing reaches for an ultimate view ... while ignoring the person' and a list of what practice does; this says bypassing as how it feels and then names it, and practice's last act as a reason",
    "whether his move carries to the bypassing and practice pair", "payoff: what bypassing is now said from the scene (someone shaking in the corner) and named last; join: practice's acts in one sentence with its reason; plain: 'stop pretending' to 'because pretending helps nobody'",
    humanized=MOVE)
add('bt-move-fl', 'bad-trips The Fear/Panic Loop, his round-22 move', 'FL', 'AI', 0.45,
    ["'maybe with metaphysics or a diagnosis' still lists"], ["'When terror comes up'", "'and we call that fear trying to solve fear'"],
    WHY + "; the loop read 97% and 51% with 'A common loop is fear trying to solve fear' first and a five-noun list; this says what happens first and names it last, the list as things the mind does",
    "whether his move carries to the fear loop", "payoff: what happens comes first (terror comes up, the mind answers it), its name after; join: the name and the list made one sentence; plain: 'desperate action' to 'doing something desperate'",
    humanized=MOVE)
add('bt-move-hk', "bad-trips Demons' hooks, his round-22 move", 'HK', 'AI', 0.45,
    ["'Hatred and fear, shame, pride and rage' a run of five"], ["'give these things something to hook into'", "'and love takes the hooks out'"],
    WHY + "; the hooks read 26% after the Human base as two clipped sentences ('... make hooks. Love removes hooks.'); this joins them into one with what the feelings do, and adds the sentence before it so 'these things' has its antecedent",
    "whether his move carries to the hooks", "payoff: what the feelings do (give these things a hold) first; join: the two clipped sentences made one; plain: 'removes hooks' to 'takes the hooks out'",
    humanized=MOVE)
add('bt-move-uh', "bad-trips Demons' unhookable, his round-22 move", 'UH', 'AI', 0.5,
    ['one denial-like turn left ("but this is how")'], ["'It might look passive, but'", "'there's nothing in love for it to grab'"],
    WHY + "; 'This is not passivity. It is becoming unhookable.' read 18% after the Human base; this says the denial as how it looks and joins the list to its point",
    "whether his move carries to 'unhookable'", "payoff: unhookable comes in the first sentence, as what this is; join: 'not passivity' and 'becoming unhookable' made one sentence, the demon's list joined to love's answer; plain: 'Love gives it nothing to grab' to 'there's nothing in love for it to grab'",
    humanized=MOVE)
add('bt-move-hp', "bad-trips For the Person Helping's opening, his round-22 move", 'HP', 'AI', 0.45,
    ['the four pulls still a run'], ["'you might feel the pull to'", "'But the job is simpler'"],
    WHY + "; 'A good sitter is not there to win a philosophy debate, perform a rescue fantasy, ...' read AI in every wording tried; this says the four as pulls the sitter might feel, then the job",
    "whether his move carries to the helper's opening", "payoff: the sitter's pulls come first, said to them; join: the job and the Zendo summary made one sentence; plain: 'demonstrate spiritual advancement' to 'show how spiritually advanced you are'",
    humanized=MOVE)
add('bt-move-tc', "bad-trips Hand on Heart's touch part, his round-22 move", 'TC', 'AI', 0.45,
    ['the five touches still a run'], ["'It might feel compassionate to'", "'but ask first'"],
    WHY + "; 'Compassion does not mean grabbing, hugging, restraining, stroking, or crowding.' read 52%; this says it as what might feel compassionate, joined to the question to ask",
    "whether his move carries to the touch part", "payoff: what to do (ask first) now in the same sentence as what tempts; join: the denial and 'Ask first' made one sentence; plain: 'crowding' to 'crowd in close'",
    humanized=MOVE)
add('bt-move-bl', "bad-trips When the Trip Feels Amazing's bliss line, his round-22 move", 'BL', 'AI', 0.5,
    ['the italic voice lines kept'], ["'That bliss can feel like proof that you're safe'", "'but more likely'"],
    WHY + "; 'Bliss is not proof of safety, and it often makes grounding less welcome.' read 51% to 69%; this says it as how bliss feels, then 'but more likely'",
    "whether his move carries to the bliss line", "payoff: what bliss does to grounding stays the paragraph's end, now after the feeling; join: one sentence as before; plain: 'is not proof of safety' to 'can feel like proof that you're safe'",
    humanized=MOVE)
add('bt-move-fr', "bad-trips After the Storm's fruit of insight, his round-22 move", 'FR', 'AI', 0.45,
    ["'the fruit of an insight' kept"], ["'It can feel like the more cosmic the story sounds'", "'But the fruit'"],
    WHY + "; 'The fruit of insight isn't how cosmic the story sounds. It's whether ...' is the same denial; this says it as how it feels, then 'But'",
    "whether his move carries to the fruit of insight", "payoff: the feeling first, the measure after it; join: the two sentences turn on 'But'; plain: 'isn't how cosmic the story sounds' to 'the more cosmic the story sounds, the bigger the insight'",
    humanized=MOVE)
# the second batch (N1, N4, W3, S3) was predicted the same way, by the lines run from the shell after the first
for a in P:
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(a[a.index('--key') + 1], '|', out[-1] if out else r.returncode)
