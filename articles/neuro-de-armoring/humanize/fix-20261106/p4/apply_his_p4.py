#!/usr/bin/env python3
"""His versions of blocks 20 and 25 (his message of 2026-11-06 23:50 UTC), word for word as he checked them, except one
stray word: his block 25 as checked begins its last sentence "If That's why I built this protocol, ...", the "If" left
from an edit (his sentence before the cut had no "If"), so it goes in as "That's why I built this protocol, ..." and is
checked again that way (E331: a real word where none belongs). Block 20: https://www.pangram.com/history/db46aa9e-1c6e-4e71-b4f3-df7e1ef85328
(Human, one window High, 90 words). Block 25: https://www.pangram.com/history/4fda6c7a-b262-4a52-845d-af7d69fbc8e5
(Human, one window High, 77 words)."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
HIS20 = ('Have you done years of CBT or EMDR and yet you still get triggered and freeze or blow up? One reason to think '
         'about, is that standard therapy is trying to rewrite the "code" (your thoughts and behaviors), while the '
         '"motherboard" (the brain\'s physical structure and chemistry) is often overheating or damaged, and code doesn\'t '
         'run well on a motherboard like that. So to address that, I\'ve designed this protocol to go after 4 specific '
         'neuro-biological problems before you go working on the psychology (well, alongside).')
HIS25_CHECKED = ('We grew up building a "role-self" to please and manage the people around us. And the role-self psychology '
                 'gets locked in physiologically by Dopamine and DeltaFosB, which also underlie addictions, so it\'s a '
                 'vicious cycle as both create the other. If That\'s why I built this protocol, to go after the chemistry '
                 'holding the false persona in place, so the person you were before the trauma (your "True-Self") can '
                 'come back out.')
HIS25 = HIS25_CHECKED.replace('If That\'s why', 'That\'s why')
STARTS = {'Have you done years of CBT or EMDR': HIS20, 'As we grow up, our "Role-Self"': HIS25}
text = ART.read_text(encoding='utf-8')
blocks = text.split('\n\n')
done = []
for start, new in STARTS.items():
    hits = [i for i, b in enumerate(blocks) if b.startswith(start)]
    assert len(hits) == 1, (start, hits)
    done.append({'block': hits[0], 'old': blocks[hits[0]], 'new': new})
    blocks[hits[0]] = new
out = '\n\n'.join(blocks)
ART.write_text(out, encoding='utf-8')
(HERE / 'HIS25-corrected.txt').write_text(HIS25 + '\n', encoding='utf-8')
(HERE / 'APPLIED-HIS-P4.json').write_text(json.dumps({'blocks': done, 'his25_as_checked': HIS25_CHECKED,
    'article_sha256_before': hashlib.sha256(text.encode()).hexdigest(),
    'article_sha256_after': hashlib.sha256(out.encode()).hexdigest()}, ensure_ascii=False, indent=1) + '\n')
print([d['block'] for d in done])
