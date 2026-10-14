#!/usr/bin/env python3
"""rawbatch.py BATCH ITEMS.json OUTDIR -> OUTDIR/v<BATCH>.json, OUTDIR/gui/b<N>-first.js, b<N>-rest<k>.js

For sections whose parts aren't in a parts file (2026-10-12: section 4's sweep fix). ITEMS.json is [[name, text], ...].
The page gets the texts themselves (no window.__PARTS), checks each text's sha-256[:12] before anything is sent, sends
three in the first call and up to three in each rest call, as sN/build_batch.py does. Also:
  rawbatch.py --section ARTICLE.md "HEADING LINE" -> prints the section's visible text as the page shows it (headings
  without '#', links as their words, no images, no HTML comments, no emphasis marks)."""
import hashlib, json, pathlib, re, sys


def visible_section(article, heading):
    art = pathlib.Path(article).read_text(encoding='utf-8')
    i = art.index(heading + '\n')
    m = re.search(r'\n# ', art[i + len(heading):])
    sec = art[i:i + len(heading) + (m.start() if m else len(art))]
    sec = re.sub(r'<!--.*?-->', '', sec, flags=re.S)
    out = []
    for b in re.split(r'\n\s*\n', sec):
        b = b.strip()
        if not b or re.match(r'^\[image \d+\]\(', b) or re.match(r'^https?://\S+$', b):
            continue
        b = re.sub(r'^#{1,6}\s+', '', b)
        b = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', b)
        b = re.sub(r'(?<!\w)\*([^*\n]+)\*(?!\w)', r'\1', b)
        out.append(b)
    return '\n\n'.join(out)


def main():
    if sys.argv[1] == '--section':
        print(visible_section(sys.argv[2], sys.argv[3]))
        return
    batch, items_path, outdir = sys.argv[1:4]
    n = batch[:-1]
    items = json.load(open(items_path, encoding='utf-8'))
    out = pathlib.Path(outdir)
    (out / 'gui').mkdir(parents=True, exist_ok=True)
    H = {name: hashlib.sha256(t.encode()).hexdigest()[:12] for name, t in items}
    json.dump({'batch': batch, 'texts': dict(items)}, open(out / f'v{n}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    first = ("const T=" + json.dumps(items, ensure_ascii=False) + "; const H=" + json.dumps(H) + "; const bad=[]; "
             "window.__B" + n + "=T.map(([name,text])=>({name,text})); "
             "for(const it of window.__B" + n + "){ if((await __h(it.text))!==H[it.name]) bad.push(it.name);} "
             "window.__B" + n + "ok=!bad.length; let r=['not sent']; if(!bad.length){ r=await __pgSubmit(window.__B" + n + ".slice(0,3)); } "
             "'bad '+bad.join(',')+' | '+r.join(' | ')+' | '+new Date().toISOString()")
    (out / 'gui' / f'b{n}-first.js').write_text(first, encoding='utf-8')
    for k, lo in enumerate(range(3, len(items), 3), 1):
        rest = (f"let r=['not sent: first call missing or its hash check failed']; if(window.__B{n}ok && window.__B{n}){{ "
                f"r=await __pgSubmit(window.__B{n}.slice({lo},{lo + 3})); }} r.join(' | ')+' | '+new Date().toISOString()")
        (out / 'gui' / f'b{n}-rest{k}.js').write_text(rest, encoding='utf-8')
    for name, t in items:
        print(name, len(t.split()), H[name], sep='\t')


if __name__ == '__main__':
    main()
