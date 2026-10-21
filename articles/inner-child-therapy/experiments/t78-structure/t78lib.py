import json,re,html,difflib,unicodedata
ART='/root/work/joel-articles/articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'
G='/root/work/joel-articles/articles/inner-child-therapy/experiments/t78-structure/gpt-r03/'
def norm(t):
    t=html.unescape(t)
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    t=re.sub(r'<[^>]+>',' ',t)
    t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t)      # md links
    t=re.sub(r'!\[[^\]]*\]\([^)]*\)',' ',t)
    t=re.sub(r'^#+\s*','',t)
    t=t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace(' ',' ')
    t=re.sub(r'[*_`>]','',t)
    t=re.sub(r'\s+',' ',t).strip().lower()
    return t
def parse(path=ART):
    s=open(path,encoding='utf-8').read()
    # split into raw chunks separated by blank lines, but keep multi-line html comments and html blocks together
    chunks=[];cur=[];incom=False
    for line in s.split('\n'):
        if not incom and line.strip()=='' :
            if cur: chunks.append('\n'.join(cur)); cur=[]
            continue
        cur.append(line)
        if '<!--' in line and '-->' not in line.split('<!--')[-1]: incom=True
        if incom and '-->' in line: incom = line.rfind('<!--')>line.rfind('-->')
    if cur: chunks.append('\n'.join(cur))
    out=[]
    for c in chunks:
        st=c.lstrip()
        if st.startswith('<!--') and st.rstrip().endswith('-->') and st.count('<!--')==1: kind='comment'; lvl=0
        elif re.match(r'^#{1,6} ',st): kind='heading'; lvl=len(st.split(' ')[0])
        else: kind='block'; lvl=0
        out.append({'kind':kind,'level':lvl,'raw':c,'n':norm(c)})
    return s,out
def gpt():
    fa=json.load(open(G+'FINAL-ASSEMBLY.json',encoding='utf-8'))
    B={b['id']:b for b in fa['blocks']}
    return fa,B
