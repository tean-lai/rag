#!/usr/bin/env bash
set -euo pipefail

SRC_DIR="artifact"
DST_DIR="artifact2"
PATTERN='query|encode|search'

mkdir -p "$DST_DIR"

# Find all regular files under artifact/, preserve subdirs into artifact2/
find "$SRC_DIR" -type f -print0 | while IFS= read -r -d '' file; do
  rel="${file#$SRC_DIR/}"
  out="$DST_DIR/$rel"

  mkdir -p "$(dirname "$out")"

  # Grep matching lines (case-sensitive). If no matches, write an empty file.
  # -- ensures filenames beginning with '-' are treated as files.
  if grep -nE -- "$PATTERN" "$file" > "$out" 2>/dev/null; then
    : # matches found and written
  else
    : > "$out" # create/empty output file
  fi
done
