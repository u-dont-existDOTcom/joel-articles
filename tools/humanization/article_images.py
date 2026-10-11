#!/usr/bin/env python3
"""article_images.py - the images an article shows, for its reviewers and for Joel's pages.

Joel, 2026-10-11 21:10 UTC, on a reviewer who missed My Journey's recap of the method: "the image should be
enough i think. the reviewer didn't see the image." The gate has said since 2026-10-02 that reviewers get what an
image shows (community section 4, where three cold reads called four named parts unnamed because the diagram
naming them showed as "[an image]"). But the Inner Child article's Markdown had no image in it at all, so no prompt
could show one: the line before the study chart ("The image below maps out the details as best as I can fit:")
pointed at nothing.

An image is an HTML comment on its own line, where the image goes:

    <!-- IMAGE https://...png : what the image shows, for a reader who can't see it -->

Comments are stripped from the text Pangram checks and from the paragraph numbering, so the note changes neither.
The review prompts show it as "[an image: what it shows]" (show()), and the article page shows the image itself
with the description as its alt text (figure_html()).
"""
import html
import re

NOTE = re.compile(r'<!--\s*IMAGE\s+(\S+)\s*:\s*(.*?)\s*-->', re.S)


def show(md):
    """The text with each image note as "[an image: description]", for a reviewer's prompt. Run it before the
    prompt's builder strips the other comments."""
    return NOTE.sub(lambda m: '[an image: %s]' % ' '.join(m.group(2).split()), md)


def figure_html(md):
    """The text with each image note as an HTML figure, for the article page."""
    def one(m):
        url, desc = m.group(1), ' '.join(m.group(2).split())
        return ('<figure class="art-img"><img src="%s" alt="%s" loading="lazy"></figure>'
                % (html.escape(url, quote=True), html.escape(desc, quote=True)))
    return NOTE.sub(one, md)


def notes(md):
    """[(url, description)] for every image note in the text, in order."""
    return [(m.group(1), ' '.join(m.group(2).split())) for m in NOTE.finditer(md)]
