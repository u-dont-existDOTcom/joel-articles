"""Section 2 v3 (2026-10-01, after Joel's answers of 14:49).

Joel's rulings: every paragraph passes alone (no section-only pass); wording can flex if the meaning is kept; in the
AI paragraph keep jobs, relationships and future outlook, feeds can go (the 1972 line is "witty altho it's kind of an
obvious ai quip": his decision is pending, so it's tested both ways); keep his C8 line; "coming to Africa, where I'm
at."; "my land" stays. He rewrote C10 and C11 himself.

This script writes the candidates that don't come from the writers:
- Joel's C10 and C11 (C10 with "leaching" spelled "leeching");
- Emulate-based versions of C1, C4 and C9 with small logged fixes (EMULATE-FALLBACK section 4, step 4): only the
  fact, invention, strength and referent fixes, no source sentence put back whole (the v2.1 lesson);
- the texts for Pangram in r4/.
"""
import json, pathlib, sys, re
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/home/claude/work'); import mdplain
U_SG = 'https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf'
P = {
 'C10j': "Communal ownership entails folks taking on visible and named stewardship duties. It requires knowing what to do if someone is leeching off the group and how to deal with it. It requires developing healthier forms of relationships. No, taking away the idea of a boss does not make everyone less passive, selfish, steal less, or try to act helpless.",
 'C11j': "People want to go back to the old way of living, but they have no idea why it failed or what to do when someone wants to own land, they run out of money, a baby is born or someone thinks they own something. They just know they are tired and alone and want to change it.",
 'C1e1': f"The same longing that motivated my dad to make his film is in the air again. In 2023, the [U.S. Surgeon General]({U_SG}) declared that about half of American adults are lonely, and made social connection a health imperative.",
 'C1e2': f"Do you remember the movie my dad made a while ago about how people were longing for village? It's happening again. The [U.S. Surgeon General]({U_SG}) released a 2023 advisory on loneliness, declaring that about half of American adults are experiencing it, and that we need to work on cultivating social connection as a matter of public health.",
 'C4e1q': "I have no proof that the rise of AI caused this uptick, but it’s hard to ignore the coincidence in timing. AI became serious around this time, and it started changing people’s jobs and relationships, and how they see the future. Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan.",
 'C4e1p': "I have no proof that the rise of AI caused this uptick, but it’s hard to ignore the coincidence in timing. AI became serious around this time, and it started changing people’s jobs and relationships, and how they see the future. Suddenly, forming a village sounded like a backup plan.",
 'C9e1': "That comment applies more to large-scale experiments in socialism than the small-scale version of communes. But it deserves a serious answer, because some people want to wash their hands of responsibility. Also, with everybody theoretically responsible for everything, lines of responsibility may become obscure, so that the same three people end up doing all the maintenance while the rest sit around expounding on the nature of freedom. This may endow the informal leaders with more power than they would otherwise have, partly because everybody's giving it to them.",
 'C9e2': "While that comment is more applicable to large-scale experiments in socialism than in small communes, it deserves a serious answer anyway, as some people just prefer to not be responsible. It’s also a problem in many communes that everyone owns everything, which means responsibility gets distributed to a handful of people who end up becoming the de-facto leaders anyway, partly due to everyone else abdicating responsibility.",
}
FIX = {
 'C10j': 'Joel\'s own (2026-10-01 14:49). One spelling fix: "leaching" to "leeching" (to leech is to live off someone; to leach is to drain out of soil). His "or try to act helpless" is left as he wrote it and asked about: as written, the boss going "does not make everyone ... try to act helpless", the opposite of what he means.',
 'C11j': 'Joel\'s own (2026-10-01 14:49), unchanged.',
 'C1e1': 'Emulate 0201-A, P1 (passed Pangram in its whole output, 2026-09-29). Fixes: "intense" cut (hype); "this film a few years ago" to "his film" (the film is from 1988, and "this" had nothing to refer to); "the US surgeon general" capitalized, with the link; "50% of Americans are lonely" to "about half of American adults are lonely" (the advisory\'s figure is roughly half of U.S. adults). Kept as wording: "motivated my dad to make" for "shaped my father\'s", "in the air" for "suddenly everywhere", "made social connection a health imperative" for "treated social connection as a public-health issue rather than a sentimental extra".',
 'C1e2': 'Emulate 0201-B, P1 (passed in its whole output). Fixes: "just released" to "released" (2023 isn\'t "just"); "about 50% of Americans" to "about half of American adults"; "It\'s happening again." added, because the version dropped the point that the longing is back; "again" moved out of the film\'s time. Kept as wording: the question opener, "longing for village", "a matter of public health".',
 'C4e1q': 'Emulate 0201-A, P4. Fixes: "is connected to this uptick" to "caused this uptick" (Joel\'s claim is about cause); "now it\'s radically changing the way we live" to "it started changing people\'s jobs and relationships, and how they see the future" (Joel: keep jobs, relationships and future outlook; feeds can go; "radically" cut as hype; the tense fixed). Joel\'s 1972 line kept, word for word.',
 'C4e1p': 'As C4e1q, with the 1972 line replaced by its point said plainly: "Suddenly, forming a village sounded like a backup plan." (Joel called the line "witty altho it\'s kind of an obvious ai quip"; his decision is pending.)',
 'C9e1': 'Emulate c9-emuB (2026-10-01, from the v2.1 text). Fixes: "That would probably apply" to "That comment applies" (after Joel\'s seminar line, "That" would point at the seminar; "probably" was Emulate\'s hedge); "it\'s worth answering" to "it deserves a serious answer" (strength); "three or four people end up doing the lawn maintenance and plumbing repairs" to "the same three people end up doing all the maintenance" (the lawn and the plumbing were invented examples; Joel\'s "the same three people" back); "since everybody\'s giving it to them" to "partly because everybody\'s giving it to them" (Joel\'s "partly"). Kept as wording: "wash their hands of responsibility", "expounding on the nature of freedom", "endow the informal leaders with more power than they would otherwise have".',
 'C9e2': 'Emulate 0202-B, P4. Fixes: "this comment" to "that comment" (the one in the image); "far more" to "more" (hype); "it\'s worth responding to anyway" to "it deserves a serious answer anyway"; "simply due to" to "partly due to" (Joel\'s "partly"). It doesn\'t have "the same three people ... discusses freedom": a handful of people doing everything carries the point, the image is gone.',
}
OUT = HERE / 'r4'; OUT.mkdir(exist_ok=True)
C2 = (HERE / 'C2.txt').read_text(encoding='utf-8').strip()
C3 = (HERE / 'trace-C3.txt').read_text(encoding='utf-8').strip()
C8o = 'The commune comments became a miniature political-philosophy seminar, as Instagram comments sometimes do.'
words = {}
def put(name, md):
    t = mdplain.plain(md).strip(); (OUT / (name + '.txt')).write_text(t + '\n', encoding='utf-8'); words[name] = len(t.split())
for k in ('C10j', 'C11j', 'C1e2', 'C4e1q', 'C4e1p', 'C9e1', 'C9e2'):
    put(k, P[k])
for k in ('C1e1', 'C1e2'):
    put(k + '-C2', P[k] + '\n\n' + C2)
for k in ('C4e1q', 'C4e1p'):
    put('C3-' + k, C3 + '\n\n' + P[k])
json.dump(dict(texts=P, fixes=FIX), open(HERE / 'fixlog-v3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(words)

# --- after the first v3 checks (r4, 2026-10-01 15:07-15:17): C3 is what flags the C3-C4 pairs (every C4 that passed
# alone failed after it), so two Emulate-based C3s with small fixes, checked in pairs with both C4s.
U_ECO = 'https://trends.google.com/explore?q=ecovillage&date=all&geo=Worldwide'
U_IC = 'https://trends.google.com/explore?q=intentional%20community&date=all&geo=Worldwide'
P['C3e2'] = f"Check out the Google Trends for “[ecovillage]({U_ECO})” and “[intentional community]({U_IC})”. After years of decline, interest is climbing sharply in the mid-2020s."
P['C3e3'] = f"Did you notice, by the way, that the graph of Google searches for “[ecovillage]({U_ECO})” and “[intentional community]({U_IC})” starts bending upwards rapidly in the mid-’20s after having drifted downward for years? (Graphs from Google Trends.)"
FIX['C3e2'] = 'Emulate 0201-B, P3. Fixes: "google trends" capitalized; the two terms in quotation marks, with their links; "skyrocketing" to "climbing sharply" (hype; Joel\'s "sharply"). Kept as wording: "Check out", "After years of decline", the present tense (it is the mid-2020s).'
FIX['C3e3'] = 'Emulate c3c4-emuA (2026-10-01), P1. Fix: "Google hits" to "Google searches" (Trends measures searches). Kept as wording: the question, "by the way", "rapidly", "(Graphs from Google Trends.)".'
C8o = 'The commune comments became a miniature political-philosophy seminar, as Instagram comments sometimes do.'
SEBA = [p for p in (HERE.parent.parent / 'sections/003-original.md').read_text(encoding='utf-8').split('\n\n') if p.startswith('It’s poppin’')][0].strip()
P['SEBAj'] = SEBA.replace('I don’t think she’s coming to Africa.', 'I don’t think she’s coming to Africa, where I\'m at.')
assert P['SEBAj'] != SEBA
FIX['SEBAj'] = 'Joel\'s own paragraph, with his edit of 2026-10-01 14:49: "coming to Africa, where I\'m at."'
C9w1 = (HERE / 'writers-r3/C9/w1.txt').read_text(encoding='utf-8').strip()
for c3 in ('C3e2', 'C3e3'):
    for c4 in ('C4e1p', 'C4e1q'):
        put(c3 + '-' + c4, P[c3] + '\n\n' + P[c4])
put('C8o-C9w1', C8o + '\n\n' + C9w1)
put('SEBAj', P['SEBAj'])
json.dump(dict(texts=P, fixes=FIX), open(HERE / 'fixlog-v3.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print({k: words[k] for k in words if k.startswith(('C3e', 'C8o', 'SEBA'))})
