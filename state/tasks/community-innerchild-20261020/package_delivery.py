"""Build both exact article families with the canonical portable review packager."""
from pathlib import Path
from zipfile import ZipFile
import subprocess,json,hashlib,html,re,shutil,sys
from bs4 import BeautifulSoup
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main(root):
 r=Path(root).resolve();w=r.parent;runtime=w/'runtime';task=r/'state/tasks/community-innerchild-20261020';c=r/'articles/intentional-communities/candidate/owner-approved-20261020';i=r/'articles/inner-child-therapy/candidate/editorial-20261020';pub=w/'delivery';pub.mkdir(exist_ok=True)
 assert sha(c/'Community-Article-r04-approved.html')=='250d499545e84aae18d23e532922b4110b8adda310b67e28c025f37bf95967be'
 assert sha(i/'Inner-Child-r03-candidate.html')=='91b9065b9a121a40fb54cad2eac1d8be99eb5a24869178c04c26786a163708a4'
 # Protocol display is a companion document, not a new rule copy.
 protocol=(r/'docs/EDITORIAL-DEDUP-EXECUTION.md').read_text();enforcement=(r/'docs/EDITORIAL-EXECUTION-ENFORCEMENT.md').read_text();h='<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{max-width:900px;margin:35px auto;padding:0 22px;font:18px/1.6 system-ui;color:#17333c}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit}h1{line-height:1.2}</style><title>Editing protocol v0.3</title><h1>Shared editing protocol v0.3</h1><p>The rules below incorporate your corrections. They do not certify model quality or install a global ChatGPT/Claude enforcement service. Exact artifact integrity and editorial judgment remain separate.</p><pre>'+html.escape(protocol)+'</pre><h1>Existing enforcement contract and limits</h1><pre>'+html.escape(enforcement)+'</pre>'
 for o in [c,i]:(o/'Editing-Protocol-v03.html').write_text(h)
 cstate='''# Community r04 — approved wording

Controlling baseline: accepted r03 e0f5e871fcc9f4f869a0465c3728be42adc77f5f704a058c8e867597de72e6a0 plus the terminal owner review JSON exported 2026-10-19T22:42:41.505Z. The raw JSON is preserved, including history; terminal decisions and final qualifications govern implementation.

Current artifact: Community-Article-r04-approved.html, SHA-256 250d499545e84aae18d23e532922b4110b8adda310b67e28c025f37bf95967be. It replaces r03 for current editing and is installed as the task branch's registered master. Owner approval is with specified revisions, not approval of the unchanged r03. Historical raw published source and all prior candidates remain preserved.

Completed: owner medicine introduction first; retained personal-model introduction next; restored value/risk opener; owner-written forward reference with two obvious copy repairs; kept detailed dissolution inventory. No new article-wide rewrite. Twenty-eight raw native objects are unchanged and ordered. Removed link occurrences belong only to the owner-deleted legal survey.

The rebuilt helper uses the canonical generator and profile. A parser correction keeps the ordinary research story card as rich HTML instead of treating a null video id as a video-post. No other compatibility strategy is changed. Static conversion and deterministic clipboard sink tests are distinct from actual Opera-to-Substack reconstruction, which remains untested. No exact-r04 Pangram result or full citation audit is asserted. Registry lifecycle remains working pending the separate citation/publication requirements; editorial acceptance is passed and owner review confirmed.

Next: use the delivered helper in a disposable Substack draft and inspect objects before replacing any publication. Nothing was posted. No new approval of the accepted basic copy fixes is requested.
'''
 (c/'PROJECT_STATE.md').write_text(cstate);(c/'CHANGELOG.md').write_text((c/'COMMENT-RESOLUTION.md').read_text()+'\n\n'+(c/'TRANSFER-TYPE-REPAIR.md').read_text());(c/'README.md').write_text('''# Community article — r04 approved

Open **Copy-to-Substack-r04.html** in Opera and click **Copy Article**. Paste into a disposable Substack draft first; actual reconstruction/playback is not certified by a successful clipboard write.

**Changes-r03-to-r04.html** shows your last corrections. **Original-to-r04.html** compares the whole pass with your earlier submitted revision. **Full-Article-r04.html** is the full commentable assembly. **Community-Article-r04-approved.html** is exact archival editor HTML, not an independent hosted website. **Editing-Protocol-v03.html** contains the updated shared rules and their enforcement limits.

The project/manifest and checksums bind the exact article, reviews, owner comments, helper and evidence. Root aliases of the article/reviews are identical copies for convenient navigation; canonical copies also live in article/ and review/. This is the current delivery, not the older r03 ZIP.
''')
 request={'format':'joel-innerchild-edit-request-v1','source_humanized_sha256':'d246b51a181cbc480a857c9406469467000675cbe31426950c66b24809c2e178','formatting_donor_sha256':'68f710a170fb33e29ed1d3e76fbe9ed95aa79a3c523ac497784e1b41ec8c6853','owner_request':'pasting my current version of humanized inner child therapy article (passes pangram 100%). i think it needs considerable work. you can remove all the paragraph numbers. and you can merge it with the formatting/embeds etc from the mostly AI version i am pasting now (which doesn\'t have paragraph #s):','authority':'Humanized owner prose controls wording. Other source is a formatting/media donor, not permission to replace the prose.','candidate_approval':'NOT_GIVEN','detector':'Original score is owner-reported only; no new result.'};(i/'source-comments.json').write_text(json.dumps(request,ensure_ascii=False,indent=2)+'\n')
 istate='''# Inner Child — structural candidate r03

Current candidate: Inner-Child-r03-candidate.html, SHA-256 91b9065b9a121a40fb54cad2eac1d8be99eb5a24869178c04c26786a163708a4. NOT owner-approved or newly detector-tested.

Wording baseline: exact owner upload d246b51a181cbc480a857c9406469467000675cbe31426950c66b24809c2e178. Formatting donor: 68f710a170fb33e29ed1d3e76fbe9ed95aa79a3c523ac497784e1b41ec8c6853. Restoration-only r01: 95a968ab65379887c34a86c946fedc4ba35757cce49260f6049717050ffc08f9. The restoration baseline remains a separate rollback; the AI donor is never a replacement master.

Completed: 322 editorial paragraph labels removed, genuine numbered lists retained; eight absent native objects restored, four current owner objects preserved, seven source-supported links returned. Every nonempty humanized source paragraph is retained. The developmental pass reorganizes the route, gathers warmth/authority/application clusters, repairs heading relationships and specific referents, retires one emptied heading and trims repeated scaffolding. Exact block mapping and local before/after records accompany the candidate.

Review: fresh complete r02 candidate-only read, then source-based reconciliation and fresh r03 review of the changed natural boundaries and exact wording. A false list-formatting finding was traced to the reviewer serialization, not silently imposed on the article. The final delta review confirmed no repair. It is not a new full-article independent pass, cross-family corroboration or Pangram certificate.

Two owner scope choices remain: extent of the spiritual-love chapter, and extent of the altered-state/pain/crisis chapters. Both are retained rather than silently cut. The diagram makes the candidate route and its alternatives explicit. Do not treat reading order as an instruction to finish internal work before seeking social support.

Native source fidelity passes. Audio and native video remain intact in archival HTML. Their source objects do not establish transfer portability: no ready-to-paste Inner Child helper or actual destination success is claimed in this editorial-review delivery.

The registered raw master and other active humanization branch are not overwritten. The uploaded owner snapshot controls this separate editing task; the parallel integration lock remains respected. The original-Claude source-only replay is separate and unrun.

Next owner boundary: review the structural page, accept or revise the candidate and resolve scope only where it matters. The raw source, restoration and earlier candidate remain available. Resume from the exact chosen version and exported decisions, not a reconstructed chat outline.
'''
 (i/'PROJECT_STATE.md').write_text(istate);(i/'README.md').write_text('''# Inner Child — editorial review package

Start with **Structure-and-Decisions-r03.html**. It shows the restored source and candidate arrangements, section purposes, dependencies, both editing sites, exact local word changes and two larger scope choices. Notes and decisions are shared per relation, saved locally and exportable as JSON or Markdown.

**Side-by-Side-r03.html** compares the restoration-only source to the proposed structure. **Owner-to-Candidate-r03.html** includes all changes from your raw upload, including paragraph labels and restored media. **Refinement-r02-to-r03.html** isolates the fresh-reader refinements. **Full-Article-r03.html** is the complete commentable candidate. **Owner-Reading-r03.html** and **Candidate-Reading-r03.html** are readable views with stable anchors and typed media placeholders, not publication previews.

**Inner-Child-r03-candidate.html** carries exact archival source media. **Inner-Child-restored-r01.html** is the version with labels removed and formatting/media restored, before reorganization. Your two raw uploaded HTML sources are included under sources/. Do not mistake the mostly-AI donor for the current prose.

This delivery is for editorial approval, not a new 100% Human certification. Native audio and video are preserved but their actual Substack destination route remains untested; a paste-ready Inner Child helper is not claimed here. The finalized Community helper is a different file in its own package.

The canonical package manifest checks every member. Root aliases of articles/reviews are identical copies provided for the structure page's navigation. No generated article is published by opening or reviewing these files.
''')
 change='''# Inner Child — what changed

## Restoration before editing

Removed only paragraph labels, not numbered practices. Restored the supplied audio/song introductions, eight missing native objects at their semantic anchors and seven existing-source links. Kept newer current-owner charts instead of replacing them with old donor images. No AI explanatory prose was imported. The exact inverse-operation check recovers all label-free owner HTML.

## Developmental changes

- Readiness no longer contains the long social/communication detour; adult representation and protective intent remain before deeper practice.
- Borrowing now includes late no-warmth difficulty, future/past competence and motivation alternatives at the point they are needed.
- Hook recognition and the simple practice chapter come forward. General method evaluation has its home in the strategy section rather than the checking example.
- The external-authority warning and its later manipulation examples are together. Guide timing remains individually qualified.
- Happiness horizon, gratitude, spiritual betrayal and felt-depth/access difficulties are gathered into a dedicated chapter.
- Social contact, paced disclosure, other people's relational capacity, response/repair and peer counseling form one application chapter.
- Altered states, pain and crisis are findable chapters rather than extensions of fake-voice troubleshooting. The source's immediate human-help paragraphs open the crisis discussion.
- Therapist selection comes before the final encouragement; clinical comparisons remain in the appendix.

No source paragraph was deleted. One heading was retired after its material moved; four redundant or orphaned scaffolding spans were trimmed. Four earlier minimal syntax/reference repairs and one navigational heading are logged. This is substantial resequencing and consolidation, not a claim of drastic word reduction or a finished answer to every possible scope choice.

Complete exact records: RESTORATION-RECEIPT.json, LOCAL-CHANGES.json, REFINEMENT-OPS.json and FINAL-ASSEMBLY.json. Reader scope and reconciliations are recorded separately from mechanical integrity checks.
'''
 (i/'CHANGELOG.md').write_text(change)
 # Render concise launch pages without altering the reviewed article/UI bytes.
 for o,title,start in [(c,'Community r04 — approved','Copy-to-Substack-r04.html'),(i,'Inner Child r03 — review candidate','Structure-and-Decisions-r03.html')]:
  (o/'START-HERE.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>body{max-width:800px;margin:40px auto;padding:0 20px;font:18px/1.6 system-ui}a{color:#176576}pre{white-space:pre-wrap;font:inherit}</style><h1>'+title+'</h1><p><a href="'+start+'">Open the main file</a></p><pre>'+html.escape((o/'README.md').read_text())+'</pre></html>')
 # Build canonical packages; root aliases preserve the structure UI's tested relative links.
 def package(o,article,reviews,name):
  for n in reviews:
   report=json.loads((o/(n.replace('.html','-browser.json'))).read_text());assert report.get('result',report.get('status')) in ['pass','PASS'],(n,report.get('result',report.get('status')))
  cmd=['python3',str(runtime/'review_package.py'),'build','--article',str(o/article)]
  for n in reviews:cmd+=['--review',str(o/n)]
  cmd+=['--source-comments',str(o/'source-comments.json'),'--project-state',str(o/'PROJECT_STATE.md'),'--changelog',str(o/'CHANGELOG.md'),'--readme',str(o/'README.md')]
  for f in sorted(o.iterdir()):
   if not f.is_file() or f.suffix not in ['.html','.md','.json','.txt']:continue
   if f.name in ['PACKAGE-RESULT.json','PACKAGE-VERIFY.json']:continue
   cmd+=['--extra',str(f)+'='+f.name]
  if o==i:
   for f in task.joinpath('inputs').glob('Inner-Child-*.html'):cmd+=['--extra',str(f)+'=sources/'+f.name]
  cmd+=['--out',str(pub/name)];result=subprocess.run(cmd,text=True,capture_output=True,check=True);(o/'PACKAGE-RESULT.json').write_text(result.stdout);verify=subprocess.run(['python3',str(runtime/'review_package.py'),'verify',str(pub/name)],text=True,capture_output=True,check=True);(o/'PACKAGE-VERIFY.json').write_text(verify.stdout);print(result.stdout.strip())
 package(c,'Community-Article-r04-approved.html',['Changes-r03-to-r04.html','Original-to-r04.html','Full-Article-r04.html'],'Community-r04-Approved.zip')
 package(i,'Inner-Child-r03-candidate.html',['Side-by-Side-r03.html','Owner-to-Candidate-r03.html','Refinement-r02-to-r03.html','Full-Article-r03.html'],'Inner-Child-r03-Editorial-Review.zip')
 (pub/'UDA-RECOVERY-REPORT.md').write_bytes((task/'UDA-RECOVERY-REPORT.md').read_bytes())
 manifest={'format':'joel-community-innerchild-delivery-v1','community_article_sha256':sha(c/'Community-Article-r04-approved.html'),'innerchild_candidate_sha256':sha(i/'Inner-Child-r03-candidate.html'),'files':{p.name:sha(p) for p in pub.iterdir() if p.is_file() and p.name!='DELIVERY-MANIFEST.json'}};(pub/'DELIVERY-MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print('Delivery output',pub,'exact package hashes',manifest['files'])
if __name__=='__main__':main(sys.argv[1])
