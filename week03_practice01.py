s = input('숫자를 입력하세요: ')
s = int(s)

for i in range(1, s+1):
    print(i, end = ' ')

print()
print(tuple(range(1,s+1,1)))
print(list(range(1,s+1,1)))