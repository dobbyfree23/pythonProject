'''
파일명: Ex02-1-circle.py

docstring
    파이썬 코드(모듈, 함수, 클래스 등)의
    첫 부분에 문자열("""...""")로 작성하는
    문서화 주석입니다.
'''
# 1. math 모듈포함
import math

# 2. 원의 넓이를 계산하는 함수 만들기
def get_area(radius):
    """
    원의 넓이를 계산하는 함수
    :param radius: 반지름
    :return: 원의 넓이
    """
    area = math.pi * math.pow(radius, 2)
    return area

# 3. 함수 사용해보기
radius = 1.5 # 반지름 값 저장
print('반지름:', radius)

area = get_area(radius)
print('원의 넓이:', area)

# 4. 함수 설명(docstring) 확인하기
print('함수 설명서:', get_area.__doc__)

help(get_area)














