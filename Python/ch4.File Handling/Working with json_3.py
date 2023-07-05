# json files = configure files
>>> import json
>>> with open('info.json') as info:
...     data = json.load(info)
...
>>> data['address']['city']
Yasuj