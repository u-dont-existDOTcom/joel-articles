#!/usr/bin/env python3
"""Put the turn of his message of 2026-11-26 00:50 UTC into HUMANIZED-SO-FAR.md (texts_x1126a: the texts and why each
changed).

- His three versions (cards W-ISO, W-AGMINTRO, W-HTPTOP; ../x1125a/ANSWERS-X1125A-20261126-0050.json), each as he
  checked it, with his link for "Phasic" Dopamine, the link to the 5-HTP section carried over, two typos fixed, and in
  the agmatine paragraph his own "receptors" for "tone" (checked by itself this turn: Human Written, one window, High).
- His answers 66, 67 and 69 in my three paragraphs (the plant medicines, The Rule, uridine): each goes in only at Human
  High by itself (apply_gate.py reads the ledger first); KEYS names the ones to put in.
- His answer 69 and his comment on W-HTPTOP in three paragraphs not yet humanized: the 5-HTP section's interaction
  paragraph, Scenario C's 5-HTP add-on and the Shield's 5-HTP trial line (no same-day rule for psychedelics; how near
  ayahuasca and iboga).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126a/apply_x1126a.py KEY ... [--write]
  (KEY: iso agm htp ss void5htp shield5htp, and ethno rule uri once each reads Human High; "all" for every one)
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import texts_x1126a as T  # noqa: E402
sys.path.insert(0, str(T.ROOT / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

H = T.H
ARTICLE = T.ARTICLE
LEDGER = H / 'pangram-ledger.jsonl'
CHECKS = {
    'iso': 'his check: https://www.pangram.com/history/364ba0a6-ea20-4584-85e8-5d8ca2c733d0 (Human Written, one window, '
           'High, 108 words)',
    'agm': 'his "tone" version: https://www.pangram.com/history/75d40a7b-25a9-4eb1-9ab6-6635b66eff58 (Human Written, one '
           'window, High, 81 words); with his "receptors", this turn: https://www.pangram.com/history/'
           '2d5f8c39-9e62-4301-ab59-5e416a8c26d5 (Human Written, one window, High, 91 words)',
    'htp': 'his check: https://www.pangram.com/history/bc1f203e-34da-44e7-99db-6e4140130364 (Human Written, one window, '
           'High, 125 words)',
    'ethno': 'my check, this turn, after two small steps that read Human High (his 66: https://www.pangram.com/history/'
             'ebe5c0d3-8542-477e-9530-d046ca9af3f1; his 67: https://www.pangram.com/history/ce8f1f83-4f9c-438c-bb53-'
             '338af9454829): https://www.pangram.com/history/c6b0ce3a-3677-45aa-bf26-0b425cb58b3f (Human Written, one '
             'window, High, 101 words)',
    'rule': 'my check, this turn: https://www.pangram.com/history/d59de519-9b7d-498a-8ca4-26f1667c60d9 (Human Written, one '
            'window, High, 71 words)',
    'uri': 'my check, this turn, after two small steps that read Human High (https://www.pangram.com/history/'
           '1a32497a-170b-4509-a586-beccff78cd45, https://www.pangram.com/history/5cc5532c-93d7-4df8-9ec7-3eabbf2c6ca8): '
           'https://www.pangram.com/history/7aa023e7-18ad-4a29-94c6-ba32631be997 (Human Written, one window, High, 113 '
           'words)',
}


def main(keys, write):
    if keys == ['all']:
        keys = list(T.OLD)
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    mine = [k for k in keys if k in T.MINE]
    if mine:
        apply_gate.require(LEDGER, [T.plain(T.NEW[k]) for k in mine])
    applied = []
    for k in keys:
        assert text.count(T.OLD[k]) == 1, k
        text = text.replace(T.OLD[k], T.NEW[k])
        applied.append({'key': k, 'whose': 'his' if k in T.HIS_KEYS else 'mine' if k in T.MINE else 'his answer, fitted',
                        'why': T.WHY[k], 'check': CHECKS.get(k, ''), 'old': T.OLD[k], 'new': T.NEW[k]})
    rec = {'about': 'his message of 2026-11-26 00:50 UTC (../joel-20261126-0050-message.txt) and his three versions',
           'applied': applied, 'before_sha256': before,
           'after_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], keys)
    if write:
        ARTICLE.write_text(text, encoding='utf-8')
        f = HERE / 'APPLIED-X1126A.json'
        prev = json.loads(f.read_text(encoding='utf-8')) if f.exists() else {'runs': []}
        prev['runs'].append(rec)
        f.write_text(json.dumps(prev, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        r = subprocess.run([sys.executable, str(T.ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                            str(H / 'FIDELITY-KEYS.json'), str(ARTICLE)], capture_output=True, text=True)
        print('fidelity:', (r.stdout + r.stderr).strip()[-1500:])


if __name__ == '__main__':
    main([a for a in sys.argv[1:] if a != '--write'], '--write' in sys.argv)
