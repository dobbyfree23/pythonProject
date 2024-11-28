'''
파일명: Ex07-1-for.py

for문
    반복 횟수가 명확하거나 시퀀스(문자열, 리스트 등)
    요소를 순차적으로 처리할 때 사용하는 반복문

    초기값, 조건식, 증감식을 별도로 지정할 필요 없어
    while문 보다 간편함

    파이썬에서 가장많이 사용되는 반복문

문법:
    for 변수 in 반복가능한객체:
        반복 수행할 코드
'''

# 1. 리스트를 사용한 반복
fruits = ['사과', '바나나', '딸기', '오렌지']
for fruit in fruits:
    '''
    1번째 반복 
    fruit = fruits[0]
    2번째 반복
    fruit = fruits[1]
    3번째 반복
    fruit = fruits[2]
    4번째 반복
    fruit = fruits[3]
     
    print(fruit, end=' ') => 사과 바나나 딸기 오렌지
    '''
    print(fruit, end=' ')
print()










