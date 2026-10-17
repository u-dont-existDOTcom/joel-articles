"""Section 15 draft v6 (2026-10-17, after batch 326g): v5 with the two paragraphs that read AI alone rebuilt from Emulate round
d (emu-d/out/, byte for byte from the laptop, sha256 checked), round r4's fixed meaning inside Emulate's sentences.
- H1-P4 (v5 0.63): variant a keeps the published sentence in d01 call A's loose shape ("go through ... and through local
  memory, along with the formal systems", "when all it takes is some aunt giving three people a task?"); variant c is d02 call
  B's ("so much is taken care of by the extended family and the memory of the people there", its "Whether it's ..." fragment).
  Emulate's slips stay out: "where I've mostly lived" (he has spent time around them), "most of the things people usually look
  to institutions for", "wherever villages or extended families exist on earth", "all take care of each other".
- H3-P2 (v5 0.49): d03 call B's sentences ("But these days ...", "People have a lot less communal life, but still carry the
  obligation", "How can they get ahead, when ...?"), with the published communal life that held the obligation up, "can"
  (B: "often"), the relatives who stay dependent because the payments give them no real alternative, and the ethic that can
  keep people alive while it eats at both sides, all of which B dropped ("can X and still Y" is Joel's tell, O17). Variant l adds the published list of what is no longer
  fully shared.
CHOICE picks the variants for v6.md (default a and plain); every variant goes to Pangram (327g). Writes v6.md and
v6-variants.json. Run from this folder: python3 make_v6.py [H1-P4 choice] [H3-P2 choice]"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'emu-d' / 'out'
for k, h in {'d01-emuA': 'c8794bccc29c', 'd02-emuB': '4eb93811e807', 'd03-emuB': '344d2e984843'}.items():
    assert hashlib.sha256((OUT / (k + '.txt')).read_bytes()).hexdigest().startswith(h), k
t = (HERE / 'v5.md').read_text(encoding='utf-8')
P4 = [b for b in t.split('\n\n') if b.startswith('In the villages and families')]
P2 = [b for b in t.split('\n\n') if b.startswith('The problem is that it can be soul destroying')]
assert len(P4) == 1 and len(P2) == 1
V4 = {
 'a': ("In the villages and families I've spent time around, land, childcare, housing, food, obligations, etc etc often go "
       "through the extended family and through local memory, along with the formal systems. Who needs a \"Rebuilding "
       "Intergenerational Belonging\" workshop when all it takes is some aunt giving three people a task?"),
 'c': ("In the villages and families I've spent time around, so much is taken care of by the extended family and the local "
       "memory, alongside the formal systems. Whether it's land, childcare, housing, food, obligations, etc, etc. Who needs a "
       "workshop called \"Rebuilding Intergenerational Belonging\" when some aunt has already given three people a task?"),
}
V2 = {
 'plain': ("But these days it can be soul destroying. People have a lot less of the communal life that held the obligation up, "
           "but they still carry it. So if one of them makes it into the cash economy, it's really hard to become independent "
           "or start a stable life, because they're expected to carry everybody. How can they get ahead, when all these people "
           "are dependent on them? And the relatives stay dependent too, since the payments don't give them a real "
           "alternative. It's the ancestral ethic playing out inside an individualistic cash economy. It can keep people alive, "
           "but it eats away at both sides too."),
 'l': ("But these days it can be soul destroying. People have a lot less of the communal life that held the obligation up (the "
       "shared land, work, childcare, food and daily belonging), but they still carry it. So if one of them makes it into the "
       "cash economy, it's really hard to become independent or start a stable life, because they're expected to carry "
       "everybody. How can they get ahead, when all these people are dependent on them? And the relatives stay dependent too, "
       "since the payments don't give them a real alternative. It's the ancestral ethic playing out inside an individualistic "
       "cash economy. It can keep people alive, but it eats away at both sides too."),
}
c4 = sys.argv[1] if len(sys.argv) > 1 else 'a'
c2 = sys.argv[2] if len(sys.argv) > 2 else 'plain'
t = t.replace(P4[0], V4[c4]).replace(P2[0], V2[c2])
(HERE / 'v6.md').write_text(t, encoding='utf-8')
(HERE / 'v6-variants.json').write_text(json.dumps({'H1-P4': V4, 'H3-P2': V2, 'chosen': [c4, c2]}, ensure_ascii=False, indent=1) + '\n',
                                       encoding='utf-8')
print('wrote v6.md with H1-P4', c4, 'and H3-P2', c2)
