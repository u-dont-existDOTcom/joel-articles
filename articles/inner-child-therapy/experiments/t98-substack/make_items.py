#!/usr/bin/env python3
"""Turn 98: the items of round 5 whose readings inside the halves decide something, each as its text in TEXT-A.txt or
TEXT-B.txt (a heading and its paragraphs, or one paragraph), found by a line it contains. Writes ITEMS.json and
items/<key>.txt (the ledger hashes those files)."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
norm = lambda s: re.sub('[“”]', '"', re.sub('[‘’]', "'", s))
ITEMS = [
    # key, half, scope, heading or None, a line in the paragraph, what it decides
    ('t98i_byt', 'A', 'section', 'Before You Try to Go Deep', None, 'whether his rewrite (P3, P4) holds inside the half'),
    ('t98i_body', 'A', 'section', 'Your Body Might Need Some Love First', None, 'whether his P3 to P5 hold inside the half'),
    ('t98i_parent', 'A', 'section', 'The Parent You Inherited', None, 'whether his rewrite holds inside the half'),
    ('t98i_padult5', 'A', 'paragraph', None, "So it's worth noticing what it's doing to you.", 'whether round 4\'s Low window here (Low 23) was the check varying'),
    ('t98i_happy', 'B', 'section', 'How Much Happiness Do You Know Is Possible?', None, 'whether his rewrite holds inside the half'),
    ('t98i_shallow', 'B', 'section', 'When the Practice Feels Real but Stays Shallow', None, 'whether his rewrite holds inside the half'),
    ('t98i_related', 'B', 'section', 'Related Clinical Work', None, 'whether my wording of his line (89: A) holds inside the half'),
    ('t98i_guide5', 'B', 'paragraph', None, "The texts and the sulking aren't", 'whether round 4\'s Low window here (Low 42) was the check varying'),
    ('t98i_write6', 'B', 'paragraph', None, 'You can say all the right words, but if the tone is accusatory', 'whether round 4\'s Low window here (Low 35) was the check varying'),
    ('t98i_forgive3', 'B', 'paragraph', None, "Seeing how they got there doesn't make it okay.", 'whether round 4\'s Low windows here (Low 13, Low 37) were the check varying'),
    ('t98i_ended1', 'B', 'paragraph', None, "You don't have to buy what it teaches about death and rebirth", 'whether round 4\'s Low window here (Low 36) was the check varying'),
    ('t98i_borrowed1', 'B', 'paragraph', None, 'Reparenting is usually talked about as something you do alone', 'whether it reads AI inside the half again, though it passes alone (E215)'),
]


def blocks(half):
    return (HERE / ('TEXT-%s.txt' % half)).read_text(encoding='utf-8').rstrip('\n').split('\n\n')


def main():
    out = {}
    (HERE / 'items').mkdir(exist_ok=True)
    for key, half, scope, head, line, decides in ITEMS:
        bl = blocks(half)
        if head:
            i = [n for n, b in enumerate(bl) if b == head]
            assert len(i) == 1, (key, i)
            i = i[0]
            # the heading's level is not in the plain text; a section runs to the next block that is a known heading of the article
            j = i + 1
            while j < len(bl) and not HEADS.get(bl[j]):
                j += 1
            text = '\n\n'.join(bl[i:j])
        else:
            hit = [b for b in bl if norm(line) in norm(b)]
            assert len(hit) == 1, (key, len(hit))
            text = hit[0]
        (HERE / 'items' / (key + '.txt')).write_text(text, encoding='utf-8')
        out[key] = {'half': half, 'scope': scope, 'words': len(text.split()), 'first': text[:80], 'decides': decides}
    (HERE / 'ITEMS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for k, v in out.items():
        print('%-15s %s %-9s %4d words | %s' % (k, v['half'], v['scope'], v['words'], v['first'][:60].replace('\n', ' / ')))


# The article's headings, as plain text, so a section stops at the next heading of any level (E220's sections are h2s or an h1's own paragraphs).
ROOT = HERE.parents[3]
_md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
HEADS = {re.sub(r'^#+\s*', '', l).strip(): True for l in _md.split('\n') if re.match(r'^#{1,4} ', l)}

if __name__ == '__main__':
    main()
