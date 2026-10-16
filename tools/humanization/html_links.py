"""html_links.py - text for Joel's pages with every web address a link he can click (2026-10-16).

Joel, 2026-10-16 21:05 UTC: "(your links are not clickable btw)". My final message gave each Pangram check as a bare address,
which his app doesn't turn into a link, and the pages had the same gap: `render_in_context.py` and
`render_article_so_far.py` escaped every note, so a check's address showed as text, and `render_questions.py` sent bare
addresses through Markdown, which only links [text](url) and <url>. Nothing checked that a link could be clicked: the link
checks asked only that a Pangram result carry its address (`pangram_links_check.py`).

  linkify(text) -> html.escape(text) with each http(s) address an <a href>.
  autolink_markdown(md) -> the Markdown with each bare address written as <url>, so Markdown links it.
  bare_urls(md) -> the addresses in a chat message that aren't written as [text](url), which is what a chat shows as a link.
  join_split_links(md) -> a link whose text spans a blank line (the post card Substack pastes: "[", a heading, "](url)")
    written as the heading with its link, which Markdown can parse. The article page showed that card's address as text.
  bare_urls_in_html(page) -> the addresses a page shows as text, outside any <a>: the check for a page sent to Joel.

  python3 tools/humanization/html_links.py PAGE.html [PAGE.html ...]   prints each page's bare addresses; exit 1 if any.
"""
import html
import re

URL = re.compile(r'https?://[^\s<>"\]`]+')


def _trim(url):
    """An address ends before the punctuation that ends its sentence or closes the parenthesis it sits in."""
    while url and (url[-1] in '.,;:!?\'"' or (url[-1] == ')' and url.count(')') > url.count('('))):
        url = url[:-1]
    return url


def linkify(text):
    out, last = [], 0
    for m in URL.finditer(text):
        url = _trim(m.group(0))
        if not url:
            continue
        out.append(html.escape(text[last:m.start()]))
        out.append('<a href="%s">%s</a>' % (html.escape(url, quote=True), html.escape(url)))
        last = m.start() + len(url)
    out.append(html.escape(text[last:]))
    return ''.join(out)


def _code_spans(md):
    """(start, end) of each `code` span and fenced block: an address there is a command's text, not a link."""
    spans = [(m.start(), m.end()) for m in re.finditer(r'```.*?```', md, re.S)]
    spans += [(m.start(), m.end()) for m in re.finditer(r'`[^`\n]+`', md)]
    return spans


def _bare(md):
    """The bare addresses of a Markdown text: (start, end, url), outside [text](url), <url> and code."""
    code = _code_spans(md)
    out = []
    for m in URL.finditer(md):
        s = m.start()
        if any(a <= s < b for a, b in code):
            continue
        if md[max(0, s - 2):s] == '](' or md[max(0, s - 1):s] == '<' or md[max(0, s - 6):s].endswith('href="'):
            continue
        url = _trim(m.group(0))
        if url:
            out.append((s, s + len(url), url))
    return out


def autolink_markdown(md):
    out, last = [], 0
    for s, e, url in _bare(md):
        out.append(md[last:s])
        out.append('<%s>' % url)
        last = e
    out.append(md[last:])
    return ''.join(out)


def bare_urls(md):
    return [url for _, _, url in _bare(md)]


SPLIT_LINK = re.compile(r'\[[ \t]*\n\s*\n(#{1,6})[ \t]*([^\n]+?)[ \t]*\n\s*\n\]\((https?://[^)\s]+)\)')


def join_split_links(md):
    return SPLIT_LINK.sub(lambda m: '\n\n%s [%s](%s)\n\n' % (m.group(1), m.group(2), m.group(3)), md)


def bare_urls_in_html(page):
    body = re.sub(r'<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->', '', page, flags=re.S | re.I)
    body = re.sub(r'<a\s[^>]*>.*?</a>', ' ', body, flags=re.S | re.I)
    body = re.sub(r'<[^>]+>', ' ', body)
    return [u for u in (_trim(html.unescape(m.group(0))) for m in URL.finditer(body)) if u]


if __name__ == '__main__':
    import sys
    bad = 0
    for f in sys.argv[1:]:
        urls = bare_urls_in_html(open(f, encoding='utf-8').read())
        bad += len(urls)
        print('%s: %s' % (f, 'every address is a link' if not urls else '%d shown as text: %s' % (len(urls), ', '.join(urls[:5]))))
    sys.exit(1 if bad else 0)
