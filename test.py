print('세 정수의 최댓값을 구합니다.')

a = int(input('정수 a의 값을 입력 : '))
b = int(input('정수 b의 값을 입력 : '))
c = int(input('정수 c의 값을 입력 : '))

maximum = a
if b> maximum:
    maximum = b
if c> maximum:
    maximum = c

print(f'최대값은 {maximum}입니다.')