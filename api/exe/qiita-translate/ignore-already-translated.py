#!/usr/bin/env python3

import sys, json, re

seeds = json.loads(sys.stdin.read())

results = []

for seed in seeds:
#  if re.search(r'^[\w\s]+$', seed['title']):
#    continue

  results.append(seed)

print(json.dumps(results))

