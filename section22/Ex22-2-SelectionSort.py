'''
파일명: Ex22-2-SelectionSort.py

선택정렬(Selection Sort)
    주어진 리스트에서 최소값을 찾아
    맨 앞에 있는 값과 교체하는 알고리즘
'''
# 선택 정렬 알고리즘
def selection_sort(arr):
    '''
       idx 0  1  2  3  4
    arr = [1, 2, 3, 4, 5]
    len(arr) : 5
    i = 0 ~ 4
    '''

    for i in range(len(arr)):

        '''
        i = 4
        min_idx = 4
        j 는 4 까지
        j = 4

        arr[4] < arr[3]

        arr[3], arr[4] = arr[4], arr[3]

        '''
        min_idx = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_idx]:
                min_idx = j

            # j for문은 여기까지!!!!!!!



        arr[i], arr[min_idx] = arr[min_idx], arr[i]


    return arr

# 실행코드
arr = [5, 4, 3, 1, 2]
print(selection_sort(arr))


