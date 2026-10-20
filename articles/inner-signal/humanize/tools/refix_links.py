"""refix_links.py - the published links' places in a refix text (2026-10-18).

A refix stretch is Emulate's rewrite, so a published link's words may be gone, reworded or moved. install_fixed.py
refuses a stretch that drops a published link without a "links" record ({"published": its anchor, "new": the words that
carry it now}). This finds them:

  python3 tools/refix_links.py check UNITS.json [...]       each published link: kept (its words are in the stretch),
                                                            recorded, or missing (with the stretch's text)
  python3 tools/refix_links.py auto UNITS.json [...]        record every link whose words the stretch still has
  python3 tools/refix_links.py set UNITS.json BLOCK "published anchor" "new words"   record one by hand

A link whose subject the stretch no longer mentions is a lost citation: a meaning problem for the triage, not a link to
force onto other words.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import assemble as A  # noqa: E402
import sections as S  # noqa: E402
import substack_merge as SM  # noqa: E402


def links_of(key, u):
    pub = '\n\n'.join(A.kb()[key][b][0] for b in u['blocks'])
    return [S.plain(m.group(1)) for m in SM.MD_LINK.finditer(pub)]


def scan(path, record=False):
    d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    out = []
    for u in d['units']:
        if u['kind'] != 'emulate':
            continue
        text = '\n\n'.join(u['paras'])
        have = {S.plain(l['published']) for l in u.get('links') or []}
        for a in links_of(d['key'], u):
            if a in have:
                out.append((u['blocks'][0], a, 'recorded', None)); continue
            i = text.lower().find(a.lower())
            if i >= 0:
                out.append((u['blocks'][0], a, 'kept', text[i:i + len(a)]))
                if record:
                    u.setdefault('links', []).append({'published': a, 'new': text[i:i + len(a)]})
            else:
                out.append((u['blocks'][0], a, 'missing', text))
    if record:
        pathlib.Path(path).write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return d['key'], out


def set_link(path, block, published, new):
    d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    u = next(x for x in d['units'] if x['kind'] == 'emulate' and x['blocks'][0] == int(block))
    if new not in '\n\n'.join(u['paras']):
        raise SystemExit('the words %r are not in stretch B%s' % (new, block))
    if published not in links_of(d['key'], u):
        raise SystemExit('stretch B%s has no published link %r' % (block, published))
    u['links'] = [l for l in u.get('links') or [] if S.plain(l['published']) != published] + [{'published': published, 'new': new}]
    pathlib.Path(path).write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'set':
        set_link(*sys.argv[2:6])
    else:
        for p in sys.argv[2:]:
            key, out = scan(p, record=(cmd == 'auto'))
            for b, a, st, x in out:
                print('%s B%d %-8s %r%s' % (key, b, st, a, '' if st != 'missing' else '\n    ' + x.replace('\n', '\n    ')))
