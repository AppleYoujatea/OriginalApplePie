"""
풀이 시간: 17:40 ~

이진 탐색의 2가지 방법
1. 재귀
2. 반복문

- 재귀로 구현
def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        binary_search(arr, target, start, mid - 1)
    
    elif arr[mid] < target:
        binary_search(arr, target, mid + 1, end)

- 반복문으로 구현
def binary_search_loop(arr, target, start, end):
    while start < end:
        
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
        
        elif arr[mid] < target:
            start = mid + 1
    
    return None
"""

