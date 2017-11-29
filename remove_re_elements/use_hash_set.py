from remove_re_elements import A
from util import count_time


@count_time
def unique(A):
    new_A = set()
    for element in A:
        if element not in new_A:
            new_A.add(element)
    return new_A

if __name__ == '__main__':
    print(unique(A))
