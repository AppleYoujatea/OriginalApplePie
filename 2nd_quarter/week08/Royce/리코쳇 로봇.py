from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(board):
    answer = 0
    
    a = len(board)
    b = len(board[0])
    
    rx, ry = 0, 0
    for i in range(a):
        for j in range(b):
            if board[i][j] == "R":
                rx, ry = i, j
                
    def BFS():
        q = deque()
        q.append((rx, ry))
        check = [[0] * b for _ in range(a)]
        check[rx][ry] = 1
    
        while q:
            px, py = q.popleft()
            if board[px][py] == "G":
                return check[px][py]
            for i in range(4):
                nx, ny = px, py
                while True:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                
                    if 0<=nx<a and 0<=ny<b and board[nx][ny] == "D":
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx < 0 or nx >= a or ny < 0 or ny >= b:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not check[nx][ny]:
                    check[nx][ny] = check[px][py] + 1
                    q.append((nx, ny))
                
        return -1
            
    
    answer = BFS()
    if answer > 0:
        answer -= 1
    
    
    return answer
