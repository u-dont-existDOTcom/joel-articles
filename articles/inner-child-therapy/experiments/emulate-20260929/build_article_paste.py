# Builds paste-ready Pangram texts for the article baselines. Written by Claude, 2026-09-29.
import re,json,hashlib,os,sys
EXP=sys.argv[1]  # .../experiments/emulate-20260929
CARD=re.compile(r'^\[[^\]]+\]\(https://[a-z0-9-]+\.substack\.com/p/[^)]*\)\[\s*$.*?^\[Read full story\]\([^)]*\)\s*$', re.M|re.S)
def plain(md):
    md=CARD.sub('', md)
    md=re.sub(r'^\[(Share|Subscribe now|Leave a comment)\]\(%%[^)]*\)\s*$', '', md, flags=re.M)
    md=re.sub(r'^\[image \d+\]\s*$', '', md, flags=re.M)
    md=re.sub(r'^\[.*\]\(https://[^)]*\)Copy link\s*$', '', md, flags=re.M)
    out=[]
    for block in re.split(r'\n\s*\n', md.strip()):
        b=block.strip()
        if re.fullmatch(r'\[image \d+\]\([^)]*\)', b): continue
        b=re.sub(r'\[image \d+\]\([^)]*\)\s*', '', b)
        b=re.sub(r'!\[([^\]]*)\]\([^)]*\)', '', b)
        b=re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', b)
        b=re.sub(r'^#{1,6}\s+', '', b, flags=re.M)
        b=re.sub(r'(\*\*\*|\*\*|\*|__)(?=\S)(.+?)(?<=\S)\1', r'\2', b)
        b=re.sub(r'^>\s?', '', b, flags=re.M)
        b=b.replace('\\*','*').replace('\\_','_').replace('\\#','#').replace('\\[','[').replace('\\]',']')
        b=b.replace('*','')
        b=re.sub(r'^\+\d+\s*$', '', b, flags=re.M)
        b=re.sub(r'^\[caption\].*$', '', b, flags=re.M).strip()
        if b: out.append(b)
    return '\n\n'.join(out)+'\n'
def rd(p): return open(p,encoding='utf-8').read()
queue=[]
def emit(slug,n,text,sections,src):
    cid=f'{slug}-baseline-{n:02d}'
    rel=f'runs/articles/{slug}/paste/{cid}.txt'
    os.makedirs(os.path.dirname(f'{EXP}/{rel}'),exist_ok=True)
    open(f'{EXP}/{rel}','w',encoding='utf-8').write(text+'\n')
    ws=text.split()
    queue.append(dict(check_id=cid,article=slug,variant='baseline',paste_file=rel,words=len(ws),sha256=hashlib.sha256((text+'\n').encode()).hexdigest(),sections=sections,source_files=src,first_words=' '.join(ws[:8]),last_words=' '.join(ws[-8:])))
for slug in ['intentional-communities','hypnosis-guide']:
    units=[]
    for s in json.load(open(f'{EXP}/runs/articles/{slug}/section-map.json')):
        t=plain(rd(f"{EXP}/{s['text_file']}")).strip()
        if t: units.append(dict(ids=[s['section_id']],src=[s['text_file']],text=t,words=len(t.split())))
    merged=[];carry=None
    for u in units:
        if carry: u=dict(ids=carry['ids']+u['ids'],src=carry['src']+u['src'],text=carry['text']+'\n\n'+u['text'],words=carry['words']+u['words']);carry=None
        if u['words']<150: carry=u;continue
        merged.append(u)
    if carry:
        m=merged[-1];merged[-1]=dict(ids=m['ids']+carry['ids'],src=m['src']+carry['src'],text=m['text']+'\n\n'+carry['text'],words=m['words']+carry['words'])
    for n,u in enumerate(merged,1): emit(slug,n,u['text'],u['ids'],u['src'])
S='runs/articles/neuro-de-armoring/sections/'
t=rd(f'{EXP}/{S}003-original.md')
cuts=[m.start() for m in re.finditer(r'^## (Part 2|Part 3)',t,re.M)]
parts=[t[:cuts[0]],t[cuts[0]:cuts[1]],t[cuts[1]:]]
emit('neuro-de-armoring',1,plain(rd(f'{EXP}/{S}002-original.md')).strip()+'\n\n'+plain(parts[0]).strip(),['neuro-de-armoring-h1-002','neuro-de-armoring-h1-003 (opening to end of Part 1)'],[S+'002-original.md',S+'003-original.md'])
emit('neuro-de-armoring',2,plain(parts[1]).strip(),['neuro-de-armoring-h1-003 (Part 2)'],[S+'003-original.md'])
emit('neuro-de-armoring',3,plain(parts[2]).strip(),['neuro-de-armoring-h1-003 (Parts 3-5 and Aftermath)'],[S+'003-original.md'])
json.dump(queue,open(f'{EXP}/runs/article-baseline-queue.json','w',encoding='utf-8'),indent=1,ensure_ascii=False)
print(len(queue),'checks',sum(q['words'] for q in queue),'words')
print('digest',hashlib.sha256(''.join(q['sha256'] for q in queue).encode()).hexdigest()[:16])
