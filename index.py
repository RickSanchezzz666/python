import datetime

сalls_info = []

def logger(func):
    def wrapper(*args, **kwargs):
        call_time = datetime.datetime.now()
        try:
            result = func(*args, **kwargs)
            info = (call_time, func.__name__, args, kwargs, 'Success', result)
        except Exception as err:
            info = (call_time, func.__name__, args, kwargs, 'Error', str(err))

        сalls_info.append(info)

        return info
    return wrapper

def file_sync(log):
    with open('log.txt', 'a') as file:
        file.write(str(log) + '\n')
        print(log)

def clear_log():
    with open('log.txt', 'w') as file:
        file.write('')

def get_logs():
    for call in сalls_info:
        yield call

clear_log()

@logger
def func(arg1, arg2):
    return f'{arg1} is not {arg2}'

func('sb', 'bones')
func('ghoste', 'fucker')
func('nigga', 'what', 2132)

logs = get_logs()

file_sync(next(logs))

file_sync(next(logs))

file_sync(next(logs))


