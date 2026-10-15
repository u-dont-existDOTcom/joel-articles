"""Texts and gate records for the Pangram batches of Joel's message of 2026-10-15 09:33 UTC.

  python3 fix-20261015/make_batch.py      # from candidate/: writes drafts.json and GATE.json

28b is my wording, which he picked ("28 b"), so its record is an owner record. Section 10's record carries the
repeats check of 2026-10-14 21:19 (fix-20261014b/gate/REPEATS.md: nothing in section 10), since the change is the
subject of one sentence.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
OLD = "Whenever you create or apply a rule, it's best practice"
NEW = "Whenever a community or a federation creates or applies a rule, it's best practice"
if OLD in art:
    art = art.replace(OLD, NEW)   # before the install: check the text it will put in
assert NEW in art
paras = [p.strip() for p in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', art, flags=re.S)) if p.strip()]
p5 = plain(next(p for p in paras if p.startswith(NEW)))
drafts = {'J10-P5b': p5, 'S10v4': section(art, '# From One Community to a Movement')}
gate = {'J10-P5b': {'kind': 'owner', 'joel': '2026-10-15 09:33 UTC: "28 b" (my wording, his pick)', 'words': len(p5.split())},
        'S10v4': {'kind': 'section', 'parts': ['J10-P5b', 'installed'], 'repeats': 0,
                  'repeats_note': 'fix-20261014b/gate/REPEATS.md (2026-10-14 21:19): nothing inside section 10; the change is one sentence\'s subject',
                  'words': len(drafts['S10v4'].split())}}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print({k: v['words'] for k, v in gate.items()})
