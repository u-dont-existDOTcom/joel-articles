"""Apply the frozen source-supported route; preserve the complete restored block set."""
from pathlib import Path
from collections import Counter
from bs4 import BeautifulSoup
import sys,re,json,hashlib,html
from restore_innerchild import split as blocks
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
def build(root):
 r=Path(root);task=r/'state/tasks/community-innerchild-20261020';out=r/'articles/inner-child-therapy/candidate/editorial-20261020'
 hs=(task/'inputs/Inner-Child-Humanized-Owner-20261019.html').read_text();ds=(task/'inputs/Inner-Child-AI-Formatting-Source-20261019.html').read_text();rs=(out/'Inner-Child-restored-r01.html').read_text()
 assert sha(hs)=='d246b51a181cbc480a857c9406469467000675cbe31426950c66b24809c2e178';assert sha(ds)=='68f710a170fb33e29ed1d3e76fbe9ed95aa79a3c523ac497784e1b41ec8c6853';assert sha(rs)=='95a968ab65379887c34a86c946fedc4ba35757cce49260f6049717050ffc08f9'
 pre,H,post=blocks(hs);_,D,_=blocks(ds);_,R,_=blocks(rs);label=re.compile(r'(<p\b[^>]*>\s*)<strong>P\d+</strong>\s*');text=lambda x:BeautifulSoup(x,'html.parser').get_text(' ',strip=True)
 after={1:[2,3,4,5,6],7:[11],45:[53],123:[122],185:[151],227:[231],267:[374]};ids=[]
 for i,b in enumerate(H):
  c,n=label.subn(r'\1',b)
  if (re.match(r'<h[1-6]\b',c) or n) and not text(c):continue
  ids.append(f'H{i:03d}');ids += [f'D{d:03d}' for d in after.get(i,[])]
 assert len(ids)==len(R);U=dict(zip(ids,R));assert pre+''.join(U[k] for k in ids)+post==rs
 sequence=[]
 def use(a,b=None):
  for i in range(a,(b if b is not None else a)+1):
   ident=f'H{i:03d}'
   if ident in U:sequence.append(ident);sequence.extend(f'D{d:03d}' for d in after.get(i,[]))
 use(0,48);use(87,98);use(99,110);use(317,322);use(111,119);use(135,170);use(80,84);use(86);use(316);use(49,54);use(323,354);use(171,207);use(85);use(208,211);use(271,315);use(355,361);use(371,372);use(362,369);use(120,134);use(384,387);use(64,72);use(55,63);use(73,79);use(388,397);use(373,383);use(212,248);use(249,256);use(257);use(259,260);use(258);use(261,270);use(401,406);use(398,400);use(407,423)
 assert Counter(sequence)==Counter(ids),'Content omission/duplication';changes=[];V=U.copy()
 levels={'H032':2,'H120':2,'H123':3,'H132':2,'H371':2,'H388':2,'H055':2,'H069':3,'H212':1,'H219':2,'H249':1,'H254':2,'H241':3}
 for ident,level in levels.items():
  old=V[ident];new=re.sub(r'<(/?)h[1-6](\b)',rf'<\1h{level}\2',old)
  if old!=new:V[ident]=new;changes.append({'id':'L'+ident,'source_id':ident,'classification':'Heading hierarchy','before_html':old,'after_html':new,'reason':'Represent the actual parent/child relationship after moving the source section.'})
 copy=[('H143','ask yourself again,','ask yourself,','The named question now receives its general discussion later; do not imply it was already asked.'),('H387','but when romance should follow when','but romance should follow when','Remove the duplicated when in an otherwise unchanged sentence.'),('H215','it is a already a part','it is already a part','Remove the duplicated article.'),('H404','I’ll talk more about those next,','I’ll talk more about those in the appendix,','The clinical comparison is in the appendix after the closing encouragement.')]
 for ident,a,b,why in copy:
  old=V[ident];assert old.count(a)==1,(ident,a);new=old.replace(a,b,1);V[ident]=new;changes.append({'id':'W'+ident,'source_id':ident,'classification':'Copy/reference repair','before_html':old,'after_html':new,'reason':why})
 add_id='N001';V[add_id]='<h2>Hearthwork: Taking Turns</h2>';sequence.insert(sequence.index('H393'),add_id);changes.append({'id':'WN001','source_id':None,'classification':'New navigational heading','before_html':'','after_html':V[add_id],'reason':'Names the peer-counseling method already defined in the following source paragraph; adds no therapeutic claim.'})
 candidate=pre+''.join(V[k] for k in sequence)+post
 for k in U:
  if not any(c['source_id']==k for c in changes):assert V[k]==U[k]
 links=lambda s:Counter(html.unescape(x.get('href','')) for x in BeautifulSoup(s,'html.parser').find_all('a'))
 assert links(candidate)==links(rs)
 assert sha(candidate)=='2ad13ba6c4aea28fd4cb23f46443ca16fbfa52c79f7a26c30ce5805b3a3dd45a','Cross-runtime identity mismatch'
 (out/'Inner-Child-r02-candidate.html').write_text(candidate);(out/'LOCAL-CHANGES.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
 inventory=[{'id':k,'old_index':i,'new_index':sequence.index(k),'source_html_sha256':sha(U[k]),'candidate_html_sha256':sha(V[k]),'original_html':U[k],'candidate_html':V[k]} for i,k in enumerate(ids)];inventory.append({'id':add_id,'old_index':None,'new_index':sequence.index(add_id),'source_html_sha256':None,'candidate_html_sha256':sha(V[add_id]),'original_html':None,'candidate_html':V[add_id]})
 (out/'ASSEMBLY.json').write_text(json.dumps({'source_sha256':sha(rs),'candidate_sha256':sha(candidate),'original_order':ids,'candidate_order':sequence,'blocks':inventory},ensure_ascii=False,indent=2)+'\n')
 headings=[];stack=[]
 for k in sequence:
  b=BeautifulSoup(V[k],'html.parser').find()
  if b and re.fullmatch(r'h[1-6]',b.name):
   lev=int(b.name[1])
   while stack and stack[-1]['level']>=lev:stack.pop()
   obj={'id':k,'level':lev,'text':b.get_text(' ',strip=True),'parent':stack[-1]['id'] if stack else None};headings.append(obj);stack.append(obj)
 (out/'HEADINGS.json').write_text(json.dumps(headings,ensure_ascii=False,indent=2)+'\n');reads=[]
 for k in sequence:
  b=V[k];soup=BeautifulSoup(b,'html.parser');tag=soup.find()
  reads.append(f'[{k} NATIVE OBJECT: {tag.get("class",[])}]' if tag and tag.name=='div' else f'[{k}] {text(b)}')
 (out/'READING-COPY.txt').write_text('\n\n'.join(reads)+'\n')
 receipt={'status':'DEVELOPMENTAL_CANDIDATE_NOT_OWNER_APPROVED','source_sha256':sha(rs),'candidate_sha256':sha(candidate),'source_content_blocks':len(ids),'candidate_content_blocks':len(sequence),'source_blocks_omitted':0,'source_blocks_duplicated':0,'new_headings':1,'local_changes':len(changes),'link_occurrences':'exact equality to restored r01','prose_policy':'Whole source passages moved; four bounded copy/reference fixes. No independent source claim deleted or added. The parent hierarchy is changed as logged.','word_reduction_is_not_completion_metric':True,'remaining':'Fresh full-reader review and exact delivery checks; owner judgment about scope of long special-topic chapters.','detector':'No new score; original upload owner-reported 100% Human.'}
 (out/'ASSEMBLY-RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':build(sys.argv[1])
