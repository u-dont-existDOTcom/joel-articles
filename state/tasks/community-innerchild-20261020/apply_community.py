from pathlib import Path
import argparse, re, json, hashlib, html
from collections import Counter
from bs4 import BeautifulSoup
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('answers');p.add_argument('out');args=p.parse_args()
src=Path(args.source).read_text();answer_path=Path(args.answers);answers=json.loads(answer_path.read_text());a=answers['answers'];out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
assert sha(src)=='e0f5e871fcc9f4f869a0465c3728be42adc77f5f704a058c8e867597de72e6a0'
assert a['overall']=='Approve this article candidate' and 'revisions as specified' in a['overall-note']
changes=[]
def replace_one(text,old,new,ids,reason):
 assert text.count(old)==1,(ids,text.count(old))
 changes.append({'owner_ids':ids,'reason':reason,'before_html':old,'after_html':new,'before_sha256':sha(old),'after_sha256':sha(new)})
 return text.replace(old,new,1)
# The author's quoted replacement controls this entire old survey, not a generic summary.
intro=a['Q1.note'].split('\n"',1)[1].rsplit('"',1)[0]
intro=intro.replace('They’ve gone/are going','They’ve gone, or are going,')
old=re.search(r'<h2>Legality and Public Practice</h2>.*?(?=<h2>No Special Shamans</h2>)',src,re.S).group()
s=replace_one(src,old,'',['Q1','W26'],'Remove the old four-paragraph legal survey and its added heading; place the owner replacement at the chapter opening.')
heading='<h1>The Medicine Part - Yes, I’m Naming It</h1>'
s=replace_one(s,heading,heading+'<p>'+html.escape(intro,quote=False)+'</p>',['Q1','W26'],'Owner public-context opener first; retain the existing personal introduction directly after it. The slash drafting notation is made grammatical without choosing one tense.')
old_start='<p>Physical and psychological negative effects of ayahuasca'
replacement='For a balanced take, we need to talk about both the value and the risk. '
s=replace_one(s,old_start,'<p>'+replacement+'Physical and psychological negative effects of ayahuasca',['W10'],'Restore the reader-facing introduction under The Case Against Psychedelics using the exact owner replacement.')
old=re.search(r'<p>Before making long-term commitments,.*?</p>',s,re.S).group()
new=a['W27.note'].split('change it to: "',1)[1].rsplit('"',1)[0]
new=new.replace('makes sense to through','makes sense to go through').replace('” sections after that','” section after that')
s=replace_one(s,old,'<p>'+html.escape(new,quote=False)+'</p>',['W27'],'Install the owner’s pointer; fix only the missing go and singular section agreement.')
# No whole-document serialization: unedited markup, including fragile objects, remains exact.
spans=lambda t:re.findall(r'<p\b[^>]*>.*?</p>|<h[1-6]\b[^>]*>.*?</h[1-6]>',t,re.S)
def links(t):return Counter((x.get('href') or '') for x in BeautifulSoup(t,'html.parser').find_all('a'))
lost=links(src)-links(s);introduced=links(s)-links(src)
allowed=Counter()
for c in changes:allowed.update(links(c['before_html']))
assert not introduced
assert not (lost-allowed)
# An exact undo proves every source byte not covered by the operation ledger survived.
t=s
for c in reversed(changes):
 if c['after_html']:
  assert t.count(c['after_html'])==1
  t=t.replace(c['after_html'],c['before_html'],1)
 else:
  t=t.replace('<h2>No Special Shamans</h2>',c['before_html']+'<h2>No Special Shamans</h2>',1)
assert t==src
file=out/'Community-Article-r04-approved.html';file.write_text(s)
record={'revision':'r04-approved','authority':'Owner approved r03 with the exact supplied revisions; no publication performed.','source_sha256':sha(src),'owner_answers_sha256':hashlib.sha256(answer_path.read_bytes()).hexdigest(),'result_sha256':sha(s),'changes':changes,'minor_realization_fixes':['gone/are going → gone, or are going,','to through → to go through','named exit sections → named exit section'],'kept':'Every accepted move and basic correction; detailed dissolution inventory (Q2) unchanged.','removed_link_occurrences':dict(lost),'source_byte_undo':'PASS','detector':'No new Pangram result; the prior assistant pointer was owner-reported to fail and has been replaced.','destination':'Not pasted or published.'}
(out/'OWNER-CORRECTION-RECEIPT.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(out/'COMMENT-RESOLUTION.md').write_text('# Community r04: owner corrections applied\n\nApproved r03 with the specified revisions, not an unchanged r03 approval.\n\n'+'\n\n'.join('**'+','.join(c['owner_ids'])+'** — '+c['reason'] for c in changes)+'\n\nQ2: detailed dissolution inventory retained unchanged. All Keep decisions remain applied. Only the three small grammatical/notation repairs listed in the receipt were made to the owner’s replacement wording. Source claims are preserved as owner wording, not independently fact-checked in this editing task. No new detector or destination-paste certificate.\n')
print('COMMUNITY APPLIED',file.name,'bytes',len(s.encode()),'sha256',sha(s),'operations',len(changes),'removed links',sum(lost.values()))
