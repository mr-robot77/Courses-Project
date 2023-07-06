>>> os.path.commonprefix(['project/test.py', 'project/main.py'])
'project/'
>>> os.path.commonprefix(['project/data/test.py', 'project/data/main.py'])
'project/data/'
>>> os.path.commonprefix(['project/data/test.py', '../main.py'])
''
>>> os.path.commonprefix(['project/data','modules/data'])
''