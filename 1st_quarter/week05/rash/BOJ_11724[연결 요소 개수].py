import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = list([] for _ in range(N + 1))

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0

visit = [False] * (N + 1)


def dfs(x):
    visit[x] = True

    for i in graph[x]:
        if not visit[i]:
            dfs(i)


for i in range(1, N + 1):
    if not visit[i]:
        dfs(i)
        cnt += 1

print(cnt)
