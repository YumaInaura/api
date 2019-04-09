#!/usr/bin/env python3

# https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html

import json, os, sys, twitterauth

twitter = twitterauth.twitter()

input_datas = json.loads(sys.stdin.read())

api_url = 'https://api.twitter.com/1.1/statuses/update.json'

max_length = int(os.environ.get('MAX_LENGTH')) if os.environ.get('MAX_LENGTH') else 140
json_key = os.environ.get('JSON_KEY') if os.environ.get('JSON_KEY') else 'text'
results = []

for input_data in input_datas:
  message = input_data[json_key]
  message = message[0:max_length]
  params = {
    "status" : message
  }

  res = twitter.post(api_url, params=params)
  results.append(res.json())

print(json.dumps(results))

