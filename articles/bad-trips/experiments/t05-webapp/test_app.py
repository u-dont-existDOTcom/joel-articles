#!/usr/bin/env python3
"""test_app.py - the rewritten Bad Trip Triage app, tested in a real browser (Chromium, Playwright), with the live app as
the control: every situation of the guide's checklist is put to the interactive triage, as on the live page, and each
answer is checked for what the guide says there. The live app must fail the checks the rewrite is for (so the test
can't pass by accident), and the rewrite must pass them all, with no console or page errors.

  python3 test_app.py APP-V8.html APP-LIVE.html [--report OUT.json]
"""
import json
import pathlib
import sys
import tempfile

from playwright.sync_api import sync_playwright

SCENARIOS = {
    '1 medical danger': ({'danger': [0]}, ['field rescue can happen in parallel']),
    '1b brain damage, psychedelic': ({'sel': {'problem': 'neurological', 'drug-type': 'psychedelic', 'neuro-status': 'reassuring'}},
                                     ['humic acid', '5mg lick', 'Metta NMT sniffer', 'whole leaf', 'flushing niacin']),
    '1b brain damage, objective signs': ({'danger': [2], 'sel': {'problem': 'neurological', 'neuro-status': 'unable'}},
                                         ['humic acid', '5mg lick']),
    '1b brain damage, MDMA': ({'sel': {'problem': 'neurological', 'drug-type': 'mdma', 'neuro-status': 'reassuring'}},
                              ['one gram per minute']),
    'MDMA jaw tension': ({'sel': {'problem': 'mdma', 'drug-type': 'mdma'}}, ['one gram per minute', 'impaired kidneys']),
    '7 too intense': ({'sel': {'problem': 'overload', 'drug-type': 'psychedelic', 'goal': 'stabilize'}},
                      ['Buteyko', 'ocean-water contact']),
    '9 entities': ({'sel': {'problem': 'entity'}}, ['sending love did', 'Love Thy Enemy']),
    '10 gut': ({'sel': {'problem': 'gut', 'drug-type': 'psychedelic'}}, ['first thought here is ozonated zeolite', 'adsorbs drugs']),
    '11 nausea': ({'sel': {'problem': 'nausea', 'drug-type': 'psychedelic', 'goal': 'stabilize'}}, ['coffee cherries']),
    '12 stop the trip': ({'sel': {'problem': 'abort', 'drug-type': 'psychedelic', 'goal': 'abort'}}, ['whole leaf', 'flushing niacin']),
    '2 unsafe momentum': ({'sel': {'problem': 'action'}}, []),
    '3 room': ({'sel': {'problem': 'environment'}}, []),
    '4 body': ({'sel': {'problem': 'body'}}, []),
    '5/6 alone': ({'sel': {'problem': 'alone'}, 'context': [4]}, []),
    '8 euphoric certainty': ({'sel': {'problem': 'grandiosity'}}, []),
    '9 psychosis-like': ({'sel': {'problem': 'psychosis'}}, []),
    '13/14 shadow work': ({'sel': {'problem': 'emotional', 'drug-type': 'psychedelic'}, 'context': [5]}, []),
}
# what must be gone from every answer and from the page
GONE = ['home rescue protocol', 'invent', 'improvis', 'field plan', 'familiar magnesium-chloride plan', 'trip-abort plan',
        'Evidence-weighted', 'not validated treatment']

RUN = """async (cfg) => {
  const form = document.querySelector('[data-btg-form]');
  const q = s => document.querySelector(s);
  form.querySelectorAll('input[type=checkbox]').forEach(c => { c.checked = false; });
  ['problem','drug-type','neuro-status','alertness','goal'].forEach(k => { const s = q('[data-btg-' + k + ']'); if (s) s.selectedIndex = 0; });
  const boxes = Array.from(form.querySelectorAll('input[type=checkbox]'));
  const danger = boxes.filter(b => b.name === 'danger'), context = boxes.filter(b => b.name === 'context');
  (cfg.danger || []).forEach(i => danger[i].checked = true);
  (cfg.context || []).forEach(i => context[i].checked = true);
  for (const [k, v] of Object.entries(cfg.sel || {})) { const s = q('[data-btg-' + k + ']'); s.value = v; s.dispatchEvent(new Event('change', {bubbles: true})); }
  form.dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}));
  await new Promise(r => setTimeout(r, 200));
  const el = q('[data-btg-result-content]');
  return {title: (q('[data-btg-result-title]') || {}).textContent || '', text: el.textContent.replace(/\\s+/g, ' '),
          shown: el.innerText.replace(/\\s+/g, ' '), closed: el.querySelectorAll('details:not([open])').length};
}"""


def harness(widget_path, d):
    page = d / (pathlib.Path(widget_path).stem + '-harness.html')
    page.write_text('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, '
                    'initial-scale=1"><title>harness</title></head><body>' +
                    pathlib.Path(widget_path).read_text(encoding='utf-8') + '</body></html>', encoding='utf-8')
    return page


def check(widget_path, pw, d):
    browser = pw.chromium.launch()
    errors, out = [], {}
    try:
        for width in (1280, 390):
            page = browser.new_page(viewport={'width': width, 'height': 900})
            page.on('pageerror', lambda e: errors.append('pageerror: %s' % e))
            page.on('console', lambda m: errors.append('console %s: %s' % (m.type, m.text)) if m.type == 'error' else None)
            page.goto(harness(widget_path, d).as_uri())
            page.wait_for_timeout(300)
            if width == 390:
                scroll = page.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
                out['_phone_sideways_scroll_px'] = scroll
                page.close()
                continue
            body = page.evaluate('document.querySelector("#btg-app").textContent')
            out['_page_gone_left'] = [g for g in GONE if g.lower() in body.lower()]
            for name, (cfg, want) in SCENARIOS.items():
                r = page.evaluate(RUN, cfg)
                out[name] = {'title': r['title'], 'missing': [w for w in want if w.lower() not in r['shown'].lower()],
                             'gone_left': [g for g in GONE if g.lower() in r['text'].lower()],
                             'closed_details': r['closed'], 'chars': len(r['text'])}
            page.close()
    finally:
        browser.close()
    out['_errors'] = errors
    return out


def main(argv):
    new, live = argv[0], argv[1]
    report = argv[argv.index('--report') + 1] if '--report' in argv else None
    with tempfile.TemporaryDirectory() as t, sync_playwright() as pw:
        d = pathlib.Path(t)
        res_new, res_live = check(new, pw, d), check(live, pw, d)
    fails = []
    for name in SCENARIOS:
        n, l = res_new[name], res_live[name]
        if n['missing'] or n['gone_left'] or n['closed_details']:
            fails.append('%s: missing %s, left %s, closed details %d' % (name, n['missing'], n['gone_left'], n['closed_details']))
        print('%-34s rewrite: %s | live app: missing %s' % (name, 'PASS' if not (n['missing'] or n['gone_left'] or n['closed_details'])
                                                         else 'FAIL', l['missing'] or '-'))
    if res_new['_page_gone_left']:
        fails.append('page still says %s' % res_new['_page_gone_left'])
    if res_new['_errors']:
        fails.append('errors: %s' % res_new['_errors'][:5])
    if res_new['_phone_sideways_scroll_px'] > 0:
        fails.append('phone width scrolls sideways by %dpx' % res_new['_phone_sideways_scroll_px'])
    control = sum(bool(res_live[n]['missing']) for n, (_, w) in SCENARIOS.items() if w)
    wanted = sum(1 for _, (_, w) in SCENARIOS.items() if w)
    print('control: the live app misses something in %d of the %d situations with checks' % (control, wanted))
    if control < wanted:
        fails.append('the live app passes some checks the rewrite is for: the check would not catch a regression there')
    print('live app page still says: %s' % res_live['_page_gone_left'])
    if report:
        pathlib.Path(report).write_text(json.dumps({'rewrite': res_new, 'live': res_live, 'fails': fails}, indent=1,
                                                   ensure_ascii=False) + '\n', encoding='utf-8')
    print('\n'.join(fails) if fails else 'PASS: every check, no errors')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
