#!/usr/bin/env python3
"""file_links_check.py - a file going to Joel for editing must carry the article's links and pictures.

Lesson E337 (Inner Child). In turn 115 I sent him the whole Inner Child guide as a Word file with every weak spot
highlighted, built from plain text: it had no links and no pictures at all. He did his whole reorganization in that file,
so 55 of the guide's 67 links and all seven of the live post's pictures and videos were gone from the guide he sent back
(Joel, 2026-11-03 21:45 UTC: "yes the links were gone when you sent me the file"). Nothing compared the file with the
article before it went. This does: every link of the article must be in the file (by address), and the file must have at
least as many pictures as the article.

  python3 tools/humanization/file_links_check.py --article ARTICLE FILE [--allow-missing-images]

ARTICLE: the article's Markdown (links as [text](url); pictures as ![..](..), "[image N](...)" lines, or the humanized
files' "<!-- IMAGE url" and "<!-- EMBED url" notes, a video, an audio or a post card counting as a picture) or its HTML
(<a href>, <img>, Substack's video, audio and post embeds, the article page's embed boxes). FILE: .docx, .odt, .html or
.md. Exit 0 when nothing is lost, 1 with the list when something is, 2 on a bad call."""
import argparse
import html as htmlmod
import pathlib
import re
import sys
import zipfile

MD_LINK = re.compile(r'(?<!!)\[([^\[\]]+)\]\s?\(<?([^()\s<>]+(?:\([^()\s]*\))?[^()\s<>]*)>?\)')
MD_IMAGE = re.compile(r'!\[[^\]]*\]\(([^)\s]+)\)|^\[image \d+\]\(([^)\s]+)\)|<!--\s*(?:IMAGE|EMBED)\s+(\S+)', re.M)
HTML_A = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S | re.I)
HTML_IMG = re.compile(r'<img\s[^>]*src="([^"]+)"', re.I)
EMBED = re.compile(r'youtube2-[A-Za-z0-9_-]+|class="native-(?:video|audio)-embed"|class="digest-post-embed"')
BOX = re.compile(r'class="art-(?:embed|img art-missing)"')   # the article page's embed boxes, and a picture it couldn't show


def html_pics(t):
    """Pictures, videos, audios and post cards in an HTML page: each picture once, each embed where it is."""
    return len(set(HTML_IMG.findall(t))) + len(set(EMBED.findall(t))) + len(BOX.findall(t))


def norm(u):
    u = htmlmod.unescape(u.strip().strip('<>'))
    u = re.sub(r'^http://', 'https://', u)
    if not re.match(r'https?://', u) and '.' in u.split('/')[0]:
        u = 'https://' + u
    return u.rstrip('/')


def read_article(path):
    t = pathlib.Path(path).read_text(encoding='utf-8')
    if path.lower().endswith(('.html', '.htm')):
        links = [(norm(h), re.sub(r'<[^>]+>', '', x)) for h, x in HTML_A.findall(t) if h.startswith('http')]
        return links, html_pics(t)
    body = re.sub(r'<!--(?!\s*(?:IMAGE|EMBED)).*?-->', '', t, flags=re.S)
    links = [(norm(u), x) for x, u in MD_LINK.findall(body) if not u.startswith('Pictures/')]
    pics = len(MD_IMAGE.findall(body))
    return links, pics


def read_file(path):
    p = path.lower()
    if p.endswith('.docx'):
        z = zipfile.ZipFile(path)
        rels = z.read('word/_rels/document.xml.rels').decode('utf-8')
        targets = dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"[^>]*TargetMode="External"', rels))
        targets.update(dict((i, t) for t, i in re.findall(r'Target="([^"]+)"[^>]*Id="([^"]+)"[^>]*TargetMode="External"', rels)))
        doc = z.read('word/document.xml').decode('utf-8')
        links = [norm(targets[i]) for i in re.findall(r'<w:hyperlink [^>]*r:id="([^"]+)"', doc) if i in targets]
        pics = sum(1 for n in z.namelist() if n.startswith('word/media/'))
        return links, pics
    if p.endswith('.odt'):
        z = zipfile.ZipFile(path)
        x = z.read('content.xml').decode('utf-8')
        links = [norm(h) for h in re.findall(r'<text:a [^>]*xlink:href="([^"]+)"', x)]
        pics = sum(1 for n in z.namelist() if n.startswith('Pictures/'))
        return links, pics
    t = pathlib.Path(path).read_text(encoding='utf-8')
    if p.endswith(('.html', '.htm')):
        return [norm(h) for h, _ in HTML_A.findall(t)], html_pics(t)
    return [norm(u) for _, u in MD_LINK.findall(t)], len(MD_IMAGE.findall(t))


def lost(article, file):
    """(links of the article missing from the file as [(url, text)], article pictures, file pictures)."""
    alinks, apics = read_article(article)
    flinks, fpics = read_file(file)
    have = set(flinks)
    missing, seen = [], set()
    for u, x in alinks:
        if u not in have and u not in seen:
            missing.append((u, x))
            seen.add(u)
    return missing, apics, fpics


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--article', required=True)
    ap.add_argument('file')
    ap.add_argument('--allow-missing-images', action='store_true', help='a file meant to have no pictures (say why in the turn)')
    a = ap.parse_args(argv)
    missing, apics, fpics = lost(a.article, a.file)
    bad = bool(missing) or (fpics < apics and not a.allow_missing_images)
    print('%s: %d of the article\'s links missing; pictures %d in the article, %d in the file'
          % (a.file, len(missing), apics, fpics))
    for u, x in missing:
        print('  missing link: "%s" -> %s' % (x[:60], u))
    if fpics < apics and not a.allow_missing_images:
        print('  missing pictures: %d' % (apics - fpics))
    print('FAIL' if bad else 'PASS')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
