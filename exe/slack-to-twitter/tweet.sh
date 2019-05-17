#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")

source "${base_dir}/../../setting.sh"

count=$(cat "$base_dir"/log/slack-message.json | jq length)

cat "$base_dir"/log/slack-message.json

if [ $count -lt 1 ]; then
  echo "No slack messages"
  exit
fi

source ~/.secret/env/twitter-yumainaura

cat "$base_dir"/log/slack-message.json \
  | JSON_KEY=text \
    "$api_dir"/twitter/create.py \
  | tee "$base_dir"/log/created-tweets.json

