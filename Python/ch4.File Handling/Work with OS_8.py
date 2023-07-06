>>> os.sep
'/'
>>> '../main/images'.split(os.sep)
['..', 'main', 'images']
>>> os.path.basename('project/control.py')
'control.py'
>>> os.path.basename('../images/animal/cat.jpg')
'cat.jpg'
>>> os.path.basename('../main/images')
'images'