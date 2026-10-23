"""Joel's own rewrite of the forces paragraph that opens "De-hypnosis: wake up inside the influence" (HG16), from his message of 2026-10-23
12:30 UTC (joel-20261023-1230-message.txt, word for word): EDITS-joel-1230.json, one 4.1 edit.

His words: "first screenshot is only AI in the article not by itself but i rewrote it". The screenshot is recheck A's
result (2026-10-22, RESULT-A.json in fix-20261022/recheck/): the paragraph's run of questions ("By a screen? ... By
repetition?") read AI, Low and Medium, in the whole guide, though the paragraph had read Human alone. Batch 472g had since
turned the questions into a list in brackets; his rewrite replaces that first part, from "One of the best side-effects" to
"It's all around you.", which he left out. The paragraph's last two sentences ("Sometimes it's benign ..." and "But you may
want to ask yourself ...") are his points about benign influence and stay after his words. Two obvious typos are fixed:
"ominpotent" and "vote for a this or that politician" (a stray "a"). Everything else is as he typed it, straight quotes
and apostrophes included.

  python3 articles/inner-signal/humanize/fix-20261023/make_joel_1230.py   (from the repo root)
  then: python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add articles/inner-signal/humanize/fix-20261023/EDITS-joel-1230.json
"""
import json, pathlib

D = pathlib.Path(__file__).resolve().parent
H = D.parent
START = 'One of the best side-effects of learning self-hypnosis is influence literacy:'
END = 'It’s all around you.'
TYPOS = [('ominpotent', 'omnipotent'), ('vote for a this or that politician', 'vote for this or that politician')]


def his_paragraph():
    msg = (D / 'joel-20261023-1230-message.txt').read_text(encoding='utf-8')
    line = next(l for l in msg.splitlines() if l.startswith('first screenshot is only AI in the article'))
    p = line.split('but i rewrote it: "', 1)[1]
    assert p.endswith('"'), p[-40:]
    p = p[:-1].strip()
    for a, b in TYPOS:
        assert p.count(a) == 1, a
        p = p.replace(a, b)
    return p


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    a = md.index(START)
    b = md.index(END, a) + len(END)
    old = md[a:b]
    assert md.count(old) == 1 and '\n' not in old, 'the span must be inside one paragraph'
    new = his_paragraph()
    edit = {
        'key': 'HG16-joel-1230',
        'section': 'HG16',
        'source': ('Joel\'s own words (his message of 2026-10-23 12:30 UTC, fix-20261023/joel-20261023-1230-message.txt): "first '
                   'screenshot is only AI in the article not by itself but i rewrote it", replacing the paragraph up to "It\'s all '
                   'around you."; two typos fixed ("ominpotent", a stray "a" before "this or that politician")'),
        'batch': 'joel-20261023-1230',
        'old': old,
        'new': new,
        'paragraph_check': None,
        'paragraph_result': 'his own rewrite; read in place in the next recheck of part A',
        'section_check': None,
        'section_result': None,
    }
    (D / 'EDITS-joel-1230.json').write_text(json.dumps([edit], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('EDITS-joel-1230.json: %d words -> his %d words' % (len(old.split()), len(new.split())))


if __name__ == '__main__':
    main()
