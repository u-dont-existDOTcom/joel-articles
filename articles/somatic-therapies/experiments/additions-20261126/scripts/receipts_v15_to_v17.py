import re
s = open('fill_receipts_v15.py').read()
def rep(old, new, cnt=1):
    global s
    assert old in s, old[:90]
    s = s.replace(old, new, cnt)
rep("ADDITIONS-15.json", "ADDITIONS-16.json"); rep("INNER-CHILD-ADDS-6.json", "INNER-CHILD-ADDS-7.json")
rep("'texts' / 'v15', HERE / 'receipts' / 'v15'", "'texts' / 'v16', HERE / 'receipts' / 'v16'")
s = s.replace('fill_receipts_v15', 'fill_receipts_v16').replace('for draft 15 of the somatic', 'for draft 16 of the somatic').replace("sixth draft (INNER", "seventh draft (INNER")
start = s.index("    'A1-S1': ("); end = s.index("    'A3-S1': (")
a1 = '''    'A1-S1': ("they place themselves: by this point in the guide they can feel their body", "it opens the section on where "
              "the reader stands after the layers before", N1 + 'a new section, on where the reader stands by now'),
    'A1-S2': ("they recognize whether they are the one who slips away from a feeling, and the two ways it shows",
              "it names the problem that remains for some readers who can feel their body", 'You might still'),
    'A1-S3': ("they get the first therapy to look into and what its therapist actually says and asks when they slip away",
              "it answers the case the sentence before described", 'In Intensive Short-Term Dynamic Psychotherapy'),
    'A1-S4': ("they learn that anxiety about the feeling is behind the slipping away, and that the therapist watches for it "
              "so it doesn't get to be too much", "it says what the therapy watches while it presses toward the feeling",
              "It's usually anxiety about the feeling"),
    'A1-S5': ("they know a slower version exists, that it's the usual one, and what it does when the anxiety climbs",
              "it says what happens when the anxiety the sentence before named is too much",
              'If you can only take a little of that anxiety'),
    'A1-S6': ("they recognize the second case, one feared feeling, and get the therapy for it and how it works",
              "it turns from slipping away from any feeling to fearing one",
              N1 + 'the next case, the second of the therapies the section promised'),
    'A1-S7': ("they recognize the third case, kindness that bounces off, and get the therapy's name",
              "it gives the next case after the feared feeling", 'And if'),
    'A1-S8': ("they picture what a session asks of them and how it works on the kindness that bounces off",
              "it says what the therapy just named does", 'The therapist'),
    'A1-S9': ("they learn the risk the three share: being steered back to feelings can get to be too much",
              "after the three therapies, it says what they have in common that matters before booking",
              N1 + 'what the three have in common, after each was described'),
    'A1-S10': ("they get the questions to ask before booking, in the guide's water-therapy form",
               "it says what to ask because of the risk the sentence before named", 'So before booking'),
    'A1-S11': ("they know which answer to look for", "it says how to judge the answer to the question", "I'd want them"),
'''
s = s[:start] + a1 + s[end:]
start = s.index("    'IC2-S1': ("); end = s.index("}\n\nISTDP = ")
ic2 = '''    'IC2-S1': ("they get two therapies to look into while the tests keep coming back normal, without stopping the search, "
               "and hear that neither calls the pain imaginary", "it follows the advice not to stop investigating with what "
               "to do meanwhile", 'While the investigation goes on'),
    'IC2-S2': ("they know where to read about both, their trials and how far they reach", "it points to the details, in his "
               "own pointer form from the same section", 'More on both'),
    'H-S1': ("they know what to ask a specialist for, including when to go to the ER, and not to stop looking for the cause",
             "it is his advice on the pain the section describes", N1 + 'his advice, after the attacks he describes'),
'''
s = s[:start] + ic2 + s[end:]
rep("PARAS['IC2'] = plain(IC['IC2']['add'])", "PARAS['IC2'] = plain(IC['IC2']['add'])\nPARAS['H'] = IC['IC2']['his_before']")
rep("""('J', ['J']), ('IC1', ['IC1']), ('IC2', ['IC2'])""", """('J', ['J']), ('IC1', ['IC1']), ('IC2', ['IC2']), ('H', ['H'])""")
# the APT sentence is A1-S6 now: rename in the marks and keeps
i = s.index("NEAR = ("); j = s.index("Q = {")
block = s[i:j].replace("'A1-S5'", "'A1-S6'").replace("SID['A1-S5']", "SID['A1-S6']")
s = s[:i] + block + s[j:]
rep('''"Even once you can feel your body just fine", "If it\\'s '
                  'one feeling"''', '''"By this layer you can probably feel your body just fine", "If '
                  'it\\'s one feeling"''')
rep('''"For that", "It\\'s usually anxiety about the feeling", "If you can only '
                  'handle", "And if", "Since in all three", "If there\\'s no room"''', '''"You might still", "In Intensive Short-Term '
                  'Dynamic Psychotherapy", "If you can only take", "And if", "So before booking", "I\\'d want them"''')
rep("""Q2='PASS: look into the '
                  'therapy; ask what they do when you get overwhelmed and what happens if you say they read you wrong; '
                  'keep looking if there\\'s no room'""", """Q2='PASS: look into the '
                  'therapy; ask what happens if you get overwhelmed or think they have your feelings wrong; want to hear '
                  'they would slow down and listen'""")
i = s.index("    'IC2': dict(Q1="); j = s.index("Q7='PASS: the reader whose tests come back normal'", i)
s = s[:i] + """    'IC2': dict(Q1='PASS: when first ("While the investigation goes on, if the tests keep coming back normal"), then the act',
                Q2='PASS: ask a specialist for a plan; look into the two; read more in the somatic guide', Q3='PASS: "two '
                   'talk therapies", named', Q4='PASS: "talk therapies that treat the pain as real" says what kind of thing '
                   'they are', Q5='PASS: "While the investigation goes on" picks up his sentence before; "More on both" the '
                   'two named', Q6='PASS: his advice, then what to do meanwhile, then where to read more', """ + s[j:]
start = s.index("TEXTS = {"); end = s.index("\n}\n", start) + 2
texts = '''TEXTS = {
    'A1-P1': dict(paras=['A1-P1'], part='A1', reader=A1R, checked=['istdp'],
                  placement='first in the new section at the end of Layer 3, after Brainspotting\\'s further reading',
                  same='none: read the section from its heading to the next; the other paragraphs say how ISTDP keeps it '
                       'bearable, the other two therapies, and what to ask'),
    'A1-P2': dict(paras=['A1-P2'], part='A1', reader=A1R, checked=['istdp'],
                  placement='after the paragraph that names the first therapy; its "also" adds the watching to the catching',
                  same='none: read the section from its heading to the next; only this paragraph says what keeps ISTDP bearable'),
    'A1-P5': dict(paras=['A1-P5'], part='A1', reader=A1R, checked=['istdp', 'apt', 'aedp'],
                  placement='last in the section, after the three therapies; "All three" points to them',
                  same='none: read the section from its heading to the next; the questions are asked once, here'),
    'IC1': dict(paras=['IC1'], part='IC1', reader=ICR1, checked=['imrs'],
                placement='a paragraph of its own at the end of Re-do Trauma Memories, after his J. paragraph, so his '
                          '"For example" story still follows the reliving it illustrates',
                same='none: read the section from its heading to the next; no other paragraph names the clinical therapy'),
    'IC2-PAIR': dict(paras=['H', 'IC2'], part='IC2', reader=ICR2, checked=['real'],
                     placement='a paragraph of its own at the end of Physical Pain? (41 words, so checked with his paragraph '
                               'before it), after his advice not to stop the investigation; its "While the investigation goes '
                               'on" points to that',
                     same='none: read the section from its heading to the next; no other paragraph names these therapies'),
    'A3-P1P2': dict(paras=['A3-P1', 'A3-P2'], part='A3', reader=A3R, checked=['prt'],
                    placement='the opening of the new section (36 words, so checked with the paragraph after it) and the '
                              'first therapy', same='none: read the section from its heading to the next; only these say '
                              'whose pain it is for and what PRT does'),
}
'''
s = s[:start] + texts + s[end:]
open('fill_receipts_v16.py', 'w').write(s)
print('ok')
