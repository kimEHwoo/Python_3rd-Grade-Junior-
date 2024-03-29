s = int(input("정수를 입력하세요: "))

def is_prime_number(x):
    for i in range(2, x):
        if x%i ==0:
            return False
    return True

for i in range(2, s):
    if is_prime_number(i) == True:
        print(i, end = ' ')