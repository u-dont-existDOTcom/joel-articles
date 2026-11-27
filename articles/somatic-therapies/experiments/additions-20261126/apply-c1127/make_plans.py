#!/usr/bin/env python3
"""make_plans.py - the insertion plans for his two live posts (turn of 2026-11-27 22:26 UTC): each new section as HTML
blocks (headings and paragraphs, Markdown links as <a href>), the heading it goes before, and the title's date.
  python3 articles/somatic-therapies/experiments/additions-20261126/apply-c1127/make_plans.py DRAFT.json IC.json [A1 A2 A3]
Writes PLAN-SOMATIC.json and PLAN-INNER.json beside this file."""
import html, json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent


def inline(t):
    out, pos = [], 0
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', t):
        out.append(html.escape(t[pos:m.start()], quote=False))
        out.append('<a href="%s">%s</a>' % (html.escape(m.group(2), quote=True), html.escape(m.group(1), quote=False)))
        pos = m.end()
    out.append(html.escape(t[pos:], quote=False))
    return ''.join(out)


def main():
    adds = {a['id']: a for a in json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))}
    ic = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding='utf-8'))
    which = sys.argv[3:] or ['A1', 'A2', 'A3']
    anchors = {'Layer 4: Unstick the Memories You Can Actually Point To': 1, 'Hypnosis, the ancestral therapy': 2,
               'Optional High-Intensity State-Shift and Release Practices': 1}
    ins = []
    for k in which:
        a = adds[k]
        blocks = ['<h%d>%s</h%d>' % (a['level'], html.escape(a['heading'], quote=False), a['level'])]
        blocks += ['<p>%s</p>' % inline(p) for p in a['paragraphs']]
        ins.append({'id': k, 'heading': a['heading'], 'before': [anchors[a['before_heading']], a['before_heading']],
                    'html': ''.join(blocks), 'texts': [a['heading']] + [re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', p) for p in a['paragraphs']]})
    som = {'post': '201523223', 'inserts': ins,
           'title': {'from': 'Somatic Therapy Modalities Map & Free Intro Sessions! Save $50k! \U0001faf6\U0001f3ff\U0001f486\U0001f3ff‍♀️(Nov 21, 2026)',
                     'to': 'Somatic Therapy Modalities Map & Free Intro Sessions! Save $50k! \U0001faf6\U0001f3ff\U0001f486\U0001f3ff‍♀️(Nov 27, 2026)'}}
    (HERE / 'PLAN-SOMATIC.json').write_text(json.dumps(som, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    inner = {'post': '189761959', 'inserts': [
        {'id': 'IC1', 'before': [4, 'Discipline Done Right?'], 'after_text': 'it might take years to imagine that correction',
         'html': '<p>%s</p>' % inline(ic['IC1']['add']), 'texts': [ic['IC1']['add_plain']]},
        {'id': 'IC2', 'before': [4, 'Compassionate Exit?'], 'after_text': 'be the end of the investigation',
         'html': '<p>%s</p>' % inline(ic['IC2']['add']), 'texts': [ic['IC2']['add_plain']]}]}
    (HERE / 'PLAN-INNER.json').write_text(json.dumps(inner, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'somatic': [(i['id'], i['before'], len(i['texts'])) for i in ins], 'inner': [(i['id'], i['before']) for i in inner['inserts']]}))


if __name__ == '__main__':
    main()
