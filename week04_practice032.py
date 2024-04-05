a = int(input('0보다 큰 정수를 입력하세요: '))

if a < 1:
    print('잘못된 정수 입력입니다.')
else:
    for i in range(1, a + 1):
        print(' ' * (a - i), end = '')
        print('*' * i)
    for j in range(1, a):
        print(' ' * j, end = '')
        print('*' * (a - j))