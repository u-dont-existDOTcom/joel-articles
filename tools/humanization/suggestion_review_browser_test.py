#!/usr/bin/env python3
"""suggestion_review_browser_test.py - a real browser test of a suggestion review page (suggestion_review.py's).

  python3 tools/humanization/suggestion_review_browser_test.py PAGE.html [--report OUT.json]

What it does, in Chromium (Playwright), on the exact file it's given, opened as a local file:
  - no console errors or page errors, in light and in dark colour schemes;
  - typed text in a comment box, and in a "Your version" box, is legible: the computed text and background colours of
    the box have a contrast of at least 4.5, under light and dark preferences; a negative fixture (the 2023-10-23 white
    box with no text colour) must fail the same check, so the check can't pass by accident;
  - a pre-decided suggestion starts with its decision; every other one starts "Not approved yet";
  - Approve, Reject, Revise and "Not approved yet" are one click each, without a dialog; the progress counts explicit
    decisions; Revise opens "Your version" filled with my version;
  - the type filters, the status filter, the search and "The ones I'd leave" toggle hide and show the right cards;
  - "Next undecided" brings an undecided card to the top;
  - "Copy my answers" gives parseable JSON (from the clipboard or the box it falls back to) with the review's identity,
    every suggestion, the statuses and the comment typed, word for word; "Save them as a file" downloads the same;
  - a reload keeps the answers (this browser's storage); after clearing it, loading the saved file restores them, and
    an answers file for another review is refused;
  - at phone width (390 px) the page has no sideways scroll.
"""
import argparse
import json
import pathlib
import sys
import tempfile

from playwright.sync_api import sync_playwright

CONTRAST_JS = """(el) => {
  const cs = getComputedStyle(el);
  function rgb(s){ const m = s.match(/rgba?\\(([^)]+)\\)/); if(!m) return [0,0,0,1]; const p = m[1].split(',').map(x=>parseFloat(x)); return [p[0],p[1],p[2],p.length>3?p[3]:1]; }
  function lum(c){ const a=c.slice(0,3).map(v=>{v/=255; return v<=0.03928? v/12.92 : Math.pow((v+0.055)/1.055,2.4)}); return 0.2126*a[0]+0.7152*a[1]+0.0722*a[2]; }
  let fg = rgb(cs.webkitTextFillColor && cs.webkitTextFillColor !== 'currentcolor' ? cs.webkitTextFillColor : cs.color);
  let bg = rgb(cs.backgroundColor); let node = el;
  while (bg[3] === 0 && node.parentElement) { node = node.parentElement; bg = rgb(getComputedStyle(node).backgroundColor); }
  const L1 = lum(fg), L2 = lum(bg);
  return {ratio: (Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05), fg: cs.color, fill: cs.webkitTextFillColor, bg: cs.backgroundColor};
}"""


def run(page_path, report_path=None):
    page_path = pathlib.Path(page_path).resolve()
    url = page_path.as_uri()
    results, failures = [], []

    def ok(name, cond, detail=''):
        results.append({'test': name, 'pass': bool(cond), 'detail': detail})
        if not cond:
            failures.append(name + (': ' + str(detail) if detail else ''))
        print(('PASS ' if cond else 'FAIL ') + name + ((' :: ' + str(detail)) if detail and not cond else ''))

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for scheme in ('light', 'dark'):
            ctx = browser.new_context(color_scheme=scheme, viewport={'width': 1280, 'height': 900}, accept_downloads=True)
            page = ctx.new_page()
            errors = []
            page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
            page.on('pageerror', lambda e: errors.append(str(e)))
            page.goto(url)
            page.wait_for_selector('.card[data-id]')
            data = json.loads(page.locator('#review-data').text_content())
            total = len(data['suggestions'])
            n_cards = page.locator('.card[data-id]').count()
            ok('%s: one card per suggestion' % scheme, n_cards == total, '%d cards, %d suggestions' % (n_cards, total))
            # first approve-advice card that isn't pre-decided
            ids = [s['id'] for s in data['suggestions'] if s['advice'] == 'approve' and not s.get('decided')]
            pre = [s for s in data['suggestions'] if s.get('decided')]
            for s in pre:
                st = page.locator('#c-%s' % s['id'].replace('.', '\\.')).get_attribute('data-status')
                ok('%s: %s starts with your decision' % (scheme, s['id']), st == s['decided']['status'], st)
            pend = page.evaluate("""() => Array.from(document.querySelectorAll('.card[data-id]')).filter(c => c.dataset.status !== 'pending').length""")
            ok('%s: every other card starts not approved' % scheme, pend == len(pre), pend)
            c1, c2, c3 = ('#c-' + i.replace('.', '\\.') for i in ids[:3])
            note = page.locator(c1 + ' textarea.note')
            text = 'Keep "this" — and check the link, please. Ünïcode ok.'
            note.click()
            note.type(text)
            ok('%s: typed comment kept' % scheme, note.input_value() == text, note.input_value())
            con = note.evaluate(CONTRAST_JS)
            ok('%s: comment text legible (contrast %.1f)' % (scheme, con['ratio']), con['ratio'] >= 4.5, con)
            page.click(c1 + ' .dec.approve')
            ok('%s: Approve is one click, no dialog' % scheme, page.locator(c1).get_attribute('data-status') == 'approved')
            ok('%s: pill says Approved' % scheme, page.locator(c1 + ' .pill').text_content() == 'Approved')
            page.click(c2 + ' .dec.reject')
            ok('%s: Reject' % scheme, page.locator(c2).get_attribute('data-status') == 'rejected')
            ok('%s: rejected looks different from not approved' % scheme,
               page.locator(c2 + ' .pill').text_content() != 'Not approved yet')
            page.click(c3 + ' .dec.revise')
            yours = page.locator(c3 + ' textarea.yours')
            ok('%s: Revise opens your version' % scheme, yours.is_visible())
            mine = next(s['proposed'] for s in data['suggestions'] if s['id'] == ids[2])
            ok('%s: your version starts from mine' % scheme, yours.input_value() == mine, yours.input_value()[:80])
            yours.type(' Mine.')
            con2 = yours.evaluate(CONTRAST_JS)
            ok('%s: your-version text legible (contrast %.1f)' % (scheme, con2['ratio']), con2['ratio'] >= 4.5, con2)
            pre_ap = sum(1 for s in pre if s['advice'] == 'approve' and s['decided']['status'] == 'approved')
            pre_n = sum(1 for s in pre if s['advice'] == 'approve')
            prog = page.locator('#prog').text_content()
            ok('%s: progress counts the decisions' % scheme,
               (' %d approved' % (1 + pre_ap) in prog) and prog.startswith('%d of' % (3 + pre_n)), prog)
            page.click(c1 + ' .dec.undo')
            ok('%s: back to not approved in one click' % scheme, page.locator(c1).get_attribute('data-status') == 'pending')
            ok('%s: approval count is explicit approvals only' % scheme, ' %d approved' % pre_ap in page.locator('#prog').text_content(),
               page.locator('#prog').text_content())
            page.click(c1 + ' .dec.approve')
            # filters
            page.click('#toolsBtn')
            typ = data['suggestions'][[s['id'] for s in data['suggestions']].index(ids[0])]['type']
            page.click('.tools [data-filter-type="%s"]' % typ)
            ok('%s: type filter hides that type' % scheme, not page.locator(c1).is_visible())
            page.click('.tools [data-filter-type="%s"]' % typ)
            ok('%s: and shows it again' % scheme, page.locator(c1).is_visible())
            page.select_option('#statusFilter', 'approved')
            vis = page.evaluate("""() => Array.from(document.querySelectorAll('.card[data-id]')).filter(c => !c.hidden && c.dataset.advice==='approve').map(c => c.dataset.status)""")
            ok('%s: status filter shows only approved' % scheme, vis and all(v == 'approved' for v in vis), vis[:5])
            page.select_option('#statusFilter', 'all')
            word = 'pendulation'
            page.fill('#search', word)
            page.wait_for_timeout(400)
            shown = page.evaluate("""() => Array.from(document.querySelectorAll('.card[data-id]')).filter(c => !c.hidden).length""")
            ok('%s: search narrows the cards' % scheme, 0 < shown < total, shown)
            page.fill('#search', '')
            page.wait_for_timeout(400)
            leave = page.locator('.card.leave').first
            ok('%s: the ones I\'d leave are hidden at first' % scheme, not leave.is_visible())
            page.check('#showLeave')
            ok('%s: and show when ticked' % scheme, leave.is_visible())
            page.uncheck('#showLeave')
            page.click('#toolsBtn')
            # next undecided
            page.evaluate('window.scrollTo(0, 0)')
            page.click('#nextBtn')
            page.wait_for_timeout(900)
            top = page.evaluate("""() => { const cs = Array.from(document.querySelectorAll('.card[data-id]')).filter(c => !c.hidden && c.offsetParent && c.dataset.status==='pending'); const vis = cs.map(c => c.getBoundingClientRect().top).filter(t => t > -5 && t < 400); return vis.length }""")
            ok('%s: Next undecided brings one to the top' % scheme, top >= 1, top)
            # export
            page.click('#saveBtn')
            page.click('#copyJson')
            page.wait_for_timeout(500)
            raw = page.evaluate('() => document.getElementById("copyArea").hidden ? null : document.getElementById("copyArea").value')
            if raw is None:
                try:
                    raw = page.evaluate('navigator.clipboard.readText()')
                except Exception:
                    raw = None
            try:
                exp = json.loads(raw or '')
            except ValueError:
                exp = None
            ok('%s: Copy gives parseable JSON' % scheme, exp is not None, (raw or '')[:80])
            if exp:
                ok('%s: export names the review and the guide version' % scheme,
                   exp['review_id'] == data['review_id'] and exp['article']['sha256'] == data['article']['sha256'] and exp.get('exported_at'))
                ok('%s: export has every suggestion' % scheme, len(exp['items']) == total, len(exp['items']))
                got = {x['id']: x for x in exp['items']}
                ok('%s: comment exported word for word' % scheme, got[ids[0]]['comment'] == text, got[ids[0]]['comment'])
                ok('%s: statuses exported' % scheme, got[ids[0]]['status'] == 'approved' and got[ids[1]]['status'] == 'rejected'
                   and got[ids[2]]['status'] == 'revise' and got[ids[2]]['your_version'].endswith(' Mine.'))
            with page.expect_download() as dl:
                page.click('#saveJson')
            path = dl.value.path()
            saved = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
            ok('%s: Save downloads the answers' % scheme, len(saved['items']) == total and saved['review_id'] == data['review_id'])
            # reload keeps it
            page.reload()
            page.wait_for_selector('.card[data-id]')
            ok('%s: a reload keeps the decisions' % scheme, page.locator(c1).get_attribute('data-status') == 'approved'
               and page.locator(c2).get_attribute('data-status') == 'rejected')
            ok('%s: a reload keeps the comment' % scheme, page.locator(c1 + ' textarea.note').input_value() == text)
            # import after clearing
            page.evaluate('localStorage.clear()')
            page.reload()
            page.wait_for_selector('.card[data-id]')
            ok('%s: cleared storage starts fresh' % scheme, page.locator(c1).get_attribute('data-status') == 'pending')
            page.click('#saveBtn')
            page.set_input_files('#importFile', path)
            page.wait_for_timeout(500)
            ok('%s: loading the saved file restores decisions' % scheme, page.locator(c1).get_attribute('data-status') == 'approved'
               and page.locator(c3).get_attribute('data-status') == 'revise', page.locator('#saveStatus').text_content())
            ok('%s: and the comment' % scheme, page.locator(c1 + ' textarea.note').input_value() == text)
            other = dict(saved, review_id='another-review')
            tmp = pathlib.Path(tempfile.mkdtemp()) / 'other.json'
            tmp.write_text(json.dumps(other), encoding='utf-8')
            page.set_input_files('#importFile', str(tmp))
            page.wait_for_timeout(400)
            ok('%s: answers for another review are refused' % scheme, 'nothing was loaded' in page.locator('#saveStatus').text_content(),
               page.locator('#saveStatus').text_content())
            page.click('#pasteToggle')
            page.fill('#pasteArea', '{not json')
            page.click('#pasteLoad')
            ok('%s: bad pasted text is refused' % scheme, "isn't a JSON" in page.locator('#saveStatus').text_content())
            ok('%s: no console or page errors' % scheme, not errors, errors[:3])
            ctx.close()
        # negative fixture: the 2026-10-23 defect (a white box, text colour left to the page) must fail the contrast check
        html = page_path.read_text(encoding='utf-8')
        start = html.index('/* review-form-controls-v1')
        end = html.index('</style>', start)
        # the browser picks light text for a form in a dark page (color-scheme), and the box is still white
        broken = html[:start] + ':root{color-scheme:light dark}textarea{background:#fff!important}' + html[end:]
        tmpdir = pathlib.Path(tempfile.mkdtemp())
        bad = tmpdir / 'broken.html'
        bad.write_text(broken, encoding='utf-8')
        ctx = browser.new_context(color_scheme='dark', viewport={'width': 1280, 'height': 900})
        page = ctx.new_page()
        page.goto(bad.as_uri())
        page.wait_for_selector('.card[data-id] textarea.note')
        t = page.locator('.card[data-id]:not(.leave) textarea.note').first
        t.click()
        t.type('invisible?')
        con = t.evaluate(CONTRAST_JS)
        ok('negative fixture: the old white-box defect fails the check (contrast %.1f)' % con['ratio'], con['ratio'] < 4.5, con)
        ctx.close()
        # phone width
        ctx = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True)
        page = ctx.new_page()
        page.goto(url)
        page.wait_for_selector('.card[data-id]')
        sw = page.evaluate('() => [document.documentElement.scrollWidth, window.innerWidth]')
        ok('phone width: no sideways scroll', sw[0] <= sw[1] + 1, sw)
        ctx.close()
        browser.close()
    rep = {'page': str(page_path), 'passed': len(results) - len(failures), 'failed': len(failures), 'results': results,
           'not_tested': ['the artifact store (db) and the downloads capability, which only exist inside claude.ai; the page falls back to this browser\'s storage and an ordinary download, tested here',
                          'a real phone browser (tested at phone width in Chromium)']}
    if report_path:
        pathlib.Path(report_path).write_text(json.dumps(rep, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d passed, %d failed' % (rep['passed'], rep['failed']))
    return 1 if failures else 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('page')
    ap.add_argument('--report')
    a = ap.parse_args()
    sys.exit(run(a.page, a.report))
