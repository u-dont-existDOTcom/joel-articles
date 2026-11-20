#!/usr/bin/env python3
import json,sys
ids=json.load(open('/home/claude/headtest/ids.json'))
try: d=json.load(open(sys.argv[1]))
except Exception as e: print('JSON does not parse:',e); sys.exit(1)
h=d.get('headings',{})
miss=[i for i in ids if not str(h.get(i,'')).strip()]
print('OK' if not miss else 'missing: '+' '.join(miss)); sys.exit(0 if not miss else 1)
