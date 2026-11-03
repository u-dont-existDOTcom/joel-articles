#!/usr/bin/env python3
"""Turn 116: which of the last guide's links go back into Joel's reorganized guide, and where (RELINK.json, RELINK.md).

His file lost 55 of the 67 links the guide had when I last gave it to him (experiments/t116-joel/LINKS.md): the words are
there with no link. A link goes back where its words are and the sentence around them is still the one the link was in
(difflib word ratio 0.5 or more between the base sentence and his, or his own typed link on those words); a link whose
words he only reused somewhere else ("Another") stays out, listed. His typed links ([text](url), which his file and
Substack show as typed) become real links with https:// in front, with the fixes the card names. Every URL here was
opened on his laptop on 2026-11-03 (experiments/t116-joel/URLS-CHECKED.txt).

  python3 relink.py"""
import difflib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BASE_SHA = '8c7068d4c572590c93145deee3bafee72d55f608'
base = subprocess.run(['git', 'show', BASE_SHA + ':articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'], cwd=ROOT,
                      capture_output=True, text=True, check=True).stdout
base = re.sub(r'<!--.*?-->', '', base, flags=re.S)
PAGE = (HERE / 'GUIDE-PAGE.md').read_text(encoding='utf-8')
BL = sr.blocks(PAGE)
LINK = re.compile(r'\[([^\[\]]+)\]\s?\(<?([^()\s<>]+(?:\([^()\s]*\))?[^()\s<>]*)>?\)')
SPLIT = re.compile(r'(?<=[.!?…])["”’)]*\s+(?=[A-Z“"(‘\'0-9«])')
# his typed URLs as they go in (Joel, 2026-11-03 21:25 UTC, for the shame guide: "you can change that link to ...")
FIX = {
    'shame.innerself.lovehttps://ibogaqueen.substack.com/p/dont-be-ashamed-of-shame-a-nuanced':
        'https://ibogaqueen.substack.com/p/dont-be-ashamed-of-shame-a-nuanced?utm_source=publication-search',
    '@KeyGoddess11': 'https://substack.com/@keygoddess11',
    'https://onlinelibrary.wiley.com/doi/10.1111/jftr.70049?af=R&utm_source=chatgpt.com': 'https://onlinelibrary.wiley.com/doi/10.1111/jftr.70049',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC12311821/?utm_source=chatgpt.com': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12311821/',
    'https://www.youtube.com/watch?v=FyZI-VaVg2g&list=RDFyZI-VaVg2g&start_radio=1': 'https://www.youtube.com/watch?v=FyZI-VaVg2g',
}


# links whose sentence he rewrote around the same words and job (the term named, the book named): they go back anyway
FORCE = {'scaffolding': 'he rewrote the sentence that names the technique; the link is the term\'s',
         'A. Helwa’s book': 'his sentence still names her book; the split at "A." hid it from the sentence match',
         '"The past didn\'t go anywhere."': 'his sister\'s quote, the same sentence; the full stop inside the quote hid it from the sentence match'}
# links that stay out though the words are there: he put his own link on them, or the words are in a heading now
SKIP = {'Serenity Prayer': 'he typed his own link on "The Serenity Prayer"',
        'iboga': 'he typed his own link on "female iboga"',
        'a relationship': 'the words were linked in a heading (If a Relationship Keeps Making You Feel Less Safe); a heading gets no link'}


def words(s):
    return re.findall(r"[a-z0-9']+", s.translate(str.maketrans({'’': "'", '‘': "'"})).lower())


def full(u):
    u = u.strip('<>')
    u = FIX.get(u, u)
    return u if re.match(r'https?://', u) else 'https://' + u


def base_sentences():
    out = []
    for para in re.split(r'\n\s*\n', base):
        flat = re.sub(r'\s+', ' ', para).strip()
        for m in LINK.finditer(flat):
            plain = LINK.sub(lambda x: x.group(1), flat)
            sents = SPLIT.split(plain)
            hit = next((s for s in sents if m.group(1) in s), plain)
            out.append({'text': m.group(1).replace('*', ''), 'url': m.group(2), 'sentence': hit})
    return out


def main():
    rows, seen = [], set()
    # 1. the base's links: back where the words and their sentence still are
    for b in base_sentences():
        t = b['text']
        cands = []
        nt = sr.norm_map(t)[0]
        for blk in BL:
            if blk['level']:
                continue
            ntext, idx = sr.norm_map(blk['text'])
            for mm in re.finditer(re.escape(nt), ntext):
                m = type('M', (), {'start': (lambda self, v=idx[mm.start()]: v), 'end': (lambda self, v=idx[mm.end() - 1] + 1: v)})()
                sents = SPLIT.split(blk['text'])
                pos, his = 0, blk['text']
                for s in sents:
                    k = blk['text'].find(s, pos)
                    if k <= m.start() < k + len(s):
                        his = s
                        break
                    pos = k + len(s)
                r = difflib.SequenceMatcher(None, words(b['sentence']), words(his), autojunk=False).ratio()
                linked = any(sg['href'] for sg in blk['segs'] if sg['t'] == t)
                cands.append((r, blk['i'], m.start(), m.end(), his, linked))
        if not cands:
            rows.append({'text': t, 'url': b['url'], 'action': 'gone', 'base_sentence': b['sentence']})
            continue
        cands.sort(key=lambda c: -c[0])
        r, i, s0, e0, his, linked = cands[0]
        key = (i, s0)
        if key in seen:
            continue
        seen.add(key)
        act = 'typed' if linked else ('restore' if r >= 0.5 or t in FORCE else 'reused')
        if t in SKIP and not linked:
            act = 'skip'
        t = blk_text = BL[i]['text'][s0:e0]
        rows.append({'text': t, 'url': b['url'], 'action': act, 'block': i, 'start': s0, 'end': e0, 'ratio': round(r, 2),
                     'base_sentence': b['sentence'], 'his_sentence': his, 'note': FORCE.get(b['text']) or SKIP.get(b['text'], '')})
    # 2. his typed links: each becomes a real link (with https://, and the card's fixes)
    typed = []
    for blk in BL:
        pos = 0
        for sg in blk['segs']:
            if sg['href'] and not sg['href'].startswith('Pictures/'):
                typed.append({'text': sg['t'], 'his_url': sg['href'], 'url': full(sg['href']), 'block': blk['i'],
                              'start': pos, 'end': pos + len(sg['t'])})
            pos += len(sg['t'])
    # the typed links the page tool can't read (a space between ] and (, or a link inside brackets)
    odd = [m.group(0) for m in re.finditer(r'\[[^\]]*\]\s+\(<?[^)\s]+>?\)|\[\[[^\]]+\]\([^)]+\)\]\s*\([^)]+\)', PAGE)]
    for r in rows:
        if r['action'] == 'restore':
            # his own typed URL where he chose one for the same words (spiritual bypassing, Buddhist enlightenment)
            mine = next((t for t in typed if t['text'].lower() == r['text'].lower()), None)
            r['url_in'] = mine['url'] if mine else full(r['url'])
            if r['text'] == 'spiritual bypassing':   # his typed "[spiritual bypassing] (bypassing.u-dont-exist.com)", which the page can't read as a link
                r['url_in'] = 'https://bypassing.u-dont-exist.com'
    out = {'base_commit': BASE_SHA, 'page': 'GUIDE-PAGE.md', 'base_links': rows, 'his_typed_links': typed, 'odd_typed_links': odd,
           'counts': {a: sum(r['action'] == a for r in rows) for a in ('restore', 'typed', 'reused', 'skip', 'gone')}}
    (HERE / 'RELINK.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    lines = ['# The links that go back into his reorganized guide (turn 116)', '',
             'From relink.py. Counts of the last guide\'s links: %s; his typed links: %d (and %d typed in a form the page '
             'tool can\'t read: %s).' % (json.dumps(out['counts']), len(typed), len(odd), '; '.join('`%s`' % o for o in odd)), '',
             '| Words | Goes back as | Why |', '|---|---|---|']
    for r in rows:
        why = {'restore': 'same sentence (%.2f)' % r.get('ratio', 0), 'typed': 'he typed his own link on these words',
               'reused': 'his sentence is a different one (%.2f): left out' % r.get('ratio', 0), 'gone': 'the words are cut',
               'skip': r.get('note', '')}[r['action']]
        if r['action'] == 'restore' and r.get('note'):
            why += '; ' + r['note']
        lines.append('| %s | %s | %s |' % (r['text'], r.get('url_in', '') if r['action'] == 'restore' else '', why))
    lines += ['', '## His typed links, as they go in', '']
    for t in typed:
        lines.append('- "%s" → %s%s' % (t['text'], t['url'], '' if t['url'] == t['his_url'] else ' (he typed `%s`)' % t['his_url']))
    (HERE / 'RELINK.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(out['counts']), 'typed', len(typed), 'odd', len(odd))
    for r in rows:
        if r['action'] in ('reused', 'gone', 'skip'):
            print(r['action'], r.get('ratio'), '|', r['text'], '|', r['base_sentence'][:90], '||', (r.get('his_sentence') or '')[:90])


if __name__ == '__main__':
    main()
