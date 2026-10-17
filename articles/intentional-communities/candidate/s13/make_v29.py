"""Section 13 draft v29 (2026-10-16): v28 with the sentences the whole-section check still reads AI (308g: 301 of 2,287 words
in four windows, b308/PREDICTIONS.md) taken back to Emulate's own sentences, the lesson of v28. Each window starts or ends on
a sentence of mine or a sentence rebuilt from the published wording:
- window 1 (H1-P2's second sentence to H1-P3's first) ends on "it's still just a circle of promising strangers", the published
  phrase, AI in every whole-section read since v26;
- windows 2 and 3 start on H2-P3's and H2-P4's runs of questions (round j's call B kept the four questions as a run; call A
  dropped them; call B's H2-P3 says the five questions as statements);
- window 4 starts on H3-P1's "If three out of twelve members own everything, then whether or not your literature says everyone
  is equal", which I had rebuilt from the published sentence in place of Emulate round i's.
Writes v29.md (all three), v29a.md (window 1 only), v29b.md (windows 2 and 3 only), v29c.md (window 4 only) and
v29-fixes.json. Run from this folder: python3 make_v29.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
blocks = lambda md: [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]
V28 = blocks((HERE / 'v28.md').read_text(encoding='utf-8'))
assert len(V28) == len(IDS)
J1B = blocks((HERE / 'emu-j' / 'out' / 'j01-emuB.txt').read_text(encoding='utf-8'))
J1A = blocks((HERE / 'emu-j' / 'out' / 'j01-emuA.txt').read_text(encoding='utf-8'))
I1A = (HERE / 'emu-i' / 'out' / 'l01-emuA.txt').read_text(encoding='utf-8')
EMU = {'H2-P3': J1B[5], 'H2-P4': J1A[7], 'H3-P1': next(p for p in blocks(I1A) if 'title to the land' in p)}
assert EMU['H2-P3'].startswith('This list should also include') and EMU['H2-P4'].startswith('When you have a good idea')
NEW = {
 'H1-P3': ('a', "Until that’s happened, you’re all still promising strangers, and you don’t want to take out a mortgage together "
           "yet. That’s okay! There’s lots you can do! You can all meet in a rented or borrowed space, or at each other’s "
           "houses, and find out how much conflict the group can handle before you need a surveyor.", None,
   ['"it’s still just a circle of promising strangers, and you don’t want to take out a mortgage with them yet" -> "you’re all '
    'still promising strangers, and you don’t want to take out a mortgage together yet" (the published "circle", which every '
    'whole-section read since v26 has read AI at, out; "promising strangers" and the advice stay; keys U7 note_v29)']),
 'H2-P3': ('b', "This list should also include your thoughts on sexuality and gender, and whether or not LGBTQ+ people should be "
           "able to live openly in your community, to date or be in relationships, and be fully protected by the community. You "
           "should also include whether or not children should be taught to question their sexual identities from a young age, "
           "and what should happen if one of the community’s children comes out as gay or transgender. You don’t have your "
           "community’s values on freedom and raising children complete until you answer these questions. Both of them!",
   'emu-j/out/j01-emuB.txt',
   ['call B, which says the five questions as statements (308g\'s window 2 started on call A\'s run of them)',
    '"LGBTQ" -> "LGBTQ+" (the published term)',
    '"whether or not it’s important that children not be forced to question their sexual identities" -> "whether or not '
    'children should be taught to question their sexual identities" (call B reversed the published question, "Should children '
    'be taught that they should question their sexual identities at an early age?")',
    '"on freedom and children" -> "on freedom and raising children" (the published "child-rearing values", keys U19)',
    '"Both of them!" (v26\'s break)']),
 'H2-P4': ('b', "When you have a good idea of what’s important to you, you can look at how a group actually functions, not just its "
           "public face. Find out how it handled its last conflict, and who can block a decision. How did leaving "
           "go for the last person who left? Who owns the land? Then make a choice whether or not it functions in a way that is "
           "important to you. It may be an uncomfortable conversation, but the view will still be there after you’ve had it.",
   'emu-j/out/j01-emuA.txt',
   ['call A (308g\'s window 3 started on call B\'s run of four questions)',
    '"you can look at how a group functions" -> "you can look at how a group actually functions, not just its public face" '
    '(call B\'s words for the published "the group’s actual behavior, not only its public language", keys U21)',
    'the published four questions back, which call A dropped, two in a sentence and two as questions (keys U22): "Find out how '
    'it handled its last conflict, and who can block a decision. How did leaving go for the last person who left? Who owns the '
    'land?" (the last two are call B\'s)',
    '", and make a choice" -> ". Then make a choice" (the questions come between)']),
 'H3-P1': ('c', "Who will have title to the land? Very important! Whoever has it will have enormous power over the rest of the "
           "community. If the deed’s in the name of the “founder,” then he or she is really your landlord, with a philosophy. "
           "If three out of twelve members own everything, then despite what your literature says about everyone being equal, there are "
           "two classes of members.",
   'emu-i/out/l01-emuA.txt',
   ['Emulate round i\'s call A back for the last two sentences (v22 on had rebuilt them from the published ones; 308g\'s window '
    '4 started there), with "it’s" -> "the deed’s" (keys U25): "If the deed’s in the name of the “founder,” then he or she is '
    'really your landlord, with a philosophy."',
    '"If it’s in the names of 3 out of 12 members, then despite what your literature says" -> "If three out of twelve members '
    'own everything, then despite what your literature says about everyone being equal" (the published "three of twelve '
    'members own everything" and "whether or not the welcome packet uses the word “equal”"; keys U26)',
    'Emulate\'s heading prefix "INTERESTED Parties --" out (the heading is Joel\'s)']),
}
log = []
for pid, (way, new, src, fixes) in NEW.items():
    log.append({'id': pid, 'way': way, 'emulate_file': src, 'emulate': EMU.get(pid), 'v28': V28[IDS.index(pid)], 'new': new,
                'fixes': fixes})
for name, ways in (('v29', 'abc'), ('v29a', 'a'), ('v29b', 'b'), ('v29c', 'c')):
    text = dict(zip(IDS, V28))
    for pid, (way, new, _, _) in NEW.items():
        if way in ways:
            text[pid] = new
    out = [V28[i] if pid is None else text[pid] for i, pid in enumerate(IDS)]
    (HERE / (name + '.md')).write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v29-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('written v29, v29a, v29b, v29c')
