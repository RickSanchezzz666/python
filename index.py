import datetime

сalls_info = []

def logger(func):
    def wrapper(*args, **kwargs):
        call_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        
        info = (call_time, func.__name__, args, kwargs, result)
        сalls_info.append(info)

        return info
    return wrapper

def get_logs():
    for call in сalls_info:
        yield call


@logger
def func(arg1, arg2):
    return f'{arg1} is not {arg2}'

func('sb', 'bones')
func('ghoste', 'fucker')

logs = get_logs()

print(next(logs))

print(next(logs))

