import sys
sys.stdin = open("4963.txt", "r")

"""
while loop으로 계속 입력 받음
0 0을 받으면 종료
8방 탐색
"""

import sys
sys.setrecursionlimit(10 ** 5)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    graph[x][y] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if graph[nx][ny] == 1:
            dfs(nx, ny)

while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    print(cnt)
