#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
python3 scripts/enable_conservative_native_audio_transfer_20260826.py --repo "$ROOT"
python3 scripts/update_inner_child_guide_20260826.py --repo "$ROOT" --clipboard --open
