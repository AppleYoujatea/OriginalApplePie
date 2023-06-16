import sys
sys.stdin = open("1806.txt", "r")

"""
풀이 시간: 17:10 ~ 17:36

i = 0번째 인덱스
j = 1번째 인덱스

5 1 3  5  10 7  4  9  2  8
5 6 10 15 25 32 36 45 47 55

while i < j
현재 투 포인터의 합이 S 이상이라면 -> 현재까지 가장 짧은 것과의 길이 비교 후 기록 -> i += 1
else: j += 1

다 돌았는데, 가장 짧은 것의 길이가 갱신되지 않았다면 -> 0 출력

--> 부분합을 사용해서 구해야 시간 초과X
"""

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

i = 0
j = 0
ans = 100001
prefix = num_list[0]

while True:
    if prefix >= s:
        ans = min(ans, j - i + 1)
        prefix -= num_list[i]
        i += 1
    else:
        j += 1

        if j == n:
            break

        prefix += num_list[j]

if ans == 100001:
    print(0)
else:
    print(ans)