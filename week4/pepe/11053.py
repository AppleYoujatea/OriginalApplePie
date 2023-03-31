import sys
sys.stdin = open("11053.txt", "r")


"""
dp에는 현재 idx까지 LCS의 길이 저장
현재 idx에 있는 값이, now 값보다 크다면, dp에 += 1
크지 않다면, dp[i]에 dp[i-1] 값 기록
"""


n = int(input())
data = list(map(int, input().split()))

dp = [1] * 1001

for i in range(1, n):
    for j in range(i):
       if data[i] > data[j]:
           dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))
