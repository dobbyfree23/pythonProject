'''
Ex09-1-built-in-function.py

내장함수
    파이썬에서 제공해주는 별도의 import 없이
    사용할 수 있는 함수
'''
# 예제1 : 리스트와 관련된 내장 함수들
number = [1, -5, 2, 3, -8, 3, 9, -3, 4, 7, -1]
print('1. 합계:', sum(number))
print('2. 최대값:', max(number))
print('3. 최솟값:', min(number))
print('4-1. 정렬된 리스트', sorted(number))
print('4-2. 역정렬 리스트', sorted(number, reverse=True))
print('5-1. 절대값 맵핑:', list(map(abs, number)))   # map(적용할 함수, 반복가능한 객체)
print('5-2. 절대값 함수:', abs(number[1]))
print('6. 리스트 길이:', len(number))

# 예제2: 문자열과 관련된 내장함수들
text = "Python Programming 123"
words = ["apple", "banana", "cherry", "date"]
str_alpha = "ABC"
str_numeric = "123"
print("1-1. 문자열이 알파벳인가?:", str_alpha.isalpha())        # isalpha()
print("1-2. 문자열이 숫자인가?:", str_numeric.isnumeric())        # isalpha()
print("2. 대문자로:", text.upper())                     # upper()
print("3. 소문자로:", text.lower())                     # lower()
print("4. 문자열 분할:", text.split())                  # split()
print("5. ASCII 코드:", ord('A'))                      # ord()
print("6. ASCII to 문자:", chr(65))                    # chr()
print("7-1. 문자열 위치:", text.find("Pro"))           # find()
print("7-2. 문자열 위치:", text.index("Pro"))          # index() - 없으면 에러
print("8. 문자 개수:", text.count('P'))                # count()
print("9. 공백 제거:", text.strip())                   # strip()
print("10. 문자열 합치기:", " ".join(words))           # join()


