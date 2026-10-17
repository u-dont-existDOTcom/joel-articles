"""Section 13 draft v34 (2026-10-17): v33 with the values subsection's last four paragraphs from Emulate round k (emu-k/, the
subsection sent whole), the meaning put back inside Emulate's sentences (the 21:05 lesson). Batch 316g read the whole of v33
AI over 291 words: the end of H2-P1 through H2-P4, while the subsection read with its opening monologue is Human (0.00). So
H2-P2 to H2-P4 have to read Human without the monologue's help: their tells were the instructions ("This list should also
include", "You should also include", "Make sure"), "whether or not" three times in three paragraphs, and the tidy verdict.
Emulate's call A said them as a person would; where it ran questions together (six in a row in H2-P3) or dropped a point
("be taught", "two years", "fully protected", "because"), the published point goes back inside its sentence, with no more than
two questions in a row. H2-P1, the monologue, is v33's. Two fixes the meaning traces of rounds r22 and r23b asked
for, in H3-P4 and H4-P8, go in too. Writes v34.md and v34-fixes.json. Run from this folder:
python3 make_v34.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v33.md').read_text(encoding='utf-8')
paras = [p for p in re.split(r'\n\s*\n', t)]
start = lambda s: [p for p in paras if p.startswith(s)][0]
NEW = {
    'H2-P2': ('Whenever you go to visit a community',
              'Bring your values with you when you go to visit a community! Make a list of what you really believe about children, '
              'money, property ownership, romance, medicine, food, spiritual practice, technology, privacy, dealing with conflict, '
              'leaving the community, etc. It’s a long list, I know! Some of them will just get a question mark, if you’re not sure '
              'yet.'),
    'H2-P3': ('This list should also include',
              'Sexuality and gender belong on there too. Would LGBTQ+ people be able to live openly in your community, date, '
              'be in relationships, and stay fully protected by the community? Should children be taught to question their '
              'sexual identities from a young age, and what happens if one of the community’s children comes out as gay or '
              'transgender? Until you answer these, your community’s values on freedom and on raising children aren’t '
              'complete. Yep. Both of them.'),
    # "if", not "when" (round r24's trace T1, item 4: the published asks what happens if a child grows up gay or trans)
    'H2-P3b': ('Are you willing to experiment?',
               'Are you willing to experiment? That’s a real value too! Put it on your list, because the people you live next to '
               'might think the experiment ended in 1978, and everything that came out of it is doctrine now.'),
    # round r24's trace T2: "look past" set the group's own account aside, where the published compares "not only its public
    # language", so Emulate's own "don't just listen to what they say. Look at how they operate." comes back (call A); and
    # "a little" shrank the published "uncomfortable conversation"; round r24b's trace T1: "Is that how you want to live?" lost the
    # published standard ("compare your values with"), so a reader could take the test as liking the lifestyle
    'H2-P4': ('Once you know what matters to you',
              'Then don’t just listen to what the group says. Look at how they really operate. A recent conflict is a good place '
              'to start: how did they handle it? There’s also who can block decisions, and what happened to the last person who '
              'left. (And who owns the land!) Does that match your values? It’s uncomfortable to talk about these things, I '
              'know, but the view isn’t going anywhere!'),
}
log = []
for pid, (head, new) in NEW.items():
    old = start(head)
    assert t.count(old) == 1, pid
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old, 'new': new, 'why': 'Emulate round k call A (emu-k/out/k01-emuA.txt), the published point '
                'put back inside its sentence; batch 316g read v33\'s H2-P2 to H2-P4 AI inside the whole section'})
# two fixes the meaning traces asked for, in paragraphs read Human alone before: round r22's trace T1 (review-r22/trace-T1.md,
# item 7) and round r23b's (review-r23b/trace-T1.md, item 6)
MORE = [
    ('H3-P4', "Write up the exit terms when it's only theoretical", "Write up the exit terms while leaving is still only theoretical",
     'trace r22 T1 item 7: "it" stood where the published "departure" stood, with no noun naming it, so "theoretical" could read '
     'as "hollow" after "only on paper"; and the published "still" (the window that closes) was gone'),
    ('H4-P8', "It'll show you whether your way of coordinating works.", "It can show you whether your way of coordinating works.",
     'trace r23b T1 item 6: with the soul clause cut, "It\'ll show you" turned the published "can reveal" into a guarantee'),
]
for pid, old_, new_, why in MORE:
    assert t.count(old_) == 1, pid
    t = t.replace(old_, new_)
    log.append({'id': pid, 'old': old_, 'new': new_, 'why': why})
(HERE / 'v34.md').write_text(t, encoding='utf-8')
(HERE / 'v34-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v34.md')
