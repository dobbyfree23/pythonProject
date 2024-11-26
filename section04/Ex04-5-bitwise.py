'''
파일명: Ex04-5-bitwise.py

비트 연산자
    이진수의 비트 단위 연산자
    & (AND): 두 비트 모두 1일 때 1
    | (OR) : 하나라도 1이면 1
    ^ (XOR) : 두 비트가 다르면 1
    ~ (NOT) : 비트 반전
    << (Left Shift) : N칸 왼쪽 비트 이동
    >> (Right Shift) : N칸 오른쪽 비트 이동
'''
a = 6   # 0 0110
b = 5   # 0 0101
print(f'a & b: {a & b}')
print(f'a | b: {a | b}')
print(f'a ^ b: {a ^ b}')
print(f'~a: {~a}') # 0 0110 -> 1 1001

print(f'a << 1: {a << 1}')  # 0110 -> 1100
print(f'a >> 1: {a >> 1}')  # 0110 -> 0011













