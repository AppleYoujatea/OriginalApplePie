n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

def fibo(x):
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[x]

print(fibo(n) % 10007)