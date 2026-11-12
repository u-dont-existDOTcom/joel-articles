"""SC-95: the ketone strategies, the first item of the read of the whole protocol (coherence/EXTRACT.md, 2.4), with
Strategy A's promise (his "drink Ketones (BHB Salts) to clear the fog"; my "need the fog gone fast").

- 2.4: block 95 says you must pick one of the two strategies, because the salts bring sodium and the diet drains it (his
  post: "You must choose your fuel strategy. This determines your electrolyte protocol."); the timeline starts on the
  salts (block 169), moves to the diet in Weeks 3 to 5 (block 177), and in that phase still says "Drink BHB" when foggy
  (block 179). Taken in turn, the two strategies don't clash; taken together, the salts' sodium goes toward the sodium
  the diet drains, and the one PTSD study with ketosis measured gave both together (Edwards 2024, a keto diet with BHB
  salts). So the sentence says what the choice decides (the salt plan) and what a drink of the salts on the diet does.
- The promise: exogenous ketones gave a modest lift to thinking against placebo in a meta-analysis of 29 trial protocols
  (1,117 people; SMD 0.29), with no difference between acute and longer use, and bigger daily doses going with bigger
  gains (Bonnechere 2026); some trials found nothing (adults with type 2 diabetes, Baranowski 2025; hypoxia, Stalmans
  2025). So "the fog gone fast" becomes "the fog to lift fast", with the trials' finding at its size.
"""
import re

EDWARDS = 'https://pubmed.ncbi.nlm.nih.gov/39588043/'
BONNECHERE = 'https://pubmed.ncbi.nlm.nih.gov/42063954/'
BARANOWSKI = 'https://pubmed.ncbi.nlm.nih.gov/39804761/'
STALMANS = 'https://pubmed.ncbi.nlm.nih.gov/40315254/'

START = 'You must pick one of two ketone strategies'
OLD = ('You must pick one of two ketone strategies, because the salts in one bring their own sodium while the diet in the '
       'other drains it. If you\'re in a crisis and need the fog gone fast, there\'s Strategy A, the "Crisis Mode". You '
       'drink BHB (beta-hydroxybutyrate) salts and keep eating a standard low-sugar diet.')
S1 = ('Your ketone strategy decides how you handle salt, since the salts bring their own sodium while the diet '
      'drains it.')
S2 = 'If you\'re in a crisis and need the fog to lift fast, there\'s Strategy A, the "Crisis Mode".'
S3 = 'You drink BHB (beta-hydroxybutyrate) salts and keep eating a standard low-sugar diet.'
S4 = ('In trials, ketone esters, salts and MCT oil improved thinking a little against a placebo, from a single dose '
      'as well as over two weeks or more ([Bonnechère, et al, 2026](%s)).' % BONNECHERE)
# the versions the two fresh reads saw (needed/sp95, his-fixes/sp95), before their marks were acted on
S1_READ = ('Which ketone strategy you\'re on decides how you handle salt: the salts in one bring their own sodium, while the '
           'diet in the other drains it, so on the diet, a drink of the salts just counts toward the extra sodium you need.')
S4_READ = 'In trials, ketone supplements gave thinking a modest lift, from the first hours as well as over weeks (Bonnechère, et al, 2026).'
NEW = ' '.join([S1, S2, S3, S4])
FOR = ('the reader choosing between the two ketone strategies learns what the choice changes in their salt plan, and what '
       'Strategy A is for and what it does, before Strategy B')


def plain(md):
    return re.sub(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', md)
