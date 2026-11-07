#!/usr/bin/env python3
"""predict_batch3.py - the predictions for h29's third batch (his After the Storm moves carried), written before the checks."""
import pathlib, subprocess, sys
REPO = pathlib.Path(__file__).resolve().parents[4]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'; H = 'articles/bad-trips/humanize/h29-20261107'
DET = "Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane"
MOVE = ("his After the Storm moves carried, after a fresh reader's sense read: the reader handed the choice in the middle of the "
        "commands (a question to them), why said and not only what, a claim left a little unbalanced, 'a' or 'an' for 'one', "
        "contractions; the linter run first ('it's tempting to', 'actually', 'without ...ing' and 'X does not Y' taken out)")
WHY = ("his own series on After the Storm went from AI High to Human High only when he gave the reader agency ('Ask your body "
       "what it needs from you now'), after explaining more than commands (High to Medium), 'an' for 'one' (High to Medium) and "
       "'true (or false)' (the first part Human)")
P = []
def add(key, lineage, name, chance, before, cause, decides, first, tells, human):
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lineage, '--scope', 'paragraph',
         '--text', '%s/TEST-base-%s.txt' % (H, name), '--key', key, '--call', 'Human' if chance >= 0.5 else 'AI',
         '--chance', str(chance), '--detector', DET, '--diagnosis', WHY + '; ' + before + '; ' + cause, '--decides', decides,
         '--receipt', '%s/TEST-base-%s.receipt.json' % (H, name), '--humanized', MOVE, '--first-fix', first]
    for t in tells: a += ['--tells', t]
    for t in human: a += ['--human-tells', t]
    P.append(a)
add('bt-as-af', "bad-trips After the Storm, no another ceremony, his After the Storm moves", 'AF', 0.5,
    "the paragraph read 72% as a nine-item don't list", "this says the pull to do more first, asks what they'd tell a rattled friend, and gives the likely answer",
    "whether agency carries to the 'another ceremony' list", "payoff: the reflex (more looks like the answer) leads; join: the don'ts made one sentence of what more looks like; plain: 'until the floor is back' to 'back on their feet'",
    ['the list of nine kept as one run'], ["'Would you tell a friend this rattled to do any of that?'", "'I'd guess you'd tell them'"])
add('bt-as-sh', "bad-trips Dealing With Shadow Thoughts, during a trip, his After the Storm moves", 'SH', 0.45,
    "the paragraph read 100% as a four-item don't list, a script and a list of five nouns", "this says the pull first ('can feel like the truth about you'), then 'Just notice it'",
    "whether agency carries to the shadow-thought paragraph", "payoff: how a shadow thought pulls leads; join: the don'ts made one sentence of urges; plain: 'identify with' to 'can feel like the truth about you'",
    ['the script kept as it is'], ["'can feel like the truth about you'", "'Just notice it'"])
add('bt-as-nr', "bad-trips No Rash Actions, the don't list, his After the Storm moves", 'NR', 0.4,
    "the list read 38% to 43%", "this asks the reader what really can't wait, answers 'Usually nothing', and keeps his list as it is",
    "whether a question to the reader carries the long don't list", "payoff: the question leads; join: the answer joined to the list; plain: none changed in his list, the question is new ('What really can't wait')",
    ['the fifteen-item list kept'], ["'What really can't wait until you've slept and eaten?'", "'Usually nothing'"])
add('bt-as-ab', "bad-trips Abuse Memories, don't confront tonight, his After the Storm moves", 'AB', 0.5,
    "the paragraph read 58%", "this puts what to do first, says why not to confront, and glosses 'integration specialist' and 'trauma-informed'",
    "whether the point first, a reason and plain glosses carry 'Don't confront tonight'", "payoff: write it down and get safe now lead; join: the urgency joined to it as 'though'; plain: 'trauma-informed therapist' to 'a therapist who works with trauma'",
    ['the list of six things seen kept'], ["'it rarely goes the way you hope'", "'though it may feel like it has to be dealt with tonight'"])
add('bt-as-al', "bad-trips Alone at 3 a.m., the movement paragraph, his After the Storm moves", 'AL', 0.5,
    "the section read 50%", "this asks the body what would calm it (his 'Ask your body' move), then gives the usual answer",
    "whether his 'ask your body' move carries to the 3 a.m. movement", "payoff: what to do (ask the body) leads; join: the answer joined as 'Usually that's'; plain: 'protect sleep' to 'let yourself sleep, or at least lie down and rest'",
    ["'small and boring' kept"], ["'ask it what would calm it down rather than wind it up'"])
add('bt-as-st', "bad-trips Stillness or Movement?, the two cases, his After the Storm moves", 'ST', 0.45,
    "the section read AI in every form tried", "this says each case as it feels ('a prison', 'an escape'), with what escape looks like, and what both are for",
    "whether plain cases and the why carry Stillness or Movement?", "payoff: the first case leads; join: both cases end on what they're for; plain: 'discharge' to 'burn off the charge', 'resemble escape' to 'turning into an escape'",
    ['two If sentences in a row'], ["'(you keep drifting toward the door)'", "'Either way'"])
add('bt-as-fl', 'bad-trips The Fear/Panic Loop, his round-22 move', 'FL2', 0.45,
    "the loop read 97%, then 100% with the denial move", "this hands the reader a test ('Notice whether the answer is calming you down or winding you up') and leaves the claim unbalanced ('maybe not every time')",
    "whether agency and an unbalanced claim carry the loop", "payoff: what the mind does with terror leads; join: the test and the name made one turn; plain: 'desperate action' to 'a desperate plan'",
    ['the five answers still a run'], ["'Notice whether the answer is calming you down or winding you up'", "'(maybe not every time, but often enough to stop and notice)'"])
add('bt-as-hp', "bad-trips For the Person Helping's opening, his round-22 move", 'HP2', 0.45,
    "the opening read 100% in every wording, the denial move included", "this asks the sitter what the person needs, answers 'I doubt it's ...', and ends on what a difficult experience can be",
    "whether a question to the sitter and a personal 'I doubt' carry the opening", "payoff: the question leads; join: the four not-needs made one 'I doubt' sentence; plain: 'difficult does not automatically mean bad' to 'a difficult experience can still be a good one'",
    ['the four not-needs still a run'], ["'think about what the person in front of you needs right now'", "'I doubt it's'"])
add('bt-as-mv', "bad-trips Minimum Viable Integration, his After the Storm moves", 'MV', 0.45,
    "the list read 66%", "this keeps the four steps and says why for two of them ('while you still remember them'; 'it may mean less than it felt like, or more')",
    "whether the why inside each step carries the numbered list", "payoff: each step keeps its label first; join: none, the list stays; plain: 'ordinary contact' to 'the people you normally see', 'behavioral changes' to 'changes in how you live'",
    ['a numbered list kept'], ["'while you still remember them'", "'(it may mean less than it felt like, or more)'"])
add('bt-as-tc', "bad-trips Hand on Heart's touch part, his round-22 move", 'TC2', 0.45,
    "the touch part read 52%, then 27% with the denial move ('Good support may be silent presence' AI Medium, the next paragraph AI High)", "this gives self-touch an example, says why touch can go wrong ('they may feel it as a threat'), and the consent paragraph with its reason",
    "whether reasons carry the touch part and its consent paragraph", "payoff: the difference between self-touch and another's comes first, with an example; join: the reason joined to the urge; plain: 'silent presence' to 'sitting quietly', 'unrelated to the helper's needs' to 'about their needs, never yours'",
    ['five touches still a run'], ["'they may feel it as a threat'", "'because any of those can mean no'"])
for a in P:
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(a[a.index('--key') + 1], '|', (out[-1] if out else r.returncode)[:200])
