"""SC-106c, the potassium card corrected again (2026-11-08, after his message of 17:09 UTC: GPT's answers on two things
SC-106b's "why" said). Checked against the sources the same day (SCIENCE-P23.md, "SC-106b checked again"):

- Nerve function: the NIH fact sheet says potassium's gradient "is required for proper nerve transmission", and that
  "Hypokalemia is rarely caused by low dietary potassium intake alone" (NIH 2022). So SC-106b's "no source shows [that
  the foods support nerve function] for eating more" holds, and what the paragraph gives the reader stays blood pressure.
- Torres 2008, read in full: the card had said too much. Both test diets raised urinary potassium about equally (+34.0
  and +35.4 mmol/d); the low-salt one lifted mood a little more; more urinary potassium went with less fatigue; the
  authors give magnesium as another explanation and leave each mineral's part to further study. Potassium's own part
  in mood is open, not ruled out.
- Kidneys and drugs: in a two-year trial in kidney disease, restricting potassium slowed nerve damage (Arnold 2017), and
  ACE inhibitors and ARBs keep potassium in (NIH 2022). With the paragraph now telling people with high blood pressure,
  who often take those drugs, to eat more potassium, the caution goes beside the step (lesson neuro-2026-11-08f's
  warnings beside their tools), on this card.
"""
import texts_x1108d as D

ABURTO = D.ABURTO
NIH = 'https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/'
ARNOLD = 'https://pubmed.ncbi.nlm.nih.gov/28893921/'
TORRES = D.TORRES
TORRES_FULL = ('https://www.cambridge.org/core/journals/british-journal-of-nutrition/article/dietary-electrolytes-are-related-'
               'to-mood/261729C7B3C7D3D2D8D5E1CDF74932FF')

NEW106 = ('The Science: Eating more potassium brings high blood pressure down ([Aburto, et al, 2013](%s)), which matters on '
          'Strategy A, since its salts bring their own sodium. If you have kidney disease or take a blood pressure drug that '
          'holds on to potassium, like an ACE inhibitor or an ARB, ask your doctor first, since potassium can build up in '
          'your blood ([NIH, 2022](%s)).' % (ABURTO, NIH))

T = []
for e in D.T:
    e = dict(e)
    if e['key'] == 'SP106B':
        e['key'] = 'SP106C'
        e['swap'] = [(D.OLD106, NEW106)]
        e['for_'] = ('the reader on Strategy A (BHB salts with a standard diet) learns why to eat potassium-rich food, and '
                     'whether it is safe for them, before the target (4,700 mg a day) and the foods')
    elif e['key'] == 'SP115D':
        e['key'] = 'SP115E'
    T.append(e)

plain = D.plain
