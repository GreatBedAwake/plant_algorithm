from functools import wraps
import time


def count_time(function):
    @wraps(function)
    def wrappers(*args, **kwargs):
        time_start = time.process_time()
        print('Start Time {}'.format(time_start))
        response = function(*args, **kwargs)
        time_end = time.process_time()
        print('End Time {}'.format(time_end))
        print('Use time {}'.format(time_end - time_start))
        return response
    return wrappers

s = 1
def h():
    print(s)

if __name__ == '__main__':
    h()