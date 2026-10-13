"""SUPERSEDED (2026-10-06 21:20 UTC): this waits for the result panel after each submit, but the dashboard no longer switches its panel to a new result, so the loop runs past the pane's 45-second limit while the page keeps submitting. Use helpers.js (__pgSubmit, then __cards / __pgRead).

gui_batch.py BATCH.json NAMES OUT.js: JavaScript for the Browser pane on Pangram's dashboard that checks each named
text in turn (set the box, press "Check for AI", wait until the result panel shows that text, read it) and returns
[{name, ok, words, block, ai_spans, before, after}] for all of them. NAMES is a comma list, or "all".
The panel test is pgcard2.py's (2026-10-03): the region between the last 'Text Query' and 'Overview' must start with
the text's first words and contain its last six, so a stale panel is never read as the new result."""
import json, sys
B = json.load(open(sys.argv[1], encoding='utf-8'))
names = list(B) if sys.argv[2] == 'all' else sys.argv[2].split(',')
items = [{'name': n, 'text': B[n].strip()} for n in names]
js = r"""const ITEMS=%s;
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const cred=()=>Number((document.body.innerText.match(/(\d+)\s*left/)||[])[1]);
const norm=s=>s.replace(/\s+/g,' ').trim();
function panel(){const t=document.body.innerText; const i=t.lastIndexOf('Text Query'); if(i<0) return null; const k=t.indexOf('Overview', i); if(k<=i) return null; return t.slice(i,k);}
const out=[];
for(const it of ITEMS){
 const w=it.text.split(/\s+/); const HEAD=w.slice(0,4).join(' '), TAIL=w.slice(-6).join(' ');
 const before=cred();
 let ta=document.querySelector('textarea');
 Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype,'value').set.call(ta,it.text);
 ta.dispatchEvent(new Event('input',{bubbles:true}));
 await sleep(700);
 if(document.querySelector('textarea').value!==it.text){out.push({name:it.name,error:'box mismatch'});continue;}
 const btn=[...document.querySelectorAll('button')].filter(b=>/Check for AI/.test(b.innerText)&&!b.disabled&&b.offsetParent)[0];
 if(!btn){out.push({name:it.name,error:'no button'});continue;}
 btn.click();
 let ok=false;
 for(let i=0;i<30;i++){await sleep(1200); const p=panel(); if(p){const hdr=norm(p.split('\n')[1]||''); if(norm(p).includes(norm(TAIL)) && hdr.length>0 && (HEAD.startsWith(hdr)||hdr.startsWith(HEAD))){ok=true;break;}}}
 await sleep(900);
 const t=document.body.innerText; const j=t.lastIndexOf('words scanned');
 const spans=[...document.querySelectorAll('span')].filter(el=>getComputedStyle(el).backgroundColor==='rgba(255, 86, 48, 0.1)').map(el=>el.textContent);
 out.push({name:it.name, ok, words:w.length, block:norm(t.slice(Math.max(0,j-60),j+120)), ai_spans:spans, before, after:cred()});
}
out""" % json.dumps(items, ensure_ascii=False)
open(sys.argv[3], 'w', encoding='utf-8').write(js)
print(len(js), names)
