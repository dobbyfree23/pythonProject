'''
파일명: Ex02-9-mutable-immutable.py

데이터 타입의 가변성
    mutable: 객체 생성 후 내용 변경 가능
             값 변경 시 메모리 주소 유지
            ex) list, set, dict
    immutable: 객체 생성 후 내용 변경 불가
            값 변경 시 새 메모리 주소 할당
            ex) int, str, tuple 등
'''

# 1. mutable 예제
pokemon = ['피카츄', '파이리', '꼬부기']
print(pokemon)
print('메모리 주소:', id(pokemon))

pokemon[1] = '잠만보'
print('변경 후:', pokemon)
print('메모리 주소:', id(pokemon))


print()

# 2. immutable 예제
level = 25
print('level:', level)
print('메모리 주소:', id(level))

level = level + 1
print('level+1:', level)
print('메모리 주소:', id(level))

age = 25
print('age:', age)
print('메모리 주소:', id(age))

'''
리터럴(Literal) - 소스코드에 고정된 값 
ex)
25  # 정수 리터럴
3.14 # 실수 리터럴

"홍길동" # 문자열 리터럴
True  # 부울 리터럴

'''
print('25 메모리주소:',id(25))

tuple1 = ('파이썬', '자바', 'C++')
print('tuple1:', tuple1)
print('메모리 주소:', id(tuple1))

tuple1 = ('러스트', 'go', 'React')
print('tuple1:', tuple1)
print('메모리 주소:', id(tuple1))



































