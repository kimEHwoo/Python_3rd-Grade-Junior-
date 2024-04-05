def babylonian_sqrt(num, precision=0.0001):
    x = num
    y = 1
    while x - y > precision:
        x = (x + y) / 2
        y = num / x
    return x

def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n

    # 각 데이터 포인트와 평균 간의 편차를 제곱한 값의 평균
    sum_of_squares = sum((x - mean) ** 2 for x in data)
    variance = sum_of_squares / n

    return variance

def calculate_std_deviation(data):
    variance = calculate_variance(data)

    # 분산의 제곱근을 계산하여 표준편차를 구함
    std_deviation = babylonian_sqrt(variance)

    return std_deviation

grades = list(map(int, input("숫자를 입력하세요: ").split()))

print()
print('===============================')
print('======파이썬 중간고사 결과======')
print('===============================')
print()

person = len(grades)
average = sum(grades) / person

# 분산 계산
variance = calculate_variance(grades)
# 표준편차 계산
std_deviation = calculate_std_deviation(grades)

print(f"학생 수: {person}")
print(f"평균 성적: {average:.2f}")
print(f"분산: {variance:.4f}")
print(f"표준편차: {std_deviation:.4f}")
