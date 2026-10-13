"""gui_read.py BATCH.json NAMES OUT.js: JavaScript that, for each named (already submitted) text, presses only that text's
card's "View Results", waits until the result panel shows that text (pgcard2.py's test: the panel header starts with the
text's first words and the panel holds its last six), and reads the verdict block and the AI-highlighted spans.
Submits nothing. Keep NAMES to about five per call (the pane's 45 s limit)."""
import json, sys
B = json.load(open(sys.argv[1], encoding='utf-8'))
names = sys.argv[2].split(',')
items = [{'name': n, 'text': B[n].strip()} for n in names]
js = r"""const ITEMS=%s;
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const norm=s=>s.replace(/\s+/g,' ').trim();
function panel(){const t=document.body.innerText; const i=t.lastIndexOf('Text Query'); if(i<0) return null; const k=t.indexOf('Overview', i); if(k<=i) return null; return t.slice(i,k);}
const out=[];
for(const it of ITEMS){
 const w=it.text.split(/\s+/); const HEAD=w.slice(0,4).join(' '), TAIL=w.slice(-6).join(' '), START=norm(it.text).slice(0,150);
 const shown=()=>{const p=panel(); if(!p) return false; const hdr=norm(p.split('\n')[1]||''); return norm(p).includes(norm(TAIL)) && hdr.length>0 && (HEAD.startsWith(hdr)||hdr.startsWith(HEAD));};
 let clicked=false;
 if(!shown()){
  const btns=[...document.querySelectorAll('button,a')].filter(b=>/View Results/.test(b.innerText)&&b.offsetParent);
  for(const b of btns){let c=b; while(c.parentElement && [...c.parentElement.querySelectorAll('button,a')].filter(x=>/View Results/.test(x.innerText)).length===1) c=c.parentElement;
   if(norm(c.innerText).startsWith(START.slice(0,140))){b.click(); clicked=true; break;}}
 }
 let ok=false; for(let i=0;i<12;i++){ if(shown()){ok=true;break;} await sleep(700); }
 await sleep(600);
 const t=document.body.innerText; const j=t.lastIndexOf('words scanned');
 const spans=[...document.querySelectorAll('span')].filter(el=>getComputedStyle(el).backgroundColor==='rgba(255, 86, 48, 0.1)').map(el=>el.textContent);
 out.push({name:it.name, ok, clicked, block:norm(t.slice(Math.max(0,j-40),j+110)), ai_spans:spans});
}
out""" % json.dumps(items, ensure_ascii=False)
open(sys.argv[3], 'w', encoding='utf-8').write(js)
print(len(js), names)
