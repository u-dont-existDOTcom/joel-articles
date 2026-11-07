from pathlib import Path
from lxml import etree
import fitz,zipfile,json,hashlib
R=Path(__file__).resolve().parent
P=R.parent/'deliverables/Bringing_Reparenting_Into_Real_Life.odt'
N={'t':'urn:oasis:names:tc:opendocument:xmlns:text:1.0','x':'http://www.w3.org/1999/xlink'}
with zipfile.ZipFile(P) as z:
    c=etree.fromstring(z.read('content.xml'))
    assert 'Fonts/NotoEmojiSubset.ttf' in z.namelist()
entries=c.xpath('//t:index-body/t:p',namespaces=N)
heads=c.xpath('//t:h[@t:outline-level != "1"]',namespaces=N)
bookmarks={x.get('{'+N['t']+'}name') for x in c.xpath('//t:bookmark-start',namespaces=N)}
links=[x.get('{'+N['x']+'}href') for x in c.xpath('//t:index-body//t:a',namespaces=N)]
assert len(entries)==30 and all(x[1:] in bookmarks for x in links)
for name in ['gate_r2','dating_gate']:
    admitted=(R/name/'admitted.txt').read_text()
    assert admitted==(R/name/'candidate.txt').read_text() and admitted in (R/'revised.md').read_text()
pdf=fitz.open(R/'render/Bringing_Reparenting_Into_Real_Life.pdf')
pages=json.loads((R/'heading-pages.json').read_text())
assert pages=={x[1]:x[2] for x in pdf.get_toc() if x[0]>1}
dests=sorted(pdf[0].get_links(),key=lambda x:x['from'].y0)
names=[''.join(h.itertext()) for h in heads]
assert len(dests)==30 and [x['page']+1 for x in dests]==[pages[n] for n in names]
for para,name in zip(entries,names):assert ''.join(para.itertext())==name+str(pages[name])
embedded=fitz.open(R/'embedded-font-check/Bringing_Reparenting_Into_Real_Life.pdf')
counts={ch:sum(pg.get_text().count(ch) for pg in embedded) for ch in '🤪🙈😌😅'}
assert counts=={'🤪':1,'🙈':3,'😌':1,'😅':1}
result={'file':P.name,'sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'size_bytes':P.stat().st_size,
        'pages':len(pdf),'toc_entries':30,'toc_links_verified':30,'toc_page_numbers_verified':30,
        'outline_levels':{'1':1,'2':6,'3':20,'4':4},'embedded_emoji_font':True,
        'embedded_font_only_render_counts':counts,
        'page_layout_review':'All 11 pages visually inspected. Initial missing emoji glyphs fixed with embedded OFL font subset; affected final pages reinspected. No clipping, overlap, blank pages, or stranded headings remain.',
        'review_files':['layout-review-pages-06-11.md','preservation-review.md'],
        'exact_candidate_admissions':['gate_r2/proof.json','dating_gate/proof.json']}
(R/'final-qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
