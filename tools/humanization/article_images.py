#!/usr/bin/env python3
"""article_images.py - the images, videos and post cards an article shows, for its reviewers and for Joel's pages.

Joel, 2026-10-11 21:10 UTC, on a reviewer who missed My Journey's recap of the method: "the image should be
enough i think. the reviewer didn't see the image." The gate has said since 2026-10-02 that reviewers get what an
image shows (community section 4, where three cold reads called four named parts unnamed because the diagram
naming them showed as "[an image]"). But the Inner Child article's Markdown had no image in it at all, so no prompt
could show one: the line before the study chart ("The image below maps out the details as best as I can fit:")
pointed at nothing.

An image is an HTML comment on its own line, where the image goes:

    <!-- IMAGE https://...png : what the image shows, for a reader who can't see it -->

A video, an audio or a post card the post embeds is the same, with EMBED (turn 117, lesson E341: the file
Joel edited had lost the post's videos, and the guide had no way to say where one goes):

    <!-- EMBED https://www.youtube.com/watch?v=... : what it is -->
    <!-- EMBED https://ibogaqueen.substack.com/p/... : Post card: "its title" -->
    <!-- EMBED substack-video:<the post's media upload id> : what it is -->    (a video uploaded to the post)
    <!-- EMBED substack-audio:<the post's audio upload id> : what it is -->    (an audio uploaded to the post)

An image's address can also be a picture of Joel's that isn't online yet: "odt:Pictures/<name>" (a picture inside his
ODT) or "laptop:<path on his laptop, %20 for a space>". The page shows it when the renderer is given a folder with the
file (render_article_so_far.py --images), and a box naming it when not.

Comments are stripped from the text Pangram checks and from the paragraph numbering, so the notes change neither.
The review prompts show them as "[an image: what it shows]" or "[a video: what it is]" (show()), and the article page
shows the image itself with the description as its alt text, and an embed as a box with its link (figure_html()).
"""
import html
import re

NOTE = re.compile(r'<!--\s*IMAGE\s+(\S+)\s*:\s*(.*?)\s*-->', re.S)
EMBED = re.compile(r'<!--\s*EMBED\s+(\S+)\s*:\s*(.*?)\s*-->', re.S)


def kind(url):
    """What an embed is, in a few words: "a video", "an audio", "a post card"."""
    if url.startswith('substack-audio:'):
        return 'an audio'
    if url.startswith('substack-video:') or re.match(r'https?://(www\.)?(youtube\.com|youtu\.be)/', url):
        return 'a video'
    if re.match(r'https?://[^/]+/p/', url):
        return 'a post card'
    return 'an embed'


def show(md):
    """The text with each image note as "[an image: description]" and each embed as "[a video: description]" (or an
    audio, a post card), for a reviewer's prompt. Run it before the prompt's builder strips the other comments."""
    md = NOTE.sub(lambda m: '[an image: %s]' % ' '.join(m.group(2).split()), md)
    return EMBED.sub(lambda m: '[%s: %s]' % (kind(m.group(1)), ' '.join(m.group(2).split())), md)


def figure_html(md, resolve=None):
    """The text with each image note as an HTML figure, and each embed as a box with its link, for the article page.
    RESOLVE(url) gives the src for an image address that isn't on the web (odt:, laptop:), or None."""
    def one(m):
        url, desc = m.group(1), ' '.join(m.group(2).split())
        src = url if re.match(r'https?://', url) else (resolve(url) if resolve else None)
        if not src:
            return ('<figure class="art-img art-missing"><figcaption>Picture: %s <i>(%s)</i></figcaption></figure>'
                    % (html.escape(desc), html.escape(url)))
        return ('<figure class="art-img"><img src="%s" alt="%s" loading="lazy"></figure>'
                % (html.escape(src, quote=True), html.escape(desc, quote=True)))

    def box(m):
        url, desc = m.group(1), ' '.join(m.group(2).split())
        k = kind(url)
        if re.match(r'https?://', url):
            where = '<a href="%s">%s</a>' % (html.escape(url, quote=True), html.escape(url))
        else:
            where = 'uploaded to the post (%s)' % html.escape(url)
        return ('<figure class="art-embed"><figcaption><b>%s</b>: %s<br>%s</figcaption></figure>'
                % (html.escape(k[0].upper() + k[1:]), html.escape(desc), where))
    return EMBED.sub(box, NOTE.sub(one, md))


def notes(md):
    """[(url, description)] for every image note in the text, in order."""
    return [(m.group(1), ' '.join(m.group(2).split())) for m in NOTE.finditer(md)]


def embeds(md):
    """[(url, description)] for every embed note in the text, in order."""
    return [(m.group(1), ' '.join(m.group(2).split())) for m in EMBED.finditer(md)]
