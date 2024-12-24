'''
파일명: Ex23-5-MergeSort.py

병합정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각을 재귀적으로 합병 정렬하고, 다시 합치면서 정렬하는 알고리즘
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    '''
        arr = [5, 2, 8, 6, 1, 9, 3, 7]
        mid = 4 
        left = merge_sort(arr[:mid])        -> [2, 5, 6, 8]
            arr = [5, 2, 8, 6]
            mid = 2
            left = merge_sort(arr[:mid]) -> [2, 5]
                arr = [5, 2]
                mid = 1
                left = merge_sort(arr[:mid]) -> [5]
                right = merge_sort(arr[mid:]) -> [2]
                merge([5], [2])     -> [2, 5]
            right = merge_sort(arr[mid:]) -> [6, 8]
                arr = [8, 6]
                mid = 1
                left = merge_sort(arr[:mid]) -> [8]
                right = merge_sort(arr[mid:]) -> [6]
                merge([8], [6])     -> [6, 8]

            merge([2, 5], [6, 8])   -> [2, 5, 6, 8]
        right = merge_sort(arr[:mid])        ->  [1, 3, 7, 9]
            arr = [1, 9, 3, 7]
            mid = 2
            left = merge_sort(arr[:mid]) -> [1, 9]
                arr = [1, 9]
                mid = 1
                left = merge_sort(arr[:mid]) -> [1]
                right = merge_sort(arr[mid:]) -> [9]
                merge([1], [9])     -> [1, 9]
            right = merge_sort(arr[mid:]) -> [3, 7]
                arr = [3, 7]
                mid = 1
                left = merge_sort(arr[:mid]) -> [3]
                right = merge_sort(arr[mid:]) -> [7]
                merge([3], [7])     -> [3, 7]

            merge([1, 9], [3, 7])   -> [1, 3, 7, 9]

        merge([2, 5, 6, 8] , [1, 3, 7, 9]) -> 

        reutnr [1, 2, 3, 5, 6, 7, 8, 9]     

    '''

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    '''
    merge([5], [2])
    left = [5]
    right = [2]
    result = [2, 5]

    left = [2, 5]
    right = [6, 8]
    len(left) = 2
    len(right) = 2
    i = 2
    j = 0
    reuslt = [2, 5, 6, 8]
    '''
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        '''
            left[1] == 5
            right[0] == 6
        '''
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)