"""SC-106d, the potassium card with his view in it (2026-11-11, after his answer of 21:01 UTC on x1108e: SC-106c to
revise, with his comment). His points, checked through PubMed (SCIENCE-P23.md, "SC-106c and his comment"):

- "brain function tends to improve in general (including mood, but not "vigor" in one study) when potassium to sodium
  ratio is increased": for mood, one small trial (Torres 2008); for memory and thinking the studies are mixed (Nowak
  2018, whose authors don't take its ratio result as a reason to change diet; Zhao 2025; Yoshida 2026). So the paragraph
  gives it as his view, with the mood trial and the limit he named, not as what the science shows.
- the paleo diet's potassium: Stone Age diets are estimated at 400 +/- 125 mEq a day, more than four times current and
  recommended intakes (Sebastian 2006); a paleo-type diet improved blood pressure and insulin in nine people over ten days
  (Frassetto 2009).
- the confounding he names (sodium and potassium move together; foods bring more than potassium; coaching in diet
  trials): kept in one clause; GPT's PTSD diet trials go to the coherence read.
The fresh reader's needed read found S2 and S3 not needed; they carry his view, so they stay, and the card shows him the
paragraph without them (needed/sp106d/READ.md).
"""
import texts_x1108d as D
import texts_x1108e as E

ABURTO = D.ABURTO
NIH = E.NIH
TORRES = D.TORRES
SEBASTIAN = 'https://pubmed.ncbi.nlm.nih.gov/17275582/'
FRASSETTO = 'https://pubmed.ncbi.nlm.nih.gov/19209185/'
NOWAK = 'https://pubmed.ncbi.nlm.nih.gov/29393090/'
ZHAO = 'https://pubmed.ncbi.nlm.nih.gov/40139389/'
YOSHIDA = 'https://pubmed.ncbi.nlm.nih.gov/42083372/'
YOUSSEF = 'https://pubmed.ncbi.nlm.nih.gov/36282607/'

S2 = ('I think more potassium for the salt you eat helps the brain too: in one trial, a diet lower in salt and higher in '
      'potassium lifted mood a little ([Torres, et al, 2008](%s)), though studies like it can\'t separate the potassium from '
      'the salt or the rest of the food.' % TORRES)
S3 = ('Stone Age diets are estimated to have had more than four times the potassium we eat now ([Sebastian, et al, '
      '2006](%s)), so eating closer to a paleo diet probably does more than adding a couple of potatoes, but the potatoes '
      'and greens below are the easy way to start.' % SEBASTIAN)
S1, S4 = E.NEW106.split(' If you have kidney disease', 1)
S4 = 'If you have kidney disease' + S4
NEW106 = ' '.join([S1, S2, S3, S4])
WITHOUT = E.NEW106   # the paragraph without his view: SC-106c's

T = []
for e in E.T:
    e = dict(e)
    if e['key'] == 'SP106C':
        e['key'] = 'SP106D'
        e['swap'] = [(D.OLD106, NEW106)]
        e['for_'] = ('the reader on Strategy A (BHB salts with a standard low-sugar diet) learns why to eat potassium-rich '
                     'food, what it may do for them, and whether it is safe for them, before the target (4,700 mg a day) '
                     'and the foods')
    elif e['key'] == 'SP115E':
        e['key'] = 'SP115F'
    T.append(e)

plain = D.plain
