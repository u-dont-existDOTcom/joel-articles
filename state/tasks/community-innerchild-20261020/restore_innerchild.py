from pathlib import Path
from html.parser import HTMLParser
import re,json,hashlib,sys
from bs4 import BeautifulSoup
VOID=set('area base br col embed hr img input link meta param source track wbr'.split())
class Parser(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=False);self.s=s;self.lines=[0]+[m.end() for m in re.finditer('\n',s)];self.stack=[];self.spans=[];self.child=None;self.feed(s)
 def pos(self):
  a,b=self.getpos();return self.lines[a-1]+b
 def handle_starttag(self,t,a):
  i=self.pos();e=i+len(self.get_starttag_text())
  if not self.stack:self.begin=e
  elif len(self.stack)==1:self.child=i
  if t not in VOID:self.stack.append(t)
  elif len(self.stack)==1:self.spans.append((i,e));self.child=None
 def handle_endtag(self,t):
  if t in VOID:return
  assert t in self.stack
  k=len(self.stack)-1-self.stack[::-1].index(t);e=self.s.find('>',self.pos())+1
  if k==1:self.spans.append((self.child,e));self.child=None
  if k==0:self.end=self.pos()
  self.stack=self.stack[:k]
def split(s):
 p=Parser(s);assert not p.stack
 return s[:p.begin],[s[a:b] for a,b in p.spans],s[p.end:]
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
def main(root):
 r=Path(root);t=r/'state/tasks/community-innerchild-20261020';o=r/'articles/inner-child-therapy/candidate/editorial-20261020';o.mkdir(parents=True,exist_ok=True)
 hs=(t/'inputs/Inner-Child-Humanized-Owner-20261019.html').read_text();ds=(t/'inputs/Inner-Child-AI-Formatting-Source-20261019.html').read_text()
 assert sha(hs)=='d246b51a181cbc480a857c9406469467000675cbe31426950c66b24809c2e178';assert sha(ds)=='68f710a170fb33e29ed1d3e76fbe9ed95aa79a3c523ac497784e1b41ec8c6853'
 pre,H,post=split(hs);_,D,_=split(ds);assert len(H)==424 and len(D)==459
 label=re.compile(r'(<p\b[^>]*>\s*)<strong>P\d+</strong>\s*');clean=[];removed=0;empty=[]
 for i,b in enumerate(H):
  c,n=label.subn(r'\1',b);removed+=n
  if (re.match(r'<h[1-6]\b',c) or n) and not BeautifulSoup(c,'html.parser').get_text(' ',strip=True):empty.append(i);continue
  clean.append((i,c))
 baseline=pre+''.join(b for i,b in clean)+post;(o/'Inner-Child-labels-removed.html').write_text(baseline)
 after={1:[2,3,4,5,6],7:[11],45:[53],123:[122],185:[151],227:[231],267:[374]}
 reasons={1:'Restore source Listen & Watch/audio/song introductions and media before If that got to you.',7:'Donor video follows the same first Chicken-and-Egg paragraph.',45:'Somatic-map card supplies the stated map and following reference.',123:'Gratitude video under the same named heading.',185:'Child gift video card beside existing article link.',227:'Mantra embed follows its existing introduction.',267:'Human-birth illustration follows turtle explanation.'}
 seq=[];placements=[]
 for i,b in clean:
  seq.append(b)
  for d in after.get(i,[]):
   seq.append(D[d]);placements.append({'donor_id':f'D{d:03d}','after_human_id':f'H{i:03d}','source_sha256':sha(D[d]),'reason':reasons[i],'kind':'adjacent source introduction' if d in [2,3,5] else 'native object'})
 s=pre+''.join(seq)+post;links=[(127,'near death experience','http://iands.org'),(152,'dramatized scene','https://www.springfieldspringfield.co.uk/movie_script.php?movie=a-beautiful-day-in-the-neighborhood'),(152,'A Beautiful Day in the Neighborhood','https://www.sonypictures.com/movies/abeautifuldayintheneighborhood'),(263,'Near-death experiences','http://iands.org'),(263,'rebirth reports','https://www.youtube.com/watch?v=0AtTM9hgCDw'),(348,'Memory is an amorphous thing, easily influenced by guided imagery and suggestions','https://pubmed.ncbi.nlm.nih.gov/33586291'),(379,'bardo','https://pemachodronfoundation.org/product/how-we-live-is-how-we-die-book')];undo=[]
 for i,a,u in links:
  old=label.sub(r'\1',H[i]);assert old in s and old.count(a)==1
  new=old.replace(a,f'<a target="_blank" rel="noopener noreferrer nofollow" href="{u}">{a}</a>',1);s=s.replace(old,new,1);undo.append((old,new));H[i]=new
 check=s
 for item in placements:check=check.replace(D[int(item['donor_id'][1:])],'',1)
 for a,b in reversed(undo):assert check.count(b)==1;check=check.replace(b,a,1)
 assert check==baseline,'Unexplained source change'
 assert sha(s)=='95a968ab65379887c34a86c946fedc4ba35757cce49260f6049717050ffc08f9','Cross-runtime output mismatch'
 for i in [1,31,60,232]:assert H[i] in s
 (o/'Inner-Child-restored-r01.html').write_text(s)
 receipt={'status':'RESTORATION_COMPLETE_STRUCTURAL_EDIT_PENDING','source_sha256':sha(hs),'donor_sha256':sha(ds),'restored_sha256':sha(s),'paragraph_labels_removed':removed,'empty_editorial_blocks_removed':empty,'placements':placements,'links_restored':[{'human_id':f'H{i:03d}','anchor':a,'href':u} for i,a,u in links],'prose_fidelity':'Exact original label-free HTML recovered after reversing link insertions and donor additions. Native owner objects preserved raw.','native_objects_added':8,'owner_native_objects_preserved':4,'donor_objects_not_used':['D000: owner top chart retained','D038: owner study chart retained','D389: same paralysis illustration already present'],'detector':'Original upload is owner-reported 100% Human; restored assembly is not newly tested.'}
 (o/'RESTORATION-RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:receipt[k] for k in ['status','restored_sha256','paragraph_labels_removed','native_objects_added']},indent=2))
if __name__=='__main__':main(sys.argv[1])
