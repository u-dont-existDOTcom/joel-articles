"""Section 16 draft v11 (2026-10-17): v10 db (every paragraph Human alone, its opening Human whole, 344g) with the two stretches
that read AI inside the whole section rebuilt from Emulate round e (emu-e/out/, three calls on each stretch whole in v10's
meaning), the published meaning put back inside the calls' sentences.
- H2 shape a, from e01's call A: H2-P2 "It's a more beautiful view for sure, but now you have the conflict PLUS goats." (A's "I've
  seen some people" is an observation the published doesn't make; its "40 acres" and "stuff" kept as "forty acres" and
  "stuff"); H2-P3 "Peer counseling only requires two people and a place to talk privately. Reparenting, somatic work, working
  on jealousy, learning how to repair conflict, etc etc?", with the deed (A lost it); H2-P4 "Even if a group practices together
  every week for two years, it may never own land." (A's "huge difference" is an intensity the published doesn't have).
- H3 shape a, from e02's calls A and C: H3-P4 "Where can you find some of these people? ... How about restorative-practice
  groups? Maybe there's an open-hearted congregation, or a mature recovery group, or a meditation group you can check out.",
  with the person back from a long retreat "kinder, rather than more impressed with themselves" (A: "a bit nicer, rather than
  just feeling good about themselves", and "Or better yet", a ranking); H3-P5 "If not, you should go!" and the requirements as
  an aside (A), with "actual" (the published) and "take visitors"; H3-P6 "drives you bananas" (C), the four lessons joined by
  "and" as trace r13 T3 asked, and the showers that send you off pricing studio apartments.
Shapes: H2 k (v10) or a; H3 k (v10) or a. Writes v11.md and v11-variants.json. Run from this folder: python3 make_v11.py [k|a] [k|a]"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
h2 = sys.argv[1] if len(sys.argv) > 1 else 'a'
h3 = sys.argv[2] if len(sys.argv) > 2 else 'a'
subprocess.run([sys.executable, str(HERE / 'make_v10.py'), 'db'], check=True, capture_output=True)
t = (HERE / 'v10.md').read_text(encoding='utf-8')
PC = '[Peer counseling](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling)'
L5 = ('[Twin Oaks](https://twinoaks.org/), [East Wind](http://eastwind.org/), [Acorn](https://www.ic.org/directory/acorn-community-'
      'farm/) and other [intentional communities](https://www.ic.org/)')
EV = '[ecovillages](https://ecovillage.org/)'
OLD = {
 'H2-P2': ("People sometimes buy forty acres and then bring all their unprocessed baggage with them to a more scenic location. The "
           "view's better, I'll give them that! But now the conflict has goats."),
 'H2-P3': ("The inner pl/ork can start right where you live, though. %s only needs two people and enough privacy to talk. And "
           "reparenting, somatic work, jealousy, conflict repair, etc etc? None of that has to wait for a deed either!" % PC),
 'H2-P4': ("A group that practices together weekly for two years may never own land. So what? It can still make a difference in "
           "how people get through divorce, illness, grief, parenting and plain old loneliness."),
 'H3-P4': ("Where do you find them? Are there any unprogrammed Quaker meetings or restorative-practice groups near you? Any "
           "open-hearted congregations? Maybe a mature recovery group, or a meditation group? Or someone who came back from a long "
           "retreat kinder, rather than more impressed with themselves?"),
 'H3-P5': ("Have you ever visited an actual community? Go! %s take visitors, and so do a lot of %s. Just check their current "
           "visitor requirements first." % (L5, EV)),
 'H3-P6': ("What do you get out of a visit? Things no manifesto can tell you. How much togetherness you actually enjoy, for one, and "
           "what kind of privacy you need. And which labor system drives you nuts! And whether communal showers feel liberating or "
           "send you off pricing studio apartments."),
}
NEW = {
 'H2-P2': ("People sometimes buy forty acres and then bring all their unprocessed stuff with them to a more scenic location. It's a "
           "more beautiful view for sure, but now you have the conflict PLUS goats."),
 'H2-P3': ("The inner pl/ork can start right where you live, though. %s only requires two people and a place to talk privately. "
           "Reparenting, somatic work, working on jealousy, learning how to repair conflict, etc etc? None of that has to wait for "
           "a deed!" % PC),
 'H2-P4': ("Even if a group practices together every week for two years, it may never own land. So what? It can still make a "
           "difference in how people get through divorce, illness, grief, parenting and plain old loneliness."),
 'H3-P4': ("Where can you find some of these people? Are there any unprogrammed Quaker meetings near you? How about "
           "restorative-practice groups? Maybe there's an open-hearted congregation, or a mature recovery group, or a meditation "
           "group you can check out. Or maybe you know someone who came back from a long retreat kinder, rather than more "
           "impressed with themselves."),
 'H3-P5': ("Have you ever been to an actual community? If not, you should go! %s take visitors, and so do a lot of %s (just check "
           "their current visitor requirements before you go)." % (L5, EV)),
 'H3-P6': ("What will you learn from a visit? Things no manifesto can tell you. How much togetherness you actually enjoy, for one, "
           "and what kind of privacy you need. And which labor system drives you bananas! And whether communal showers feel "
           "liberating, or send you off pricing studio apartments."),
}
for k, v in OLD.items():
    assert t.count(v) == 1, k
for k in OLD:
    if (k.startswith('H2') and h2 == 'a') or (k.startswith('H3') and h3 == 'a'):
        t = t.replace(OLD[k], NEW[k])
(HERE / 'v11.md').write_text(t, encoding='utf-8')
(HERE / 'v11-variants.json').write_text(json.dumps({'old': OLD, 'new': NEW, 'H2': h2, 'H3': h3}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v11.md with H2', h2, 'and H3', h3)
