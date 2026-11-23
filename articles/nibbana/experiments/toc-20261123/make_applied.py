#!/usr/bin/env python3
"""APPLIED.md: what his contents picks of 2026-11-23 put into his live post, from PLAN.json, his answers, the section-link
catalog (../../SECTION-LINKS.json) and the Pangram ledger (../../humanize/pangram-ledger.jsonl). Every section it names
links to its anchor on the live post (lesson toc-2026-11-23b).

  python3 make_applied.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

POST = 'https://ibogaqueen.substack.com/p/what-if-everything-is-already-perfect-bdc'
GIT = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/nibbana/'
plan = json.load(open(os.path.join(HERE, 'PLAN.json'), encoding='utf-8'))
ans = json.load(open(os.path.join(HERE, 'answers', 'JOEL-20261123-1724.json'), encoding='utf-8'))
cat = json.load(open(os.path.join(HERE, '..', '..', 'SECTION-LINKS.json'), encoding='utf-8'))
ledger = [json.loads(l) for l in open(os.path.join(HERE, '..', '..', 'humanize', 'pangram-ledger.jsonl'), encoding='utf-8') if l.strip()]
anchor = {h['id']: h['anchor'] for h in cat['headings']}
text = {h['id']: h['text'] for h in cat['headings']}


def sec(i, words=None):
    """A section's name linked to its anchor on the live post."""
    return '[%s](%s/i/%s/%s)' % ((words or text[i]).replace('|', '\\|'), cat['post']['base'], cat['post']['id'], anchor[i])


def fits(t, lvl):
    f, shown, w, room = ts.shown(t, lvl)
    return 'cut off' if not f else ('only just fits' if room - w < 12 else 'fits')


results = {}
preds = {}
for r in ledger:
    if r.get('type') == 'prediction' and str(r.get('lineage', '')).startswith('NB-toc'):
        preds[r['sha256']] = r
    if r.get('type') == 'result' and str(r.get('prediction', '')).startswith('NB-toc'):
        results[r['prediction']] = r
whose = {'own': 'his own words', 'fable': "Fable's", 'now': 'his, kept'}
picks = ans['picks']
rows = []
for e in plan['sections']:
    if not e['heading'] or (e['heading'] == e['was'] and e['level'] == e['was_level'] and 'held' not in e):
        continue
    who = whose.get(picks.get(e['id']), 'the proposal')
    if 'held' in e:
        who = 'his own words (his second pick, 19:46 UTC)'
    if e['heading'] == e['was'] and 'held' not in e:
        who = 'his words, a new level'
    lvl = '' if e['level'] == e['was_level'] else ' (now %s, was %s)' % ('#' * e['level'], '#' * e['was_level'])
    rows.append('| %s | %s | %s%s | %s |' % (e['id'], e['was'].replace('|', '\\|'), sec(e['id']), lvl, who))

md = ['# His contents picks, in the post (2026-11-23)', '',
      'His answers on the picks page (2026-11-23 17:24 UTC, [the record](%sexperiments/toc-20261123/answers/JOEL-20261123-1724.json)) '
      'went into [the post](%s) at 18:01:47 UTC, as one change in the editor '
      '([apply_in_editor.js](%sexperiments/toc-20261123/apply_in_editor.js), from [PLAN.json](%sexperiments/toc-20261123/PLAN.json)). '
      'Checked afterwards on the live post: all 58 headings and their levels as planned, every heading has its anchor, '
      'and every new link lands on a heading.' % (GIT, POST, GIT, GIT), '',
      '## Later that evening', '',
      '- 19:39 UTC: he published the draft that put %s back at the end, after %s: moved into the manual, its first two '
      'sentences had read AI in the whole check ([NB-toc-live#41](%s), one window with High confidence); at the end they read '
      'Human High ([NB-toc-live-END#43](%s)).' % (sec('S060'), sec('S058'), results['NB-toc-live#41']['link'], results['NB-toc-live-END#43']['link']),
      '- 19:46 UTC: his second picks for the two headings whose first picks had read Human Low as windows of their own, '
      '%s ([NB-toc-S055#44](%s)) and %s ([NB-toc-S060#45](%s)); his ruling (19:42 UTC): the heading\'s own window may read '
      'Low, the body text must read High (lesson toc-2026-11-23c). Both bodies read High, and the whole post with them '
      '([NB-toc-final#46](%s)) has nothing below High in either section.' % (sec('S055'), results['NB-toc-S055#44']['link'],
      sec('S060'), results['NB-toc-S060#45']['link'], results['NB-toc-final#46']['link']), '',
      '## Body text that reads lower than in the morning', '',
      'The whole post as it is now ([NB-toc-final#46](%s): 47 Human High, 41 Medium, 7 Low, 1 AI Low) against the post '
      'that morning ([NB-toc-before#34](%s): 49 High, 43 Medium, 7 Low, 3 AI Low). The three AI windows of the morning '
      'read Human Medium now; three body windows of his read lower:' % (results['NB-toc-final#46']['link'], results['NB-toc-before#34']['link']), '',
      '- "Stream entry’s greatest prize is a “release date”..." (21 words), the first sentence under %s: High in the morning, AI Low now. The new heading splits it into a window of its own.' % sec('S051'),
      '- "A false attainment claim brings Pārājika 4..." (12 words), mid-section in %s: Medium, now Low.' % sec('S010'),
      '- "I believe the Dhammapada is right to call unbinding the foremost ease..." (30 words), mid-section in %s: Medium, now Low.' % sec('S017'),
      '', 'The last two are mid-section, away from any changed heading: the whole post is split into windows differently.']
md += ['', '## Headings', '', '| Section | His heading before | Now | Whose |', '|---|---|---|---|'] + rows
md += ['', '## Structure and lines (his answers)', '',
       '- "Realization Isn\'t Enough" (###) is gone: its text sits under %s, with %s still under it as ###.' % (sec('S022'), sec('S024')),
       '- %s and %s are ## now; %s sits under %s.' % (sec('S008'), sec('S018'), sec('S019'), sec('S018')),
       '- %s opens with his blessing, "🫶🏿 May All Beings Be Loving, Peaceful & Free 🫶🏿", and %s with "Your fingers are already enlightened, but your hand is deluded."' % (sec('S008'), sec('S018')),
       '- "Appendix" is gone; its one section, %s, is at the end, after %s (see 19:39 above).' % (sec('S060'), sec('S058')),
       '- In %s, "both of us were really desperate" is now "both Bāhiya and I were really desperate": the heading he picked no longer says "For Me & Bāhiya" (rule 9).' % sec('S015'),
       '', '## Links to sections (gate inner-child-2026-11-20c)', '', '| In | Words | Goes to |', '|---|---|---|']
for l in cat['links']:
    md.append('| %s | %s | %s |' % (sec(l['in']), l['text'], sec(l['target'])))
md += ['', 'Left unlinked on purpose:', '']
for u in cat['unlinked_on_purpose']:
    md.append('- %s, "%s": %s.' % (sec(u['in']) if u['in'] in anchor else u['in'], u['text'], u['why']))
md += ['', '## Pangram (web app, his account)', '',
       'Each check reads the text as readers see the post ([check_texts.py](%sexperiments/toc-20261123/check_texts.py)); predictions came first, in '
       '[the ledger](%shumanize/pangram-ledger.jsonl).' % (GIT, GIT), '', '| Check | What | Result | Windows |', '|---|---|---|---|']
what = {'NB-toc-whole#32': 'the whole post with his picks (before the two holds)', 'NB-toc-before#34': 'the whole post as it was',
        'NB-toc-S015#33': 'the S015 fix with its heading', 'NB-toc-S051#35': 'Who Gets Reborn? in its section',
        'NB-toc-S051-before#38': 'the same section as it was', 'NB-toc-S055#36': 'his pick Did It Work or Go Wrong? in its section',
        'NB-toc-S055-before#39': 'the same section as it was', 'NB-toc-S060#37': 'his pick Is It Safe When "I" Vanish? in its section',
        'NB-toc-S060-before#40': 'the same section as it was', 'NB-toc-live#41': 'the post as published at 18:01:47 UTC',
        'NB-toc-live-END-APPENDIX#42': 'the same with the flashbacks section back at the end under Appendix',
        'NB-toc-live-END#43': 'the same with the flashbacks section at the end, no Appendix (his publish, 19:39)',
        'NB-toc-S055#44': 'his second pick Checking If It Worked in its section', 'NB-toc-S060#45': 'his second pick Disappearing Flashbacks? in its section',
        'NB-toc-final#46': 'the whole post with both (published 19:46)'}
for k in what:
    r = results.get(k)
    if r:
        md.append('| [%s](%s) | %s | %s | %s |' % (k, r['link'], what[k], r.get('headline', r['verdict']), (r.get('shading') or '').replace('|', '\\|')))
md += ['', 'The first whole check ([NB-toc-whole#31](%shumanize/pangram-ledger.jsonl)) was voided: its text had a space at every tag boundary.' % GIT, '']
open(os.path.join(HERE, 'APPLIED.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('APPLIED.md:', len(rows), 'headings,', len(cat['links']), 'links,', sum(1 for k in what if k in results), 'Pangram results')
