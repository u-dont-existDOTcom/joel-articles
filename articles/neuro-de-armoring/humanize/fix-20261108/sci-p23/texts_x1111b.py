"""SC-106e, the potassium card rethought on the science (2026-11-11, after his message of 22:07 UTC: a claim he makes as
science rests on science, not on "I think"; SC-106d made potassium look like a one-study artifact; my research was thin;
GPT's research; low intakes are common). Sources checked through PubMed and the pages named (SCIENCE-P23.md,
"Rethought on the science"):

- nerves need it: the potassium gradient "is required for proper nerve transmission" (NIH 2022);
- most people eat less than the recommended amount: 28% of Americans aged 1 and up are above the Adequate Intake (the
  2025 Dietary Guidelines Advisory Committee's scientific report, Table D.1.6, published December 2024);
- mood: a diet with more potassium for its salt lifted mood a little (Torres 2008); potassium helped 13 of 16 children
  with steroid-induced mood and behavior problems (Pariury 2019, a retrospective review);
- thinking: older adults who ate more scored higher on cognitive tests and reported less memory decline (Na 2022); not
  every study agrees (Cherbuin 2014; Zingales 2025); nothing shows potassium alone doing it for people who get enough;
- needs differ: diarrhea, vomiting and diuretics cause low potassium (NIH 2022); an inherited kidney condition wastes it
  (Gitelman syndrome, Cruz 2001);
- his paleo point, which he worded as his own view ("probably"), stays as it was on SC-106d;
- blood pressure (Aburto 2013) and the kidney and drug caution (NIH 2022), as before.
"""
import texts_x1108d as D
import texts_x1108e as E
import texts_x1111a as A

NIH = E.NIH
DGAC = 'https://www.dietaryguidelines.gov/sites/default/files/2024-12/Part%20D_Ch%201_%20Data%20Analysis_FINAL_508.pdf'
TORRES = D.TORRES
PARIURY = 'https://pubmed.ncbi.nlm.nih.gov/31538841/'
NA = 'https://doaj.org/article/335f413ec4a5414d8abb24b26101837e'
CRUZ = 'https://pubmed.ncbi.nlm.nih.gov/11168953/'
CHERBUIN = 'https://pubmed.ncbi.nlm.nih.gov/24550825/'
ZINGALES = 'https://pubmed.ncbi.nlm.nih.gov/41081007/'
TAIM = 'https://pubmed.ncbi.nlm.nih.gov/2003706/'
DAI = 'https://pubmed.ncbi.nlm.nih.gov/41316473/'
SEBASTIAN = A.SEBASTIAN
ABURTO = D.ABURTO

S1 = ('The Science: Your nerves need potassium to fire and reset ([NIH, 2022](%s)), yet most of us eat less than the '
      'recommended amount: only about 3 in 10 Americans reach it ([Dietary Guidelines Advisory Committee, 2024](%s)).'
      % (NIH, DGAC))
S2 = ('In a diet trial, people who took in more potassium and less salt had better mood and less fatigue ([Torres, et '
      'al, 2008](%s)), and potassium supplements eased mood and behavior problems in 13 of 16 children taking steroid '
      'drugs, which mimic the stress hormone cortisol ([Pariury, et al, 2019](%s)).' % (TORRES, PARIURY))
S3 = ('People who eat more of it also tend to think and remember better as they get older ([Na, et al, 2022](%s)), '
      'though not every study agrees, and none yet shows extra potassium helping people who already get enough.' % NA)
S4 = ('Some people need more than others, too, since diarrhea, diuretics and some inherited kidney conditions drain it '
      '([NIH, 2022](%s); [Cruz, et al, 2001](%s)).' % (NIH, CRUZ))
S5 = ('More potassium also brings high blood pressure down ([Aburto, et al, 2013](%s)), which matters on Strategy A, since '
      'its salts bring their own sodium.' % ABURTO)
S6 = A.S3   # his paleo point, as on SC-106d
S7 = A.S4   # the kidney and drug caution, as on SC-106c and d
NEW106 = ' '.join([S1, S2, S3, S4, S5, S6, S7])

T = []
for e in A.T:
    e = dict(e)
    if e['key'] == 'SP106D':
        e['key'] = 'SP106E'
        e['swap'] = [(D.OLD106, NEW106)]
        e['for_'] = ('the reader on Strategy A (BHB salts with a standard low-sugar diet), in a protocol for an anxious, '
                     'easily triggered nervous system, learns why potassium matters for them, what raising it may do, '
                     'whether they may need more, and whether it is safe for them, before the target (4,700 mg a day) and '
                     'the foods')
    elif e['key'] == 'SP115F':
        e['key'] = 'SP115G'
    T.append(e)

plain = D.plain
