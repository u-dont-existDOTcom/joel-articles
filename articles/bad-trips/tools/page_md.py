"""The bad-trips guide as the Markdown the shared review pages read (one list item per block, one quoted paragraph per
block, images as [image N](url), bold left out since the pages don't render it), plus the map from the block ids (B0..B438 in original-blocks.json) to the page's
block indices (tools/humanization/suggestion_review.py blocks()).

  python3 articles/bad-trips/tools/page_md.py articles/bad-trips/original-blocks.json OUT.md OUT-map.json
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402


def page_blocks(b, img_no):
    k, md = b['kind'], b['md']
    if k == 'image':
        m = re.match(r'!\[[^\]]*\]\(([^)]+)\)', md)
        img_no[0] += 1
        return ['[image %d](%s)' % (img_no[0], m.group(1))]
    if k == 'youtube':
        return [md]
    if k == 'hr':
        return ['---']
    if k in ('ul', 'ol'):
        items = []
        for line in md.split('\n'):
            if re.match(r'^(\d+\.|-) ', line):
                items.append(line)
            elif items:
                items[-1] += ' ' + line.strip()
        return items
    if k == 'blockquote':
        paras, cur = [], []
        for line in md.split('\n'):
            if line.strip() == '>':
                if cur:
                    paras.append(cur)
                cur = []
            else:
                cur.append(re.sub(r'^>\s?', '', line).rstrip())
        if cur:
            paras.append(cur)
        return ['> ' + ' '.join(x.strip() for x in p if x.strip()) for p in paras]
    return [md.replace('  \n', ' ')]


def main(blocks_json, out_md, out_map):
    bl = json.load(open(blocks_json, encoding='utf-8'))
    img_no, parts, owner = [0], [], []
    for b in bl:
        for pb in page_blocks(b, img_no):
            pb = pb.replace('**', '')  # the review pages don't render bold (no other lane's Markdown has it)
            if re.search(r'\*\[|\]\([^)]*\)\*|\[\*', pb):  # italics around or inside a link confuse the page's reader;
                pb = pb.replace('*', '')                      # the article text has no literal asterisks
            parts.append(pb)
            owner.append(b['id'])
    md = '\n\n'.join(parts) + '\n'
    pathlib.Path(out_md).write_text(md, encoding='utf-8')
    pbl = SR.blocks(md)
    # each page block (non-empty) belongs to the B block it came from, in order
    raw = [p for p in parts]
    assert len(pbl) == len([p for p in raw if p.strip()]), (len(pbl), len(raw))
    mp = {}
    for i, bid in enumerate(owner):
        mp.setdefault(bid, []).append(i)
    json.dump({'about': 'B id -> page block indices in %s' % pathlib.Path(out_md).name, 'map': mp}, open(out_map, 'w'), indent=0)
    print(len(bl), 'B blocks ->', len(pbl), 'page blocks')


if __name__ == '__main__':
    main(*sys.argv[1:4])
