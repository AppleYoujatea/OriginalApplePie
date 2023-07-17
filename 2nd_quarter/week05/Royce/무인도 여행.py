
from collections import deque
    
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def BFS(maps, i, j, n, m, check):
    queue = deque()
    queue.append((i, j))
    check[i][j] = 1
    s = int(maps[i][j])
    
    while queue:
        x, y = queue.popleft()
        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]
            
            if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 and maps[nx][ny] != 'X':
                check[nx][ny] = 1
                s += int(maps[nx][ny])
                queue.append((nx, ny))
    return s
            


def solution(maps):
    answer = []
    

    
    n, m = len(maps), len(maps[0])
    check = [[0] * m for _ in range(n)]
        
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and check[i][j] == 0:
                answer.append(BFS(maps, i, j, n, m, check))
                
    if answer:
        return sorted(answer)
    else:
        return [-1]
                
