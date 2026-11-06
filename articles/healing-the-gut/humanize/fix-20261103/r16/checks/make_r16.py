#!/usr/bin/env python3
"""The check texts and making-sense receipts (gate E365) for r16's three changed stretches: the intro (blocks 1-3), the
HRP line with the plant-food paragraph it follows (16-17), and the Gem note with the note under it (35-36), each checked
with the paragraph it leans on (E349). Payoffs for sentences r15 already had come from r15's receipts; the new ones are
here. Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R16 = HERE.parent
FIX = R16.parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

b16 = sr.blocks((R16 / 'r16.md').read_text(encoding='utf-8'))
HIS = (FIX / 'r15' / 'checks' / 'HIS.txt').read_text(encoding='utf-8')
OLD = {}
for f in (FIX / 'r15' / 'checks').glob('RECEIPT-*.json'):
    for x in json.loads(f.read_text(encoding='utf-8'))['sentences']:
        if x.get('payoff'):
            OLD[x['s']] = (x['payoff'], x['follows'])
NEW = {
    'But in this article, I will consolidate the most important texts on this topic so that you can directly consult '
    'with Gemini to extract': (
        'The reader knows what this article gives them (the books, made into something Gemini can answer from), with the '
        'Gemini mode left to the Gem section where they open the Gem.',
        'It follows his old posts on diarrhea, constipation and DMSO with what this one does instead.'),
    'For the most research-backed recommendations you can check this deep research report from an older version of '
    'AskRigor': (
        'The reader knows where the research-backed recommendations are, what made them (AskRigor, his research tool, in '
        'an older version), and how to get them up to date (re-check them with askrigor.com).',
        'It follows the carnivore paragraph, which says the diet is hard to get off, with where to look for what the '
        'research supports.'),
    'I have consolidated the top 9 most effective gut healing books into a customized smart Gemini Gut Health Gem.': (
        'The reader knows what the Gem is (the nine books in one Gemini Gem) and where to open it.',
        'It opens the section on the Gem, after the causes.'),
    'I tested it on free Gemini and it works, but use the highest thinking level you can for the best answers.': (
        'The reader knows they don\'t need a paid plan, and which setting gives the best answers.',
        'It follows what the Gem is for with how to use it, before he asks for better books.'),
}
TEXTS = {'r16-A': [1, 2, 3], 'r16-HRP': [16, 17], 'r16-F': [35, 36]}
READER = {
    'r16-A': "Someone with poor gut health opening the article, deciding whether to read on and how they'll use it.",
    'r16-HRP': "Someone with poor gut health who finds plants bother them, weighing the carnivore diet, who wants to "
               "know what the research supports and has never heard of AskRigor.",
    'r16-F': "Someone deciding whether to use Joel's Gemini Gem, without a paid Gemini plan, and which parts of its phases "
             "are his own rather than the books'.",
}
Q = {
    'Q1': 'PASS: each new sentence leads with its point (where the recommendations are; that the Gem works on free '
          'Gemini) and explains AskRigor in the sentence that first names it',
    'Q2': 'PASS: the instructions say what they get the reader (re-check it for an up-to-date verification; the highest '
          'thinking level for the best answers)',
    'Q3': 'PASS: the report, the tool and the setting are each named exactly (an older version of AskRigor; askrigor.com; '
          'the highest thinking level)',
    'Q4': 'PASS: AskRigor is explained where first named ("my research tool"); "thinking level" is the setting\'s name in '
          'Gemini, his word; no other new term',
    'Q5': 'PASS: the "but" in the Gem sentence turns on "it works": free is enough, the highest level is better',
    'Q6': 'PASS: nothing moved between paragraphs; the Gem advice sits after what the Gem is for',
    'Q7': 'PASS: each change is what this reader needs to use the report or the Gem',
    'Q8': 'N/A: no list items changed',
    'Q9': 'PASS: his answer\'s "re-check it with askrigor.com for an up-to-date verification" joined to the sentence it '
          'follows, one step; nothing compressed',
}
PLACEMENT = {
    'r16-A': 'The intro, his order; only the mode in brackets left out, to be named once in the Gem section.',
    'r16-HRP': 'The line after the carnivore paragraph, where he points to the research, as before; the report now named '
               'by what made it.',
    'r16-F': 'The Gem section, his order; his test and advice after what the Gem is for, before his ask for books.',
}
CHECKED = [{'point': 'the report came from an older version of AskRigor; readers can re-check it with askrigor.com',
            'found': 'his answer F10-4, 2026-11-05 22:58 UTC ("yes it was an old version of askrigor basically, we can '
                     'tell them to re-check it with askrigor.com for an up-to-date verification")',
            'still_needed': 'yes: "HRP" told readers nothing', 'fate': 'kept'},
           {'point': 'the Gem works on free Gemini; the highest thinking level gives the best answers',
            'found': 'his answer F10-5, 2026-11-05 22:56 UTC ("i just tested it with free gemini and it worked ... i\'d '
                     'just tell people to use the highest thinking level they can for best answers as usual")',
            'still_needed': 'yes: the two modes named before disagreed', 'fate': 'kept'}]
ok = True
for name, ids in TEXTS.items():
    t = '\n\n'.join(b16[i]['text'].strip() for i in ids)
    (HERE / ('CHECK-%s.txt' % name)).write_text(t, encoding='utf-8')
    r = S.make(t, b16[ids[0]].get('section', '') or 'the intro', READER[name], HIS)
    for s in r['sentences']:
        if s.get('his'):
            continue
        hit = [v for k, v in NEW.items() if s['s'].startswith(k)] or ([OLD[s['s']]] if s['s'] in OLD else [])
        assert len(hit) == 1, (name, s['s'][:80])
        s['payoff'], s['follows'] = hit[0]
    r['questions'], r['placement'], r['checked'] = dict(Q), PLACEMENT[name], CHECKED
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(t, r)
    ok = ok and not probs
    print(name, len(t.split()), 'words', 'PASS' if not probs else probs)
sys.exit(0 if ok else 1)
