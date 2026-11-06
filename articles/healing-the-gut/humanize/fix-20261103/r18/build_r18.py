#!/usr/bin/env python3
"""r18 = r17 with the three old Low windows gate E354 found still in the article fixed (Joel, 2026-11-06 20:13 UTC: "if
it's "low" we should fix it"): Phase 1's opening sentence (r12-g07, AI Low with its heading) and the stacks list (r12-g13
and r11c-g13, AI Low: its intro with item 1, and item 3). Under E373 these are the model's words he kept, so the fixes
are mine, tested, on approve cards. His usual fixes first (E368): the reader's reason, then the act named (E371); a term
explained where it is first used (E369: "prebiotic" was first used here, unexplained); the plain word. Writes r18.md and
CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r17' / 'r17.md').read_text(encoding='utf-8')
CHANGES = []


def ch(old, new, kind, why):
    global md
    assert md.count(old) == 1, (old[:60], md.count(old))
    md = md.replace(old, new)
    CHANGES.append({'old': old, 'new': new, 'kind': kind, 'why': why})


ch('Before you throw supplements or antimicrobials at your gut, the system mechanics that are foundational to gut '
   'function have to work.',
   'Before you throw supplements or antimicrobials at your gut, check your nervous system and your bile, the mechanics '
   'they need to work.', 'window',
   'AI Low with its heading (r12-g07, #125): the act first, named (check your nervous system and your bile, the two '
   'checks the phase makes), then why; "the mechanics" kept, since Phase 2 opens "Once the mechanics work"')
ch('A good stack should cover these 3 categories:', 'Look for a stack that covers these 3 categories:', 'window',
   'AI Low with item 1 (r12-g13, #131; r11c-g13, #136): the reader\'s act first')
ch('1. First, support the Microbiome with a well-tolerated probiotic or probiotic system.',
   '1. First, your gut needs its good bacteria back, so take a probiotic that\'s easy on your stomach.', 'window',
   'AI Low (#131, #136): the reader\'s reason, then the act (E371); "easy on your stomach", the plain word for '
   '"well-tolerated"')
ch('2. Then keep the probiotics well-fed with a good prebiotic, and take something that helps short-chain fatty acid '
   'production, especially the main one, butyrate, or take butyrate itself.',
   '2. Then keep them fed with a prebiotic, the kind of fiber they eat, and take something that helps them make '
   'short-chain fatty acids, especially the main one, butyrate, or take butyrate itself.', 'term',
   'E369: "prebiotic" is first used here and was never explained; "helps them make", the plain verb for "helps ... '
   'production"; the item read AI Low with items 1 and 3 in #136, in an older wording')
ch('3. Other nutrients will help support barrier repair, such as glutamine, zinc carnosine, colostrum, mucosal-support '
   'herbs, or similar compounds.',
   '3. Last, something to help your gut lining heal, like glutamine, zinc carnosine, colostrum, or herbs that soothe '
   'it.', 'window',
   'AI Low on its own (r11c-g13, #136): what it is for first (to help your gut lining heal), then the examples word for '
   'word; "herbs that soothe it", the plain words for "mucosal-support herbs"; "or similar compounds" said nothing')
(HERE / 'r18.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'changes;', len(md.split()), 'words')
