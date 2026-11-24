#!/usr/bin/env python3
"""The Medium pass's outcome, paragraph by paragraph: for each section whose last try read Human High in every window,
its changed paragraphs, mapped to the post's paragraph numbers. A changed paragraph of model text goes into MINE-R37.json
(a layer of whole/build.py after HIS-S05.json); one with his own words (his page versions) goes to CARDS-T7.json for the
seventh marking page, with the check that read its section.

  python3 build_layer.py      ->  MINE-R37.json, CARDS-T7.json (the changes), and prints what went where
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
M = HERE / 'medium'
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
repl = {int(k): v for k, v in json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8')).items()}
post = {}
for line in (FIX / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        post[r['n']] = r['text']
cur = lambda n: repl.get(n, [post[n]])
plain = lambda t: re.sub(r'\[([^\]]+)\]\((?:[^()\s]|\([^()\s]*\))+\)', r'\1', t)


TAG = {}
for line in (FIX / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        TAG[r['n']] = r['tag']


def live_of(par):
    hits = [(n, i) for n in post for i, x in enumerate(cur(n)) if norm(plain(x)) == norm(par)]
    # a list item and the paragraph inside it hold the same words; the fixed version is built from the list item
    # (whole/fixed_md.py skips the paragraph), so the change goes on the list item
    if len(hits) == 2 and hits[1][0] == hits[0][0] + 1 and TAG.get(hits[0][0]) == 'LI':
        hits = hits[:1]
    assert len(hits) == 1, (par[:70], hits)
    return hits[0]


# section key: (the try that read High in every window, its check, {paragraph index: 'his' card id} for his words)
DONE = {
    'r36-07-can-casual-sex-or-a-situationship-actual': ('texts', 'https://www.pangram.com/history/d29e7a30-b543-45c9-a1af-c0eeeb7b3caf', {2: 'M-07'}),
    'r36-12-spirituality-to-bypass-intimacy-p1': ('texts', 'https://www.pangram.com/history/3063201e-8884-4008-b625-09bddfcfca7a', {}),
    'r36-16-and-deeper-is-the-point': ('t3', 'https://www.pangram.com/history/0b928214-0ed5-43e5-b495-f68bfc7028b9', {0: 'M-16'}),
    'r36-26-the-conversation-about-flaws': ('texts', 'https://www.pangram.com/history/39e78fb6-8b3e-4692-bec6-4cc4f261b23f', {3: 'M-26'}),
    'r36-28-my-flaws-p2': ('t3', 'https://www.pangram.com/history/bd788843-ff5f-417c-9242-5aeee7123f33', {1: 'M-28', 2: 'M-28', 3: 'M-28'}),
    'r36-30-beware-idealization-in-either-direction-p1': ('texts', 'https://www.pangram.com/history/00f004a8-9c64-4a96-9276-3d2458624496', {}),
    'r36-31-beware-idealization-in-either-direction-p2': ('texts', 'https://www.pangram.com/history/8d070089-ca59-4476-a372-f3fbe75cb711', {1: 'M-31', 2: 'M-31'}),
    'r36-35-if-slow-isn-t-realistic-for-you': ('texts', 'https://www.pangram.com/history/1867a533-baa4-4926-af33-d26bf54676fb', {2: 'M-35'}),
    'r36-41-the-relationship-as-crucible': ('texts', 'https://www.pangram.com/history/cb39187a-38cb-431c-a1ed-1af24036df11', {}),
    'r36-49-some-babies-grow-up-faster-p2': ('texts', 'https://www.pangram.com/history/892aceae-c811-45d4-9d4b-d915b0a6e7ca', {}),
    'r36-54-muses-directors-p1': ('t3', 'https://www.pangram.com/history/1b906fcb-7099-4a0e-8948-7d0db749969b', {2: 'M-54'}),
    'r36-68-two-pillars-don-t-hold-the-roof-up-p2': ('texts', 'https://www.pangram.com/history/231c824d-3dbe-44c5-be5d-3fe52fc88574', {2: 'M-68'}),
    'r36-71-which-marriage-vows-are-honest': ('texts', 'https://www.pangram.com/history/0be19217-8018-41f2-bd98-6d20fc089ac8', {}),
    'r36-77-doing-it-consciously-imagination-as-a-di-p2': ('texts', 'https://www.pangram.com/history/b0977a4a-7599-4289-ab03-9322ea1d97a7', {}),
    'r36-81-why-all-of-this-sounds-artificial': ('texts', 'https://www.pangram.com/history/ea848794-d8b1-456d-84a3-56fab928d798', {}),
    'r36-82-if-you-re-already-in-it-p1': ('texts', 'https://www.pangram.com/history/7a6a097c-d8a6-4c63-af8b-afd18d8193d8', {3: 'M-82'}),
    'r36-83-if-you-re-already-in-it-p2': ('texts', 'https://www.pangram.com/history/862385ed-24c1-44dd-aa3f-865e4b685b0a', {}),
}
EXTRA = json.loads((HERE / 'LATE.json').read_text(encoding='utf-8')) if (HERE / 'LATE.json').exists() else {}
for k, v in EXTRA.items():
    DONE[k] = (v[0], v[1], {int(a): b for a, b in v[2].items()})
mine, cards = [], {}
for key, (where, link, his) in DONE.items():
    old = [p for p in (FIX / 'r36' / 'checks' / ('CHECK-%s.txt' % key)).read_text(encoding='utf-8').split('\n\n')]
    new = [p for p in (M / where / ('%s.txt' % key)).read_text(encoding='utf-8').split('\n\n')]
    if len(old) == len(new):
        pairs = [(i, o, n) for i, (o, n) in enumerate(zip(old, new)) if o != n]
    else:  # 41: a one-line paragraph joined into the one before it
        assert len(old) == len(new) + 1, key
        j = next(i for i in range(len(new)) if old[i] != new[i])
        pairs = [(j, old[j], new[j]), (j + 1, old[j + 1], None)] + [
            (i + 1, o, n) for i, (o, n) in enumerate(zip(old[j + 2:], new[j + 1:]), start=j + 1) if o != n]
    for i, o, n in pairs:
        live, idx = live_of(o)
        before = cur(live)[idx]
        assert norm(plain(before)) == norm(o)
        ch = {'card': his.get(i, 'R37-%s-p%d' % (key[4:6], i + 1)), 'kind': 'para', 'live': live, 'before': before,
              'after': [n] if n is not None else [], 'his_checks': [link], 'section_key': key, 'paragraph': i + 1}
        if i in his:
            cards.setdefault(his[i], []).append(ch)
        else:
            ch['why'] = 'a sentence in a window that read Medium, fixed his way (lesson romance-2026-11-23i); the section then read Human High'
            mine.append(ch)
(HERE / 'MINE-R37.json').write_text(json.dumps({
    'about': 'My tested Medium-window fixes of 2026-11-24 (his message of 2026-11-23 23:49 UTC: "i often find the medium '
             'windows indicate other issues also"; lesson romance-2026-11-23i), model text only, each in a section that read '
             'Human High in every window afterwards (ledger batch romance-r37). A layer after r37/HIS-S05.json; the fixes '
             'of his own words are cards on the seventh marking page.',
    'whose': 'mine', 'changes': mine}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'CARDS-T7.json').write_text(json.dumps(cards, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('in:', len(mine), 'paragraph changes;', 'cards:', ', '.join('%s (%d)' % (c, len(v)) for c, v in cards.items()))
for c in mine:
    print('  live %d %s' % (c['live'], ('cut' if not c['after'] else c['after'][0][:70])))
