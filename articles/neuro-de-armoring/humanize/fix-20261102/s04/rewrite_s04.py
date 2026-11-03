"""Part 1 C to E of the neuro de-armoring article ("The Hardened Circuit", "The Lagging System", "The Save Button"), which
read AI Generated, 100% AI in the baseline (batch n1102, ../baseline/RESULTS.md), rewritten for his card, every compound,
dose, unit, timing and warning kept (FIDELITY-KEYS.json; fidelity_keys.py check must pass).

What read AI there (every window AI): the template ("The Problem:", "The Fix:", "The Hardening:", labels glued to each
paragraph), a question answered by its own next word ("Why don't these drugs work ...? Because ..."), and short closers
("The engine is flooded."). The rewrite (gate E321's order): the labels go and their paragraphs say the same thing in
sentences; the self-answered question becomes a statement; the closer folds into its sentence; short sentences are joined.
Every claim stays as strong as it was ("zero effect", "permanently", "immediately", "You must ... 10–20 minutes"), and the
game's four steps stay word for word.

  python3 articles/neuro-de-armoring/humanize/fix-20261102/s04/rewrite_s04.py
Writes CANDIDATE.md (the whole article with this section rewritten) and SECTION.txt (the section's text, as checked).
"""
import hashlib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MASTER_SHA = 'a4b4e05ae5b6930519e79708f0d7dbedf5cb4f9c6158bf2efd60121501fdef0f'
U1 = 'https://academic.oup.com/ijnp/article/15/6/825/761323?login=false'
U2 = 'https://pubmed.ncbi.nlm.nih.gov/20473292/'
U3 = ('https://www.rockefeller.edu/news/38266-increasing-the-level-of-the-protein-pi31-demonstrates-neuroprotective-effects-'
      'in-mice/')
EDITS = [
    ("The Problem: To protect itself from the Glutamate storm, the brain eventually releases Dynorphin, a chemical blanket that "
     "suppresses dopamine. This creates the “Void”—a state of apathy, grayness, and an inability to feel pleasure.",
     "To protect itself from the Glutamate storm, the brain eventually releases Dynorphin, a kind of chemical blanket that "
     "suppresses dopamine. That’s how you end up in the “Void”, all apathy and grayness, unable to feel pleasure."),
    ("Why Standard Meds Failed You If you have tried SSRIs (antidepressants) and failed, you are not crazy. Ipser & Stein "
     "[2012 study ](%s)showed that Prozac had zero effect on male combat veterans with calcified PTSD. And the side effects "
     "are well-known, including anhedonia, zombification, and sexual dysfunction." % U1,
     "If you’ve tried SSRIs (antidepressants) and they failed you, you’re not crazy. Ipser & Stein’s [2012 study](%s) showed "
     "that Prozac had zero effect on male combat veterans with calcified PTSD. And the side effects are well-known, including "
     "anhedonia, zombification, and sexual dysfunction." % U1),
    ("Why don’t these drugs work on calcified PTSD? Because standard serotonin drugs treat the “software” (mood), but they "
     "cannot penetrate the “hardware” (the structural changes in the amygdala caused by severe trauma). This protocol uses "
     "Ketones and HDAC Inhibitors to remodel the physical structure of the brain that resists standard medication.",
     "They don’t work on calcified PTSD because standard serotonin drugs treat the “software” (mood) and can’t get through "
     "to the “hardware”, the structural changes in the amygdala caused by severe trauma. This protocol uses Ketones and HDAC "
     "Inhibitors to remodel that physical structure, the part of the brain that resists standard medication."),
    ("The Hardening: Chronic cycles lead to the accumulation of DeltaFosB, a protein switch that permanently alters gene "
     "expression to cement the trauma circuitry ([Vialou, et al, 2010](%s))." % U2,
     "With chronic cycles, DeltaFosB builds up. It’s a protein switch that permanently alters gene expression to cement the "
     "trauma circuitry in place ([Vialou, et al, 2010](%s))." % U2),
    ("The Fix (The Unlock): You cannot “wait” for this to pass. We use “System Reformats” (Shrooms/Iboga) to stimulate "
     "GDNF, which physically rewires the brain around these hardened loops.",
     "You can’t just “wait” for this to pass, though. For the unlock, we use “System Reformats” (shrooms or iboga) to "
     "stimulate GDNF, which physically rewires the brain around these hardened loops."),
    ("The Problem: “Brain Fog” is often a fuel crisis. Trauma causes cerebral insulin resistance—your neurons are swimming "
     "in glucose (sugar) but cannot burn it. The engine is flooded.",
     "“Brain Fog” is often a fuel crisis. Trauma causes cerebral insulin resistance, so your neurons are swimming in glucose "
     "(sugar) and can’t burn it, like a flooded engine."),
    ("The Fix: If the brain cannot burn sugar, we switch fuels. We use PQQ to boost ATP, and Ketones, which bypass the "
     "broken glucose pathways and enter the mitochondria directly. This turns the lights back on immediately. We alternate "
     "hot and cold showers to [boost p131](%s) and heat shock proteins and reduce inflammation." % U3,
     "If the brain can’t burn sugar, we switch fuels: PQQ to boost ATP, and Ketones, which bypass the broken glucose "
     "pathways and go straight into the mitochondria. This turns the lights back on immediately. We alternate hot and cold "
     "showers to [boost p131](%s) and heat shock proteins and reduce inflammation." % U3),
    ("The Problem: Every time you have a flashback, your brain attempts to “save” the memory again, often reinforcing the "
     "emotional trauma loop.",
     "Every time you have a flashback, your brain tries to “save” the memory again, and that often reinforces the emotional "
     "trauma loop."),
    ("The Fix (”The Jammer”): Memories require visual processing power to be restored. If you occupy the Visual-Spatial "
     "Working Memory (e.g., playing Tetris) during the critical window *after* a flashback, the brain fails to “save” the "
     "visual details. The memory is restored, but the emotional “sting” is permanently reduced.",
     "The fix is “The Jammer”. Restoring a memory takes visual processing power, so if you keep your Visual-Spatial Working "
     "Memory busy (playing Tetris, say) during the critical window *after* a flashback, the brain fails to “save” the visual "
     "details. The memory is restored, but the emotional “sting” is permanently reduced."),
    ("Instead of Tetris (which requires app/phone), you can use the “Color-Path Connect” method. This is more effective "
     "than simple counting because it forces your brain to map 3D space, which directly competes with the visual “saving” "
     "of a traumatic memory.",
     "Tetris needs an app or a phone. The “Color-Path Connect” method doesn’t, and it works better than simple counting "
     "because it forces your brain to map 3D space, which competes directly with the visual “saving” of a traumatic "
     "memory."),
]
FIRST, LAST = '#### C. The “Hardened” Circuit: Dynorphin & DeltaFosB', '+1'


def main():
    md = (H.parent / 'master.md').read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == MASTER_SHA
    new = md
    for old, rep in EDITS:
        assert new.count(old) == 1, old[:60]
        new = new.replace(old, rep)
    (HERE / 'CANDIDATE.md').write_text(new, encoding='utf-8')
    bl = sr.blocks(new)
    i = [b['i'] for b in bl if b['text'] == FIRST.lstrip('# ').strip()][0]
    j = [b['i'] for b in bl if b['text'] == LAST and b['i'] > i][0]
    sec = '\n\n'.join(b['text'] for b in bl[i:j + 1] if b['text'] != 'Double click to interact with video')
    (HERE / 'SECTION.txt').write_text(sec, encoding='utf-8')
    print(hashlib.sha256(new.encode('utf-8')).hexdigest()[:12], len(sec.split()), 'words in the section')


if __name__ == '__main__':
    main()
