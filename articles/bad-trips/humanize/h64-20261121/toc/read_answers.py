"""Joel's round 47 answers -> his contents, checked.

Takes his answers as the page saved them (the database document, or what "Copy my answers" gave) and:
  1. works the headings out again from his picks with the columns he saw (PAGE-OPTIONS.json as published in turn 56),
     and stops if that disagrees with the headings the page saved (lesson bad-trips-2026-11-21c);
  2. writes HIS-PICKS.json (contents order, level, heading, which column) and CONTENTS-HIS.txt / LINES-HIS.json for
     fresh readers;
  3. runs the contents check (tools/humanization/toc_check.py) for headings that repeat their parent or the one
     before (lesson bad-trips-2026-11-21a), so each gets a fate before anything is applied.

  python3 read_answers.py ANSWERS.json
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'humanization'))
import toc_sidebar as ts  # noqa: E402

OPTS = json.load(open(os.path.join(HERE, 'PAGE-OPTIONS.json'), encoding='utf-8'))
NOW = json.load(open(os.path.join(HERE, 'NOW.json'), encoding='utf-8'))
COLS = {k: {e['id']: e for e in json.load(open(os.path.join(HERE, m['file']), encoding='utf-8'))}
        for k, m in OPTS['options'].items()}
COLS['now'] = {e['id']: e for e in NOW}


def resolve(ans):
    picks, own = ans.get('picks', {}), ans.get('own', {})
    out = []
    for e in NOW:
        p = picks.get(e['id']) or OPTS['pick'].get(e['id']) or 'now'
        if p == 'own':
            out.append({'id': e['id'], 'level': e['level'], 'heading': own.get(e['id']) or e['heading'], 'from': 'own'})
            continue
        src = COLS.get(p, {}).get(e['id']) or e
        out.append({'id': e['id'], 'level': src['level'], 'heading': src['heading'], 'from': p if src is not e else 'now'})
    return out


def main(path):
    raw = open(path, encoding='utf-8').read()
    ans = json.loads(raw[raw.index('{'):raw.rindex('}') + 1])
    mine = resolve(ans)
    saved = ans.get('headings')
    if saved:
        bad = [(e['id'], e['heading'], saved.get(e['id'])) for e in mine if saved.get(e['id']) != e['heading']]
        if bad:
            for b in bad:
                print('DISAGREES', b)
            sys.exit('the saved headings and his picks disagree: stop and ask him')
    if ans.get('added'):
        sys.exit('he kept added headings: place them by hand (none were expected in round 47)')
    json.dump(mine, open(os.path.join(HERE, 'HIS-PICKS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    lines, ids = [], []
    for n, e in enumerate(mine, 1):
        fits, shown, w, room = ts.shown(e['heading'], e['level'])
        lines.append('%-3d%s%s' % (n, '    ' * (e['level'] - 1), shown))
        ids.append({'n': n, 'id': e['id']})
    open(os.path.join(HERE, 'CONTENTS-HIS.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    json.dump(ids, open(os.path.join(HERE, 'LINES-HIS.json'), 'w', encoding='utf-8'), indent=1)
    froms = {}
    for e in mine:
        froms[e['from']] = froms.get(e['from'], 0) + 1
    print('his contents:', len(mine), 'headings;', ', '.join('%s %d' % kv for kv in sorted(froms.items())))
    print('cut in the sidebar:', [e['heading'] for e in mine if not ts.shown(e['heading'], e['level'])[0]])
    if ans.get('comment'):
        print('his comment:', ans['comment'])
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'humanization', 'toc_check.py'),
                    os.path.join(HERE, 'HIS-PICKS.json')])


if __name__ == '__main__':
    main(sys.argv[1])
