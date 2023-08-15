"""
풀이 시간: 18:21 ~

BFS
백준에 있는 구슬탈출 문제처럼 한 쪽 방향으로 이동할 수 있는 만큼 이동하기
이동을 다루는 함수를 따로 만들어서 이동시켜야 할 듯 ?

모두 방문했는데 G에 도달하지 못 하면 -1 return
"""
from collections import deque

def solution(board):
    rows, cols = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 로봇 위치(R)과 목표 위치(G) 찾기
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "R":
                start = (i, j)
            if board[i][j] == "G":
                target = (i, j)
    
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, 0)])

    while queue:
        (row, col), moves = queue.popleft()

        # 목표 위치에 도달한 경우
        if (row, col) == target:
            return moves
        
        for dr, dc in directions:
            n_row, n_col = row, col

            # 미끄러지면서 이동
            while 0 <= n_row + dr < rows and 0 <= n_col + dc < cols and board[n_row + dr][n_col + dc] != "D":
                n_row += dr
                n_col += dc
            
            if (n_row, n_col) != (row, col) and not visited[n_row][n_col]:
                visited[n_row][n_col] = True
                queue.append(((n_row, n_col), moves + 1))
    
    return -1