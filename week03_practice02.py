a, b = map(int, input('숫자를 입력하세요: ').split())

print("AND  연산 결과: ",bool(a and b))
print("OR   연산 결과: ",bool(a or b))
print("NAND 연산 결과: ",bool(not(a and b)))
print("NOR  연산 결과: ",bool(not(a or b)))
print("XOR  연산 결과: ",bool((a and not b) or (not a and b)))