#!/usr/bin/env python3

import requests, os, json, sys, re

messages = json.loads(sys.stdin.read())

results = []

for message in messages:
  ext = {
    'files' : [],
  }

  for file in message.get('files', []):
    public_file_path = re.sub(r'https://slack-files.com/(\w+)-(\w+)-(\w+)', \
       "https://files.slack.com/files-pri/\\1-{name}\\2/?pub_secret=\\3".format(**file), \
       file.get('permalink_public'))

    ext['files'].append({ "url_public" : public_file_path })

  message['ext'] = ext

  results.append(message)

print(json.dumps(results))

