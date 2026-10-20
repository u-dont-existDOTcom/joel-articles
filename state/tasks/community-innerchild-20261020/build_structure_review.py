"""Reuse the tested structure-review UI with an exact current article model."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,re,hashlib,html,difflib
import sys
esc=html.escape
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def build(root):
 r=Path(root);o=r/'articles/inner-child-therapy/candidate/editorial-20261020';d=json.loads((o/'FINAL-ASSEMBLY.json').read_text());B={b['id']:b for b in d['blocks']};old_order=d['original_order'];new_order=d['candidate_order'];plain=lambda s:BeautifulSoup(s or '', 'html.parser').get_text(' ',strip=True)
 purposes={
 'D002':('Can I feel what this is about?','Offer the supplied meditation and subtitled song before the author responds to them.'),
 'H006':('Who is meant to grow, and what if that adult is missing?','Explain the three adult functions, the child’s worth, and the provisional path of borrowed adulthood.'),
 'H018':('Why did this matter to the author?','Ground the guide in lived experience and show why spiritual freedom alone did not reach every wound.'),
 'H032':('How do I accept help without surrendering my judgment?','Gather the general safeguard and the later concrete mechanisms of misplaced authority.'),
 'H038':('Am I ready for the depth I am about to try?','Keep orientation, bodily access, representation and protective intent near the start, without the long social detour.'),
 'H087':('What if thinking does not take the form of voices?','Keep nonverbal and deliberate verbal options available before asking for inner dialogue.'),
 'H091':('What if the present adult actually wants to harm vulnerability?','Keep the source’s exceptional adult-focused restriction visible before child-directed methods.'),
 'H099':('How can usable care begin before I feel like the adult?','Bring small competencies, absent warmth, remembered competence, perspective and motivation into one chapter.'),
 'H104':('What is the smallest adult function I can actually borrow?','Place the no-warmth and threatening-imagery difficulty immediately beside the existing minimal-care response.'),
 'H317':('Could a wiser future perspective help now?','Keep this alternative beside the other borrowed perspectives rather than separated in the late exercise inventory.'),
 'H321':('Have I handled something before that can help me now?','Use actual past competence without turning it into a new standard for self-attack.'),
 'H359':('What brought me here when I feel no self-love?','Use the person’s actual motivation as an entry point, without insisting it is already love.'),
 'H111':('What existing love or caring perspective can I use?','Distinguish accessible love for others from care that lands for oneself; keep practical experiments.'),
 'H117':('What sincere wish is available before warm love?','Keep goodwill as an early alternative, not an obligation to feel the right emotion.'),
 'H137':('How does care become credible over time?','Connect visible actions, love and distrust, bounded promises and daily relationship.'),
 'H080':('When does processing become a demand for certainty?','Distinguish revisiting pain from checking; move general strategy assessment to the strategy section.'),
 'H316':('What can I try in a session or ordinary day?','Bring simple exercises forward after usable adult care and trust, before extended troubleshooting.'),
 'H049':('What is the first moment I can notice before reacting?','Place the hook explanation before the daily practice that uses it, retaining present-danger exceptions.'),
 'H345':('How can an old photograph help without becoming evidence of an invented memory?','Keep the photographic exercise and its epistemic limits together.'),
 'H352':('How do I finish and return to the room?','Keep the closure directly after the photo exercise it names, with checking already introduced.'),
 'H171':('Why does the adult voice feel fake or get blocked?','Concentrate inherited scripts, protective responses and strategy changes rather than beginning a long special-topic detour.'),
 'H197':('How can I hear the guard without forcing it aside?','Join the emotional-permission explanation to the actual protective-part method.'),
 'H202':('What should change if the practice is not helping?','Bring general outcome assessment into the explicit strategy decision, away from the checking example.'),
 'H208':('What does a sudden wish to escape tell me?','Keep the early warning against forcing through guards; its later altered-state application remains distinct.'),
 'H271':('What if an authentic child or preference never had room to develop?','Preserve late developmental play and differentiation without turning uncertainty into defectiveness.'),
 'H294':('Can new preferences be allowed to grow imperfectly?','Prepare the direct new-interest example in the following Guide section.'),
 'H298':('How do direction and standards support rather than suppress development?','Keep the Guide’s examples and individual timing, without the heading implying an absolute sequence.'),
 'H313':('Does everyone need the same order?','Preserve the source’s timing qualification and the later named cross-reference.'),
 'H364':('How much love and wellbeing might be possible beyond ordinary coping?','Gather the extended happiness, gratitude, spiritual-loss and felt-depth material into one identifiable chapter.'),
 'H120':('What about a love much larger than everyday affection?','Retain the author’s spiritual depth and connect it to the following gratitude practice.'),
 'H123':('How does gratitude become experiential rather than forced?','Preserve the personal examples, caveats and return to the child in one sustained treatment.'),
 'H132':('What if spiritual support itself has been damaged?','Keep betrayal and relinquishing control within the same spiritual-love chapter.'),
 'H362':('What if bodily holding blocks emotional access?','Keep this bodily route alongside the other remaining difficulties with receiving love.'),
 'H371':('What if contact is real but still feels small?','Distinguish shallow contact from absence of love without an orphaned opposite-problem transition.'),
 'H384':('How does this work with actual people?','Gather first contact, paced disclosure, others’ capacity, fair response and peer counseling as applications.'),
 'H064':('Must I finish healing before reaching toward people?','Preserve the explicit no: connection is part of the care, not a reward for completing this reading route.'),
 'H055':('What can I realistically rely on from this particular person?','Keep recurring behavior, valid boundaries and uncertainty together.'),
 'H073':('How can I revise a response without rejecting the person who wrote it?','Preserve the pause, concrete story, responsibility and return to care.'),
 'N001':('How does shared peer attention work?','Name the Hearthwork passage already present, without adding a therapeutic claim.'),
 'H373':('How can forgiveness coexist with accountability and boundaries?','Preserve a distinct relational decision rather than treating it as synonymous with trust or reconciliation.'),
 'H378':('What if life has changed and the next identity is not clear yet?','Keep transitions, grief and uncertainty as their own application.'),
 'H212':('What do altered states change, and what do they not establish?','Make the specialist discussion visible after the core method; retain personal experiences, interpretation and limits.'),
 'H249':('How does physical pain interact with emotional care?','Keep the author’s account and the bodily/meaning distinction in a findable special-topic chapter.'),
 'H257':('What happens when somebody wants to die?','Keep the source’s immediate human-help paragraphs first, followed by its attributed spiritual reasoning.'),
 'H401':('What kind of therapist could help with this?','Place practical referral choices before the final encouragement, keeping clinical comparisons in the appendix.'),
 'H398':('What does the author want me to take into life?','Preserve the brief personal encouragement as the real ending, not an introduction to more logistics.'),
 'H407':('How does this relate to other clinical approaches?','Keep reference comparisons available after the main article.'),
 }
 def nodes(order,field):
  result=[];stack=[]
  for i,k in enumerate(order):
   raw=B[k][field]
   if not raw or not re.match(r'<h[1-6]\b',raw):continue
   lev=int(re.match(r'<h([1-6])',raw).group(1));title=plain(raw)
   while stack and stack[-1]['level']>=lev:stack.pop()
   end=i+1
   while end<len(order):
    following=B[order[end]][field] or '';m=re.match(r'<h([1-6])',following)
    if m and int(m.group(1))<=lev:break
    end+=1
   content=[plain(B[j][field]) for j in order[i+1:end] if B[j][field] and not B[j][field].startswith('<div')];q,p=purposes.get(k,('What does “'+title+'” add here?','Develop the source’s '+title.lower()+' discussion within its shown parent; its exact text remains in the reading view.'))
   n={'id':k,'title':title,'level':lev,'parent':stack[-1]['id'] if stack else None,'index':i,'block_ids':order[i:end],'opening':content[0] if content else '', 'ending':content[-1] if content else '', 'reader_question':q,'purpose':p,'interpretation_status':'EDITORIAL_JUDGMENT'};result.append(n);stack.append(n)
  return result
 old=nodes(old_order,'original_html');new=nodes(new_order,'candidate_html');old_by={n['id']:n for n in old}
 for n in new:n['old']=old_by.get(n['id']);n['changed']=not n['old'] or any(n[x]!=n['old'][x] for x in ['index','parent','title','level'])
 moves=[
 ('M01',['H038','H087','H091'],'Concentrate readiness before deeper practice','A readiness chapter containing long social and communication detours','Orientation, body, representation and protective intent together','The practical adult-building method arrives without the long outward-relationship interruption.','Social application comes later, but the article still explicitly rejects waiting to be healed before seeking company.'),
 ('M02',['H099','H104','H317','H321','H359'],'One home for getting access to adult care','Borrowing, later simple exercises and late missing-love troubleshooting','The Borrow the Adult chapter','Alternatives can be compared where the reader actually needs to begin. The no-warmth difficulty sits beside its existing response.','The main chapter is longer; distinct alternatives are retained rather than forced into one method.'),
 ('M03',['H316','H049','H080','H352'],'Bring practice forward and keep it usable','Exercises after identity and many special circumstances; hook and checking earlier elsewhere','Trust → checking → Simple Practices, with hook explanation and deliberate ending','The reader gets usable practice before the extended troubleshooting and special topics.','Some deeper spiritual material is later; it remains reachable rather than a prerequisite to every practice.'),
 ('M04',['H171','H197','H202','H208'],'Keep fake-voice troubleshooting on its problem','Protective parts followed by altered states, pain and crisis before returning to development','Inherited script → protective response → strategy → escape warning','The chapter stays with why attempts feel fake and what changes the next attempt.','The later altered-state chapter must point back to the guard warning; the existing reference remains accurate.'),
 ('M05',['H032','H298','H313'],'Gather authority safeguards and qualify Guide timing','General warning early, manipulation mechanisms later inside Guide','One authority discussion; the Guide keeps development and timing','Concrete mechanisms elaborate the same warning instead of reopening it later. The Guide heading no longer implies an absolute rule.','The early safeguard grows; the direct new-interest example and Timing Is Individual remain together.'),
 ('M06',['H364','H120','H123','H132','H362','H371'],'One sustained chapter for deeper love','Long gratitude discussion inside borrowing, happiness/access questions much later','How Much Happiness Do You Know Is Possible?','The basic method no longer pauses for the whole spiritual exploration, and its related difficulties have one home.','The resulting spiritual chapter remains substantial and distinctive. Shortening or separating it is left as an explicit scope choice.'),
 ('M07',['H384','H064','H055','H073','N001'],'Gather relationship applications','Social contact and replies before adult-building; peer counseling near the end','Connection → disclosure → others’ capacity → response → peer counseling','The same external-relationship task develops in one place.','This is a reading order, not a condition that somebody finish internal practice before contacting a friend.'),
 ('M08',['H212','H249','H257','H401','H398'],'Make special cases visible and preserve the ending','Special topics buried within fake-voice material; therapists after encouragement','Separate altered-state, pain and crisis chapters; therapists → encouragement → appendix','Skimmers can find the relevant situation and the core teaching keeps moving. Crisis support already present in the source is brought first.','The guide remains long. The scope of the special-topic chapters is an owner decision, not silently deleted content.')]
 def neighbor(order,k,field,offset):
  if k not in order:return ''
  i=order.index(k)+offset
  while 0<=i<len(order):
   raw=B[order[i]][field]
   if raw and plain(raw):return plain(raw)[:700]
   i+=offset
  return '(Article boundary)'
 M=[]
 for mid,ids,title,fr,to,why,cost in moves:
  sites=[]
  for k in ids:
   original=B[k]['original_html'];current=B[k]['candidate_html'];name=plain(current or original)
   sites.append('<h4>'+esc(name)+'</h4><div class="comparison two-sites"><section><h3>Old site</h3><div class="excerpt">'+esc(neighbor(old_order,k,'original_html',-1))+'<br><del>'+esc(plain(original) if original else '(No source heading)')+'</del><br>'+esc(neighbor(old_order,k,'original_html',1))+'</div>'+('<a href="Owner-Reading-r03.html#source-'+k+'">Source context</a>' if original else 'New navigation, not moved source wording')+'</section><section><h3>New site</h3><div class="excerpt">'+esc(neighbor(new_order,k,'candidate_html',-1))+'<br><ins>'+esc(plain(current))+'</ins><br>'+esc(neighbor(new_order,k,'candidate_html',1))+'</div><a href="Candidate-Reading-r03.html#candidate-'+k+'">Revised context</a></section></div>')
  M.append({'id':mid,'nodes':ids,'title':title,'from':fr,'to':to,'why':why,'cost':cost,'repairs':['Exact source blocks remain traceable in both reading views.','Any changed wording is paired in the lexical cards and canonical diff.'],'status':'PROPOSED_IN_CANDIDATE','local_sites_html':''.join(sites)})
 E=[('H006','H099','definition','The model supplies the adult functions that borrowing teaches.'),('H038','H099','prerequisite','Readiness precedes adult/child practice.'),('H032','H401','agency','Therapist selection must not surrender the agency established early.'),('H049','H336','prerequisite','The morning practice uses hook recognition already explained.'),('H080','H352','reference','The closure can point back to checking rather than require another certainty ritual.'),('H345','H352','adjacency','The end follows the photograph exercise that it explicitly names.'),('H294','H298','example','The Guide’s new-interest example follows the experimental-play discussion.'),('H313','H212','reference','The altered-state timing pointer now points backward accurately.'),('H208','H212','application','The later altered-state chapter applies the earlier guard warning.'),('H197','H212','reference','The guard method is available before altered-state applications.'),('H120','H212','reference','The altered-state chapter can refer back to the sacred-love discussion.'),('H123','H398','callback','The ending’s loan callback follows the original gratitude section.'),('H064','H384','application','Reaching toward people is part of the relationship work, not postponed until healing is complete.'),('H401','H407','reference','The therapist section names the appendix as the destination for clinical comparisons.')]
 questions=[{'id':'Q1','title':'Keep the extended spiritual-love chapter here?','current':'All the source’s gratitude stories, happiness horizon and spiritual-betrayal material remain. They are now gathered in one chapter.','question':'Keep the full chapter, retain a shorter core with the rest in a companion article, or discuss a specific cut?','recommendation':'Keep it for this candidate: it is distinctive author material. A shorter general-reader guide would need an explicit scope decision.','options':['Keep the complete chapter','Propose a shorter core and separate companion','Discuss as noted'],'excerpts':[{'id':k,'text':plain(B[k]['candidate_html'])} for k in ['H364','H124','H131']]},{'id':'Q2','title':'How large should the special-circumstances part be?','current':'Altered states, spirit relationships, physical pain and the crisis discussion are retained as visible chapters rather than buried inside fake-voice troubleshooting.','question':'Keep them in the main guide, or propose a shorter entry with the detailed treatment linked separately?','recommendation':'Retain them unless you want a narrower core guide. Their length cannot be solved losslessly by deleting a few repeated sentences.','options':['Keep the complete special-topic chapters','Propose a core guide plus separate detailed treatment','Discuss as noted'],'excerpts':[{'id':k,'text':plain(B[k]['candidate_html'])} for k in ['H212','H249','H257']]}]
 D={'format':'joel-literal-article-map-v1','revision':'inner-child-r03-candidate','source_sha256':d['source_sha256'],'candidate_sha256':d['candidate_sha256'],'owner_answers_sha256':None,'audience_assumption':'General readers of Joel’s reparenting guide seeking a usable relationship and practical methods, including people interested in spiritual depth. This is an editorial assumption for review, not a new clinical protocol.','nodes':new,'old_nodes':old,'edges':[{'from':a,'to':b,'type':t,'why':why} for a,b,t,why in E],'moves':M,'questions':questions,'clusters':[],'constraints':[],'alternatives':[{'name':'Selected: core method, then complications and applications','summary':'Experience/model → readiness → borrowing/trust → practice → troubleshooting/development → deeper love → relationships → special circumstances → resources.','gain':'The reader can begin before taking every long side route. Similar explanations and applications have identifiable homes.','cost':'Some warnings and applications point backward; this is not an instruction to delay social support until self-work is finished.'},{'name':'Retain the associative original route','summary':'Keep each complication where the author first thought to introduce it.','gain':'Conversational exploration and fewer long-distance pointers.','cost':'Readers encounter extensive social, spiritual and special-topic material before reaching the basic repeatable practices.'}],'review_status':'AWAITING_OWNER_REVIEW','replay_status':'NOT_A_SOURCE_ONLY_REPLAY'}
 (o/'STRUCTURE-MAP.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
 template=BeautifulSoup((r/'articles/intentional-communities/candidate/finalization-20261019/Structure-and-Decisions-r03.html').read_text(),'html.parser')
 template.title.string='Inner Child · structure and editorial decisions';template.header.find(class_='eyebrow').string='Owner prose preserved · developmental candidate r03';template.header.h1.string='How the Inner Child guide now fits together';template.header.find(class_='subtitle').string='Select a section to compare its place, purpose and dependencies. The source column is the restoration-only baseline: paragraph labels removed and missing media returned. This candidate is not newly Pangram-tested or owner-approved.'
 links=template.header.find(class_='links');links.clear()
 for href,label in [('Side-by-Side-r03.html','Exact wording and placement diff'),('Full-Article-r03.html','Complete commentable article'),('Owner-Reading-r03.html','Read restoration-only baseline'),('Candidate-Reading-r03.html','Read revised order'),('#questions','Two scope decisions')]:
  a=template.new_tag('a',href=href);a.string=label;links.append(a)
 for ident,label in [('export','Export review answers'),('export-md','Export Markdown')]:
  b=template.new_tag('button',id=ident);b['class']='export';b.string=label;links.append(b)
 route=template.find(class_='route');route.clear();route.string='Understand → prepare → borrow care → build trust → practice → troubleshoot → develop → apply → explore special circumstances'
 template.find(id='old-track').parent.h2.string='Restored owner arrangement';template.find(id='changes').h2.string='Eight structural decisions';template.find(id='questions').h2.string='Two scope choices — retained pending your decision';template.find(id='questions').p.string='No independent source claim was silently removed to make the guide shorter. These are the two larger scope decisions the current pass leaves visible.'
 lex=template.find(id='lexical');lex.clear();h=template.new_tag('h2');h.string='Exact local wording changes';lex.append(h);p=template.new_tag('p');p.string='These are disclosures, not a request to reapprove every obvious copy repair. Unchanged moved paragraphs remain intact. You can leave notes on any change you disagree with.';lex.append(p);lexids=[]
 for b in d['blocks']:
  k=b['id'];a=b['original_html'];c=b['candidate_html']
  if a==c or (a and c and plain(a)==plain(c)):continue
  if a and re.match(r'<h',a) and not c:reason='The heading is retired because its complete content now has named homes; no paragraph is deleted.'
  else:reason='Bounded copy/reference repair, heading clarification or redundant scaffolding trim; complete source remains in the baseline.'
  oldwords=re.findall(r'\s+|\S+',plain(a));newwords=re.findall(r'\s+|\S+',plain(c));left=[];right=[]
  for tag,i,j,x,y in difflib.SequenceMatcher(None,oldwords,newwords,autojunk=False).get_opcodes():
   av=esc(''.join(oldwords[i:j]));bv=esc(''.join(newwords[x:y]));left.append(av if tag=='equal' else '<del>'+av+'</del>');right.append(bv if tag=='equal' else '<ins>'+bv+'</ins>')
  lid='W'+k;lexids.append(lid);card='<article class="panel lexical-card" id="lex-'+lid+'"><h3>'+lid+'</h3><p>'+reason+'</p><div class="comparison"><div class="excerpt">'+''.join(left)+'</div><div class="excerpt">'+''.join(right)+'</div></div><p>'+('<a href="Owner-Reading-r03.html#source-'+k+'">Source location</a>' if a else 'New navigational heading')+' · '+('<a href="Candidate-Reading-r03.html#candidate-'+k+'">Revised location</a>' if c else 'Retired heading; content is retained elsewhere')+'</p><label>Optional note<textarea data-answer="'+lid+'.note" aria-label="Note for '+lid+'"></textarea></label></article>';lex.append(BeautifulSoup(card,'html.parser'))
 D['word_change_ids']=lexids;template.find(id='map-data').string=json.dumps(D,ensure_ascii=False).replace('<','\\u003c')
 approval=template.find(id='overall').find_parent('section');approval.h2.string='Candidate approval';approval.p.string='Community r04 is already approved with your specified corrections. This separate Inner Child restructuring is a candidate for your judgment. The restoration baseline remains available; there is no new Pangram result and native audio transfer is not destination-tested.'
 overall=template.find(id='overall');overall.clear()
 for value in ['', 'Approve with revisions as specified','Approve this candidate as-is','Revise the organization as noted','Keep the restoration-only version for now']:
  t=template.new_tag('option',value=value);t.string=value or 'Not decided';overall.append(t)
 script=template.find_all('script')[-1];js=script.string;js=js.replace("'joel-community-r03-'","'joel-innerchild-r03-'").replace("let selected='T107'","let selected='H099'").replace("format:'joel-community-finalization-review-v1'","format:'joel-innerchild-editorial-review-v1'").replace('Community-r03-review','Inner-Child-r03-review').replace('# Community r03 review','# Inner Child r03 review').replace('${m.id} · applied','${m.id} · proposed in candidate')
 js=js.replace("function select(id,rerender=true){if(!all.has(id))return;", "function select(id,rerender=true){if(!all.has(id)){const retired=old.get(id);if(retired){$('detail').innerHTML='<h2>'+esc(retired.title)+'</h2><p>This heading was retired. Its paragraphs remain in the borrowing, protective-part and deeper-love treatments.</p><a href=\"Owner-Reading-r03.html#source-'+id+'\">Read the old location</a>'; }return;}")
 js=js.replace("if(rerender&&n.level>1&&!$('new-'+id)){", "if(rerender&&((o&&!$('old-'+id))||!$('new-'+id))){")
 script.string=js;(o/'Structure-and-Decisions-r03.html').write_text(str(template))
 style='body{margin:0 auto;max-width:820px;padding:28px 22px;font:19px/1.65 Georgia,serif;color:#172a35}p,blockquote,ol,ul{margin:1em 0}h1{margin-top:2em;line-height:1.25}h2,h3,h4{line-height:1.3}section{scroll-margin-top:20px}.native{padding:15px;border:1px dashed #8b9ca6;background:#f5f6f7;font:15px/1.5 system-ui}.id{font:11px system-ui;color:#687b87}a{color:#1e667c}nav{font:15px/1.5 system-ui}'
 for order,field,filename,prefix,title in [(old_order,'original_html','Owner-Reading-r03.html','source-','Restored owner source'),(new_order,'candidate_html','Candidate-Reading-r03.html','candidate-','Revised Inner Child candidate')]:
  pieces=[]
  for k in order:
   raw=B[k][field]
   if not raw:continue
   root=BeautifulSoup(raw,'html.parser').find()
   if root and root.name=='div':
    label='Native '+', '.join(root.get('class',[]));alts=list(dict.fromkeys(x.get('alt','') for x in root.find_all('img') if x.get('alt')));raw='<aside class="native">'+esc(label)+('<details><summary>Source description</summary>'+esc(' | '.join(alts))+'</details>' if alts else '')+'</aside>'
   pieces.append('<section id="'+prefix+k+'"><span class="id">'+k+'</span>'+raw+'</section>')
  (o/filename).write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+'</title><style>'+style+'</style><nav><a href="Structure-and-Decisions-r03.html">Structure and decisions</a> · <a href="Full-Article-r03.html">Commentable article</a></nav><h1>'+esc(title)+'</h1><p>Reading view with typed native-object placeholders; archival HTML carries exact source media markup. Stable IDs below are review locators, not published paragraph labels.</p>'+''.join(pieces)+'</html>')
 print('Structure review:',len(new),'headings',len(M),'relations',len(lexids),'exact lexical cards; source/revision reading anchors generated.')
if __name__=='__main__':build(sys.argv[1])
