from pathlib import Path
from bs4 import BeautifulSoup
import json,re,hashlib,sys,html
from collections import Counter
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
def refine(o):
 o=Path(o);data=json.loads((o/'ASSEMBLY.json').read_text());old=(o/'Inner-Child-r02-candidate.html').read_text();assert sha(old)=='2ad13ba6c4aea28fd4cb23f46443ca16fbfa52c79f7a26c30ce5805b3a3dd45a'
 order=data['candidate_order'][:];U={b['id']:b['candidate_html'] for b in data['blocks']};V=U.copy();ops=[]
 def move(ids,before=None,after=None,why=''):
  positions=[order.index(k) for k in ids];order[:]=[k for k in order if k not in ids];j=order.index(before) if before else order.index(after)+1;order[j:j]=ids;ops.append({'kind':'move','ids':ids,'before':before,'after':after,'reason':why,'old_positions':positions})
 move(['H356','H357'],before='H106',why='Bring absent warmth and threatening/lonely imagery into the existing basic-care teaching before the floor and borrowed-warmth response.')
 move(['H358'],after='H201',why='Place emotional-permission guard explanation beside the protective-part method; retain external-trust distinction.')
 move(['H359','H360','H361'],after='H322',why='Offer motivation-based entry beside the other borrowing alternatives.')
 move(['H309','H310','H311','H312'],before='H037',why='Gather specific authority/manipulation mechanisms before the existing Borrow adulthood. Do not surrender it closer.')
 group=[f'H{i:03d}' for i in range(364,370)]+[f'H{i:03d}' for i in range(120,135)]+['H362','H363','H371','H372'];move(group,after='H315',why='One deeper-love chapter develops happiness, gratitude, spiritual betrayal, bodily opening and shallow-versus-unavailable contact.')
 order.remove('H355');ops.append({'kind':'heading_retired','id':'H355','reason':'Missing warmth is merged into its core home; remaining depth material uses its existing question as parent.'})
 replacements=[('H356',' That doesn’t close the door, though, it just means you start smaller.','','Duplicate announcement of the smaller step immediately taught in H357/H106.'),('H106','If the love still isn’t coming, you can at least','You can at least','Repeated no-love condition is established immediately before.'),('H358',' (see the section Hear the Protective Part First)','','Remove same-section pointer after relocation.'),('H372','Some people have the opposite problem. ','','Former opposing branch is no longer adjacent; surviving opener directly states the problem.'),('H298','The Inner Guide Comes Later','The Inner Guide','Remove categorical timing implication from heading; preserve Timing Is Individual and direct new-interest example.')]
 for k,a,b,why in replacements:
  assert V[k].count(a)==1,(k,a);prev=V[k];V[k]=V[k].replace(a,b,1);ops.append({'kind':'wording','id':k,'before_html':prev,'after_html':V[k],'reason':why})
 prev=V['H364'];V['H364']=re.sub(r'<(/?)h2\b',r'<\1h1',prev);ops.append({'kind':'heading_level','id':'H364','before_html':prev,'after_html':V['H364'],'reason':'Existing depth question becomes the parent.'})
 first=old.index(U[data['candidate_order'][0]]);last=old.rfind(U[data['candidate_order'][-1]])+len(U[data['candidate_order'][-1]]);candidate=old[:first]+''.join(V[k] for k in order)+old[last:]
 assert Counter(order)==Counter(k for k in data['candidate_order'] if k!='H355')
 links=lambda s:Counter(html.unescape(a.get('href','')) for a in BeautifulSoup(s,'html.parser').find_all('a'));assert links(candidate)==links(old);assert len(BeautifulSoup(V['H015'],'html.parser').select('ol > li'))==5
 changed={x['id'] for x in ops if x['kind'] in ['wording','heading_level']}
 for k in order:
  if k not in changed:assert V[k]==U[k]
 assert sha(candidate)=='91b9065b9a121a40fb54cad2eac1d8be99eb5a24869178c04c26786a163708a4'
 (o/'Inner-Child-r03-candidate.html').write_text(candidate);(o/'REFINEMENT-OPS.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');inv=[]
 for b in data['blocks']:
  x=dict(b);k=x['id'];x['r02_index']=x['new_index'];x['new_index']=order.index(k) if k in order else None;x['candidate_html']=V[k] if k in order else None;x['candidate_html_sha256']=sha(V[k]) if k in order else None;inv.append(x)
 final={**data,'candidate_sha256':sha(candidate),'candidate_order':order,'blocks':inv};(o/'FINAL-ASSEMBLY.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
 def read_block(raw):
  el=BeautifulSoup(raw,'html.parser').find()
  if not el:return ''
  if el.name in ['ol','ul']:return '\n'.join((f'{i}. ' if el.name=='ol' else '- ')+li.get_text(' ',strip=True) for i,li in enumerate(el.find_all('li',recursive=False),1))
  if el.name=='div':
   alts=list(dict.fromkeys(x.get('alt','') for x in el.find_all('img') if x.get('alt')));return '[NATIVE OBJECT '+str(el.get('class',[]))+('; source alt text: '+' | '.join(alts) if alts else '')+']'
  prefix='#'*int(el.name[1])+' ' if re.fullmatch(r'h[1-6]',el.name) else ('> ' if el.name=='blockquote' else '');return prefix+el.get_text(' ',strip=True)
 (o/'FINAL-READING-COPY.txt').write_text('\n\n'.join('['+k+'] '+read_block(V[k]) for k in order)+'\n')
 headings=[{'id':k,'level':int(BeautifulSoup(V[k],'html.parser').find().name[1]),'text':BeautifulSoup(V[k],'html.parser').get_text(' ',strip=True)} for k in order if re.match(r'<h[1-6]\b',V[k])];(o/'FINAL-HEADINGS.json').write_text(json.dumps(headings,ensure_ascii=False,indent=2)+'\n')
 receipt={'status':'CANDIDATE_FOR_OWNER_REVIEW','source_r01_sha256':data['source_sha256'],'candidate_sha256':sha(candidate),'r02_sha256':sha(old),'source_paragraphs_deleted':0,'source_heading_retired':['H355'],'scaffolding_trims':['H356 last sentence','H106 redundant condition','H358 self-reference','H372 unanchored opposite-problem opener'],'independent_claims_deleted':0,'links_unchanged_from_restored_baseline':True,'five_stage_list_items':5,'new_prose_from_donor':'Only recorded adjacent media introductions, no AI explanatory material','detector':'No new measurement','review_scope':'Fresh whole r02 read plus local reconciliation; final r03 delta review pending.'};(o/'FINAL-ASSEMBLY-RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':refine(sys.argv[1])
