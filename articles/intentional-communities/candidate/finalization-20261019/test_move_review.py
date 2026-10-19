from pathlib import Path
import json,hashlib,tempfile,shutil
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;D=W/'delivery';f=D/'Structure-and-Decisions-r03.html';checks=[]
def ck(n,v):checks.append({'check':n,'passed':bool(v)});assert v,n
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=shutil.which('brave-browser'),headless=True);c=b.new_context(accept_downloads=True,viewport={'width':1440,'height':1000});page=c.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(f.as_uri())
 ck('paired lexical diffs',page.locator('.lexical-card').count()==15 and page.locator('.lexical-card del').count()>0 and page.locator('.lexical-card ins').count()>0)
 card=page.locator('#move-M03');card.locator('summary',has_text='Both editing sites').click();ck('two-site contexts',card.locator('.two-sites').count()==2)
 ck('source/destination links',card.locator('a[href*="Owner-Reading"]').count()==2 and card.locator('a[href*="Candidate-Reading"]').count()==2)
 page.locator('#decision-M03').select_option('Keep');page.locator('[data-answer="M03.note"]').fill('TEST one relation');page.locator('#decision-M03').select_option('Revise');page.locator('#old-T107').click();page.locator('#new-T107').click();ck('shared relation comment persists',page.locator('[data-answer="M03.note"]').input_value()=='TEST one relation')
 with page.expect_download() as ev:page.locator('#export').click()
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'a.json';ev.value.save_as(t);data=json.loads(t.read_text())
 ck('export relation endpoints and history',len(data['relations'])==6 and any(x['field']=='M03.decision' and x['after']=='Revise' for x in data['answers']['_history']))
 with page.expect_download() as ev:page.locator('#export-md').click()
 ck('Markdown export',ev.value.suggested_filename.endswith('.md'))
 page.evaluate('localStorage.clear()');page.reload();ck('test answers cleared',page.locator('[data-answer="M03.note"]').input_value()=='')
 for name,anchor in [('Owner-Reading-r03.html','source-T184'),('Candidate-Reading-r03.html','candidate-T184')]:
  page.set_viewport_size({'width':390,'height':844});page.goto((D/name).as_uri()+'#'+anchor);ck(name+' full-length paragraph view',page.locator('p').count()>250 and page.locator('#'+anchor).count()==1);ck(name+' mobile fit',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'))
 ck('no JavaScript exceptions',not errors);b.close()
(D/'MOVE-REVIEW-BROWSER-CHECK.json').write_text(json.dumps({'status':'PASS','file_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'scope':'Exact local files, move-site/lexical/decision-history/reading-view controls. Not a new prose judgment.','checks':checks},indent=2)+'\n');print('PASS',len(checks),'move-aware controls')
