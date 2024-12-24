'''
파일명: Ex20-6-O(2^n).py

O(2^n)
    지수 시간 복잡도, 피보나치 수열처럼 재귀적 알고리즘

'''

'''

fibonacci(3)    -> 1 + 1 => 2
    fibonacci(2) -> 1 + 0 -> 1 
        fibonacci(1) -> 1
            return 1
        fibonacci(0) -> 0
            return 0
     fibonacci(1) -> 1
            return 1
        
'''

def fibonacci(n):
    print(n)
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))