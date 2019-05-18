#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")

source "${base_dir}/../../setting.sh"

mkdir -p "$base_dir"/log
mkdir -p "$base_dir"/history

channel=${CHANNEL:-CG1JV3ETU}

interval_minute=${INTERVAL:-1}
OLDEST=$(($(date +%s) - $(($interval_minute*60)))) \
CHANNEL=$channel \
  "$api_dir"/slack/channel-message.sh \
     TOKEN=$(cat ~/.secret/slack-token.txt) \
       "$api_dir"/slack/channel-message-public-image-publish.py \
  | tee "$base_dir"/log/slack-message.json

count=$(cat "$base_dir"/log/slack-message.json | jq length)

if [ $count -lt 0 ]; then
  cp "$base_dir"/log/slack-message.json \
      "$base_dir"/history/slack-message-"$(date +%s)".json
fi

