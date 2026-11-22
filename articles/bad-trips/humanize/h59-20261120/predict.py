#!/usr/bin/env python3
"""predict.py - turn 51's predictions (pangram_ledger.py predict), written before each batch's checks.

  python3 predict.py a      s01 (his round-44 section with one word read his way) and every unit of build.py, as the
                            guide has it (--unchanged); each unit's call, chance and tells from the windows its blocks
                            showed in their newest checks (../h57-20261119/STATUS.json)
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h59-20261120/'
DET = "Pangram web app (his account, Pangram Professional), in the desktop app's browser pane"
DEC_A = ("whether it needs a lesson-19b fix: below High by itself, it is the near miss the next try starts from; Human High "
         "in every window by itself, it stays as it is")
sys.path.insert(0, str(HERE))
import build as BD  # noqa: E402


def run(a, key):
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1][:160] if out else r.returncode)
    if r.returncode:
        print(out[:1500])


def guess(ids):
    rows = [r for i in ids for r in BD.BELOW.get(i, [])]
    ai = [r for r in rows if r['status'].startswith('AI')]
    hum = [r for r in rows if r['status'].startswith('Human')]
    call = 'AI' if len(ai) * 2 >= len(rows) and ai else 'Human'
    chance = 0.3 if call == 'AI' else 0.55
    tells = [(ai or rows)[0]['s']] if rows else []
    human = [hum[0]['s']] if hum else []
    why = '; '.join(sorted({'%s %s' % (r['status'], (r.get('link') or '').rsplit('/', 1)[-1][:8]) for r in rows}))
    return call, chance, tells, human, why


def predict_s01():
    ids, scope, what = BD.UNITS['s01-shadow-section']
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips Dealing With Shadow Thoughts, his round-44 section in place (h59)', '--scope', 'section',
         '--text', REL + 'TEST-s01-shadow-section.txt', '--key', 's01-shadow-section', '--batch', 'h59a',
         '--call', 'Human', '--chance', '0.8', '--detector', DET,
         '--decides', ('whether "we re-identify" (his "we re-identifying" read his way) keeps his section Human High; if not, '
                       'his own word goes back and the card asks him'),
         '--diagnosis', ('his check ab6720fc read this section Human High 370 with "we re-identifying"; one word read his '
                         'way, nothing else changed'),
         '--his', ('his own: Dealing With Shadow Thoughts, his round-44 version (review/r44/ANSWERS-R44-20261120-1353.json), '
                   'with "we re-identifying as the gold-panners" read as "we re-identify as the gold-panners"'),
         '--human-tells', 'like water flowing over rocks', '--tells', 'the best, truest, loveliest, most skillful thoughts']
    run(a, 's01-shadow-section')


def predict_a(key):
    ids, scope, what = BD.UNITS[key]
    call, chance, tells, human, why = guess(ids)
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h59)' % what, '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', 'h59a',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_A,
         '--diagnosis', ('its blocks\' newest windows below High (STATUS.md): %s. Checked by itself as the guide has it, '
                         'before any change (lesson 19b: the near miss to start from)' % why),
         '--unchanged', what]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    run(a, key)


if __name__ == '__main__':
    if sys.argv[1:2] == ['a']:
        keys = sys.argv[2:] or list(BD.UNITS)
        for k in keys:
            predict_s01() if k == 's01-shadow-section' else predict_a(k)


# Batch h59b: the first fixes of four units that read AI High over every word by themselves in h59a (no Human window
# to start from, so lesson 19b's near-miss rule has nothing to work from); each written in his ways first, read by the
# three fresh readers, and their marks fixed (reads/, TEST-KEY.receipt.json).
DEC_B = ('whether this first fix in his ways reads Human High by itself: if so it goes into the guide in place of the '
         'unit; if not, its Human windows are the near miss the next try starts from (lesson 19b)')
B = {
    'b01-harm-1': ('a06-harm-1', 'AI', 0.35, ['take it as a sign that someone could get hurt'],
                   ["can turn things into a fight over who's right"],
                   ('payoff: the sign it is comes first, then what to do (start from what they believe, like the lines '
                    'below), then the two mistakes with what each leads to; join: the old rule-pair said as what each '
                    'mistake can do; plain: "status fight" as "a fight over who\'s right", "non-harm" as "not hurting '
                    'anyone", "safety signal" as "a sign that someone could get hurt"'),
                   'a06 (4d379486) read AI High over all 54 words'),
    'b02-touch-1': ('a15-touch-1', 'AI', 0.35, ['Sometimes the best support is to sit six feet away and stay silent.'],
                    ['If they say stop, stop'],
                    ('payoff: ask first, with the question, then why (a hug can be too much, holding down an attack), '
                     'then the six-feet answer, when to stop, the helper\'s reasons; join: "nonsexual, consensual, and '
                     'unrelated to the helper\'s needs" joined into checking your own reasons; plain: "compassion does '
                     'not mean grabbing, hugging, restraining, stroking, or crowding" as what a hug and holding down can '
                     'feel like'),
                    'a15 (45accf90) read AI High over all 64 words'),
    'b03-demons-4': ('a19-demons-4', 'AI', 0.3, ['help them get steady first, with the lights down and a doctor if they '
                                                  'need one'],
                     ['save the demon philosophy for later'],
                     ('payoff: the first sentence is his pinned move and leads with the payoff already ("this is how you '
                      'become unhookable"); the second now leads with what love does ("the demon has nothing to hook '
                      'into"), the reason after it; the third leads with when it applies; join: the four-item list said as '
                      'one picture, hooks that catch on hatred and fear; plain: "medically, physically, or '
                      'psychologically" as "sick or too scared to think straight", "nondual demonology" as "the demon '
                      'philosophy"'),
                     'a19 (5d8b8a34) read AI High over all 68 words'),
    'b04-spirit-2': ('a22-spirit-2', 'AI', 0.4, ['Practice says love is here too, so we take care of that person.'],
                     ['the person shaking in the corner'],
                     ('payoff: bypassing defined in the sentence that names it; practice leads with what it does, its steps '
                      'after; join: the five-part list split into the care and the honesty; plain: "an ultimate view" as '
                      '"a big spiritual truth", "make the room safer" as dimming the lights and clearing away what they '
                      'could get hurt on, "hold the experience without becoming it" as the feeling being allowed to move '
                      'through'),
                     'a22 (91088c1e) read AI High over all 64 words'),
}


def predict_b(key):
    base, call, chance, tells, human, first, diag = B[key]
    ids, scope, what = BD.UNITS[base]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h59)' % what, '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', 'h59b',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_B,
         '--diagnosis', ('%s, no Human window to start from. This try is a first fix in his ways (his_fixes_brief.md), '
                         'with the three fresh reads\' marks fixed (reads/%s). Better: Human High in every window'
                         % (diag, key)),
         '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--humanized', 'his eleven ways first (payoff first in every sentence, lesson 20c), then the fresh reads\' marks',
         '--first-fix', first,
         '--big-change', ('%s: no Human window to start a small fix from, so this is the first fix in his ways, not a '
                          'retry of a near miss' % diag)]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    run(a, key)


if __name__ == '__main__' and sys.argv[1:2] == ['b']:
    for k in sys.argv[2:] or list(B):
        predict_b(k)


# Batch h59c: the second tries, after the tell panels on the first (panel-b0N-*/PANEL.md). c01 and c03 start from their
# near misses (b01 5daecc97, b03 84881428: Human Low windows) and change what a reader could take two ways, under the
# ledger's 20% (lesson 19b); c02 is a new wording, since b02 read AI over every word, as a15 did.
DEC_C = ('whether the words the panel and the reads marked, changed, lift the unit to Human High by itself: if so it goes '
         'into the guide; if not, the windows show which part to fix next')
C = {
    'c01-harm-1': ('a06-harm-1', 'b01-harm-1', 'AI', 0.4, ['Start from what they believe and lead them back to not hurting '
                                                            'anyone'],
                   ["dig in to prove they're God"],
                   ('payoff: unchanged order (the sign first, what to do, the mistakes), each changed sentence already leads '
                    'with what the reader gets from it: "take it as a sign they could really hurt someone" leads with the '
                    'sign; join: none, the last sentence\'s split waits a check (lesson 19b); plain: "someone could get '
                    'hurt" said as "they could really hurt someone", "turn things into a fight over who\'s right" as "dig '
                    'in to prove they\'re God", "when they say" (the friend, or the lines?) as "by saying"'), None),
    'c02-touch-1': ('a15-touch-1', 'b02-touch-1', 'AI', 0.4, ['Be honest with yourself about why you want to touch them.'],
                    ['If they pull away or freeze, stop then too'],
                    ('payoff: each sentence opens on what to do or what can happen (ask, a hug can be too much, stop, ask '
                     'again, hold off); join: none needed, the reads asked for the packed sentences to be split, and each '
                     'of the panel\'s agreed sentences is said a new way; plain: "the best support is to sit six feet away '
                     'and stay silent" as "sit about six feet away and only talk if they want to", "say so" as "say '
                     'stop", "anything sexual in it" as "Never touch them in a sexual way, whatever they say"'),
                    ('b02 (cdb4b340) and a15 (45accf90) read AI High over every word, with no Human window to start a '
                     'small fix from; the tell panel agreed on four of five sentences, each said a new way')),
    'c03-demons-4': ('a19-demons-4', 'b03-demons-4', 'AI', 0.4, ['help them get steady first, with the lights down and a '
                                                                  'doctor if they need one'],
                     ['Leave the demon talk until they can think again.'],
                     ('payoff: the first sentence is his pinned move and already leads with the payoff ("this is how you '
                      'become unhookable"); the changed ones lead with what love does and when to set it aside, as '
                      'before; join: the closer split off into its own sentence, as the read against his fixes asked; '
                      'plain: "reach love" said as "send love", the section\'s own words, "things like hatred and fear" '
                      'as "hatred and fear", "save the demon philosophy for later" as "Leave the demon talk until they can '
                      'think again"'), None),
}


def predict_c(key):
    base, prev, call, chance, tells, human, first, big = C[key]
    ids, scope, what = BD.UNITS[base]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h59)' % what, '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', 'h59c',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_C,
         '--diagnosis', ('%s read below High (RESULTS-h59b.json); the tell panel agreed on its sentences (panel-%s/PANEL.md); '
                         'this try fixes what they and the three fresh reads marked (reads/*-%s.txt). Better: Human High in '
                         'every window' % (prev, prev, key)),
         '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--panel', REL + 'panel-%s/PANEL.md' % prev,
         '--humanized', ('lesson 19b from the near miss, a word or two a reader could take two ways' if not big else
                         'a new wording in his ways, the panel\'s agreed tells and the reads\' marks fixed'),
         '--first-fix', first]
    if big:
        a += ['--big-change', big]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    run(a, key)


if __name__ == '__main__' and sys.argv[1:2] == ['c']:
    for k in sys.argv[2:] or list(C):
        predict_c(k)


# Batch h59d: the third small tries. d01 from c01 (166c0ee5, its best near miss): the last sentence split as the read
# against his fixes asked, and the second sentence's payoff first (his Hunter fix, lesson 20c). d03 within 20% of b03
# (84881428, the lineage's best near miss by likelihood): "maybe" out, "the lights turned down", "think straight again".
D = {
    'd01-harm-1': ('a06-harm-1', 'c01-harm-1', 'b01-harm-1', 'AI', 0.4,
                   ["And if you nod along as if hurting someone could be spiritually fine, they might hear it as permission."],
                   ['To lead them back to not hurting anyone, start from what they believe'],
                   ('payoff: "To lead them back to not hurting anyone, start from what they believe" now leads with what '
                    'the reader gets, the means after (lesson 20c); join: the two mistakes split into two sentences, as the '
                    'read against his fixes asked; plain: the words of c01 kept, nothing new added')),
    'd03-demons-4': ('a19-demons-4', 'c03-demons-4', 'b03-demons-4', 'AI', 0.45,
                     ['help them get steady first, with the lights turned down and a doctor if they need one'],
                     ['Leave the demon talk until they can think straight again.'],
                     ('payoff: none moved, and each changed sentence already leads with what the reader gets from it: the '
                      'third with when to set the advice aside, the fourth with what waits; join: none, the third '
                      'sentence\'s split waits a check (lesson 19b); plain: "maybe because" said as "because", "the lights '
                      'down" uncompressed to "the lights turned down", "think again" as "think straight again", matching '
                      '"too scared to think straight"')),
}


def predict_d(key):
    base, prev, panel, call, chance, tells, human, first = D[key]
    ids, scope, what = BD.UNITS[base]
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', 'bad-trips %s (h59)' % what, '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', 'h59d',
         '--call', call, '--chance', str(chance), '--detector', DET, '--decides', DEC_C,
         '--diagnosis', ('%s read below High (RESULTS-h59c.json); this try changes a word or two from the near miss, what the '
                         'panel (panel-%s/PANEL.md) and the reads (reads/*-%s.txt) marked. Better: Human High in every '
                         'window' % (prev, panel, key)),
         '--receipt', REL + 'TEST-%s.receipt.json' % key,
         '--panel', REL + 'panel-%s/PANEL.md' % panel,
         '--humanized', 'lesson 19b from the near miss, a word or two a reader could take two ways',
         '--first-fix', first]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    run(a, key)


if __name__ == '__main__' and sys.argv[1:2] == ['d']:
    for k in sys.argv[2:] or list(D):
        predict_d(k)
