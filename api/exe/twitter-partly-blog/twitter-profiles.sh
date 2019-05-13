#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")

source "${base_dir}/../../setting.sh"
source "${base_dir}/../twitter-setting.sh"

rm -f "$log_dir"/all-user-profiles-"$TWITTER_JA_USER_NAME".md

cat "$log_dir"/recent-"$TWITTER_JA_USER_NAME".json \
  | jq '[.[] | select(.quoted_status.entities.user_mentions)]' \
  | jq -r '.[].quoted_status.entities.user_mentions[].screen_name' \
  | sort \
  | uniq \
  > "$log_dir"/quoted-user-screen-names-"$TWITTER_JA_USER_NAME".txt

for display_name in "$TWITTER_JA_USER_NAME" $(cat "$log_dir"/quoted-user-screen-names-"$TWITTER_JA_USER_NAME".txt); do
  "$api_dir"/twitter/user-show.sh "$display_name" \
  | "$api_dir"/twitter/markdown-user.py \
  >> "$log_dir"/all-user-profiles-"$TWITTER_JA_USER_NAME".md
done

if [ -f "$log_dir"/all-user-profiles-"$TWITTER_JA_USER_NAME".md  ]; then
  cat "${log_dir}/github-issue-body-"$TWITTER_JA_USER_NAME".md" \
    "$log_dir"/all-user-profiles-"$TWITTER_JA_USER_NAME".md \
    > "${log_dir}/github-issue-body-all-"$TWITTER_JA_USER_NAME".md"
else
  cp "${log_dir}/github-issue-body-"$TWITTER_JA_USER_NAME".md" \
     "${log_dir}/github-issue-body-all-"$TWITTER_JA_USER_NAME".md"
fi

cat "${log_dir}/github-issue-body-all-"$TWITTER_JA_USER_NAME".md"
