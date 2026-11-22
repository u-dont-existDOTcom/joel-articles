#!/usr/bin/env python3
"""predict.py - turn 52's predictions (pangram_ledger.py predict), written before each batch's checks.

  python3 predict.py e [KEY...]     try 5 of the three units h59 left below High (B286; B391 and B392; B401 and B404)
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h60-20261120/'
H59 = 'articles/bad-trips/humanize/h59-20261120/'
DET = "Pangram web app (his account), in the desktop app's browser pane"
LINEAGE = {  # the lineage names h59 used (UNITS of h59's build.py), so the ledger's near-miss rule sees every try
    'harm': 'bad-trips When What They Say Turns Toward Harm: B286 (51 words), by itself as the guide has it (h59)',
    'touch': 'bad-trips Touch, Consent, and Compassion: B391, B392 (62 words), by itself as the guide has it (h59)',
    'demons': 'bad-trips Demons, Jinn, Entities, and Shadow Forces: B401, B404 (66 words), by itself as the guide has it (h59)',
}
DEC = ('whether this change from the near miss lifts the unit to Human High by itself: if so it goes into the guide in '
       'place of the unit (apply_gate.py); if not, the windows say which part the sixth and last try changes, and what '
       'stays below High after it goes to his marking page as a round-45 teaching card with the best tries')


def run(a, key):
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1][:200] if out else r.returncode)
    if r.returncode:
        print(out[:2500])
    return r.returncode


E = {
    'e01-harm-1': ('harm', 'paragraph', 'panel-b01-harm-1', 'AI', 0.25,
                   ['To lead them back to not hurting anyone, start from what they believe, like the lines below do by '
                    'saying God is in everyone.'],
                   ["they might think you're okay with them doing it"],
                   ('d01 (bce7e4bf) read Human Medium 20, AI Medium 24, AI High 37; the AI High window over the two '
                    'mistakes stayed at 37 words through b01, c01 and d01 while the arguing sentence changed twice; its '
                    'other half, the panel\'s agreed "they might hear it as permission" (a hedged, tidy twist; permission '
                    'to do what?), never changed. This try changes only that tail, within 20% of c01 (lesson 19b). Better: '
                    'the 37-word window Human; Human High in every window is the bar'),
                   ('payoff: the changed sentence still leads with what the reader gets, the mistake ("if you nod along as '
                    'if hurting someone could be spiritually fine"), and now ends on what the friend takes from it, said '
                    'plainly; join: none, the two mistakes stay two sentences; plain: "they might hear it as permission" '
                    'said as "they might think you\'re okay with them doing it"')),
    'e02-touch-1': ('touch', 'pair', 'panel-b02-touch-1', 'AI', 0.3,
                    ["Be honest with yourself about why you want to touch them, and hold off if it's mostly to calm "
                     "yourself down."],
                    ['Pulling away or freezing means stop too'],
                    ('c02 (0f63c962) read AI Low over every window (34, 38, 57 words), with five sentences built as "if X, '
                     'Y" (his way 2); this try builds them differently and fixes the three reads\' marks ("In that state", '
                     '"say it", "whatever they say"). Better: any window Human; Human High in every window is the bar'),
                    ('payoff: "Even a hug can be too much" now leads its sentence, the state after it; "Pulling away or '
                     'freezing means stop too" leads with the sign and what it means; "Ask again whenever" leads with the '
                     'act; join: the motive check and what it finds joined ("and hold off if it\'s mostly to calm yourself '
                     'down"); plain: "In that state" as "when they\'re already overwhelmed", "say it" as "tell you to '
                     'stop", "whatever they say" as "even if they ask you to"')),
    'e03-demons-4': ('demons', 'pair', 'panel-b03-demons-4', 'AI', 0.35,
                     ['Leave the demon talk until they can think straight again.'],
                     ['Turn the lights down, and get them a doctor if they need one.'],
                     ('d03 (bcf53335) read Human High 34 (the first paragraph), AI Medium 35 (the third sentence), AI Low '
                      '10 (the last); the third sentence packs who, why, getting steady, the lights and the doctor (way 1, '
                      'marked by both reads against his fixes); this try says the lights and the doctor as their own '
                      'clauses, the change h59 named as next. Better: the third sentence Human; Human High in every window '
                      'is the bar'),
                     ('payoff: the condition still leads the third sentence (when to set the advice aside), and the new '
                      'fourth leads with the act ("Turn the lights down"), the doctor after it; join: none; plain: "with '
                      'the lights turned down and a doctor if they need one" said as two acts, "Turn the lights down, and '
                      'get them a doctor if they need one"')),
}


def predict_e(key):
    lin, scope, panel, call, chance, tells, human, diag, first = E[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', LINEAGE[lin], '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', 'h60e',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC,
         '--diagnosis', diag,
         '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--panel', H59 + '%s/PANEL.md' % panel,
         '--humanized', 'lesson 19b from the near miss: the next word or two a reader could take two ways, one change a check',
         '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    return run(a, key)


if __name__ == '__main__' and sys.argv[1:2] == ['e']:
    for k in sys.argv[2:] or list(E):
        predict_e(k)


# Batch h60f: harm and demons at try 6 of 6, touch at try 5 of 6.
DEC_F = ('whether this try lifts the unit to Human High by itself: if so it goes into the guide in place of the unit '
         '(apply_gate.py); if not, and it is the lineage\'s sixth try, the unit goes to his marking page as a round-45 '
         'teaching card with the best tries, the same turn')
F = {
    'f01-harm-1': ('harm', 'paragraph', 'panel-b01-harm-1', 'AI', 0.3,
                   ['Arguing can make them dig in to prove they\'re God, so don\'t tell them "No you\'re not" or "That\'s '
                    'delusional."'],
                   ["If you nod along, they might think you're okay with them hurting someone."],
                   ('e01 (373f11b3) read Human Medium 20, AI Low 24, AI High 41: the near miss c01\'s two small tries '
                    '(d01, e01) left the window over the two mistakes AI High (37 to 41 words), whichever half changed. '
                    'This, the lineage\'s last try, fixes at once what the reads and the panel marked: S2\'s unnamed '
                    'belief and lines (both reads of e01), the parenthesis of lines and the pair\'s build (the panel on '
                    'b01), the first sentence as it is. Better: the two mistakes\' window Human; Human High in every '
                    'window is the bar'),
                   ('payoff: the second sentence leads with what the reader gets ("To lead them back to not hurting '
                    'anyone"); the arguing sentence now leads with what arguing does, the lines not to say after it; '
                    'the last leads with the act and what it does; join: none, the two mistakes stay two sentences, '
                    'each built its own way; plain: "the lines below do by saying God is in everyone" said as "like the '
                    'script below does: God is in everyone, so every body is sacred", the parenthesis said in the '
                    'sentence, "hear it as permission" as "think you\'re okay with them hurting someone"')),
    'f02-touch-1': ('touch', 'pair', 'panel-b02-touch-1', 'AI', 0.3,
                    ['Ask again whenever you can\'t tell what they want.'],
                    ['ask yourself whether the touch is for them or for you'],
                    ('e02 (043b2d5d) read the lineage\'s first Human window (Human Low 25, the asking) and AI Low and '
                     'Medium elsewhere; its AI Medium window (32 words) was "Ask again whenever ... Be honest with '
                     'yourself about why you want to touch them, and hold off if it\'s mostly to calm yourself down". '
                     'This try, within 20% of e02, says the motive check as the question the helper asks, with its two '
                     'answers named, and what it can find as its own sentence. Better: that window Low or Human; Human '
                     'High in every window is the bar'),
                    ('payoff: "Before you touch them" leads, then the question; "If it\'s mostly to calm yourself down, '
                     'hold off" leads with what the check finds; join: e02\'s joined motive sentence split in two, one '
                     'step each; plain: "Be honest with yourself about why you want to touch them" said as "ask yourself '
                     'whether the touch is for them or for you"')),
    'f03-demons-4': ('demons', 'pair', 'panel-b03-demons-4', 'Human', 0.55,
                     ['Once they can think straight again, you can teach them to send the demon love.'],
                     ['Turn the lights down, and get them a doctor if they need one.'],
                     ('e03 (d5484803) read Human Written: Human High 70, Human Medium 10 ("Leave the demon talk until '
                      'they can think straight again."), where "the demon talk" could be any talk of demons or the advice '
                      'to send it love. This try says what waits, "teach them to send the demon love", the rest as e03. '
                      'Better: Human High in every window'),
                     ('payoff: the condition leads the last sentence (when), then the act; join: none; plain: "the demon '
                      'talk" said as "teach them to send the demon love"')),
}


def predict_f(key):
    lin, scope, panel, call, chance, tells, human, diag, first = F[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', LINEAGE[lin], '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', 'h60f',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_F,
         '--diagnosis', diag,
         '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--panel', H59 + '%s/PANEL.md' % panel,
         '--humanized', ('the near miss\'s small tries spent: the reads\' and the panel\'s marks fixed at once'
                         if key == 'f01-harm-1' else
                         'lesson 19b from the near miss: the next word or two a reader could take two ways, one change a check'),
         '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    return run(a, key)


if __name__ == '__main__' and sys.argv[1:2] == ['f']:
    for k in sys.argv[2:] or list(F):
        predict_f(k)


# g02: touch's last try (6 of 6), from f02 (df0baed1), one change.
G = {
    'g02-touch-1': ('touch', 'pair', 'panel-b02-touch-1', 'AI', 0.25,
                    ['Ask again whenever you can\'t tell what they want.'],
                    ['If they pull away or freeze, that means stop too'],
                    ('f02 (df0baed1) read Human Low 25 (the asking), AI Low 12, AI Low 38, AI Medium 53 (from "Pulling away '
                     'or freezing ..." to "... hold off."), AI Low 13. The reads against his fixes on e02 and f02 both '
                     'marked "Pulling away or freezing" as having nobody\'s name on it: this try names it and says what it '
                     'means ("If they pull away or freeze, that means stop too"), within 20% of f02. Better: the 53-word '
                     'window Low or Human; Human High in every window is the bar'),
                    ('payoff: the sign leads its sentence, then what it means ("that means stop too"), the reason after; '
                     'join: none; plain: "Pulling away or freezing means stop too" said as "If they pull away or freeze, '
                     'that means stop too"')),
}


def predict_g(key):
    lin, scope, panel, call, chance, tells, human, diag, first = G[key]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', LINEAGE[lin], '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', 'h60g',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_F,
         '--diagnosis', diag,
         '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--panel', H59 + '%s/PANEL.md' % panel,
         '--humanized', 'lesson 19b from the near miss: the next word or two a reader could take two ways, one change a check',
         '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    return run(a, key)


if __name__ == '__main__' and sys.argv[1:2] == ['g']:
    for k in sys.argv[2:] or list(G):
        predict_g(k)
