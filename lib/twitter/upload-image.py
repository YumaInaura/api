#!/usr/bin/env python3

# source ~/.secret/env/twitter-yumainaura && echo '[{"ext":{"files":[{"url":"https://dummyimage.com/600x400/000/fff"}]}}]' | ./upload-image.py

import json, config, os, re, twitterauth, sys, requests, base64, pdb

atomic_json = sys.stdin.readlines()[0]
lines = json.loads(atomic_json)

sys.stdin = open('/dev/tty')

twitter = twitterauth.twitter()

media_api_url = 'https://upload.twitter.com/1.1/media/upload.json'

results = []

for line in lines:
  files_ext = []

  for file_data in line.get('ext').get('files'):
    if file_data.get('url') and not file_data.get('base64'):
      url = file_data.get('url')
      image_bytes = base64.b64encode(requests.get(url).content)
      file_data['base64'] = str(image_bytes.decode('utf-8'))
 
    if file_data.get('base64'):
       media_api_params = {
         "media_data": file_data.get('base64')
       }

       media_api_res = twitter.post(media_api_url, params = media_api_params)
       file_data['media_id_string'] = media_api_res.json().get('media_id_string')

    files_ext.append(file_data)

  line['ext']['files'] = files_ext

  results.append(line)

print(json.dumps(lines))


