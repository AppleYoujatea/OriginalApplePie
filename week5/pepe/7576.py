import sys
sys.stdin = open("7576.txt", "r")

"""
m, n = 가로, 세로

그래프 탐색하며 토마토 위치 저장
BFS 탐색
n, m에서 return
중간에 return 안 되고 while loop 끝나면 -1 출력
return 되었으면 그래프 다시 탐색
0 있으면 -1 출력 후 종료
탐색 완료했는데 0 없으면 graph[n][m] 출력
"""

from collections import deque

m, n = map(int, input().split())
graph =  [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

# 토마토 위치 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j)) 

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

maxNum = 0
bfs()

for i in range(n):
    maxNum = max(maxNum, max(graph[i]))
    if 0 in graph[i]:
        print(-1)
        break
else:
    print(maxNum - 1)
