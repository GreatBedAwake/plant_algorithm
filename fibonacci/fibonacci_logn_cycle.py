from time import time


def count_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        count_list = []
        while n > 0:
            if n % 2:
                count_list.append(1)
            else:
                count_list.append(0)
            n = int(n / 2)
        count_list.reverse()
        fn_1 = 1
        fn = 0
        for num in count_list:
            if num:
                tn_1 = fn_1 * (fn_1 + 2 * fn)
                tn = fn_1 * fn_1 + fn * fn
            else:
                tn_1 = fn_1 * fn_1 + fn * fn
                tn = fn * (2 * fn_1 - fn)

            fn_1 = tn_1
            fn = tn
        return fn


count_n = 10000
start = time()
print(count_fibonacci(count_n))
end = time()
count_time = end - start
print(count_time)
