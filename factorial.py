import math
def factorial(n : int )-> int:
    if n>0:
        return n * factorial(n-1)
    else:
        return 1


if __name__ == '__main__':
    n = int(input('출력할 팩토리얼값'))
    print(f'{n}의 팩토리얼값 {factorial(n)}')
    print(math.factorial(n))