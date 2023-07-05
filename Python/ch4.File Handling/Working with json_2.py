# dumps function in json for convert python structure to json
>>> import json
>>> json.dumps([1, 2, 3])
'[1, 2, 3]'
>>> json.dumps({"key": 2, "list": [12, 'ali']})
'{"key": 2, "list": [12, "ali"]}'
>>> json.dumps([{"key": "value"}])
'[{"key": "value"}]'
>>> json.dumps(2)
'2'