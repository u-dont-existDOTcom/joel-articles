from pathlib import Path
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import hashlib,json,re,copy
VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class Top(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=False);self.s=s;self.offsets=[0];self.offsets.extend(m.end() for m in re.finditer('\n',s));self.stack=[];self.spans=[];self.opening='';self.start=None
 def pos(self):
  l,c=self.getpos();return self.offsets[l-1]+c
 def handle_starttag(self,t,a):
  pos=self.pos()
  if not self.stack:
   self.opening=self.get_starttag_text();self.stack.append(t);return
  if len(self.stack)==1:self.start=pos
  if t in VOID:
   if len(self.stack)==1:self.spans.append((self.start,pos+len(self.get_starttag_text())));self.start=None
  else:self.stack.append(t)
 def handle_startendtag(self,t,a):
  pos=self.pos()
  if len(self.stack)==1:self.spans.append((pos,pos+len(self.get_starttag_text())))
 def handle_endtag(self,t):
  if not self.stack:return
  if t!=self.stack[-1]:raise ValueError((t,self.stack[-4:]))
  self.stack.pop()
  if len(self.stack)==1:
   self.spans.append((self.start,self.s.index('>',self.pos())+1));self.start=None

def parse(s):
 p=Top(s);p.feed(s);rows=[]
 for n,(a,b) in enumerate(p.spans):
  raw=s[a:b];tag=BeautifulSoup(raw,'html.parser').find();rows.append({'id':f'T{n:03}','index':n,'start':a,'end':b,'tag':tag.name,'text':tag.get_text(' ',strip=True),'raw':raw,'classes':tag.get('class',[])})
 assert p.opening+''.join(x['raw'] for x in rows)+'</div>'==s
 return p.opening,rows
