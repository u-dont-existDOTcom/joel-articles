#!/usr/bin/env python3
"""Turn 107: OWNER-EDITS.json for Joel's answers of 2026-10-25 00:24 UTC. Entries whose strings his new My Journey or
Not Every Hero paragraphs replaced carry his current strings or are superseded, each with a history note, and two new
entries record what went in: his two sections, and 103.3 A and 103.4 A."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import apply_t107 as A  # noqa: E402

P = HERE.parents[1] / 'OWNER-EDITS.json'
WHEN = 'Turn 107 (his answers of 2026-10-25 00:24 UTC, experiments/t107-answers/JOEL-20261025-0024.md)'
data = json.loads(P.read_text(encoding='utf-8'))
by = {e['id']: e for e in data['entries']}
assert not any(e['id'].startswith('joel-107-') for e in data['entries']), 'already applied'


def history(e, note):
    e.setdefault('history', []).append(WHEN + ': ' + note)


def swap(eid, field, old, new, note):
    e = by[eid]
    hits = [k for k, v in enumerate(e[field]) if v == old]
    assert len(hits) == 1, (eid, field, old[:50], hits)
    e[field][hits[0]] = new
    history(e, note)


swap('mpv-p2-logic', 'must_contain',
     "It's evidence you're safe to be around and that you accept them. Love needs both, but without warmth they can still feel like they're only being put up with.",
     "All of that is evidence they're accepted and you're safe to be around. Love needs those to start with, but without warmth they can still feel like they're only being put up with.",
     'his own P2 (103.2) says the evidence line his way, and it keeps both logic fixes: "if they\'re right", and evidence that they\'re accepted and you\'re safe, which love needs.')
by['mpv-p2-shows']['status'] = 'superseded'
history(by['mpv-p2-shows'], 'his own P2 (103.2) leaves out "All of that shows as clearly to them as the clean room did." (entry joel-107-20261025-sections).')
swap('joel-72-74-20261021', 'must_contain',
     'That didn\'t stop me from practicing, but I did stop when I felt fake, stop in the sense of ... like I might still kind of allow the exercise to play out somehow but I would stop "pushing" it to be a certain way',
     'That didn\'t stop me from practicing, but I did stop "pushing" it to be a certain way',
     'his own My Journey (103.1) says his 72d clarification in an article sentence of his. I had put it in as he typed it in chat ("you put in some of my things too verbatim").')
swap('joel-72-74-20261021', 'must_contain', 'I found more love in', 'I also found more love in the rest of the',
     'his own My Journey (103.1): "I also found more love in the rest of the Buddhist teachings".')
history(by['q3-therapist-story-20261011'], 'his own My Journey (103.1) tells it in his article sentences: "Years later, I found a warm, intuitive inner child therapist, named Daja, randomly, while in Kenya. I figured I already knew this stuff, but I gave it a shot." His chat answer had gone in close to word for word.')
e = by['joel-106-20261024-sections']
old = [s for s in e['must_contain_exact'] if 'if it progress is stagnating' in s]
assert len(old) == 1
e['must_contain_exact'] = [s.replace('if it progress is stagnating', 'if progress is stagnating') for s in e['must_contain_exact']]
history(e, '103.4 A: "But do notice if progress is stagnating." for his "if it progress".')

NEW = A.article_paragraphs()
data['entries'] += [
    {'id': 'joel-107-20261025-sections', 'status': 'applied',
     'what': "Joel's own My Journey (all thirteen paragraphs, his bypassing paragraph second) and his own first three paragraphs of Not Every Hero Wears A Cape, word for word, each checked by him. Each link and the two italic words are on the same words as before, since his paste is plain text, and each of his lines is its own paragraph. Make It Intentional stays as it was. Installed by experiments/t107-installs/apply_t107.py.",
     'joel': '2026-10-25 00:24 UTC: "103a oh i had not read that whole section, it looks still a little ai, and you put in some of my things too verbatim. here\'s the fixed, fully green section"; "103.2 i fixed the section, it\'s all dark green now"',
     'where': 'My Journey; Not Every Hero Wears A Cape',
     'must_contain_exact': NEW['journey'] + NEW['hero'],
     'must_not_contain': ['stop in the sense of', 'The way I picture it is almost stupidly simple.', 'Metta gave all that love somewhere to land.',
                          'structured sessions with an inner-child therapist deepened it', "although I didn't think I needed it",
                          'in general and map it out completely', 'Plenty of seekers and gurus do it too',
                          'All of that shows as clearly to them as the clean room did.']},
    {'id': 'joel-107-20261025-103', 'status': 'applied',
     'what': '103.3 A: his acacia sentence stays as he wrote it. 103.4 A: "But do notice if progress is stagnating." in his When to Change the Strategy.',
     'joel': '2026-10-25 00:24 UTC: "103.3 a people can read it how they want, homie don\'t play that game otherwise i\'ll have to change "he/she" to "he/zhe/she/they/them" everywhere also"; "103.4 a"',
     'where': 'When Escape Leaves Reality Behind; When to Change the Strategy',
     'must_contain': ['but excellent if you want to know how it feels to be painfully autistic + schizo!', 'But do notice if progress is stagnating.'],
     'must_not_contain': ['do notice if it progress is stagnating']},
]
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits updated:', len(data['entries']), 'entries')
