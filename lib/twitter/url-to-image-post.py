#!/usr/bin/env python3

import json, config, os, re, twitterauth, sys, requests, base64

url = sys.argv[1]

twitter = twitterauth.twitter()

image_bytes = base64.b64encode(requests.get(url).content)
image_base64_str = image_bytes.decode('utf-8')

media_api_params = {
  "media_data": image_base64_str
}

media_api_url = 'https://upload.twitter.com/1.1/media/upload.json'
media_api_res = twitter.post(media_api_url, params = media_api_params)

media_id_string = media_api_res.json().get('media_id_string')



update_api_params = {
  "status" : "test message",
  "media_ids" : media_id_string,
}

update_api_url = 'https://api.twitter.com/1.1/statuses/update.json'

update_api_res = twitter.post(update_api_url, params = update_api_params)


print(json.dumps(media_api_res.json()))


