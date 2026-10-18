"""show.py KEY FIXED.json B... - each stretch's published blocks and its current text (for adjudicating findings)."""
import json, sys
sys.path.insert(0, '../tools')
import faithful as F
key, fx = sys.argv[1], sys.argv[2]
want = {int(b) for b in sys.argv[3:]}
d = json.load(open(fx, encoding='utf-8'))
pub = F.pub_blocks(key)
for u in d['units']:
    if u['kind'] == 'emulate' and u['blocks'][0] in want:
        print('== %s B%s' % (key, '-'.join(map(str, [u['blocks'][0], u['blocks'][-1]]))))
        for b in u['blocks']:
            print('   PUB[B%d] %s' % (b, pub[b]))
        for p in u['paras']:
            print('   NOW %r' % p)
