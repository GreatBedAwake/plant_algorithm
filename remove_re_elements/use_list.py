from remove_re_elements import A
from util import count_time


@count_time
def unique(A):
    new_A = []
    for element in A:
        status = True
        for new_element in new_A:
            if new_element == element:
                status = False
                break
        if status:
            new_A.append(element)
    return new_A

if __name__ == '__main__':
     print(unique(A))
