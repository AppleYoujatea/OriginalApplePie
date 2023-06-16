import sys
sys.stdin = open("1764.txt", "r")

"""
풀이 시간: 12:54 ~ 12 : 56 ~ 13 : 01
듣도 set
보도 set
set(듣도) & set(보도)
"""

n, m = map(int, input().split())

듣도 = set()
보도 = set()

for _ in range(n):
    듣도.add(input())

for _ in range(m):
    보도.add(input())

result = sorted(list(듣도 & 보도)) # 문제 조건 제대로 보지 않아서 오답

print(len(result))
print(*result, sep="\n")