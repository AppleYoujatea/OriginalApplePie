import sys
sys.stdin = open("1749.txt", "r")

"""
풀이 시간: 11:04 ~ 11:59

1. 2차원 누적합 행렬
2. 누적합 행렬로부터 -> 모든 부분 행렬 구함
"""

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# 누적합 행렬
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = graph[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

# 모든 부분 행렬
ans = int(-1e9) # 정답 변수 초기화

for x1 in range(1, n + 1):
    for y1 in range(1, m + 1):
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                ans = max(ans, prefix[x2][y2] + prefix[x1 - 1][y1 - 1] - prefix[x2][y1 - 1] - prefix[x1 - 1][y2])

print(ans)