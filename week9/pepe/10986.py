import sys
sys.stdin = open("10986.txt", "r")

"""
풀이 시간: 12:11 ~ 

1. 누적합 만듦
2. 부분합 살펴보면서 m으로 나눠떨어지는지

다른 풀이 봄
1. 부분합: pre[j] - pre[i - 1]
2. 이때 pre[j]와 pre[i-1]의 나머지가 같다면, 서로 뺴면 나머지가 0으로 M으로 나누어 떨어짐
3. M으로 나눠떨어지는 부분합 == 나머지가 동일한 원소끼리 조합 구하기
"""

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 나머지가 같은 원소 저장하는 배열
remainder = [0 for _ in range(m)]
remainder[0] = 1 # 누적합의 첫 번째 항은 0이므로 나머지가 0인 원소라고 치고 += 1

tot = 0
for i in range(n):
    tot += nums[i] # 누적합
    r = tot % m # 나머지
    remainder[r] += 1 # 현재 누적합을 m으로 나눈 나머지에 += 1

# 나머지에 따라 나뉜 누적합 구간들 -> 같은 나머지에서 2개 뽑는 조합
cnt = 0
for size in remainder:
    cnt += size * (size - 1) // 2

print(cnt)