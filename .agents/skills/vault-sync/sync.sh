#!/usr/bin/env bash
# vault-sync: pull-rebase the vault, push only changes under the drop folder.
# Refuses to run if there are modifications outside 00-inbox/cluster/.
#
# Exit codes:
#   0  success (pulled; pushed if drops existed)
#   1  setup error (not a git repo, etc.)
#   2  refused — edits outside the drop folder
#   3  git operation failed (pull conflict, push rejected, etc.)

set -euo pipefail

VAULT_DIR="${VAULT_DIR:-$HOME/vault}"
DROP_PREFIX="00-inbox/cluster/"

if [ ! -d "$VAULT_DIR/.git" ]; then
  echo "vault-sync: $VAULT_DIR is not a git repo" >&2
  exit 1
fi

cd "$VAULT_DIR"

# 1. Boundary check. Any tracked or untracked change outside the drop folder
#    is a refuse condition. Run before pulling so we don't muddy state.
out_of_bounds="$(
  git status --porcelain |
    awk '{
      # porcelain: "XY path" or "XY old -> new" for renames.
      # Take the last whitespace-separated field.
      print $NF
    }' |
    grep -v "^${DROP_PREFIX}" || true
)"
if [ -n "$out_of_bounds" ]; then
  echo "vault-sync: refusing — edits outside ${DROP_PREFIX}:" >&2
  echo "$out_of_bounds" >&2
  exit 2
fi

# 2. Pull with autostash so any in-progress drop-folder edits survive the rebase.
if ! git fetch --quiet; then
  echo "vault-sync: git fetch failed" >&2
  exit 3
fi
if ! git pull --rebase --autostash --quiet; then
  echo "vault-sync: git pull --rebase failed (likely conflict in drop folder)" >&2
  exit 3
fi

# 3. Stage only drop-folder paths.
git add -- "$DROP_PREFIX"

# 4. Commit + push if anything is staged. Otherwise we are pull-only this run.
if git diff --cached --quiet; then
  echo "vault-sync: pulled; no local drops to push"
  exit 0
fi

host="$(hostname -s)"
ts="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
if ! git commit --quiet -m "cluster drop: ${host} ${ts}"; then
  echo "vault-sync: git commit failed" >&2
  exit 3
fi
if ! git push --quiet; then
  echo "vault-sync: git push failed" >&2
  exit 3
fi
echo "vault-sync: pushed cluster drop (${host} ${ts})"
