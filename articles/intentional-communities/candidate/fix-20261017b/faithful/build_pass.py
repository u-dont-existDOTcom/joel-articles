"""The whole-article faithfulness pass of 2026-10-17 (Joel, 17:16 UTC, his 45: "we should do a final pass to make sure it's
faithful to the original ... i feel like we've been doing section by section which could potentially lose the forest for the
trees"). Builds the inputs for five fresh readers: four read sections side by side (1-4, 5-8, 9-12, 13-17) for lost,
shifted and added points; one reads both whole articles for the spine, callbacks, contradictions, repeats, voice and length.
Joel's own sentences are marked with tools/humanization/meaning_sweep.py's author marks (the ledger and every joel-2026*
text, as sweep-20261016/ did). Also writes LINKS.md, the mechanical link comparison.
Run from candidate/: python3 fix-20261017b/faithful/build_pass.py"""
import glob, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
A = C.parent
REPO = A.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import meaning_sweep as ms  # noqa: E402

ART, PUB = C / 'HUMANIZED-SO-FAR.md', A / 'original.md'
owner_files = sorted(glob.glob(str(C / 'joel-2026*' / '*.txt'))) + sorted(glob.glob(str(C / 'joel-20261013' / '*.md')))
owners = ms.owner_strings(str(C / 'OWNER-EDITS.json'), owner_files)
pub = ms.h1_sections(PUB.read_text(encoding='utf-8'))
art = ms.h1_sections(ART.read_text(encoding='utf-8'))
assert len(pub) == len(art) == 17

GROUPS = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12], 'D': [13, 14, 15, 16, 17]}
for g, secs in GROUPS.items():
    text = ms.build(str(ART), str(PUB), secs, str(C / 'OWNER-EDITS.json'), owner_files)
    (HERE / ('PAIRS-%s.md' % g)).write_text(text, encoding='utf-8')

full_rw, full_pub, rows = ['# The rewrite, whole', ''], ['# The published article, whole', ''], []
for i, ((ph, pb), (ah, ab)) in enumerate(zip(pub, art), 1):
    marked = ms.mark_author(ab, owners)
    full_rw += [ah, '', marked, '']
    full_pub += [ph, '', pb, '']
    his = sum(len(m.split()) for m in re.findall(re.escape(ms.MARK_OPEN) + r'(.*?)' + re.escape(ms.MARK_CLOSE), marked, re.S))
    rows.append((i, ph.lstrip('# '), len(pb.split()), len(ab.split()), his))
(HERE / 'REWRITE-FULL.md').write_text('\n'.join(full_rw), encoding='utf-8')
(HERE / 'PUBLISHED-FULL.md').write_text('\n'.join(full_pub), encoding='utf-8')
tp, tr, th = (sum(r[k] for r in rows) for k in (2, 3, 4))
lines = ['# Word counts, published and rewrite', '',
         'Visible words (comments, image lines and link targets left out). "Joel\'s" is the rewrite\'s words inside author marks.', '',
         '| # | Section | Published | Rewrite | Change | Joel\'s words in the rewrite |', '|---|---|---|---|---|---|']
lines += ['| %d | %s | %d | %d | %+d%% | %d |' % (i, h, p, r, round(100 * (r - p) / p), j) for i, h, p, r, j in rows]
lines += ['| | Total | %d | %d | %+d%% | %d |' % (tp, tr, round(100 * (tr - tp) / tp), th)]
(HERE / 'LENGTHS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

led = json.loads((C / 'OWNER-EDITS.json').read_text(encoding='utf-8'))
out = ['# Changes Joel made or approved', '',
       'From the owner-edits ledger: each entry is a change he made himself ("his" words) or a wording of mine he approved '
       '("proposed" words). "Cuts" are published words he took out or approved taking out. A difference these explain is his '
       'choice, not a fault of the rewrite.', '']
for e in led['entries']:
    if e.get('status') == 'superseded':
        continue
    j = e.get('joel', '')
    if isinstance(j, str) and len(j) > 500:
        j = j[:500] + ' ...'
    out += ['- **%s** (%s, %s words): %s' % (e['id'], e.get('when', '')[:16], e.get('words', '?'), e.get('what', '')),
            '  - Joel: "%s"' % (j if isinstance(j, str) else json.dumps(j, ensure_ascii=False)[:500])]
    if e.get('must_not_contain'):
        out.append('  - Cuts: ' + '; '.join('"%s"' % s for s in e['must_not_contain']))
(HERE / 'JOEL-CHANGES.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'UNINCORPORATED-IDEAS.md').write_text((A / 'UNINCORPORATED-IDEAS.md').read_text(encoding='utf-8'), encoding='utf-8')

# Links: every URL of the published article that the rewrite no longer has, and every new one.
URLS = re.compile(r'\]\((https?://[^)\s]+)\)')
def urls(md):
    return URLS.findall(re.sub(r'<!--.*?-->', ' ', md, flags=re.S))
pu, au = urls(PUB.read_text(encoding='utf-8')), urls(ART.read_text(encoding='utf-8'))
gone = [u for u in dict.fromkeys(pu) if u not in au]
new = [u for u in dict.fromkeys(au) if u not in pu]
L = ['# Links, published and rewrite', '', 'Published: %d links (%d distinct). Rewrite: %d links (%d distinct).' %
     (len(pu), len(set(pu)), len(au), len(set(au))), '', '## In the published article, not in the rewrite', '']
L += ['- %s' % u for u in gone] or ['- none']
L += ['', '## In the rewrite, not in the published article', '']
L += ['- %s' % u for u in new] or ['- none']
(HERE / 'LINKS.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
print('pairs A-D, REWRITE-FULL (%d author marks), LENGTHS (%d -> %d words, %d his), JOEL-CHANGES, LINKS (%d gone, %d new)'
      % ('\n'.join(full_rw).count(ms.MARK_OPEN), tp, tr, th, len(gone), len(new)))
