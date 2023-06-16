N, M = map(int, input().split())
num = [[0] * (N + 1)]

D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    num.append([0] + [int(x) for x in input().split()])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        D[i][j] = D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1] + num[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)
