#!/usr/bin/env python3
"""His fix of "Talk about making love before you do it", part 2 (2026-11-23 23:49 UTC: "actually i don't like the medium
windows ... i fixed that talk about making love section"), as a layer after r36: HIS-S05.json. his-s05.txt is the text of
his check, https://www.pangram.com/history/4028a476-97bc-4504-961b-dd80a7192238 (Human High, one window, 344 words), byte
for byte (SHA-256 c04b9ee4df3a6840...). Its first paragraph is the fixed version's 15 unchanged; 16 to 18 are his."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
text = (HERE / 'his-s05.txt').read_text(encoding='utf-8').rstrip('\n')
assert hashlib.sha256(text.encode('utf-8')).hexdigest().startswith('c04b9ee4df3a6840')
paras = [p.rstrip() for p in text.split('\n\n')]
repl = {int(k): v for k, v in json.loads((HERE.parent / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8')).items()}
post = {}
for line in (HERE.parent / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        post[r['n']] = r['text']
assert repl[15] == [paras[0]], 'his first paragraph is 15 as the fixed version has it'
link = 'https://www.pangram.com/history/4028a476-97bc-4504-961b-dd80a7192238'
out = [{'card': 'his S05 fix', 'kind': 'para', 'live': n, 'before': post[n], 'after': [p], 'his_checks': [link],
        'comment': "actually i don't like the medium windows ... i often find the medium windows indicate other issues also. "
                   "i fixed that talk about making love section"}
       for n, p in zip((16, 17, 18), paras[1:])]
data = {'about': __doc__.strip().split('\n\n')[0], 'answers': "his message of 2026-11-23 23:49 UTC", 'links': [], 'embeds': [],
        'changes': out}
(HERE / 'HIS-S05.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('changes', len(out))
