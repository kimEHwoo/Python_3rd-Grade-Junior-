for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j}*{i}={j*i}', end='')
        if j < 9:
            print(',', end = '\t')
    print()