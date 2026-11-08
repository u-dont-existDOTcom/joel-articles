"""Put his three approvals of 8 November (11:03 UTC) into HUMANIZED-SO-FAR.md.

SC-37 (approved; his comment is answered in RECHECK-SC37.md), SC-38 and SC-42 (both approved, no comment).
T37b and T38b are drafts_0108's T37_FIXED and T38_FIXED; B042r is ../B042r.md. Each carries its links.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1108a/apply_x1108a.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
sys.path.insert(0, str(FIX))
import drafts_0108 as D  # noqa: E402

H = FIX.parent / 'HUMANIZED-SO-FAR.md'
ANS = json.loads((HERE / 'ANSWERS-X1108A-20261108-1103.json').read_text(encoding='utf-8'))
status = {i['id']: i['status'] for i in ANS['items']}
assert status == {'SC-37': 'approved', 'SC-38': 'approved', 'SC-42': 'approved'}, status
new = {'SC-37': ('The Mechanism: When glutamate floods', D.T37_FIXED),
       'SC-38': ('The Secondary Signal Dial (GluD Receptors):', D.T38_FIXED),
       'SC-42': ('The Repair (L-Serine): Your brain makes', (FIX / 'B042r.md').read_text(encoding='utf-8').strip())}
lines = H.read_text(encoding='utf-8').split('\n')
done = {}
for sid, (start, text) in new.items():
    hits = [i for i, l in enumerate(lines) if l.startswith(start)]
    if len(hits) != 1:
        sys.exit('%s: %d lines start with %r' % (sid, len(hits), start))
    i = hits[0]
    done[sid] = {'line': i + 1, 'old': lines[i], 'new': text}
    lines[i] = text
H.write_text('\n'.join(lines), encoding='utf-8')
(HERE / 'APPLIED-X1108A.json').write_text(json.dumps(done, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('applied', ', '.join('%s@%d' % (k, v['line']) for k, v in done.items()))
