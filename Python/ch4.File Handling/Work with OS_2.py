>>> os.mkdir('images/other')
>>> os.mkdir('images/other/2019')
>>> os.listdir('images/other')
['2019']
>>> os.rmdir('images/other')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [WinError 145] The directory is not empty:
'/home/ali/Desktop/python/os_sample/images/other'
>>> os.rmdir('images/other/2019')
>>> os.listdir('images/other')
[]