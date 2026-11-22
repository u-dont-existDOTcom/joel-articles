#!/usr/bin/env python3
"""update_owner_edits.py - the OWNER-EDITS entries that pinned a heading's old words, brought in line with his round-47
picks (apply_r47.py), and the round's own entries added. A pinned heading line (in must_contain, must_contain_exact or
order) is found in the guide as it was before round 47 (git HEAD's blocks) and becomes the same block's heading now; a
pinned phrase his pick took out of a heading is said in the entry's "changed" note, with where the text still says it.

  python3 articles/bad-trips/review/r47/update_owner_edits.py        (from the repo root, after apply_r47.py)
"""
import json, pathlib, subprocess

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
OE = ART / 'OWNER-EDITS.json'
NOTE = '2026-11-21 (turn 58): headings renamed by his round-47 picks (review/r47/apply_r47.py)'
DROPPED = {
    'DMSO + Humic Acid + Electrolytes First': (
        'his round-47 pick for the heading is "\\"My Brain Feels Damaged\\"" (my pick, kept): the heading\'s "DMSO + Humic Acid + '
        'Electrolytes First" went with it, and the section\'s first paragraph (B103) still says it: DMSO first, then '
        'smelling humic acid, then electrolytes to drink'),
}


def main():
    old = json.loads(subprocess.run(['git', 'show', 'HEAD:articles/bad-trips/GUIDE-SO-FAR-blocks.json'], cwd=REPO,
                                    capture_output=True, text=True, check=True).stdout)
    new = {b['id']: b['md'] for b in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}
    heads = [(b['id'], b['md']) for b in old if b['md'].startswith('#')]
    guide = (ART / 'GUIDE-SO-FAR.md').read_text(encoding='utf-8')

    def renamed(s):
        """The heading line s pinned (or a start of it), as the same block's heading reads now; None if s is no heading."""
        if not s.startswith('#'):
            return None
        first = s.split('\n', 1)
        hits = [bid for bid, md in heads if md.startswith(first[0])]
        if len(hits) != 1 or hits[0] not in new:
            return None
        if new[hits[0]] == heads[[h[0] for h in heads].index(hits[0])][1]:
            return None
        return new[hits[0]] + ('\n' + first[1] if len(first) > 1 else '')

    oe = json.loads(OE.read_text(encoding='utf-8'))
    changed = []
    for e in oe['entries']:
        touched = False
        for field in ('must_contain', 'must_contain_exact', 'order'):
            vals = e.get(field)
            if not vals:
                continue
            out = []
            for s in vals:
                if s in DROPPED:
                    e.setdefault('changed', []).append(NOTE + ': ' + DROPPED[s])
                    touched = True
                    continue
                r = renamed(s) if s not in guide or field == 'order' else None
                if r and r != s:
                    out.append(r)
                    touched = True
                else:
                    out.append(s)
            e[field] = out
        if touched:
            if NOTE not in e.setdefault('changed', []):
                e['changed'].append(NOTE)
            changed.append(e['id'])
    ids = {e['id'] for e in oe['entries']}
    for entry in [
        {'id': 'r47-headings', 'status': 'applied',
         'what': ('his headings for Substack\'s contents sidebar: 11 in his own words, Fable\'s "The Feel-Good Bypass", the '
                  'rest my pick; "How To Check For SS" in title case, his rule; the links a heading carried kept on its '
                  'words or moved to the same words in its text (review/r47/apply_r47.py)'),
         'joel': '2026-11-21 14:28 UTC: his round-47 export (review/r47/ANSWERS-R47-20261121-1428.json), "continue"',
         'applied_by': 'review/r47/apply_r47.py',
         'must_contain_exact': ['### How to Check for SS', '### Act Now on SS', '### Niacin "Flushes" Trips Out',
                                '## Off the Healing Treadmill', '### Mango Leaf Tea: Chill Bliss',
                                '### Metta Sniffer: Chill Love 🫶🏿', '### Lime or EOs for Calm']},
        {'id': 'r47-inner-signal-out', 'status': 'applied',
         'what': ('the Inner Signal section out of the guide until his app is ready, kept word for word in '
                  'review/r47/REMOVED-B65.md'),
         'joel': '2026-11-21 14:28 UTC, for the Inner Signal heading: "remove this section for now since my app isn\'t ready"',
         'applied_by': 'review/r47/apply_r47.py',
         'must_not_contain': ['Inner Signal App to the Rescue!', 'I developed the [**Inner Signal app**]']},
    ]:
        if entry['id'] not in ids:
            oe['entries'].append(entry)
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('updated:', ', '.join(changed))


if __name__ == '__main__':
    main()
