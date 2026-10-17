"""Section 13 draft v33 (2026-10-17): v32 with H2-P4 rewritten. Batch 314g read v32 Human in every changed paragraph alone and
in its first and land subsections, but the whole section read one AI window of 89 words, exactly H2-P4 ("Mostly Human
Written", 0.09), as v30 had (310g), though H2-P4 alone reads Human (312g, low). Its tells: "not just its public face", the four
published questions as a list and a run, "Then make a choice whether or not it functions in a way that is important to you",
and the neat callback closer. Joel, 2026-10-16 23:38 UTC: "that means it's all fairly borderline human. so we should fix it."
v33 keeps every published point (compare with how the group really behaves, not only what it says; the four questions; the
view will still be there after the uncomfortable conversation), with Emulate's "the view isn't going anywhere" (round j's call
B). Writes v33.md and v33-fixes.json. Run from this folder: python3 make_v33.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
OLD = ('When you have a good idea of what’s important to you, you can look at how a group actually functions, not just its '
       'public face. Find out how it handled its last conflict, and who can block a decision. How did leaving go for the last '
       'person who left? Who owns the land? Then make a choice whether or not it functions in a way that is important to you. '
       'It’ll be an uncomfortable conversation, but the view will still be there after you’ve had it.')
NEW = ('Once you know what matters to you, look past what the group says about itself to how it really works. A recent '
       'conflict is a good place to start: how did that get handled? There’s also who can block a decision, and what happened '
       'to the last person who left. (And who owns the land!) Then it comes down to whether that’s how you want to live. These '
       'are uncomfortable conversations, I know, but the view isn’t going anywhere!')
t = (HERE / 'v32.md').read_text(encoding='utf-8')
assert t.count(OLD) == 1
t = t.replace(OLD, NEW)
# the two repeats round r21's repeats check found a reader would most notice inside this section (review-r21/REPEATS.md, its
# list "The five repeats a reader would most notice", 1 and 2)
MORE = [
    ('H1-P3', 'and find out how much conflict the group can handle before you need a land surveyor.',
     'long before anyone needs a land surveyor.',
     'repeats r21 item 19 (most noticed): "a real conflict" first is H1-P2\'s, the paragraph before; H1-P3 keeps the land coming '
     'later'),
    ('H4-P8', "Do a trial run like that before anybody sells their house to move in. It won't show you anyone's soul, but it can "
              "show you whether your way of coordinating works.",
     "Do a trial run like that before anybody sells their house to move in. It'll show you whether your way of coordinating "
     "works.",
     'repeats r21 item 22 (most noticed): H4-P6\'s "no good person detector" and the faker (H4-P4) already say watching can\'t '
     'show who someone is; the trial run\'s own point stays'),
]
for pid, old_, new_, why in MORE:
    assert t.count(old_) == 1, pid
    t = t.replace(old_, new_)
(HERE / 'v33.md').write_text(t, encoding='utf-8')
(HERE / 'v33-fixes.json').write_text(json.dumps([{'id': 'H2-P4', 'old': OLD, 'new': NEW, 'why': (
    'batch 314g: the whole section read one AI window, exactly this paragraph (89 words); the tells named above, each '
    'replaced; every published point kept')}] + [{'id': p_, 'old': o_, 'new': n_, 'why': w_} for p_, o_, n_, w_ in MORE],
    ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v33.md')
