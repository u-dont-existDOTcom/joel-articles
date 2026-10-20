from pathlib import Path
import json,base64,hashlib,shutil
import re
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;D=Path('/home/joel/.cache/article-completion-20261020/repo/articles/intentional-communities/candidate/owner-approved-20261020');f=D/'Copy-to-Substack-r04.html';M=json.loads(re.search(r'<script[^>]*id=[\"\']hva-transfer-manifest[\"\'][^>]*>(.*?)</script>',f.read_text(),re.S).group(1));expected=base64.b64decode(M['segments'][0]['html_b64']).decode();plain=base64.b64decode(M['segments'][0]['plain_b64']).decode();checks=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path=shutil.which('brave-browser'),headless=True)
 for mode in ['modern','fallback']:
  c=browser.new_context();page=c.new_page();page.route('http://**',lambda r:r.abort());page.route('https://**',lambda r:r.abort())
  modern="""window.sink=[];class CI{constructor(types){this.types=types;}};Object.defineProperty(window,'ClipboardItem',{value:CI,configurable:true});Object.defineProperty(navigator,'clipboard',{value:{write(items){window.sink=items;window.calledDuringClick=window.inTrustedClick;return Promise.resolve();}},configurable:true});document.addEventListener('click',()=>{window.inTrustedClick=true;setTimeout(()=>window.inTrustedClick=false,0)},true);"""
  fallback="""window.legacyHTML=null;Object.defineProperty(window,'ClipboardItem',{value:undefined,configurable:true});document.execCommand=command=>{if(command!=='copy')return false;const sel=getSelection();const r=sel.getRangeAt(0);let p=r.commonAncestorContainer;p=p.nodeType===1?p:p.parentElement;window.legacyHTML=p.innerHTML;window.legacyDuringClick=window.inTrustedClick;return true;};document.addEventListener('click',()=>{window.inTrustedClick=true;setTimeout(()=>window.inTrustedClick=false,0)},true);"""
  page.add_init_script(modern if mode=='modern' else fallback);page.goto(f.as_uri());page.get_by_role('button',name='Copy Article',exact=True).click();page.wait_for_function("document.getElementById('status-0').textContent==='Copied'")
  if mode=='modern':
   got=page.evaluate("async()=>({html:await sink[0].types['text/html'].text(),plain:await sink[0].types['text/plain'].text(),immediate:calledDuringClick})");ok=got['html']==expected and got['plain']==plain and got['immediate']
  else:
   got=page.evaluate('({html:legacyHTML,immediate:legacyDuringClick,leftover:document.querySelectorAll("div[aria-hidden=true][contenteditable=true]").length})');normalized=page.evaluate('(s)=>{const d=document.createElement("div");d.innerHTML=s;return d.innerHTML}',expected);ok=got['html']==normalized and got['immediate'] and got['leftover']==0
  assert ok,(mode,got.keys());checks.append({'check':mode+' exact payload and synchronous gesture path','passed':True});c.close()
 browser.close()
R={'format':'joel-clipboard-sink-check-v1','status':'PASS','helper_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'candidate_sha256':M['source_sha256'],'payload_sha256':hashlib.sha256(expected.encode()).hexdigest(),'checks':checks,'scope':'Exact local HTML in headless Brave. Deterministic injected ClipboardItem/execCommand sinks, not actual OS clipboard permission or Opera-to-Substack reconstruction.'};(D/'CLIPBOARD-SINK-CHECK.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(R,indent=2))
