import sys
sys.stdin = open("1253.txt", "r")

"""
풀이 시간: 10:16 ~ 

n = 2000이니까 전부 투포인터 탐색하면 될 듯
"""

N = int(input())

nums = list(map(int, input().split()))
nums.sort()

ans = 0

for i in range(N):
    tmp = nums[:i] + nums[i+1:]
    s = 0
    e = len(tmp) - 1

    while s < e:

        tot = tmp[s] + tmp[e]

        if tot == nums[i]:
            ans += 1
            break

        elif tot < nums[i]:
            s += 1

        else:
            e -= 1

print(ans)