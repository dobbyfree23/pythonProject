'''
파일명: Ex22-3-InsertionSort.py

삽입정렬(Insertion Sort)
    리스트의 모든 요소를 앞에서 부터 차례대로
    이미 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입
'''


def insertion_sort(arr):
    n = len(arr)
    '''    0  1  2  3  4  5
    arr = [3, 5, 6, 1, 2, 4]
    n = 6
    i: 1 ~ 5까지 반복
    i = 1
        key = 5
        j = -1
    i = 2
        key = 3
        j = -1
        arr[1] = arr[0]
    '''

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# 실행코드
arr = [6, 5, 3, 1, 2, 4]
print(insertion_sort(arr))
