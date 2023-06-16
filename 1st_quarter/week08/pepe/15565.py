import sys
sys.stdin = open("15565.txt", "r")

"""
풀이 시간: 21:41 ~ 22:16

prefix 배열
1이 k개 미만으로 있으면 j += 1
k개 이상으로 있으면 i += 1 최대한 줄여봄
"""

n, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = int(1e9)
cnt = 0 # 현재 투 포인터에서 라이언 수
i = 0
j = 0

if nums[j] == 1:
    cnt += 1

while j < n:
    if cnt == k:
        
        ans = min(ans, j - i + 1)
        
        if nums[i] == 1:
            cnt -= 1

        i += 1
    
    else:
        j += 1
        if j < n and nums[j] == 1:
            cnt += 1

if ans == int(1e9):
    print(-1)
else:
    print(ans)