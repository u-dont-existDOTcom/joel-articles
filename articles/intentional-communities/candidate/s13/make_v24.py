"""Section 13 draft v24 (2026-10-16): v23 with round r16's dispositions (review-r16/DISPOSITIONS-r16.md). Under the
convergent-review rule, an unchanged item keeps its verdict; a new finding on unchanged words is fixed here only when the fix
puts back the published words, or makes a sentence two readers paused at plain, and loses nothing. Exact old -> new pairs on
v23 (way A) and on v23b's H5-P2 (way B); H1-P2 goes back to v22's, since dropping its last line cost it its break in one march
reading. Writes v24.md, v24b.md and v24-fixes.json. Run from this folder: python3 make_v24.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
A = blocks((HERE / 'v23.md').read_text(encoding='utf-8'))
B = blocks((HERE / 'v23b.md').read_text(encoding='utf-8'))
V22 = dict(zip(IDS, blocks((HERE / 'v22.md').read_text(encoding='utf-8'))))
assert len(IDS) == len(A) == len(B)
text = {i: b for i, b in zip(IDS, A) if i}
text['H5-P2b'] = dict(zip(IDS, B))['H5-P2']
text['H1-P2'] = V22['H1-P2']
BOOK = ('https://library.uniteddiversity.coop/Ecovillages_and_Low_Impact_Development/'
        'Creating_a_Life_Together-Practical_Tools_to_Grow_Ecovillages_and_Intentional_Communities.pdf')
R16 = 'review-r16/DISPOSITIONS-r16.md'
FIX = {
 'H1-P1': [
  ("It sounds cheesy but it's true.", "It may sound cheesy, but it's true all the same.",
   'the subsection lint (B7/B13): H1-P2 keeps its last line (above), so this one is no longer a short landing; the same '
   'aside, still the paragraph\'s break')],
 'H3-P2': [
  ("what happens when an owner dies,", "how inheritance works,",
   'stance check against the article so far (review-r16/STANCE-sofar.md): "what happens when an owner dies" narrowed the '
   'published "inheritance" to an owner\'s death (a member\'s heirs and children left out). The published word back, '
   'nothing else; round r17\'s reviews ran before this change')],
 'H3-P3': [
  ("How will you handle VISIBILITY of what you have?",
   "And how will you handle the VISIBILITY of what the community has?",
   'cold read r16 b: the opener didn\'t follow from the paragraph before (the opener rule of 2026-10-16), and reader a paused '
   'at "VISIBILITY of what you have"; "And" makes it the next decision after H3-P2\'s, "the community" says whose'),
  ("where conflicts of interest are, etc. Could anyone in your group answer all of that today?",
   "where conflicts of interest are, etc.",
   'trace T3: the question implied the group can\'t answer now, which the published doesn\'t say. Its replacement in the '
   'first v24, "Who\'s keeping track of all that?", read as a step in both march readings of round r17 (T12), so the break '
   'moves (below)'),
  ("you'll still have scarce resources and bottlenecks.", "you'll still have scarce resources and bottlenecks. Sorry!",
   'the break: the writer reacting to the claim just made, mid-paragraph, no claim of its own (E176)'),
  ("(whether it's cash, if you use it, or tools,", "(cash, if you use it, but also tools,",
   'trace T3: "or" made the other things alternatives to cash; the published "Cash if the community uses it, but also '
   'tools ..." (a cash-only right still depends on spare money, which the next sentence says); readers a and V1 paused at '
   '"unless the community has spare money"')],
 'H3-P5': [
  ("For the full sequence, see Diana Leafe Christian's [*Creating a Life Together*](%s) (on the reading list at the end) -- "
   "vision, then members, then pooling major resources, then land." % BOOK,
   "For the full sequence -- vision, then members, then pooling major resources, then land -- see Diana Leafe Christian's "
   "[*Creating a Life Together*](%s) (on the reading list at the end). It's the first book I'd hand to any group starting "
   "out." % BOOK,
   'a repeated pause (r9 a, r14 a, r16 a and b: "the full sequence" before the reader learns what it is): the sequence '
   'goes right after the phrase, as in the published sentence. The break (round r17\'s march: none in either reading, T14) is the '
   'writer\'s own recommendation, from his appendix\'s "start here for sequencing, membership, money, land, and agreements"; '
   'eleven words, so the land subsection\'s landing rate holds')],
 'H4-P2': [
  ("There’s some correspondence first.", "First, correspond with them.",
   'a repeated pause (V1 and r16 a: "There\'s some correspondence first"): the published "Correspond first.", with whom said (key U40 "correspond"); round r17\'s trace T3: "for a while" added a length, so it went')],
 'H4-P6': [
  ("It’s also easy to mistake people just doing what everyone else is doing for safety.",
   "It’s also easy to take people doing what everyone else is doing as a sign of safety.",
   'a repeated pause (V1, r16 a and b): "doing ... for safety" read first as what they do it for; the published "mistaking '
   'conformity for safety" without the garden path (key U47 kept)')],
 'H4-P7': [
  ("You can find out by asking if you’ve seen them do this thing before,",
   "You can find out by checking whether you’ve seen them do this thing before,",
   'a repeated pause (V1, r16 a and b): "asking" whom?')],
 'H4-P9': [
  ('What about people who aren\'t fully "in" the commune politically?',
   'Then there are the people who aren\'t fully "in" the commune politically.',
   'cold read r16 b: after the trial run with candidates, the question first read as being about them; "Then there are" '
   'opens the new group'),
  ("are entitled to some rights when decisions really affect their pay or access to common resources.",
   "are entitled to some rights when decisions really affect their pay or access to common resources. Why wouldn't they be?",
   'the break, a question about the claim just made (E176); it replaces "That\'s only fair." below'),
  (" That's only fair.", "",
   'trace T4: a new justification (fairness); the published argues from the servant-class risk')],
 'H5-P1': [
  ("a serious danger to others (or to everyone in general)", "a serious or generalized danger to others",
   'trace T5: "serious" came to cover both cases; the published "a serious or generalized danger"')],
 'H5-P2b': [
  ("What might call for immediate action", "What conduct might call for immediate action",
   'trace T7: LOST "conduct" (the published "what conduct triggers immediate protective action")')],
}
log, new = [], dict(text)
for pid, fixes in FIX.items():
    t = new[pid]
    for old, new_s, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new_s)
        log.append({'id': pid, 'old': old, 'new': new_s, 'why': why, 'disposition': R16})
    new[pid] = t
log.append({'id': 'H1-P2', 'old': text['H1-P2'] if False else 'v23\'s H1-P2', 'new': 'v22\'s H1-P2',
            'why': 'march r16 reading a found no break once "Until then, what\'s it worth?" was gone', 'disposition': R16})
for name, p2 in (('v24.md', 'H5-P2'), ('v24b.md', 'H5-P2b')):
    t = dict(new)
    t['H5-P2'] = new[p2]
    out = [b if i is None else t[i] for i, b in zip(IDS, A)]
    (HERE / name).write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v24-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for pid in list(FIX) + ['H1-P2']:
    print('%-7s %3d words | %s' % (pid, len(new[pid].split()), new[pid][:220]))
print(len(log), 'changes')
