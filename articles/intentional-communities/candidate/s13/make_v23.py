"""Section 13 draft v23 (2026-10-16): v22 with round r15's dispositions (review-r15/DISPOSITIONS-r15.md) and Joel's answers of
2026-10-16 18:22 UTC (joel-20261016/): 33 a (the 😜 stays) and his cut of "How do you know?" at the head of H4-P6 ("what's that?
know what? doesn't seem to follow..."). That question was the paragraph's only break in both march readings of r15, so H4-P6 gets
a break that follows from the sentence before it. Each fix is an exact old -> new pair on one v22 paragraph (way A) or on v22b's
H5-P2 (way B); everything else is v22. Writes v23.md, v23b.md and v23-fixes.json. Run from this folder: python3 make_v23.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
A = blocks((HERE / 'v22.md').read_text(encoding='utf-8'))
B = blocks((HERE / 'v22b.md').read_text(encoding='utf-8'))
assert len(IDS) == len(A) == len(B) and all((i is None) == b.startswith('#') for i, b in zip(IDS, A))
assert [a for a, i in zip(A, IDS) if i != 'H5-P2'] == [b for b, i in zip(B, IDS) if i != 'H5-P2']
text = {i: b for i, b in zip(IDS, A) if i}
text['H5-P2b'] = dict(zip(IDS, B))['H5-P2']

R15 = 'review-r15/DISPOSITIONS-r15.md'
FIX = {
 'H1-P2': [
  ("whatever agreement you come up with means anything. Until then, what's it worth?",
   "whatever agreement you come up with means anything.",
   'lint, H1 as a whole: B7/B13 FAIL, two of its four paragraphs end on a short line (the subsection lint of 2026-10-15). '
   'This one goes: H1-P2 keeps its other break, "But really, truly dealt with it." (march r15, T2, both readings)')],
 'H2-P2': [
  ("Where are you still unsure? Mark those places too.",
   "Mark the places on your list where you're still unsure, too.",
   'lint, H2 as a whole: B7/B13 FAIL, three of its five paragraphs end on a short line. H2-P2 had no break in either march '
   'reading (r15, T6), so its end becomes one sentence; the published "Mark where you are unsure" kept')],
 'H3-P1': [
  ("If it's in the names of three out of twelve members, then despite what your literature says about everyone being equal, "
   "there are two classes of members.",
   "If three out of twelve members own everything, then whether or not your literature says everyone is equal, there are two "
   "classes of members.",
   'trace T1: LOST "own everything" ("it" was the deed, so the condition shrank to holding title) and SHIFT "despite" (it '
   'presupposed the literature claims equality; the published "whether or not"). Published words back, Emulate\'s shape kept')],
 'H3-P2': [
  ("what about outside debt (can an owner borrow money outside the community, and what happens if they do?), how improvements "
   "get handled, what happens when someone wants to leave the community, etc., etc. Lots of decisions to make!",
   "what about outside debt, how improvements get handled, and what happens when someone wants to leave the community. Lots of "
   "decisions to make!",
   'trace T1 and three stance checks: the parenthesis made outside debt an owner\'s private borrowing, where the essay means '
   'the community\'s own debts (section 14, the capacity budget); trace T1: "etc., etc." opened the published closed list. '
   '"Lots of decisions to make!" stays, the paragraph\'s break in both march readings')],
 'H3-P3': [
  ("who has authority to hand out the major resources, where conflicts of interest are, etc. It won't do",
   "who has authority to hand out the major resources, where conflicts of interest are, etc. Could anyone in your group answer "
   "all of that today? It won't do",
   'march r15: no break in either reading (T12). A question made from the paragraph\'s own list, placed right after it, not '
   'last (E176 and the landing lesson)')],
 'H4-P6': [
  ("How do you know? At each stage, always judge people based on their conduct. No matter how good it sounds when they talk "
   "about their spirituality or their therapy, don’t go by that.",
   "At each stage, always judge people based on their conduct. No matter how good it sounds when they talk about their "
   "spirituality or their therapy, don’t go by that. What do they actually do?",
   'Joel, 2026-10-16 18:22 UTC: "i would cut the first sentence "How do you know?" ... know what? doesn\'t seem to follow". '
   'It was the paragraph\'s only break (march r15, T20, both readings), so a question that follows from the sentence before '
   'it takes its place')],
 'H4-P9': [
  ('What about people who aren\'t "in" the commune politically?',
   'What about people who aren\'t fully "in" the commune politically?',
   'trace T4: LOST "full" (the published "do not need full political membership")'),
  ("are entitled to some rights when decisions really affect them, like pay and access to common resources.",
   "are entitled to some rights when decisions really affect their pay or access to common resources.",
   'trace T4: "like" made the published closed list of triggers examples, and "and" replaced "or"'),
  ("The same is true for decisions really affecting their schedule, safety, housing, records or discipline. Equality is for "
   "everybody, not just members, or communes can end up recreating a servant class that moves from commune to commune.",
   "The same is true for decisions really affecting their schedule, safety, housing, records or discipline. That's only fair. "
   "Equality that stops at the membership line can end up recreating a servant class that moves from commune to commune.",
   'trace T4 and two stance checks: "Equality is for everybody" was a new universal claim; the published "Egalitarianism that '
   'stops at the membership boundary can recreate a servant class". "That\'s only fair." gives the paragraph a break both march '
   'readings can see (r15: reading a only, T23), from what the paragraph says')],
 'H5-P1': [
  ("repeatedly violate essential community boundaries,", "repeatedly violate essential boundaries,",
   'trace T4: "community" narrowed the published "essential boundaries"'),
  ("If it's possible to do restorative work with the person in question in a reasonable amount of time, all the better.",
   "If restorative work can work with the person in question in a reasonable amount of time, all the better.",
   'trace T4: "possible to do" lost the published "when it can work" (effectiveness, not feasibility)'),
  ("But if the person is dangerous, the community", "But if the person is endangering everyone else, the community",
   'trace T4: LOST "everyone else" (the published "a person who is endangering everyone else")')],
 'H5-P2': [
  ("Who will recuse themselves?", "Who will be recused?",
   'trace T5: self-recusal for the published "who is recused"'),
  ("access to common resources and outside funds (if any)", "access to common resources or outside funds (if any)",
   'trace T5: "and" for the published "or"')],
 'H5-P2b': [
  ("Who will collect and preserve evidence?", "Who will preserve evidence?",
   'trace T6: "collect and" added a duty'),
  ("How will the person be able to reply to the charges against them?", "How will the person be able to reply?",
   'trace T6: "the charges against them" framed formal charges the published doesn\'t'),
  ("without creating danger?", "without endangering others?", 'trace T6: LOST "others"'),
  ("outside money (if any), etc., during the separation?", "outside money (if any) during the separation?",
   'trace T6: "etc." opened the published closed list')],
}
log, new = [], {}
for pid, fixes in FIX.items():
    t = text[pid]
    for old, new_s, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new_s)
        log.append({'id': pid, 'old': old, 'new': new_s, 'why': why, 'disposition': R15})
    new[pid] = t
for name, p2 in (('v23.md', 'H5-P2'), ('v23b.md', 'H5-P2b')):
    t = dict(text)
    t.update({k: v for k, v in new.items() if k != 'H5-P2b'})
    t['H5-P2'] = new.get(p2, text[p2])
    out = [b if i is None else t[i] for i, b in zip(IDS, A)]
    (HERE / name).write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v23-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for pid in FIX:
    print('%-7s %3d words | %s' % (pid, len(new[pid].split()), new[pid]))
    print()
print(len(log), 'fixes')
