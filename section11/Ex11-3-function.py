'''
파일명: Ex11-3-function.py

Return
    함수는 작업을 수행한 결과를 변환(return)할 수 있다.
    반환된 값은 함수 호출한 위치에서 사용할 수 있다.
'''
# 매개변수 없음, 리턴 값 있음
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)

# 매개변수 있음, 리턴 값 있음
def plus(num1 = 10, num2 = 0):
    return num1 + num2

result = plus(20, 30)
print(result)


