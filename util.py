from functools import wraps
import time


def count_time(function):
    @wraps(function)
    def wrappers(*args, **kwargs):
        time_start = time.process_time()
        response = function(*args, **kwargs)
        time_end = time.process_time()
        print('use time {}'.format(time_end - time_start))
        return response
    return wrappers