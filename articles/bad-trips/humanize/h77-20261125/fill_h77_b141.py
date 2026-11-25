"""The gut-driven paragraph's part of fill_h77.py: its sentences, sources and what the reads of its first draft marked."""
POST = 'his post as of 2026-11-03 (original.md), the paragraph as it stood in the guide before this turn'
PAY141 = {
    'If a trip comes with diarrhea': ('they know the signs that point to the gut or the brain as what is making the mind feel crazy',
                                      'the body reasons the paragraphs before it give', None),
    'Those trips are what the remedies': ('they know which part of the guide to use: the remedies below for those trips, the shadow work further down for a mainly emotional crisis',
                                          'the trips with those signs, just described', 'Those trips'),
    'A gut-driven mental hell is often': ('they know the two get mixed up, so they check the gut before treating a mental hell as shadow work',
                                          'the shadow work, just named', 'A gut-driven mental hell'),
}
SRC141 = [
    {'point': 'a trip with diarrhea, nausea, toxic heaviness, a dirty body-feeling, loss of bodily control, jaw tension, neurological disorganization, or the sense that the mind is going crazy because the gut or brain is going crazy belongs in a different branch from a mainly emotional crisis',
     'found': (POST + '; every sign stays, in his words. "A different branch" named nothing a reader can see: the branch is the '
               'remedies this section lists, and the other is the shadow work in the sections after it (his line R27-HIER, two '
               'paragraphs up: "The hierarchy appears before the mystical sections")'),
     'still_needed': 'yes: they choose between treating the body with the remedies below and working with the feeling', 'fate': 'changed'},
    {'point': 'a gut-driven mental hell is often mistaken as shadow work',
     'found': POST + '; his own line, on the keep-as-is list (K2, round 1, card RP-4), so it stays word for word as the paragraph\'s last sentence. My second try joined it to the sentence before; `keep_as_is.py` caught that when the try was applied, and the try was taken back out (lesson bad-trips-2026-11-25o)',
     'still_needed': 'yes: they check the gut before they treat a mental hell as shadow work', 'fate': 'kept'},
]
NOTE141 = ('the three fresh reads and the tell panel on his post\'s text (reads/*-asis-rescue-sec.txt, panel-b141/PANEL.md: both '
           'sentences agreed), then three fresh reads on my first draft (reads/*-a1-rescue-sec.txt). Changed from their marks: '
           '"That" is "Those trips"; the verb the first sentence left unsaid is back ("is going crazy", his words), and "only" is out, '
           'which read as "nothing to worry about". Kept: his last line, word for word (keep-as-is K2), the run of '
           'signs, each his post\'s, and "a mainly emotional crisis". Not answered, because the section doesn\'t hold it: what a '
           'friend would see for "loss of bodily control" and "neurological disorganization", and how to tell a gut-driven mental '
           'hell from an emotional crisis in the moment. Those are his to give, so they are his question on round 59 '
           '(lesson bad-trips-2026-11-25a)')
UNNEEDED141 = {}
