import random
from util import count_time


@count_time
def insertion_sort(A):
    len_A = len(A)
    for i in range(1, len_A):
        j = find_postion(A, i)
        move_list(A, j, i)


def find_postion(A, i):
    tmp = A[i]
    while i > 0:
        if A[i-1] <= tmp:
            return i
        i -= 1
    return 0


def move_list(A, j, i):
    tmp = A[i]
    while i > j:
        A[i] = A[i-1]
        i -= 1
    A[j] = tmp

if __name__ == '__main__':
    A = []
    for i in range(10000):
        A.append(random.randint(0, 10000))
    # A = [4, 2, 7, 4, 6, 1, 34]
    insertion_sort(A)
    print(A)
