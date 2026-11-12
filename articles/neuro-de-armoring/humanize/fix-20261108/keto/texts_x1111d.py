"""SC-48c: two points in his clause on block 48's last sentence, checked against the review he cites (his answers on
x1111c, exported 2026-11-12 18:23 UTC; KETO-PTSD.md, "His clause, checked").

- "the salts work for rats with trauma": the rat studies the review covers gave BHB by injection, under the skin
  (Yamanashi 2020: DL-BHB in buffered saline, 250 mg/kg, subcutaneous; anxiety-related behavior eased) or by injection
  twice a day for a week (Jung 2025: anxiety and fear behaviors prevented, corticosterone normalized), or MCT oil by mouth
  (Yoshioka 2026). None gave the salts by mouth. So: "BHB injections work for rats with trauma".
- "although not nearly as proven for humans as the keto diet is": the review says no ketogenic therapy has shown efficacy
  for PTSD in people against a control group, and "Another open question remains whether supplementation can achieve
  effects comparable to ketogenic diets." So: "although in humans it's still an open question whether the salts work as
  well as the keto diet".

The rest of his sentence, his forum point and his link stay as he wrote them.
"""
import re

import texts_x1111c as C

REDDIT = 'https://www.reddit.com/r/keto/comments/1fmu0po/ketone_supplements_insanely_good/'
ENGELHARDT = 'https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2026.1854499/full'
YAMANASHI = 'https://pubmed.ncbi.nlm.nih.gov/33303808/'
JUNG = 'https://pubmed.ncbi.nlm.nih.gov/41412336/'
YOSHIOKA = 'https://pubmed.ncbi.nlm.nih.gov/41942638/'

START = C.START
RATS_OLD = 'and the salts work for rats with trauma'
RATS_NEW = 'and BHB injections work for rats with trauma'
PEOPLE_OLD = 'although not nearly as proven for humans as the keto diet is'
PEOPLE_NEW = 'although in humans it\'s still an open question whether the salts work as well as the keto diet'
SWAPS = [(RATS_OLD, RATS_NEW), (PEOPLE_OLD, PEOPLE_NEW)]
FOR = ('the reader with trauma learns why the usual drugs fall short and what this protocol does instead, and what has '
       'been seen when people and animals with PTSD tried ketosis, and how far it goes')


def plain(md):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', md))
