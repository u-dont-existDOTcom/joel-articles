"""Finish the ODT's native table of contents without changing the article text."""
from pathlib import Path
from lxml import etree as E
import zipfile,json,sys

R=Path(__file__).resolve().parent
SRC=R/'converted/Bringing_Reparenting_Into_Real_Life.odt'
OUT=R.parent/'deliverables/Bringing_Reparenting_Into_Real_Life.odt'
N={'t':'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
   'o':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
   's':'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
   'f':'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
   'x':'http://www.w3.org/1999/xlink',
   'svg':'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
   'm':'urn:oasis:names:tc:opendocument:xmlns:manifest:1.0'}
def q(k):a,b=k.split(':');return '{'+N[a]+'}'+b
def sub(p,tag,attrs=None,text=None):
    x=E.SubElement(p,q(tag),{q(k):v for k,v in (attrs or {}).items()});x.text=text;return x
with zipfile.ZipFile(SRC) as z:files={x.filename:z.read(x.filename) for x in z.infolist()}
c=E.fromstring(files['content.xml']);styles=E.fromstring(files['styles.xml'])
idx=c.find('.//'+q('t:table-of-content'));source=idx.find(q('t:table-of-content-source'))
source.set(q('t:outline-level'),'3');source.set(q('t:use-outline-level'),'false');source.set(q('t:use-index-source-styles'),'true')
title=source.find(q('t:index-title-template'));title.text='Contents'
for node in source.findall(q('t:index-source-styles')):source.remove(node)
for level in (1,2,3):
    node=sub(source,'t:index-source-styles',{'t:outline-level':str(level)})
    sub(node,'t:index-source-style',{'t:style-name':f'Heading_20_{level+1}'})
    template=source.find(f"{q('t:table-of-content-entry-template')}[@{q('t:outline-level')}='{level}']")
    template.set(q('t:style-name'),f'Contents_20_{level}')
    for child in template.findall(q('t:index-entry-chapter')):template.remove(child)
    for child in template.findall(q('t:index-entry-tab-stop')):child.set(q('s:position'),'6.8in')

# Replace the separate imported heading and placeholder with one native index title.
prev=idx.getprevious()
if prev is not None and ''.join(prev.itertext())=='Contents':prev.getparent().remove(prev)
body=idx.find(q('t:index-body'));body.clear()
it=sub(body,'t:index-title',{'t:name':'Table of Contents1_Head'})
sub(it,'t:p',{'t:style-name':'Contents_20_Heading'},'Contents')
pages=json.loads((R/'heading-pages.json').read_text()) if (R/'heading-pages.json').exists() else {}
for h in c.findall('.//'+q('t:h')):
    level=int(h.get(q('t:outline-level')))
    if level==1:continue
    heading=''.join(h.itertext());bm=h.find(q('t:bookmark-start')).get(q('t:name'))
    p=sub(body,'t:p',{'t:style-name':f'Contents_20_{level-1}'})
    a=sub(p,'t:a',{'x:type':'simple','x:href':'#'+bm,'t:style-name':'Index_20_Link','t:visited-style-name':'Index_20_Link'},heading)
    tab=sub(a,'t:tab');tab.tail=str(pages.get(heading,2))

for level in (1,2,3):
    st=styles.find(f".//{q('s:style')}[@{q('s:name')}='Contents_20_{level}']")
    pp=st.find(q('s:paragraph-properties'));tp=st.find(q('s:text-properties'))
    pp.set(q('f:margin-left'),f'{(level-1)*.2:.1f}in');pp.set(q('f:margin-top'),'0in');pp.set(q('f:margin-bottom'),'0.0417in')
    pp.set(q('f:line-height'),'105%');pp.set(q('f:keep-with-next'),'always' if level==1 else 'auto')
    pp.set(q('f:keep-together'),'always')
    tp.set(q('f:font-weight'),'bold' if level==1 else 'normal');tp.set(q('s:font-weight-asian'),'bold' if level==1 else 'normal')
    for x in pp.findall(q('s:tab-stops')):pp.remove(x)
    tabs=sub(pp,'s:tab-stops')
    sub(tabs,'s:tab-stop',{'s:position':'6.8in','s:type':'right','s:leader-style':'dotted','s:leader-text':'.'})

# Imported character formatting must not suppress the heading styles' weight.
for h in c.findall('.//'+q('t:h')):
    for span in h.findall('.//'+q('t:span')):span.attrib.pop(q('t:style-name'),None)
linkstyle=styles.find(f".//{q('s:style')}[@{q('s:name')}='Index_20_Link']")
if linkstyle is None:
    linkstyle=sub(styles.find(q('o:styles')),'s:style',{'s:name':'Index_20_Link','s:family':'text'})
if linkstyle is not None:
    tp=linkstyle.find(q('s:text-properties'))
    if tp is None:tp=sub(linkstyle,'s:text-properties')
    tp.set(q('f:color'),'#000000');tp.set(q('s:text-underline-style'),'none')

# Use a native ODT page-number field in the existing centered footer.
for footer in styles.findall('.//'+q('s:footer')):
    ps=footer.findall(q('t:p'))
    if ps:
        p=ps[0]
        for ch in list(p):p.remove(ch)
        p.text=None
        sub(p,'t:page-number',{'t:select-page':'current'},'1')

# Embed the source emoji glyphs so they remain visible on systems without an
# installed emoji font. The upstream font is OFL licensed; retain that license.
for root in (c,styles):
    for el in root.iter():
        for key,value in list(el.attrib.items()):
            if 'Noto Color Emoji' in value:el.set(key,value.replace('Noto Color Emoji','Noto Emoji'))
    decl=root.find(q('o:font-face-decls'))
    ff=decl.find(f"{q('s:font-face')}[@{q('s:name')}='Noto Emoji']")
    if ff is None:ff=sub(decl,'s:font-face',{'s:name':'Noto Emoji','svg:font-family':"'Noto Emoji'",'s:font-pitch':'variable'})
    for child in list(ff):ff.remove(child)
    fs=sub(ff,'svg:font-face-src')
    fu=sub(fs,'svg:font-face-uri',{'x:href':'Fonts/NotoEmojiSubset.ttf','x:type':'simple'})
    sub(fu,'svg:font-face-format',{'svg:string':'truetype'})
manifest=E.fromstring(files['META-INF/manifest.xml'])
for path,mime in [('Fonts/NotoEmojiSubset.ttf','application/x-font-ttf'),('Fonts/OFL.txt','text/plain')]:
    files[path]=(R/'fonts'/Path(path).name).read_bytes()
    sub(manifest,'m:file-entry',{'m:full-path':path,'m:media-type':mime})
files['META-INF/manifest.xml']=E.tostring(manifest,xml_declaration=True,encoding='UTF-8')

files['content.xml']=E.tostring(c,xml_declaration=True,encoding='UTF-8')
files['styles.xml']=E.tostring(styles,xml_declaration=True,encoding='UTF-8')
OUT.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(OUT,'w') as z:
    z.writestr('mimetype',files.pop('mimetype'),compress_type=zipfile.ZIP_STORED)
    for name,data in files.items():z.writestr(name,data,compress_type=zipfile.ZIP_DEFLATED)
print(json.dumps({'output':str(OUT),'toc_entries':len(body.findall(q('t:p'))),'pages_resolved':len(pages)}))
