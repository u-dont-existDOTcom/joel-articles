"""SC-48b: block 48's last sentence, after his message of 2026-11-11 22:53 UTC ("ketones do seem to help ppl with ptsd")
and GPT's review of ketogenic diets and ketone salts for PTSD (../joel-20261111-2253-gpt-ketone-review.txt).

The sentence, mine and kept in his own version of the paragraph on SC-48 ("Whether ketosis does that in people hasn't
been tested."), is true of the HDAC route but reads as if ketosis had never been tried in people with PTSD. Checked
through PubMed and ClinicalTrials.gov (KETO-PTSD.md):

- Edwards 2024: a keto diet with BHB salts for 4 weeks in Oslo; 3 included, 2 finished; the PCL-5, the standard 80-point
  PTSD checklist, fell 70 to 50 and 50 to 40, "a reliable and clinically meaningful improvement"; ketosis on 87% of days.
- Bellamy & Laurent 2025: a case; PCL-5 80 (its maximum) to 0 by week 12; three years of trauma-focused therapy "did not
  notably improve her symptoms".
- Laurent 2026: a case of PTSD "nonresponsive to conventional interventions including psychotherapy and
  pharmacotherapy"; PCL-5 32 to 2 at 27 weeks.
- No controlled trial of the diet: the registered studies are single-arm (NCT05415982, Edwards's; NCT07415590, six people
  in Munich, completed in August 2026, no results posted); the 2026 integrative review finds "only minimal reliable
  information" from human studies.
- Youssef 2022: BHB salts against a placebo for six weeks; no difference between the groups (p = .60 after; group by time
  p = .80 per GPT's reading of the full paper), with the groups unbalanced at the start and few finishing: too small to
  tell either way, as its authors say.
"""
import re

SHIMAZU = 'https://escholarship.org/uc/item/4w889738'
WHITTLE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3961057'
EDWARDS = 'https://pubmed.ncbi.nlm.nih.gov/39588043/'
BELLAMY = 'https://pubmed.ncbi.nlm.nih.gov/40626225/'
LAURENT = 'https://pubmed.ncbi.nlm.nih.gov/41783812/'
YOUSSEF = 'https://pubmed.ncbi.nlm.nih.gov/36282607/'

START = 'Why don\'t these drugs work on calcified PTSD?'
HIS = ('Why don\'t these drugs work on calcified PTSD? Because even if they did work for mood by modulating serotonin '
       'transmission, PTSD is not a mood disorder. That\'s a bit like putting some Bengay on a broken leg. This protocol '
       'tries to get at the underpinnings of the problem.')
OLD = 'Whether ketosis does that in people hasn\'t been tested.'
S6 = ('In people with PTSD, the first small study of a keto diet with BHB supplements found that both people who finished '
      'its four weeks improved, by 20 and 10 points on the standard 80-point PTSD checklist, which its authors call '
      'clinically meaningful ([Edwards, et al, 2024](%s)).' % EDWARDS)
S7 = ('In two case reports, women whose PTSD hadn\'t responded to treatment were nearly or fully free of symptoms after '
      'months on the diet ([Bellamy & Laurent, 2025](%s); [Laurent, 2026](%s)).' % (BELLAMY, LAURENT))
S8 = ('No controlled trial of the diet has been done yet, and the one placebo-controlled trial of BHB supplements alone '
      'was too small to tell either way ([Youssef, et al, 2022](%s)).' % YOUSSEF)
NEW = ' '.join([S6, S7, S8])
FOR = ('the reader with trauma learns why the usual drugs fall short and what this protocol does instead, and what has '
       'been seen when people with PTSD tried ketosis')


def plain(md):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md))
