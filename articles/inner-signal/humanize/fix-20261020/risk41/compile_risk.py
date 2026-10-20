"""Compile the four 4.1 risk reads of the hypnosis guide (RISK-1.md to RISK-4.md, written by Sonnet readers from
PROMPT-1.txt to PROMPT-4.txt, tools/humanization/pangram41_risk_prompt.py) into one table, and check that every quoted
sentence is in the guide as quoted (a misquote can't be found when the 4.1 result comes back).

  python3 articles/inner-signal/humanize/fix-20261020/risk41/compile_risk.py   (from the repo root)

Writes RISK-SUMMARY.md and RISK-ITEMS.json here.
"""
import json, pathlib, re

D = pathlib.Path(__file__).resolve().parent
LINE = re.compile(r'^\s*[-*]?\s*(RED|LIGHT):\s*["“](.+?)["”]\s*\((\d)[^:)]*:?\s*(.*?)\)\s*$')
RISK = re.compile(r'^\s*[-*]?\s*RISK:\s*(low|medium|high)', re.I)


def norm(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', t).strip()


def main():
    items, sections = [], []
    for n in range(1, 5):
        rp = D / ('RISK-%d.md' % n)
        part = norm((D / ('part%d.md' % n)).read_text(encoding='utf-8'))
        if not rp.exists():
            sections.append({'part': n, 'section': '(no report)', 'risk': None, 'red': 0, 'light': 0})
            continue
        cur = None
        for line in rp.read_text(encoding='utf-8').splitlines():
            if line.startswith('## '):
                cur = {'part': n, 'section': line[3:].strip(), 'risk': None, 'red': 0, 'light': 0}
                sections.append(cur)
                continue
            m = LINE.match(line)
            if m and cur is not None:
                kind, quote, pattern, why = m.groups()
                q = norm(quote).rstrip('.')
                found = q in part or q.rstrip('.!?') in part
                items.append({'part': n, 'section': cur['section'], 'kind': kind, 'quote': quote, 'pattern': int(pattern),
                              'why': why, 'found': found})
                cur['red' if kind == 'RED' else 'light'] += 1
                continue
            m = RISK.match(line)
            if m and cur is not None:
                cur['risk'] = m.group(1).lower()
    (D / 'RISK-ITEMS.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    by_pat = {}
    for it in items:
        if it['kind'] == 'RED':
            by_pat[it['pattern']] = by_pat.get(it['pattern'], 0) + 1
    out = ['# Pangram 4.1 risk read of the hypnosis guide: summary', '',
           'From RISK-1.md to RISK-4.md (one Sonnet reader per quarter of the guide, brief '
           '`tools/humanization/reviewer/pangram41_risk.md`). A forecast for the prediction and for where to look first, '
           'never a reason to skip a check or to change a sentence that 4.1 reads Human.', '',
           '%d sections; %d RED and %d LIGHT sentences; %d quotes not found as quoted. RED by pattern: %s.' % (
               len(sections), sum(s['red'] for s in sections), sum(s['light'] for s in sections),
               sum(not it['found'] for it in items),
               ', '.join('%d: %d' % (k, v) for k, v in sorted(by_pat.items())) or 'none'), '',
           '| part | section | risk | RED | LIGHT |', '|---|---|---|---|---|']
    for s in sections:
        out.append('| %d | %s | %s | %d | %d |' % (s['part'], s['section'], s['risk'] or '-', s['red'], s['light']))
    out += ['', 'Patterns: 1 wry quips and joke similes; 2 aphorisms and balanced contrasts that close a thought; 3 tidy '
            'follow-ups that restate, sum up or reassure; 4 general explanations in parallel or signposting form; 5 a generic '
            '"you" or "imagine" scenario; 6 stock AI words and frames.', '']
    (D / 'RISK-SUMMARY.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out[4:6]))
    for s in sections:
        if s['risk'] == 'high':
            print('high:', s['part'], s['section'], s['red'], s['light'])


if __name__ == '__main__':
    main()
