def bubblesort(arr):
    length = len(arr)-1
    for i in range(length):
        for j in range(length-i):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


stack = [i for i in range(1, 6)]

while True:
    n = int(input('숫자를 입력하세요: '))

    if n == 0:
        print('프로그램 종료')
        break
    else:
        stack.append(n)
        stack = bubblesort(stack)  # 정렬된 배열을 다시 stack에 할당
        stack.pop(0)
        print(stack)