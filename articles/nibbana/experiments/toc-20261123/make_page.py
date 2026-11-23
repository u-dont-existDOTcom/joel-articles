#!/usr/bin/env python3
"""This run's picks page, built by the shared tools/humanization/contents_picks_page.py (which began as this file, after
../../../inner-child-therapy/experiments/t131-toc-check/make_page.py, and gained the own-words cut-off marker on
2026-11-23, lesson toc-2026-11-23a).

  python3 make_page.py PAGE-OPTIONS.json OUT.html
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import contents_picks_page

if __name__ == '__main__':
    contents_picks_page.main(HERE, *sys.argv[1:])
