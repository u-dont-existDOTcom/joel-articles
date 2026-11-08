"""SC-106b, the potassium card again (2026-11-08, after his answer of 15:45 UTC on x1108c: SC-106 to revise, with GPT's
critique of it). Each of GPT's points was checked against its source through PubMed (SCIENCE-P23.md, "SC-106 revised"):
its facts hold; my card had stated one patient's arm and leg nerves in severe hypokalemia as what "nerve cells" do, and
assumed the potassium around the brain's neurons follows the blood's. The brain holds its own (Hladky & Barrand 2016),
so neither the drop stress brings to the blood nor what you eat sets the KCNQ brakes; what holds for eating potassium
is blood pressure (Aburto 2013), which the salts of Strategy A make worth watching (block 102).

Each entry: the block's opening (to find it), the swap inside it (or a cut: the whole block goes), and what the
paragraph is for (the needed read's WHAT IT IS FOR). Lessons neuro-2026-11-08g to j.
"""
import texts_p23 as P

BROWN = P.BROWN
ABURTO = 'https://pubmed.ncbi.nlm.nih.gov/23558164/'
HLADKY = 'https://pubmed.ncbi.nlm.nih.gov/27799072/'
BIERVERT = 'https://pubmed.ncbi.nlm.nih.gov/9430594/'
GORJI = 'https://pubmed.ncbi.nlm.nih.gov/11454323/'
JAVAHERI = 'https://pubmed.ncbi.nlm.nih.gov/7302394/'
TORRES = 'https://pubmed.ncbi.nlm.nih.gov/18466657/'
KUWABARA = P.KUWABARA
CAMPESE = P.CAMPESE

OLD106 = ('The Science: Your neurons have "brakes" called KCNQ channels that stop them from firing uncontrollably. These '
          'brakes run on Potassium ions. If you are low on potassium (common in high stress), your brakes fail. You can '
          'push the pedal (breathe), but the car won\'t stop.')
# the fresh reader's needed read (needed/sp106b/READ.md) said the second sentence of the version it read isn't needed
# once the brakes story is gone; it is cut, and what it said is on the card
READ106 = ('The Science: Eating more potassium brings high blood pressure down ([Aburto, et al, 2013](%s)), which matters on '
           'Strategy A, since its salts bring their own sodium. It won\'t calm your nerves, though, because your brain keeps '
           'the potassium around its neurons within tight limits, whatever your blood is doing ([Hladky & Barrand, '
           '2016](%s)), even when stress lowers the potassium in your blood by pushing it into your cells ([Brown, et al, '
           '1983](%s)).' % (ABURTO, HLADKY, BROWN))
NEW106 = ('The Science: Eating more potassium brings high blood pressure down ([Aburto, et al, 2013](%s)), which matters on '
          'Strategy A, since its salts bring their own sodium.' % ABURTO)

T = [
    dict(key='SP104', start='Goal: Install the "Brake Pads"', cut=True,
         for_='the label named the brakes story; with potassium there for blood pressure, the label goes'),
    dict(key='SP105', start='Mechanism: Potassium Channels (KCNQ)', cut=True,
         for_='the label named the mechanism that doesn\'t hold; it goes with it'),
    dict(key='SP106B', start='The Science: Your neurons have "brakes" called KCNQ channels', swap=[(OLD106, NEW106)],
         for_='the reader on Strategy A (BHB salts with a standard diet) learns why to eat potassium-rich food, before the '
              'target and the foods'),
    dict(key='SP115D', start='The Strategy: Eat 2 large potatoes',
         swap=[(' This saturates your cells, lowering your "resting voltage" so you become physically harder to trigger.', '')],
         for_='the reader knows how to reach the potassium target with food'),
]

plain = P.plain
