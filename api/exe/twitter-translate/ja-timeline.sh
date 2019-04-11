#!/usr/bin/env bash

set -eu

basedir=$(dirname "$0")
source "${basedir}/../../setting.sh"

mkdir -p "$log_dir"

source ~/.secret/env/twitter-yumainaura

ALL=1 ROUND=1 \
  "$api_dir"/twitter/timeline.py \
  | TWITTER_USER_NAME=YumaInaura "$api_dir"/twitter/timeline-add-ext.py \
  > "$log_dir"/ja-timeline.json
