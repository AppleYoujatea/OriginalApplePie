from collections import deque

def bfs(i, j, visited, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tot = 0

    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        tot += int(maps[x][y])  # visited[x][y] is always True when pop from the queue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < len(maps) and ny >= 0 and ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return tot

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                res = bfs(i, j, visited, maps)
                answer.append(res)
    
    answer.sort() 

    return answer if answer else [-1]

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))
