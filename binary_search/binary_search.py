import math


def binary_search(A, key):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = math.floor((l + r) / 2)
        if A[m] == key:
            return m
        elif A[m] < key:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':
    A = [1, 3, 5, 6, 7, 9]
    print(binary_search(A, 8))
