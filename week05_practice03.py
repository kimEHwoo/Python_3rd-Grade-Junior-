def babylonian_sqrt(num, precision = 0.0001):
    x = num/2
    while True:
        new_x = (x+num/x)/2
        if abs(new_x-x)<precision:
            break
        x = new_x
    return x

def calculate_variance(data):
    n = len(data)
    mean = sum(data)/n
    
    sum_of_squares = sum((x-mean)**2 for x in data)
    variance = sum_of_squares/n
    return variance

def calculate_std_deviation(data):
    variance = calculate_variance(data)
    std_deviation = babylonian_sqrt(variance)

    return std_deviation

grades = list(map(int, input('숫자를 입력하세요: ').split()))

print()
print('===============================')
print('======파이썬 중간고사 결과======')
print('===============================')
print()

person = len(grades)
average = sum(grades)/person

variance = calculate_variance(grades)
deviation = calculate_std_deviation(grades)

print(f"전체 수강생 수는 {person}명입니다.")
print(f"평균은 {average}입니다.")
print(f"분산은 {variance:.2f}입니다.")
print(f"표준편차는 {deviation:.2f}입니다.")