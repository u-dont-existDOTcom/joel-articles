#!/usr/bin/env bash
# The daily look at Joel's live posts, run from his laptop by a systemd user timer.
#
# Why here: Substack answers GitHub's servers with HTTP 403 (2026-11-25, runs 45659968509 and 45661315269 of
# .github/workflows/depends-watch.yml), and it answers his laptop. Joel, 2026-11-26 22:44 UTC: "yes you can run the
# check on daily timer sure".
#
# What it does, once a day: brings its own clone of joel-articles up to main (a folder only this script uses), runs
# scripts/watch_live_posts.py against the four live posts, and opens, updates or closes the GitHub issues the same way
# the workflow would (labels depends-watch and depends-watch-fetch), with his gh. When a registered passage changed it
# also shows a desktop notice, if the desktop allows one. Nothing outside its folder is written; the repository itself
# is only read. Its folder: ${XDG_DATA_HOME:-~/.local/share}/joel-articles-watch (clone, last report, last result, log).
#
# Install or update: scripts/laptop/install-depends-watch.sh. Run once by hand: systemctl --user start depends-watch
set -u
REPO_URL=https://github.com/u-dont-existDOTcom/joel-articles
DIR="${XDG_DATA_HOME:-$HOME/.local/share}/joel-articles-watch"
CLONE="$DIR/repo"
LOG="$DIR/watch.log"
mkdir -p "$DIR"
stamp=$(date -u +%Y-%m-%dT%H:%MZ)
{
  echo "== $stamp start"
  if [ -d "$CLONE/.git" ]; then
    git -C "$CLONE" fetch -q --depth 1 origin main && git -C "$CLONE" reset -q --hard FETCH_HEAD
  else
    git clone -q --depth 1 "$REPO_URL" "$CLONE"
  fi
  if [ $? -ne 0 ]; then echo "could not bring the clone up to main; nothing was checked"; exit 3; fi
  echo "main at $(git -C "$CLONE" log -1 --format='%h %cI')"
  cd "$CLONE" || exit 3
  python3 scripts/watch_live_posts.py --root . --report "$DIR/last-report.md" --json > "$DIR/last-result.json"
  code=$?
  echo "watch exit $code (0 nothing registered changed, 1 a registered passage changed, 2 a post could not be fetched)"
  case "$code" in 0|1|2) ;; *) echo "the check itself failed: nothing was compared"; exit "$code" ;; esac
  GH_REPO=u-dont-existDOTcom/joel-articles python3 scripts/watch_live_posts.py --issues-from "$DIR/last-result.json"
  echo "issues step exit $?"
  if [ "$code" = 1 ] && command -v notify-send >/dev/null 2>&1; then
    notify-send "joel-articles" "A passage another post depends on changed on Substack. The GitHub issue labelled depends-watch says which." || true
  fi
  echo "== done"
} >>"$LOG" 2>&1
# keep the log short: its last 3000 lines
if [ "$(wc -l < "$LOG")" -gt 3000 ]; then tail -n 3000 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"; fi
