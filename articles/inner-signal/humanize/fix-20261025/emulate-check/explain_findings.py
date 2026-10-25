"""Mark each reader finding that his own words account for, and gather them all into READS-ALL.json.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/explain_findings.py DIR ARTICLE "TEXT1,TEXT2,..." none

DIR holds the readers' READ-<part>.json; ARTICLE is the article they read; the texts are his own words beyond the
check's sources (his messages, the new sentences he approved, his inner child guide and texts). A finding is his when its
new words are in one of them, or when half its paragraph's sentences are (a paragraph he rewrote himself). "show" as the
last argument prints the rest that matter, and every slip.
"""
import json,sys,glob,re,difflib
sys.path.insert(0,'tools/humanization')
import emulate_artifacts as ea
D=sys.argv[1]; art=sys.argv[2]; extra=sys.argv[3].split(',') if len(sys.argv)>3 and sys.argv[3] else []
mode=sys.argv[4] if len(sys.argv)>4 else 'show'
blocks={b['i']:b for b in ea.load(art)}
pairs={p['block']:p for p in json.load(open(D+'/PAIRS.json'))}
joel=ea.Corpus(extra) if extra else None
out=[]
for f in sorted(glob.glob(D+'/READ-*.json')):
    part=re.findall(r'READ-(\w+)\.json',f)[0]
    for k,x in enumerate(json.load(open(f))):
        b=blocks.get(x.get('block'))
        x['id']='%s.%d'%(part,k)
        x['new_found']=(not x.get('new')) or (b is not None and ea.norm(x['new']) in ea.norm(b['text']))
        expl=None
        if joel and x.get('new') and joel.has(x['new']):
            expl='his own words (his messages)'
        if joel and b is not None and expl is None:
            sents=[b['text'][a:z] for a,z in ea.sentences(b['text'])]
            his=sum(1 for s in sents if (joel.best(s) or [(0,None)])[0][0]>=0.8)
            if sents and his/len(sents)>=0.5: expl='paragraph he rewrote himself (%d of %d sentences in his messages)'%(his,len(sents))
        x['explained']=expl
        out.append(x)
json.dump(out,open(D+'/READS-ALL.json','w'),ensure_ascii=False,indent=1)
import collections
print('all',len(out),'| explained by his messages',sum(1 for x in out if x['explained']),'| quote not found',sum(1 for x in out if not x['new_found']))
print(collections.Counter((x['kind'],x['severity']) for x in out if not x['explained']))
if mode=='show':
    for x in out:
        if x['explained'] or not (x['severity']=='matters' or x['kind']=='error'): continue
        print('#%s [%s %s] %s (block %s)%s' % (x['id'],x['kind'],x['severity'],x.get('where','')[:60],x.get('block'),'' if x['new_found'] else ' NEW?'))
        if x.get('new'): print('   NEW:',x['new'][:260])
        if x.get('his'): print('   HIS:',x['his'][:260])
        print('   WHY:',x.get('why','')[:240])
