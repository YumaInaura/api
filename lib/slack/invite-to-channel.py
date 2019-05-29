#!/usr/bin/env python3

# https://api.slack.com/methods/channels.invite
# https://slack.com/api/channels.invite

import requests, os, json, sys

url = "https://slack.com/api/channels.invite"

members = json.dumps(sys.stdin.read())

for member in members:
  params = {
    "token" : os.environ.get('SLACK_TOKEN'),
    "channel" : os.environ.get('CHANNEL'),
    "user" : member.get('id'),
  }
  
  headers = {
    'Content-type': 'application/json'
  }

  res = requests.post(url, headers=headers, params=params)

  print(json.dumps(res.json()))

