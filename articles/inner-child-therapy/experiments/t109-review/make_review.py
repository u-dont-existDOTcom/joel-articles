#!/usr/bin/env python3
"""Turn 109's review page for Joel (tools/humanization/decision_page.py): every decision this turn leaves him, with
Approve / Revise / Reject / Pending and a note on each (UDA patterns/owner-questions-page.md).

- the sections in the new shape (his 104 A), each beside what it was, with their Pangram checks;
- his Pink paragraph's question (is she OK being named with her diagnosis);
- the point-of-view read (project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md, "Actual POV required", its omission test
  first): the cuts, the places my pick gives his reason, the places only he can fill, and the flags I left, with why
  (experiments/t109-pov/CHECKED.json, from my_check.py).

  python3 make_review.py      writes SPEC.json, REVIEW.html (a file to open) and REVIEW-artifact.html (for a Claude artifact)"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
EXP = HERE.parent
ART = EXP.parent
ROOT = ART.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402
import decision_page as D  # noqa: E402
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402

BEFORE = 'b71d5399'  # the lane's last commit before turn 109's changes: the article as it was
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/'
ST = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})

md_now = (ART / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
md_old = subprocess.run(['git', 'show', BEFORE + ':articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'], cwd=ROOT,
                        capture_output=True, text=True, check=True).stdout
text_now = C.reading_text(md_now, 'md')
LINES = text_now.split('\n')
CHECKS = {}
for f in sorted((EXP / 't109-api').glob('API-RESULTS-*.jsonl')):
    for l in f.read_text(encoding='utf-8').splitlines():
        r = json.loads(l)
        CHECKS[r['name']] = r


def section_paras(md, heading):
    """The plain paragraphs of the section under HEADING (to the next heading), without notes or link marks."""
    body = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    i = body.index('\n' + heading + '\n') + 1
    j = body.index('\n#', i + len(heading))
    return [plain(p.strip()) for p in body[i:j].split('\n\n')[1:] if p.strip()]


def check_line(name):
    r = CHECKS[name]
    f = r['fraction_ai'] or 0
    pct = '0%' if round(f, 4) == 0 else ('%.1f%%' % (100 * f) if f >= 0.01 else '%.2f%%' % (100 * f))
    return '%s, %s AI' % (r['headline'], pct), r['dashboard_link']


def para_of(quote):
    q = quote.translate(ST)
    hit = [l for l in LINES if q in l.translate(ST)]
    assert len(hit) == 1, quote
    return hit[0]


def marked(line, span, mark):
    """LINE as pieces with SPAN marked (found also when only the quote marks differ)."""
    t, s = line.translate(ST), span.translate(ST)
    i = t.index(s)
    return [[line[:i], ''], [line[i:i + len(span)], mark], [line[i + len(span):], '']]


WINDOWS = json.loads((EXP / 't109-windows' / 'WINDOWS.json').read_text(encoding='utf-8'))['items']


def round6(quote):
    """The saved round-6 windows below Human-High that share words with QUOTE."""
    q = re.sub(r'\s+', ' ', quote.translate(ST)).strip()
    out = []
    for w in WINDOWS:
        t = re.sub(r'\s+', ' ', w['text'].translate(ST)).strip()
        if len(t.split()) >= 4 and (t in q or q in t or any(s in t for s in re.split(r'(?<=[.!?])\s+', q) if len(s.split()) >= 5)):
            out.append('%s: %s, %s confidence, %d words (half %s)' % (w['id'], w['label'], w['confidence'], w['words'], w['half']))
    return out


def shape_items():
    items = []
    # Hear the Guard First: four tries
    old = section_paras(md_old, '### Hear the Guard First')
    now = section_paras(md_now, '### Hear the Guard First')
    tries = [('First try (the worked example you approved)', 't109_guard_p1', 't109_guard_p3'),
             ('Second try (installed now, my pick)', 't109_guard_p1b', 't109_guard_p3b'),
             ('Third try', 't109_guard_p1c', 't109_guard_p3c'),
             ('Fourth try (the harder-voice case back in P1)', 't109_guard_p1d', None)]
    rows = []
    for label, a, b in tries:
        x = check_line(a)
        s = '%s: P1 %s' % (label, x[0])
        if b:
            s += '; the performance paragraph %s' % check_line(b)[0]
        rows.append(s)
    items.append({
        'id': 'S1', 'group': 'shape', 'title': 'Hear the Guard First: which arrangement to keep',
        'section': 'When the Adult Voice Feels Fake › Start With Whatever Showed Up › Hear the Guard First',
        'whose': 'yours and mine, every sentence word for word; only the order and the breaks change',
        'blocks': [{'label': 'Before this turn', 'paras': [[[p, '']] for p in old]},
                   {'label': 'Now (the second try)', 'paras': [[[p, '']] for p in now]}],
        'fields': [
            {'label': 'What happened', 'text': 'In the shape you approved, the performance paragraph read 99.8% AI alone. Four arrangements of the same sentences showed why: one line of yours, "It puts you into the role of the Nurturer, which alleviates the instinct to argue back.", carried whichever paragraph held it to Human, and the other one read AI. The plain path stripped to instructions read AI each time it had no line like that.'},
            {'label': 'The four tries', 'list': rows},
            {'label': 'My pick', 'text': 'Keep the second try, installed now: your reply line and its reason stay together, the way you wrote them, and the plain path is short before them. Its first paragraph read 28% AI alone, with only Low-confidence Human windows, so the section check decides; it comes once your decision on "I\'d still keep it the same." (the point-of-view card for this section) is in. If that paragraph still reads AI in its section, fresh readers name its tells before I ask you for anything.'}],
        'links': [{'text': 'the checks, with their windows', 'url': B + 'experiments/t109-api/API-CHECKS.md'}] +
                 [{'text': '%s, %s' % (lab.split(' (')[0].lower(), w), 'url': check_line(n)[1]} for lab, a, b in tries for n, w in ((a, 'P1'), (b, 'P3')) if n],
        'approve': 'keep the second try.',
        'reject': 'put the section back the way it was before this turn (it read Human).'})
    # Start With Whatever Showed Up: the second try
    old = section_paras(md_old, '## Start With Whatever Showed Up')
    now = section_paras(md_now, '## Start With Whatever Showed Up')
    items.append({
        'id': 'S2', 'group': 'shape', 'title': 'Start With Whatever Showed Up: the path first',
        'section': 'When the Adult Voice Feels Fake › Start With Whatever Showed Up',
        'whose': 'yours and mine, every sentence word for word; only the order and the breaks change',
        'blocks': [{'label': 'Before this turn', 'paras': [[[p, '']] for p in old]},
                   {'label': 'Now', 'paras': [[[p, '']] for p in now]}],
        'fields': [
            {'label': 'What changed', 'text': 'Your P1 as it was, then your line to say and its wait, your "If nothing comes" and your "Or if you do get an answer" side by side; the paragraphs on fears and stray thoughts, on naming parts, on anxiety and on a part\'s no come after, each as it was.'},
            {'label': 'The checks', 'text': 'The first try joined your P1\'s first sentences to your line to say, and that paragraph read %s alone: a run of instructions with your "Maybe it just has something to say" taken out of it. In this second try your P1 is whole again, and your "If nothing comes" paragraph read %s alone. The section check waits for the point-of-view item on its last paragraph.' % (check_line('t109_start_p1')[0], check_line('t109_start_p4')[0])},
            {'label': 'Nothing of yours here', 'text': 'The fears and stray thoughts paragraph, the anxiety paragraph and the last one (a part\'s no) are mine; a moment of yours in any of them would be the first thing of yours there.'}],
        'links': [{'text': 'first try, P1', 'url': check_line('t109_start_p1')[1]}, {'text': '"If nothing comes"', 'url': check_line('t109_start_p4')[1]}],
        'approve': 'keep the new shape.', 'reject': 'put it back the way it was.'})
    old = section_paras(md_old, '#### Before You Tell the Hardest Stuff')
    now = section_paras(md_now, '#### Before You Tell the Hardest Stuff')
    items.append({
        'id': 'S3', 'group': 'shape', 'title': 'Before You Tell the Hardest Stuff: what to do first',
        'section': 'Borrowed Adulthood in Relationship › First Social Connections, Done Right › Opening up honestly to the right people at the right pace › Before You Tell the Hardest Stuff',
        'whose': 'yours, every sentence word for word (your upload of 2026-10-19); only the order and the breaks change',
        'blocks': [{'label': 'Before this turn', 'paras': [[[p, '']] for p in old]},
                   {'label': 'Now', 'paras': [[[p, '']] for p in now]}],
        'fields': [
            {'label': 'What changed', 'text': 'What to do first comes first: your "I\'d assume" and your danger lines. Then the reasons, one a paragraph: what a phone or a server keeps, who has to report, your question to ask and why you wouldn\'t bother, and your dream narrative.'},
            {'label': 'The checks', 'text': 'The first paragraph read %s alone, the reporting paragraph %s, and the whole section %s.' % (check_line('t109_hardest_p1')[0], check_line('t109_hardest_p3')[0], check_line('t109_sec_hardest')[0])}],
        'links': [{'text': 'P1 alone', 'url': check_line('t109_hardest_p1')[1]}, {'text': 'P3 alone', 'url': check_line('t109_hardest_p3')[1]},
                  {'text': 'the section', 'url': check_line('t109_sec_hardest')[1]}],
        'approve': 'keep the new shape.', 'reject': 'put it back the way it was.'})
    items.append({
        'id': 'S4', 'group': 'shape', 'title': 'The densest sections I left as they are',
        'section': 'from the density page, densest first',
        'fields': [{'label': 'Why each one stays', 'list': [
            'If You Want to Kill Yourself: it already starts with the steps, and its second paragraph is yours.',
            'When to Change the Strategy, and Not Every Hero Wears A Cape: your own rewrites of this week, already one situation a paragraph.',
            'What to Make of a Passing Feeling: your text, one case a paragraph (someone else\'s boundary, feelings about yourself, the other extreme).',
            'Notice the Part That Came Here: it builds to its one instruction, and its first line answers the love section before it.',
            'The Belief Behind the Guards: "With any of these patterns" needs the patterns before it, so the plain path can\'t come first without new words.']},
            {'label': 'Next', 'text': 'The next batch, densest first: How to Forgive Without Forgetting, The Parent You Inherited (your rewrite, so only with your OK), How Much Happiness Do You Know Is Possible?, Borrow One Competency at a Time and Differentiation.'}],
        'links': [{'text': 'the density page', 'url': B + 'experiments/t108-shape/DENSITY.md'}],
        'approve': 'leave them as they are.', 'reject': 'reshape them too (say which in the note).'})
    return items


def yours_items():
    p = para_of('as my friend Pink, who has been healing her Dissociative Identity Disorder')
    return [{
        'id': 'Y1', 'group': 'yours', 'title': 'Your friend Pink, named with her diagnosis',
        'section': 'Appendix › How This Relates to IFS, its last paragraph',
        'whose': 'yours (2026-10-25), word for word but for "explained" (your "expalined")',
        'blocks': [{'label': 'Your paragraph, as it is now', 'paras': [marked(p, 'my friend Pink, who has been healing her Dissociative Identity Disorder', 'mark')]}],
        'fields': [
            {'label': 'The checks', 'text': 'It read %s alone and the section %s.' % (check_line('t109_ifs_p8')[0], check_line('t109_sec_ifs')[0])},
            {'label': 'Question for you', 'text': 'Is she OK being named with her diagnosis in a public post? If you haven\'t asked her, the paragraph works the same with "a friend who has been healing her Dissociative Identity Disorder".'},
            {'label': 'My pick', 'text': 'Keep it as you wrote it if she\'s OK with it; you know her and I don\'t.'}],
        'links': [{'text': 'the paragraph alone', 'url': check_line('t109_ifs_p8')[1]}, {'text': 'the section', 'url': check_line('t109_sec_ifs')[1]}],
        'approve': 'keep "my friend Pink" as you wrote it.',
        'reject': 'make it "a friend who has been healing her Dissociative Identity Disorder", her name out.'}]


def pov_items():
    checked = json.loads((EXP / 't109-pov' / 'CHECKED.json').read_text(encoding='utf-8'))
    out, left = [], []
    n = {'cut': 0, 'pov': 0, 'ask': 0}
    for y in sorted(checked, key=lambda y: (y.get('line') or 0)):
        g = y['group']
        line = para_of(y['quote'])
        sec = y.get('heading') or y.get('section')
        if g == 'left':
            left.append('%s ("%s"): %s' % (sec, y['quote'][:90] + ('...' if len(y['quote']) > 90 else ''), y['note']))
            continue
        n[g] += 1
        iid = {'cut': 'C', 'pov': 'P', 'ask': 'Q'}[g] + str(n[g])
        fields = [{'label': 'What the text around it already says' if g == 'cut' else 'What\'s missing', 'text': y['missing']}]
        if g == 'pov' and y.get('povs'):
            fields.append({'label': 'Points of view it could have (the reader\'s)', 'list': y['povs']})
        if y.get('note'):
            fields.append({'label': 'My check', 'text': y['note']})
        if y.get('question'):
            fields.append({'label': 'Question for you', 'text': y['question']})
        fields.append({'label': 'My pick', 'text': y['my_pick']})
        r6 = round6(y['quote'])
        if r6:
            fields.append({'label': 'Round 6 read it below Human-High', 'list': r6})
        if g == 'cut':
            struck, after = C.cut_paragraph(text_now, y['quote'])
            blocks = [{'label': 'Now', 'paras': [marked(line, y['quote'], 'del')]},
                      {'label': 'After the cut', 'paras': [[[after, '']]] if after else [[['(the whole paragraph goes)', '']]]}]
            title = 'Cut "%s"' % (y['quote'] if len(y['quote']) < 70 else y['quote'][:67].rstrip() + '...')
            approve, reject = 'make the cut.', 'keep the line.'
        elif g == 'pov':
            old, new = y['edit']
            t = line.translate(ST)
            i = t.index(old.translate(ST))
            old_real = line[i:i + len(old)]  # the paragraph's own characters (its quote marks)
            # the words my pick changes, word by word: cut words struck through, new words marked
            import difflib
            ow, nw = re.findall(r'\S+\s*', old_real), re.findall(r'\S+\s*', new)
            pieces = [[line[:i], '']]
            for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, ow, nw, autojunk=False).get_opcodes():
                if op == 'equal':
                    pieces.append([''.join(nw[b1:b2]), ''])
                else:
                    if a2 > a1:
                        pieces.append([''.join(ow[a1:a2]), 'del'])
                    if b2 > b1:
                        pieces.append([''.join(nw[b1:b2]), 'ins'])
            pieces.append([line[i + len(old):], ''])
            blocks = [{'label': 'Now', 'paras': [marked(line, y['quote'], 'mark')]},
                      {'label': 'With my pick', 'paras': [[p for p in pieces if p[0]]]}]
            title = y['my_pick'].rstrip('.') + ': "%s"' % (y['quote'] if len(y['quote']) < 60 else y['quote'][:57].rstrip() + '...')
            approve, reject = 'make my change.', 'leave it as it is.'
        else:
            blocks = [{'label': 'Now', 'paras': [marked(line, y['quote'], 'mark')]}]
            title = 'Your words for "%s"' % (y['quote'] if len(y['quote']) < 60 else y['quote'][:57].rstrip() + '...')
            approve, reject = 'your words in the note go in.', 'it stays as it is.'
        out.append({'id': iid, 'group': g, 'title': title, 'section': sec, 'whose': y['whose'], 'blocks': blocks,
                    'fields': fields, 'approve': approve, 'reject': reject, 'reader_key': y['key']})
    out.append({'id': 'L1', 'group': 'left', 'title': 'The %d flags I left as they are, with why' % len(left),
                'fields': [{'label': 'Each one, in the article\'s order', 'list': left}],
                'links': [{'text': 'all 61 flags with the readers\' notes', 'url': B + 'experiments/t109-pov/POV-READ.md'}],
                'approve': 'leave them all as they are.', 'reject': 'take up the ones your note names.'})
    return out, len(left)


def main():
    shape, yours = shape_items(), yours_items()
    pov, nleft = pov_items()
    items = shape + yours + pov
    counts = {g: sum(1 for x in items if x['group'] == g) for g in ('shape', 'yours', 'cut', 'pov', 'ask', 'left')}
    import hashlib
    spec = {
        'review_id': 'inner-child-t109-20261025', 'title': 'Inner Child Review Sheet', 'eyebrow': 'Inner Child Therapy · turn 109',
        'source_name': 'the humanized article as of turn 109', 'source_sha256': hashlib.sha256(md_now.encode('utf-8')).hexdigest(),
        'repo_file': B + 'experiments/t109-review/REVIEW.html',
        'intro': [
            'Everything this turn leaves for you to decide, one card each. Approve, Revise, Reject or Pending on each, and a note if you want; nothing changes in the article until you decide. When you\'re done, press Copy JSON and paste it into the chat, from either account.',
            'The point-of-view read: eight fresh readers each read an eighth of the guide under the new rule, the omission test first, and flagged 61 places. I checked each against the whole article and your own words: %d are cuts, %d have a fix from your own words, %d need words only you have, and %d I left, with why, on the last card.' % (counts['cut'], counts['pov'], counts['ask'], nleft),
            'Round 6\'s stretches below Human with high confidence are saved on [their own page](%s); a card here says when its line was one of them.' % (B + 'experiments/t109-windows/WINDOWS.md')],
        'groups': [
            {'id': 'shape', 'title': 'Sections in the new shape (104 A)', 'intro': 'The plain path first, then one situation a paragraph, with every sentence word for word. Each one is beside what it was.'},
            {'id': 'yours', 'title': 'Your own new text'},
            {'id': 'cut', 'title': 'Lines that only say again what\'s already there', 'intro': 'Take the line out, and nothing the reader needs goes with it.'},
            {'id': 'pov', 'title': 'Places my pick gives your reason', 'intro': 'Advice anyone could have written; my pick gives it your reason, from your own words in the article or in your answers.'},
            {'id': 'ask', 'title': 'Places only you can fill', 'intro': 'The reason is something only you know. Approve with your words in the note puts them in.'},
            {'id': 'left', 'title': 'Flagged, and left as they are'}],
        'items': items}
    (HERE / 'SPEC.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'REVIEW.html').write_text(D.build(spec), encoding='utf-8')
    (HERE / 'REVIEW-artifact.html').write_text(D.build(spec, full=False), encoding='utf-8')
    print(counts, len(items), 'items')


if __name__ == '__main__':
    main()
