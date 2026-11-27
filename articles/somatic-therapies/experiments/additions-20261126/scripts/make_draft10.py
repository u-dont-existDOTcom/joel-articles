#!/usr/bin/env python3
"""Write draft 10 of the somatic additions (A1 rewritten from the draft-9 reads, A1-P3 back to its near miss with one
change, A2 his version, A3 as draft 9) and draft 2 of the inner child sentences, plus the numbered text for readers."""
import hashlib, json, pathlib, re, sys

D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-9.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}

ISTDP = 'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and'
APT = 'https://psykologtidsskriftet.no/node/15971/pdf'
AEDP = 'https://www.apa.org/pubs/videos/4310759'

A1 = [
    "Water therapy and Brainspotting let a feeling come up on its own. But some people can feel their body just fine and "
    "still slip away from a feeling the moment it shows up in a session, explaining it instead of feeling it, or agreeing "
    "with whatever the therapist says. If that's you, look into talk therapies like [Intensive Short-Term Dynamic "
    "Psychotherapy](%s), where the therapist points out each time you slip away and helps you turn back toward the "
    "feeling." % ISTDP,
    "The therapist also watches your body for signs of the anxiety that's making you slip away, like tense muscles, "
    "sighing or a foggy head, to see how much you can take. Most people who try this therapy get a slower version, where "
    "the therapist stops to help them settle whenever the anxiety climbs.",
    "If it's one feeling in particular that scares you, like grief, [Affect Phobia Therapy](%s) treats that fear a lot "
    "like a phobia, getting you used to the feeling bit by bit, at a pace your anxiety can handle. [Accelerated "
    "Experiential Dynamic Psychotherapy](%s) is for when you can't let kindness in, when someone cares about you and it "
    "just bounces off. The therapist first makes sure you don't feel alone with the feelings that come up, then follows "
    "where you feel them in your body." % (APT, AEDP),
    "As with water therapy, I'd ask before booking: \"What do you do when I start slipping away from a feeling, and what "
    "if I get overwhelmed?\" If the answer leaves no room for you to slow down, or to tell them they've got your feeling "
    "wrong, keep looking.",
]

def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)

out = []
for aid in ('A1', 'A2', 'A3'):
    a = dict(by[aid])
    if aid == 'A1':
        a['paragraphs'] = A1
    text = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['text'] = text
    a['sha256'] = hashlib.sha256(text.encode('utf-8')).hexdigest()
    a['words'] = len(text.split())
    a['draft'] = 10 if aid == 'A1' else a.get('draft', 9)
    out.append(a)
(D / 'ADDITIONS-10.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

IC = {
    "IC1": {
        "section": "Re-do Trauma Memories (inner child guide)",
        "where": "a paragraph of its own at the end of the section, after his J. paragraph (\"... it might take years to imagine that correction.\"), before the heading \"How should discipline have been done right?\"",
        "his_before": "Whatever the situation was, we will contrast it with the corrected version. For my friend J., whose dad savagely beat him every time he smiled, I'd have the corrected version be, he smiles, and his dad smiles, happy to see him happy. Ok, that one might seem too easy, although for J, it might take years to imagine that correction.",
        "add": "If a memory feels too big to redo on your own, there's even a clinical therapy for this, called [Imagery Rescripting](https://ibogaqueen.substack.com/i/201523223/imagery-rescripting), where at first a therapist steps in as the ideal adult, until you learn to do that yourself.",
    },
    "IC2": {
        "section": "Physical Pain? (inner child guide)",
        "where": "a paragraph of its own at the end of the section, after his \"I'd ask for a chronic pain specialist ...\" paragraph, before the heading \"Listen To Your Body, Or Else!\"",
        "his_before": "I'd ask for a chronic pain specialist and a written plan for the flare-ups you can see coming, including the new or severe signs that mean you go to the ER right away, but don't let amelioration of symptoms be the end of the investigation.",
        "add": "While the investigation goes on, you might look into Pain Reprocessing Therapy and Emotional Awareness and Expression Therapy, two therapies that have helped in trials with chronic back, muscle and joint pain. (For more on both, check [my somatic guide](https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit).)",
    },
}
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-2.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

# numbered sentences for the readers
sys.path.insert(0, str(D.parents[3] / 'tools' / 'humanization'))
import sense_receipt
lines = []
for a in out:
    if a['id'] == 'A2':
        continue
    lines.append('## %s, "%s" (%s)' % (a['id'], a['heading'], 'h%d' % a['level']))
    n = 0
    for i, p in enumerate(a['paragraphs'], 1):
        lines.append('[paragraph %d]' % i)
        for s in sense_receipt.sentences(plain(p)):
            n += 1
            lines.append('%s-S%d: %s' % (a['id'], n, s))
    lines.append('')
for k, v in IC.items():
    lines.append('## %s, in "%s"' % (k, v['section']))
    lines.append('Where: ' + v['where'])
    for j, s in enumerate(sense_receipt.sentences(v['add_plain']), 1):
        lines.append('%s-S%d: %s' % (k, j, s))
    lines.append('')
(D / 'reads' / 'drafts10-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
for a in out:
    print(a['id'], a['words'], a['sha256'][:12])
