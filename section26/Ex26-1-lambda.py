'''
파일명: Ex26-1-lambda.py

람다 함수란?
    람다 함수는 이름 없는 익명 함수
    단일 표현식을 사용하여 간단한 함수를 만드는 방법
    보통 일회용 함수로 사용한다.

기본문법
    lambda 인자 : 표현식

'''

# 일반함수
def add(x, y):
    return x + y

print(add(5, 3))

# 람다 함수
add = lambda x, y: x + y
print(add(5, 3))













