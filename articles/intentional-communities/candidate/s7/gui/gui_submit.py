"""gui_submit.py BATCH.json NAMES OUT.js: JavaScript that submits each named text on Pangram's dashboard (set the box,
press "Check for AI", wait 4 s for its card) and returns at once with what it submitted. Results are read later with
gui_read.py: the dashboard keeps showing the old result panel after a submit (2026-10-03), so a submit never reads."""
import json, sys
B = json.load(open(sys.argv[1], encoding='utf-8'))
names = sys.argv[2].split(',')
items = [{'name': n, 'text': B[n].strip()} for n in names]
js = r"""const ITEMS=%s;
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const cred=()=>Number((document.body.innerText.match(/(\d+)\s*left/)||[])[1]);
const out=[];
for(const it of ITEMS){
 const before=cred();
 const ta=document.querySelector('textarea');
 Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype,'value').set.call(ta,it.text);
 ta.dispatchEvent(new Event('input',{bubbles:true}));
 await sleep(600);
 if(document.querySelector('textarea').value!==it.text){out.push({name:it.name,error:'box mismatch'});continue;}
 const btn=[...document.querySelectorAll('button')].filter(b=>/Check for AI/.test(b.innerText)&&!b.disabled&&b.offsetParent)[0];
 if(!btn){out.push({name:it.name,error:'no button (under 50 words?)'});continue;}
 btn.click(); await sleep(4000);
 out.push({name:it.name, words:it.text.split(/\s+/).length, before, after:cred()});
}
out""" % json.dumps(items, ensure_ascii=False)
open(sys.argv[3], 'w', encoding='utf-8').write(js)
print(len(js), names)
