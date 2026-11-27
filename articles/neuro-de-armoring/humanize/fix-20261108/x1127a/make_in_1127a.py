"""IN.json for batch x1127a/checks-1127a: his answers 73a and 74b (his message of 2026-11-27 15:45 UTC), each warning
checked by itself before it goes in (gate bad-trips-2026-11-12l), from the receipts' texts."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
R = HERE / 'receipts'
MSG = 'his answers of 2026-11-27 15:45 UTC ("73 a  but i also can\'t recommend starting them 74 b")'
DECIDES = ('whether it goes in; below High, the next try starts from it and changes a word or two a reader could take two '
           'ways')
ITEMS = {
    'lma-73a': dict(lineage='W-LMA-73a', receipt='LMA-73A', chance=0.7,
                    name='Lion\'s mane and ashwagandha, with 73a and his line "can\'t recommend starting them"',
                    diagnosis=MSG + ' change this warning: his line opens it ("I can\'t recommend starting ..."), 73a\'s '
                    'gloss and stop sign end it, the stop sign fixed for the fresh reads (x1127a/v1). As it stood (the '
                    'fold) it read Human High by itself (https://www.pangram.com/history/0d102087-7015-4501-bf13-'
                    'f8c40fec8d21).',
                    human='his own card version: "Post-ashwa and post-lion\'s mane syndrome are rare, but it\'s the same '
                          'kind of thing SSRIs and finasteride can do"',
                    tells='my stop-sign clause after "so": a condition with a list and an aside ("or any sexual '
                          'problems, since you started it")',
                    first_fix='payoff: the first sentence opens on his advice (not to start either herb) and the last '
                              'clause on what to stop for; join: none, two sentences as his; plain: none, his words and '
                              'the plain words of question 73',
                    humanized='his card version with 73a and his line put in; my words are the stop sign\'s clause, fixed '
                              'for the v1 reads (either herb, one condition then the act, a baseline, sexual problems)',
                    big_change='his answer 73a and his line "i also can\'t recommend starting them" change the first '
                               'sentence\'s opening, the gloss and the last clause; the rest is his card version as it '
                               'read High'),
    # A lineage of its own (W-LMA-73a), as his versions got theirs (W35-his, W-AGMINTRO-his): 73a and his line are his
    # decision on what the warning says, not a retry for Pangram, so the near-miss rule of W-LMA-his (whose best try, the
    # fold, read High) doesn't bind it; the try before it in the article is that fold.
    'prec-74b': dict(lineage='W015-his', receipt='PREC-74B', chance=0.8,
                     name='Precautions, with 74b ("on the same day as")',
                     diagnosis=MSG + ': 74b puts "on the same day as" for "concurrently with". As it stood it read Human '
                     'High by itself (https://www.pangram.com/history/6fd9e6f1-1e19-481c-8a65-618ec3e54bf5).',
                     human='his own paragraph: "Do not use agmatine ... (will reduce tolerance), clonidine and/or '
                           'guanfacine"',
                     first_fix='payoff: unchanged, his paragraph; join: none; plain: "on the same day as", his pick',
                     humanized='his own paragraph, with 74b\'s "on the same day as" (his pick of my option b) and last '
                               'turn\'s "It\'s"'),
}
out = {}
for k, v in ITEMS.items():
    t = (R / (v['receipt'] + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    d = {'lineage': 'neuro-de-armoring/' + v['lineage'], 'scope': 'paragraph', 'name': v['name'], 'text': t,
         'chance': v['chance'], 'receipt': str(R / (v['receipt'] + '.receipt.json')), 'diagnosis': v['diagnosis'],
         'decides': DECIDES, 'first_fix': v['first_fix'], 'humanized': v['humanized'], 'human_tells': v['human']}
    for o in ('tells', 'big_change'):
        if v.get(o):
            d[o] = v[o]
    out[k] = d
(HERE / 'checks-1127a' / 'IN.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(out), 'items')
