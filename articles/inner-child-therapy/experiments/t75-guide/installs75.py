# Turn 75 installs (registered with register(name, old, new); see t75.py). Joel's answer of 2026-10-19 00:26 UTC
# (experiments/t75-answers/JOEL-20261019-0026.md): "63a".

SAID75 = 'his answer of 2026-10-19 00:26 UTC (experiments/t75-answers/JOEL-20261019-0026.md)'


def note(text):
    return '<!-- Turn 75 (%s): %s -->\n\n' % (SAID75, text)


register('fat4b', lambda: para('Before choosing a therapist, get to know the strengths and pitfalls of their approach'),
         lambda: note('63, A: one sentence of mine added to his P4, after his spiritual-experiences sentence, for his guide\'s safety points that the removed IFS P8 carried ("a skilled, grounded, trauma-informed IFS therapist who isn\'t suggestive may help, especially one who understands dissociation"). The rest is his, word for word. experiments/t75-guide/drafts/fat4-b.txt. @@FAT4@@') + draft('fat4-b'))
