#!/usr/bin/env bash

base_dir=$(dirname "$0")

log_dir="$base_dir"/log
 
mkdir -p "$log_dir"

cat /dev/stdin \
  | "${base_dir}"/markdown-to-html.py \
  > "$log_dir"/en-seed-html.json

cat "$log_dir"/en-seed-html.json \
  | \
    TOKEN=$("$base_dir"/get-token.sh) \
    TRANSLATE_JSON_KEY=text \
    FORMAT=html \
    FROM=ja \
    TO=en \
      "$base_dir"/translate-json.py \
  > "$log_dir"/en-translated-html.json

cat "$log_dir"/en-translated-html.json \
  | "${base_dir}"/html-to-markdown.py \
  | tee "$log_dir"/en-translated-markdown.json

