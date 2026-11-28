#!/usr/bin/env python3
"""Write RESULTS.md (the run's record, which GitHub renders) and PAGE-OPTIONS.json (what make_page.py turns into Joel's
picks page) from this folder's scores, proposals, reads and fates. Every number comes from SCORES.json (score_reads.py)
and the reads' HARD lines; every section of his post that a note, question or table names links to its anchor on the
live post (section_links.py url; lesson toc-2026-11-23b), from the headings as they stand there now.

  python3 make_results.py [PAGE_URL]
  python3 make_page.py PAGE-OPTIONS.json PICKS-PAGE.html
"""
import copy, html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts
import section_links as sl

GIT = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/romance/experiments/toc-20261128/'
POST = 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents'
CATALOG = os.path.join(HERE, '..', '..', 'SECTION-LINKS.json')
RUNS = [  # key, label, contents file, reads, lines file
    ('now', 'Yours, as the sidebar shows it', None, ['READ-NOW-SIDEBAR-1.md', 'READ-NOW-SIDEBAR-2.md'], 'LINES-NOW.json'),
    ('nowfull', 'Yours, whole (nothing cut off)', None, ['READ-NOW-FULL-1.md'], 'LINES-NOW.json'),
    ('fable', "Fable's version", 'PROPOSAL-FABLE.json', ['READ-FABLE-1.md', 'READ-FABLE-2.md'], 'LINES-FABLE.json'),
    ('pick1', 'First proposal', 'PROPOSAL-PICK.json', ['READ-PICK-1.md', 'READ-PICK-2.md'], 'LINES-PICK.json'),
    ('pick2', 'Second (4 changed after its readers)', 'PROPOSAL-PICK2.json', ['READ-PICK2-1.md', 'READ-PICK2-2.md'], 'LINES-PICK2.json'),
    ('final', 'Final proposal (1 of those 4 back)', 'PROPOSAL-PICK3.json', ['READ-PICK3-1.md', 'READ-PICK3-2.md'], 'LINES-PICK3.json'),
]
YOURS = ('now', 'nowfull')
PICKS = ('pick1', 'pick2', 'final')
KINDS = {'fit': 'cut off in the sidebar', 'reader': 'named for what readers look for', 'case': 'capitals only',
         'retest': 'changed after the readers', 'kept': ''}

# The questions on the page. {L:Sxxx} is that section's heading on the live post, linked to it; {O:...} an outline
# (ids, with "=" for the heading as proposed and its new level after "@"); {F:Sxxx,...} how many readers marked any of
# those sections hard; {R:n,...} how many readers of the proposals went first to the right section for those situations.
QUESTIONS = [
    ('1. The top links',
     "<b>Your two links at the top are headings.</b> {L:S001} has no text, and {L:S002} sits over your opening: your dad's "
     "answer, why you wrote the guide, and who it's for. So the sidebar files the opening under the card game, and no reader of "
     "yours or Fable's looking for whether the advice applies to them, or how sure you are of it, found it (0 of 10 tries). "
     "In the proposals the opening has its own heading, <i>Who This Guide Is For</i>, with the card-game link kept as a heading "
     "just above it, named <i>Try My Couples Card Game</i>; then readers found it {R:41,42}. "
     "{O:now=S001,S002|would=S001@1:Ask an AI About This Guide,CTA@1:Try My Couples Card Game,S002@1:Who This Guide Is For} "
     "Which do you want? <b>(a)</b> That: both links stay headings, with the short names, and the opening gets its own "
     "(my pick, fairly sure: both links stay in the sidebar). <b>(b)</b> Both links become plain lines at the top, so the "
     "sidebar starts at <i>Who This Guide Is For</i> (the cleanest sidebar, but the links leave it). <b>(c)</b> The chat link "
     "stays a heading and the card-game link becomes a plain line. <b>(d)</b> Leave the top as it is, and pick yours or "
     "Fable's for that heading above."),
    ('2. Levels',
     "<b>Three of your # headings go straight to ### under them.</b> The sidebar indents by level, so those sit deeper than "
     "their neighbours, and readers of every version said the levels look broken ({F:S010,S011,S012,S035,S036,S037,S039,S040,S041,S068}). "
     "Raise each one a level, as below? It also gives each 12 pixels more room in the sidebar, and no heading's words change "
     "for it. My pick: yes, sure. "
     "{O:now=S009,S010,S011,S012,S013,S014,S015|would=S009,S010@2,S011@2,S012@2,S013@3,S014@3,S015} "
     "{O:now=S034,S035,S036,S037,S038,S039,S040,S041|would=S034,S035@2,S036@2,S037@2,S038@3,S039@2,S040@2,S041@2} "
     "{O:now=S067,S068,S069,S070|would=S067,S068@2,S069,S070}"),
    ('3. The casual-sex answer',
     "<b>The answer to {L:S006} sits at the end of {L:S008}.</b> Its last two paragraphs (“I can't decide what is okay for "
     "anybody else...” and “Outside a loving poly community or tribe, I think honest casual sex is almost impossible...”) "
     "answer the casual-sex question, and readers of every version said the labels heading sits under casual sex but reads "
     "as commitment ({F:S008}). <b>(a)</b> Give those two paragraphs a heading of their own, <i>When Is It Honest?</i>, "
     "after the labels section, so nothing moves (my pick, fairly sure). <b>(b)</b> Move them to the end of the casual-sex "
     "section's own text, before {L:S007}. <b>(c)</b> Leave them. Text that moves gets a Pangram check where it lands before "
     "it goes in. {O:now=S006,S007,S008|would=S006,S007,S008,NEW@3:When Is It Honest?}"),
    ('4. Exclusive or poly',
     "<b>{L:S056} holds two things.</b> It starts with jealousy, and from “I do believe two people can choose sexual "
     "exclusivity honestly” on, it's about choosing exclusivity or polyamory. Start a section of its own there, "
     "<i>Exclusive or Poly?</i>, after the jealousy part? Nothing moves. My pick: yes, fairly sure. "
     "{O:now=S054,S055,S056|would=S054,S055,S056,NEW@3:Exclusive or Poly?}"),
    ('5. The Missing Middle',
     "<b>{L:S019} sits under {L:S015}.</b> It's about a stage between being interested in someone and sleeping with them: "
     "how a relationship starts, not how to find one. Readers said it sits in the wrong place, and that it competes with "
     "{L:S005} for the slow stage before sex ({F:S019}). Move it to be the first section under {L:S020}, which has no text "
     "of its own and goes straight to the window of clarity? My pick: yes, not sure: the place is yours. A moved section "
     "gets a Pangram check in the whole post (your extension, the free way) before it goes in. "
     "{O:now=S015,S016,S017,S018,S019,S020,S021|would=S015,S016,S017,S018,S020,S019@2,S021}"),
    ('6. Leaving someone in a crisis',
     "<b>{L:S068} ends with a paragraph about something else:</b> “If you've been there for someone, don't abandon them in a "
     "crisis unless it's unsafe for you to stay or they're creating the crisis to keep you...”, which is about how to leave "
     "someone who depends on you, not about memories that clash. Move it to the end of {L:S067}'s own text, which is about "
     "whether to leave, or to the start of {L:S069}? My pick: to the end of {L:S067}'s text; not sure. It gets a Pangram "
     "check where it lands."),
    ('7. Your phrases',
     "<b>The proposal takes some of your playful phrases out of the contents:</b> {L:S031}, {L:S032}, {L:S033}, {L:S013} "
     "with {L:S014}, {L:S045}, {L:S052}, {L:S057} and {L:S067}. Each is still a choice under its heading above. Should "
     "any open its section as a line of its own instead, such as “Slow & steady may win the race, but turtles have problems "
     "too!” as the first line of <i>What if the Sex Is Bad?</i>? A new line gets a Pangram check before it goes in. And "
     "whatever {L:S052} is called, your sentence at the end of {L:S041} (“If neither is relevant to you, skip ahead to Two "
     "Pillars Don't Hold The Roof Up.”) says the new name, with its link."),
]


def load(name):
    return json.load(open(os.path.join(HERE, name), encoding='utf-8'))


def esc(s):
    return html.escape(s, quote=False)


def same(a, b):
    f = lambda s: s.replace('’', "'").replace('“', '"').replace('”', '"')
    return f(a) == f(b)


def main(page_url=''):
    now = load('CONTENTS-NOW.json')
    ids = [e['id'] for e in now]
    NOW = {e['id']: e for e in now}
    FINAL = {e['id']: e for e in load('PROPOSAL-PICK3.json')}
    FABLE = {e['id']: e for e in load('PROPOSAL-FABLE.json')}
    cat = json.load(open(CATALOG, encoding='utf-8'))
    base, pid = cat['post']['base'], cat['post']['id']
    URL = {i: sl.url(base, pid, NOW[i]['heading']) for i in ids}
    heads = {k: ({i: NOW[i]['heading'] for i in ids} if f is None else {e['id']: e['heading'] for e in load(f)})
             for k, _, f, _, _ in RUNS}
    S = load('SCORES.json')['reads']
    key = load('EXPECTED-REVIEWED.json')['situations']
    sit = dict(re.findall(r'(?m)^\s*(\d+)\. (.*)$', open(os.path.join(HERE, 'SITUATIONS.md'), encoding='utf-8').read()))
    linemap, hard = {}, {}
    for k, _, _, reads, lines in RUNS:
        lm = {int(x['n']): x['id'] for x in load(lines)}
        for r in reads:
            linemap[r] = lm
            hard[r] = {}
            for n, w in re.findall(r'(?m)^HARD:\s*(\d+)\s*\|\s*(.*)$', open(os.path.join(HERE, 'reads', r), encoding='utf-8').read()):
                i = lm.get(int(n))
                if i:
                    hard[r].setdefault(i, []).append(w.strip())
    allreads = [r for _, _, _, rs, _ in RUNS for r in rs]
    finalreads = RUNS[-1][3]
    pickreads = [r for k, _, _, rs, _ in RUNS if k in PICKS for r in rs]
    yourreads = [r for k, _, _, rs, _ in RUNS if k in YOURS for r in rs]
    lowmap = {NOW[i]['heading'].lower(): i for i in ids}

    def link(i, text=None):
        return '<a href="%s">%s</a>' % (URL[i], esc(text or NOW[i]['heading']))

    def autolink(h):
        """Link every quoted phrase that is one of his live headings (quotes as plain or curly)."""
        def sub(m):
            q = m.group(2)
            i = lowmap.get(html.unescape(q).lower())
            return '%s%s%s' % (m.group(1), link(i, html.unescape(q)) if i else q, m.group(3))
        return re.sub(r'(["“])([^"“”<>]{2,90})(["”])', sub, h)

    def label(i, text):
        if same(text, FINAL[i]['heading']):
            return 'this heading'
        if same(text, NOW[i]['heading']):
            return 'yours'
        if same(text, FABLE[i]['heading']):
            return "Fable's"
        return '“%s”' % text

    ev = {}
    for k, _, _, reads, _ in RUNS:
        for r in reads:
            for n, p in S[r]['per'].items():
                for i in key[n]['right']:
                    g = ev.setdefault(i, {}).setdefault(n, {})
                    lab = label(i, heads[k][i])
                    g.setdefault(lab, [0, 0])
                    g[lab][1] += 1
                    g[lab][0] += p['kind'] == 'right'

    def evidence(i):
        out = []
        for n, g in sorted(ev.get(i, {}).items(), key=lambda x: int(x[0])):
            if len(g) < 2:
                continue
            order = sorted(g, key=lambda l: (l == 'this heading', l != 'yours'))
            parts = ['%d of %d with %s' % (g[l][0], g[l][1], l) for l in order]
            out.append(('Readers looking for it (“%s”) went here first: ' % sit[n]) + '; '.join(parts) + '.')
        return out

    def flags(i, reads):
        return [w for r in reads for w in hard[r].get(i, [])]

    def flagline(i):
        f = flags(i, finalreads)
        if not f:
            return ''
        return ('%d of %d readers of the final proposal called it hard (%d of %d readers of yours). One said: %s'
                % (len({r for r in finalreads if i in hard[r]}), len(finalreads),
                   len({r for r in yourreads if i in hard[r]}), len(yourreads), f[0][:160] + ('…' if len(f[0]) > 160 else '')))

    def qflag(idlist):
        n = len({r for r in allreads for i in idlist if i in hard[r]})
        return '%d of the %d readers marked %s hard' % (n, len(allreads), 'it' if len(idlist) == 1 else 'one of them or more')

    def qright(ns):
        a = sum(S[r]['per'][n]['kind'] == 'right' for r in pickreads for n in ns)
        return '%d of %d tries' % (a, len(pickreads) * len(ns))

    def outline(spec):
        cols = []
        for part in spec.split('|'):
            name, items = part.split('=', 1)
            lines = []
            for it in items.split(','):
                m = re.match(r'(\w+)(?:@(\d))?(?::(.*))?$', it.strip())
                i, lvl, text = m.group(1), m.group(2), m.group(3)
                if name == 'now':
                    e = NOW[i]
                    lines.append('%s%s %s' % ('&nbsp;' * 4 * (e['level'] - 1), '#' * e['level'], link(i)))
                else:
                    level = int(lvl) if lvl else (NOW[i]['level'] if i in NOW else 1)
                    words = text if text else (FINAL[i]['heading'] if i in FINAL else i)
                    lines.append('%s%s %s' % ('&nbsp;' * 4 * (level - 1), '#' * level, esc(words)))
            cols.append('<div style="flex:1;min-width:230px"><div style="font:600 12px/1.4 Inter,system-ui,sans-serif;color:var(--faint);margin-bottom:3px">%s</div>%s</div>'
                        % ('Now, on the post' if name == 'now' else 'Would be', '<br>'.join(lines)))
        return ('<div style="display:flex;gap:18px;flex-wrap:wrap;font:13px/1.55 Inter,system-ui,sans-serif;background:rgba(127,127,127,.06);'
                'border:1px solid var(--line);border-radius:8px;padding:9px 11px;margin:9px 0">%s</div>' % ''.join(cols))

    def fill(text):
        text = re.sub(r'\{L:(S\d{3})\}', lambda m: link(m.group(1)), text)
        text = re.sub(r'\{F:([S\d,]+)\}', lambda m: qflag(m.group(1).split(',')), text)
        text = re.sub(r'\{R:([\d,]+)\}', lambda m: qright(m.group(1).split(',')), text)
        return re.sub(r'\{O:([^}]+)\}', lambda m: outline(m.group(1)), text)

    # ---- scores
    rows = []
    for k, lab, _, reads, _ in RUNS:
        t = [S[r]['tally'] for r in reads]
        rows.append((lab, len(reads), *[' · '.join(str(x[c]) for x in t) for c in ('right', 'near', 'wrong', 'guess', 'found')]))
    changed_sits = []
    for n in sorted(key, key=int):
        a = sum(S[r]['per'][n]['kind'] == 'right' for r in yourreads)
        b = sum(S[r]['per'][n]['kind'] == 'right' for r in finalreads)
        if a / len(yourreads) != b / len(finalreads):
            changed_sits.append((n, a, b))
    ncut_now = sum(not ts.shown(NOW[i]['heading'], NOW[i]['level'])[0] for i in ids)
    ntight_now = sum(ts.status(NOW[i]['heading'], NOW[i]['level']) == 'tight' for i in ids)
    nwords = sum(FINAL[i]['heading'].lower() != NOW[i]['heading'].lower() for i in ids)
    ncase = sum(FINAL[i]['heading'] != NOW[i]['heading'] and FINAL[i]['heading'].lower() == NOW[i]['heading'].lower() for i in ids)
    nsit = len(key)
    head_cols = ('Contents', 'Readers', 'Right on first try (of %d)' % nsit, 'Near (its parent)', 'Wrong', 'Guessed', 'Found in two tries')
    table_html = ('<div class="scroll"><table class="sc"><thead><tr>' + ''.join('<th>%s</th>' % c for c in head_cols) + '</tr></thead><tbody>'
                  + ''.join('<tr><td>%s</td>' % esc(r[0]) + ''.join('<td class="n">%s</td>' % c for c in r[1:]) + '</tr>' for r in rows)
                  + '</tbody></table></div>'
                  + '<p class="legend">%d situations, each a reader looking for one thing (written from your text with the headings taken out, '
                    'and checked by a second reader). Each fresh reader saw only one contents list, drawn as the sidebar draws it, and named '
                    'the heading they would click first. One number per reader. The proposals were read with question 1’s recommended '
                    'answer: the card-game link as a heading of its own above <i>Who This Guide Is For</i>.</p>' % nsit
                  + '<p class="legend"><b>Where it changed</b> (readers of yours → readers of the final proposal who went to the right section first):</p><ul class="legend">'
                  + ''.join('<li>“%s”: %d of %d → %d of %d</li>' % (esc(sit[n]), a, len(yourreads), b, len(finalreads)) for n, a, b in changed_sits)
                  + '</ul>')
    question_html = ('<b>Which heading should each section of your romance guide have in the contents sidebar?</b> '
                     '%d of your %d headings are cut off there today, and %d more only just fit (your browser likely cuts their last letters). '
                     'The proposal renames %d, puts %d more in title case (your heading rule) and cuts off none. '
                     'It is picked for every heading to start with: keep it, take yours or Fable’s, or write your own. Then the %d questions at the bottom. '
                     'Nothing on the post has changed for this yet. <a href="%s">The post</a>.') % (ncut_now, len(ids), ntight_now, nwords, ncase, len(QUESTIONS), POST)
    git_html = ('This page is a view of <a href="%sRESULTS.md">the run’s record in Git</a>, which has the same lists and numbers. '
                'Your answers save to this page and in this browser; “Copy my answers” gives the same record to paste into the chat.') % GIT

    notes, pick = {}, {}
    for i in ids:
        parts = ['<a href="%s">On the post</a>' % URL[i]]
        if FINAL[i].get('why'):
            parts[0] += ' · ' + autolink(esc(FINAL[i]['why']))
        parts += [autolink(esc(x)) for x in evidence(i)]
        fl = flagline(i)
        if fl:
            parts.append(autolink(esc(fl)))
        notes[i] = '<br>'.join(parts)
        pick[i] = 'now' if FINAL[i]['heading'] == NOW[i]['heading'] else 'pick'
    questions = [{'id': qid, 'text': fill(text)} for qid, text in QUESTIONS]
    opts = {'title': 'Romance guide: your contents picks',
            'sub': 'For “Romance Advice I Wish My Parents Taught Me”, 2026-11-28. Your picks save as you go.',
            'store': 'romance-toc-20261128', 'primary': 'pick',
            'options': {'pick': {'label': 'Proposed', 'file': 'PROPOSAL-PICK3.json'},
                        'fable': {'label': "Fable's version", 'file': 'PROPOSAL-FABLE.json'}},
            'pick': pick, 'notes': notes, 'kinds': KINDS, 'questions': questions,
            'scores': {'question': question_html, 'table': table_html, 'git': git_html}}
    json.dump(opts, open(os.path.join(HERE, 'PAGE-OPTIONS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # ---- link changes the final proposal makes (a dry run of section_links.py rename on a copy of the catalog)
    c = copy.deepcopy(cat)
    changes = []
    for i in ids:
        if FINAL[i]['heading'] != NOW[i]['heading']:
            for ln, old, new in sl.rename(c, NOW[i]['heading'], FINAL[i]['heading']):
                changes.append((i, ln, old, new))
    json.dump([{'section': i, 'words': ln['text'], 'in': ln['in'], 'old': o, 'new': n} for i, ln, o, n in changes],
              open(os.path.join(HERE, 'PICK-LINK-CHANGES.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    assert not sl.links_check(c), sl.links_check(c)

    # ---- RESULTS.md
    def st(t, lvl):
        return {'fits': 'fits', 'tight': 'only just fits', 'cut': 'cut off'}[ts.status(t, lvl)]

    def mdl(i, text=None):
        return '[%s](%s)' % ((text or NOW[i]['heading']).replace('|', '\\|').replace('[', '\\[').replace(']', '\\]'), URL[i])

    def mdtext(h):
        h = re.sub(r'<a href="([^"]+)">([^<]+)</a>', lambda m: '[%s](%s)' % (m.group(2), m.group(1)), h)
        h = re.sub(r'</?b>', '**', h)
        h = re.sub(r'</?i>', '*', h)
        return html.unescape(re.sub(r'<[^>]+>', ' ', h))

    def mdoutline(spec):
        out = []
        for part in spec.split('|'):
            name, items = part.split('=', 1)
            lines = []
            for it in items.split(','):
                m = re.match(r'(\w+)(?:@(\d))?(?::(.*))?$', it.strip())
                i, lvl, text = m.group(1), m.group(2), m.group(3)
                if name == 'now':
                    lines.append('%s%s %s' % ('    ' * (NOW[i]['level'] - 1), '#' * NOW[i]['level'], NOW[i]['heading']))
                else:
                    level = int(lvl) if lvl else (NOW[i]['level'] if i in NOW else 1)
                    lines.append('%s%s %s' % ('    ' * (level - 1), '#' * level, text or (FINAL[i]['heading'] if i in FINAL else i)))
            out.append(('Now, on the post:' if name == 'now' else 'Would be:') + '\n\n```\n' + '\n'.join(lines) + '\n```')
        return '\n\n' + '\n\n'.join(out) + '\n\n'

    md = ['# Romance guide: contents test, 2026-11-28', '',
          'For [Romance Advice I Wish My Parents Taught Me](%s). Run the way the Inner Child, bad trips and Nirvāna contents were done '
          '([how](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/FIXING-AN-ARTICLE.md), section 3). '
          'Nothing on the post has changed for this yet; the section links went in earlier the same morning (below).' % POST, '']
    if page_url:
        md += ['**Your picks page:** [%s](%s). Pick a heading for each section and answer the %d questions; your answers save there.'
               % (page_url, page_url, len(QUESTIONS)), '']
    md += ['## What fresh readers found', '',
           '%d of your %d headings are cut off in the sidebar today, and %d more only just fit. The final proposal renames %d, '
           'puts %d more in title case, and cuts off none.' % (ncut_now, len(ids), ntight_now, nwords, ncase), '',
           '| ' + ' | '.join(head_cols) + ' |', '|' + '---|' * len(head_cols)]
    md += ['| %s |' % ' | '.join(str(c) for c in r) for r in rows]
    md += ['', '%d situations, each a reader looking for one thing, written from the text with the headings taken out and checked by a '
           'second reader ([situations](%sSITUATIONS.md), [answer key](%sEXPECTED-REVIEWED.json)). Each fresh reader (Sonnet) saw only '
           'one contents list, drawn as the sidebar draws it, and named the heading they would click first; one number per reader. '
           'Scored by [score_reads.py](%sscore_reads.py). The proposals were read with question 1’s recommended answer (the card-game '
           'link as a heading of its own above "Who This Guide Is For").' % (nsit, GIT, GIT, GIT), '',
           '### Where it changed', '', '| Situation | Right first, with yours | With the final proposal |', '|---|---|---|']
    md += ['| %s | %d of %d | %d of %d |' % (sit[n], a, len(yourreads), b, len(finalreads)) for n, a, b in changed_sits]
    md += ['', '## The proposal, heading by heading', '', 'Each heading of yours links to its section on the post.', '',
           '| # | Yours | Proposed | Why |', '|---|---|---|---|']
    for n, i in enumerate(ids, 1):
        e, f = NOW[i], FINAL[i]
        yours = '%s %s (%s)' % ('#' * e['level'], mdl(i), st(e['heading'], e['level']))
        if f['heading'] == e['heading']:
            prop = 'kept'
        else:
            prop = '%s (%s)' % (f['heading'].replace('|', '\\|'), st(f['heading'], e['level']))
            if not same(FABLE[i]['heading'], f['heading']) and not same(FABLE[i]['heading'], e['heading']):
                prop += "<br>Fable's: %s" % FABLE[i]['heading'].replace('|', '\\|')
        extra = evidence(i) + ([flagline(i)] if flagline(i) else [])
        why = '<br>'.join([x for x in [f.get('why', '')] + extra if x]).replace('|', '\\|')
        md.append('| %d %s | %s | %s | %s |' % (n, i, yours, prop, why))
    md += ['', '## Questions on the page', '']
    for qid, text in QUESTIONS:
        t = re.sub(r'\{O:([^}]+)\}', lambda m: mdoutline(m.group(1)), text)
        t = re.sub(r'\{L:(S\d{3})\}', lambda m: mdl(m.group(1)), t)
        t = re.sub(r'\{F:([S\d,]+)\}', lambda m: qflag(m.group(1).split(',')), t)
        t = re.sub(r'\{R:([\d,]+)\}', lambda m: qright(m.group(1).split(',')), t)
        md.append('**%s.** %s' % (qid, mdtext(t).strip()))
        md.append('')
    md += ['## Section links', '',
           'The ten links to sections went into the post on 2026-11-28 (09:58 UTC; [the plan](%sLINK-PLAN.json)), and the post\'s '
           'catalog is [SECTION-LINKS.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/romance/SECTION-LINKS.json): '
           'every heading with its anchor, every link, and the %d mentions left unlinked on purpose with why. The final proposal\'s '
           'renames change %d of those links (a dry run of `section_links.py rename` on a copy of the catalog; '
           '[the list](%sPICK-LINK-CHANGES.json)):' % (GIT, len(cat['unlinked_on_purpose']), len(changes), GIT), '',
           '| Link words | In | Now | Would be |', '|---|---|---|---|']
    md += ['| %s | %s | `%s` | `%s` |' % (ln['text'], ln['in'], o, nw) for i, ln, o, nw in changes]
    md += ['', 'One of them also changes its words: the last sentence of "Different levels in different domains can be complementary" '
           'names the section it links to by its old heading ("skip ahead to Two Pillars Don\'t Hold The Roof Up"), so it says the new '
           'name with the rename (question 7).', '',
           '## How it was done', '',
           '1. The live post read on 2026-11-28 ([its HTML](%sLIVE-BODY-20261128.html)); [the sections](%sARTICLE-SECTIONS.md) and the '
           'contents as the sidebar shows it ([yours](%sTOC-NOW-SIDEBAR.md), [whole](%sTOC-NOW-FULL.md)).' % (GIT, GIT, GIT, GIT),
           '2. An agent that saw no headings wrote %d situations from [the text with its headings taken out](%sTEXT-NO-HEADINGS.md); '
           'a second one checked the answer key against the text.' % (nsit, GIT),
           '3. Three fresh readers on yours (two sidebar, one whole headings).',
           '4. Fable renamed with the headings brief ([its list](%sPROPOSAL-FABLE.json), [its notes](%sPROPOSAL-FABLE-NOTES.md)); two readers.' % (GIT, GIT),
           '5. The first proposal ([its script](%smake_pick.py): yours where the sidebar shows it whole with room and readers found it, '
           'otherwise your words cut down, or the reader\'s question where readers missed it); two readers. Four headings both its readers '
           'marked hard changed in the second; two readers. One of those four went back (it pulled a reader to the wrong section); two '
           'readers of the final. [All the reads](%sreads/READ-PICK3-1.md) are in the reads folder.' % (GIT, GIT),
           '6. The repeat and hard-heading check passed with a fate for each of the 26 headings it lists ([fates](%sFATES-PICK3.json)).' % GIT,
           '', '## After your picks', '',
           'Your picks go into the post by script (`section_links.py rename` for each, so the links follow), with your answers to the '
           'questions, the sentence fixes a renamed heading needs, a Pangram check of any text that moves or changes, the post\'s '
           '"Updated" date and no email; then I check the sidebar on the live post.', '']
    open(os.path.join(HERE, 'RESULTS.md'), 'w', encoding='utf-8').write('\n'.join(md))
    print('RESULTS.md and PAGE-OPTIONS.json written: %d renamed, %d capitals only, %d cut now (+%d tight), %d situations changed, %d link changes'
          % (nwords, ncase, ncut_now, ntight_now, len(changed_sits), len(changes)))


if __name__ == '__main__':
    main(*sys.argv[1:])
