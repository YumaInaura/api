#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")

source "${base_dir}/../../setting.sh"

mkdir -p "$base_dir"/log

OLDEST=$(($(date +%s) - $((60*60*24)))) \
CHANNEL=CG1JV3ETU \
  "$api_dir"/slack/channel-message.sh | jq '.messages' \
  | tee "$base_dir"/log/slack-message.json


