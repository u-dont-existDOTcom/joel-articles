"""Build a traceable structural map from the literal article and editorial judgments."""
from pathlib import Path
import json, hashlib, re
from bs4 import BeautifulSoup
B=Path(__file__).resolve().parent
source=json.loads((B/'source-blocks.json').read_text())
ledger=json.loads((B/'ASSEMBLY-LEDGER.json').read_text()); revised=ledger['blocks']
# These purposes are editorial interpretations, not new byline text or source claims.
purposes={
'T001':('Why listen to this author?', 'Establish the family history and lived encounters that make the missing third option matter.'),
'T024':('Why does community feel urgent now?', 'Connect renewed demand with loneliness, current interest and the practical objection of freeloading.'),
'T033':('Who takes responsibility when there is no boss?', 'Distinguish shared ownership from the practical work of stewardship and responsibility.'),
'T041':('Why have the available models disappointed?', 'Show the recurring split between outer freedom and inner healing, then articulate the desired combination.'),
'T043':('What does procedural freedom fail to address?', 'Show emotional material becoming politics when no shared practice can address it.'),
'T047':('What can a spiritual community suppress?', 'Expose dependence on a founder’s doctrine while retaining the value of inner practice.'),
'T050':('What positive alternative is being proposed?', 'Bring distributed authority, sacred practice, play and revisable agreements together.'),
'T058':('What are the model’s parts?', 'Define pl/ork and the four complementary functions without making their numbers a chapter schedule.'),
'T062':('What is inner pl/ork?', 'Introduce reparenting and the somatic foundation, with links to the fuller guides.'),
'T067':('What belongs to relational pl/ork?', 'Introduce peer counseling, limits of competence and the separation of listening from control.'),
'T072':('What role might medicine have?', 'Name the optional medicine component and point to its fuller treatment.'),
'T074':('What holds the practices together materially?', 'Introduce the logistical and governance conditions that give the practices a stable home.'),
'T079':('Has the author seen something resembling the whole model?', 'Supply a substantial lived political-economic example, its teaching model and its limits.'),
'T085':('What did the author experience or infer spiritually?', 'Keep personal recollection and speculation visible as the author’s reading, not settled proof.'),
'T087':('How can representatives remain accountable?', 'Describe authority from assemblies and institutional development through lived practice.'),
'T091':('Can accumulated power be brought back down?', 'Use institutional revision and its social foundations to complicate copying a governance chart.'),
'T095':('How can outsiders learn without receiving a blueprint?', 'Explain learning autonomy through everyday participation and the limits of exporting it.'),
'T099':('Does this example establish a fully moneyless economy?', 'Bound the example and distinguish teaching a replicable community from selling transformative visits.'),
'T102':('How much transfer has actually been demonstrated?', 'Preserve the research limitation and a different governance tradition available to study.'),
'T107':('What can I do before committing my life or buying land?', 'Connect values, people, visits, shared practice, capacity and staged participation in one practical route.'),
'T114':('Where might compatible people or communities be found?', 'Offer possible starting communities and explain what visiting teaches about fit.'),
'T120':('Which values need to be visible before attraction takes over?', 'Create a compatibility screen, including unresolved questions rather than assumed agreement.'),
'T126':('What are we materially committing to?', 'Separate land, rights, resources and money stages from the preliminary practice group.'),
'T128':('How could internal and external money use change?', 'Retain the three stages and their constraints rather than treating moneylessness as one switch.'),
'T135':('Who can overrule or replace those who founded this?', 'Make formal and informal power inspectable, including the author’s own potential power.'),
'T146':('How could these very practices become coercive?', 'Apply the model’s own commitments to privacy, dissent, rights and cult risk.'),
'T156':('How can autonomy spread without one founder or new central state?', 'Place distributed learning, solidarity and experimentation directly after concentrated-power risks.'),
'T162':('Must a disagreement lead immediately to full separation?', 'Give a gradient of experiments and preserve cases that need real assets to be tested fairly.'),
'T166':('Do my needs and this group’s resources fit now?', 'Explain capacity without treating it as moral worth; preserve self-implication and the elitism risk.'),
'T184':('How do interest and a visit become responsibilities and membership?', 'Keep gradual participation adjacent to capacity, while making later agreements prerequisites to commitment.'),
'T193':('What happens when living together ends?', 'Distinguish voluntary departure, protective removal and institutional dissolution after commitments are visible.'),
'T194':('Can someone actually afford to leave?', 'Make exit materially possible and agreed before conflict.'),
'T196':('How can removal protect people without becoming abuse?', 'Retain cause, fair process, evidence, independent review and support during separation.'),
'T201':('Who carries essential obligations when the institution ends?', 'Preserve continuity of care, practical transition responsibilities and relationships that can outlast the commune.'),
'T210':('Which outside systems do we keep, limit or share?', 'Turn technology and health-care dependence into concrete shared-life decisions.'),
'T223':('What changes when attraction and breakup affect a whole group?', 'Separate relationship agreements from jealousy governing housing, security and communal power.'),
'T233':('How does this arrangement work for children who did not choose it?', 'Use children’s later perspective to examine care, attachment, freedom, protection and adult departure.'),
'T243':('What can communal parenting add without displacing attachment?', 'Distinguish distributed care from separating children from secure parental bonds.'),
'T248':('How do children get autonomy without losing protection?', 'Keep agency, ordinary adult bonds, reporting and protection usable together.'),
'T256':('What about children who themselves seriously endanger others?', 'Retain the evidentiary gap and competent-help boundary for the hardest cases.'),
'T258':('Will grown children be free and able to choose their next life?', 'Make departure and possible return or new communities meaningful rather than compulsory belonging.'),
'T261':('What practical preparation makes departure possible?', 'Balance survival constraints with transferable skills, records, relationships and feasible next steps.'),
'T267':('What distinguishes this healing-community proposal?', 'Explain the medicine component early, keeping preparation, benefits, risks, authority and legal conditions together.'),
'T274':('What has to come before a ceremony?', 'Keep somatic, relational and reparenting prerequisites ahead of the fuller benefit discussion.'),
'T279':('What can an established community contribute to an experience?', 'Develop integration, belonging, trust, rhythm, logistics and play as distinct benefits.'),
'T281':('When should the community pause or say no?', 'Retain adverse-effects evidence and limits without the repeated announcement of being balanced.'),
'T285':('Why not give all authority to a special shaman?', 'State the author’s stance, respect and disagreements with traditions, and the risk of informal hierarchy.'),
'T292':('What practical competence does a peer ceremony require?', 'Keep preparation, screening, sober support and emergency planning with the activity they govern.'),
'T298':('What should follow the urge to build a village after a peak experience?', 'Distinguish a durable call from grandiosity and connect training with helping others build.'),
'T304':('What changes when communal life is inherited rather than newly assembled?', 'Ground the proposal in present lived surroundings, warmth and serious limits.'),
'T316':('Who may be excluded from a generous communal culture?', 'Keep belonging, social cruelty and avoidance of confrontation in the same lived account.'),
'T325':('What happens to communal obligation inside a cash economy?', 'Explain the mismatch between inherited sharing duties and weakened communal support.'),
'T330':('What does the author hope readers will do, and what is his own plan?', 'Return to the father’s work and a plural future without misrepresenting current recruitment.'),
'T335':('Where can readers go deeper?', 'Keep films, practical manuals, competing models and the research trail available outside the main route.'),
'T336':('What can I watch?', 'Provide the curated films and their distinct reasons for inclusion.'),
'T338':('What can I read next?', 'Group books and papers into useful subject paths.'),
'T339':('Where is the child-rearing material?', 'Point to the two distinct parenting sources.'),
'T341':('Where are detailed founding tools?', 'Point to practical community-building manuals.'),
'T343':('Where are the governance exercises and manuals?', 'Separate deeper procedural guidance from the persuasive article.'),
'T345':('What counts as success beyond longevity?', 'Collect different accounts of commitment, authority and durable communities.'),
'T347':('Where are the Zapatista sources?', 'Keep the historical book and direct movement archive accessible.'),
'T349':('Where is the larger source audit?', 'Link the research report without turning the article into its complete ledger.'),
'N001':('How do we try living relationally before taking on property?', 'Keep enjoyable shared practice before its harder conflict and commitment tests.'),
'N002':('What legal and public conditions affect this component?', 'Preserve the existing jurisdictional examples and local-advice conclusion without making them the chapter opening.')}
old={x['id']:x for x in source};new={x['id']:x for x in revised}
def extract(rows):
 out=[];stack=[]
 for i,b in enumerate(rows):
  if b['tag'] not in ('h1','h2','h3','h4','h5','h6'): continue
  level=int(b['tag'][1]);title=b['text']
  while stack and stack[-1][1]>=level:stack.pop()
  parent=stack[-1][0] if stack else None
  stop=next((j for j in range(i+1,len(rows)) if rows[j]['tag'].startswith('h') and rows[j]['tag'][1:].isdigit() and int(rows[j]['tag'][1])<=level),len(rows))
  content=[x for x in rows[i+1:stop] if x['text'] and x['tag'] in ('p','ol','ul','blockquote')]
  entry=content[0]['text'] if content else ''
  exit=content[-1]['text'] if content else ''
  out.append({'id':b['id'],'title':title,'level':level,'parent':parent,'index':i,'block_ids':[x['id'] for x in rows[i:stop]],'opening':entry,'ending':exit})
  stack.append((b['id'],level))
 return out
on=extract(source);nn=extract(revised);od={x['id']:x for x in on};nd={x['id']:x for x in nn}
for n in nn:
 q,p=purposes[n['id']];n['reader_question']=q;n['purpose']=p;n['interpretation_status']='EDITORIAL_JUDGMENT'
 n['old']=od.get(n['id']);n['changed']=n['id'] not in od or (n['parent'],n['level'],n['title']) != (od[n['id']]['parent'],od[n['id']]['level'],od[n['id']]['title'])
# Order-change reports use named groups; simple raw-index deltas would label everything after an insertion as moved.
moves=[
 {'id':'M01','nodes':['T267'],'title':'Bring the distinctive medicine chapter forward','from':'After the children’s chapter','to':'Immediately after the Zapatista example','why':'Readers reach the feature that inspired the article before a long run of administrative choices. The concrete whole-model example still comes first.','cost':'The legal and ceremonial detail arrives before the practical group-building route. A new internal heading and the existing integration-first section keep it navigable.','repairs':['Medicine opens with the author’s actual reason for including it, followed by preparation.','The legal survey is retained under Legality and Public Practice.','The informal-shaman paragraph points forward to the Founderism questions.'],'status':'APPLIED'},
 {'id':'M02','nodes':['T107','T120','T114','N001'],'title':'Make the practice route follow successive decisions','from':'Activities and conflict first, then finding people, then values','to':'Values → people and visits → shared practice → readiness → staged membership','why':'Readers can screen their values before visiting or romanticizing a place, then learn what to try with actual people.','cost':'It places reflection before some of the immediately enjoyable suggestions. The short no-land opening and goats example preserve the invitation.','repairs':['Added Practice Before Committing as a small orientation heading.','Kept the conflict test and its next-paragraph referents adjacent.'],'status':'APPLIED'},
 {'id':'M03','nodes':['T166','T184'],'title':'Keep readiness and entry into membership together','from':'A separate late absorption chapter followed by its membership subsection','to':'Two linked subsections within Practicing Community','why':'Personal capacity, available communal support, visits and growing responsibilities now form one reader task.','cost':'Full financial and governance agreements are explained later. Reading about the membership process must not be mistaken for permission to commit before settling them.','repairs':['Added a short pointer at the end of the practice chapter to the later commitments and exit terms.','Preserved optional medicine, care exceptions and the warning about capacity becoming elitism.'],'status':'APPLIED'},
 {'id':'M04','nodes':['T210','T223','T233','T126'],'title':'Work through shared-life and material commitments before endings','from':'Leaving and dissolution preceded technology, relationships, children and medicine','to':'Technology → relationships → children → property/money → governance → leaving','why':'The reader knows what life together requires before considering how it ends. Land is no longer a subsection of a preliminary practice group.','cost':'The detailed exit section is later than the first discussion of property and membership.','repairs':['Property points directly to the Founderism test and named exit section.','The practice chapter also names the later exit agreement.'],'status':'APPLIED'},
 {'id':'M05','nodes':['T135','T156'],'title':'Keep the founderism problem beside its distributed alternative','from':'Founderism followed by Movement','to':'Same adjacency, after material commitments','why':'This directly implements Joel’s clarification: federation, daughter communities and supported experiments answer the danger of capture by a single founder.','cost':'Some early discussions already raise power questions. The early medicine pointer gives readers access without repeating the whole critique.','repairs':['No extra chapter is inserted between Founderism and Movement.','The owner’s earlier-approved informal-founder wording is left intact.'],'status':'APPLIED'},
 {'id':'M06','nodes':['T058','T033','T126','T338'],'title':'Make heading levels match actual parent–child relations','from':'Skipped overview levels, money inside practice, book categories at the wrong level','to':'Model components under their overview; money its own chapter; book categories beneath Books and Papers','why':'Skimmers and the visual outline now see the structure the prose actually uses.','cost':'Heading sizes change on the publishing surface, while words and native media remain intact.','repairs':['Removed only the stray 3: from the full medicine chapter, not the numbered model overview.'],'status':'APPLIED'}]
edges=[]
def edge(a,b,kind,why):edges.append({'from':a,'to':b,'type':kind,'why':why})
edge('T058','T267','definition','The model overview defines medicine pl/ork before its detailed chapter.')
edge('T079','T156','example','The Zapatista example supplies the precedent for autonomy spreading beyond one community.')
edge('T274','T279','reading_prerequisite','Preparation and integration precede the expanded account of benefits.')
edge('T274','T292','action_prerequisite','Preparatory relational and somatic work precedes actual medicine use; reading position is not a use schedule.')
edge('T285','T135','cross_reference','The medicine discussion names the later founder accountability test.')
edge('T120','T114','reading_prerequisite','The values list is available before the visiting advice.')
edge('T114','N001','reader_progression','Find people or visit a community, then try activities and work through conflict.')
edge('N001','T166','reader_progression','Shared experience is followed by a capacity and fit assessment.')
edge('T166','T184','reader_progression','Capacity and membership stages are adjacent subsections.')
for x in ['T210','T223','T233','T126','T135','T193']:edge(x,'T184','action_prerequisite','These agreements must be understood before long-term commitment, although their detail is read after the membership process is introduced.')
edge('T126','T135','cross_reference','The property paragraph explicitly directs the reader to founder power.')
edge('T126','T193','cross_reference','Property contributions need the later exit terms before anyone commits.')
edge('T135','T156','antidote','Joel explicitly identifies Movement as the antidote to founderism and asks for adjacency.')
edge('T156','T162','reader_progression','Understand the distributed movement before deciding how much independence an experiment needs.')
edge('T233','T193','reading_prerequisite','Child-related commitments remain visible before departure and dissolution.')
edge('T304','T330','payoff','A present communal culture’s strengths and limits lead into the author’s personal hope and plan.')
edge('T001','T330','callback','The ending returns to the father’s film introduced at the beginning.')
questions=[
 {'id':'Q1','title':'How much of the legal survey belongs in the main article?','heading':'Legality and Public Practice','blocks':['T268','T269','T270','T271'],'current':'All jurisdictional examples and distinctions remain, unchanged. They now sit later within the early medicine chapter.','question':'Keep the complete survey here, or move the detailed country examples to the appendix while leaving the jurisdictional warning and local-advice conclusion here?','recommendation':'Retain it in this candidate. Moving examples to the appendix is a reversible pacing option; do not silently delete their distinct legal meanings.','options':['Keep the current body treatment','Move examples to the appendix; retain links and distinctions','Discuss a shorter replacement first']},
 {'id':'Q2','title':'How much dissolution detail should the reader carry in the main text?','heading':'When the Community Dissolves','blocks':['T204','T205'],'current':'The full continuity-of-care and asset/responsibility inventory remains. No independent obligation was deleted as “obvious.”','question':'Keep the detailed inventory in the main chapter, or retain a shorter main explanation and move the complete checklist to the appendix?','recommendation':'Keep the existing wording until you choose its scope. Care, dependants, records, assets and liability are not all the same obligation.','options':['Keep the detailed inventory','Move the complete inventory to the appendix with a pointer','Discuss a compact integrated version first']}]
# Bind question quotes to literal source blocks rather than recreating passages.
for q in questions:q['excerpts']=[{'id':x,'text':old[x]['text']} for x in q['blocks']]
clusters=[
 {'id':'C-practice','topic':'Beginning together, readiness and admission','occurrences':['T107','T114','T120','T166','T184'],'primary_home':'T107','dispositions':{k:'RELOCATED_WITH_DISTINCT_FUNCTION' for k in ['T107','T114','T120','T166','T184']},'result':'RESOLVED','why':'The complete current cluster has one parent. Values, finding people, practice, capacity and admission are separate steps rather than repeated invitations.'},
 {'id':'C-medicine','topic':'Preparation, benefits, risks and peak-experience temptation','occurrences':['T072','T274','T279','T281','T298'],'primary_home':'T267','dispositions':{'T072':'SHORT_OVERVIEW_POINTER','T274':'PREREQUISITES','T279':'DISTINCT_BENEFITS','T281':'DISTINCT_RISKS','T298':'POST_PEAK_FOUNDING_MOTIVE'},'result':'RETAINED_DISTINCT_FUNCTIONS','why':'The brief overview points to the full treatment. Preparation is not a duplicate of observed benefits; the closing founding urge has a different decision.'},
 {'id':'C-exit','topic':'Independent choice, material commitments and exit','occurrences':['T127','T187','T190','T194','T196','T201','T258'],'primary_home':'T193','dispositions':{'T127':'EARLY_PROPERTY_POINTER','T187':'MEMBERSHIP_AGREEMENT','T190':'OPTIONAL_MEDICINE_AND_FIT','T194':'VOLUNTARY_EXIT','T196':'INVOLUNTARY_REMOVAL','T201':'INSTITUTION_END','T258':'GROWN_CHILD_AUTONOMY'},'result':'RETAINED_DISTINCT_FUNCTIONS','why':'These affect different actors or powers. Short early pointers keep later safeguards available without reprinting their procedures.'},
 {'id':'C-overcompletion','topic':'Long research/legal and continuity checklists','occurrences':['T268','T269','T204','T205'],'primary_home':None,'dispositions':{'T268':'RETAINED_PENDING_OWNER_Q1','T269':'RETAINED_PENDING_OWNER_Q1','T204':'RETAINED_PENDING_OWNER_Q2','T205':'RETAINED_PENDING_OWNER_Q2'},'result':'RETAINED_PENDING_OWNER','why':'Distinct examples and obligations remain. Optional scope decisions are shown with exact source passages; no permission is inferred from AI provenance.'}]
flow={'format':'joel-literal-article-map-v1','revision':'r03-candidate','source_sha256':ledger['source_sha256'],'candidate_sha256':ledger['candidate_sha256'],'owner_answers_sha256':ledger['owner_answers_sha256'],'audience_assumption':'Interested readers of Joel’s healing and community writing, including people exploring a practice group or a move—not only legal incorporators. This is an editorial assumption offered for review.','nodes':nn,'old_nodes':on,'edges':edges,'moves':moves,'questions':questions,'clusters':clusters,'constraints':[{'type':'adjacent_h1','before':'T135','after':'T156','authority':'owner sequence.note'}, {'type':'same_parent','nodes':['T166','T184'],'parent':'T107','authority':'implementation of owner tentative practice/readiness proposal'}, {'type':'before','before':'T233','after':'T193','authority':'owner commitments before leaving'}, {'type':'before','before':'T126','after':'T193','authority':'owner commitments before leaving'}, {'type':'before','before':'T120','after':'T114','authority':'chosen reader-values-before-visits route'}, {'type':'before','before':'T274','after':'T279','authority':'preserved preparation-first source architecture'}, {'type':'heading','node':'T267','title':'The Medicine Part - Yes, I’m Naming It','authority':'owner E19'}], 'alternatives':[{'name':'Chosen: distinctive model, then decisions','summary':'Whole example → early medicine → values/people/practice/capacity/admission → life and material agreements → Founderism/Movement → exit.','gain':'Honors the signature draw, links fit to entry and preserves the founderism antidote.','cost':'Some agreements follow the introduction of membership; exact forward pointers make them prerequisites to commitment.'},{'name':'Strict action-order route','summary':'Practice and agreements first; detailed medicine only after institutional preparation.','gain':'Procedure reads in approximately the order it is performed.','cost':'Buries the distinctive feature the owner says inspired the article; reading about medicine early is not taking it early.'},{'name':'Design-first admission route','summary':'Capacity early, all institutional design, then staged membership before leaving.','gain':'Every commitment is explained before the membership procedure.','cost':'Separates personal fit from the next practical contact/visit steps by many chapters. A fresh reader preferred tighter adjacency.'}], 'review_status':'AWAITING_OWNER_FINAL_APPROVAL','replay_status':'NOT_RUN'}
(B/'STRUCTURE-MAP.json').write_text(json.dumps(flow,ensure_ascii=False,indent=2)+'\n')
print('Map',len(nn),'headings',len(edges),'dependencies',len(moves),'change groups')
