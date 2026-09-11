#!/usr/bin/env python3
"""Test an unchanged canonical helper with injected clipboard sinks, not the OS clipboard.

No helper generation, no destination mutation, no claim of Opera/Substack acceptance.
"""
import argparse,base64,hashlib,json,re,shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('helper',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 raw=a.helper.read_text();m=json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>',raw,re.S).group(1).replace('<\\/','</'))
 expected=[base64.b64decode(x['html_b64']).decode() for x in m['segments']]
 results=[]
 with sync_playwright() as pw:
  browser=pw.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('chromium-browser') or shutil.which('google-chrome'),args=['--no-sandbox'])
  for fallback in (False,True):
   page=browser.new_page();page.route('**/*',lambda route:route.abort());errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.evaluate('''() => {
     window.copied=[];
     window.ClipboardItem=class {constructor(data){this.data=data;}};
     Object.defineProperty(navigator,'clipboard',{configurable:true,value:{write:async items=>{
       window.copied.push(await items[0].data['text/html'].text());
     }}});
   }''')
   page.set_content(raw,wait_until='domcontentloaded')
   if fallback:
    page.evaluate('''() => {window.ClipboardItem=undefined;document.execCommand=cmd=>{
      if(cmd!=='copy')return false;let h=document.createElement('div');
      h.appendChild(getSelection().getRangeAt(0).cloneContents());window.copied.push(h.innerHTML);return true;
    };}''')
   for i,exp in enumerate(expected):
    page.locator(f'button[data-segment-index="{i}"]').click();page.wait_for_function(f"document.getElementById('status-{i}').textContent==='Copied'")
    actual=page.evaluate('window.copied')[-1]
    normalized=page.evaluate('(x)=>{let h=document.createElement("div");h.innerHTML=x;return h.innerHTML;}',exp) if fallback else exp
    assert actual==normalized,(fallback,i)
   assert not errors,errors
   results.append({'path':'execCommand selected-rich-DOM sink' if fallback else 'ClipboardItem Blob sink','segments':len(expected),'status':'pass'})
   page.close()
  browser.close()
 report={'format':'clipboard-interaction-test-v1','helper_sha256':hashlib.sha256(raw.encode()).hexdigest(),'source_sha256':m['source_sha256'],'canonical_helper_format':m['format'],'tests':results,'status':'pass','navigation':'exact HTML set_content in headless Chromium; no local-file/Opera claim','clipboard':'injected sinks, not operating-system clipboard','destination':'not tested; no Substack mutation','native_reconstruction':'requires actual destination inspection'}
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
