from remove_re_elements import A
from util import count_time


@count_time
def unique(A):
    len_A = len(A)
    if not len_A:
        return A
    A.sort()
    left = 0
    right = 0
    new_A = []
    while right < len_A:
        if A[left] != A[right]:
            new_A.append(A[left])
            left = right
        right += 1
    new_A.append(A[left])
    return new_A
if __name__ == '__main__':
    print(unique(A))
