>>> os.rename('test.py', 'model.py')
>>> os.listdir()
['project', 'model.py', 'main.py']
>>> os.rename('model.py', 'project/model.py')
>>> os.listdir()
['project', 'main.py']
>>> os.rename('main.py', 'project/a.py')
>>> os.listdir()
['project']
>>> os.listdir('project')
['control.py', 'a.py', 'view.py', 'model.py']
>>> os.system('python codes/main.py')