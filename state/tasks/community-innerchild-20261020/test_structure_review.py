from pathlib import Path
import json,re,hashlib,tempfile
from urllib.parse import urlsplit,unquote
from playwright.sync_api import sync_playwright
r=Path(__file__).resolve().parents[3];o=r/'articles/inner-child-therapy/candidate/editorial-20261020';pagefile=o/'Structure-and-Decisions-r03.html';checks=[]
def check(name,condition):
 checks.append({'check':name,'passed':bool(condition)});assert condition,name
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/brave-browser');ctx=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True);page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.route('http://**',lambda route:route.abort());page.route('https://**',lambda route:route.abort());page.goto(pagefile.as_uri(),wait_until='load')
 check('local-file navigation',page.url.startswith('file:'))
 check('both heading arrangements rendered',page.locator('#old-track button').count()>10 and page.locator('#new-track button').count()>10)
 page.locator('#new-H364').click();check('matching source and candidate selection',page.locator('#new-H364').get_attribute('aria-pressed')=='true' and page.locator('#old-H364').get_attribute('aria-pressed')=='true')
 check('purpose and dependency displayed','gratitude' in page.locator('#detail').inner_text().lower())
 page.locator('#subsections').check();check('complete heading tree',page.locator('#new-track button').count()==77)
 page.locator('#old-H355').click();check('retired heading explained','retired' in page.locator('#detail').inner_text())
 page.locator('#search').fill('motivation');check('purpose search',0<page.locator('#new-track button').count()<77);page.locator('#search').fill('')
 page.locator('#decision-M02').select_option('Revise');page.locator('textarea[data-answer="M02.note"]').fill('AUTOMATED TEST: retain source detail.')
 page.locator('#overall').select_option('Approve with revisions as specified');page.locator('#overall-note').fill('AUTOMATED TEST ONLY, NOT OWNER APPROVAL.')
 with page.expect_download() as info:page.locator('#export').click()
 with tempfile.TemporaryDirectory() as tmp:
  dest=Path(tmp)/'notes.json';info.value.save_as(dest);data=json.loads(dest.read_text())
 check('bound answer export',data['candidate_sha256']=='91b9065b9a121a40fb54cad2eac1d8be99eb5a24869178c04c26786a163708a4' and data['answers']['M02.note']=='AUTOMATED TEST: retain source detail.')
 check('relation identity and history',len(data['relations'])==8 and len(data['answers']['_history'])>=3)
 with page.expect_download() as info:page.locator('#export-md').click()
 with tempfile.TemporaryDirectory() as tmp:
  dest=Path(tmp)/'notes.md';info.value.save_as(dest);text=dest.read_text()
 check('Markdown export','AUTOMATED TEST: retain source detail.' in text)
 page.reload(wait_until='load');check('local persistence',page.locator('textarea[data-answer="M02.note"]').input_value()=='AUTOMATED TEST: retain source detail.')
 page.evaluate('localStorage.clear()');page.reload(wait_until='load');check('test answers removed',not page.locator('textarea[data-answer="M02.note"]').input_value())
 check('eleven paired lexical cards',page.locator('.lexical-card').count()==11)
 check('move cards have two local contexts',page.locator('#move-M02 .two-sites').count()>=2)
 # Verify every packaged local path and fragment, including dynamically rendered relation contexts.
 links=page.locator('a[href]').evaluate_all('(els)=>els.map(x=>x.getAttribute("href"))');missing=[]
 for href in links:
  u=urlsplit(href)
  if u.scheme or href.startswith('mailto:'):continue
  file=(o/unquote(u.path)) if u.path else pagefile
  if not file.is_file():missing.append(href);continue
  if u.fragment:
   if file==pagefile:exists=page.locator('[id="'+u.fragment.replace('"','\\"')+'"]').count()>0
   else:exists=bool(re.search(r'id=[\"\']'+re.escape(unquote(u.fragment))+r'[\"\']',file.read_text()))
   if not exists:missing.append(href)
 check('all local links and anchors resolve',not missing)
 page.set_viewport_size({'width':390,'height':844});check('mobile no horizontal overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'))
 check('no JavaScript exceptions',not errors);browser.close()
result={'status':'PASS','scope':'Exact local-file UI, local navigation, comments/history/exports; not article judgment or publishing playback','file_sha256':hashlib.sha256(pagefile.read_bytes()).hexdigest(),'checks':checks};(o/'STRUCTURE-BROWSER-CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
