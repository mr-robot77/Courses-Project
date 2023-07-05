# loads function in json for convert json data to python structure
>>> import json
>>> info = json.loads(data)
>>> info['address']
{'city': 'Yasuj', 'village': 'Karim-Abad'}
>>> info['isAlive']
True
>>> json.loads('2')
2
>>> json.loads('{"people": ["ali", "mamad", "reza"]}')
{'people': ['ali', 'mamad', 'reza']}