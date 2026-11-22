#!/usr/bin/env python3
"""restore_my_cuts.py - three of turn 27's overcompletion cuts put back: each took out a belief or reason of his.

Turn 27's overcompletion read (../h36-20261108/overcompletion/, cut_overcompletion.py) judged "already said" by the
point a line makes, not by whose belief or reason it carries. His message of 17:24 UTC ("this bad trips guide lost my
actual beliefs or like maybe they got put in one corner", lesson bad-trips-2026-11-08e) and the beliefs read after it
(beliefs/LOST.md, findings 8, 14 and 17) show three of the nine cuts took his reasons out:
- B197, after his ozone story: "The mistake showed me that DMSO and aged ozonated-charcoal water address different
  kinds of overload." (why he treats the two as different tools);
- B337, after Spiritual ≠'s practice line: "That is tripsitting, shadow work, and the path becoming practical." (the
  line that makes the three one practice);
- B401, in Demons: "A demon can fight your hatred, feed on your fear, argue with your pride or seduce your grandiosity,
  but there's nothing in love for it to grab." (why love works against an entity).
They were my cuts of the same day, not his, so they go back as they were (the blocks before cut_overcompletion.py, from
the commit before it, c4528b75).

  python3 restore_my_cuts.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
by = {b['id']: b for b in blocks}
A197 = 'I don\'t recommend inhaling ozone.'
assert by['B197']['md'].endswith(A197)
by['B197']['md'] += ' The mistake showed me that DMSO and aged ozonated-charcoal water address different kinds of overload.'
A401 = 'It might look passive, but this is how you become unhookable.'
assert by['B401']['md'] == A401
by['B401']['md'] += (' A demon can fight your hatred, feed on your fear, argue with your pride or seduce your grandiosity, but '
                     'there\'s nothing in love for it to grab.')
assert 'B337' not in by
i = [k for k, b in enumerate(blocks) if b['id'] == 'B336'][0]
blocks.insert(i + 1, {'id': 'B337', 'kind': 'p', 'md': 'That is tripsitting, shadow work, and the path becoming practical.',
                      'text': None})
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('B197, B337, B401 put back')
