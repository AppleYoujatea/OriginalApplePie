"""
1. 최솟값 찾음
2. 가장 왼쪽 인덱스와 최솟값 인덱스 값 교체
3. 반복

1. i: 0 ~ n - 1 까지 탐색
2. j: i + 1 ~ n 까지 탐색
3. 최솟값 찾기
4. 교체
"""

def selection_sort(arr):

    for i in range(len(arr) - 1):
        min_idx = i

        for j in range(i + 1, len(arr)):

            if arr[min_idx] > arr[j]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

arr = [5, 3, 8, 1, 2, 7]
print(selection_sort(arr))