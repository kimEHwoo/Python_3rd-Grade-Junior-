# # def format_number(num):

# def format_number(num):
#     return str(num).rjust(3)

# def print_pattern(n):
#     matrix = [[0] * n for _ in range(n)]
#     num = 1

#     for i in range(n):
#         if i % 2 == 0:  # 짝수 번째 행
#             matrix[i] = [format_number(x) for x in range(num, num + n)]
#         else:  # 홀수 번째 행
#             matrix[i] = [format_number(x) for x in range(num, num + n)][::-1]
#         num += n

#     for row in matrix:
#         print(*row)

# # 사용자 입력 받기
# n = int(input("자연수를 입력하세요: "))
# print_pattern(n)

# a = [1,2,3,5]
# a.sort(reverse=True)
# print(a)

a = int(input("자연수를 입력하세요: "))

a_list = [i for i in range(1, a**2+1)]

for i in range(0, a):
    if i % 2 == 0:  # 홀수 열
        print(*(f"{num:3}" for num in a_list[a*i:a*(i+1)]))
    else:  # 짝수 열
        a_rev = a_list[a*i:a*(i+1)]
        a_rev.reverse()
        print(*(f"{num:3}" for num in a_rev))
