#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
printf '%s\n' 'Deprecated clipboard-specific entry point; using local source auto-discovery.' >&2
exec bash scripts/run_inner_child_guide_update_20260826.sh "$@"
