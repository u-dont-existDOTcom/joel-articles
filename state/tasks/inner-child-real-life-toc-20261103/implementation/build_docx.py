from pathlib import Path
import json,re
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT=Path('/workspace/scratch/4845c4a6c885/odt_work')
ast=json.loads((ROOT/'document.json').read_text())
ledger=json.loads((ROOT/'preservation-ledger.json').read_text())
doc=Document()
sec=doc.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=Inches(.8);sec.bottom_margin=Inches(.75)
sec.left_margin=Inches(.85);sec.right_margin=Inches(.85)
sec.footer_distance=Inches(.32)
normal=doc.styles['Normal'];normal.font.name='Liberation Serif';normal.font.size=Pt(12)
normal.font.color.rgb=RGBColor(0,0,0)
normal.paragraph_format.line_spacing=1.12
normal.paragraph_format.space_after=Pt(7)
normal.paragraph_format.widow_control=True
normal.paragraph_format.keep_together=False
for s in ['Body Text','First Paragraph','List Paragraph']:
    if s in doc.styles:
        doc.styles[s].base_style=normal
        doc.styles[s].font.name='Liberation Serif'
        doc.styles[s].font.size=Pt(12)
        doc.styles[s].paragraph_format.space_after=Pt(7)
for level,size,before,after in [(1,24,0,15),(2,17,18,8),(3,13.5,13,6),(4,12,10,5)]:
    st=doc.styles[f'Heading {level}']
    st.font.name='Liberation Sans';st.font.size=Pt(size);st.font.bold=True;st.font.color.rgb=RGBColor(0,0,0)
    st.paragraph_format.space_before=Pt(before);st.paragraph_format.space_after=Pt(after)
    st.paragraph_format.keep_with_next=True;st.paragraph_format.keep_together=True
    st.paragraph_format.widow_control=True
    # Explicit outline levels survive the ODT conversion and drive Navigator.
    pr=st.element.get_or_add_pPr();el=pr.find(qn('w:outlineLvl'))
    if el is None: el=OxmlElement('w:outlineLvl');pr.append(el)
    el.set(qn('w:val'),str(level-1))
    borders=pr.find(qn('w:pBdr'))
    if borders is not None: pr.remove(borders)
for level in range(1,5):
    name=f'TOC {level}'
    st=doc.styles[name] if name in doc.styles else doc.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
    st.base_style=normal;st.font.name='Liberation Sans';st.font.size=Pt(10.5)
    st.font.color.rgb=RGBColor(0,0,0);st.font.bold=(level==2)
    st.paragraph_format.left_indent=Inches(max(0,level-2)*.2)
    st.paragraph_format.space_after=Pt(3);st.paragraph_format.space_before=Pt(0)
    st.paragraph_format.line_spacing=1.05;st.paragraph_format.keep_with_next=False
    st.paragraph_format.keep_together=False
for name in ['TOC Heading','Contents Heading']:
    st=doc.styles[name] if name in doc.styles else doc.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
    st.base_style=normal;st.font.name='Liberation Sans';st.font.size=Pt(15);st.font.bold=True;st.font.color.rgb=RGBColor(0,0,0)
    st.paragraph_format.space_before=Pt(6);st.paragraph_format.space_after=Pt(10)
    pr=st.element.get_or_add_pPr();el=pr.find(qn('w:outlineLvl'))
    if el is None: el=OxmlElement('w:outlineLvl');pr.append(el)
    el.set(qn('w:val'),'9')

def text_of(xs):
    s=''
    for x in xs:
        t=x['t'];c=x.get('c')
        if t=='Str':s+=c
        elif t in ('Space','SoftBreak','LineBreak'):s+=' '
        elif t in ('Emph','Strong','Strikeout','SmallCaps'):s+=text_of(c)
        elif t=='Link':s+=text_of(c[1])
        elif t=='Quoted':s+=text_of(c[1])
        elif t=='Code':s+=c[1]
    return s

def inline(p,xs,bold=False,italic=False):
    for x in xs:
        t=x['t'];c=x.get('c')
        if t in ('Str','Space','SoftBreak','LineBreak'):
            val=c if t=='Str' else ('\n' if t=='LineBreak' else ' ')
            r=p.add_run(val);r.bold=bold;r.italic=italic
            if any(ord(ch)>0x1f000 for ch in val):
                r.font.name='Noto Color Emoji'
                rf=r._r.get_or_add_rPr().get_or_add_rFonts();rf.set(qn('w:eastAsia'),'Noto Color Emoji')
        elif t=='Emph':inline(p,c,bold,True)
        elif t=='Strong':inline(p,c,True,italic)
        elif t=='Link':
            label=text_of(c[1]);url=c[2][0]
            link=OxmlElement('w:hyperlink');link.set(qn('r:id'),p.part.relate_to(url,RT.HYPERLINK,is_external=True))
            r=OxmlElement('w:r');pr=OxmlElement('w:rPr');color=OxmlElement('w:color');color.set(qn('w:val'),'174C79');pr.append(color)
            u=OxmlElement('w:u');u.set(qn('w:val'),'single');pr.append(u);r.append(pr)
            tx=OxmlElement('w:t');tx.text=label;r.append(tx);link.append(r);p._p.append(link)
        elif t=='Code':p.add_run(c[1])
        elif t=='RawInline':
            if c[0]=='html':p.add_run(re.sub('<[^>]+>','',c[1]))
        else: raise ValueError(('Unsupported inline',x))

def bookmark(p,name,ident):
    start=OxmlElement('w:bookmarkStart');start.set(qn('w:id'),str(ident));start.set(qn('w:name'),name)
    end=OxmlElement('w:bookmarkEnd');end.set(qn('w:id'),str(ident))
    p._p.insert(0,start);p._p.append(end)

heading_id=0;body_paras=[];comment_target=None
def block(b):
    global heading_id,comment_target
    t=b['t'];c=b.get('c')
    if t=='Header':
        level=c[0];p=doc.add_paragraph(style=f'Heading {level}');inline(p,c[2]);heading_id+=1;bookmark(p,f'ic_heading_{heading_id:02d}',heading_id)
        return p
    if t in ('Para','Plain'):
        p=doc.add_paragraph(style='Normal');inline(p,c);body_paras.append(p)
        if p.text.startswith('You may not know for certain whether the other person'):
            comment_target=p
        return p
    if t=='BulletList':
        for item in c:
            for j,entry in enumerate(item):
                assert entry['t'] in ('Para','Plain')
                p=doc.add_paragraph(style='List Bullet' if j==0 else 'List Paragraph');inline(p,entry['c']);body_paras.append(p)
        return None
    raise ValueError(('Unsupported block',t))

blocks=ast['blocks'];assert blocks[0]['t']=='Header'
block(blocks[0])
doc.add_paragraph('Contents',style='TOC Heading')
p=doc.add_paragraph()
r=p.add_run();a=OxmlElement('w:fldChar');a.set(qn('w:fldCharType'),'begin');a.set(qn('w:dirty'),'true');r._r.append(a)
r=p.add_run();a=OxmlElement('w:instrText');a.set(qn('xml:space'),'preserve');a.text=' TOC \\o "2-4" \\h \\z ';r._r.append(a)
r=p.add_run();a=OxmlElement('w:fldChar');a.set(qn('w:fldCharType'),'separate');r._r.append(a)
p.add_run('Contents')
r=p.add_run();a=OxmlElement('w:fldChar');a.set(qn('w:fldCharType'),'end');r._r.append(a)
doc.add_page_break()
for b in blocks[1:]:block(b)

assert comment_target is not None
note=ledger['comment']['visible_text']
if hasattr(doc,'add_comment'):
    doc.add_comment(comment_target.runs,text=note,author='Joel source note',initials='JR')
else:raise RuntimeError('python-docx comments support missing')

fp=sec.footer.paragraphs[0];fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=fp.add_run();r.font.name='Liberation Sans';r.font.size=Pt(9)
a=OxmlElement('w:fldSimple');a.set(qn('w:instr'),'PAGE');r._r.append(a)
settings=doc.settings.element
u=settings.find(qn('w:updateFields'))
if u is None:u=OxmlElement('w:updateFields');settings.append(u)
u.set(qn('w:val'),'true')
doc.core_properties.title='Bringing Reparenting Into Real Life'
doc.core_properties.author='Joel Rosenblum'
doc.core_properties.subject='Inner child therapy guide'
doc.core_properties.comments=''
out=ROOT/'Bringing_Reparenting_Into_Real_Life.docx';doc.save(out)
print(json.dumps({'docx':str(out),'headings':heading_id,'body_paragraphs':len(body_paras),'comments':1},ensure_ascii=False))
