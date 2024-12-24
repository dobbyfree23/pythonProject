'''
파일명: Ex22-1-BubbleSort.py

버블정렬(Bubble Sort)
    인접한 두 원소를 비교하여 정려하는 알고리즘
    가장 간단한 정렬 알고리즘

    시간복잡도 O(n^2)
'''

def bubble_sort(arr):
    '''    0  1  2  3  4  5
    arr = [1, 2, 3, 4, 5, 6]
    n = 6
    i : 0 ~ 5까지 반복
    i = 0
        j: range(5) -> 0 ~ 4까지 반복
        j = 0
        조건: arr[0] > arr[1]
        j = 1
        조건: arr[1] > arr[2]
        j = 2
        조건: arr[2] > arr[3]
        j = 3
        조건: arr[3] > arr[4]
        j = 4
        조건: arr[4] > arr[5]
    i = 1
        j: range(4) -> 0 ~ 3까지 반복
        j = 0
        조건: arr[0] > arr[1]
        j = 1
        조건: arr[1] > arr[2]
        j = 2
        조건: arr[2] > arr[3]
        j = 3
        조건: arr[3] > arr[4]
    i = 2
        j: range(3) -> 0 ~ 2까지 반복
        j = 0
        조건: arr[0] > arr[1]
        j = 1
        조건: arr[1] > arr[2]
        j = 2
        조건: arr[2] > arr[3]

    i = 3
        j: range(2) -> 0 ~ 1까지 반복
        j = 0
        조건: arr[0] > arr[1]
        j = 1
        조건: arr[1] > arr[2]

    i = 4
        j: range(1) -> 0
        j = 0
        조건: arr[0] > arr[1]
    i = 5
        j: range(0)

    '''
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# 실행코드
arr = [6, 5, 3, 1, 2, 4]
print(bubble_sort(arr))















