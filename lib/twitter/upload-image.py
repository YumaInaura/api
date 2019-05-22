#!/usr/bin/env python3

import json, config, os, re, twitterauth, sys, requests, base64, pdb

lines = json.loads(sys.stdin.read())

twitter = twitterauth.twitter()

media_api_url = 'https://upload.twitter.com/1.1/media/upload.json'

results = []

for line in lines:
  files_ext = []

  for file_data in line.get('ext').get('files'):
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


