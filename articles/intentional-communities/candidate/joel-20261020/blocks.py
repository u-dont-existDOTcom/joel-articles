"""Block texts of a Substack editor paste, in order: headings, paragraphs, list items (with their heading path)."""
import sys, json, re
from bs4 import BeautifulSoup

def blocks(path):
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    out = []
    head = ''
    for el in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li']):
        if el.name == 'p' and el.find_parent('li'):
            continue
        if el.find_parent(['figure', 'figcaption']) is not None and el.name == 'p':
            kind = 'caption'
        else:
            kind = el.name
        t = re.sub(r'\s+', ' ', el.get_text(' ', strip=True)).strip()
        t = re.sub(r' ([,.;:!?)])', r'\1', t).replace('( ', '(')
        if not t:
            continue
        if kind.startswith('h'):
            head = t
        out.append({'kind': kind, 'head': head, 'text': t})
    return out

if __name__ == '__main__':
    for p in sys.argv[1:]:
        b = blocks(p)
        json.dump(b, open(p + '.blocks.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print(p, len(b), 'blocks', sum(len(x['text'].split()) for x in b), 'words', sum(x['kind'].startswith('h') for x in b), 'headings')
