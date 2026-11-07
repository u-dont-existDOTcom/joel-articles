"""r26's check text in the romance article (2026-11-07), linted before its check (gate bad-trips-2026-11-07h).

The jealousy section read 26% AI with r22's 367 and r23's 368 and 369 (#133), though each read Human by itself. A fresh
reader read the live 367 to 369 for sense before they went on a card to Joel (gate bad-trips-2026-11-07i;
../../../../review/teach-20261107/SENSE-T2.md) and found the links between them missing: 367's "I would rather" has no
alternative and never says to whom the attractions are mentioned; the step from "only serious ones" to "a major event" is
missing; 368 jumps from disclosure to promises to polyamory; "negotiable means negotiating is required" doesn't follow;
369 rebuts a claim nobody made, its "too" points at a dishonesty only implied, and "a way to admit a lack of
self-control" contradicts its own point (admitting is honest). That is a cause my tries hadn't touched: each paragraph
made sense alone, and the three didn't follow one another (E355). This try puts each link in words:
- 367 ties to 366 ("For that to stay honest") and says the missing step ("then any mention sounds serious");
- 368 says the dishonesty 369's "too" points back to ("so a lot of them end up pretending") and why polyamory's
  boundaries need negotiating ("Polyamory leaves those rules open");
- 369 makes the second case the dishonest one it is (someone who can't stop cheating "just renames it polyamory") and
  says what "saying so" means ("say so up front than to promise it and pretend").
The whole section, after the fix (its two tries spent)."""
import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r25_texts', HERE.parent.parent / 'r25' / 'checks' / 'texts.py')
R25 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R25)
LIVE = R25.R24.LIVE
NEW = {
    367: 'For that to stay honest, I’d rather we could both mention attractions to other people casually, like saying '
         '“she’s cute” about a woman at the next table. If only the serious ones ever get mentioned, then any mention '
         'sounds serious, and people stop mentioning them at all.',
    368: 'Lots of couples promise forever and nobody else, and far fewer actually live that way, so a lot of them end up '
         'pretending. Polyamory leaves those rules open, so the boundaries have to be negotiated out loud, '
         'down to who gets to stay the night.',
    369: 'Polyamory can be dishonest too, though, like when someone who can’t get close to any one person dates four at '
         'once and calls it polyamory. Or when someone who can’t stop cheating just renames it polyamory, without '
         'necessarily doing the work on themselves that would make it ethical. Still, if you can’t do monogamy, it’s more '
         'honest to say so up front than to promise it and pretend, since pretending can do more damage than an affair '
         'would have.',
}
TEXTS = {'r26-jeal': '\n\n'.join(R25.R83[:10] + [NEW[367], NEW[368], NEW[369], LIVE[370]])}
