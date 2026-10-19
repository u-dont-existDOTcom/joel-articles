from pathlib import Path
from article_edit import parse,BASE,SOURCE
from bs4 import BeautifulSoup
import json,hashlib,re,shutil

source=SOURCE.read_text();opening,items=parse(source)
by={i['id']:dict(i) for i in items}; changes=[]
def replace(block,old,new,reason,kind='wording'):
 r=by[block];assert r['raw'].count(old)==1,(block,old)
 before=r['raw'];r['raw']=before.replace(old,new,1)
 changes.append({'id':f'W{len(changes)+1:02}','block':block,'kind':kind,'before_html':before,'after_html':r['raw'],'old':old,'new':new,'reason':reason})
def level(block,old,new,why):
 r=by[block];assert r['tag']==old
 before=r['raw'];r['raw']=re.sub(r'^<'+old+r'\b','<'+new,r['raw']);r['raw']=r['raw'].replace('</'+old+'>','</'+new+'>');r['tag']=new
 changes.append({'id':f'W{len(changes)+1:02}','block':block,'kind':'heading_level','before_html':before,'after_html':r['raw'],'reason':why})
def add(key,raw,why):
 assert key not in by;tag=BeautifulSoup(raw,'html.parser').find();by[key]={'id':key,'index':None,'start':None,'end':None,'tag':tag.name,'text':tag.get_text(' ',strip=True),'raw':raw,'classes':[]}
 changes.append({'id':f'W{len(changes)+1:02}','block':key,'kind':'addition','before_html':'','after_html':raw,'reason':why})
def R(a,b):return [f'T{x:03}' for x in range(a,b)]

# Owner's note distinguishes component numbers from chapter order.
replace('T267','3: The Medicine Part','The Medicine Part','Owner E19: remove orphaned chapter number; the four component labels remain unchanged.','heading')
# Repair obvious transcription/typing defects only; do not normalize colloquial voice.
for block,old,new,why in [
('T048','Many people already realized that are more interested','Many people have already realized that they are more interested','Restore the missing grammatical subject; preserve the comparison.'),
('T048','prison-monestary','prison-monastery','Spelling only.'),
('T118','you mind find','you might find','Obvious typo.'),
('T113','once you’re passed those phases','once you’re past those phases','Passed/past grammar in the existing sentence.'),
('T253','amazng','amazing','Obvious typo.'),
('T255','going on their as a disciplinary practice','going on there as a disciplinary practice','Their/there typo.'),
('T014','childrens’ psyches','children’s psyches','Plural possessive spelling.')]:
 replace(block,old,new,why,'copyedit')
# A new opening should name its subject without importing a new proposition.
replace('T272','I’m talking about it here','I’m talking about psychedelics here','The author’s reason for including medicine now opens the chapter; make the referent explicit.')
replace('T282','If this article is going to be honest, it has to talk about both the value and the risk. ','','Remove a self-referential preview; The Case Against Psychedelics and the following risk evidence already perform that job.','duplicate_scaffolding')
# A meaningful navigation pointer, not a new safety or factual claim.
replace('T290','Though neither of these seem like a complete solution.','Though neither of these seem like a complete solution. The four questions in “Founderism” below apply to these roles too.','Medicine moves early; point to the later accountability test rather than repeat it.')
# Existing numbered component list remains internal to its overview.
for b in ['T062','T067','T072','T074']:
 level(b,'h3','h2','The numbered components are direct children of the four-part overview, not subchildren of a missing h2.')
level('T033','h3','h2','The Freeloader Problem is the first direct subsection of Communes Are Hot Again.')
level('T126','h2','h1','Property and resource commitments become their own chapter after shared-life choices.')
level('T128','h3','h2','Moving Beyond Money remains the subsection of the property/resource chapter.')
level('T166','h1','h2','Readiness/capacity now belongs inside Practicing Community, beside staged admission.')
# Formal membership remains h2, adjacent to readiness inside Practice.
for b in ['T339','T341','T343','T345','T347']:
 level(b,'h2','h3','Book categories belong beneath Books and Papers, in Reading Order.')
add('N001','<h2>Practice Before Committing</h2>','After finding people, the existing meals, peer practice and conflict-test paragraphs answer what to try together.')
add('N002','<h2>Legality and Public Practice</h2>','Relocate the existing country-law survey as background inside the medicine chapter rather than leading with it. No legal content changed.')
add('N003','<p>Before making long-term commitments, work through the choices below about technology, relationships, children, money, and founder power. The exit terms in “Leaving, Removal, and Dissolution” belong in those agreements too.</p>','The practice, readiness and staged-membership process is kept together. This pointer makes the later policy and exit agreements prerequisites to commitment, not later optional homework.')
replace('T127','outside debts… oh my!','outside debts… oh my! Read the founderism questions next, and agree on the exit terms in “Leaving, Removal, and Dissolution” before anyone commits.','Property decisions need both governance and exit arrangements; bring later safeguards to the decision point with an exact heading pointer.')

# Every original top-level object is retained once; only the explicitly logged text edits differ.
# Existing separator objects travel with the adjacent source block group where possible.
order=(R(0,107) +
       ['T267','T272','T273'] + R(274,285) + ['N002'] + R(268,272) + R(285,304) +
       R(107,111) + R(120,126) + R(114,120) + ['N001'] + R(111,114) + R(166,192) + ['N003'] + ['T192'] +
       R(210,267) + R(126,166) + R(193,210) + R(304,351))
assert len(order)==len(set(order)), 'repeated block in assembly'
assert set(order)==set(by), (set(by)-set(order),set(order)-set(by))
revised=opening+''.join(by[x]['raw'] for x in order)+'</div>'
parse(revised)  # Round-trip structural integrity.
source_copy=BASE/'Owner-Source-1454.html';source_copy.write_text(source)
candidate=BASE/'Community-Article-r03-candidate.html';candidate.write_text(revised)
# Exact owner answers already live beside this case; do not copy a file onto itself.

# Provenance IDs live in external ledgers; no spurious metadata is inserted in Substack content.
for idx,key in enumerate(order):
 by[key]['new_index']=idx
 by[key]['text']=BeautifulSoup(by[key]['raw'],'html.parser').get_text(' ',strip=True)
for c in changes:
 c['candidate_index']=order.index(c['block']);c['source_index']=next((x['index'] for x in items if x['id']==c['block']),None)
sha=lambda x:hashlib.sha256(x.encode()).hexdigest()
ledger={'format':'joel-editorial-assembly-v1','revision':'r03-candidate','source_sha256':sha(source),'candidate_sha256':sha(revised),'owner_answers_sha256':hashlib.sha256((BASE/'OWNER-ANSWERS.json').read_bytes()).hexdigest(),'status':'OWNER_REVIEW_PENDING','article_published':False,'source_only_replay':'NOT_RUN','article_factual_review':'NOT_PERFORMED','pangram':'NOT_RETESTED','old_order':[x['id'] for x in items],'new_order':order,'blocks':[{k:by[key][k] for k in ['id','index','new_index','tag','text','raw']} for key in order],'edits':changes}
(BASE/'ASSEMBLY-LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print('Candidate hash',sha(revised),'bytes',len(revised.encode()),'edits',len(changes),'blocks',len(order))
for x in order:
 if by[x]['tag']=='h1':print(x,by[x]['text'])
