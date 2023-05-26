import sys
sys.stdin = open("10986.txt", "r")

"""
풀이 시간: 12:11 ~ 

1. 누적합 만듦
2. 구간합 살펴보면서 m으로 나눠떨어지는지
"""

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합
prefix = [0 for _ in range(n + 1)]
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

# 구간합
cnt = 0
for i in range(n):
    for j in range(i, n):
        tmp = prefix[j + 1] - prefix[i]
        if tmp % m == 0:
            cnt += 1

print(cnt)