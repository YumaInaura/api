#!/usr/bin/env python3

import requests, os, json, sys, re, base64

messages = json.loads(sys.stdin.read())

results = []

for message in messages:
  ext = {
    'files' : [],
  }

  for file in message.get('files', []):
    public_file_path = re.sub(r'https://slack-files.com/(\w+)-(\w+)-(\w+)', \
       "https://files.slack.com/files-pri/\\1-\\2/{name}?pub_secret=\\3".format(**file), \
       file.get('permalink_public'))

    if os.getenv('URL_TO_BASE64'):
      public_file_base64 = base64.b64encode(requests.get(public_file_path).content).decode()
  
      ext['files'].append({
        "url_public" : public_file_path,
        "base64" : public_file_base64,
      })

  message['ext'] = ext

  results.append(message)

print(json.dumps(results))

