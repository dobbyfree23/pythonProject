'''
파일명: Ex02-4-String.py

문자열(String, str)
    - 문자들의 순서가 있는 나열
    - 작은따옴표(') 또는 큰따옴표(")로표현
    - 문자열은 변경불가능(immutable)
'''

# 1. 문자열 생성 방법
str1 = 'Hello Python'   # 작은 따옴표
str2 = "Hello Python"   # 큰 따옴표
# 여러줄 문자열 작은 따옴표
str3 = '''Hello
Python
'''
# 여러줄 문자열 큰 따옴표
str4 = """Hello
Python
"""

# 줄복사 단축키 Ctrl + d
# 줄삭제 단축키 Ctrl + y
print(str1)
print(str2)
print(str3)
print(str4)

# 2. 문자열 인덱싱
'''
       | h | e | l | l | o | 
index    0   1   2   3   4
역순번호 -5  -4   -3  -2  -1
'''
str = 'hello'
print('1번째 문자:', str[0])
print('마지막 문자:', str[4])
print('-1번째 문자:', str[-1])

# 3. 문자열 슬라이싱
str = 'Python Programming'
print('처음부터 4글자:', str[0:4])
print('처음부터 4글자:', str[:4])
print('7번째문자부터:', str[7:])
print('마지막 5글자:', str[-5:])

# 4. 주요 문자열 메소드(함수)
str = '   P y t h o n   '
print('원본:', str)
print('공백제거:', str.strip())
print('모두 대문자:', str.upper())
print('모두 소문자:', str.lower())
print('문자 교체:', str.replace('P', 'J'))
print('문자 사이까지 공백제거:', str.replace(' ', ''))

print('   가나다라   '.strip())





