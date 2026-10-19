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


BA3 = os.environ.get('BA3', 'ba3-e')
AS4B = os.environ.get('AS4B', 'as4b-f')
AG5B = os.environ.get('AG5B', 'ag5b-c')
LOMED = os.environ.get('LOMED', 'lo-med-h')
LOSH1 = os.environ.get('LOSH1', 'lo-share1-j')
LOSH2 = os.environ.get('LOSH2', 'lo-share2-i')

after("Say they're the one who always remembers your appointments.", 'ba3',
      "PGQ-028 (support isn't a shortcut to romance), from %s: a paragraph of mine after his P2, so at the end of the h1 rather than right after P1 as the queue has it, since his P2's \"Say they're the one\" points back at P1's one person. experiments/t76-guide/drafts/%s.txt. @@BA3@@" % (Q76, BA3), BA3)
after('Jack Kornfield has a whole book on what comes next', 'as4b',
      "PGQ-032 (a drug peak that changes nothing; his example of 2026-10-14 23:26 UTC), from %s: a paragraph of mine right after the beautiful-state paragraph, where the queue has it, with no public figure named (question 64). experiments/t76-guide/drafts/%s.txt. @@AS4B@@" % (Q76, AS4B), AS4B)
after('Of course, that’s not to say you should not try to suffer less.', 'ag5b',
      "PGQ-033 (\"if only I had X\"), from %s: a short paragraph of mine after his P5, next to his gratitude part as the queue has it; the survey he remembered isn't cited, since no source has turned up (question 65). experiments/t76-guide/drafts/%s.txt. @@AG5B@@" % (Q76, AG5B), AG5B)
UE27 = os.environ.get('UE27', 'ue27-f')
UE29 = os.environ.get('UE29', 'ue29-b')
EMBED = '<!-- Native YouTube embed from source, unchanged: Garchen Rinpoche chanting Om Mane Pemme Hum'
register('ue2', lambda: para(EMBED),
         lambda: (para(EMBED) + '\n\n'
                  + note("PGQ-027 (urgent medical care during unbearable pain instead of a relief known to make it worse), from %s, checked against the guide's own paragraph (innerSignalGraph guides/inner-child-guide-2026-10-11-r6.txt, \"If the urge to escape comes during severe physical pain\"): a paragraph of mine at the end of this h3 rather than right after P1 as the queue has it, since P2's \"So why not just blast right past that part\" points back at P1's hurt; it opens on the urge to escape by name, and its last sentence sends only a fear of acting, or not knowing whether you're safe, to If You Want to Kill Yourself (the grounding's MUST, experiments/t76-guide/GROUNDING-t76.md). experiments/t76-guide/drafts/%s.txt. @@UE27@@" % (Q76, UE27)) + draft(UE27) + '\n\n'
                  + note("PGQ-029 (frequent severe pain: a specialist and a written flare plan, with the new or severe signs that still mean going in), from %s and the guide's next paragraph (\"If severe pain attacks happen almost every day\"); the France example compressed, as the queue asks. experiments/t76-guide/drafts/%s.txt. @@UE29@@" % (Q76, UE29)) + draft(UE29))
         if para(EMBED) else None)
register('lo', lambda: para("And reaching out doesn't mean telling strangers everything."),
         lambda: (para("And reaching out doesn't mean telling strangers everything.") + '\n\n'
                  + note("PGQ-030 (medical agency after coercive or harmful care), from %s: a paragraph of mine right after the graded-disclosure paragraph, where the queue has it. experiments/t76-guide/drafts/%s.txt. @@LOMED@@" % (Q76, LOMED)) + draft(LOMED)
                  + ('' if os.environ.get('LOSH', '1') == '0' else '\n\n' + note("PGQ-039 (before sharing something legally or personally sensitive), from %s and the passage drafted in innerSignalGraph issue #180: two paragraphs of mine after PGQ-030's, merged with it and with PGQ-003 rather than repeating them, as the queue asks. No law or country is named; legal review before publishing is question 67. experiments/t76-guide/drafts/%s.txt and %s.txt. @@LOSH@@" % (Q76, LOSH1, LOSH2)) + draft(LOSH1) + '\n\n' + draft(LOSH2)))
         if para("And reaching out doesn't mean telling strangers everything.") else None)

HERO6 = os.environ.get('HERO6', 'hero6-e')
CS57X = os.environ.get('CS57X', 'cs57x-a')
after("Whichever stage you're at, saying the right thing", 'cs57',
      "PGQ-037 (reparenting isn't an exercise), from %s: a short paragraph of mine after my PGQ-012 paragraph, since the queue's place (after the guide's \"Reparenting begins when the present-day person occupies an adult position\") isn't in the article, and three versions of these sentences inside the PGQ-012 paragraph made it read AI alone (rounds t76a to t76c). The queue asks for one or two sentences; at 42 words it's under the gate's 50, so its check is the h1's. experiments/t76-guide/drafts/%s.txt. @@CS57@@" % (Q76, CS57X), CS57X)
after('After the day, look at what actually happened.', 'hero6',
      "PGQ-038 (keeping yourself safe is part of the work), from %s: a short paragraph of mine at the end of this h2, since the queue's place, right after \"Warmth can come later.\", is inside P3 here, and P4 picks up P3's last word; it keeps the guide's permission not to call it reparenting (\"if you like seeing it that way\"). The queue asks for one or two sentences; at 49 words it's under the gate's 50, so its check is the h2's and the h1's; four longer versions read AI alone (rounds t76a to t76c). experiments/t76-guide/drafts/%s.txt. @@HERO6@@" % (Q76, HERO6), HERO6)
