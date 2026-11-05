"""Joel's Substack editor HTML for the bad-trips guide -> Markdown, word for word, plus a block map.

Every word and link is his; nothing is rewritten. Images become ![alt](src) with Substack's full-size URL, YouTube
embeds become a link line with the video id, horizontal rules become ---. Each block gets a stable id (B0, B1, ...) in
blocks.json (numbered as tools/humanization/reviewer/reviewer.py numbers them, from B0) with its kind, its heading path and its text, so maps and review pages can point at it.

  python3 articles/bad-trips/tools/editor_to_md.py SOURCE.html OUT.md OUT-blocks.json   (from the repo root)
"""
import json, re, sys
from bs4 import BeautifulSoup, NavigableString, Tag


def inline(node):
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ''
    name = node.name
    inner = ''.join(inline(c) for c in node.children)
    if name in ('strong', 'b'):
        return f'**{inner}**' if inner.strip() else inner
    if name in ('em', 'i'):
        return f'*{inner}*' if inner.strip() else inner
    if name == 'a':
        href = node.get('href', '')
        return f'[{inner}]({href})' if href else inner
    if name == 'br':
        return '  \n' if 'ProseMirror-trailingBreak' not in (node.get('class') or []) else ''
    if name in ('sub', 'sup'):
        return f'<{name}>{inner}</{name}>'
    if name == 'code':
        return f'`{inner}`'
    return inner


def figure_md(div):
    img = div.find('img')
    if not img:
        return None
    attrs = img.get('data-attrs')
    src = img.get('src', '')
    alt = img.get('alt', '') or ''
    if attrs:
        try:
            a = json.loads(attrs)
            src = a.get('src') or src
            alt = a.get('alt') or alt
        except Exception:
            pass
    cap = div.find('figcaption')
    line = f'![{alt}]({src})'
    if cap and cap.get_text(strip=True):
        line += f'\n\n*{inline(cap).strip()}*'
    return line


def list_md(lst, depth=0):
    out = []
    ordered = lst.name == 'ol'
    for i, li in enumerate(lst.find_all('li', recursive=False), 1):
        parts, subs = [], []
        for c in li.children:
            if isinstance(c, Tag) and c.name in ('ul', 'ol'):
                subs.append(list_md(c, depth + 1))
            elif isinstance(c, Tag) and c.name == 'p':
                parts.append(inline(c).strip())
            else:
                t = inline(c).strip()
                if t:
                    parts.append(t)
        marker = f'{i}.' if ordered else '-'
        out.append('  ' * depth + f'{marker} ' + ' '.join(p for p in parts if p))
        out.extend(subs)
    return '\n'.join(out)


def blockquote_md(bq):
    lines = []
    for c in bq.children:
        if isinstance(c, Tag) and c.name == 'p':
            txt = inline(c).strip()
            for ln in txt.split('\n'):
                lines.append('> ' + ln.rstrip())
            lines.append('>')
        elif isinstance(c, Tag):
            t = inline(c).strip()
            if t:
                lines.append('> ' + t)
    while lines and lines[-1] == '>':
        lines.pop()
    return '\n'.join(lines)


def main(src, out_md, out_blocks):
    soup = BeautifulSoup(open(src, encoding='utf-8').read(), 'html.parser')
    root = soup.find('div', attrs={'data-testid': 'editor'}) or soup
    blocks, path = [], {}
    n = -1  # B0 first, as reviewer.py numbers blocks

    def add(kind, md, text):
        nonlocal n
        n += 1
        hp = [path[k] for k in sorted(path)]
        blocks.append({'id': f'B{n}', 'kind': kind, 'headings': hp, 'md': md, 'text': text})

    for el in root.children:
        if not isinstance(el, Tag):
            if str(el).strip():
                add('p', str(el).strip(), str(el).strip())
            continue
        name = el.name
        cls = el.get('class') or []
        if re.fullmatch(r'h[1-6]', name):
            level = int(name[1])
            txt = inline(el).strip()
            for k in list(path):
                if k >= level:
                    del path[k]
            path[level] = el.get_text(' ', strip=True)
            add(name, '#' * level + ' ' + txt, el.get_text(' ', strip=True))
        elif name == 'p':
            txt = inline(el).strip()
            if not txt:
                continue
            add('p', txt, el.get_text(' ', strip=True))
        elif name in ('ul', 'ol'):
            add(name, list_md(el), el.get_text(' ', strip=True))
        elif name == 'blockquote':
            add('blockquote', blockquote_md(el), el.get_text(' ', strip=True))
        elif name == 'hr':
            add('hr', '---', '')
        elif name == 'div' and 'captioned-image-container' in cls:
            md = figure_md(el)
            if md:
                add('image', md, '')
        elif name == 'div' and 'youtube-wrap' in cls:
            vid = json.loads(el.get('data-attrs', '{}')).get('videoId', '')
            add('youtube', f'[YouTube video {vid}](https://www.youtube.com/watch?v={vid})', '')
        else:
            txt = inline(el).strip()
            if txt:
                add(name, txt, el.get_text(' ', strip=True))

    md = '\n\n'.join(b['md'] for b in blocks) + '\n'
    open(out_md, 'w', encoding='utf-8').write(md)
    json.dump(blocks, open(out_blocks, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    words = sum(len(b['text'].split()) for b in blocks)
    print(f'{len(blocks)} blocks, {words} words, {len(md)} characters of Markdown')


if __name__ == '__main__':
    main(*sys.argv[1:4])
