import json, os, sys, re

timelines = sys.stdin

results = []

def format(text):
    text = re.sub(r'https://t\.co/\w+', '' ,line['full_text'])
    text = re.sub(r'#', '' , text)

    text = '# ' + text
    if 'media' in line['entities'].keys():
      for media in line['entities']['media']:
        text += "\n"
        text += "![image]("+media['media_url_https']+')'
    text += "\n"

    if 'quoted_status' in line:
      text += "\n>" + line['quoted_status']['full_text'] + "\n"

    # text += "\n" + '<a href="https://twitter.com/YumaInaura/status/' + str(line['id']) + '">' + line['created_at'] + '</a>'
    text += "\n" + '<a href="https://twitter.com/YumaInaura/status/' + str(line['id']) + '">' + 'Tweet'  + '</a>'

    return(text)

for line in timelines:
    line = json.loads(line)

    if line['full_text'].find('RT') >= 0:
      continue

    results.append(format(line['full_text']))

results.reverse()

for result in results:
  print(result)

