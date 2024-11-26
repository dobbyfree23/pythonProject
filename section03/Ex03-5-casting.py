'''
파일명: Ex03-5-casting.py

형변환(casting)
    변수에 유형을 지정하려는 경우 형변환으로 가능.
    주요 함수: int(), float(), str(), list(), tuple()
'''
# 1. 정수 형변환
str_num1 = '15'
str_num2 = '20'

result = str_num1 + str_num2
print(f'결과: {result}')
result = int(str_num1) + int(str_num2)
print(f'형변환 후 결과: {result}')

# 2. 실수 형변환
x = float('1.52654')
y = float(3)
print(x)
print(y)

z = int(3.141592)
print(z)

# 3. 문자 형변환
strX = str(1)
strY = str(2)
result = strX + strY
print(result)

# 4. 아스키코드 변환
a = ord('A')
print(a)
b = chr(65)
print(b)



'''
주의사항:
부적절한 형변환 시도 시 ValueError 발생
    int('3.14')
    int('ABC')
'''


















