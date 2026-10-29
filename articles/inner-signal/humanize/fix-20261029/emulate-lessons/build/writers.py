"""Shape-coding of our own writers' versions with the same labels, for the comparison (step 5).
Batch 482: fresh writers with the current brief (no Pangram reading yet). Batch 472: Claude's six versions of the seam (all AI High)."""
from ex import J, T
from data1 import L, O

TG = 'fix-20261029/b482/TARGETS.json'
CH = 'fix-20261029/b482/CHOICES.json'
V = 'fix-20261029/b482/writers/VERSIONS-%s.json'

# (target, writer, v1 labels, v2 labels, Emulate's earlier version of the same words, if any)
CODES = [
    ('T1', 'W1', [L['split'], L['colon'], L['def'], L['notxy'], O['reason'], L['casual'], L['uneven']],
                 [L['colon'], L['notxy'], O['reason'], L['def'], L['order'], L['casual']],
     'reverse-X1.5: Emulate\'s plain instruction "Put this screen on the shelf and conduct the practice." read Human (High).'),
    ('T4', 'W1', [L['split'], L['casual'], L['hedge'], L['order'], L['people']],
                 [L['split'], L['casual'], L['subj'], O['conn']],
     'b479-S2: Emulate\'s "So, I came up with the idea of constructing a bridge – a temporary fix – ..., if I can put it that way." read Human (High); the writers made the same first-person, came-up-with move but kept tidy sentences, no dashes, brackets or self-conscious hedge.'),
    ('T7', 'W1', [L['def'], L['people'], L['split'], L['quip_out']],
                 [L['def'], L['people'], L['quip_out'], L['casual']],
     'reverse-X5.3: Emulate had dropped the definition and kept only the instruction (Human High).'),
    ('T10', 'W1', [L['casual'], L['order'], O['tight']],
                  [L['order'], O['reason']],
     None),
    ('T13', 'W1', [L['casual'], O['minimal'], O['tight']],
                  [L['casual'], 'other: afterthought tag added ("not until ...")'],
     None),
    ('T16', 'W1', [L['split'], L['notxy']],
                  [L['order'], L['casual']],
     'reverse-X10.7: Emulate\'s shorter "Let that experience inform what you OPEN yourself up to." read Human (High).'),
    ('T2', 'W2', [L['colon'], L['split_list'], L['people'], L['hedge'], L['casual'], O['poly'], O['loose']],
                 [L['colon'], L['people'], O['poly'], L['split']],
     'reverse-X1.11: Emulate dropped the list ("It\'s got to lead somewhere!", Human High); the writers kept every outcome, as things people do, without the colon.'),
    ('T5', 'W2', [L['split'], L['def'], L['uneven']],
                 [L['join'], O['poly'], L['hedge'], O['etc'], O['loose']],
     'fail-41-emu-bf-ones: this flagged line is Emulate\'s own (High three times, then AI Low).'),
    ('T8', 'W2', [L['subj'], L['people'], L['split'], L['notxy']],
                 [L['split'], L['subj'], L['people']],
     None),
    ('T11', 'W2', [L['people'], L['subj'], L['casual']],
                  [L['people'], L['subj'], L['casual']],
     'b481-S32: Emulate\'s "An Ethical Double Bind Question gives someone a choice between two genuinely safe things to do." read Human (High): the writers made the same move.'),
    ('T14', 'W2', [L['quip_out'], L['notxy'], L['split'], L['casual'], O['loose']],
                  [L['quip_out'], L['notxy'], L['casual'], O['loose']],
     '40-refix-HG33-quip and reverse-X9.10: Emulate dropped the joke (Human High).'),
    ('T17', 'W2', [O['aside'], L['split'], L['casual']],
                  [L['split'], L['casual']],
     'reverse-X11.13: Emulate\'s short "Autonomous: write whatever you get." read Human (High). The writers took the brackets OUT (Emulate usually puts lists into them).'),
    ('T3', 'W3', [L['colon'], L['order'], L['first'], O['tight']],
                 [L['colon'], L['first'], O['conn'], L['casual'], L['order']],
     '40-HG12-outside: Emulate dropped this closing claim altogether.'),
    ('T6', 'W3', [L['split'], L['notxy'], L['casual']],
                 ['other: conditional "If you..." opening added', O['poly'], O['etc'], L['casual'], O['loose']],
     'reverse-X4.6: Emulate\'s version had no examples ("You can borrow qualities, but ...", Human High).'),
    ('T9', 'W3', [L['def'], L['people'], L['notxy'], L['order'], L['casual']],
                 [L['def'], L['notxy'], L['split'], L['casual'], L['uneven']],
     'reverse-X8.4: Emulate dropped the definition (Human High).'),
    ('T12', 'W3', [L['colon']],
                  [L['colon'], O['conn']],
     None),
    ('T15', 'W3', [L['split'], L['casual']],
                  [L['split'], L['casual']],
     'fail-41-br-fix: the flagged words are Emulate\'s (br); both versions keep the permission formula "You don\'t (need to/have to) fix it."'),
    ('J1', 'W4', [O['minimal']],
                 [O['minimal'], O['formal']],
     'b481-S31: Emulate\'s "You may have fooled yourself in the past" reached only Medium.'),
    ('J2', 'W4', [L['join'], O['runon']],
                 [L['first'], L['hedge'], L['casual']],
     'b479-S4: Emulate joined these two sentences into one run-on instruction (Human High twice); v1 makes the same join.'),
    ('J3', 'W4', [O['q2s'], L['quip_out']],
                 [O['q2s'], L['order'], L['casual']],
     'b479-S5: Emulate turned the question into "If you can\'t do this in a loving way today, just ..." (Human High); v2 has the same shape.'),
    ('J4', 'W4', [O['poly']],
                 [O['signpost_out'], O['direct'], O['poly'], L['casual']],
     'b479-S6: Emulate made it a direct question (Human High twice); neither version uses a question.'),
]


def entries():
    tg = {t['id']: t for t in __import__('json').loads(open(str(__import__('ex').H / TG)).read())['items']}
    ch = __import__('json').loads(open(str(__import__('ex').H / CH)).read())
    E = []
    for tid, w, l1, l2, emu in CODES:
        i = [t['id'] for t in tg.values()].index(tid)
        for v, labs in (('v1', l1), ('v2', l2)):
            E.append(dict(id='b482-%s-%s' % (tid, v), batch='482', writer=w, target=tid,
                          where=tg[tid]['where'], reading_of_flagged='; '.join(tg[tid]['readings']),
                          flagged=J(TG, 'items/%d/flagged_stretch' % i), version=J(V % w, '%s/%s' % (tid, v)),
                          picked=(ch.get(tid, {}).get('pick') == v), labels=labs, emulate_earlier=emu or ''))
    return E


# Batch 472: Claude's versions of the seam, every one AI (High) through the API (API-CHECKS.md); Emulate's re-run bj passed.
SEAM = [  # key in b472/CANDIDATES.json, labels; every one read AI (High) through the API
    ('b472_s2b', [L['casual'], O['direct'], O['ifrun'], O['tight']]),
    ('b472_s2c', [L['casual'], O['direct'], O['closer_in'], O['tight']]),
    ('b472_s2e', [L['casual'], L['split'], L['quip_in'], O['closer_in'], O['ifrun']]),
    ('b472_s2f', [L['casual'], L['join'], L['quip_in'], L['concrete'], L['order'], O['ifrun']]),
]
