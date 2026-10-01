"""Community section 2 ("Communes Are Hot Again"), v1: Emulate first (GPT's website versions 0201/0202 A/B),
with Joel's rulings (docs/HUMANIZATION-GATE.md, owner rulings 2026-09-30) applied as logged fixes."""
import json, sys
sys.path.insert(0, '/home/claude/work'); import mdplain
SRC = open('../../sections/003-original.md', encoding='utf-8').read().strip()
U_SG = 'https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf'
U_ECO = 'https://trends.google.com/explore?q=ecovillage&date=all&geo=Worldwide'
U_IC = 'https://trends.google.com/explore?q=intentional%20community&date=all&geo=Worldwide'
U_IG2 = 'https://instagram.com/p/DaLvZV2qIk2/'
src = SRC.split('\n\n')
img = {k: [p for p in src if p.startswith('[image %d]' % k)][0] for k in (4, 5, 6)}
seba = [p for p in src if p.startswith('It’s poppin’ on Instagram')][0]
P = {
 'C1a': f"The longing that shaped my father’s film is suddenly in the air again. In 2023, the [U.S. Surgeon General’s advisory]({U_SG}) reported that roughly half of American adults experience loneliness, and treated social connection as a public-health issue rather than a sentimental extra.",
 'C1b': f"The longing that shaped my father’s film is suddenly in the air again. In 2023, the [U.S. Surgeon General’s advisory]({U_SG}) reported that roughly half of American adults experience loneliness, and treated social connection as a public-health issue.",
 'C2': "Whether you want to call that loneliness an “epidemic” or not, it’s obvious that a lot of people can’t tolerate modern life in isolation anymore. People may disagree about politics, food, God, sex, or whether shoes are oppressive, but they agree that something about the way things are now is starvin’ them.",
 'C3': f"If you look at Google Trends for “[ecovillage]({U_ECO})” and “[intentional community]({U_IC})”, you can see that interest drifted down for years, then bent upward sharply in the mid-2020s.",
 'C4a': "I have no proof that AI caused this turn, but it’s hard to ignore the timing. That’s around when AI stopped being a tech-news curiosity and started reorganizing people’s jobs, feeds, relationships, and expectations of the future. Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan.",
 'C4b': "I have no proof that AI caused this turn, but it’s hard to ignore the timing. That’s around when AI stopped being a tech-news curiosity and started changing the way people live. Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan.",
 'C6': f"Then another large influencer [floated the commune idea]({U_IG2}), and the comments started turning into a recruitment board. People were finding future members under a post, the way you’d normally find a second-hand sofa.",
 'C7a': "Not everybody in the comments was trying to join. The oldest objection came up almost immediately: maybe most people don’t want the responsibility that anarchism requires, and communal property ends up “owned by everyone, cared for by nobody.”",
 'C7b': "Not everyone commented with interest. The oldest objection came up almost immediately: the idea that maybe most people don’t want the responsibility a working anarchism would require of them, and that communal property ends up “owned by everyone, cared for by nobody.”",
 'C8o': "The commune comments became a miniature political-philosophy seminar, as Instagram comments sometimes do.",
 'C8': "Those comments became a little seminar on political philosophy, which you don’t normally find on Instagram.",
 'C9a': "While this objection is more applicable to large-scale experiments in socialism than to small communes, it deserves a serious answer anyway, since some people really would rather let somebody else take responsibility. Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom. Informal leaders then gain power partly because everyone keeps handing it to them.",
 'C9b': "While this objection is more applicable to large-scale experiments in socialism than to small communes, it deserves a serious answer anyway, since some people really would rather let somebody else take responsibility. Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom, and informal leaders gain power partly because everyone keeps handing it to them.",
 'C10a': "Communal ownership needs named stewardship and visible duties, and consequences for chronic freeloading. It also needs enough relational capacity to confront the problem before resentment becomes the real government. A community can’t run on the assumption that getting rid of bosses gets rid of passivity, selfishness, theft, or learned helplessness.",
 'C10b': "Communal ownership needs named stewardship and visible duties, and consequences for chronic freeloading. It also needs enough relational capacity to confront the problem before resentment becomes the real government. It’s naive to think that getting rid of bosses will get rid of passivity, selfishness, theft, or learned helplessness.",
 'C11a': "The desire to go back to a natural way of living together has outrun the knowledge of how to actually do it. People know they’re lonely and exhausted. They usually don’t know why so many earlier communities failed, why the same conflicts keep coming back, or how quickly beautiful land stops mattering once money, children, jealousy and ownership come into it.",
 'C11b': "The desire to go back to a natural way of living together has outrun the knowledge of how to actually do it. People know they’re lonely and exhausted. They usually don’t know why so many earlier communities failed, or why the same conflicts keep coming back. And they don’t see how quickly beautiful land stops mattering once money, children, jealousy and ownership come into the picture.",
 'C12': "I am not currently recruiting for a community or attempting to start one, which makes it easier for me to write an article like this, since I’m not trying to get you onto my land. I do plan to buy land, and people may naturally end up living near me. But all of the warnings in this article apply to me, too.",
}
WHY = {
 '_about': 'Section 2 v2 (2026-10-01). v1 = Emulate versions with logged fixes; v2 = the fixes for the blind trace of v1 (scratchpad s2-trace.md, copied to v1/TRACE-v1.md). Each entry: where the text comes from, then the fixes. Joel\'s published text is sections/003-original.md.',
 'C1': 'Emulate 0201-A, P1. v1: "a few years ago" was false (the film is from 1988); "intense" (hype) dropped; "my dad" back to "my father"; the advisory\'s claim back to the source\'s wording; link restored. v2 (trace): "the same longing that pushed my father to make that film" back to Joel\'s "the longing that shaped my father\'s film" ("pushed ... to make" was a new causal claim, and "that film" had no referent in this section); "suddenly" restored. a keeps "rather than a sentimental extra"; b drops it (a cut, needs Joel\'s OK).',
 'C2': 'Emulate 0201-A, P2. v1: the list back to Joel\'s items. v2 (trace): "This seems to be true regardless of politics, food..." had dropped that people disagree and added a hedge; back to Joel\'s "People may disagree about politics, food, God, sex, or whether shoes are oppressive, but they agree that something about..."; "it" given its referent ("that loneliness"); "any more" to "anymore". Kept from Emulate: "Whether you want to call that loneliness an epidemic or not" for Joel\'s "I\'m less interested in declaring an official epidemic than in the obvious fact underneath it" (same job: the label doesn\'t matter, the fact does; his first person is lost, flagged), and "starvin\'" (open question).',
 'C3': 'Emulate 0201-A, P3. v1: links restored. v2 (trace): "terms like" (broader) back to Joel\'s two terms; "dramatically" back to "sharply"; "after a long decline" back to "drifted down for years"; present perfect with "mid-2020s" fixed.',
 'C4': 'Emulate 0201-A, P4. v1: Joel\'s "1972 leftover ... backup plan" line put back. v2 (trace): "connected to this uptick" back to "caused this turn" (Joel\'s claim is about cause); "AI became serious" back to "stopped being a tech-news curiosity"; tense fixed. a restores Joel\'s four areas ("jobs, feeds, relationships, and expectations of the future"); b keeps Emulate\'s "changing the way people live" (drops the four, needs Joel\'s OK).',
 'C6': 'Emulate 0202-B, P1 (keeps the sofa line). v1: "even bigger" and "on Instagram" were invented; link restored. v2 (trace): "brought it up" (no referent) back to Joel\'s "floated the commune idea"; "flooded the comments" (volume not in the source) back to "the comments started turning into a recruitment board"; "their communes" (ownership not in the source) cut; "trying to find" back to "finding". Cut, needs Joel\'s OK: "It was chaotic, sincere, and revealing." (recommend deleting).',
 'C7': 'Emulate 0202-A, P2. v1: "maybe most people" put back; the commenter\'s words put back. v2 (trace): the quoted line back inside the objection and inside "maybe" (Emulate made it a flat claim in nobody\'s voice); "response to this idea" (no referent) back to "objection"; "pretty quickly" back to "almost immediately"; the long conditional ("if we actually had a functioning anarchism where...") cut back to Joel\'s "the responsibility anarchism requires". a is close to Joel\'s sentence; b keeps more of Emulate\'s shape.',
 'C8': 'Emulate 0202-A, P3. Emulate turned Joel\'s "as Instagram comments sometimes do" into "which you don\'t normally find on Instagram"; the candidate keeps that (Joel\'s line is wry, which he bans) and asks him. "This led to some interesting comment-thread discussions" (v1) back to Joel\'s seminar image. C8o is his line, checked in the pair for comparison. The opener is "Those comments", not "The thread": with "The", three paragraphs of the section opened the same way (linter B13, a hard fail).',
 'C9': 'Emulate 0202-B, P4. v1: "far more" back to "more"; Joel\'s "same three people ... discusses freedom" put back. v2 (trace): "it\'s worth responding to anyway, as some people just prefer not to be responsible" back to Joel\'s "deserves a serious answer" and "some people really would rather let somebody else take responsibility"; "this comment" to "this objection". a keeps his informal-leaders sentence; b joins it to the sentence before.',
 'C10': 'Emulate 0202-A, P5, rebuilt in v1 (what communal ownership needs, put back as two sentences; "learned helplessness"; Emulate\'s "very tired very fast" cut). v2 (trace): "It\'s naive to think" (a judgment of people, not in the source) back to Joel\'s "A community can\'t run on the assumption that..." in a; b keeps "naive" (needs Joel\'s OK).',
 'C11': 'Emulate 0202-B, P6, rebuilt in v1. v2 (trace): "Another problem is that" (added) cut; scare quotes on "natural" (not in the source) removed; "Most don\'t know" back to "They usually don\'t know"; "so many earlier communities failed" restored; "come into the mix" back to "come into it"; "kids" back to Joel\'s "children". a keeps one list sentence; b splits it.',
 'C12': 'Emulate 0202-A, P7. v1: the invented feeling and timing cut; "get you onto my land" put back. v2: unchanged.',
}
CHOICE = dict(c1='C1a', c4='C4a', c7='C7a', c9='C9a', c10='C10a', c11='C11a')  # a before b; change after Pangram
def section(c1, c4, c7, c9, c10, c11):
    parts = ['# Communes Are Hot Again 🔥', P[c1], P['C2'], P['C3'], img[4], P[c4], seba, P['C6'], '### The Freeloader Problem', P[c7], img[5], P['C8'], P[c9], P[c10], P[c11], P['C12'], img[6]]
    return '\n\n'.join(parts)
MUST = ['shaped my father’s film', 'disagree about politics', 'sharply', 'caused this turn', '1972 leftover', 'backup plan', 'floated the commune idea', 'started turning into a recruitment board', 'finding future members', 'second-hand sofa', 'oldest objection', 'almost immediately', 'maybe most people', 'owned by everyone, cared for by nobody', 'deserves a serious answer', 'let somebody else take responsibility', 'same three people maintain everything while everybody else discusses freedom', 'named stewardship', 'before resentment becomes the real government', 'learned helplessness', 'lonely and exhausted', 'usually don’t know', 'so many earlier communities', 'beautiful land', 'get you onto my land', 'warnings in this article apply to me', 'roughly half of American adults', 'I applied']
MUSTNOT = ['a few years ago', '50% of Americans', 'even bigger', 'his post', 'I’m okay with the idea', 'at some point', 'skyrocketing', 'far outstrips', 'far more applicable', 'intense longing', 'very tired very fast', 'proclivities', 'pushed my father', 'dramatically', 'uptick', 'radically', 'flooded', 'response to this idea', 'worth responding to', 'Another problem is that', 'seems to be true', 'that film', 'This led to', 'any more', 'pretty quickly', 'their communes', 'brought it up']
names = []
def build(c1, c4, c7, c9, c10, c11):
    md = section(c1, c4, c7, c9, c10, c11); name = 'section-' + '-'.join((c1, c4, c7, c9, c10, c11))
    miss = [m for m in MUST if m not in md]; bad = [m for m in MUSTNOT if m in md]
    assert not miss and not bad, (name, miss, bad)
    open(name + '.md', 'w', encoding='utf-8').write(md + '\n'); open(name + '.txt', 'w', encoding='utf-8').write(mdplain.plain(md).strip() + '\n'); names.append(name)
    return name
CHOSEN = build(**CHOICE)
words = {}
def alone(name, md):
    t = mdplain.plain(md).strip(); open(name + '.txt', 'w', encoding='utf-8').write(t + '\n'); words[name] = len(t.split())
for k in ('C2', 'C4a', 'C4b', 'C7a', 'C7b', 'C9a', 'C9b', 'C10a', 'C10b', 'C11a', 'C11b', 'C12'):
    alone(k, P[k])
for k in ('C1a', 'C1b', 'C3', 'C6', 'C8'):
    alone('trace-' + k, P[k])
alone('C1a-C2', P['C1a'] + '\n\n' + P['C2']); alone('C1b-C2', P['C1b'] + '\n\n' + P['C2'])
alone('C3-C4a', P['C3'] + '\n\n' + P['C4a']); alone('C3-C4b', P['C3'] + '\n\n' + P['C4b'])
alone('C6-C7a', P['C6'] + '\n\n' + P['C7a']); alone('C6-C7b', P['C6'] + '\n\n' + P['C7b'])
alone('C8-C9a', P['C8'] + '\n\n' + P['C9a']); alone('C8o-C9a', P['C8o'] + '\n\n' + P['C9a']); alone('C8-C9b', P['C8'] + '\n\n' + P['C9b'])
json.dump(WHY, open('fixlog-s2.json', 'w'), indent=1, ensure_ascii=False)
json.dump(dict(note='Checks from the fix log (the trace and Emulate\'s inventions), not Joel\'s edits: Joel has given none for this section yet.', must=MUST, must_not=MUSTNOT), open('fix-checks-s2.json', 'w'), indent=1, ensure_ascii=False)
print(words); print('section:', CHOSEN, len(open(CHOSEN + '.txt', encoding='utf-8').read().split()), 'words')
