'''
Ex04-4-logical.py

논리 연산자
    참/거짓을 판단하는 연산자
    and: 둘 다 True일 때만 True
    or : 하나라도 True 이면 True
    not: True ↔ False 반전
'''

a = 10
b = 0
print(f'{a} > 0 and {b} > 0: {a > 0 and b > 0}')
print(f'{a} > 0 or {b} > 0: {a > 0 or b > 0}')

print(True and False)
print(True or False)

print(f'not {a}: {not a}')
print(f'not {b}: {not b}')

print(not True)
print(not False)







