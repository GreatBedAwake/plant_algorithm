from remove_re_elements import A
from util import count_time


@count_time
def unique(A, new_A):
    # A_max = max(A)
    # A_min = min(A)
    # new_A = [0 for _ in range(A_max - A_min + 1)]
    for element in A:
        new_A[element] += 1
    return new_A

if __name__ == '__main__':
    A_max = max(A)
    A_min = min(A)
    new_A = [0 for _ in range(A_max - A_min + 1)]
    print(unique(A, new_A))
