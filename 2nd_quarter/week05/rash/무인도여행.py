def solution(maps):
    answer = []
    visited = [[False] * len(maps[i]) for i in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if visited[i][j] == False and maps[i][j] != "X":
                answer.append(bfs(visited, i, j, maps))

    answer.sort()
    if len(answer) == 0:
        answer.append(-1)

    return answer


def bfs(visited, i, j, maps):
    dX = [1, 0, -1, 0]
    dY = [0, 1, 0, -1]
    queue = [[i, j]]
    visited[i][j] = True
    cnt = 0
    while queue:

        x, y = queue.pop(-1)
        cnt += int(maps[x][y])
        for k in range(4):
            nX = x + dX[k]
            nY = y + dY[k]
            if nX < 0 or nX >= len(maps) or nY < 0 or nY >= len(maps[0]) or visited[nX][nY] or maps[nX][nY] == "X":
                continue
            queue.append([nX, nY])
            visited[nX][nY] = True

    return cnt