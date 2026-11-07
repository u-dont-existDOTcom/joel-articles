"""r23's check texts in the romance article (2026-11-07), each linted before its check (gate bad-trips-2026-11-07h).

r22 (../../r22/checks/RESULTS-r22.json): the Romance section read Human with every window High or Medium (#122), and
Idealization 147 with 148 read Human, High and Medium (#123). Jealousy, narrowed to its paragraphs: 367 read Human
(Medium, then Low on its second sentence); 368 with 369 read 100% AI (#125), 369 alone AI Medium (#126). Cause: the
essay shape, a claim with two abstract reasons joined by "or" and a verdict, which taking the idioms out didn't touch.
- Jealousy 369: each reason told as what some people do, the way his S2 told the monks' reasons ("dates four at once and
  calls it polyamory"; "keeps cheating until they finally announce they’re poly").
- Jealousy 368: its first sentence followed by something for the reader to look at ("Look around at how many actually
  live that way").
- Jealousy 367: its Low second sentence joined to the first as its reason.
- Idealization, the section (143 to 151) with r22's 147 and 148: its try 2 of 2, #92's text with only those two changed."""
import importlib.util
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


R22 = load('r22_texts', HERE.parent.parent / 'r22' / 'checks' / 'texts.py')
LIVE = R22.LIVE
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
PRED = {d['id']: d for d in map(json.loads, LEDGER.read_text(encoding='utf-8').splitlines()) if d.get('type') == 'prediction'}
R92 = [p for p in re.split(r'\n\s*\n', PRED['romance-low-ideal#92']['text']) if p.strip()]
assert R92[4] == LIVE[147]

NEW = {
    367: 'I’d rather be able to say “she’s cute” about a woman at the next table, and have my girlfriend say the same about '
         'some guy, without it turning into a fight, because if only the serious crushes ever get mentioned, every crush '
         'you do mention feels like a confession, and people start hiding them all.',
    368: 'Lots of couples promise forever and nobody else. Look around at how many actually live that way. In a '
         'polyamorous relationship the boundaries might be more negotiable, but then somebody has to sit down and '
         'negotiate them, down to who gets to stay the night.',
    369: 'Polyamory can be dishonest too, like when someone who can’t get close to any one person dates four at once and '
         'calls it polyamory. Or when someone keeps cheating until they finally announce they’re poly, without necessarily '
         'doing the work on themselves that would make it ethical. If you can’t do monogamy, say so, since pretending '
         'can do more damage than an affair would have.',
}
TEXTS = {
    'r23-jeal367': NEW[367],
    'r23-jeal368': '\n\n'.join([NEW[368], NEW[369]]),
    'r23-jeal369': NEW[369],
    'r23-ideal': '\n\n'.join(R92[:4] + [R22.NEW[147], R22.NEW[148]] + R92[6:]),
}

if __name__ == '__main__':
    for k, v in TEXTS.items():
        print(k, len(v.split()), 'words')
