"""JOEL-TEXTS.txt for the community article's Emulate check: everything in this folder that is Joel's own words.

  python3 articles/intentional-communities/candidate/joel-20261025/emulate-check/make_joel_texts.py

His messages and attachments as saved word for word (joel-*-message.txt, *-attachment.txt, *-raw.txt), his own section
texts (s5/section-joel-20261006.md, s5/joel-s5-*.txt) and the strings in his answer files (s6, s8, s9 joel-*.json). The
check's main source is his published post (../../../original.md); these are the second source, so a sentence of his
that went in from an answer counts as his.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parents[1]
files = sorted(set(CAND.rglob('joel-*-message.txt')) | set(CAND.rglob('*-attachment.txt')) | set(CAND.rglob('*-raw.txt'))
               | set(CAND.glob('s5/section-joel-20261006.md')) | set(CAND.glob('s5/joel-s5-*.txt')))
jsons = sorted(p for p in CAND.glob('s*/joel-*/*.json')) + sorted(CAND.glob('s6/joel-*.json'))


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


parts = []
for f in files:
    parts.append(f.read_text(encoding='utf-8'))
for f in jsons:
    parts += [s for s in strings(json.loads(f.read_text(encoding='utf-8'))) if len(s.split()) >= 4]
(HERE / 'JOEL-TEXTS.txt').write_text('\n\n'.join(p.strip() for p in parts if p.strip()) + '\n', encoding='utf-8')
print(len(files), 'text files,', len(jsons), 'answer files,', sum(len(p.split()) for p in parts), 'words')

# His and GPT's edits after my final version (master.md of 2026-10-18, commit 1a215ca0, copied here as
# MY-FINAL-20261018.md): his message of 2026-10-20 22:01 UTC, "this is AFTER the final version that *started* with your
# final version -- i then edited it a lot more, as did GPT". Every sentence of his final Substack paste that my version
# doesn't have (under 80% of its words in one sentence of mine), with its links, as Markdown, so the check counts them as
# approved. (r04, community-r04-approved.html, is his "final full html", already after those edits.)
import difflib  # noqa: E402
import sys  # noqa: E402
sys.path.insert(0, str(HERE.parents[4] / 'tools' / 'humanization'))
import emulate_artifacts as ea  # noqa: E402

r04 = ea.load(HERE / 'MY-FINAL-20261018.md')   # mine; named r04 below for the comparison
final = ea.load(CAND / 'joel-20261020' / 'community-final-substack-20261020.html')
r04_sents = [ea.words(b['text'][a:z]) for b in r04 for a, z in ea.sentences(b['text'])]
grams = {}
for k, w in enumerate(r04_sents):
    for g in ea.grams(w):
        grams.setdefault(g, set()).add(k)
lines = []
for b in final:
    spans = ea.seg_spans(b['segs'])
    for a, z in ea.sentences(b['text']):
        w = ea.words(b['text'][a:z])
        cand = set().union(*(grams.get(g, set()) for g in ea.grams(w))) if w else set()
        if any(w == r04_sents[k] for k in cand):
            continue
        md = ''
        for s, e, sg in spans:
            if e <= a or s >= z:
                continue
            t = sg['t'][max(a, s) - s:min(z, e) - s]
            md += '[%s](%s)' % (t, sg['href']) if sg['href'] and t.strip() else t
        lines.append(md.strip())
(HERE / 'JOEL-EDITS-20261020.md').write_text('\n\n'.join(x for x in lines if x) + '\n', encoding='utf-8')
print(len(lines), 'sentences of his final paste that my version of 2026-10-18 does not have')

# The links he added in that paste (the link check reads them; a link on an unchanged sentence counts too).
r04_urls = {sg['href'] for b in r04 for sg in b['segs'] if sg['href']}
added = []
for b in final:
    for sg in b['segs']:
        if sg['href'] and sg['href'] not in r04_urls and sg['href'] not in [u for _t, u in added]:
            added.append((sg['t'], sg['href']))
with open(HERE / 'JOEL-EDITS-20261020.md', 'a', encoding='utf-8') as f:
    f.write('\n' + '\n\n'.join('[%s](%s)' % (t.strip() or 'link', u) for t, u in added) + '\n')
print(len(added), 'links he added in that paste')
