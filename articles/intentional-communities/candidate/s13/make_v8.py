"""Section 13 draft v8 (2026-10-15): v7 with gate round r5's findings fixed (review-r5: five traces, two cold reads, two
march reads, two stance checks). Each fix is an exact old -> new pair on one v7 paragraph, with the finding it answers;
two paragraphs are split back the way the published text has them (the experiment line, and the book's sequence).
Writes v8.md and v8-fixes.json. Run from this folder: python3 make_v8.py

Breaks (the march read found none, in one reading or both, in 11 of v7's 21 rebuilt paragraphs): each new break says
again something the paragraph already says, as a reaction, a question or an aside (E176), or is an aside without a
claim ("Yes, it keeps getting longer." and "That's not much of a right.", both passed by earlier traces)."""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v7 = blocks((HERE / 'v7.md').read_text(encoding='utf-8'))
src = json.loads((HERE / 'v7-sources.json').read_text(encoding='utf-8'))
ids, k = [], 0
for b in v7:
    if b.startswith('#'):
        ids.append(None)
    else:
        ids.append(src[k]['id'])
        k += 1
text = {pid: b for pid, b in zip(ids, v7) if pid}

FIX = {
 'H1-P2': [
  ('What comes up in conflicts is always jealousy, humiliation, fear, or other old material, so find out which.',
   'What comes up in the conflict is jealousy, humiliation, fear, or old material, and you find out which.',
   'trace T1 (shift: "always", and fear filed under old material) and both stance checks (every conflict made old wounds); '
   '"the conflict" is the one being processed. Not an imperative: the linter counted the paragraph as instructions (E23)'),
  ('and then you can make one.', 'and then you can make one. Otherwise, what\'s it worth?',
   'march: no break in either reading; the published "enough that the agreement means something" said again as a question'),
 ],
 'H1-P4': [
  ("you'll also need to budget for the group's physical needs.", "you'll also need to budget for the group's practical side.",
   'trace T1: "physical needs" lists needs, not what the group can provide, and narrows the list'),
  ("What critical skills will the group need that they don't currently have?",
   'What are the few critical skills that would stop everything if nobody had them?',
   'trace T1: the published "the few skills whose absence can stop everything", not only the missing ones'),
  ("It's boring stuff but in the end, a group could be great", "It's boring stuff, I know. But in the end, a group could be great",
   'march: a break in one reading only; "It\'s the boring part, I know." read as a break in both readings of round r4'),
 ],
 'H2-P1': [
  ('Have you noticed people choose', 'Have you noticed people often choose', 'trace T1: "often" lost'),
 ],
 'H2-P3': [
  ('Throw sexuality and gender onto that list. Is it ok', 'Throw sexuality and gender onto that list. Yes, it keeps getting longer. Is it ok',
   'march: no break in either reading; the aside rounds r2 to r4 passed ("an aside", no claim)'),
  ('if you are a member of the aforementioned community?', 'if you are LGBTQ+?',
   'trace T2: "the aforementioned community" could be the community visited'),
  ('Will your children be encouraged or discouraged', 'Should children be encouraged or discouraged',
   'trace T2: "should" (what the community teaches), not "will", and children, not your own'),
  ('Should your children grow up to be gay or transgender', 'Should one of the children grow up to be gay or transgender',
   'trace T2: one of the children, as published'),
 ],
 'H2-P4': [
  ('It might be uncomfortable to have some of these conversations', 'It’ll be uncomfortable to have these conversations',
   'trace T2: the published says the conversation is uncomfortable, not that it might be'),
 ],
 'H3-P1': [
  ("People tend to not take this into account enough. Whoever has the title to the land has a massive amount",
   "Who has the title to the land? People tend to not take this into account enough. Whoever has it has a massive amount",
   'trace T2: "this" pointed at nothing (a heading comes between); the question names it, and is the break the march read '
   'wanted (one reading had none)'),
  ("If it's in the name of three members out of twelve,", "If three members out of twelve own everything,",
   'trace T2: everything owned, not only the title'),
 ],
 'H3-P3': [
  ('If the community does not use money, it still needs to be able to provide people with resources when they leave (tools,',
   'Whether or not the community uses money, it still needs to be able to provide people with resources when they leave (cash '
   'if it uses money, plus tools,',
   'trace T2 and both stance checks: in-kind exit rights for every community, cash as well where it is used ("plus", '
   'not the published "but also": the linter\'s O36)'),
  ('if there is money around.', 'if there is money around. That\'s not much of a right.',
   'march: no break in either reading; round r3\'s trace: "Not a claim", it repeats "paper right"'),
 ],
 'H3-P4': [
  ('Good people leave for good reasons, often due to a dying parent,', 'Good people leave for good reasons, like a dying parent,',
   'trace T3: the list is the reasons, not frequent causes among others'),
  ('You should set the terms of letting someone leave when no one is leaving, and it’s just a theoretical discussion.',
   'You should write down the exit terms while no one is leaving yet, and it’s still just a theoretical discussion.',
   'trace T3: "write", "exit terms" and "still" lost'),
 ],
 'H4-P2': [
  ('do the practices?', 'do the relevant practices?', 'trace T3: "relevant" lost'),
  ('It’s better to just find out that way than after you spend six months together, right?',
   'It’s a lot cheaper to find out that way than after six months of misunderstanding, right?',
   'trace T3: the published "costs far less than a six-month misunderstanding"'),
 ],
 'H4-P3': [
  ("If you go for a week or two and just participate in normal life", "If they come for a week or two and just participate in normal life",
   'cold read b: "you go" made the visitor the one judging, then "they" the one judged'),
  ("so if that's all you do,", "so if that's all they do,", 'cold read b, the same'),
 ],
 'H4-P4': [
  ("to actually experience any inconvenience or conflict with the person in question",
   "to actually experience inconvenience and conflict with the person in question",
   'trace T3: both, not either'),
  ("bored, etc. Even", "bored, etc. (Hopefully not all at once!) Even",
   'march: no break in either reading; an aside on the five states, no claim'),
  ("may be able to pull off an act for a few months if they're really motivated, so",
   "may be able to pull off an act for months, so",
   'trace T3: "if they\'re really motivated" a new cause, "a few" a cap'),
 ],
 'H4-P5': [
  ("Who will make the decision about a person becoming a full member? (It shouldn't be",
   "Who will make the decision about a person becoming a full member? (Hint: it shouldn't be",
   'march: no break in either reading; the published "the recruiter should not control the decision" said again as an aside'),
  ('(These should be addressed', '(Both should be addressed',
   'trace T4: "These" took in the provisional questions; the founding agreements set full membership\'s terms'),
 ],
 'H4-P6': [
  ('Even giving it six months will not give you enough data to know if someone is a good person.',
   'Even giving it six months will give you more data, but it won’t tell you if someone is a good person.',
   'trace T4: more data doesn\'t make the judging valid; the limit isn\'t the amount of data'),
 ],
 'H4-P7': [
  ('you want to know how they handle that specific thing.',
   'you want to know how they handle that specific thing. Being great with kids doesn’t mean someone should have the van keys!',
   'march: no break in either reading; the published "conduct-specific evidence" said again as an example'),
  ('You can do this by asking if you\u2019ve seen them', 'You can find out by asking if you\u2019ve seen them',
   'after the new example, "do this" could point at it; "find out" (how they handle that thing) can\'t'),
  ('some way for someone to appeal to a separate authority if needed.',
   'some way for someone to appeal that decision to a separate authority if needed.',
   'trace T4: what is appealed, lost'),
 ],
 'H4-P8': [
  ('Do stuff together prior to making them provisional members. Can',
   'Do stuff together prior to making them provisional members. Hanging out doesn\'t count! Can',
   'march: no break in either reading; the published "do more than hang out" said again as a reaction'),
  ('before people have to sell their houses to join.', 'before anybody sells a house.',
   'trace T4: the published doesn\'t say joining means selling a house'),
 ],
 'H4-P9': [
  ("even if they're not \"in\" the commune politically?", "even if they're not fully \"in\" the commune politically?",
   'trace T4: "full" political membership'),
  ('pay or use of resources,', 'pay or access to shared resources,', 'trace T4: access, and shared'),
  ('records, discipline, etc.', 'records or discipline.', 'trace T4: "etc." opened the list of what a decision has to affect'),
  ("a risk of creating servant classes from commune to commune.",
   "a risk of recreating a servant class that moves from commune to commune.",
   'trace T4: one class between communes, and "recreating"'),
 ],
 'H5-P1': [
  ('If someone won’t follow basic rules and boundaries, and won’t stop,',
   'If someone won’t respect essential boundaries, and won’t stop,',
   'both stance checks: refusing rules isn\'t a ground for ejection; the published "essential boundaries"'),
  ('If the community feels like they can do restorative work with them in a reasonable amount of time that’s cool, but if',
   'If restorative work with them can work in a reasonable amount of time, that’s cool! But if',
   'trace T5: the work\'s chance of working is the test, not the community\'s feeling; and the march (no break in either '
   'reading): "that’s cool!" as its own reaction'),
  ('the community doesn’t have to provide them treatment.', 'the community doesn’t have to turn into their treatment program.',
   'trace T5: the published denies turning the commune into a program, not all treatment'),
 ],
 'H5-P2': [
  ('How do you preserve the evidence and make sure that people who are involved in it aren’t participating in the decision?',
   'Who preserves the evidence, and how do you make sure that people who are involved in the case aren’t participating in '
   'the decisions?',
   'trace T5: who, not how; "it" named nothing; every decision, not one'),
  ('How does the person reply, and appeal the decision, without endangering others?',
   'How does the person reply, and what review or appeal is possible without endangering others?',
   'trace T5: "review" lost, and "without endangering others" had taken in the reply'),
  ('have access to outside funds?', 'have access to outside funds, if any?', 'trace T5: "if any" lost'),
  ('When do people reach for outside help?', 'When do people reach for outside help? (More on that one next.)',
   'march: no break in either reading; an aside about the text, no claim'),
 ],
 'H5-P3': [
  ("(It's true that I've been kinda assuming that in", "(It's true that at first my research kinda leaned too far toward "
   "the nation-state.)",
   'trace T5, both stance checks and cold read b: the lean was early and since corrected, and "that" could be either'),
  ("All that's really needed is", "What's really needed is", 'trace T5: "all" made it the only requirement'),
  ("But that doesn't mean that they can violate non-waivable individual rights, or that there can't be jurisdiction above them.",
   "But autonomy doesn't mean that these institutions can violate non-waivable individual rights, or that outside "
   "jurisdiction stops applying to them.",
   'trace T5 and cold read a: who "they" are; outside jurisdiction stays, and "above" put a layer over the community'),
 ],
 'H5-P4': [
  ('they are unlikely to trust them.', 'the parties often do not trust them.',
   'trace T5: "often", and "they" had just meant the mediator'),
 ],
}

# H5-P3's first fix replaces the link sentence; its link moves to "my research" in the new wording
LINKFIX = ("(It's true that at first my research kinda leaned too far toward the nation-state.)",
           "(It's true that at first [my research](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) "
           "kinda leaned too far toward the nation-state.)")

log = []
for pid, fixes in FIX.items():
    t = text[pid]
    for old, new, why in fixes:
        if pid == 'H5-P3' and old.startswith("(It's true"):
            # the old aside runs on to its link: "(It's true that I've been kinda assuming that in [my research](URL).)"
            m = re.search(r"\(It's true that I've been kinda assuming that in \[my research\]\([^)]*\)\.\)", t)
            assert m, pid
            t = t[:m.start()] + LINKFIX[1] + t[m.end():]
            log.append({'id': pid, 'old': m.group(0), 'new': LINKFIX[1], 'why': why})
            continue
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new)
        log.append({'id': pid, 'old': old, 'new': new, 'why': why})
    text[pid] = t

# The experiment line goes back to a paragraph of its own (as published), with the published "a real value" and "because"
p3 = text['H2-P3']
cut = 'Also make sure that your list declares whether or not you value experimenting, the folks next to you may think ' \
      'experimenting ended in 1978 and anything that came from it is doctrine now.'
assert p3.endswith(cut)
text['H2-P3'] = p3[:-len(cut)].rstrip()
text['H2-P3b'] = ('Willing to experiment? That\'s a real value too! Make sure that your list declares whether or not you value '
                  'experimenting, because the folks next to you may think experimenting ended in 1978 and anything that came '
                  'from it is doctrine now.')
log.append({'id': 'H2-P3b', 'old': cut, 'new': text['H2-P3b'],
            'why': 'trace T2 (lost: "a real value", and the "because"), cold read a (experimenting with what? read inside the '
                   'sexuality questions); its own paragraph again, as published, with the published claim said again as a '
                   'question and an exclamation (the break)'})
# The book's sequence goes back to a paragraph of its own (as published), tied to the section
p4 = text['H3-P4']
m = re.search(r' For the whole sequence, see Diana Leafe Christian’s (\[\*Creating a Life Together\*\]\([^)]*\)): First you get '
              r'the vision, then you get the members, then you pool the major resources, and lastly you get the land\.$', p4)
assert m, 'book'
text['H3-P4'] = p4[:m.start()]
text['H3-P5'] = ('For the order to do all this in, see Diana Leafe Christian’s ' + m.group(1) + ': First you get the vision, '
                 'then you get the members, then you pool the major resources, and lastly you get the land. So yes, the land '
                 'comes last!')
log.append({'id': 'H3-P5', 'old': m.group(0).strip(), 'new': text['H3-P5'],
            'why': 'cold reads a and b of r5, and b of r4: "which sequence?", "why here?" after the exit terms. Its own '
                   'paragraph again, as published, and "for the order to do all this in" ties it to the section; "So yes, '
                   'the land comes last!" is the break, the sequence\'s last step said again as a reaction'})

order = []
for pid, b in zip(ids, v7):
    if pid is None:
        order.append(b)
        continue
    order.append(text[pid])
    if pid == 'H2-P3':
        order.append(text['H2-P3b'])
    if pid == 'H3-P4':
        order.append(text['H3-P5'])
(HERE / 'v8.md').write_text('\n\n'.join(order) + '\n', encoding='utf-8')
(HERE / 'v8-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v8.md:', len([b for b in order if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes')
