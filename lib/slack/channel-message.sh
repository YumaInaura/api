#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")


TOKEN=$(cat ~/.secret/slack-token.txt) \
CHANNEL="$CHANNEL" \
  "$base_dir"/channel-message.py \
  | jq .messages \
  | "$base_dir"/channel-message-ext.py

