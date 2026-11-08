"""Put B039n, B040n and B041n into HUMANIZED-SO-FAR.md (2026-11-08 turn).

These came out of the needed read (needed/b039..b041): what the reader can't use is cut,
and b041's "less of the voltage gets through" (a sense error) becomes "less calcium gets in".
B040n also drops the Gemini label "("Lock, Stock, and Barrel")": only "Lock" names a tool,
"Stock" and "Barrel" name nothing, so the label tells the reader nothing.
All three read AI in Pangram, as the versions they replace did (see RESULTS-0108.md).
"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drafts_0108 as D
H = HERE.parents[0] / 'HUMANIZED-SO-FAR.md'
new = {d['name']: d['text'] for d in D.D}
new['B040n'] = new['B040n'].replace('The Fix ("Lock, Stock, and Barrel"): ', 'The Fix: ')
starts = {'B039n': 'D-serine may help therapy update old memories, because',
          'B040n': 'The Fix ("Lock, Stock, and Barrel"):The Brake (NAC)',
          'B041n': 'The Lock (Zinc/Magnesium): Magnesium physically plugs'}
lines = H.read_text().split('\n')
done = {}
for k, s in starts.items():
    hits = [i for i, l in enumerate(lines) if l.startswith(s)]
    if len(hits) != 1:
        sys.exit(f'{k}: {len(hits)} lines start with {s!r}')
    i = hits[0]
    done[k] = {'line': i + 1, 'old': lines[i], 'new': new[k]}
    lines[i] = new[k]
H.write_text('\n'.join(lines))
(HERE / 'APPLIED-0108N.json').write_text(json.dumps(done, indent=1, ensure_ascii=False) + '\n')
print('applied', ', '.join(f"{k}@{v['line']}" for k, v in done.items()))
