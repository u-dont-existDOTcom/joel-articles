from pathlib import Path
import json,html,difflib,re
from bs4 import BeautifulSoup
W=Path(__file__).resolve().parent;D=W/'delivery';L=json.loads((D/'ASSEMBLY-LEDGER.json').read_text());M=json.loads((D/'STRUCTURE-MAP.json').read_text());old=json.loads((D/'source-blocks.json').read_text());new=L['blocks'];O={b['id']:b for b in old};N={b['id']:b for b in new};OI=[b['id'] for b in old];NI=L['new_order'];esc=html.escape

def diff(a,b):
 x=re.findall(r'\S+\s*|\s+',a);y=re.findall(r'\S+\s*|\s+',b);outa=[];outb=[]
 for k,i,j,u,v in difflib.SequenceMatcher(None,x,y,autojunk=False).get_opcodes():
  aa=esc(''.join(x[i:j]));bb=esc(''.join(y[u:v]));outa.append(aa if k=='equal' else '<del>'+aa+'</del>' if aa else '');outb.append(bb if k=='equal' else '<ins>'+bb+'</ins>' if bb else '')
 return ''.join(outa),''.join(outb)
def txt(raw):return BeautifulSoup(raw,'html.parser').get_text(' ',strip=True)
def near(rows,index,direction):
 for j in range(index+direction,-1 if direction<0 else len(rows),direction):
  b=rows[j]
  if b['tag'] in ['p','h1','h2','h3','ol','ul','blockquote'] and b['text']:return b['id'],b['text']
 return None,'Document boundary'
# One paired card per actual wording edit, independent of sequence-match heuristics for moved blocks.
wordcards=[]
for e in L['edits']:
 if e['kind']=='heading_level':continue
 a,b=txt(e['before_html']),txt(e['after_html']);da,db=diff(a,b);id=e['block'];wid=e['id'];ctxa=near(old,OI.index(id),-1)[1] if id in O else 'New text; no source passage';ctxb=near(new,NI.index(id),-1)[1]
 wordcards.append(f'<article class="panel lexical-card" id="lex-{wid}"><div class="eyebrow">{wid} · {esc(id)} · {esc(e["kind"])}</div><p>{esc(e["reason"])}</p><div class="comparison"><div><h3>Exact source wording</h3><div class="excerpt">{da or "[no source wording]"}</div></div><div><h3>Exact candidate wording</h3><div class="excerpt">{db or "[removed]"}</div></div></div><details><summary>Old and new preceding context</summary><div class="comparison"><div class="excerpt">{esc(ctxa)}</div><div class="excerpt">{esc(ctxb)}</div></div></details><p><a href="Owner-Reading-r03.html#source-{id}">Full source location</a> · <a href="Candidate-Reading-r03.html#candidate-{id}">Full revised location</a></p><label class="form">Decision<select data-answer="{wid}.decision"><option value="">Not reviewed</option><option>Keep</option><option>Revise</option><option>Discuss</option></select></label><textarea data-answer="{wid}.note" aria-label="Comment on {wid}" placeholder="Comment on this exact wording change"></textarea></article>')
M['word_change_ids']=[e['id'] for e in L['edits'] if e['kind']!='heading_level']
# Sanitized, full-length paragraph-faithful reading copies with stable deep links; native content is never fabricated.
for label,rows in [('Owner',old),('Candidate',new)]:
 mode='source' if label=='Owner' else 'candidate';body=[]
 for b in rows:
  id=b['id'];soup=BeautifulSoup(b['raw'],'html.parser');root=soup.find();tag=b['tag'];classes=set(b.get('classes',[]))
  if classes&{'captioned-image-container','digest-post-embed','youtube-wrap','button-wrapper'}:
   cap=soup.find('figcaption');text=cap.get_text(' ',strip=True) if cap else ('Embedded post or video retained in archival source' if classes&{'digest-post-embed','youtube-wrap'} else 'Native image or publication control retained in archival source');body.append(f'<aside id="{mode}-{id}" class="native">{esc(text)}</aside>');continue
  if root:
   for x in soup.find_all(True):
    allowed={k:v for k,v in x.attrs.items() if k in ['href','target','rel']};x.attrs=allowed
   root['id']=f'{mode}-{id}';body.append(str(soup))
 style='body{max-width:840px;margin:30px auto;padding:0 22px;font:18px/1.75 Georgia,serif;color:#18343f;background:#fffdf8}p{margin:0 0 1.1em}h1{margin-top:2em;line-height:1.25;font-size:30px}h2{font-size:24px}h3{font-size:20px}a{color:#176576}.native{padding:13px;background:#eef2f2;margin:20px 0;font:14px/1.5 system-ui}nav{font:14px system-ui;position:sticky;top:0;padding:14px;background:#eff4f4} [id]{scroll-margin-top:65px}'
 (D/f'{label}-Reading-r03.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+label+' article · source-faithful reading view</title><style>'+style+'</style><nav><a href="Structure-and-Decisions-r03.html">Structure and decisions</a> · <a href="Side-by-Side-r03.html">Canonical commentable diff</a></nav><body>'+''.join(body)+'</body></html>')
# Two local sites per move group, with original/revised context and visible heading removal/insertion.
for m in M['moves']:
 sites=[]
 for id in m['nodes']:
  if id not in O or id not in N:continue
  oi,ni=OI.index(id),NI.index(id);prevold=near(old,oi,-1)[1];prevnew=near(new,ni,-1)[1];origtitle=O[id]['text'];newtitle=N[id]['text'];a,b=diff(origtitle,newtitle)
  sites.append(f'<div class="comparison two-sites"><section><h3>Old location · {esc(id)}</h3><div class="excerpt">{esc(prevold)}<br><del>{esc(origtitle)}</del><p class="small">This section is no longer developed here; its preserved content is at the destination.</p></div><a href="Owner-Reading-r03.html#source-{id}">Old full context</a></section><section><h3>New location · {esc(id)}</h3><div class="excerpt">{esc(prevnew)}<br><ins>{esc(newtitle)}</ins><p class="small">Inserted here. Any wording changes are paired below and in the exact diff.</p></div><a href="Candidate-Reading-r03.html#candidate-{id}">New full context</a></section></div>')
  # Relocation also needs the exact in-section edits, not just a label.
  groupnodes=next((x['block_ids'] for x in M['nodes'] if x['id']==id),[]);w=[e['id'] for e in L['edits'] if e['block'] in groupnodes and e['kind']!='heading_level'];
  if w:sites.append('<p>Exact changes inside this section: '+', '.join(f'<a href="#lex-{wid}">{wid}</a>' for wid in w)+'</p>')
 m['local_sites_html']=''.join(sites)
(D/'STRUCTURE-MAP.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
p=D/'map_template.html';s=p.read_text()
s=s.replace('<a href="Full-Article-r03.html">Full commentable article</a>','<a href="Full-Article-r03.html">Full commentable article</a><a href="Owner-Reading-r03.html">Read full source</a><a href="Candidate-Reading-r03.html">Read full revision</a>')
s=s.replace('<section id="questions">','<section id="lexical"><h2>Exact local wording changes</h2><p>Source and candidate text are paired even when the paragraph moved. Removed words are struck through; additions are highlighted. Each card opens both full article locations.</p>'+''.join(wordcards)+'</section><section id="questions">')
s=s.replace("${form(m.id,['Keep','Revise','Discuss'])}","<details><summary>Both editing sites and exact context</summary>${m.local_sites_html||''}</details>${form(m.id,['Keep','Revise','Discuss'])}")
s=s.replace("let state={};try", "let state={};try")
s=s.replace("function save(){try", "function remember(k,value){const prev=state[k]??'';if(prev!==value){state._history=state._history||[];state._history.push({field:k,before:prev,after:value,at:new Date().toISOString()});}state[k]=value;save()}\nfunction save(){try")
s=s.replace("state[el.dataset.answer]=el.value;save()","remember(el.dataset.answer,el.value)").replace("state[id]=$(id).value;save()","remember(id,$(id).value)")
s=s.replace("answers:state};const blob", "relations:D.moves.map(m=>({id:m.id,classification:'Moved or reorganized',source_ids:m.nodes.filter(id=>D.old_nodes.some(n=>n.id===id)),destination_ids:m.nodes})),answers:state};const blob")
# Add Markdown alongside JSON. Existing canonical review controls remain unchanged.
s=s.replace('<button id="export" class="export">Export review answers</button>','<button id="export" class="export">Export review answers</button><button id="export-md" class="export">Export Markdown</button>')
s=s.replace("$('export').onclick=exportAnswers;", "$('export-md').onclick=()=>{let text='# Community r03 review\\n\\nCandidate: '+D.candidate_sha256+'\\n\\n';for(const [k,v]of Object.entries(state)){if(k!=='_history')text+='## '+k+'\\n'+String(v)+'\\n\\n';}text+='## Decision history\\n```json\\n'+JSON.stringify(state._history||[],null,2)+'\\n```\\n';const u=URL.createObjectURL(new Blob([text],{type:'text/markdown'}));const a=document.createElement('a');a.href=u;a.download='Community-r03-review.md';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)};$('export').onclick=exportAnswers;")
p.write_text(s);(D/'Structure-and-Decisions-r03.html').write_text(s.replace('__DATA__',json.dumps(M,ensure_ascii=False).replace('</','<\\/')))
print('Move review includes',len(wordcards),'paired lexical cards, both-site context links, full source/revision reading modes, relation history and Markdown export.')
