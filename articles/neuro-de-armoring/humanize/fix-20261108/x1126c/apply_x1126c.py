#!/usr/bin/env python3
"""Put his answer "72a" of 2026-11-26 23:30 UTC into the article: each warning's label folded into its first sentence,
and The Rule's and agmatine's openings fixed, each paragraph in only at Human High by itself (the Cognitive Warning, under
50 words, with the paragraph after it).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126c/apply_x1126c.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import apply_gate  # noqa: E402
import texts_x1126c as T  # noqa: E402

H = 'https://www.pangram.com/history/'
NEW = {'dmso': (T.FOLD['dmso'], H + 'c122d183-0686-48a8-a938-0225ba2e10ec', 'one window, High, 152 words'),
       'elec': (T.FOLD['elec'], H + '3eef685c-d5bb-4d36-9780-7bf5ce81342f', 'one window, High, 59 words'),
       'ethno': (T.FOLD['ethno'], H + '7dada8cf-90a9-40b5-88f1-b2637462237d', 'one window, High, 100 words'),
       'iso': (T.TRY2['iso-a'], H + 'd0307fad-8033-4600-a211-55a5fbe847aa', 'one window, High, 109 words; try 2, '
               'after the fold read two Medium windows'),
       'rule': (T.TRY2['rule-a'], H + '71736380-8f72-43e4-89cc-ff3378253463', 'one window, High, 76 words; its second '
                'sentence fixed, as 72a asks'),
       'cog': (T.FOLD['cog'], H + '69498d51-4485-47ad-b3be-c50dd04d2c7f', 'with the paragraph after it: one window, '
               'High, 110 words'),
       'lma': (T.FOLD['lma'], H + '0d102087-7015-4501-bf13-f8c40fec8d21', 'one window, High, 66 words'),
       'agm': (T.TRY2['agm-a'], H + '90af11fc-5156-43fb-8737-b132481f3e30', 'one window, High, 90 words; its opening '
               'tied to the herbs ("do"), as 72a asks'),
       'prec': (T.TRY2['prec-a'], H + 'f2c7211d-0412-40cc-b6ee-d77946543489', 'one window, High, 89 words; try 2, its '
                'last two sentences given their subject after the fold read Human Low there'),
       'htp': (T.FOLD['htp'], H + '9af71813-fc24-44d0-a70d-fa6afdadf554', 'one window, High, 129 words')}
ORDER = ['dmso', 'elec', 'ethno', 'iso', 'rule', 'cog', 'lma', 'agm', 'prec', 'htp']


def main(write):
    gate = [T.plain(NEW[k][0]) for k in ORDER if k != 'cog'] + [T.plain(NEW['cog'][0]) + '\n\n' + T.plain(T.FACES)]
    apply_gate.require(T.H / 'pangram-ledger.jsonl', gate)
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    applied = []
    for k in ORDER:
        new, link, how = NEW[k]
        assert text.count(T.OLD[k]) == 1, k
        text = text.replace(T.OLD[k], new)
        applied.append({'key': k, 'whose': 'mine' if k in ('dmso', 'elec', 'ethno', 'rule', 'cog') else
                        'his card version, with the fold of mine', 'check': 'my check, this turn: %s (Human Written, %s)'
                        % (link, how), 'old': T.OLD[k], 'new': new})
    print('\n'.join('%s: %s' % (a['key'], a['check']) for a in applied))
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        rec = {'about': 'his answer "72a" of 2026-11-26 23:30 UTC (fix-20261108/joel-20261126-2330-message.txt): each '
                        'warning\'s label folded into its first sentence, opening on its subject, his nicknames kept in '
                        'the sentence; The Rule\'s and agmatine\'s openings fixed. The "CRITICAL MEDICAL DISCLAIMER:" line '
                        'stays as the list\'s title.',
               'runs': [{'applied': applied, 'before_sha256': before,
                         'after_sha256': hashlib.sha256(text.encode()).hexdigest()}]}
        (HERE / 'APPLIED-X1126C.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', rec['runs'][0]['after_sha256'][:8])


def prec3(write):
    """The second run: the Precautions' try 3 in place of try 2, which read High but broke his words "use with extreme
    caution" (fidelity key W009)."""
    old, new = T.TRY2['prec-a'], T.TRY2['prec-c']
    link = H + '6fd9e6f1-1e19-481c-8a65-618ec3e54bf5'
    apply_gate.require(T.H / 'pangram-ledger.jsonl', [T.plain(new)])
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    assert text.count(old) == 1
    text = text.replace(old, new)
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        f = HERE / 'APPLIED-X1126C.json'
        rec = json.loads(f.read_text(encoding='utf-8'))
        rec['runs'].append({'applied': [{'key': 'prec', 'whose': 'his own paragraph, with the fold of mine',
                                         'check': 'my check, this turn: %s (Human Written, one window, High, 88 words; '
                                                  'try 3, his "Use with extreme caution" kept, "It\'s" before his "not '
                                                  'recommended")' % link, 'old': old, 'new': new}],
                            'before_sha256': before, 'after_sha256': hashlib.sha256(text.encode()).hexdigest()})
        f.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', rec['runs'][-1]['after_sha256'][:8])


def joins(write):
    """The third run: the section's last check read two Medium windows, each a short sentence whose point the next one
    draws; both joined by "so", each paragraph High by itself."""
    pairs = [('ethno', T.FOLD['ethno'], T.TRY2['ethno-a'], H + '8834b342-f1dd-43b4-9fcc-b7bc5c0bb0c4', '100 words'),
             ('rule', T.TRY2['rule-a'], T.TRY2['rule-b'], H + '46e550c9-24ef-48f2-aa42-01fd2bf9cdde', '76 words')]
    apply_gate.require(T.H / 'pangram-ledger.jsonl', [T.plain(n) for _, _, n, _, _ in pairs])
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    applied = []
    for k, old, new, link, words in pairs:
        assert text.count(old) == 1, k
        text = text.replace(old, new)
        applied.append({'key': k, 'whose': 'mine', 'check': 'my check, this turn: %s (Human Written, one window, High, %s; '
                        'the sentence that read Human Medium in the section joined to the next by "so")' % (link, words),
                        'old': old, 'new': new})
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        f = HERE / 'APPLIED-X1126C.json'
        rec = json.loads(f.read_text(encoding='utf-8'))
        rec['runs'].append({'applied': applied, 'before_sha256': before,
                            'after_sha256': hashlib.sha256(text.encode()).hexdigest()})
        f.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', rec['runs'][-1]['after_sha256'][:8])


def faces(write):
    """The fourth run: the section's check after the joins read one Medium window, the first sentence of the paragraph
    after the Cognitive Warning; my "reads ... into" back to his post's "projects ... onto", the pair High by itself."""
    link = H + '787fc317-0dc4-47a4-87e8-2c9ac3df278e'
    apply_gate.require(T.H / 'pangram-ledger.jsonl', [T.plain(T.FOLD['cog']) + '\n\n' + T.plain(T.FACES2)])
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    assert text.count(T.FACES_S1) == 1
    text = text.replace(T.FACES_S1, T.FACES_S1B)
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        f = HERE / 'APPLIED-X1126C.json'
        rec = json.loads(f.read_text(encoding='utf-8'))
        rec['runs'].append({'applied': [{'key': 'faces', 'whose': 'mine', 'check': 'my check, this turn: %s (Human '
                                         'Written, with the Cognitive Warning: one window, High, 110 words; "reads ... '
                                         'into" back to his post\'s "projects ... onto")' % link,
                                         'old': T.FACES_S1, 'new': T.FACES_S1B}],
                            'before_sha256': before, 'after_sha256': hashlib.sha256(text.encode()).hexdigest()})
        f.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', rec['runs'][-1]['after_sha256'][:8])


if __name__ == '__main__':
    if '--faces' in sys.argv:
        faces('--write' in sys.argv)
    elif '--joins' in sys.argv:
        joins('--write' in sys.argv)
    elif '--prec3' in sys.argv:
        prec3('--write' in sys.argv)
    else:
        main('--write' in sys.argv)
