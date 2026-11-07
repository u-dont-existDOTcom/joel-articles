"""r22's check texts in the romance article (2026-11-07), each linted before its check (gate bad-trips-2026-11-07h).

r21 (../../r21/checks/RESULTS-r21.json): his S2 and S17 sections read Human, High whole; Romance 284 to 288 read Human
with every window High or Medium. Two missed:
- Jealousy 366 to 370 read 95% AI (#119). Cause: idiom stacking. Every sentence swapped a plain word for a stock idiom,
  and even his untouched 366 read AI Low beside it. This try (2 of 2) puts particular scenes where r21 had idioms ("say
  “she’s cute” about a woman at the next table", "who gets to stay the night", "an affair" for "an outside connection",
  "say “I can’t help myself” out loud" for "admit a lack of self-control"), brings his plain words back ("pretending",
  "ethical", "negotiate"), gives the last line its reason with "since", and keeps one idiom at most a sentence.
- Idealization 147 and 148 read 33.6% AI (#121): 148 AI Low, told as a general sequence. This try (3 of 6) joins the
  flip into one sentence the reader can follow ("first in private and then in front of everybody"), the rewriting into
  one with "until", and joins his quote in 147 into one sentence ("You’re perfect, I can’t find any flaw"), which
  Pangram cut at its full stop into two Low and Medium windows twice.
- Romance, the section (282 to 290) with r21's 285 to 287, which read Human by themselves (#120): its try 2 of 2,
  #98's text with only those three paragraphs changed."""
import importlib.util
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
R21 = HERE.parent.parent / 'r21' / 'checks'
_spec = importlib.util.spec_from_file_location('r21_texts', R21 / 'texts.py')
_r21 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_r21)
LIVE, NEW21 = _r21.LIVE, _r21.NEW

LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
PRED = {d['id']: d for d in map(json.loads, LEDGER.read_text(encoding='utf-8').splitlines()) if d.get('type') == 'prediction'}


def paras(t):
    return [p for p in re.split(r'\n\s*\n', t) if p.strip()]


NEW = {
    367: 'I’d rather be able to say “she’s cute” about a woman at the next table, and have my girlfriend say the same about '
         'some guy, without it turning into a fight. If only the serious crushes get mentioned, every mention turns '
         'into a confession, so people end up hiding all of them.',
    368: 'Plenty of couples vow to be together forever with nobody else, and far fewer actually live that way. In a '
         'polyamorous relationship the boundaries might be more negotiable, but then somebody has to sit down and '
         'negotiate them, down to who gets to stay the night.',
    369: 'Polyamory can be dishonest too: a lot of the time, I think people use it to cope because they can’t '
         'connect deeply with one person, or to say “I can’t help myself” out loud without necessarily doing the inner '
         'work that would make the arrangement ethical. If you can’t do monogamy, it’s more honest to say so, since '
         'pretending sometimes does more damage than an affair would have.',
    # The tell panel (../panel-ideal147/PANEL.md) agreed on 147's disclaimer and on 148's last two sentences: each
    # gets a fix, the disclaimer by its wording only.
    147: LIVE[147].replace('“You’re perfect. I can’t find any flaw,”', '“You’re perfect, I can’t find any flaw,”').replace(
        'I don’t mean this as a clinical diagnosis, but I use it almost diagnostically in my own life.',
        'I don’t mean it as a clinical diagnosis, but I do use it almost like one in my own life.'),
    148: 'When the BPD splitting happens, she can go from worshipping me to hating me, first in private and then in front '
         'of everybody. Suddenly she can find plenty of flaws, and all of them become evidence I was faking it all '
         'along. Sometimes she ends up accusing me of thinking I’m perfect, when she’s the one who used to say I was.',
}
assert NEW[147].count('almost like one') == 1 and '“You’re perfect, I' in NEW[147]
R98 = paras(PRED['romance-low-romance#98']['text'])
assert R98[2] == LIVE[284] and R98[6] == LIVE[288]

TEXTS = {
    'r22-jeal366': '\n\n'.join([LIVE[366], NEW[367], NEW[368], NEW[369], LIVE[370]]),
    'r22-ideal147': '\n\n'.join([NEW[147], NEW[148]]),
    'r22-romance': '\n\n'.join(R98[:3] + [NEW21[285], NEW21[286], NEW21[287]] + R98[6:]),
    # The jealousy stretch narrowed to its paragraphs first (E343; the ledger refused its try 2 until then): 367 and 369
    # by themselves; 368 (46 words, under the web app's 50) with 369, the paragraph that answers it (E349).
    'r22-jeal367': NEW[367],
    'r22-jeal368': '\n\n'.join([NEW[368], NEW[369]]),
    'r22-jeal369': NEW[369],
}

if __name__ == '__main__':
    for k, v in TEXTS.items():
        print(k, len(v.split()), 'words')
