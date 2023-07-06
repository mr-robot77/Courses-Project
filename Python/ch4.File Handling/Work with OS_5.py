>>> w = os.walk('.')
>>> type(w)
<class 'generator'>
>>> list(w)
[('.', ['project'], ['main.py']), ('./project', [], ['control.py', 'a.py', 'view.py', 'model.py'])]
>>> list(os.walk('..'))
[('..', ['codes', 'data', 'images'], ['README.md']), ('../codes', ['project'], ['main.py']), ('../codes/project', [], ['control.py', 'a.py', 'view.py', 'model.py']), ('../data', [], ['secrets.txt', 'python.txt']), ('../images', ['animal'], []), ('../images/animal', [], ['ant.jpg', 'dog.png', 'cat.jpg'])]