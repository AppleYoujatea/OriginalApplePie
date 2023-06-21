"""
레버까지 최소 거리 + 레버부터 출구까지 최소 거리

bfs(start, lever, maps)
bfs(lever, end, maps)
"""

from collections import deque

def bfs(start, end, maps):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append(start)

    dist = [[-1] * len(maps[0]) for _ in range(len(maps))]
    dist[start[0]][start[1]] = 0 # 시작 위치 거리값 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or maps[nx][ny] == "X":
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    return dist[end[0]][end[1]]


def solution(maps):

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)
    
    to_lever = bfs(start, lever, maps)
    to_end = bfs(lever, end, maps)

    if to_lever == -1 or to_end == -1:
        return -1
    else:
        return to_lever + to_end