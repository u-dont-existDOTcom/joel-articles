"""Section 1, v3: Joel's rulings of 2026-09-30 18:58 UTC applied to v2 (002-section-candidate.md)."""
import json, re, subprocess, sys
sys.path.insert(0, '/home/claude/work'); import mdplain
V2 = open('002-section-candidate.md', encoding='utf-8').read()
log = []
def fix(text, old, new, why):
    assert text.count(old) == 1, old[:60]
    log.append(dict(before=old, after=new, why=why)); return text.replace(old, new)
U = 'https://schoolsforchiapas.org/advances/schools/la-escuelita/'
LIST = ('[Twin Oaks](https://twinoaks.org/), [Acorn](https://www.ic.org/directory/acorn-community-farm/), [East Wind](http://eastwind.org/), '
        '[Padanaram](https://www.facebook.com/p/Padanaram-100064853281734/), [Zendik](https://highlandscurrent.org/2017/05/09/leaving-zendik-farm/)')
paras = V2.split('\n\n')
def idx(start): i = [k for k, p in enumerate(paras) if p.startswith(start)]; assert len(i) == 1, start; return i[0]
P4 = {
 'D': f"That’s where the ***escuelita*** in my title comes in. *Escuelita* means “little school.” I’m borrowing the word from the Zapatistas, whose [*Escuelita*]({U}) brought outsiders into their communities to learn autonomy by living it. The healing communities I’m proposing should do the same: people live there, heal, learn the relational and practical methods, and some eventually leave to start the next one. Otherwise, we’ve built a lovely refuge for whoever got there first.",
 'C': f"That’s where the ***escuelita*** in my title comes in. The word “escuelita,” meaning “little school,” is one I’m borrowing from the Zapatistas in Mexico. Their [*Escuelita*]({U}) had outsiders come and stay in their communities for a while, learning autonomy by living it. The healing communities I’m proposing should do the same: people live there, heal, learn the relational and practical methods, and some eventually leave to start the next one. Otherwise, we’ve built a lovely refuge for whoever got there first.",
 'B': f"That’s where the ***escuelita*** in my title comes in. *Escuelita* means “little school.” I’m borrowing the word from the Zapatistas in Mexico, whose [*Escuelita*]({U}) brought outsiders into their communities for a while to learn autonomy by living it. In the same way, people would live in the healing communities I’m proposing, to heal and to learn the relational and practical methods, so that some of them could eventually leave and set up another one somewhere else. Otherwise, we’ve built a lovely refuge for whoever got there first.",
 'A': f"That’s where the ***escuelita*** in my title comes in. The word “escuelita,” meaning “little school,” is one I’m borrowing from the Zapatistas in Mexico. Their [*Escuelita*]({U}) had outsiders come and stay in their communities for a while, learning autonomy by living it. In the same way, people would live in the healing communities I’m proposing, to heal and to learn the relational and practical methods, so that some of them could eventually leave and set up another one somewhere else. Otherwise, we’ve built a lovely refuge for whoever got there first.",
}
P5 = {
 'A': f"I spent much of my childhood being carried through {LIST}, and many other communities. I was usually just a visitor’s kid, close enough to see how people lived but never quite part of the tribe. At the time that meant a lot of boredom, with some adventures mixed in, but those years gave me a great sample to compare against.",
 'B': f"I spent much of my childhood being carried through one community after another ({LIST}, and many others). Since I was usually just a visitor’s kid, close enough to see how people lived but never quite part of the tribe, there was a lot of boredom at the time, with some adventures mixed in, but those years gave me a great sample to compare against.",
}
i4, i5 = idx('This is the ***escuelita***'), idx('I grew up on shoulders')
i1, i10, i11, i12, i13, i14, i15 = (idx(s) for s in ('I just put a movie', 'The [East Wind]', 'Even at East Wind', 'There were like eight', '[Twin Oaks](https://twinoaks.org/) was big', 'One thing that struck me', 'Which meant weekly'))
paras[i1] = fix(paras[i1], 'without recreating all the loneliness', 'without recreating the same loneliness', 'my slip in v2; the source says "the same" (fix approved 18:58)')
paras[i10] = fix(paras[i10], 'enough to be diverse', 'enough to have a variety of personalities', 'Joel: "diverse sounds more like ethnically diverse ... could say diverse personalities or variety of personalities"')
paras[i10] = fix(paras[i10], 'I was very happy there.', 'I was happy there.', 'Joel: "don\'t hype up happy to very happy"')
paras[i10] = fix(paras[i10], 'in a big communal shower', 'in a communal shower', '"big" was invented (fix approved 18:58)')
paras[i11] = fix(paras[i11], 'there was a power issue. They had a nut butter factory, which was providing a lot of their income, and the woman who was running the factory was very hard to question.',
                 'there was a quieter power issue. They had a nut butter factory that brought in a lot of their income, which seemed to make the woman running it very hard to question.', 'puts back the source\'s reason and "quieter" (fix approved 18:58)')
paras[i12] = fix(paras[i12], "I didn't feel like it was really a commune I could join so much as a group of people who were already friends,", "I couldn't tell whether it was a commune I might join or a group of people who were already friends,", 'Joel: "it shouldn\'t switch couldn\'t tell for the hyped up version"')
paras[i12] = fix(paras[i12], "It would have been hard to join; it would have been more like asking whether their group chat had an opening.", "Joining would have felt less like applying to a commune than asking whether their group chat had an opening.", 'drops the added claim "hard to join", which the restored "couldn\'t tell" contradicts; the source\'s comparison back')
paras[i13] = fix(paras[i13], 'was big, like two or three hundred people, and almost institutional. It was friendly enough and interesting enough,', 'was much bigger, like two or three hundred people at the time, and almost institutional. It was friendly and interesting,', 'Joel: "shouldn\'t switch larger to big ... Bigger is ok"; "at the time" and no "enough"s (approved 18:58)')
paras[i13] = fix(paras[i13], 'It was more like a tiny hippie town, with a really complicated labor credit system.', "It was more like a tiny hippie town, but with a highly structured political system that didn't seem intuitive for hippies.", "Joel's sentence (18:58): he doesn't know the labor credit system was complicated")
paras[i14] = fix(paras[i14], 'One thing that struck me as odd about all of them, basically, was that they didn\'t have a communal therapy practice. All the usual human pain and suffering came into the commune with them,',
                 'Looking back, almost none of them had a communal therapy practice. People brought all the usual human pain and suffering in with them,', 'Joel: "you can\'t change it to say that it struck me as odd, because i was too young to have any reference point"; "them" fixed')
paras[i15] = fix(paras[i15], 'the things you wanted to talk about', 'the things you needed to talk about', 'Joel: "we can\'t change needed for wanted"')
paras[i15] = fix(paras[i15], '(Some people solved this problem', '(Some people, including me, solved this problem', 'Joel: "we could just say, Some people, including me, solved this"')

paras[i11] = fix(paras[i11], 'Otherwise I thought it had a great social life', 'Otherwise I thought the community had a great social life', 'blind trace (v3): "it" switched from the factory to East Wind between sentences')
paras[i12] = fix(paras[i12], 'at the [Acorn](https://www.ic.org/directory/acorn-community-farm/) commune when I was there', 'at [Acorn](https://www.ic.org/directory/acorn-community-farm/) when I was there', 'blind trace (v3): calling it "the Acorn commune" clashed with "I couldn\'t tell whether it was a commune"; the source doesn\'t call it one there')
paras[i14] = fix(paras[i14], 'Looking back, almost none of them had', 'Looking back, almost none of these communities had', 'blind trace (v3): "them" had nothing to refer to after the Twin Oaks paragraph')
paras[i14] = fix(paras[i14], 'People brought all the usual human pain and suffering in with them,', 'People brought the usual human pain and suffering with them,', 'blind trace (v3): "in" had no destination, and "all" came twice')
MUST = ['the same loneliness', "That’s where the ***escuelita*** in my title comes in.", 'borrowing', 'learn', 'autonomy by living it', 'I’m proposing', 'relational and practical methods', 'being carried through', 'many other', 'usually just a visitor', 'never quite part of the tribe', 'adventures mixed in',
        'variety of personalities', 'I was happy there.', 'quieter power issue', 'seemed to make the woman running it', "I couldn't tell whether", 'much bigger', 'at the time, and almost institutional', 'friendly and interesting,', "highly structured political system that didn't seem intuitive for hippies", 'Looking back, almost none of these communities', 'suffering with them', 'needed to talk about', 'Some people, including me,']
MUSTNOT = ['grew up on shoulders', 'boring as hell', 'very happy', 'enough to be diverse', 'big communal shower', 'was big,', 'enough and interesting enough', 'labor credit', 'struck me as odd', 'wanted to talk about', "didn't feel like it was really", 'hard to join', 'referenced in my title', 'recreating all the']
out = {}
for k4 in P4:
    for k5 in P5:
        pp = list(paras); pp[i4] = P4[k4]; pp[i5] = P5[k5]; md = '\n\n'.join(pp)
        miss = [m for m in MUST if m not in md]; bad = [m for m in MUSTNOT if m in md]
        assert not miss and not bad, (k4, k5, miss, bad)
        open(f'v3/section-P4{k4}-P5{k5}.md', 'w', encoding='utf-8').write(md)
        open(f'v3/section-P4{k4}-P5{k5}.txt', 'w', encoding='utf-8').write(mdplain.plain(md).strip() + '\n')
def alone(name, md):
    t = mdplain.plain(md).strip(); open(f'v3/{name}.txt', 'w', encoding='utf-8').write(t + '\n'); out[name] = len(t.split())
alone('P1', paras[i1])
for k in P4: alone('P4' + k, P4[k])
for k in P5: alone('P5' + k, P5[k])
for n, i in (('P10', i10), ('P11', i11), ('P12', i12), ('P13', i13), ('P15', i15)): alone(n, paras[i])
alone('P14-P15', paras[i14] + '\n\n' + paras[i15])
json.dump(log, open('v3/fixlog-v3.json', 'w'), indent=1, ensure_ascii=False)
json.dump(dict(must=MUST, must_not=MUSTNOT, source='Joel, 2026-09-30 18:58 UTC'), open('v3/owner-edits-v3.json', 'w'), indent=1, ensure_ascii=False)
print('words alone:', out); print(len(log), 'fixes; owner-edit checks pass on all 8 combinations')
for f in ('P4D','P4C','P4B','P4A','P5A','P13','P14-P15'):
    r = subprocess.run(['python3','/home/claude/ho/articles/inner-child-therapy/tools/tells_lint.py',f'v3/{f}.txt'],capture_output=True,text=True).stdout
    print(f, re.search(r'verdict: (\w+)', r).group(1), '|', '; '.join(l.strip() for l in r.splitlines() if 'HARD' in l)[:120])
