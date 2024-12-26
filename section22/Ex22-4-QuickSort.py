'''
파일명: Ex22-4-QuickSort.py

퀵 정렬(Quick Sort)
    분할 정복 알고리즘, 기준점(pivot)을 설정하고
    pivot 보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할한 후
    각 부분 리스트에 대해 재귀적으로 퀵정렬을 수행하는 알고리즘
'''

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    '''
    arr = [6, 5, 3, 1, 2, 4]
    pivot = 6
    left = [5, 3, 1, 2, 4]
    right = []
    equal = [6]
    quick_sort(left) -> [1, 2, 3, 4, 5]
        arr = [5, 3, 1, 2, 4]
        pivot = 5
        left = [3, 1, 2 ,4]
        right = []
        equal = [5]
        quick_sort(left)    -> [1, 2, 3, 4]
            arr = [3, 1, 2 ,4]
            pivot = 3
            left = [1, 2]
            right = [4]
            equal = [3]
            quick_sort(left)    -> [1, 2]
                arr = [1, 2]
                pivot = 1
                left = []
                right = [2]
                equal = [1]
                quick_sort(left) -> []                  
                quick_sort(right) -> [2]
                quick_sort(left) + equal + quick_sort(right) -> [] + [1] + [2] -> [1, 2]
            quick_sort(right) -> [4]
                arr = [4]
            quick_sort(left) + equal + quick_sort(right) -> [1,2] + [3] + [4] -> [1, 2, 3, 4]
        quick_sort(right) -> []
        quick_sort(left) + equal + quick_sort(right) ->   [1, 2, 3, 4] + [5] + [] -> [1, 2, 3, 4, 5] 
        
    
    '''
    pivot = arr[0]
    left, right, equal = [], [], []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)

    return quick_sort(left) + equal + quick_sort(right)

# 실행코드
arr = [6, 5, 3, 1, 2, 4]
print(quick_sort(arr))












