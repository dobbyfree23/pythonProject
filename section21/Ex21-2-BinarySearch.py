'''
파일명: Ex21-2-BinarySearch.py

이진검색(Binary Search)
    데이터가 정렬되어 있는 상태에서 사용가능한 알고리즘
    중앙값과 비교하여 탐색 범위를 반으로 줄여가며 찾는 탐색 알고리즘

'''


def binary_search(arr, x):

    low = 0
    high = len(arr) - 1

    '''        0  1  2  3  4  5   6  7   8
        arr = [1, 3, 5, 7, 8, 9, 10, 11, 21]
        x = 11
        low = 7
        high = 8
        mid = 7
    '''

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

# 실행코드
arr = [1, 10, 5, 7, 8, 9, 3, 11, 21]
arr = sorted(arr)
print(arr)
print(binary_search(arr, 11))