"""His answers to Neuro De-Armoring Cards, 4 November (4) (ANSWERS-20261104-2234.json, exported 22:34:03 UTC; the session
of 22:37 UTC, his GH handoff line pasted above the JSON, ANSWERS-20261104-2234.txt), into the article. Both are his
versions ("revise"), each checked by him in Pangram's web app (his links below; the lane could not read them back this
turn: the link fetch asked for an approval nobody answered, so the SHA-256 match with the text he sent waits for the next
turn).

- Y-92, the 5-HTP stop signs: his version, "this is the fully human one i'd use" (his first link). The dangerous pattern
  first, said as what to watch out for and why ("diagnostic of serotonin syndrome, which can be deadly if untreated"), then
  the lesser signs, with the overlap between the two lists said ("some of which are part of serotonin syndrome, but not
  dangerous alone"): "again the logic problem, you listed dangerous symptoms and less dangerous symptoms which overlapped".
  The double space after "blood pressure." is made one (a typo fix, no recheck).
- Y-93, the 5-HTP interactions: his version, Human (High) in his second link ("then i added an exclamation mark where it
  needed to be after that crazy story and now it's high conf human"), with one word out: his "this MedlinePlus case report"
  names the case report as MedlinePlus's, and it isn't (it is Patel and Marzella 2017 on PubMed Central, PMC5580516; the
  MedlinePlus link was the page on what serotonin syndrome looks like, which his version folded in). So the case report
  keeps its own link as "this case report", and the MedlinePlus page's link goes on his first words, "Serotonin syndrome",
  where the reader meets the term. The one-word change goes to him on Cards (5) (E348) and gets its own check next turn.

The fidelity check runs before and after each card; what his versions change in the protocol goes into "owner_changes",
each entry naming his card.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/apply_cards_x1104e.py [--check]
Writes HUMANIZED-SO-FAR.md, FIDELITY-KEYS.json and APPLIED-CARDS-E.json.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import fidelity_keys as fk  # noqa: E402
from apply_cards_x1104 import delta  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
KEYS = H / 'FIDELITY-KEYS.json'
ANSWERS = HERE / 'ANSWERS-20261104-2234.json'
BY = 'fix-20261104/cards/ANSWERS-20261104-2234.json, card %s (his version, 2026-11-04)'
MEDLINEPLUS = 'https://medlineplus.gov/ency/article/007272.htm'
CASE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5580516/'
HARMALA = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7678905/'
HIS_CHECKS = {
    'Y-92': 'https://www.pangram.com/history/c5f40d94-efae-4a5b-9830-5f58e44a30d3 (his version, "the fully human one"); '
            'https://www.pangram.com/history/9a21d29d-a678-4f7f-ac7c-3d4d63604dde (the conversational intro without the '
            'overlap fixed)',
    'Y-93': 'https://www.pangram.com/history/87cee5fc-7af1-487b-abdd-53917e062206 (without the exclamation mark: "human but '
            'not yet all high conf"); https://www.pangram.com/history/67441215-b92b-4ca5-a6ff-86941d93f7c2 (with it: "high '
            'conf human"). The version in the article differs by one word ("MedlinePlus" out): the lane checks it next turn.',
}


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    assert answers['review_id'] == 'neuro-de-armoring-cards-20261104-x1104e' and answers['article']['sha256'] == sha
    A = {x['id']: x for x in answers['items']}
    assert set(A) == {'Y-92', 'Y-93'} and all(x['status'] == 'revise' and x['your_version'].strip() for x in A.values())
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    at = {}
    for k in A:
        hits = [i for i, b in enumerate(raw) if plain(b) == A[k]['before']]
        assert len(hits) == 1, (k, hits)
        at[k] = hits[0]
    keys = json.loads(KEYS.read_text(encoding='utf-8'))
    work = copy.deepcopy(keys)
    prev = fk.check(copy.deepcopy(work), md)
    assert prev['pass'], prev
    applied = []

    def put(card, how, text, override=None):
        nonlocal prev
        raw[at[card]] = text
        now = '\n\n'.join(raw) + '\n'
        r = fk.check(copy.deepcopy(work), now)
        d = delta(prev, r)
        if override is not None:
            d = override
        if any(d.values()):
            work.setdefault('owner_changes', []).append(dict({'by': BY % card + ('; ' + how if how else '')},
                                                             **{k: v for k, v in d.items() if v}))
            r = fk.check(copy.deepcopy(work), now)
        assert r['pass'], (card, r)
        applied.append({'id': card, 'how': how, 'his_check': HIS_CHECKS[card], 'text': text,
                        'fidelity_change': {k: v for k, v in d.items() if v}})
        prev = r

    y92 = re.sub(r'  +', ' ', A['Y-92']['your_version'].strip())
    assert y92.count('  ') == 0 and A['Y-92']['your_version'].count('  ') == 1
    put('Y-92', 'his version as he checked it ("the fully human one i\'d use"); the double space after "blood pressure." '
                'made one', y92)

    his93 = A['Y-93']['your_version'].strip()
    assert his93.count('this MedlinePlus case report') == 1 and his93.startswith('Serotonin syndrome usually')
    assert his93.count("ayahuasca's harmala MAOI chemistry") == 1
    y93 = his93.replace('this MedlinePlus case report', '[this case report](%s)' % CASE)
    y93 = y93.replace('Serotonin syndrome usually', '[Serotonin syndrome](%s) usually' % MEDLINEPLUS, 1)
    y93 = y93.replace("ayahuasca's harmala MAOI chemistry", "ayahuasca's [harmala MAOI chemistry](%s)" % HARMALA)
    assert plain(y93) == his93.replace('this MedlinePlus case report', 'this case report')
    put('Y-93', 'his version with "MedlinePlus" taken out of "this MedlinePlus case report" (the case report is Patel and '
                'Marzella 2017 on PubMed Central, not MedlinePlus); the MedlinePlus page linked on "Serotonin syndrome"; '
                'to him on Cards (5), card Y-93b. His first sentence says the hard interaction rule (W046) as its cause, with '
                'no warning word ("made it clear to start with rather than a warning for no reason"); his version folds the '
                'MedlinePlus sentence (W048) into a link ("i took out redundancy")', y93,
        override={'numbers_lost': [], 'numbers_new': [], 'terms_lost': ['MedlinePlus'],
                  'keys_lost': {'W046': [['interaction'], ['5-HTP'], ['serotonin-raising'], ['casually']],
                                'W048': [['interaction'], ['MedlinePlus'], ['serotonin-syndrome'], ['overview']]}})

    out = '\n\n'.join(raw) + '\n'
    final = fk.check(copy.deepcopy(work), out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'his two versions on Neuro De-Armoring Cards, 4 November (4)', 'answers': ANSWERS.name,
           'before_sha256': sha, 'after_sha256': after, 'cards': applied, 'fidelity_pass': final['pass'],
           'his_links_read_back': False,
           'why_not_read_back': 'the link fetch asked for an approval nobody answered (2026-11-04 22:4x UTC); next turn'}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert final['pass'], final
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    KEYS.write_text(json.dumps(work, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'APPLIED-CARDS-E.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
