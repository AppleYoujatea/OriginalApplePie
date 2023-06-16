
"""
1 : 1
2 : 11, 2 = 2
3 : 111, 12 = 2
4 : 1111, 112, 22 = 3
5 : 11111, 1112, 122, 5 = 4
6 : 111111, 11112, 1122, 222, 15 = 5
7 : 1111111, 111112, 11122, 1222, 115, 25 = 6
8 : 11111111, 1111112, 111122, 11222, 2222, 5111, 521 = 7
"""

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for now in range(coin, k + 1):
        dp[now] += dp[now - coin]

print(dp[k])