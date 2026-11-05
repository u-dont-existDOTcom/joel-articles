#!/usr/bin/env python3
"""cut_widget.py - the Bad Trip Triage app's Elementor HTML widget, cut from the source of its page
(https://ibogaqueen.com/1625-2/, saved with curl on Joel's laptop): from its opening comment ("<!-- Bad Trip Triage Guide
App") to the end of its script, which is exactly what the widget holds.

  python3 cut_widget.py PAGE.html OUT.html
"""
import hashlib
import sys

page = open(sys.argv[1], encoding='utf-8').read()
a = page.index('<!-- Bad Trip Triage Guide App')
s = page.index('<script', page.index('id="btg-app"'))
e = page.index('</script>', s) + len('</script>')
w = page[a:e]
assert w.count('<div id="btg-app"') == 1 and w.count('<style id="btg-app-styles">') == 1, 'not the app widget'
open(sys.argv[2], 'w', encoding='utf-8').write(w)
print('%d characters; sha256 %s' % (len(w), hashlib.sha256(w.encode()).hexdigest()))
