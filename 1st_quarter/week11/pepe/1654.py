import sys
sys.stdin = open("1654.txt", "r")

"""
풀이 시간: 15:12 ~

k, n = 영식이 갖고 있는 랜선 개수, 필요한 랜선 개수
k줄에 걸쳐 갖고 있는 랜선의 길이

포인터: 랜선의 최대 길이
"""

k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]

l = 1
r = max(k_list)

while l <= r:

    mid = (l + r) // 2
    tot = 0

    for i in range(k):
        tot += k_list[i] // mid
    
    if tot >= n:
        l = mid + 1
    
    else:
        r = mid - 1

print(r) 
# l이 아닌 이유:
# while을 벗어나면 l > r인 상태
# 위 문제에서는 포인터(랜선의 길이) 값이 작을 수록, 더 많은 개수를 얻을 수 있음
# 최대 개수를 얻는 것이 목표이므로, 더 작은 값인 r을 출력