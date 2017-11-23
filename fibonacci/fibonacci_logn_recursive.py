from time import time


# return fn+1 fnf
def fibonacci(n):
    # odd
    if n > 0:
        m = n / 2
        fm_1, fm = fibonacci(m)

        if n % 2:
            fn_1 = fm_1 * (fm_1 + 2*fm)
            fn = fm_1 * fm_1 + fm * fm
        # even
        else:
            fn_1 = fm_1 * fm_1 + fm * fm
            fn = fm * (2 * fm_1 - fm)

        return fn_1, fn
    else:
        return 1, 0


def count_fibonacci(n):
    return fibonacci(n)[1]

count_n = 10000000
start = time()
count_fibonacci(count_n)
end = time()
count_time = end - start
print count_time
