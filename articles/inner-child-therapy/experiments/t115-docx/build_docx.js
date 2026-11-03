// Turn 115: the docx from SPEC.json (build_spec.py): the whole guide, the pass as tracked changes, the spots below
// Human, high shaded with comments, and Track Changes on so Joel's own edits show as his.
//   node build_docx.js SPEC.json OUT.docx
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, InsertedTextRun, DeletedTextRun, ShadingType,
  CommentRangeStart, CommentRangeEnd, CommentReference, AlignmentType,
} = require('docx');

const [, , specPath, outPath] = process.argv;
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const AUTHOR = spec.author;
const DATE = spec.date;
let rev = 1;
const LEVEL = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3, 4: HeadingLevel.HEADING_4,
  5: HeadingLevel.HEADING_5, 6: HeadingLevel.HEADING_6 };

function runOf(r) {
  const opts = { text: r.t };
  if (r.i) opts.italics = true;
  if (r.shade) opts.shading = { type: ShadingType.CLEAR, color: 'auto', fill: r.shade };
  if (r.br_before) opts.break = 1;
  if (r.ins) return new InsertedTextRun({ ...opts, id: rev++, author: AUTHOR, date: DATE });
  if (r.del) return new DeletedTextRun({ ...opts, id: rev++, author: AUTHOR, date: DATE });
  return new TextRun(opts);
}

function children(runs) {
  const out = [];
  for (const r of runs) {
    for (const c of (r.cstart || [])) out.push(new CommentRangeStart(c));
    out.push(runOf(r));
    for (const c of (r.cend || [])) {
      out.push(new CommentRangeEnd(c));
      out.push(new TextRun({ children: [new CommentReference(c)] }));
    }
  }
  return out;
}

const body = [];
body.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(spec.title)] }));
for (const k of spec.key) body.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: k, size: 21 })] }));
// a sample of each shade, so the key's colors can be seen
const NAMES = { AI: 'AI', Low: 'Human, Low', Medium: 'Human, Medium', Nearly: 'Human, Medium, nearly High', Seam: 'a seam' };
body.push(new Paragraph({ spacing: { after: 240 }, children: Object.entries(spec.shade).flatMap(([k, fill], i) => [
  new TextRun({ text: ' ' + NAMES[k] + ' ', shading: { type: ShadingType.CLEAR, color: 'auto', fill } }),
  new TextRun({ text: i < Object.keys(spec.shade).length - 1 ? '   ' : '' })]) }));
for (const b of spec.blocks) {
  if (b.type === 'h') {
    body.push(new Paragraph({ heading: LEVEL[Math.min(b.level + 0, 6)], children: children(b.runs) }));
  } else {
    body.push(new Paragraph({ spacing: { after: 160 }, indent: b.quote ? { left: 567 } : undefined, children: children(b.runs) }));
  }
}

const doc = new Document({
  creator: AUTHOR,
  title: spec.title,
  features: { trackRevisions: true },
  comments: { children: spec.comments.map((c) => ({ id: c.id, author: AUTHOR, date: new Date(DATE),
    children: [new Paragraph({ children: [new TextRun(c.text)] })] })) },
  styles: { default: { document: { run: { font: 'Calibri', size: 22 } } } },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 } } }, children: body }],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(outPath, buf); console.log('wrote', outPath, buf.length, 'bytes'); });
