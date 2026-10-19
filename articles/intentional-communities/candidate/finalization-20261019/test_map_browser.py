from pathlib import Path
from playwright.sync_api import sync_playwright
import json,hashlib,tempfile,shutil
B=Path(__file__).resolve().parent;f=B/'Structure-and-Decisions-r03.html';checks=[]
def ck(n,v):checks.append({'check':n,'passed':bool(v)});assert v,n
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path=shutil.which('brave-browser') or shutil.which('chromium'),headless=True,args=['--no-sandbox']);context=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True);page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.route('http://**',lambda r:r.abort());page.route('https://**',lambda r:r.abort())
 try:page.goto(f.as_uri());mode='file'
 except Exception:
  mode='set_content';shim="<script>window.testStore={};Object.defineProperty(window,'localStorage',{value:{getItem:k=>testStore[k]||null,setItem:(k,v)=>testStore[k]=v,clear:()=>window.testStore={}},configurable:true})</script>";page.set_content(f.read_text().replace('<script id="map-data"',shim+'<script id="map-data"'))
 ck('original and revised overview',page.locator('#old-track .node').count()==17 and page.locator('#new-track .node').count()==17)
 page.locator('#old-T267').click();ck('same medicine node selected in both views',page.locator('button.selected').count()==2);ck('selected move has visible connector',page.locator('#connectors path').count()==1);ck('node explains purpose and move', 'What distinguishes' in page.locator('#detail').inner_text() and 'M01' in page.locator('#detail').inner_text())
 page.locator('#subsections').check();ck('all current mapped headings shown',page.locator('#new-track .node').count()==64);page.locator('#new-T184').click();ck('membership shown under practice', 'Practicing Community' in page.locator('#detail .where').inner_text())
 page.locator('#search').fill('free resource');ck('concept search uses purpose',page.locator('#new-track .node').count()<64);page.locator('#search').fill('')
 page.locator('#decision-M03').select_option(label='Keep');page.locator('[data-answer="M03.note"]').fill('AUTOMATED TEST: shared move decision')
 page.locator('#decision-Q1').select_option(index=1);page.locator('#overall-note').fill('AUTOMATED TEST: not owner approval')
 with page.expect_download() as ev:page.locator('#export-bottom').click()
 with tempfile.TemporaryDirectory() as d:
  target=Path(d)/'a.json';ev.value.save_as(target);data=json.loads(target.read_text())
 ck('export carries candidate and relation note', data['candidate_sha256']==json.loads((B/'ASSEMBLY-LEDGER.json').read_text())['candidate_sha256'] and data['answers']['M03.note']=='AUTOMATED TEST: shared move decision')
 if mode=='file':
  page.reload();ck('browser persistence',page.locator('[data-answer="M03.note"]').input_value()=='AUTOMATED TEST: shared move decision');page.evaluate('localStorage.clear()');page.reload();ck('test review cleared',page.locator('[data-answer="M03.note"]').input_value()=='')
 else:
  ck('in-page storage calls',page.evaluate('Object.values(window.testStore).some(x=>x.includes("AUTOMATED TEST"))'));page.evaluate('localStorage.clear()')
 page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(B/'map-desktop-check.png'))
 page.set_viewport_size({'width':390,'height':844});ck('mobile no horizontal overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'));page.screenshot(path=str(B/'map-mobile-check.png'));ck('no JavaScript exceptions',not errors);browser.close()
result={'format':'joel-structure-map-browser-check-v1','status':'PASS','file_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'checks':checks,'navigation_mode':mode,'scope':'UI/interaction only; set_content mode does not prove file navigation or real persistence. No Substack destination or editorial judgment.'};(B/'MAP-BROWSER-CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
