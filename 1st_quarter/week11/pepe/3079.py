import sys
sys.stdin = open("3079.txt", "r")

"""
풀이 시간: 14:21 ~ 

n, m = 입국심사대, 친구
ni = i번째 입국 심사대 소요 시간
"""

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 포인터 == 걸리는 시간의 최솟값을 구하기 위한 범위
l = min(arr)        # 최소 시간: 가장 빠른 심사대에서 1번
r = max(arr) * m    # 최대 시간: 가장 느린 심사대에서 친구 수(m)만큼 심사
ans = r  # =============> 이 부분을 int(1e9)로 수정하면 틀리다고 함. 왜지 ??

 # mid가 목표값과 정확히 일치하는 것X 
 # 최소값을 구할 때는 l == r일 때도 반복하게 하는 것이 개념
while l <= r:

    mid = (l + r) // 2
    tot = 0

    for i in range(n):
        tot += mid // arr[i] # greedy한 풀이

    if tot >= m:            # 모든 친구가 심사 성공
        ans = min(ans, mid) # 현재 중간값(mid)과 가장 최근에 저장된 최솟값을 비교 후, 작은 것 저장
        r = mid - 1
    
    else:
        l = mid + 1

print(ans)