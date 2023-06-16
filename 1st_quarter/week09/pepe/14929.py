import sys
sys.stdin = open('14929.txt', "r")

"""
풀이 시간: 17:20 ~ 17:40

아이디어 안 떠올라서 검색해봄... 분배 법칙 !!
Xn까지 누적합 * Xn+1
"""

n = int(input())
nums = list(map(int, input().split()))

prefix = 0
ans = 0

for i in range(n - 1):
    prefix += nums[i]
    ans += nums[i + 1] * prefix

print(ans)