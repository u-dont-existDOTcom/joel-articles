"""Fates for every heading the contents check or a reader flagged in his round-47 contents as it went into the guide
(lessons bad-trips-2026-11-21a/b): his picks stay his; the two that a reader could trip on go to him as questions."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
F5 = json.load(open(os.path.join(HERE, 'FATES-PICK6.json'), encoding='utf-8'))
HIS = 'kept: his pick in round 47; '
F = {
    'repeat:B102': HIS + '"brain" is the parent\'s topic word, and this names one case of it, in the words a friend hears',
    'repeat:R32-SEIZE': HIS + '"Seizure" repeats its parent\'s topic word but names its own part, what else helps; the '
                        'later picks\' "What Else May Help" read no better (one of two readers flagged each)',
    'repeat:B217': F5['repeat:B217'].replace('kept: ', HIS),
    'hard:B217': HIS + 'one reader of his contents found it close to "My Acute Rescue Remedies" above it, but the parent is '
                 'what to reach for and this is what to be careful with',
    'repeat:H54-CREATINE-H': HIS + 'it shares "brain" with "Humic Acid for the Brain" before it, and they are different '
                             'remedies for the same thing',
    'repeat:H54-MANGO-H': HIS + 'his "Chill Bliss" shares "bliss" with "Creatine for Brain & Bliss" before it; different '
                          'remedies, his playful words',
    'repeat:B189': HIS + 'his "Holy Water" shares only "water" with "Ocean Water Calms" before it; different remedies, which '
                   'his text compares',
    'repeat:B210': HIS + 'his pun ("Flushes") names how niacin ends a trip; Beach Morning Glory sits between it and its parent',
    'repeat:B410': F5['repeat:B410'].replace('kept: ', HIS),
    'hard:B166': ('kept: his own words for now, asked him in turn 58: "(Coffee Cherry for Brain also)" runs past the '
                  'sidebar\'s room ("(Coffee Cherry for Brain …"), so both readers couldn\'t tell what it is; "Coffee Cherry, '
                  'Brain Too" or "(Coffee Cherry, Brain Too)" fits'),
    'hard:B261': ('kept: his pick for now, asked him in turn 58: both readers read "Who to Contact, and When" as asking again '
                  'what "When to Get Outside Help" above it asks (the readers of my second pick found the same); "Who to '
                  'Contact" fits and keeps his words'),
    'hard:B332': HIS + 'his sign and his phrase; readers find it cryptic in the sidebar, and still opened it first for "someone '
                 'told me a bad trip is just shadow work"',
    'hard:B338': HIS + 'Fable\'s, which he picked over mine; "bypass" is what the section is about, as is the one before it on '
                 'spiritual ass-kicking',
    'hard:B347': HIS + 'his own words from his old heading; the metaphor is his',
    'hard:B96': F5['hard:B96'].replace('kept: ', HIS),
    'hard:N-SF-1': F5['hard:N-SF-1'].replace('kept: ', HIS),
}
json.dump(F, open(os.path.join(HERE, 'FATES-APPLIED.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(F))
