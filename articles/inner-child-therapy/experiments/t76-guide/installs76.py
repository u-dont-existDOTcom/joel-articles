# Turn 76 installs (registered with register(name, old, new); see t76.py). Joel's message of 2026-10-19 00:55 UTC
# (experiments/t76-answers/JOEL-20261019-0055.md): "start workin on the innerSignalGraph queue i guess". The queue is
# innerSignalGraph's authoring/PENDING-PUBLIC-GUIDE-CHANGES.md, version 2026-10-18-r12, at 55b2b0dd.

SAID76 = 'his message of 2026-10-19 00:55 UTC (experiments/t76-answers/JOEL-20261019-0055.md), "start workin on the innerSignalGraph queue"'
Q76 = "innerSignalGraph's queue, version 2026-10-18-r12 (authoring/PENDING-PUBLIC-GUIDE-CHANGES.md at 55b2b0dd)"


def note(text):
    return '<!-- Turn 76 (%s): %s -->\n\n' % (SAID76, text)


def after(start, name, text, stem):
    """Register NAME: the paragraph (or comment line) starting with START, then a new paragraph: TEXT's note and STEM."""
    register(name, lambda: para(start), lambda: para(start) + '\n\n' + note(text) + draft(stem) if para(start) else None)


BA3 = os.environ.get('BA3', 'ba3-b')
AS4B = os.environ.get('AS4B', 'as4b-d')
AG5B = os.environ.get('AG5B', 'ag5b-b')
UE2 = os.environ.get('UE2', 'ue2-a')
LOMED = os.environ.get('LOMED', 'lo-med-b')
LOSH1 = os.environ.get('LOSH1', 'lo-share1-c')
LOSH2 = os.environ.get('LOSH2', 'lo-share2-c')

after("Say they're the one who always remembers your appointments.", 'ba3',
      "PGQ-028 (support isn't a shortcut to romance), from %s: a paragraph of mine after his P2, so at the end of the h1 rather than right after P1 as the queue has it, since his P2's \"Say they're the one\" points back at P1's one person. experiments/t76-guide/drafts/%s.txt. @@BA3@@" % (Q76, BA3), BA3)
after('Jack Kornfield has a whole book on what comes next', 'as4b',
      "PGQ-032 (a drug peak that changes nothing; his example of 2026-10-14 23:26 UTC), from %s: a paragraph of mine right after the beautiful-state paragraph, where the queue has it, with no public figure named (question 64). experiments/t76-guide/drafts/%s.txt. @@AS4B@@" % (Q76, AS4B), AS4B)
after('Of course, that’s not to say you should not try to suffer less.', 'ag5b',
      "PGQ-033 (\"if only I had X\"), from %s: a short paragraph of mine after his P5, next to his gratitude part as the queue has it; the survey he remembered isn't cited, since no source has turned up (question 65). experiments/t76-guide/drafts/%s.txt. @@AG5B@@" % (Q76, AG5B), AG5B)
after('<!-- Native YouTube embed from source, unchanged: Garchen Rinpoche chanting Om Mane Pemme Hum', 'ue2',
      "PGQ-027 and PGQ-029 (urgent medical care for unbearable pain instead of a relief known to make it worse; a specialist pathway and a written plan for frequent severe pain, with urgent care as the backup), from %s: one paragraph of mine at the end of this h3 rather than right after P1 as the queue has it, since P2's \"that part\" points back at P1; the France example is compressed, as the queue asks, and the last sentence points to If You Want to Kill Yourself for immediate danger. experiments/t76-guide/drafts/%s.txt. @@UE2@@" % (Q76, UE2), UE2)
register('lo', lambda: para("And reaching out doesn't mean telling strangers everything."),
         lambda: (para("And reaching out doesn't mean telling strangers everything.") + '\n\n'
                  + note("PGQ-030 (medical agency after coercive or harmful care), from %s: a paragraph of mine right after the graded-disclosure paragraph, where the queue has it. experiments/t76-guide/drafts/%s.txt. @@LOMED@@" % (Q76, LOMED)) + draft(LOMED) + '\n\n'
                  + note("PGQ-039 (before sharing something legally or personally sensitive), from %s and the passage drafted in innerSignalGraph issue #180: two paragraphs of mine after PGQ-030's, merged with it and with PGQ-003 rather than repeating them, as the queue asks. No law or country is named; legal review before publishing is question 67. experiments/t76-guide/drafts/%s.txt and %s.txt. @@LOSH@@" % (Q76, LOSH1, LOSH2)) + draft(LOSH1) + '\n\n' + draft(LOSH2))
         if para("And reaching out doesn't mean telling strangers everything.") else None)

CS57 = os.environ.get('CS57', 'cs57-c')
HERO6 = os.environ.get('HERO6', 'hero6-a')
register('cs57', lambda: para("Whichever stage you're at, saying the right thing"),
         lambda: note("PGQ-037 (reparenting isn't an exercise), from %s: two sentences of mine at the end of my PGQ-012 paragraph, since the queue's place (after the guide's \"Reparenting begins when the present-day person occupies an adult position\") isn't in the article; this paragraph already says the session isn't enough, as the queue asks when PGQ-012 is in. experiments/t76-guide/drafts/%s.txt. @@CS57@@" % (Q76, CS57)) + draft(CS57)
         if para("Whichever stage you're at, saying the right thing") else None)
after('After the day, look at what actually happened.', 'hero6',
      "PGQ-038 (keeping yourself safe is part of the work), from %s: a paragraph of mine at the end of this h2, since the queue's place, right after \"Warmth can come later.\", is inside P3 here, and P4 picks up P3's last word; it keeps the guide's \"if that way of putting it fits you\" (Also Look Outward). experiments/t76-guide/drafts/%s.txt. @@HERO6@@" % (Q76, HERO6), HERO6)
