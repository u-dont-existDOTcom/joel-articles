#!/usr/bin/env python3
"""decision_page_browser_test.py - the review page's behaviour in a real browser (UDA patterns/owner-questions-page.md:
"Before claiming success, test typing, visible contrast, approval/rejection/revision, filtering, JSON download and parse,
and importing a prior response").

  python3 tools/humanization/decision_page_browser_test.py PAGE.html [--json OUT.json]

Opens PAGE.html from disk in Chromium (Playwright), light and then dark, and checks: no script errors; one card an item;
typed text in a note keeps its value and reads at 4.5:1 or more (text, caret and placeholder against the field) in both
themes, with every field, select and option measured the same way; Approve, Revise and Reject each set their card's
status; the status filter and the search narrow the list; Copy JSON gives JSON that parses, with the review's identity and
the typed note; decisions survive a reload; Clear all takes two clicks; the export imports back; an export for another
review is refused. Prints one line a check and exits 1 if any fails."""
import argparse
import json
import pathlib
import sys

CONTRAST = """() => {
  const lum=s=>{const v=s.match(/[\\d.]+/g).slice(0,3).map(Number).map(x=>x/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return v[0]*.2126+v[1]*.7152+v[2]*.0722;};
  const ratio=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);};
  const bad=[];let count=0,min=100;
  for(const el of document.querySelectorAll('textarea,select,option,input[type=search],input[type=text]')){
    const s=getComputedStyle(el);count++;
    if(s.backgroundColor==='rgba(0, 0, 0, 0)'){bad.push({id:el.id,reason:'transparent field background'});continue;}
    const colors=[s.color,s.webkitTextFillColor||s.color];
    if(el.matches('input,textarea'))colors.push(s.caretColor,getComputedStyle(el,'::placeholder').color);
    for(const color of colors){const r=ratio(color,s.backgroundColor);min=Math.min(min,r);if(r<4.5)bad.push({id:el.id,tag:el.tagName,color,bg:s.backgroundColor,contrast:r});}
  }return {count,minContrast:min,bad};
}"""


def run(page_path, timeout_ms=20000):
    from playwright.sync_api import sync_playwright
    results = []

    def check(name, ok, detail=''):
        results.append({'check': name, 'ok': bool(ok), 'detail': detail})

    url = pathlib.Path(page_path).resolve().as_uri()
    spec = None
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for scheme in ('light', 'dark'):
            ctx = browser.new_context(color_scheme=scheme, accept_downloads=True)
            ctx.add_init_script("Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async t=>{window.__clip=String(t);}}});")
            # the page needs nothing from the network (its fonts have fallbacks), so every request off the disk is blocked
            ctx.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
            page = ctx.new_page()
            page.set_default_timeout(timeout_ms)
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            page.on('console', lambda m: errors.append(m.text) if m.type == 'error' and not m.text.startswith('Failed to load resource') else None)
            page.goto(url)
            spec = page.evaluate("JSON.parse(document.getElementById('review-data').textContent)")
            ids = [x['id'] for x in spec['items']]
            n = page.locator('article.card').count()
            check('%s: one card an item' % scheme, n == len(ids), '%d cards, %d items' % (n, len(ids)))
            first, second, third = ids[0], ids[1 % len(ids)], ids[2 % len(ids)]
            note = page.locator('#note-' + first)
            note.fill('Typed in the %s theme: keep the last line.' % scheme)
            check('%s: the typed note keeps its value' % scheme, note.input_value().startswith('Typed in the %s theme' % scheme))
            c = page.evaluate(CONTRAST)
            check('%s: every field reads at 4.5:1 or more' % scheme, not c['bad'] and c['count'] > 0,
                  '%d fields, lowest %.2f%s' % (c['count'], c['minContrast'], (', failing: %s' % c['bad'][:3]) if c['bad'] else ''))
            bg = page.evaluate("getComputedStyle(document.body).backgroundColor")
            check('%s: the page has its own background' % scheme, bg not in ('rgba(0, 0, 0, 0)', 'transparent'), bg)
            page.click('#d-%s-approved' % first)
            if second != first:
                page.click('#d-%s-needs_revision' % second)
            if third not in (first, second):
                page.click('#d-%s-rejected' % third)
            st = page.evaluate("[...document.querySelectorAll('article.card')].slice(0,3).map(c=>c.dataset.status)")
            want = ['approved', 'needs_revision', 'rejected'][:min(3, len(ids))]
            check('%s: Approve, Revise and Reject set the status' % scheme, st[:len(want)] == want, str(st))
            page.select_option('#fstatus', 'approved')
            vis = page.evaluate("[...document.querySelectorAll('article.card')].filter(c=>!c.hidden).map(c=>c.dataset.id)")
            check('%s: the status filter shows only approved items' % scheme, vis == [first], str(vis))
            page.select_option('#fstatus', '')
            word = spec['items'][-1]['id']
            page.fill('#search', word)
            vis = page.evaluate("[...document.querySelectorAll('article.card')].filter(c=>!c.hidden).map(c=>c.dataset.id)")
            check('%s: the search narrows the list' % scheme, vis and vis[0] == word and len(vis) < len(ids), '%r: %d shown' % (word, len(vis)))
            page.fill('#search', '')
            page.click('#copyJson')
            page.wait_for_function('window.__clip !== undefined')
            exported = json.loads(page.evaluate('window.__clip'))
            got = {x['id']: x for x in exported['items']}
            check('%s: Copy JSON parses, with the identity, statuses and note' % scheme,
                  exported['review_id'] == spec['review_id'] and exported['source_sha256'] == spec['source_sha256']
                  and got[first]['status'] == 'approved' and got[first]['note'].startswith('Typed in the %s theme' % scheme)
                  and len(got) == len(ids) and exported.get('exported_utc'), json.dumps(exported['counts']))
            with page.expect_download() as d:
                page.click('#downloadJson')
            dl = json.loads(pathlib.Path(d.value.path()).read_text(encoding='utf-8'))
            check('%s: Download JSON gives the same decisions (from a file on disk)' % scheme, {x['id']: x['status'] for x in dl['items']} == {k: v['status'] for k, v in got.items()})
            page.reload()
            st2 = page.evaluate("document.getElementById('item-%s').dataset.status" % first)
            check('%s: decisions survive a reload' % scheme, st2 == 'approved', st2)
            page.click('#clearAll')
            once = page.evaluate("document.getElementById('item-%s').dataset.status" % first)
            page.click('#clearAll')
            twice = page.evaluate("[...document.querySelectorAll('article.card')].every(c=>c.dataset.status==='pending')")
            check('%s: Clear all takes two clicks' % scheme, once == 'approved' and twice, 'after one: %s' % once)
            page.fill('#importBox', json.dumps(exported))
            page.click('#importText')
            st3 = page.evaluate("document.getElementById('item-%s').dataset.status" % first)
            n3 = page.locator('#note-' + first).input_value()
            check('%s: the export imports back, notes included' % scheme, st3 == 'approved' and n3.startswith('Typed'), page.inner_text('#statusLine'))
            wrong = dict(exported, review_id='another-review')
            page.fill('#importBox', json.dumps(wrong))
            page.click('#importText')
            msg = page.inner_text('#statusLine')
            check('%s: an export for another review is refused' % scheme, msg.startswith('Not imported'), msg)
            check('%s: no script errors' % scheme, not errors, '; '.join(errors[:3]))
            ctx.close()
        browser.close()
    return results


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('page')
    ap.add_argument('--json')
    a = ap.parse_args(argv)
    results = run(a.page)
    for r in results:
        print('%s %s%s' % ('PASS' if r['ok'] else 'FAIL', r['check'], (' (%s)' % r['detail']) if r['detail'] else ''))
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(results, indent=1) + '\n', encoding='utf-8')
    return 0 if all(r['ok'] for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())
