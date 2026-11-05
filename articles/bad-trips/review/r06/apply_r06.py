#!/usr/bin/env python3
"""apply_r06.py - round 6's answers (Joel, exported 2026-11-05 15:14:55 UTC; ANSWERS-R06-20261105-1514.json, sent with
"ok idk why you can't use pangram other lanes are using it try again" at 15:20 UTC) put into the guide. All three cards
Revise.

Starts from the guide after round 5 (../../GUIDE-SO-FAR-blocks.json, which round 6's page showed; PAGE-R06.md's SHA-256
is the one his export names) and writes the guide after round 6 (GUIDE-AFTER-R06.md and GUIDE-AFTER-R06-blocks.json
beside this script), which becomes ../../GUIDE-SO-FAR.md.

- CBD-TRIAL: his version (the card's "your_version") is the whole run of the section's warning-stage and cannabis
  paragraphs, in his order: the warning stage (with his own hunch about humic/fulvic acid added), cannabis at an aura with
  the nasal and under-the-tongue routes and Brazil's ABRACE rescue spray, what forums and the rat study say, and the skin
  gel. The 7-OH-CBD point is out: "nobody asked why CBD is better or worse than 7-OH-CBD, the only reason to mention that
  is if that's important to consider which we establish it probably IS NOT" (a meant cut, KEEP-AS-IS C9). Changes, none
  to his meaning:
  * "comapny" -> "company"; "[testified in Congress] (url)" made a link; "in this vid: <url>" -> "in [this vid](url)";
    the line break inside his second paragraph joined; the trailing space after his first paragraph's last sentence gone;
  * the skin-gel trial keeps its link on "12-week trial";
  * one sentence corrected to what the paper says (gate E348; his card Y-B on round 7's page): he wrote "The study
    authors suggested the dosing may have been too low, or it works better for generalized rather than focal seizures."
    The paper (O'Brien et al. 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC9270696/) says the doses may have been too
    low, and that the response in focal epilepsy "is not as robust as seen in patients with Dravet syndrome"; it doesn't
    say "generalized". So: "... or that CBD just doesn't work as well for focal seizures as it does in Dravet syndrome,
    where many of the seizures are generalized." His next sentence stays: "Generalized are the type people usually have
    with MDMA & psychedelic overdoses."
- SEIZ-WARN: where the warning stage goes: "we should move the non-cannabis para above all the cannabis info ... let's
  put it after p2 before p3". It goes after the rescue-benzodiazepine paragraph (B110), before the adjunct paragraph
  (B111).
- And from his question on CBD-TRIAL, "why are we talking about focal seizures, when seizures from mdma and psychedelic
  overdoses are generalized seizures, right? so we should extrapolate from cbd evidence for that which we already stated
  in the para above with dravet and lennox types": B111's last sentence, "For focal seizures outside those syndromes, the
  evidence is mixed, but still long-term.", goes (my decision on his question, his card Y-C on round 7's page). Drug-
  induced seizures are generalized (MDMA's come mostly from low sodium and heat), so the focal evidence doesn't serve this
  reader; the skin-gel trial keeps its focal point because it says why that trial may not apply.
- MOVE-YOURS: B236 (his dangers paragraph) and B237 (the movement line) become his one paragraph, as he checked it
  (Human Written, 0%, High / Medium / High: https://www.pangram.com/history/e9d8d85c-5c0f-46b6-b780-91652f1efd15, its
  text his version plus a trailing newline).

  python3 apply_r06.py            write the guide after round 6 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R06.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R06-20261105-1514.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R06.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R06-blocks.json'

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r06', (ANSWERS['review_id'], REVIEW['review_id'])
assert hashlib.sha256((HERE / 'PAGE-R06.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {'CBD-TRIAL', 'SEIZ-WARN', 'MOVE-YOURS'} and all(x['status'] == 'revise' for x in ITEM.values())

GEL = 'https://pubmed.ncbi.nlm.nih.gov/35802375/'
CONGRESS = 'https://escriba.camara.leg.br/escriba-servicosweb/html/58445'
VID = 'https://www.youtube.com/watch?v=bgVi5o_2v_w'
UNIT = {b['id']: b for b in BLOCKS}
LOG = []


def one(md, old, new):
    assert md.count(old) == 1, (old, md)
    return md.replace(old, new)


# ---------------------------------------------------------------- CBD-TRIAL (his run of paragraphs)
his = ITEM['CBD-TRIAL']['your_version']
paras = [p.strip() for p in his.split('\n\n')]
assert len(paras) == 4, len(paras)
aura, canna, forums, gel = paras
assert aura.startswith('Some people get a warning before a seizure takes hold') and 'humic/fulvic' in aura
assert canna.startswith('As for CBD/cannabis') and canna.count('\n') == 1
canna = re.sub(r' *\n', ' ', canna)
canna = one(canna, 'a comapny called ABRACE', 'a company called ABRACE')
canna = one(canna, '[testified in Congress] (%s)' % CONGRESS, '[testified in Congress](%s)' % CONGRESS)
canna = one(canna, 'being used on a child in this vid: %s' % VID, 'being used on a child in [this vid](%s).' % VID)
assert forums.startswith('I also read on forums')
assert gel.startswith('As for topical CBD') and '7-OH' not in his
gel = one(gel, '12-week trial', '[12-week trial](%s)' % GEL)
gel = one(gel, 'or it works better for generalized rather than focal seizures.',
          'or that CBD just doesn\'t work as well for focal seizures as it does in Dravet syndrome, where many of the '
          'seizures are generalized.')
assert gel.endswith('Generalized are the type people usually have with MDMA & psychedelic overdoses.')

old_gel = UNIT['N-CBD-2']
assert old_gel['md'].startswith("And topical CBD hasn't been well-studied") and '7-OH-CBD' in old_gel['md']

# ---------------------------------------------------------------- B111: the focal sentence out
FOCAL = ' For focal seizures outside those syndromes, the evidence is mixed, but still long-term.'
UNIT['B111']['md'] = one(UNIT['B111']['md'], FOCAL, '')
LOG.append('B111: its last sentence out ("For focal seizures outside those syndromes, ..."), from his question on '
           'CBD-TRIAL; card Y-C on round 7\'s page')

# ---------------------------------------------------------------- place them (SEIZ-WARN: after P2, before P3)
i110 = BLOCKS.index(UNIT['B110'])
BLOCKS.insert(i110 + 1, {'id': 'N-AURA', 'kind': 'p', 'md': aura, 'text': None})
ig = BLOCKS.index(old_gel)
BLOCKS[ig:ig + 1] = [{'id': 'N-CANNA', 'kind': 'p', 'md': canna, 'text': None},
                     {'id': 'N-FORUMS', 'kind': 'p', 'md': forums, 'text': None},
                     {'id': 'N-CBD-2', 'kind': 'p', 'md': gel, 'text': None}]
LOG.append('CBD-TRIAL + SEIZ-WARN: his warning-stage paragraph (N-AURA) after B110; N-CBD-2 becomes his three paragraphs '
           '(N-CANNA, N-FORUMS, N-CBD-2); the 7-OH-CBD point out (his cut); "comapny" -> "company"; his two links made '
           'links; the trial authors\' reason corrected to the paper (card Y-B)')

# ---------------------------------------------------------------- MOVE-YOURS
mv = ITEM['MOVE-YOURS']['your_version'].strip()
assert hashlib.sha256((mv + '\n').encode()).hexdigest() == \
    'ff3babec15cbdacc8e2bad7e3d155a7350bc17f9dc1b209bb8dd49c705c313fe'
assert UNIT['B237']['md'].startswith('Movement is allowed.') and UNIT['B236']['md'].startswith('Anything that could')
UNIT['B236']['md'] = mv
BLOCKS.remove(UNIT['B237'])
LOG.append('B236 + B237: MOVE-YOURS, his one paragraph as he checked it (Human Written, 0%, High/Medium/High)')

# ---------------------------------------------------------------- write
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
OUT.write_text(text, encoding='utf-8')
OUT_BLOCKS.write_text(json.dumps([{'id': b['id'], 'kind': b['kind'], 'md': b['md'], 'text': None} for b in BLOCKS],
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
before = (ART / 'GUIDE-SO-FAR.md').read_text(encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before)), len(re.findall(r'\S+', text))
print('\n'.join(LOG))
print('3 cards applied (his versions); %d words -> %d (%+d); %s sha256 %s' % (
    w0, w1, w1 - w0, OUT.name, hashlib.sha256(text.encode()).hexdigest()))
