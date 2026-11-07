"""r21's check texts in the romance article (2026-11-07), each linted before its check (gate bad-trips-2026-11-07h).

Joel's marking-page answers (22:57 UTC, ../../../../review/teach-20261107/ANSWERS-T1.json) gave his own versions of S2
(the monk paragraphs, 60 to 62) and S17 (Kim Anami and the Keenes, 309 to 312). Each read Human, High by itself in his
account. They go in as he wrote them, with one change of mine: "you're attention" to "your attention" (his apostrophes
stay as he typed them; the linter's O62 prefers straight ones anyway). Then the lessons from them (docs/lessons/2026-11-07-2257-romance.md) on the three
stretches that kept reading AI the way S2 did:
- Jealousy 367 to 369: the stacked adjectives ("foundational, permanent, exclusive romantic partnership") and abstract
  nouns ("an inability to connect deeply", "a lack of self-control", "the self-development") said as plain, idiomatic
  things a person does ("promise to be each other's one and only forever", "can't keep it in their pants").
- Romance 285 to 287: each list ("softness, helplessness, or cuteness"; "too emotional, too difficult, not logical enough,
  or too needy"; "help, lead, or give her pleasure") said as particular things, built differently; the parallel
  "I might ask ... because ..., and she might ask ... because ..." broken; "When a strong woman surrenders, she is
  choosing to, which is sexy." and the Toft sentence (High) kept word for word.
- Idealization 148: its list ("public accusations, rewriting the whole past and treating every flaw as proof") said in
  two sentences built differently; its last sentence (his punchline) kept.
Each stretch goes with the paragraph before and after it, unchanged (E349)."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LIVE = {int(k): v.strip() for k, v in json.loads((HERE / 'LIVE.json').read_text(encoding='utf-8')).items()}
ANS = json.loads((ROOT / 'articles/romance/review/teach-20261107/ANSWERS-T1.json').read_text(encoding='utf-8'))
R20 = (HERE.parent.parent / 'r20' / 'checks' / 'CHECK-r20-spir304.txt').read_text(encoding='utf-8').rstrip('\n')


def his(item_id):
    """His version from the marking page, one paragraph per line, with the one change of mine named above."""
    t = next(i for i in ANS['items'] if i['id'] == item_id)['your_version']
    t = t.replace("you're attention", 'your attention')
    return [x.strip() for x in t.split('\n') if x.strip()]


S2 = his('TEACH-MONASTIC-PERKS')       # 60, 61, 62
S17 = his('TEACH-KIM-ANAMI')           # 309, 310, 311, 312
assert len(S2) == 3 and len(S17) == 4, (len(S2), len(S17))
R20_PARAS = R20.split('\n\n')          # 304', 305', 306', 307, 308, 309 (live)
assert R20_PARAS[-1] == LIVE[309] and R20_PARAS[3] == LIVE[307] and R20_PARAS[4] == LIVE[308]

NEW = {
    367: 'I’d rather be able to mention any attraction casually, including the little ones that don’t mean '
         'anything. If you’re '
         'only supposed to bring up the serious ones, every time you do it turns into a whole sit-down talk, so people '
         'mostly just keep quiet.',
    368: 'Lots of couples promise to be each other’s one and only forever, and way fewer of them pull it off. In '
         'a polyamorous relationship the boundaries might be more negotiable, but then you actually have to do the '
         'negotiating.',
    369: 'Polyamory can be just as dishonest, though, and these days I think a lot of people use it because going deep '
         'with one person is more than they can handle. Or it’s their way of admitting they can’t keep it in their pants, '
         'without necessarily doing the work on themselves that would make the whole arrangement ethical. If you can’t do '
         'monogamy, it’s still more honest to just say so than to fake it. Sometimes all that pretending does more damage '
         'than the other relationship ever would have.',
    285: 'The same is true for a woman. She shouldn’t have to play the damsel every minute, pretending she can’t open a '
         'jar, just to prove she’s feminine. Her surrender means a lot more when she could take charge but just doesn’t '
         'feel like it right then. When a strong woman surrenders, she is choosing to, which is sexy.',
    286: 'Women can get pulled in two directions here. She may worry that I don’t find her beautiful enough, or that '
         'she’s too much of a handful. Maybe she thinks she cries too easily and needs too much, and that I’d like her '
         'better if she were more logical. Then she can swing the other way and act like she needs nobody. Letting a man '
         'take care of her starts to feel like weakness, and so does letting him lead.',
    287: 'Toft says that after fifty years he still tells his wife she’s beautiful, including finding new kinds of beauty '
         'as she ages. Anami talks a lot about women learning to receive. Letting a man help her, or lead for a while, leaves '
         'a strong woman just as strong. So does lying back while he pleases her. And a man she takes care of stays a grown '
         'man. Sometimes it’s as simple as a woman who drives just fine asking '
         'me to drive, because she likes how it feels when I do. She’s choosing the ride. Or I might ask, “Honey, how do '
         'you see this intuitively?” because I want her to use her power. She might have me think through the practical '
         'side with her, since that’s the part she wants from me.',
    148: 'Once the BPD splitting kicks in, a woman who worshipped me can start hating me in private. Then come the public '
         'accusations. She rewrites our whole history, and every flaw she finds is suddenly a sign that I was fake '
         'all along. Sometimes the woman who thought I was perfect later accuses me of thinking I’m perfect.',
}


def join(paras):
    return '\n\n'.join(paras)


TEXTS = {
    # The section "Spirituality to bypass intimacy", 53 to 62: the live post's 53 to 59, then his S2.
    'r21-bypass': join([LIVE[i] for i in range(53, 60)] + S2),
    # The section "Can making love be a spiritual practice?", 304 to 317 as #45 had it: r20's 304 to 308 (read Human,
    # High by themselves, #115), his S17 for 309 to 312, then the live post's twin-flame paragraphs 313 to 317 (the h1
    # "Twin Flames?" before 313 left out, as in #45).
    'r21-spir': join(R20_PARAS[:5] + S17 + [LIVE[i] for i in range(313, 318)]),
    # Jealousy 366 to 370: the live 366 and 370 around the new 367 to 369.
    'r21-jeal366': join([LIVE[366], NEW[367], NEW[368], NEW[369], LIVE[370]]),
    # Romance 284 to 288: the live 284 and 288 around the new 285 to 287.
    'r21-rom284': join([LIVE[284], NEW[285], NEW[286], NEW[287], LIVE[288]]),
    # Idealization 147 and 148: the live 147 with the new 148 (148 alone is under the web app's 50 words).
    'r21-ideal147': join([LIVE[147], NEW[148]]),
}
# Which live paragraphs each text replaces, for the fixed version (../../whole/assemble.py).
REPLACES = {60: S2[0], 61: S2[1], 62: S2[2], 309: S17[0], 310: S17[1], 311: S17[2], 312: S17[3], **NEW}

if __name__ == '__main__':
    for k, v in TEXTS.items():
        print(k, len(v.split()), 'words')
