#!/usr/bin/env python3
"""suggestion_review_browser_test.py - a real browser test of a suggestion review page (suggestion_review.py's).

  python3 tools/humanization/suggestion_review_browser_test.py PAGE.html [--report OUT.json]

What it does, in Chromium (Playwright), on the exact file it's given, opened as a local file:
  - no console errors or page errors, in light and in dark colour schemes;
  - typed text in a comment box, and in a "Your version" box, is legible: the computed text and background colours of
    the box have a contrast of at least 4.5, under light and dark preferences; a negative fixture (the 2023-10-23 white
    box with no text colour) must fail the same check, so the check can't pass by accident;
  - a pre-decided suggestion starts with its decision; every other one starts "Not approved yet";
  - Approve, Reject, Revise and "Undo my answer" are one click each, without a dialog; the progress counts explicit
    decisions; Revise opens "Your version" filled with my version;
  - "Undo my answer" shows only on a card he has answered, says what it does, and takes the card back to undecided
    (1.11; Joel, 2026-11-11 19:54 UTC: "can you durably fix this cards thing because 'not approved yet' doesn't work as
    a button": the button was labelled with a state, and showed, pressed, on every undecided card, where a click did
    nothing);
  - the type filters, the status filter, the search and "The ones I'd leave" toggle hide and show the right cards;
  - every changed paragraph shows as two clean texts, as it is now and as it would read, each exactly that version (so a
    paste can't run them together, E266 (Inner Child)), and a passage shown whole reads exactly as my version;
  - a question card takes an answer, says Answered, counts it apart from the decisions and exports it;
  - a stretch to edit (advice "edit") keeps in one click, opens "Your version" filled with the paragraph as it is, and
    counts apart from the suggestions; every highlight in the article has its type's colour;
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


def settle(page, limit_ms=5000):
    """Wait until a smooth scroll has stopped (scrollY unchanged for 300 ms): a jump of several thousand pixels can take
    longer than a fixed wait, and a check read mid-scroll sees the card still below the bar (2026-11-03, the gut page)."""
    last, still, waited = None, 0, 0
    while waited < limit_ms:
        y = page.evaluate('scrollY')
        still = still + 100 if y == last else 0
        if still >= 300:
            return
        last = y
        page.wait_for_timeout(100)
        waited += 100

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
            # Approve, Reject and Revise are tried on three cards; a page of two (2026-11-02, Hypnosis Guide Cards, 2 November
            # (2), after the gate held its third card back) tries Revise on the rejected card, so it ends as revise
            three = len(ids) >= 3
            # a page with fewer than two cards to approve (2026-11-03, Hypnosis Guide Cards, 3 November: one stretch of his
            # to edit and nothing else) runs the same checks on its first stretch to edit: a comment, Keep and Edit, the
            # export, the reload and the import
            edit_only = len(ids) < 2
            if edit_only:
                eds0 = [s['id'] for s in data['suggestions'] if s['advice'] == 'edit']
                if not eds0 and len(ids) == 1:
                    # a page of one suggestion to approve and nothing else (the bad trips guide's round 9, 2026-11-06: his
                    # exercise, one card) runs the same checks on that card, its Revise standing in for Edit
                    ok('%s: a page of one suggestion to approve, no stretches to edit' % scheme, True)
                    eds0 = ids[:]
                else:
                    ok('%s: a page of stretches to edit (%d), no suggestions to approve' % (scheme, len(eds0)), len(eds0) >= 1, eds0)
                ids = eds0[:1] * 2
            c1, c2 = ('#c-' + i.replace('.', '\\.') for i in ids[:2])
            c3 = '#c-' + ids[2].replace('.', '\\.') if three else c2
            id3 = ids[2] if three else ids[1]
            n_dec = 3 if three else 2
            st2 = 'rejected' if three else 'revise'
            note = page.locator(c1 + ' textarea.note')
            text = 'Keep "this" — and check the link, please. Ünïcode ok.'
            note.click()
            note.type(text)
            ok('%s: typed comment kept' % scheme, note.input_value() == text, note.input_value())
            con = note.evaluate(CONTRAST_JS)
            ok('%s: comment text legible (contrast %.1f)' % (scheme, con['ratio']), con['ratio'] >= 4.5, con)
            if not edit_only:
                ok('%s: no undo button on an undecided card' % scheme,
                   page.locator(c1).get_attribute('data-status') != 'pending' or not page.locator(c1 + ' .dec.undo').is_visible())
                page.click(c1 + ' .dec.approve')
                und = page.locator(c1 + ' .dec.undo')
                ok('%s: once answered, a button that says what it does' % scheme,
                   und.is_visible() and und.text_content() == 'Undo my answer', und.text_content())
                ok('%s: Approve is one click, no dialog' % scheme, page.locator(c1).get_attribute('data-status') == 'approved')
                ok('%s: pill says Approved' % scheme, page.locator(c1 + ' .pill').text_content() == 'Approved')
                page.click(c2 + ' .dec.reject')
                ok('%s: Reject' % scheme, page.locator(c2).get_attribute('data-status') == 'rejected')
                ok('%s: rejected looks different from not approved' % scheme,
                   page.locator(c2 + ' .pill').text_content() != 'Not approved yet')
                page.click(c3 + ' .dec.revise')
                yours = page.locator(c3 + ' textarea.yours')
                ok('%s: Revise opens your version' % scheme, yours.is_visible())
                mine = next(s['proposed'] for s in data['suggestions'] if s['id'] == id3)
                ok('%s: your version starts from mine' % scheme, yours.input_value() == mine, yours.input_value()[:80])
                yours.type(' Mine.')
                con2 = yours.evaluate(CONTRAST_JS)
                ok('%s: your-version text legible (contrast %.1f)' % (scheme, con2['ratio']), con2['ratio'] >= 4.5, con2)
                pre_ap = sum(1 for s in pre if s['advice'] == 'approve' and s['decided']['status'] == 'approved')
                pre_n = sum(1 for s in pre if s['advice'] == 'approve')
                prog = page.locator('#prog').text_content()
                ok('%s: progress counts the decisions' % scheme,
                   (' %d approved' % (1 + pre_ap) in prog) and prog.startswith('%d of' % (n_dec + pre_n)), prog)
                page.click(c1 + ' .dec.undo')
                ok('%s: back to not approved in one click' % scheme, page.locator(c1).get_attribute('data-status') == 'pending')
                ok('%s: and the undo button goes away' % scheme, not page.locator(c1 + ' .dec.undo').is_visible())
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
                # a word some cards have and others don't, from the cards themselves
                hay = page.evaluate("""() => Array.from(document.querySelectorAll('.card[data-id]')).map(c => { const b = document.getElementById('b' + c.dataset.block); return (c.textContent + ' ' + (b ? b.textContent : '')).toLowerCase(); })""")
                words = sorted({w for h in hay for w in __import__('re').findall(r'[a-z]{7,}', h)})
                word = next((w for w in words if 0 < sum(w in h for h in hay) < len(hay) // 2 + 1), words[0] if words else 'the')
                page.fill('#search', word)
                page.wait_for_timeout(400)
                shown = page.evaluate("""() => Array.from(document.querySelectorAll('.card[data-id]')).filter(c => !c.hidden).length""")
                ok('%s: search narrows the cards' % scheme, 0 < shown < total, shown)
                page.fill('#search', '')
                page.wait_for_timeout(400)
            else:
                # the type filter, on the stretch to edit (one card: nothing for the status filter or the search to narrow)
                page.click('#toolsBtn')
                typ = data['suggestions'][[s['id'] for s in data['suggestions']].index(ids[0])]['type']
                page.click('.tools [data-filter-type="%s"]' % typ)
                ok('%s: type filter hides that type' % scheme, not page.locator(c1).is_visible())
                page.click('.tools [data-filter-type="%s"]' % typ)
                ok('%s: and shows it again' % scheme, page.locator(c1).is_visible())
            if page.locator('.card.leave').count():
                leave = page.locator('.card.leave').first
                ok('%s: the ones I\'d leave are hidden at first' % scheme, not leave.is_visible())
                page.check('#showLeave')
                ok('%s: and show when ticked' % scheme, leave.is_visible())
                page.uncheck('#showLeave')
            else:
                ok('%s: no cards I\'d leave on this page, so nothing to hide' % scheme, True)
            page.click('#toolsBtn')
            # each version clean (E266 (Inner Child)): one changed paragraph's two sides, a whole passage's paragraphs
            sides = page.evaluate("""() => Array.from(document.querySelectorAll('.card[data-id]')).map(c => ({id: c.dataset.id,
                now: Array.from(c.querySelectorAll('.side.now')).map(x => x.textContent),
                after: Array.from(c.querySelectorAll('.side.after')).map(x => x.textContent),
                reads: Array.from(c.querySelectorAll('.reads .rd')).map(x => x.textContent)}))""")
            sug = {x['id']: x for x in data['suggestions']}
            one = [x for x in sides if x['after'] and not x['reads']]
            # each side is one whole version: in my version, or in the text as it is now, word for word
            bad = [x['id'] for x in one if not all(t in sug[x['id']]['proposed'] for t in x['after'])
                   or not all(t in sug[x['id']]['before'] for t in x['now'])]
            ok('%s: each changed paragraph shows as two clean texts (%d cards)' % (scheme, len(one)), not bad, bad[:5])
            whole = [x for x in sides if x['reads']]
            badr = [x['id'] for x in whole if '\n\n'.join(x['reads']) != sug[x['id']]['proposed']]
            ok('%s: a passage shown whole reads as my version (%d cards)' % (scheme, len(whole)), not badr, badr[:5])
            asks = [x['id'] for x in data['suggestions'] if x['advice'] == 'ask']
            if asks:
                qa = '#c-' + asks[0].replace('.', '\\.')
                ans = 'From people I\'ve talked to.'
                page.locator(qa + ' textarea.note').fill(ans)
                page.wait_for_timeout(200)
                ok('%s: a question card says Answered' % scheme, page.locator(qa + ' .pill').text_content() == 'Answered',
                   page.locator(qa + ' .pill').text_content())
                ok('%s: answers count apart from decisions' % scheme, ('1 of %d questions answered' % len(asks)) in page.locator('#prog').text_content(),
                   page.locator('#prog').text_content())
            # a stretch to edit (advice "edit", 2026-10-27): Keep is one click, Edit opens his version filled with the
            # paragraphs as they are, and the progress counts them apart from the suggestions
            eds = [x['id'] for x in data['suggestions'] if x['advice'] == 'edit']
            if eds:
                e1 = '#c-' + eds[0].replace('.', '\\.')
                page.click(e1 + ' .dec.reject')
                ok('%s: Keep on a stretch to edit' % scheme, page.locator(e1).get_attribute('data-status') == 'rejected'
                   and page.locator(e1 + ' .pill').text_content() == 'Keep as it is', page.locator(e1 + ' .pill').text_content())
                page.click(e1 + ' .dec.revise')
                ey = page.locator(e1 + ' textarea.yours')
                now = next(x['proposed'] for x in data['suggestions'] if x['id'] == eds[0])
                ok('%s: Edit opens your version, filled with the paragraph as it is' % scheme,
                   ey.is_visible() and ey.input_value() == now, ey.input_value()[:80])
                ok('%s: stretches to edit count apart' % scheme,
                   ('of %d stretches looked at' % len(eds)) in page.locator('#prog').text_content(), page.locator('#prog').text_content())
                page.click(e1 + ' .dec.undo')
            # every highlight shows in its type's colour (2026-10-27: four types the template didn't know showed none)
            # (a quiet one I'd leave, and one already decided, are transparent on purpose)
            bare = page.evaluate("""() => Array.from(document.querySelectorAll('mark.hl:not(.leave):not(.done)')).filter(m => {
                const b = getComputedStyle(m).backgroundColor; return !b || b === 'transparent' || b === 'rgba(0, 0, 0, 0)'; }).length""")
            ok('%s: every highlight has a colour' % scheme, bare == 0, '%d without one' % bare)
            # next undecided (on a small page the clicks above can leave no card undecided, so the first card is set back
            # to undecided first: 2026-11-02, the three-card page read 0 here while the button worked on a fresh page)
            # the first decision card: a question card has no undo button, so a page that opens on a question (the
            # bad-trips guide's structure question, 2026-11-03) timed out here
            # a page of edit cards only has no approve card (the gut fuels' help page, 2026-11-04): take the first card
            # that has an undo button, and leave the reset out when none has
            first, was = None, 'pending'
            for s in [s for s in data['suggestions'] if s['advice'] in ('approve', 'leave')] + \
                     [s for s in data['suggestions'] if s['advice'] == 'edit']:
                if page.locator('#c-' + s['id'].replace('.', '\\.') + ' .dec.undo').count():
                    first = s['id'].replace('.', '\\.')
                    was = page.locator('#c-' + first).get_attribute('data-status')
                    if was != 'pending':
                        page.click('#c-' + first + ' .dec.undo')
                    break
            page.evaluate('window.scrollTo(0, 0)')
            page.click('#nextBtn')
            # wait for the smooth scroll to end, not a fixed 900 ms: on a long page the first undecided card can be
            # 13,000 px down (the bad-trips guide's round 1, 2026-11-03), and the scroll was still under way at 900 ms
            last = -1
            for _ in range(40):
                page.wait_for_timeout(250)
                y = page.evaluate('Math.round(window.scrollY)')
                if y == last:
                    break
                last = y
            top = page.evaluate("""() => { const cs = Array.from(document.querySelectorAll('.card[data-id]')).filter(c => !c.hidden && c.offsetParent && c.dataset.status==='pending'); const vis = cs.map(c => c.getBoundingClientRect().top).filter(t => t > -5 && t < 400); return vis.length }""")
            ok('%s: Next undecided brings one to the top' % scheme, top >= 1, top)
            # Next walks the undecided cards in the order they stand on the page, questions included (Joel, 2026-11-03
            # 19:12 UTC: "your next button is skipping questions fix that"; it followed REVIEW.json's order, which listed
            # the question cards last). Only cards the page can scroll to the top are counted.
            page.evaluate('window.scrollTo(0, 0)')
            page.wait_for_timeout(300)
            want = page.evaluate("""() => { const lim = document.documentElement.scrollHeight - innerHeight + 100;
                return Array.from(document.querySelectorAll('.card[data-id]')).filter(c => !c.hidden && c.offsetParent
                    && c.dataset.status === 'pending' && c.getBoundingClientRect().top + scrollY < lim).map(c => c.dataset.id); }""")
            got = []
            for _ in range(len(want)):
                # a scripted click, as a reader's: Playwright's own click first scrolls the page to show the button, which
                # moves the card just reached below the bar again, so Next would pick it a second time (2026-11-03)
                page.evaluate("document.getElementById('nextBtn').click()")
                settle(page)
                got.append(page.evaluate("""() => { let best = null, d = 1e9; document.querySelectorAll('.card[data-id]').forEach(c => {
                    if (c.hidden || !c.offsetParent) return; const t = Math.abs(c.getBoundingClientRect().top - 120);
                    if (t < d) { d = t; best = c.dataset.id; } }); return best; }"""))
            ok('%s: Next walks every undecided card in page order, questions included' % scheme, got == want,
               'expected %s, got %s' % (want, got))
            if was != 'pending':   # the first card's decision back, for the export and reload checks after this
                page.click('#c-' + first + ' .dec.' + {'approved': 'approve', 'rejected': 'reject', 'revise': 'revise'}[was])
            if edit_only:   # the stretch edited, for the export, reload and import checks below
                page.click(c1 + ' .dec.revise')
                page.locator(c1 + ' textarea.yours').type(' Mine.')
            first_status = 'revise' if edit_only else 'approved'
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
                ok('%s: statuses exported' % scheme, got[ids[0]]['status'] == first_status and got[ids[1]]['status'] == st2
                   and got[id3]['status'] == 'revise' and got[id3]['your_version'].endswith(' Mine.'))
                if asks:
                    ok('%s: the answer is exported with its question' % scheme, got[asks[0]]['comment'] == ans
                       and got[asks[0]]['status'] == 'answered' and got[asks[0]].get('question'), got[asks[0]])
            with page.expect_download() as dl:
                page.click('#saveJson')
            path = dl.value.path()
            saved = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
            ok('%s: Save downloads the answers' % scheme, len(saved['items']) == total and saved['review_id'] == data['review_id'])
            # reload keeps it
            page.reload()
            page.wait_for_selector('.card[data-id]')
            ok('%s: a reload keeps the decisions' % scheme, page.locator(c1).get_attribute('data-status') == first_status
               and page.locator(c2).get_attribute('data-status') == st2)
            ok('%s: a reload keeps the comment' % scheme, page.locator(c1 + ' textarea.note').input_value() == text)
            # import after clearing
            page.evaluate('localStorage.clear()')
            page.reload()
            page.wait_for_selector('.card[data-id]')
            ok('%s: cleared storage starts fresh' % scheme, page.locator(c1).get_attribute('data-status') == 'pending')
            page.click('#saveBtn')
            page.set_input_files('#importFile', path)
            page.wait_for_timeout(500)
            ok('%s: loading the saved file restores decisions' % scheme, page.locator(c1).get_attribute('data-status') == first_status
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
