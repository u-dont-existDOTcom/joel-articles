"""Section 13 draft v9 (2026-10-15): v8 with round r6's findings fixed (review-r6/DISPOSITIONS-r6.md says what each
finding got) and new breaks where a march reading found none. Each fix is an exact old -> new pair on one v8 paragraph.
Writes v9.md and v9-fixes.json. Run from this folder: python3 make_v9.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v8 = blocks((HERE / 'v8.md').read_text(encoding='utf-8'))
# paragraph ids in v8's order
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v8) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v8))
text = {i: b for i, b in zip(IDS, v8) if i}

FIX = {
 'H1-P1': [("you are already a community. It sounds", "you are already a community, even if it's still an untested one. It sounds",
            'both cold reads and the so-far stance check of r6 (cold read b of r5 too): "already a community" against H1-P3\'s '
            '"still a circle of promising strangers"; this says in what sense')],
 'H1-P4': [("you'll also need to budget for the group's practical side.",
            "you'll also need to budget for what the group can provide on the practical side.",
            'trace T1 of r6: name the budget as what the group can provide (not "capacity", which Joel called an AI tell)'),
           ('that would stop everything if nobody had them?', 'that could stop everything if nobody had them?',
            'trace T1 of r6: "can", not "would"')],
 'H2-P3': [('Is it ok to be openly part of the LGBTQ+ community? Is it okay to date and/or be in a relationship with whomever '
            'you choose? Will your community keep you fully protected if you are LGBTQ+?',
            'Could an LGBTQ+ member live openly there? Date and/or be in a relationship with whomever they choose? Would the '
            'community keep them fully protected?',
            'trace T1 of r6: the community being judged and its LGBTQ+ member, not "the LGBTQ+ community" or anyone\'s '
            'partner choice'),
           ('Should children be encouraged or discouraged to question', 'Should children be taught to question',
            'traces T2 of r5 and T1 of r6: "taught", as published'),
           ('Until your prospective community has answered these questions,', 'Until a group has answered these questions,',
            'trace T1 of r6: any group, the reader\'s own included')],
 'H3-P1': [('People tend to not take this into account enough.', 'People tend to not take this into account enough, but it matters so much!',
            'march: no break in either reading; the published "enormous power" said again as a reaction')],
 'H4-P2': [('Did they read the materials?', 'Did they read the materials? (Not everyone does!)',
            'march: no break in reading b; an aside on the question\'s point'),
           ('find out that way than after', 'find out through a thoughtful exchange than after',
            'traces T3 of r5 and r6: "thoughtful"')],
 'H4-P3': [("most people can be charming for two weeks, so if that's all they do, congratulations, you've established",
            "most people can be charming for two weeks. So if that's all they do, congratulations! You've established",
            'march: no break in either reading; the published "Congratulations" as its own reaction')],
 'H4-P5': [('(Both should be addressed in the agreements you draw up when you are first starting your group.)',
            "(A full member's rights and responsibilities should be addressed in the agreements you draw up when you are first "
            "starting your group.) Yes, it's a lot of homework!",
            'traces T4 of r5 and r6: name what the founding agreements cover; the march (no break in either reading): a remark '
            'on the text, like "That\'s a lot of deciding, I realize."')],
 'H4-P7': [('Being great with kids doesn’t mean someone should have the van keys!',
            'I wouldn’t hand someone the van keys just because they’re great with kids!',
            'march: a break in one reading only; the same example in the writer\'s voice')],
 'H4-P8': [("Hanging out doesn't count!", "Sorry, hanging out doesn't count!",
            'march: no break in either reading; the writer\'s voice on the published "do more than hang out"')],
 'H4-P9': [("politically? When decisions", "politically? (Yes, even the interns!) When decisions",
            'march: no break in reading a; an aside on the published "interns ... have rights"')],
 'H5-P1': [('it’s okay to eject them.', 'it can be okay to eject them.',
            'stance check, published essay, r6: "can be the right answer", not a flat "okay"'),
           ('and/or is just not someone people can live with,', 'and/or is just impossible to live with,',
            'the same check: the published "makes ordinary shared life impossible"; Joel\'s "impossible to live with" '
            '(2026-10-11 23:12)')],
 'H5-P2': [('Who preserves the evidence, and how do you make sure that people who are involved in the case aren’t '
            'participating in the decisions?',
            'Who preserves the evidence, and who has to step aside from the decisions?',
            'traces T5 of r5 and r6: who is recused, anyone too close, not only people in the case')],
 'H5-P3': [('The Zapatistas have been very important in opening my eyes', 'The Zapatistas have been important in opening my eyes',
            'trace T5 of r6: "very" made them matter more than published (the rest kept: DISPOSITIONS-r6.md)')],
 'H5-P4': [('Why should a mediator or ombud be chosen beforehand? Because if they are chosen in a crisis, and if the parties have '
            'not met this “neutral stranger” before, the parties often do not trust them.',
            'Also pick a mediator or ombud beforehand. Why bother? Because if they are chosen in a crisis, and nobody has met this '
            '“neutral stranger” before, people often do not trust them.',
            'trace T6 ("Also" lost; "people", not "the parties") and cold read a (the question took the claim as made): the '
            'instruction first; "Why bother?", the reader\'s objection, is the break (march: none in reading a)'),
           ('although mediation can help restore good relations,', 'although mediation is for repairing relations,',
            'trace T6: what mediation is for, not what it can help with'),
           ('if one party no longer consents to staying.', 'once consent is gone.',
            'trace T6: whose consent and to what are the published\'s to leave open (round r4\'s trace on "living together")')],
}

log = []
for pid, fixes in FIX.items():
    t = text[pid]
    for old, new, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new)
        log.append({'id': pid, 'old': old, 'new': new, 'why': why})
    text[pid] = t
out = [b if i is None else text[i] for i, b in zip(IDS, v8)]
(HERE / 'v9.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v9-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v9.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
