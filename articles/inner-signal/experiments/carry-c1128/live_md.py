#!/usr/bin/env python3
"""live_md.py - the Self-Hypnosis guide as it is live (LIVE-HYPNOSIS-POST-20261128.json, fetched 2026-11-28 through his
laptop) as Markdown for the marking page: the somatic lane's converter
(articles/somatic-therapies/experiments/additions-20261126/live_markdown.py), with each top-level quote box opened so the
picture inside it is kept as an IMAGE note in its place instead of being left out.
  python3 articles/inner-signal/experiments/carry-c1128/live_md.py
Writes LIVE-HYPNOSIS-20261128.md beside this file."""
import importlib.util, json, pathlib
from bs4 import BeautifulSoup
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
spec = importlib.util.spec_from_file_location('lm', ROOT / 'articles/somatic-therapies/experiments/additions-20261126/live_markdown.py')
lm = importlib.util.module_from_spec(spec); spec.loader.exec_module(lm)
body = json.loads((HERE / 'LIVE-HYPNOSIS-POST-20261128.json').read_text(encoding='utf-8'))['post']['body_html']
soup = BeautifulSoup(body, 'html.parser')
opened = 0
for bq in [t for t in soup.children if getattr(t, 'name', None) == 'blockquote']:
    bq.unwrap(); opened += 1
md = lm.convert(str(soup))
(HERE / 'LIVE-HYPNOSIS-20261128.md').write_text(md, encoding='utf-8')
print(opened, 'quote boxes opened;', md.count('<!-- IMAGE'), 'pictures,', md.count('<!-- EMBED'), 'embeds,', len(md.split()), 'words')
