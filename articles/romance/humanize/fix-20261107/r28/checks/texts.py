"""r28's check texts (2026-11-08, after his whole-article check of 16:47 UTC, ../../r27/checks/RESULTS-whole-r27.json): the
one AI Low and seven Human Low windows that check showed, each a sentence of mine (or, for 334, the live post's), fixed
his way (gate E368; romance-2026-11-08b and c): the point first, the plain or particular word, short sentences joined, an
announcing opener cut, a slack ending. Each is checked in its section, as the fixed version has it; 331 and 334, whose
section is long and holds an owner lock, in the stretch 330 to 336."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
LEDGER = FIX.parent / 'pangram-ledger.jsonl'
PRED = {}
for line in LEDGER.read_text(encoding='utf-8').splitlines():
    d = json.loads(line)
    if d.get('type') == 'prediction':
        PRED[d['id']] = d


def check_text(pid):
    key = PRED[pid]['key']
    f = next(FIX.glob('*/checks/CHECK-%s.txt' % key))
    return f.read_text(encoding='utf-8').strip()


EDITS = {
    'r28-labels': ('romance-low-labels#84', [(
        'Here’s the funny thing many people don’t understand: labels don’t create commitment, but they can still expose '
        'whether two people think they’re in the same relationship, which matters a lot.',
        'Here’s the funny thing about labels: you can call someone your boyfriend or girlfriend for years and still have one '
        'foot out the door, but the word at least shows pretty fast whether you both think you’re in the same '
        'relationship.')]),
    'r28-deeper': ('romance-low-deeper#97', [(
        'I get why, since neither of us could believe one day in the wrong shoes could do that, but it still felt '
        'dismissive, like part of her just wanted my knee to be fine.',
        'I get it, neither of us could believe one day in the wrong shoes could do that, but it still felt like she was '
        'brushing me off because she wanted my knee to be fine.')]),
    'r28-bundling': ('romance-s6#30', [(
        'Well, it didn’t exactly solve the problem. In late-eighteenth-century New England, where lots of couples bundled, '
        '30–40 percent of brides were already pregnant on their wedding day, so it wasn’t a very reliable way to keep '
        'courtship nonsexual.',
        'Well, it didn’t exactly solve the problem: in late-1700s New England, where lots of couples bundled, 30–40 percent '
        'of brides were already pregnant on their wedding day.')]),
    'r28-ptsd': ('romance-low-ptsd#73', [(
        'That dynamic alone isn’t necessarily the main problem: a lot of women have seen me that way.',
        'A lot of women have seen me that way, and honestly that part can be fine.')]),
    'r28-dam': ('romance-low-dam#70', [(
        'Sometimes I actually learned something, and sometimes nothing changed except that now I’m attached, so the new '
        'certainty is just harder for me to question.',
        'Sometimes I actually learned something about her, but other times all that changed is I’m attached now, and that '
        'just makes me less likely to question it.')]),
    'r28-slow': ('romance-low-slow#96', [(
        'Touch or smell can feel wrong, or your desire levels or kinks don’t fit. Maybe one person is sexually shut down, '
        'or the bodies just don’t connect.',
        'Maybe their smell turns you off, or one of you wants it every day while the other is happy with once a month. Your '
        'kinks might not line up either, or one person is sexually shut down, or your bodies just don’t click.')]),
}
TEXTS = {}
for name, (pid, edits) in EDITS.items():
    t = check_text(pid)
    for a, b in edits:
        assert t.count(a) == 1, (name, a[:50])
        t = t.replace(a, b)
    TEXTS[name] = t

# 330 to 336: the live post's words (read from the post API, 2026-11-08), with 331 and 335 as the fixed version has them
# (S18 #25, S19 #32) and 331's and 334's Low sentences fixed.
LIVE = {
    330: 'Even if I found my twin flame, she’d still be one person. The polarity could be perfect and we’d still need other '
         'people around us.',
    332: 'Maybe an unusually strong couple can get away without much outside support. I think that’s rare. But often, a '
         'friend who actually knows us both sees the dysfunctional pattern before either of us does. On the other hand, If '
         'both people are falling apart, there is only so much anyone else can do.',
    333: 'Separate confidants can be helpful and harmful. Sometimes you need privacy from your partner and somewhere else to '
         'say what you’re feeling. But if your confidant doesn’t have a good connection with your partner, the conversation '
         'can turn into an echo chamber very easily.',
    334: 'Having the same confidant creates the opposite problem: now you may not have a release valve when you want '
         'privacy from your partner. There isn’t one perfect arrangement.',
    336: 'I lived all the permutations of this with Bee, except that we never lived in community. I suspect if we had, we '
         'might still be together. She would not have been capable of demonizing me when everyone already knew both of us '
         'and knew I wasn’t a narcissistic abuser. It would have contained all the insanity. Baseless accusations only work '
         'with friends who only know one side.',
}
REPL = json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8'))
S331 = REPL['331'][0].replace(
    'Let me show you how this looked for me. I’ve noticed in my own relationships that whenever a serious issue arises, both '
    'of us tend to turn to our separate circles of friends for support.',
    'Here’s how this looks for me: whenever something serious comes up in my relationships, we each run to our own '
    'friends for support.')
assert S331 != REPL['331'][0]
S334 = LIVE[334].replace(
    'now you may not have a release valve when you want privacy from your partner. There isn’t one perfect arrangement.',
    'now you may not have a release valve when you want privacy from your partner, so neither way is perfect.')
assert S334 != LIVE[334]
TEXTS['r28-pillars'] = '\n\n'.join([LIVE[330], S331, LIVE[332], LIVE[333], S334, REPL['335'][0], LIVE[336]])
NEW_PARAS = {'38': None, '72': None, '103': None, '157': None, '175': None, '181': None, '331': S331, '334': S334}

# r28-slow (#149) read 19.8% AI: AI Medium on my two "Maybe ... or ..." sentences (the list in any shape: #96's form read
# Low in his whole check), Human Low on the opener before them. The needed read found the second list sentence was more of
# the same; his fix for a list (cut to two particular items, #112) and a slack ending that ties back to the opener, joined
# to it: r28-slow-b.
OLD_SLOW = ('You can know somebody for twenty years and then discover on the first night that the polarity isn’t there. '
            'Maybe their smell turns you off, or one of you wants it every day while the other is happy with once a month. '
            'Your kinks might not line up either, or one person is sexually shut down, or your bodies just don’t click.')
NEW_SLOW = ('You can know somebody for twenty years and then discover on the first night that the polarity isn’t there: '
            'maybe their smell turns you off, or one of you wants it every day and the other once a month, and twenty years '
            'of talking would never have told you that.')
assert TEXTS['r28-slow'].count(OLD_SLOW) == 1
TEXTS['r28-slow-b'] = TEXTS['r28-slow'].replace(OLD_SLOW, NEW_SLOW)
