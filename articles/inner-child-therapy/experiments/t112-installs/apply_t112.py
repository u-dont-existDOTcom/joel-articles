#!/usr/bin/env python3
"""Turn 112: his answer to 108.1 (his message of 2026-10-25 21:40 UTC, experiments/t112-answers/JOEL-20261025-2140.md), his
own version of Borrow Love's third paragraph, put in word for word with his characters (his curly apostrophes in "you’d" and
"Solomon’s"). His paste is plain text, so the two links his earlier version had are kept on the words that name what they
go to (the lane's rule for a plain-text paste): "psychological trick" for Kross and Grossmann 2012, "Boosting wisdom:
distance from the self enhances wise reasoning, attitudes, and behavior" (PMID 21728454, the old "cheap trick" link), and
"Solomon’s paradox" for Grossmann and Kross 2014, "Exploring Solomon's paradox" (PMID 24916084). Both were opened through
PubMed's E-utilities on 2026-10-25. 108.2 is A, no change. Applied once; it refuses to run again."""
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2] / 'HUMANIZED-ARTICLE-SO-FAR.md'
OLD = ("Or put somebody you care about into your exact life, your family, your bank account and all, and then step outside it "
       "and ask what you'd tell them. It's a [cheap trick for becoming the outsider to your own mess]"
       "(https://pubmed.ncbi.nlm.nih.gov/21728454/). And the gap it gets around even has a name, [Solomon's paradox]"
       "(https://pubmed.ncbi.nlm.nih.gov/24916084/), after the king everybody brought their disputes to, who then wrecked his "
       "own life.")
NEW = ("Or put somebody you care about into your exact life, your family, all the conditions you face, and then step outside "
       "it and ask what you’d tell them as a friend. This [psychological trick](https://pubmed.ncbi.nlm.nih.gov/21728454/) has "
       "a rich history around it, and even has a name, [Solomon’s paradox](https://pubmed.ncbi.nlm.nih.gov/24916084/), after "
       "the biblical king everybody brought their disputes to, who then wrecked his own life.")
HIS = ("Or put somebody you care about into your exact life, your family, all the conditions you face, and then step outside "
       "it and ask what you’d tell them as a friend. This psychological trick has a rich history around it, and even has a "
       "name, Solomon’s paradox, after the biblical king everybody brought their disputes to, who then wrecked his own life.")
NOTE = ("<!-- Turn 112 (his message of 2026-10-25 21:40 UTC, experiments/t112-answers/JOEL-20261025-2140.md): 108.1, his own "
        "version of this paragraph, word for word (\"this version passes\", his check), with the two links his earlier version "
        "had: \"psychological trick\" goes to the self-distancing study the old \"cheap trick\" link went to, and \"Solomon’s "
        "paradox\" to the Solomon's paradox study. Question 109 asks whether the name should go on the gap, as the study has "
        "it. -->\n\n")

md = ART.read_text(encoding='utf-8')
assert md.count(OLD) == 1, 'the paragraph is not there once (already applied?)'
# his words are exactly what the paragraph says, once the link marks are taken out
import re
assert re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', NEW) == HIS
md = md.replace(OLD, NOTE + NEW)
ART.write_text(md, encoding='utf-8')
print('installed 108.1 (his version) in Borrow Love P3')
