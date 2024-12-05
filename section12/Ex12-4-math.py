'''
파일명: Ex12-4-math.py

표준모듈
    파이썬에서 기본적으로 설치되어 있는 모듈

math - 수학 관련 모듈
'''

import math

# 원주율
print(math.pi)

# 올림
print(math.ceil(1.1))

# 내림
print(math.floor(1.9))

# 반올림 - math에 없고 내장함수로 가능
# 첫번째 인자 - 반올림할 숫자
# 두번째 인자 - 반올림할 소수점자리수 (기본값 0)
print(round(3.141592, 2))

# 정수로 절삭
print(math.trunc(1.9))

# 제곱근
print(math.sqrt(25))

# 제곱
print(math.pow(2, 3))













