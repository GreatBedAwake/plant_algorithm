from time import time


def count_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fn = 0
        fn_1 = 1
        for i in xrange(n-1):
            tmp = fn_1
            fn_1 += fn
            fn = tmp

        return fn_1

count_n = 100000000

start = time()
count_fibonacci(count_n)
end = time()
count_time = end - start
print count_time
