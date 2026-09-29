#!/usr/bin/env python3
"""Numbers for CLAUDE-SLOP-COMPARISON.md. Run from the experiment folder:
   python3 analysis/slop_numbers.py
Reads runs/emulate/, inputs/learning/ and ../../tools/ (tells_lint.py, calibration/)."""
import subprocess, re, glob, os, ast, collections, difflib, statistics as st, importlib.util
EXP=os.getcwd(); TOOLS=os.path.normpath(EXP+'/../../tools'); LINT=TOOLS+'/tells_lint.py'
spec=importlib.util.spec_from_file_location('tl',LINT); tl=importlib.util.module_from_spec(spec); spec.loader.exec_module(tl)
A=EXP+'/inputs/learning/A_joelfixes/'; B=EXP+'/inputs/learning/B_protector/'; E=EXP+'/runs/emulate/'
def lint(path, owner=None):
    out=subprocess.run(['python3',LINT,path]+(['--owner',owner] if owner else []),capture_output=True,text=True).stdout
    met=ast.literal_eval(re.search(r'^metrics: (.*)$',out,re.M).group(1))
    rules=collections.Counter({r:int(n) for r,n in re.findall(r'^-- (.+) \((\d+)\)$',out,re.M)})
    return met, rules
groups={
 'Claude drafts (A)':[(p,None) for p in sorted(glob.glob(A+'A*_before.txt'))],
 'Emulate (A)':[(p,None) for p in sorted(glob.glob(E+'gpt_A??_api_r1.txt'))],
 'Emulate (all)':[(p,None) for p in sorted(glob.glob(E+'*.txt')) if not p.endswith('.lint.txt') and 'DOM_DIAGNOSTIC' not in p],
 'Joel fixes':[(p,None) for p in sorted(glob.glob(A+'A*_joel_after_REFERENCE_ONLY.txt'))],
 'Claude passing':[(p, p[:-4]+'.owner.txt' if os.path.exists(p[:-4]+'.owner.txt') else None) for p in sorted(glob.glob(TOOLS+'/calibration/PASS_*.txt')) if 'joel' not in os.path.basename(p).lower() and not p.endswith('.owner.txt')]}
RULES=['B11 tic','B2 contrast','B1 finished principle','B5 announces the paragraph','E41 coach phrase','B4/E15 list or packed sentence','B3 short knock-down','B7 short landing at paragraph end','E23 paragraph of instructions']
res={g:[lint(p,o) for p,o in fs] for g,fs in groups.items()}
print('linter hits per 100 of the writer\'s words')
print('rule | '+' | '.join(f'{g} ({len(res[g])})' for g in groups))
for r in RULES+['ALL']:
    row=[]
    for g in groups:
        mw=sum(m['my_words'] for m,_ in res[g])
        n=sum((sum(c[k] for k in RULES) if r=='ALL' else c[r]) for _,c in res[g])
        row.append(f'{100*n/mw:.2f}')
    print(r,'|',' | '.join(row))
# copying and length, set A, whole-rewrite pairs only
def norm(t): return t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','-')
def sents(t): return [s for p in tl.paragraphs(tl.clean(norm(t))) for s in tl.sentences(p)]
def W(t): return re.findall(r"[a-z']+", norm(t).lower())
def kept(b,a): return sum(1 for x in sents(b) if max((difflib.SequenceMatcher(None,x.lower(),y.lower()).ratio() for y in sents(a)),default=0)>=0.85)
def copied(b,a):
    bs={tuple(W(b)[i:i+4]) for i in range(len(W(b))-3)}; aw=W(a); cov=[0]*len(aw)
    for i in range(len(aw)-3):
        if tuple(aw[i:i+4]) in bs: cov[i:i+4]=[1]*4
    return sum(cov)/max(len(aw),1)
ids=[i for i in (os.path.basename(p)[:3] for p in sorted(glob.glob(A+'A*_before.txt'))) if os.path.exists(E+f'gpt_{i}_api_r1.txt') and i not in ('A19','A21')]
rd=lambda p: open(p,encoding='utf-8').read()
tot=dict(sent=0,ek=0,jk=0); ec=[];jc=[];el=[];jl=[]
for i in ids:
    b,e,j=rd(A+f'{i}_before.txt'),rd(E+f'gpt_{i}_api_r1.txt'),rd(A+f'{i}_joel_after_REFERENCE_ONLY.txt')
    tot['sent']+=len(sents(b)); tot['ek']+=kept(b,e); tot['jk']+=kept(b,j)
    ec.append(copied(b,e)); jc.append(copied(b,j)); el.append(len(W(e))/len(W(b))); jl.append(len(W(j))/len(W(b)))
print(f"\nset A, {len(ids)} pairs (A19, A21 left out: their 'after' is one added sentence)")
print(f"draft sentences kept (>=85% same): Emulate {tot['ek']}/{tot['sent']}, Joel {tot['jk']}/{tot['sent']}")
print(f"words inside 4-word runs copied from draft: Emulate {st.mean(ec):.0%}, Joel {st.mean(jc):.0%}; pairs >=50%: Emulate {sum(c>=.5 for c in ec)}, Joel {sum(c>=.5 for c in jc)}")
print(f"median length vs draft: Emulate {st.median(el):.0%}, Joel {st.median(jl):.0%}")
# surface markers
pats={'we/us/our':r"\b(we|us|our|we're|we’re)\b",'exclamation':r"!",'parentheses':r"\(",'etc':r"\betc\b",'I/me/my':r"\b(I|me|my|I'm|I’m|I've|I’ve|I'd)\b",'questions':r"\?"}
def rate(t,p): return 100*len(re.findall(p,t,0 if p.startswith(r"\b(I|") else re.I))/len(re.findall(r"[A-Za-z']+",t))
allA=[i for i in (os.path.basename(p)[:3] for p in sorted(glob.glob(A+'A*_before.txt'))) if os.path.exists(E+f'gpt_{i}_api_r1.txt')]
print(f'\nmarkers per 100 words, set A ({len(allA)} trios): draft / Emulate / Joel')
for k,p in pats.items():
    print(k, *(f"{rate(' '.join(rd(f) for f in fs),p):.2f}" for fs in ([A+f'{i}_before.txt' for i in allA],[E+f'gpt_{i}_api_r1.txt' for i in allA],[A+f'{i}_joel_after_REFERENCE_ONLY.txt' for i in allA])))
bi=[p for p in sorted(glob.glob(B+'B*.txt')) if os.path.exists(E+f'gpt_{os.path.basename(p)[:3]}_api_r1.txt')]
print(f'set B ({len(bi)} pairs): draft / Emulate')
for k,p in pats.items():
    print(k, f"{rate(' '.join(rd(f) for f in bi),p):.2f}", f"{rate(' '.join(rd(E+'gpt_'+os.path.basename(f)[:3]+'_api_r1.txt') for f in bi),p):.2f}")
