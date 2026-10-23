"""Nibbāna batch n1's fixes that go in (2026-10-23): the working copy HUMANIZED-SO-FAR.html, Joel's editor HTML of
2026-10-22 with the edits that read Human on their own through the API and passed the reader's check (REVIEW.md), and
EDITS-n1.json, the record of each (its check's link and try, its review).

The post itself is never touched: the working copy goes into a temporary draft for the whole-article recheck, and Joel
applies the fixes to his post when he wants them.

  python3 articles/nibbana/humanize/fix-20261023/n1/install_n1.py   (from the repo root)
"""
import importlib.util, json, pathlib

N = pathlib.Path(__file__).resolve().parent
H = N.parents[1]
spec = importlib.util.spec_from_file_location('make_n1', N / 'make_n1.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
PAGE = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/'
        'fix-20261023/n1/API-CHECKS.md')
# key: (the API check that read Human, its try in its lineage, the edits). n1-science's try 1 read Human, but the reader
# found two additions a reader would take as claims (REVIEW.md, item 4) and the reader's own fix read AI (n1_science_t2),
# so it went to Joel as question N1; his answer (2026-10-23 12:30 UTC, "n1 a.") put try 1's words in.
GO = {
    'n1-unification': ('n1_unification', 1, M.E['n1-unification'][2]),
    'n1-percentages': ('n1_percentages_t2', 2, M.T2['n1-percentages']),
    'n1-last-test': ('n1_last_test', 1, M.E['n1-last-test'][2]),
    'n1-rebirth': ('n1_rebirth', 1, M.E['n1-rebirth'][2]),
    'n1-science': ('n1_science', 1, M.E['n1-science'][2]),
}
# Joel's own words (question N2: A), from his message of 2026-10-23 12:30 UTC (../joel-20261023-1230-message.txt, word for
# word): he took each stretch's third try, rewrote it, and checked it himself ("dark green"). Each replaces its whole
# paragraph(s) of the source, his text as he typed it with the paragraph's links put back on the same words, and the
# obvious typos fixed (listed in TYPOS). The driving caution's last line, "That's my own CYA showing. 😇", stays after his
# second paragraph, as it stayed after the third try he rewrote.
MSG = N.parent / 'joel-20261023-1230-message.txt'
JOEL = {  # key: (the tag in his message, the source paragraphs' first words, the links as (words, the source's <a> tag))
    'n1-nde': ('n1_nde_t3:', ['The closest comparison that’s worth mentioning is the out-of-body perception'], None),
    'n1-burden': ('n1_burden_t3:', ['The Buddha splits the accounting cleanly in'], None),
    'n1-diamond': ('n1_diamond_t3:', ['I used to attribute “life is like a dream” directly to the historical Buddha.'], None),
    'n1-driving': ('n1_driving_t3:', ['My buddy E. told me he had much stronger episodes while driving:',
                                      'Whatever the explanation, to be safe, I wouldn’t keep driving through that.'], None),
}
TYPOS = {'n1-burden': [('burden(even', 'burden (even'), ('dart)  of', 'dart) of'), ('counterinuitive', 'counterintuitive')]}
KEEP_AFTER = {'n1-driving': ' That’s my own CYA showing. 😇'}
# a link whose words he changed goes on his words: the source's words -> his
LINK_WORDS = {'n1-burden': {'quarks supply less than 1% of a proton’s mass; roughly 99% comes from gluon-binding energy':
                            'quarks supply less than 1% of a proton’s mass, roughly 99% comes from gluon-binding energy'}}


def his_text(tag):
    msg = MSG.read_text(encoding='utf-8')
    tags = [t for _k, (t, _p, _l) in JOEL.items()]
    i = msg.index(tag)
    ends = [msg.index(t, i + 1) for t in tags if t != tag and msg.find(t, i + 1) > 0] + [msg.index('\n----', i)]
    block = msg[i:min(ends)]
    a = block.index('"') + 1
    b = block.rindex('"')
    return [x.strip() for x in block[a:b].split('\n\n') if x.strip()]


def links_of(para_html):
    import re
    return [(re.sub(r'<[^>]+>', '', m.group(2)), m.group(0)) for m in re.finditer(r'(<a [^>]*>)(.*?)</a>', para_html)]


def joel_edits(work):
    import html, re
    out = []
    for key, (tag, firsts, _l) in JOEL.items():
        paras = his_text(tag)
        assert len(paras) == len(firsts), (key, len(paras))
        for k, (first, new) in enumerate(zip(firsts, paras)):
            for a, b in TYPOS.get(key, []):
                if a in new:
                    new = new.replace(a, b)
            i = work.index('<p>' + first)
            j = work.index('</p>', i)
            old_inner = work[i + 3:j]
            body = html.escape(new, quote=False)
            for words, a_tag in links_of(old_inner):
                his = LINK_WORDS.get(key, {}).get(words, words)
                plain = html.escape(his, quote=False)
                assert body.count(plain) == 1, (key, his)
                open_tag = re.match(r'<a [^>]*>', a_tag).group(0)
                inner = re.sub(r'^<a [^>]*>(.*)</a>$', r'\1', a_tag)  # the link's inner HTML (an <em> stays)
                inner = inner.replace(html.escape(words, quote=False), plain) if his != words else inner
                body = body.replace(plain, open_tag + inner + '</a>')
            if k == len(firsts) - 1 and key in KEEP_AFTER:
                assert old_inner.endswith(KEEP_AFTER[key]), key
                body += KEEP_AFTER[key]
            out.append((key, old_inner, body))
            work = work[:i + 3] + body + work[j:]
    return work, out


def main():
    results = {}
    for f in sorted(N.glob('API-RESULTS-*.jsonl')):
        for l in f.read_text(encoding='utf-8').splitlines():
            if l.strip():
                r = json.loads(l)
                results[r['name']] = r
    src = M.SRC.read_text(encoding='utf-8')
    work, rec = src, []
    for key, (check, tr, pairs) in GO.items():
        r = results[check]
        assert r['headline'] == 'Human Written', (key, r['headline'])
        for old, new in pairs:
            assert work.count(old) == 1, key
            work = work.replace(old, new)
            rec.append({'key': key, 'windows': M.E[key][0], 'shape': M.E[key][1], 'old': old, 'new': new,
                        'check': PAGE + '#' + check, 'try': tr,
                        'result': '%s (Pangram %s, the API, %s; %d words on its own)' % (r['headline'], r['version'],
                                                                                          r['utc'], r['words']),
                        'review': 'fix-20261023/n1/REVIEW.md'})
    work, joel = joel_edits(work)
    for key, old, new in joel:
        rec.append({'key': key + '-joel-1230', 'windows': M.E[key][0], 'shape': 'his own words (question N2: A)', 'old': old, 'new': new,
                    'check': None, 'try': None,
                    'result': 'his own check ("dark green", his message of 2026-10-23 12:30 UTC); read in place in the next recheck',
                    'source': 'fix-20261023/joel-20261023-1230-message.txt', 'typos_fixed': [a for a, b in TYPOS.get(key, [])],
                    'review': None})
    (H / 'HUMANIZED-SO-FAR.html').write_text(work, encoding='utf-8')
    (N / 'EDITS-n1.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('HUMANIZED-SO-FAR.html: %d edits in, from %s' % (len(rec), M.SRC.name))


if __name__ == '__main__':
    main()
