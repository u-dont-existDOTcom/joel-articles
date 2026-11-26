#!/usr/bin/env bash
# Installs (or updates) the daily look at the live posts on this computer, as a systemd user timer.
# Run from a clone of joel-articles:  bash scripts/laptop/install-depends-watch.sh
# Joel said yes to it on 2026-11-26 ("yes you can run the check on daily timer sure"). It needs git, python3 and an
# authenticated gh. To stop it: systemctl --user disable --now depends-watch.timer
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
dir="${XDG_DATA_HOME:-$HOME/.local/share}/joel-articles-watch"
units="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
mkdir -p "$dir" "$units"
install -m 755 "$here/depends-watch-run.sh" "$dir/depends-watch-run.sh"
install -m 644 "$here/depends-watch.service" "$units/depends-watch.service"
install -m 644 "$here/depends-watch.timer" "$units/depends-watch.timer"
for need in git python3 gh; do command -v "$need" >/dev/null || { echo "missing: $need"; exit 1; }; done
gh auth status >/dev/null 2>&1 || { echo "gh is not signed in: gh auth login"; exit 1; }
systemctl --user daemon-reload
systemctl --user enable --now depends-watch.timer
systemctl --user list-timers depends-watch.timer --no-pager
