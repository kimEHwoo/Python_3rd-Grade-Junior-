print("================================")

a,b,c = map(int, input("점수를 입력하세요: ").split())

mean = (a+b+c)/3
var = ((a-mean)**2+(b-mean)**2+(c-mean)**2)/3
std = var**(1/2)


print()
print("================================")
print("====== 파이썬 중간고사 결과 ======")
print("================================")
print("전체 수강생 수:", 3)
print("평균:", mean)
print("분산:", var)
print("표준편차:",std)