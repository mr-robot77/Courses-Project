class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    transformed_errors = []
    
    for func in func_ls:
        try:
            func()
            transformed_errors.append(ExceptionProxy("ok!", func))
        except Exception as e:
            transformed_errors.append(ExceptionProxy(str(e), func))
            
    return transformed_errors

def f():
    1/0

def g():
    pass

tr_ls = transform_exceptions([f, g])

for tr in tr_ls:
    print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)