#!/usr/bin/env python3

import requests, os, json, sys, re

messages = json.loads(sys.stdin.read())

TOKEN = os.environ.get('TOKEN')

results = []

for message in messages:
  ext = {}

  message['ext'] = ext

  if message.get('files'):
      for file in message.get('files'):
        if file.get('is_external'):
          continue

        file_id = file['id']
        share_api_url ='https://slack.com/api/files.sharedPublicURL?token=' + TOKEN + '&file=' + file_id + '&pretty=1'
        requests.get(share_api_url)
    
  results.append(message)

print(json.dumps(results))

