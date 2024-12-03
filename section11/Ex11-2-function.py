'''
파일명: Ex11-2-function.py

매개변수
    함수는 다양한 입력값(매개변수)를 받을 수 있으며,
    입력값 바탕으로 작업을 수행한다.

매개변수(parameter): 함수 정의 시 함수가 입력받는 변수
인자(Argument): 함수 호출 시 실제로 함수에 전달되는 값
'''

# 매개변수 있음, 리턴 값 없음
def introduce(name, age):
    '''
        name = '홍길동'
        age = 25
    '''
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')

introduce('홍길동', 25)


# 가변 매개변수 함수
def show(*args):
    for item in args:
        print(item)

show('PYTHON', 'JAVA', 'C++')






