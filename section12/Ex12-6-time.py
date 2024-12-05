'''
파일명: Ex12-6-time.py

time 모듈
    기본적인 시간처리 기능 제공

datetime 모듈
    날짜와 시간을 더 직관적으로 다루는 기능 제공

timedelta
    datetime 모듈의 시간 연산을 위한 클래스
    날짜/시간의 차이를 계산하거나 더하고 뺄 때 사용

'''
import time
from datetime import datetime, timedelta


# time.time(): Unix timestamp 반환 (1970년 1월 1일부터의 초)
print(f'현재 timestamp: {time.time()}')
print(f'현재 시간: {time.strftime("%Y.%m.%d. %H:%M:%S")}')
print(f'현재 시간: {time.strftime("%Y년 %m월 %d일 %H:%M:%S")}')

# datetime.now(): 현재 날짜와 시간을 datetime 객체로 반환
now = datetime.now()
print(f'현재 날짜/시간: {now}')
print(f'현재 날짜/시간: {now.strftime("%Y.%m.%d. %H:%M:%S")}')
y = datetime.now().year
m = datetime.now().month
d = datetime.now().day
print(f'{y}년 {m}월 {d}일')

# timedelta
today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(f'내일: {tomorrow}, 어제: {yesterday}')

# datetime 객체간의 차이 계산
date1 = datetime(2024, 12, 5)
date2 = datetime(2025,1, 1)
diff = date2 - date1
print(f'날짜 차이: {diff.days}일')


sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)   # 1초 동안 프로그램 실행 중지
    sec += 1














