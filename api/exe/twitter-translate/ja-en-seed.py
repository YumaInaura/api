#!/usr/bin/env python3

import sys, json, re, os

tweets = json.loads(sys.stdin.read())

results = []

for tweet in tweets:
  seed = {}
  seed['text'] = tweet['translated_text'][:280]
  seed['attachment_url'] = tweet['url']
  seed['in_reply_to_status_id'] = tweet['id_str']
  results.append(seed)

print(json.dumps(results))
