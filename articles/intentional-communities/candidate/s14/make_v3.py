"""Section 14 draft v3 (2026-10-16): v2 with round r3's findings (review-r3/DISPOSITIONS-r3.md) and four endings for P6 and
P7, which read AI together (batch 301g, 0.92) and with P5 (302g, 0.67) though the whole section read Human (high).

Round r3's fixes are exact old -> new pairs on v2. The endings are W1 (v2's P6, a new P7), W2 (P6's list split, an aside on
his questions), W3 (the film named, as the article's opening names it), W5 (P6 as what the writer sees). Each P7 ends on the
writer's own hedge about the published "may continue" instead of v2's "That gives me hope.". The two P6/P7 rewrites of
review-r2b (V-a, V-b) are not used: read without the section around them, neither P6 had a break in either march reading.

Writes v3-W1.md, v3-W2.md, v3-W3.md, v3-W5.md and v3-fixes.json. Run from this folder: python3 make_v3.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE / 'v2.md').read_text(encoding='utf-8')) if b.strip()]
assert bl[0] == '# Dissolution and Exit' and bl[1].startswith('[image 18]') and len(bl) == 9
IDS = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
text = dict(zip(IDS, bl[2:]))
R3 = 'review-r3/DISPOSITIONS-r3.md'
FIX = {
 'P1': [("Dissolution is something founders probably don’t want to talk about",
         "Dissolution is something founders rarely want to talk about",
         'trace T1: "probably don\'t want" made the published pattern ("rarely want to discuss") a guess; the trace\'s own fix')],
 'P2': [("If the commune dissolves,", "If the community dissolves,",
         'trace T1: the published "If the community ends"; "commune" narrowed the questions'),
        ("Who takes responsibility for bridging gaps in food, housing, care, external income/benefits, etc., if applicable?",
         "Who takes responsibility for tiding people over until they’re housed and settled again, including with outside "
         "cash or benefits, if relevant?",
         'trace T1: "etc." opened the published closed list; both cold reads paused at "bridging gaps in food, housing, care", '
         'which the two questions just before it already ask about (a place to live, food, medications and care). The '
         'published "bridges food, housing, care, outside cash or benefits if relevant" said plainly: to tide people over is '
         'to carry them across the gap in what those questions name, and the published "outside cash" and "if relevant" are '
         'back, with "housed" (key U4: the published "keeps people housed"). Its own list of food, housing and care went: with the buildings list it made two lists of three in the '
         'paragraph (linter E125, FAIL)'),
        ("for ensuring obligations to the land are met,", "for making sure land obligations are met,",
         'trace T1: "obligations to the land" read as duties owed to the land; the published "land obligations" (taxes, leases, '
         'covenants too). Both cold reads paused at "obligations to the land"')],
 'P5': [("Institutions and the relationships that make them up don’t have to die at the same time.",
         "Institutions and relationships don’t die at the same time.",
         'trace T3: "don\'t have to" made the published fact ("do not die at the same time") a possibility, and "the '
         'relationships that make them up" narrowed the published "relationships" and added a claim; the published words'),
        ("American Commune follows two sisters", "The film *American Commune* follows two sisters",
         'both cold reads paused at "American Commune follows two sisters": v2 lost the published italics, so it read as a '
         'group, not a title. The italics back, and "The film" from the reading list at the end, which gives its YouTube link'),
        ("The communal economy they were born into had changed dramatically,", "The communal economy had changed dramatically,",
         'trace T3: "they were born into" was a new fact, and "they" could be the former members; the published words')],
}
P7_HEAD = "Even after the community ends as a legal entity, some of what people learned to give one another may "
ENDINGS = {
 'W1': ("My father carried the Bruderhof with him long after he left it. It shaped the foundation he started, the film he "
        "made, the places he took me, and the questions I’m still asking.",
        P7_HEAD + "go on. I hope so, anyway."),
 'W2': ("My father carried the Bruderhof with him long after he left it. It shaped the foundation he started and the film he "
        "made. It shaped the places he took me, too, and the questions I’m still asking (as you may have noticed!).",
        P7_HEAD + "go on. I hope so, anyway."),
 'W3': ("My father carried the Bruderhof with him long after he left it. It shaped the foundation he started, and *Where’s "
        "Utopia?*, the film he made. It shaped the places he took me. And it’s shaped the questions I’m still asking, as "
        "you’ve probably noticed by now!",
        "The community can end as a legal entity, and some of what people learned to give one another may still go on. I "
        "like to think so, anyway."),
 'W5': ("My father carried the Bruderhof with him long after he left it. I can see it in the foundation he started and the "
        "film he made, and in the places he took me. And honestly, I can see it in the questions I’m still asking.",
        P7_HEAD + "go on. That’s what I’m hoping for, at least."),
}
WHY_P7 = ('both cold reads paused at "the legal entity", which after P6 could be the Bruderhof\'s; "the community" says whose '
          '(P2\'s word). The published "may continue" back for v2\'s "can go on" (U17 keeps "go on"), and the break is the '
          'writer\'s hedge on that "may", not v2\'s "That gives me hope." (P6 and P7 read AI together, 301g)')
log = []
for pid, fixes in FIX.items():
    for old, new_s, why in fixes:
        assert text[pid].count(old) == 1, (pid, old)
        text[pid] = text[pid].replace(old, new_s)
        log.append({'id': pid, 'old': old, 'new': new_s, 'why': why, 'disposition': R3})
for w, (p6, p7) in ENDINGS.items():
    t = dict(text, P6=p6, P7=p7)
    (HERE / ('v3-%s.md' % w)).write_text('\n\n'.join(bl[:2] + [t[p] for p in IDS]) + '\n', encoding='utf-8')
    log.append({'id': 'P6', 'ending': w, 'old': text['P6'], 'new': p6, 'why': 'ending %s (docstring)' % w})
    log.append({'id': 'P7', 'ending': w, 'old': text['P7'], 'new': p7, 'why': WHY_P7})
(HERE / 'v3-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for p in ['P1', 'P2', 'P5']:
    print('%s %3d words | %s' % (p, len(text[p].split()), text[p][:200]))
for w, (p6, p7) in ENDINGS.items():
    print('%s P6 %d words, P7 %d words' % (w, len(p6.split()), len(p7.split())))
print(len(log), 'entries')
