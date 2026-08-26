#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

# Accept an explicit source as the first argument. Otherwise find the newest
# local raw/editor HTML whose content unambiguously identifies the separate
# Inner Child Self-Love Reparenting Guide. This deliberately rejects the
# Inner Signal/self-hypnosis guide, which shares some inner-child language.
if [[ $# -gt 0 ]]; then
  SOURCE="$1"
else
  SOURCE="$({
    python3 - <<'PY'
from pathlib import Path

roots = [Path.home() / "Téléchargements", Path.home() / "Downloads"]
required = (
    "<h1>The Chicken-and-Egg Problem</h1>",
    "<h1>Borrow the Adult Before You Can Be the Adult</h1>",
    "<h2>When Love Is There but Doesn’t Feel Safe</h2>",
    "<h1>How to Forgive Without Forgetting</h1>",
)
wrong_article = "<h1>How to use this very large guide</h1>"
outputs = {
    "inner-child-guide-updated-20260826.html",
    "inner-child-guide-substack-transfer-helper.html",
}

candidates = []
for root in roots:
    if not root.is_dir():
        continue
    for path in root.rglob("*"):
        if not path.is_file() or path.name in outputs:
            continue
        if path.suffix.lower() not in {".html", ".htm", ".txt"}:
            continue
        try:
            if path.stat().st_size > 25_000_000:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        # Some chat-exported copies escape angle brackets.
        normalized = text.replace("\\<", "<").replace("\\>", ">")
        if wrong_article in normalized:
            continue
        if all(marker in normalized for marker in required):
            candidates.append((path.stat().st_mtime, path))

if not candidates:
    raise SystemExit(
        "NO_INNER_CHILD_SOURCE: no local file in ~/Téléchargements or ~/Downloads "
        "matched all four Inner Child guide identity anchors."
    )

candidates.sort(key=lambda item: (item[0], str(item[1])), reverse=True)
print(candidates[0][1])
PY
  } 2>&1)" || {
    printf '%s\n' "$SOURCE" >&2
    printf '%s\n' "Pass the raw Inner Child guide file explicitly, e.g.:" >&2
    printf '%s\n' "  bash scripts/run_inner_child_guide_update_20260826.sh ~/Téléchargements/<file>.html" >&2
    exit 1
  }
fi

SOURCE="$(realpath "$SOURCE")"
printf 'Using Inner Child source: %s\n' "$SOURCE"

python3 scripts/enable_conservative_native_audio_transfer_20260826.py --repo "$ROOT"
python3 scripts/update_inner_child_guide_20260826.py \
  --repo "$ROOT" \
  --input "$SOURCE" \
  --open
