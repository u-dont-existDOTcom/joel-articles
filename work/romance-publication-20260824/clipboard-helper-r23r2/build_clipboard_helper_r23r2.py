#!/usr/bin/env python3
"""Build the conservative Romance r23r2 Substack clipboard helper.

The registered Romance authority is Markdown with position-locked publication
markers. The repository does not contain the raw Substack editor HTML that the
publishing protocol requires for exact native-widget identity and metadata.
Accordingly, this builder preserves the exact prose and ordinary Markdown
structure, carries only identities present in the registered markers, and
records the raw-HTML limitation instead of inventing native markup.
"""
from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import html
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt


EXPECTED_MASTER_SHA256 = "f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c"
EXPECTED_MASTER_WORDS = 20_364
EXPECTED_NATIVE_MARKERS = 11
EXPECTED_MARKDOWN_LINKS = 22
EXPECTED_HEADINGS = 44
EXPECTED_OWNER_FINAL_SPAN = (
    "Maybe an unusually strong couple can get away without much community. I think that's rare.  "
    "But sometimes a friend who actually knows us both sees the pattern before either of us does. "
    "On the other hand, If both people are falling apart, there is only so much anyone else can do."
)
FORMAT = "joel-romance-r23r2-markdown-clipboard-fallback-v1"
PAYLOAD_PREFIX = '<div dir="auto" class="body markup">'
PAYLOAD_SUFFIX = "</div>"
NATIVE_RE = re.compile(r"^\[NATIVE (?P<body>.+)\]$")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def b64(value: str) -> str:
    return base64.b64encode(value.encode("utf-8")).decode("ascii")


def git_value(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=root, check=True, text=True, capture_output=True
    ).stdout.strip()


def nearby_anchor(lines: list[str], line_index: int, step: int) -> str | None:
    cursor = line_index + step
    while 0 <= cursor < len(lines):
        value = lines[cursor].strip()
        if value:
            return value[:240]
        cursor += step
    return None


def classify_native_marker(marker: str) -> tuple[str, str, str | None]:
    if marker.startswith("IMAGE —"):
        url = re.search(r"https?://[^\]]+", marker)
        if not url:
            raise ValueError(f"Image marker lacks URL: {marker}")
        return "image", "standard_image_html_from_registered_url", url.group(0)
    if marker.startswith("SUBSTACK PREVIEW —"):
        url = re.search(r"https?://[^\]]+", marker)
        if not url:
            raise ValueError(f"Substack preview marker lacks URL: {marker}")
        return "substack_preview", "canonical_url_in_payload_fallback", url.group(0)
    if marker.startswith("YOUTUBE —"):
        match = re.search(r"videoId:\s*([^\s\]]+)", marker)
        if not match:
            raise ValueError(f"YouTube marker lacks videoId: {marker}")
        video_id = match.group(1)
        return "youtube", "canonical_youtube_url_in_payload", video_id
    if marker.startswith("BUTTON — Subscribe now —"):
        return "subscribe", "manual_native_reinsertion", "%%checkout_url%%"
    if "VIDEO" in marker.upper():
        return "unclassified_video", "blocked_without_raw_editor_html", None
    return "unknown", "blocked_without_raw_editor_html", None


def marker_html(object_id: str, object_type: str, identity: str | None) -> str:
    object_attr = html.escape(object_id, quote=True)
    if object_type == "image" and identity:
        src = html.escape(identity, quote=True)
        return (
            f'<figure data-romance-transport-object="{object_attr}" '
            f'data-source-kind="registered-markdown-marker"><img src="{src}" alt=""></figure>'
        )
    if object_type == "substack_preview" and identity:
        return (
            f'<p data-romance-transport-object="{object_attr}" '
            f'data-source-kind="registered-markdown-marker">{html.escape(identity)}</p>'
        )
    if object_type == "youtube" and identity:
        url = f"https://www.youtube.com/watch?v={identity}"
        return (
            f'<p data-romance-transport-object="{object_attr}" '
            f'data-source-kind="registered-markdown-marker">{html.escape(url)}</p>'
        )
    raise ValueError(f"No portable fallback conversion for {object_type}")


def text_projection(raw_html: str, *, remove_transport_objects: bool) -> str:
    soup = BeautifulSoup(raw_html, "html.parser")
    if remove_transport_objects:
        for node in soup.select("[data-romance-transport-object]"):
            node.decompose()
    lines = [line.strip() for line in soup.get_text("\n").replace("\r\n", "\n").splitlines()]
    return "\n".join(line for line in lines if line)


def heading_projection(raw_html: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(raw_html, "html.parser")
    return [
        {"level": int(node.name[1]), "text": node.get_text()}
        for node in soup.find_all(re.compile(r"^h[1-6]$"))
    ]


def link_projection(raw_html: str) -> list[str]:
    soup = BeautifulSoup(raw_html, "html.parser")
    return [str(node.get("href")) for node in soup.find_all("a", href=True)]


def structural_counts(raw_html: str) -> dict[str, int]:
    soup = BeautifulSoup(raw_html, "html.parser")
    return {
        "emphasis": len(soup.find_all("em")),
        "strong": len(soup.find_all("strong")),
        "blockquotes": len(soup.find_all("blockquote")),
        "ordered_lists": len(soup.find_all("ol")),
        "unordered_lists": len(soup.find_all("ul")),
        "list_items": len(soup.find_all("li")),
        "horizontal_rules": len(soup.find_all("hr")),
    }


def helper_document(embedded: dict[str, Any]) -> str:
    data = json.dumps(embedded, ensure_ascii=False).replace("</", "<\\/")
    source_hash = html.escape(embedded["source"]["master_sha256"])
    payload_hash = html.escape(embedded["segments"][0]["payload_sha256"])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Romance r23r2 — Substack clipboard helper</title>
<style>
:root {{ color-scheme: light; }}
body {{ font-family: system-ui, sans-serif; max-width: 780px; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; color: #222; }}
.status {{ border: 1px solid #bbb; border-radius: 10px; padding: 1rem; margin: 1rem 0; }}
.warning {{ border-color: #b26a00; background: #fff6e6; }}
.verified {{ border-color: #19733a; background: #eefaf2; }}
.copy {{ font: inherit; font-weight: 700; padding: .8rem 1rem; cursor: pointer; }}
.copy:disabled {{ cursor: wait; opacity: .55; }}
.result {{ margin-left: .65rem; font-weight: 700; }}
code {{ overflow-wrap: anywhere; }}
.meta {{ font-size: .9rem; color: #555; }}
</style>
</head>
<body>
<h1>Romance r23r2 — Substack clipboard helper</h1>
<div class="status verified"><strong id="verification">Verifying r23r2 payload…</strong></div>
<div class="status warning">
<strong>Native-object limitation:</strong> GitHub does not contain the original raw Substack editor HTML.
This helper preserves the exact registered prose and ordinary formatting, carries registered image/preview/YouTube identities,
and does not invent widget metadata. Manually reinsert the native Share and Subscribe controls, then verify every object in a disposable draft.
</div>
<section class="status">
<h2>1. Copy rich article</h2>
<button class="copy" type="button" id="copy-article" disabled>Copy rich article</button>
<span class="result" id="copy-result" aria-live="polite"></span>
</section>
<section class="status">
<h2>2. Manual native controls</h2>
<ol>
<li>Insert the native <strong>Share</strong> control after the opening image and before “I asked my dad about sex when I was five…”.</li>
<li>Insert the native <strong>Subscribe</strong> control after “I believe Rumi was right: A sacred relationship will open and purify your hearts regardless of whether it ends.”</li>
</ol>
</section>
<p class="meta">Registered master SHA-256: <code>{source_hash}</code><br>
Payload SHA-256: <code>{payload_hash}</code><br>
Segments: 1 · standalone native uploaded-video markers: 0 · raw-source video classification: unavailable.<br>
“Copied” proves clipboard completion only; Substack reconstruction still needs a disposable-draft check.</p>
<script id="romance-transfer-manifest" type="application/json">{data}</script>
<script>
(() => {{
  const manifest = JSON.parse(document.getElementById('romance-transfer-manifest').textContent);
  const button = document.getElementById('copy-article');
  const verification = document.getElementById('verification');
  const result = document.getElementById('copy-result');
  const decode = value => new TextDecoder().decode(Uint8Array.from(atob(value), c => c.charCodeAt(0)));
  const toHex = bytes => Array.from(new Uint8Array(bytes), b => b.toString(16).padStart(2, '0')).join('');

  function legacyCopyRich(rich) {{
    const holder = document.createElement('div');
    holder.contentEditable = 'true';
    holder.setAttribute('aria-hidden', 'true');
    holder.style.position = 'fixed';
    holder.style.left = '-100000px';
    holder.style.top = '0';
    holder.innerHTML = rich;
    document.body.appendChild(holder);
    const range = document.createRange();
    range.selectNodeContents(holder);
    const selection = getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    const ok = document.execCommand('copy');
    selection.removeAllRanges();
    holder.remove();
    if (!ok) throw new Error('Legacy rich copy failed');
  }}

  function copyRichImmediate(rich, plain) {{
    try {{
      if (!navigator.clipboard || !window.ClipboardItem) throw new Error('ClipboardItem unavailable');
      const pending = navigator.clipboard.write([new ClipboardItem({{
        'text/html': new Blob([rich], {{type: 'text/html'}}),
        'text/plain': new Blob([plain], {{type: 'text/plain'}})
      }})]);
      return Promise.resolve(pending).catch(() => legacyCopyRich(rich));
    }} catch (error) {{
      legacyCopyRich(rich);
      return Promise.resolve();
    }}
  }}

  async function verifyPayload() {{
    const segment = manifest.segments[0];
    const rich = decode(segment.html_b64);
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(rich));
    if (toHex(digest) !== segment.payload_sha256) throw new Error('embedded payload hash mismatch');
    verification.textContent = 'VERIFIED r23r2';
    button.disabled = false;
  }}

  button.addEventListener('click', () => {{
    result.textContent = '';
    const segment = manifest.segments[0];
    const rich = decode(segment.html_b64);
    const plain = decode(segment.plain_b64);
    copyRichImmediate(rich, plain)
      .then(() => {{ result.textContent = 'Copied'; }})
      .catch(error => {{ result.textContent = 'Failed'; console.error(error); }});
  }});

  verifyPayload().catch(error => {{
    verification.textContent = 'FAILED verification — do not copy';
    console.error(error);
  }});
}})();
</script>
</body>
</html>'''


def parse_helper_manifest(helper_text: str) -> dict[str, Any]:
    match = re.search(
        r'<script id="romance-transfer-manifest" type="application/json">(.*?)</script>',
        helper_text,
        re.S,
    )
    if not match:
        raise ValueError("Helper lacks embedded transfer manifest")
    return json.loads(match.group(1).replace("<\\/", "</"))


def build_state(root: Path) -> tuple[dict[str, Any], str, str]:
    master_path = root / "articles/romance/master.md"
    registry_path = root / "articles/INDEX.json"
    current_state_path = root / "articles/romance/CURRENT-STATE.md"
    master_bytes = master_path.read_bytes()
    master = master_bytes.decode("utf-8")
    if sha256_bytes(master_bytes) != EXPECTED_MASTER_SHA256:
        raise ValueError("Registered Romance master is not exact r23r2")
    if len(master.split()) != EXPECTED_MASTER_WORDS:
        raise ValueError("Romance r23r2 word count changed")

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    romance = next(item for item in registry["articles"] if item["id"] == "romance")
    if romance["authority"]["master"]["sha256"] != EXPECTED_MASTER_SHA256:
        raise ValueError("Registry does not point to exact r23r2")

    lines = master.splitlines(keepends=True)
    native_count = sum(1 for line in lines if NATIVE_RE.match(line.rstrip("\r\n")))
    links = LINK_RE.findall(master)
    headings_source = [
        {"level": len(match.group(1)), "text": match.group(2)}
        for line in master.splitlines()
        if (match := HEADING_RE.match(line))
    ]
    if native_count != EXPECTED_NATIVE_MARKERS:
        raise ValueError(f"Expected {EXPECTED_NATIVE_MARKERS} native markers; found {native_count}")
    if len(links) != EXPECTED_MARKDOWN_LINKS:
        raise ValueError(f"Expected {EXPECTED_MARKDOWN_LINKS} Markdown links; found {len(links)}")
    if len(headings_source) != EXPECTED_HEADINGS:
        raise ValueError(f"Expected {EXPECTED_HEADINGS} headings; found {len(headings_source)}")

    transport_lines: list[str] = []
    prose_lines: list[str] = []
    objects: list[dict[str, Any]] = []
    manual_steps: list[dict[str, Any]] = []
    native_order = 0
    share_count = 0
    for index, raw_line in enumerate(lines):
        line = raw_line.rstrip("\r\n")
        newline = raw_line[len(line):]
        marker_match = NATIVE_RE.match(line)
        if marker_match:
            native_order += 1
            marker = marker_match.group("body")
            object_type, treatment, identity = classify_native_marker(marker)
            object_id = f"native-{native_order:02d}"
            item = {
                "id": object_id,
                "source_order": len(objects) + 1,
                "native_marker_order": native_order,
                "line": index + 1,
                "type": object_type,
                "source_marker": line,
                "source_sha256": sha256_text(line),
                "identity": identity,
                "preceding_anchor": nearby_anchor([v.rstrip("\r\n") for v in lines], index, -1),
                "following_anchor": nearby_anchor([v.rstrip("\r\n") for v in lines], index, 1),
                "transfer_treatment": treatment,
                "raw_editor_identity_status": "unavailable",
            }
            objects.append(item)
            if treatment == "manual_native_reinsertion":
                manual_steps.append({
                    "object_id": object_id,
                    "type": object_type,
                    "instruction": "Insert the native Subscribe control at the article end after the final Rumi sentence.",
                    "preceding_anchor": item["preceding_anchor"],
                    "following_anchor": item["following_anchor"],
                })
                continue
            if treatment.startswith("blocked_"):
                raise ValueError(f"Unportable marker requires raw editor HTML: {line}")
            transport_lines.append(marker_html(object_id, object_type, identity) + newline)
            continue

        if line == "[Share](%%share_url%%)":
            share_count += 1
            item = {
                "id": "share-01",
                "source_order": len(objects) + 1,
                "line": index + 1,
                "type": "share",
                "source_marker": line,
                "source_sha256": sha256_text(line),
                "identity": "%%share_url%%",
                "preceding_anchor": nearby_anchor([v.rstrip("\r\n") for v in lines], index, -1),
                "following_anchor": nearby_anchor([v.rstrip("\r\n") for v in lines], index, 1),
                "transfer_treatment": "manual_native_reinsertion",
                "raw_editor_identity_status": "unavailable",
            }
            objects.append(item)
            manual_steps.append({
                "object_id": "share-01",
                "type": "share",
                "instruction": "Insert the native Share control after the opening image and before the first prose paragraph.",
                "preceding_anchor": item["preceding_anchor"],
                "following_anchor": item["following_anchor"],
            })
            continue

        transport_lines.append(raw_line)
        prose_lines.append(raw_line)

    if share_count != 1:
        raise ValueError(f"Expected one Share action marker; found {share_count}")

    markdown = MarkdownIt("commonmark", {"html": True})
    transport_markdown = "".join(transport_lines)
    prose_markdown = "".join(prose_lines)
    converted_body = markdown.render(transport_markdown)
    expected_prose_html = markdown.render(prose_markdown)
    payload = PAYLOAD_PREFIX + converted_body + PAYLOAD_SUFFIX
    plain_payload = BeautifulSoup(payload, "html.parser").get_text("\n")
    if EXPECTED_OWNER_FINAL_SPAN not in payload:
        raise ValueError("Exact owner-final Two Pillars span changed during transport")

    source_text_projection = text_projection(expected_prose_html, remove_transport_objects=False)
    payload_text_projection = text_projection(payload, remove_transport_objects=True)
    if payload_text_projection != source_text_projection:
        mismatch = next(
            (position for position, pair in enumerate(zip(source_text_projection, payload_text_projection)) if pair[0] != pair[1]),
            min(len(source_text_projection), len(payload_text_projection)),
        )
        raise ValueError(
            "Article prose projection differs after transport conversion at "
            f"{mismatch}: source={source_text_projection[mismatch:mismatch + 120]!r} "
            f"payload={payload_text_projection[mismatch:mismatch + 120]!r}"
        )

    payload_soup = BeautifulSoup(payload, "html.parser")
    for node in payload_soup.select("[data-romance-transport-object]"):
        node.decompose()
    prose_payload_html = str(payload_soup)
    headings_payload = heading_projection(prose_payload_html)
    if headings_payload != headings_source:
        raise ValueError("Heading hierarchy/text changed in transport conversion")

    source_links = link_projection(expected_prose_html)
    payload_links = link_projection(prose_payload_html)
    if payload_links != source_links:
        raise ValueError("Ordinary link order/destinations changed in transport conversion")

    source_structure = structural_counts(expected_prose_html)
    payload_structure = structural_counts(prose_payload_html)
    if payload_structure != source_structure:
        raise ValueError("Emphasis/list/blockquote/rule structure changed in transport conversion")

    transferred_ids = [
        node.get("data-romance-transport-object")
        for node in BeautifulSoup(payload, "html.parser").select("[data-romance-transport-object]")
    ]
    expected_transferred_ids = [
        item["id"] for item in objects if item["transfer_treatment"] != "manual_native_reinsertion"
    ]
    if transferred_ids != expected_transferred_ids:
        raise ValueError("Publication-object order changed in transport payload")

    object_counts = Counter(item["type"] for item in objects)
    registered_native_video_markers = sum(
        1 for item in objects if item["type"] in {"native_video", "unclassified_video"}
    )
    if registered_native_video_markers:
        raise ValueError("Registered standalone native-video marker requires segmentation/raw source")

    state: dict[str, Any] = {
        "format": FORMAT,
        "source": {
            "repository": "u-dont-existDOTcom/joel-articles",
            "ref": git_value(root, "merge-base", "HEAD", "origin/main"),
            "branch": "main",
            "task_branch": git_value(root, "branch", "--show-current"),
            "master_path": "articles/romance/master.md",
            "master_sha256": EXPECTED_MASTER_SHA256,
            "master_words_whitespace": EXPECTED_MASTER_WORDS,
            "registry_path": "articles/INDEX.json",
            "registry_sha256": sha256_bytes(registry_path.read_bytes()),
            "current_state_path": "articles/romance/CURRENT-STATE.md",
            "current_state_sha256": sha256_bytes(current_state_path.read_bytes()),
            "candidate_id": "romance-r23r2-owner-final-20260824",
        },
        "authority_boundary": {
            "raw_substack_editor_html_available": False,
            "full_protocol_helper_status": "BLOCKED",
            "blocker": (
                "The repository contains no authoritative raw Substack editor HTML for Romance. "
                "Exact native-widget markup, metadata, and raw-source video classification cannot be certified from Markdown."
            ),
            "delivered_artifact_class": "conservative_markdown_and_registered_identity_transport_fallback",
            "invented_native_widget_metadata": False,
        },
        "transport": {
            "browser": "Opera",
            "opening_context": "downloaded local HTML file opened directly",
            "destination": "Substack editor",
            "wrapper": {"tag": "div", "attributes": {"dir": "auto", "class": "body markup"}},
            "segment_count": 1,
            "payload_mode": "single_rich_html_from_registered_marker_inventory",
            "registered_standalone_native_uploaded_video_marker_count": 0,
            "raw_source_certified_native_uploaded_video_count": None,
            "registered_substack_video_post_marker_count": 0,
            "raw_source_certified_substack_video_post_count": None,
            "split_disposition": (
                "No split: no registered marker represents a standalone native Substack-uploaded video. "
                "Raw-source absence prevents certifying the complete editor-object inventory."
            ),
        },
        "source_inventory": {
            "headings": len(headings_source),
            "markdown_links_including_share_action": len(links),
            "ordinary_links_transferred": len(source_links),
            "native_markers": native_count,
            "share_action_markers": share_count,
            "publication_objects_total": len(objects),
            "object_counts": dict(sorted(object_counts.items())),
            "objects": objects,
        },
        "manual_steps": manual_steps,
        "validation": {
            "registered_master_identity": "PASS",
            "word_count": "PASS",
            "prose_projection": "PASS",
            "prose_projection_sha256": sha256_text(source_text_projection),
            "heading_hierarchy_and_text": "PASS",
            "owner_final_two_pillars_span": "PASS",
            "owner_final_two_pillars_span_sha256": sha256_text(EXPECTED_OWNER_FINAL_SPAN),
            "ordinary_link_order_and_destinations": "PASS",
            "emphasis_lists_blockquotes_rules": "PASS",
            "structural_counts": source_structure,
            "publication_object_order": "PASS",
            "unexplained_article_text_deltas": 0,
            "authorized_transport_transformations": len(objects),
            "destination_result": "PENDING_DISPOSABLE_OPERA_TO_SUBSTACK_TEST",
        },
        "segments": [{
            "index": 1,
            "label": "Copy rich article",
            "payload_sha256": sha256_text(payload),
            "plain_text_sha256": sha256_text(plain_payload),
            "html_b64": b64(payload),
            "plain_b64": b64(plain_payload),
        }],
        "pangram": {"called": False, "status": "NOT_RUN_BY_OWNER_INSTRUCTION"},
    }
    return state, payload, source_text_projection


def write_outputs(root: Path, out_dir: Path) -> None:
    state, _payload, _projection = build_state(root)
    embedded = copy.deepcopy(state)
    helper_text = helper_document(embedded)
    helper_path = out_dir / "romance-r23r2-substack-clipboard-helper.html"
    manifest_path = out_dir / "manifest.json"
    validation_path = out_dir / "VALIDATION.md"
    repository_checks_path = out_dir / "REPOSITORY-CHECKS.md"
    readme_path = out_dir / "README.md"
    checksums_path = out_dir / "CHECKSUMS.sha256"
    out_dir.mkdir(parents=True, exist_ok=True)
    helper_path.write_text(helper_text, encoding="utf-8")

    external = copy.deepcopy(state)
    external["segments"] = [
        {key: value for key, value in segment.items() if key not in {"html_b64", "plain_b64"}}
        for segment in state["segments"]
    ]
    external["deliverables"] = {
        "helper": helper_path.name,
        "helper_sha256": sha256_bytes(helper_path.read_bytes()),
        "manifest": manifest_path.name,
        "validation": validation_path.name,
        "readme": readme_path.name,
    }
    manifest_path.write_text(json.dumps(external, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    validation_path.write_text(
        f"""# Romance r23r2 Clipboard Helper Validation

Status: **PASS for conservative Markdown/registered-identity transport; BLOCKED for full raw-editor native-object certification.**

- Registered master: `articles/romance/master.md`
- Master SHA-256: `{state['source']['master_sha256']}`
- Master words (whitespace): {state['source']['master_words_whitespace']:,}
- Helper payload SHA-256: `{state['segments'][0]['payload_sha256']}`
- Segment count: **1**
- Registered native markers: **{state['source_inventory']['native_markers']}**
- Publication-object sequence: **{state['source_inventory']['publication_objects_total']}** objects including the separate Share action marker
- Registered standalone native uploaded-video markers: **0**
- Registered Substack video-post markers: **0**
- Manual native reinsertion steps: **2** — Share and Subscribe
- Prose projection: **PASS**, SHA-256 `{state['validation']['prose_projection_sha256']}`
- Exact owner-final Two Pillars span: **PASS**, SHA-256 `{state['validation']['owner_final_two_pillars_span_sha256']}`
- Headings: **PASS** ({state['source_inventory']['headings']})
- Ordinary link destinations/order: **PASS** ({state['source_inventory']['ordinary_links_transferred']} transported; source has {state['source_inventory']['markdown_links_including_share_action']} Markdown links including Share)
- Emphasis, lists, blockquote, and horizontal rules: **PASS**
- Publication-object order: **PASS**
- Unexplained article-text deltas: **0**
- Pangram: **not run**
- Destination result: **pending a real Opera → disposable Substack draft check**

## Authority blocker

The repository does not contain the original raw Romance Substack editor HTML. Under the current publishing protocol, that HTML is the sole authority for exact native-widget markup, metadata, captions/dimensions, raw native-video classification, and byte-identical object identity. This fallback therefore carries only the identities present in the registered Markdown markers and does not claim a fully protocol-authoritative native-object reconstruction.
""",
        encoding="utf-8",
    )

    readme_path.write_text(
        f"""# Romance r23r2 Substack Clipboard Helper

Open `romance-r23r2-substack-clipboard-helper.html` directly in Opera. Wait for **VERIFIED r23r2**, click **Copy rich article**, and paste into a blank Substack draft.

## Ordered copy parts

1. **Copy rich article** — one rich-HTML segment. The registered marker inventory contains no standalone native Substack-uploaded video marker, so no video split was introduced.

## Manual reinsertion

1. Insert Substack's native **Share** control after the opening image and before the paragraph beginning `I asked my dad about sex when I was five…`.
2. Insert Substack's native **Subscribe** control after the final sentence beginning `I believe Rumi was right…`, at the end of the article.

The helper carries three registered image URLs, one Substack-preview URL, and six YouTube IDs in source order. Verify all ten reconstructed/carried objects in the disposable draft.

## Exact source and limitation

- Registered r23r2 master SHA-256: `{state['source']['master_sha256']}`
- Helper SHA-256: `{external['deliverables']['helper_sha256']}`
- Payload SHA-256: `{state['segments'][0]['payload_sha256']}`
- Segment count: **1**
- Pangram was not run.

The canonical repository has no raw Romance Substack editor HTML. This is therefore a conservative exact-prose/registered-identity fallback, not a certification of original native-widget markup or metadata. Do not infer additional video splits or widget identities from Markdown; if authoritative raw editor HTML becomes available, rebuild with the canonical `html_islands.py.txt` and `substack_transfer_helper.py.txt` workflow.
""",
        encoding="utf-8",
    )

    checksum_files = [helper_path, manifest_path, validation_path, readme_path]
    if repository_checks_path.is_file():
        checksum_files.append(repository_checks_path)
    checksums_path.write_text(
        "".join(f"{sha256_bytes(path.read_bytes())}  {path.name}\n" for path in checksum_files),
        encoding="utf-8",
    )


def verify_outputs(root: Path, out_dir: Path) -> None:
    state, _payload, _projection = build_state(root)
    helper_path = out_dir / "romance-r23r2-substack-clipboard-helper.html"
    manifest_path = out_dir / "manifest.json"
    checksums_path = out_dir / "CHECKSUMS.sha256"
    helper_text = helper_path.read_text(encoding="utf-8")
    embedded = parse_helper_manifest(helper_text)
    if embedded != state:
        raise ValueError("Embedded helper manifest differs from exact current source conversion")
    if "navigator.clipboard.write" not in helper_text or "new ClipboardItem" not in helper_text:
        raise ValueError("Helper lacks immediate ClipboardItem path")
    if "document.execCommand('copy')" not in helper_text or "contentEditable = 'true'" not in helper_text:
        raise ValueError("Helper lacks silent rich-copy fallback")
    if re.search(r"<textarea\b", helper_text, re.I):
        raise ValueError("Helper contains forbidden visible textarea fallback")
    listener = re.search(r"button\.addEventListener\('click'.*?\n\s*\}\);", helper_text, re.S)
    if listener and re.search(r"\bawait\b", listener.group(0)):
        raise ValueError("Clipboard click path awaits work before ClipboardItem")

    external = json.loads(manifest_path.read_text(encoding="utf-8"))
    if external["deliverables"]["helper_sha256"] != sha256_bytes(helper_path.read_bytes()):
        raise ValueError("External manifest helper hash mismatch")
    for row in checksums_path.read_text(encoding="utf-8").splitlines():
        digest, name = row.split("  ", 1)
        if sha256_bytes((out_dir / name).read_bytes()) != digest:
            raise ValueError(f"Checksum mismatch: {name}")
    print("Romance r23r2 helper verification: PASS")
    print(f"master={state['source']['master_sha256']}")
    print(f"payload={state['segments'][0]['payload_sha256']}")
    print(f"helper={sha256_bytes(helper_path.read_bytes())}")
    print(f"segments={state['transport']['segment_count']}")
    print(f"objects={state['source_inventory']['publication_objects_total']}")
    print(f"manual_steps={len(state['manual_steps'])}")
    print("full_raw_editor_native_object_certification=BLOCKED")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "verify"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        if args.command == "build":
            write_outputs(args.root.resolve(), args.out_dir.resolve())
            print(f"Built Romance r23r2 helper in {args.out_dir.resolve()}")
        else:
            verify_outputs(args.root.resolve(), args.out_dir.resolve())
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
