from itertools import product


numbers = [1,2,3,4,5]


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    s = list(map(sum, product(*l)))
    print()
    return s.count(target)
