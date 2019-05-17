#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")

source "${base_dir}/../../setting.sh"

mkdir -p "$base_dir"/log
mkdir -p "$base_dir"/history

OLDEST=$(($(date +%s) - $((1*60)))) \
CHANNEL=CG1JV3ETU \
  "$api_dir"/slack/channel-message.sh | jq '.messages' \
  | tee "$base_dir"/log/slack-message.json

count=$("$base_dir"/log/slack-message.json | jq length)

if [ $count -lt 0 ]; then
  cp "$base_dir"/log/slack-message.json \
      "$base_dir"/history/slack-message-"$(date +%s)".json
fi

