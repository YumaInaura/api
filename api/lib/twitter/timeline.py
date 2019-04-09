#!/usr/bin/env python3

# https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html

import json, config, os, re
import time
import datetime
import twitterauth
from datetime import timedelta

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
last_id = ''

include_rts =     True if (os.environ.get('INCLUDE_RTS') or os.environ.get('ALL') ) else False
include_replies = True if (os.environ.get('INCLUDE_REPLIES') or os.environ.get('ONLY_REPLIES') or os.environ.get('ALL')) else False

round = int(os.environ.get('ROUND')) if os.environ.get('ROUND') else 3
count = int(os.environ.get('COUNT')) if os.environ.get('COUNT') else 200

def response(max_id):
  api_params = {
    'trim_user' : True,
    'exclude_replies' : not(include_replies),
    'tweet_mode' : 'extended',
    'count' : count,
		'include_rts' : include_rts,
  }
  
  if max_id:
    api_params['max_id'] = max_id

  if os.environ.get('COUNT'):
    api_params['count'] = os.environ.get('COUNT')

  res = twitter.get(url, params = api_params)
  
  if res.status_code != 200:  
      print("Failed: %d" % res.status_code)
      exit()

  return res

results = []

for i in range(0, round):
  res = response(last_id)

  timelines = json.loads(res.text)
  last_id = timelines[-1]['id']

  if i >= 2:
    timelines.pop()

  results += timelines

results.reverse()

print(json.dumps(results))

