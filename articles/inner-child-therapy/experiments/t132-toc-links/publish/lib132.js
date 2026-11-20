// lib132.js: shared helpers for turn 132's edit of his post (prepended to probe132.js and build132.js).
const P132 = {
  findAll(doc, needle) {
    // every occurrence of needle inside one textblock: [{from, to, node, pos}] in document positions
    const out = [];
    doc.descendants((node, pos) => {
      if (!node.isTextblock) return true;
      let text = '', map = [];
      node.forEach((child, off) => {
        if (child.isText) { for (let k = 0; k < child.text.length; k++) { map.push(pos + 1 + off + k); } text += child.text; }
        else { map.push(null); text += '￼'; }
      });
      let i = text.indexOf(needle);
      while (i >= 0) {
        const a = map[i], b = map[i + needle.length - 1];
        if (a !== null && b !== null) out.push({from: a, to: b + 1, node, pos});
        i = text.indexOf(needle, i + 1);
      }
      return false;
    });
    return out;
  },
  headings(doc) { const h = []; doc.forEach((n, off) => { if (n.type.name === 'heading') h.push({pos: off, level: n.attrs.level, text: n.textContent, node: n}); }); return h; },
  links(doc) { const l = []; doc.descendants((n) => { if (n.isText) for (const m of n.marks) if (m.type.name === 'link') l.push({text: n.text, href: m.attrs.href}); }); return l; },
  sha: async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))].map((x) => x.toString(16).padStart(2, '0')).join(''),
};
