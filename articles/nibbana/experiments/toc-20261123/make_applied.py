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
    if not e['heading'] or (e['heading'] == e['was'] and e['level'] == e['was_level']):
        continue
    if 'held' in e:
        continue
    who = whose.get(picks.get(e['id']), 'the proposal')
    if e['heading'] == e['was']:
        who = 'his words, a new level'
    lvl = '' if e['level'] == e['was_level'] else ' (now %s, was %s)' % ('#' * e['level'], '#' * e['was_level'])
    rows.append('| %s | %s | %s%s | %s |' % (e['id'], e['was'].replace('|', '\\|'), sec(e['id']), lvl, who))

md = ['# His contents picks, in the post (2026-11-23)', '',
      'His answers on the picks page (2026-11-23 17:24 UTC, [the record](%sexperiments/toc-20261123/answers/JOEL-20261123-1724.json)) '
      'went into [the post](%s) at 18:01:47 UTC, as one change in the editor '
      '([apply_in_editor.js](%sexperiments/toc-20261123/apply_in_editor.js), from [PLAN.json](%sexperiments/toc-20261123/PLAN.json)). '
      'Checked afterwards on the live post: all 58 headings and their levels as planned, every heading has its anchor, '
      'and every new link lands on a heading.' % (GIT, POST, GIT, GIT), '',
      '## Two of his picks wait for him', '',
      'Both read below High in Pangram in their sections, so they kept their headings (his rule: nothing goes in below High '
      'confidence). The section itself moved where he said.', '']
for e in plan['sections']:
    if 'held' in e:
        md.append('- %s: his pick "%s" read Human Low (%s); his heading as it is reads %s. Its section %s.' % (
            sec(e['id']), e['held']['his_pick'], e['held']['why'].split('(')[-1].rstrip(')'),
            {'S055': 'Medium with its first sentence', 'S060': 'High'}[e['id']],
            'moved after ' + sec('S056') + ', as he said' if e['id'] == 'S060' else 'stayed where it was'))
md += ['', '## Headings', '', '| Section | His heading before | Now | Whose |', '|---|---|---|---|'] + rows
md += ['', '## Structure and lines (his answers)', '',
       '- "Realization Isn\'t Enough" (###) is gone: its text sits under %s, with %s still under it as ###.' % (sec('S022'), sec('S024')),
       '- %s and %s are ## now; %s sits under %s.' % (sec('S008'), sec('S018'), sec('S019'), sec('S018')),
       '- %s opens with his blessing, "🫶🏿 May All Beings Be Loving, Peaceful & Free 🫶🏿", and %s with "Your fingers are already enlightened, but your hand is deluded."' % (sec('S008'), sec('S018')),
       '- "Appendix" is gone; its one section, %s, follows %s.' % (sec('S060'), sec('S056')),
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
        'NB-toc-S060-before#40': 'the same section as it was'}
for k in what:
    r = results.get(k)
    if r:
        md.append('| [%s](%s) | %s | %s | %s |' % (k, r['link'], what[k], r.get('headline', r['verdict']), (r.get('shading') or '').replace('|', '\\|')))
md += ['', 'The first whole check ([NB-toc-whole#31](%shumanize/pangram-ledger.jsonl)) was voided: its text had a space at every tag boundary.' % GIT, '']
open(os.path.join(HERE, 'APPLIED.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('APPLIED.md:', len(rows), 'headings,', len(cat['links']), 'links,', sum(1 for k in what if k in results), 'Pangram results')
