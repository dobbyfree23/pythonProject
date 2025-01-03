'''
파일명: Ex26-2-lambda.py
'''

# 람다 함수와 함께 사용하는 함수
# map() 함수 - 맵은 리스트나 튜플 같은 순회 가능한 데이터구조 모든요소에 함수적용
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, numbers))
print(result)

# filter() 함수 - 요소들을 특정 조건으로 걸러내는 함수
numbers = [1, 2, 3, 4, 5]
filter_result = list(filter(lambda x: x % 2 == 0, numbers))
print(filter_result)










