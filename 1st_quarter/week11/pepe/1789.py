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

"""
풀이 시간: 10:35 ~ 

N개의 자연수를 합으로 나타내는 방법 중 가장 작은 자연수부터 시작하여 계속 더해보면 다음과 같습니다:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 = 190

여기서 합이 190이므로, 남은 200 - 190 = 10을 추가적으로 합에 더할 수 있습니다.
최댓값 N을 구하기 위해서는 남은 값을 더하는 방법을 고려해야 합니다. 남은 값은 10이고, 자연수 중에서 가장 큰 값인 10을 사용하여 합에 더할 수 있습니다.

따라서, S = 200일 때, N의 값은 19이며, 자연수 N개는 1부터 19까지의 수와 10을 포함한 20개의 자연수입니다.
N = 19, 자연수 N개: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10
"""

s = int(input())
tot = 0
n = 1

while tot <= s:     # 현재까지 누적합이, 목표값보다 작거나 같은 경우

    tot += n        # 누적합에 현재 포인터 값을 더함

    if tot <= s:    # 포인터 값을 더한 뒤에, 여전히 목표값보다 작은 경우
        n += 1      # 포인터를 오른쪽으로 이동

# 누적합이 목표값보다 큰 경우 break
# 가장 최근 더한 포인터 값을 지우고, 기존 값 중에 적절한 자연수를 중복해서 더해줌 -> 목표값 달성
# 서로 다른 개수는 포인터 값을 지울 때 -= 1, 중복된 자연수를 중복해서 더할 때 += 0
# 따라서 n - 1
print(n - 1)        