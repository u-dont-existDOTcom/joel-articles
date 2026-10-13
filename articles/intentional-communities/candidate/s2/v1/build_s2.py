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
 'C1a': f"The same longing that pushed my father to make that film is in the air again. In 2023, the [U.S. Surgeon General’s advisory]({U_SG}) reported that roughly half of American adults experience loneliness, and treated social connection as a public-health issue rather than a sentimental extra.",
 'C1b': f"The same longing that pushed my father to make that film is in the air again. In 2023, the [U.S. Surgeon General’s advisory]({U_SG}) reported that roughly half of American adults experience loneliness, and made social connection a public-health issue.",
 'C2': "Whether you want to call it an epidemic or not, it’s obvious that a lot of people simply cannot tolerate modern life in isolation any more. This seems to be true regardless of politics, food, God, sex, or whether shoes are oppressive. People agree that the way things are now is starvin’ them.",
 'C3': f"If you look at Google Trends for terms like “[ecovillage]({U_ECO})” or “[intentional community]({U_IC})”, you can see that after a long decline in interest, the curve has bent upward dramatically in the mid-2020s.",
 'C4': "I have no proof that the rise of AI is connected to this uptick, but it’s hard to ignore the coincidence in timing. AI became serious around this time, and now it’s radically changing the way we live. Suddenly “maybe we should form a village” sounded less like a 1972 leftover and more like a backup plan.",
 'C6': f"Then another large influencer [brought it up]({U_IG2}). People flooded the comments, essentially trying to find other people to join their communes, the way you’d normally find a second-hand sofa.",
 'C7': "Not everyone commented with interest. The oldest response to this idea came up pretty quickly: the idea that maybe most people don’t want the responsibility that would be required of them if we actually had a functioning anarchism where we could have true communal ownership of property. Communal property becomes “owned by everyone, cared for by nobody.”",
 'C8': "This led to some interesting comment-thread discussions about political philosophy, which you don’t normally find on Instagram.",
 'C9a': "While this comment is more applicable to large-scale experiments in socialism than to small communes, it’s worth responding to anyway, as some people just prefer not to be responsible. Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom. Informal leaders then gain power partly because everyone keeps handing it to them.",
 'C9b': "While this comment is more applicable to large-scale experiments in socialism than to small communes, it’s worth responding to anyway, as some people just prefer not to be responsible. Shared ownership can blur responsibility until the same three people maintain everything while everybody else discusses freedom, and those few end up as the de facto leaders, partly because everyone else keeps handing them the job.",
 'C10': "Communal ownership needs named stewardship and visible duties, and consequences for chronic freeloading. It also needs enough relational capacity to confront the problem before resentment becomes the real government. It’s naive to think that simply eliminating the possibility of having a “boss” will eliminate the potential for people to be passive, selfish or thieving, or to fall into learned helplessness.",
 'C11a': "Another problem is that the desire to go back to a more “natural” way of living together has outstripped people’s knowledge of how to actually do it. People know they’re lonely and exhausted. Most don’t know why past attempts have failed, or why the same conflicts keep coming back, or how quickly beautiful land stops mattering once money, kids, jealousy and questions about ownership come into the mix.",
 'C11b': "Another problem is that the desire to go back to a more “natural” way of living together has outstripped people’s knowledge of how to actually do it. People know they’re lonely and exhausted. Most don’t know why past attempts have failed, or why the same conflicts keep coming back. They don’t see how quickly beautiful land stops mattering once money, kids, jealousy and ownership come into it.",
 'C12': "I am not currently recruiting for a community or attempting to start one, which makes it easier for me to write an article like this, since I’m not trying to get you onto my land. I do plan to buy land, and people may naturally end up living near me. But all of the warnings in this article apply to me, too.",
}
WHY = {
 'C1': 'Emulate 0201-A, P1. Fixed: "a few years ago" was false (the film is from 1988); "intense" (hype) dropped; "my dad" back to "my father" as in section 1; the advisory\'s claim back to the source\'s wording ("roughly half of American adults experience loneliness", not "50% of Americans are lonely"); link restored. a keeps "rather than a sentimental extra"; b drops it.',
 'C2': 'Emulate 0201-A, P2. Fixed: the list back to Joel\'s items ("politics, food, God, sex, or whether shoes are oppressive"); Emulate had lengthened it. "starvin\'" kept: Joel writes "poppin\'" in this section.',
 'C3': 'Emulate 0201-A, P3. Links restored; "Google Trends" capitalized.',
 'C4': 'Emulate 0201-A, P4, plus Joel\'s line put back: "Suddenly maybe we should form a village sounded less like a 1972 leftover and more like a backup plan" (both versions dropped it).',
 'C6': 'Emulate 0202-B, P1 (keeps the sofa joke). Fixed: "even bigger" was invented; "on Instagram" after the sofa was invented; link restored. Dropped with it: "It was chaotic, sincere, and revealing." (recommend deleting).',
 'C7': 'Emulate 0202-A, P2. Fixed: "maybe most people" put back (Emulate dropped the hedge); one of two "actually"s cut; the commenter\'s words put back ("owned by everyone, cared for by nobody").',
 'C8': 'Emulate 0202-A, P3, past tense. Both versions turned "as Instagram comments sometimes do" into "which you don\'t normally find on Instagram".',
 'C9': 'Emulate 0202-B, P4. Fixed: "far more" back to "more"; Joel\'s "same three people ... discusses freedom" put back. a keeps his informal-leaders sentence; b folds it into one sentence.',
 'C10': 'Emulate 0202-A, P5, rebuilt. Both versions dropped what communal ownership needs; put back as two sentences ("named stewardship and visible duties, and consequences for chronic freeloading" / "enough relational capacity ... before resentment becomes the real government"). "helpless" back to "learned helplessness". Emulate\'s added "the people doing the work will get very tired very fast" cut.',
 'C11': 'Emulate 0202-B, P6, rebuilt. "far outstrips" (stronger than "has outrun") back to plain; "People know they\'re lonely and exhausted" and "why the same conflicts keep coming back" and "how quickly beautiful land stops mattering" put back. a keeps one list sentence; b splits it.',
 'C12': 'Emulate 0202-A, P7. Fixed: "I\'m okay with the idea that people may naturally be drawn" was an invented feeling, back to "people may naturally end up living near me"; "at some point" was invented timing; Joel\'s "since I\'m not trying to get you onto my land" put back.',
}
def section(c1, c9, c11):
    parts = ['# Communes Are Hot Again 🔥', P[c1], P['C2'], P['C3'], img[4], P['C4'], seba, P['C6'], '### The Freeloader Problem', P['C7'], img[5], P['C8'], P[c9], P['C10'], P[c11], P['C12'], img[6]]
    return '\n\n'.join(parts)
MUST = ['1972 leftover', 'backup plan', 'second-hand sofa', 'same three people maintain everything while everybody else discusses freedom', 'before resentment becomes the real government', 'get you onto my land', 'roughly half of American adults', 'maybe most people', 'owned by everyone, cared for by nobody', 'learned helplessness', 'lonely and exhausted', 'beautiful land', 'Every warning' if False else 'warnings in this article apply to me', 'named stewardship', 'my father', 'I applied']
MUSTNOT = ['a few years ago', '50% of Americans', 'even bigger', 'his post', "I’m okay with the idea", 'at some point', 'skyrocketing', 'far outstrips', 'far more applicable', 'intense longing', 'very tired very fast', 'proclivities']
os_ = __import__('os')
for c1 in ('C1a', 'C1b'):
    for c9 in ('C9a', 'C9b'):
        for c11 in ('C11a', 'C11b'):
            md = section(c1, c9, c11); name = f'section-{c1}-{c9}-{c11}'
            miss = [m for m in MUST if m not in md]; bad = [m for m in MUSTNOT if m in md]
            assert not miss and not bad, (name, miss, bad)
            open(name + '.md', 'w', encoding='utf-8').write(md + '\n')
            open(name + '.txt', 'w', encoding='utf-8').write(mdplain.plain(md).strip() + '\n')
words = {}
def alone(name, md):
    t = mdplain.plain(md).strip(); open(name + '.txt', 'w', encoding='utf-8').write(t + '\n'); words[name] = len(t.split())
for k in ('C1a', 'C1b', 'C2', 'C3', 'C4', 'C7', 'C10', 'C11a', 'C11b', 'C12'):
    alone(k, P[k])
alone('C6-C7', P['C6'] + '\n\n' + P['C7'])
alone('C8-C9a', P['C8'] + '\n\n' + P['C9a']); alone('C8-C9b', P['C8'] + '\n\n' + P['C9b'])
json.dump(WHY, open('fixlog-s2.json', 'w'), indent=1, ensure_ascii=False)
json.dump(dict(must=MUST, must_not=MUSTNOT), open('owner-edits-s2.json', 'w'), indent=1, ensure_ascii=False)
print(words)
