# found to file or folder with isfile() and isdir()
>>> os.path.isdir('project')
True
>>> os.path.isdir('project/view.py')
False
>>> os.path.isfile('project/view.py')
True