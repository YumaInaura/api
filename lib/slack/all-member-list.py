#!/usr/bin/env python3

# https://api.slack.com/methods/users.list

import requests, os, json

url = "https://slack.com/api/users.list"

params = {
  "token" : os.environ.get('SLACK_TOKEN'),
}

headers = {
  'Content-type': 'application/json'
}

res = requests.get(url, headers=headers, params=params)

print(json.dumps(res.json()))

