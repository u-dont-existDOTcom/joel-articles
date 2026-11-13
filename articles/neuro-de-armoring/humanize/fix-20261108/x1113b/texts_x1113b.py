"""x1113b: his answers of 2026-11-12 20:16 UTC (SC-95, the ketone strategies) and 2026-11-13 14:04 and 15:22 UTC (SC-DMSO
and SC-DMSOb), merged as his comments ask ("wasn't sure if this was the place or if we are repeating stuff about the
benefits in diff places..."; "not sure if info is being duplicated, we should try to merge the DMSO info if it is
duplicated"). His words are copied from the files he saved, by script; every change to them is named below and on its card.
Sources: ../coherence/ketone/KETONE-STRATEGY.md ("His SC-95 answer, checked") and ../dmso/DMSO-PTSD.md ("His two DMSO
answers, checked").

SC-95b, block 95 (Strategy A): his version, less two sentences.
- "Data on ketones for PTSD specifically are sparse." goes: block 48 says it already, with the studies (Edwards 2024, the
  case reports, Youssef 2022, Engelhardt 2026).
- His Parkinson's and Alzheimer's sentence moves to block 54 (SC-54): those were a diet and coconut oil, not the salts
  this paragraph is about, and block 54 is where the protocol says ketones are a backup fuel for brains that burn less
  sugar, naming Alzheimer's.
- The trials' link (Bonnechere 2026) back on its words: the cards page showed him the text without links.
SC-54, block 54 (the Fog's fix): his Parkinson's and Alzheimer's sentence, checked.
- The Alzheimer's case in his thread (LongeCity, 2008, quoting the Tampa Bay Times) is Steve Newport, a man; his wife, a
  doctor, said coconut oil seemed to help and that nothing could repair the damage, so "reversed" becomes "improved
  markedly", the 2015 case report's words for his 20 months on a ketone drink (Newport, et al, 2015).
- The Parkinson's study is VanItallie 2005, quoted in the same thread: five people, a month on a ketogenic diet, all
  improved, no comparison group. The randomized trial (Phillips 2018, 47 people) goes with it: the diet eased fatigue,
  sleepiness and thinking problems more than a low-fat diet, movement about the same on both.
SC-DMSOc, the DMSO item after Magnesium: his two versions as one.
- His 15:22 version is the frame, in its order; from his 14:04 version come the 10% vs 5% side effects in stem cell
  transplants, "(that I know of, yet)", the minute after nebulizing, taking it in the morning, and "Translating mouse
  research to humans isn't straightforward."
- 10% vs 5%: his link was Kortleve 2023, a survey of transplant centres about fluids; the finding is the randomized
  trial it cites (Mitrus 2018, 150 adults), so the citation is the trial.
- "including children" moves to the young-mouse study, whose authors worried about the children who get it in stem
  cell transplants: in the uses sentence, the fit read took it as a sign it is safe for children. "as it
  treats hundreds of them" becomes what the book covers (its publisher's page), from arthritis to brain injuries. The link goes to the publisher, since Amazon refused my check ("unauthorized AI agent").
- The sheep: his "prevent toxic cotton smoke from killing 4/6 sheep" was the other way round. Brown 1988: all seven
  untreated sheep died, four of the six given DMSO alone died, all seven given DMSO with heparin lived; the route isn't
  in its abstract. Nebulized is Kimura 1988, the same lab: DMSO with heparin into the windpipe, less lung damage.
- "other rodent studies under other conditions" names its condition: young brains (Hanslick 2009, mice in their first
  month; its authors' worry for children getting it in transplants).
- "No trial has tested it for PTSD" becomes his own "It hasn't been tested (that I know of, yet) specifically for PTSD"
  (lesson neuro-2026-11-13a).
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
ANS = json.loads((FIX / 'dmso' / 'ANSWERS-X1113A-20261113-1524.json').read_text(encoding='utf-8'))
DB = json.loads((FIX / 'CARDS-PAGE-DECISIONS-20261113-1525.json').read_text(encoding='utf-8'))['docs']
HIS = {it['id']: it['your_version'] for it in ANS['items']}
HIS95 = HIS['SC-95']                      # 2026-11-12 20:16 UTC
HIS_D2 = HIS['SC-DMSOb']                  # 2026-11-13 15:22 UTC
HIS_D1 = DB['SC-DMSO']['text']            # 2026-11-13 14:04 UTC, saved on the page, never sent
assert DB['SC-95']['text'] == HIS95 and DB['SC-DMSOb']['text'] == HIS_D2

BONNECHERE = 'https://pubmed.ncbi.nlm.nih.gov/42063954/'
LONGECITY = 'https://www.longecity.org/forum/viewtopic.php?t=1025608'
NEWPORT = 'https://pubmed.ncbi.nlm.nih.gov/25301680/'
VANITALLIE = 'https://pubmed.ncbi.nlm.nih.gov/15728303/'
PHILLIPS = 'https://pubmed.ncbi.nlm.nih.gov/30098269/'
LU = 'https://pubmed.ncbi.nlm.nih.gov/11421595/'
RAMIREZ = 'https://doi.org/10.1111/j.1749-6632.1967.tb34937.x'
JACOB = 'https://www.routledge.com/Dimethyl-Sulfoxide-DMSO-in-Trauma-and-Disease/Jacob-Torre/p/book/9781138894624'
MITRUS = 'https://pubmed.ncbi.nlm.nih.gov/29269805/'
KIMURA = 'https://pubmed.ncbi.nlm.nih.gov/2458858/'
BROWN = 'https://pubmed.ncbi.nlm.nih.gov/3356738/'
HANSLICK = 'https://pubmed.ncbi.nlm.nih.gov/19100327/'


def plain(md):
    return re.sub(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', md)


def cut(text, old):
    assert text.count(old) == 1, old[:50]
    return text.replace(old, '')


def swap(text, old, new):
    assert text.count(old) == 1, old[:50]
    return text.replace(old, new)


# ---- SC-95b: block 95 ----
OLD95 = ('You must pick one of two ketone strategies, because the salts in one bring their own sodium while the diet in '
         'the other drains it. If you\'re in a crisis and need the fog gone fast, there\'s Strategy A, the "Crisis Mode". '
         'You drink BHB (beta-hydroxybutyrate) salts and keep eating a standard low-sugar diet.')
H95_PD = ('And one study shows large improvement for Parkinson\'s, and [one woman\'s Alzheimer\'s was reversed] '
          '(https://www.longecity.org/forum/viewtopic.php?t=1025608).')
H95_PTSD = 'Data on ketones for PTSD specifically are sparse.'
H95_AMAZON = 'Amazon reviews do show many folks noting increased mental clarity, though.'
K95 = cut(cut(HIS95, ' ' + H95_PD), ' ' + H95_PTSD)
K95 = swap(K95, '(Bonnechère, et al, 2026)', '([Bonnechère, et al, 2026](%s))' % BONNECHERE)
assert K95.endswith(H95_AMAZON)

# ---- SC-54: block 54 ----
OLD54 = ('The Fix: If the brain is burning less sugar, we give it another fuel. Ketones are its backup fuel, and brains '
         'that take up less glucose (as in early Alzheimer\'s) still take up ketones normally ([Cunnane, et al, 2016]'
         '(https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2016.00053/text)). PQQ '
         'made mouse cells build more mitochondria, the parts of the cell that burn fuel ([Chowanadisai, et al, 2010]'
         '(https://pmc.ncbi.nlm.nih.gov/articles/PMC2804159)); whether it does that in the human brain hasn\'t been shown.')
N54_AD = ('And [one man\'s Alzheimer\'s improved markedly](%s) on coconut oil, and later on a ketone drink ([Newport, et '
          'al, 2015](%s)).' % (LONGECITY, NEWPORT))
N54_PD = ('In Parkinson\'s too, one small study with no comparison group showed large improvement on a ketogenic diet '
          '([VanItallie, et al, 2005](%s)).' % VANITALLIE)
N54_RCT = ('In a bigger trial against a low-fat diet, the keto diet eased fatigue, sleepiness and thinking problems more, '
           'but movement improved about the same on both ([Phillips, et al, 2018](%s)).' % PHILLIPS)
AT54 = 'still take up ketones normally ([Cunnane, et al, 2016](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2016.00053/text)).'
K54 = swap(OLD54, AT54, AT54 + ' ' + ' '.join([N54_AD, N54_PD, N54_RCT]))

# ---- SC-DMSOc: the DMSO item ----
D2 = [p.strip() for p in HIS_D2.split('\n\n')]
D1 = [p.strip() for p in HIS_D1.split('\n\n')]
assert len(D2) == 4 and len(D1) == 4, (len(D2), len(D1))
# M1: his 15:22 first paragraph (my SC-DMSOb sentences he kept), the links back on its two citations
M1 = swap(D2[0], '(Lu & Mattson, 2001)', '([Lu & Mattson, 2001](%s))' % LU)
M1 = swap(M1, '(Ramírez & Luza, 1967)', '([Ramírez & Luza, 1967](%s))' % RAMIREZ)
# M2: his 15:22 second paragraph, with his 14:04 transplant side effects and his own hedge
D1_KORTLEVE = ('There is evidence ([Kortleve, et al, 2023](https://assets-eu.researchsquare.com/files/rs-2624641/v1/'
               '45119f29-3464-4680-8468-490477ae59ae.pdf?c=1688109028)) that using too much DMSO (10% vs 5%) in stem '
               'cell transfusions increases mild side effects in adult humans.')
assert D1_KORTLEVE in D1[2]
H_USES = ('It is used for humans routinely in stem cell transplants and by many humans, including children, for all kinds '
          'of medical problems, as it treats hundreds of them ([Jacob & De La Torre, 2015](https://www.amazon.com/'
          'Dimethyl-Sulfoxide-DMSO-Trauma-Disease/dp/1498714676)).')
M_USES = ('It is used for humans routinely in stem cell transplants and by many humans for all kinds of medical '
          'problems, from arthritis to brain injuries ([Jacob & de la Torre, 2015](%s)).' % JACOB)
M_SIDE = D1_KORTLEVE.replace('[Kortleve, et al, 2023](https://assets-eu.researchsquare.com/files/rs-2624641/v1/'
                             '45119f29-3464-4680-8468-490477ae59ae.pdf?c=1688109028)',
                             '[Mitrus, et al, 2018](%s)' % MITRUS)
H_PTSD = 'No trial has tested it for PTSD, so for PTSD it rests on what people report, and many say it helps.'
M_PTSD = ('It hasn\'t been tested (that I know of, yet) specifically for PTSD, so for PTSD it rests on what people report, '
          'and many say it helps.')
assert '(that I know of, yet) specifically for' in D1[2]
M2 = swap(swap(D2[1], H_USES, M_USES + ' ' + M_SIDE), H_PTSD, M_PTSD)
# M3: his 15:22 third paragraph, the sheep the right way round and the rodents' condition named
H_SHEEP = ('Nebulized DMSO has been shown to prevent toxic cotton smoke from killing 4/6 sheep in one study ([Brown, et al, '
           '1988(https://pubmed.ncbi.nlm.nih.gov/3356738/)]).')
M_SHEEP = ('Nebulized DMSO with heparin (a blood thinner) has been shown to cut the lung damage from toxic cotton smoke in '
           'sheep ([Kimura, et al, 1988](%s)). In another study, the smoke killed all seven untreated sheep and four of '
           'the six given DMSO alone, while all seven given DMSO with heparin survived ([Brown, et al, 1988](%s)).'
           % (KIMURA, BROWN))
H_RODENT = 'It has shown some neurotoxic effects in other rodent studies under other conditions.'
M_RODENT = ('But it has shown some neurotoxic effects in rodent studies. In mice in their first month of life, even the '
            'smallest dose tested set off brain cell death, and the authors worried about the children who get it in '
            'transplants ([Hanslick, et al, 2009](%s)).' % HANSLICK)
D1_MOUSE = 'Translating mouse research to humans isn\'t straightfoward.'
assert D1_MOUSE in D1[3]
M3 = swap(swap(D2[2], H_SHEEP, M_SHEEP), H_RODENT, M_RODENT) + ' ' + D1_MOUSE.replace('straightfoward', 'straightforward')
# M4: his 15:22 fourth paragraph, with his 14:04 minute after nebulizing and his morning advice
D1_NEB = ('When I nebulize it, within a minute, my brain feels crystal clean and super blissed out (much more bliss than '
          'other routes).')
D1_MORNING = 'so it\'s best taken in the morning, and reduce the dose if you notice you\'re sleeping less.'
assert D1_NEB in D1[1] and D1_MORNING in D1[1]
H_JOIN = '(especially when nebulized), but when used too close to bedtime or too much, it can reduce sleep.'
M_JOIN = ('(especially when nebulized). ' + D1_NEB + ' But when used too close to bedtime or too much, it can reduce '
          'sleep, ' + D1_MORNING)
M4 = swap(D2[3], H_JOIN, M_JOIN)
DMSO = [M1, M2, M3, M4]
DMSO_TEXT = '\n\n'.join(DMSO)
BEFORE = 'The Dynorphin Bridge (Apathy / DAWS-pattern Void)'
AFTER = 'Magnesium Glycinate: 400mg (Night).'
# his own words in the item, for the receipts' "his": both his versions as he saved them
HIS_D_ALL = HIS_D1 + '\n\n' + HIS_D2
