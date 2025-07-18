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

# 예제2: 문자열과 관련된 함수들
text = "Python Programming 123"
words = ["apple", "banana", "cherry", "date"]
print("1. ASCII 코드:", ord('A'))                      # ord()
print("2. ASCII to 문자:", chr(65))                    # chr()

# 예제 3: 수학과 관련된 내장 함수들
print("1. 반올림:", round(3.7))                        # round()
print("2. 절대값:", abs(-5))                          # abs()
print("3. 거듭제곱:", pow(2, 3))                      # pow()
