import json, hashlib
EXP='/home/claude/lessons/articles/inner-child-therapy/experiments/emulate-20260929'
src=open(f'{EXP}/runs/articles/intentional-communities/paste/intentional-communities-baseline-01.txt',encoding='utf-8').read().strip().split('\n\n')
def rd(p): return open(p,encoding='utf-8').read().strip()
fixlog=[]
def fix(run, text, old, new, why):
    assert text.count(old)==1, (run, old)
    fixlog.append(dict(run=run, before=old, after=new, why=why))
    return text.replace(old,new)
# P1: Emulate API version 1 of the paragraph alone (heading kept from the source)
p1=rd('ic01-p1-api1.txt')
p1=fix('ic01-p1-api1', p1, "up on the Internet: Where's Utopia?", "up on the Internet for the first time: Where's Utopia?", 'puts back "for the first time"')
p1=fix('ic01-p1-api1', p1, "How do we live together without lots of loneliness, domination, and stupidity?", "How do we live together without recreating all the loneliness, domination, and stupidity we were supposedly escaping?", 'puts back the source\'s point that the escape reproduced the problems')
# P5: 0102 A
p5=rd(f'{EXP}/runs/emulate/intentional-communities-rewrite-0102-A.txt')
p5=fix('0102-A', p5, 'visiting every community I could at the time', 'visiting every community we could at the time', 'he was carried along, so "we" not "I"')
p5=fix('0102-A', p5, "because I was just a visitor’s kid, not part of any tribe,", "because I was just a visitor’s kid, close enough to see how people lived but not part of any tribe,", 'puts back "close enough to see how people lived"')
# P10-15: 0103 B, with A's second paragraph spliced in
A=rd(f'{EXP}/runs/emulate/intentional-communities-rewrite-0103-A.txt').split('\n\n')
B=rd(f'{EXP}/runs/emulate/intentional-communities-rewrite-0103-B.txt').split('\n\n')
assert len(A)==6 and len(B)==6
b1=B[0]
b1=fix('0103-B', b1, 'when I was there--enough to be diverse, small enough to actually be friends with everyone.', 'when I was there, enough to be diverse, small enough to actually make friends.', '"friends with everyone" overstated the source; dashes typed as "--"')
b1=fix('0103-B', b1, 'I was very happy there, mostly.', 'I was very happy there.', '"mostly" was invented')
b3=fix('0103-B', B[2], 'it would have been more like asking to be invited into their group chat.', 'it would have been more like asking whether their group chat had an opening.', "puts back Joel's line")
b5=fix('0103-B', B[4], 'One thing that struck me as odd--about all of them, basically, was', 'One thing that struck me as odd about all of them, basically, was', 'typed "--" broke the sentence')
p10_15=[b1, A[1], b3, B[3], b5, B[5]]
fixlog.append(dict(run='0103-A', before='(B paragraph 2)', after=A[1][:60]+'…', why='splice: A\'s second paragraph replaces B\'s, which invented "mostly around electricity" and that the woman "started" the factory'))
paras=[src[0], p1, src[2], src[3], src[4], p5, src[6], src[7], src[8], src[9]] + p10_15 + [src[16], src[17]]
plain='\n\n'.join(paras)
open('ic01-section-v1.txt','w',encoding='utf-8').write(plain+'\n')
json.dump(fixlog, open('ic01-fixlog.json','w'), indent=1, ensure_ascii=False)
print(len(plain.split()),'words;',len(paras),'paragraphs;',len(fixlog),'log entries')
print(hashlib.sha256((plain+'\n').encode()).hexdigest()[:12])
