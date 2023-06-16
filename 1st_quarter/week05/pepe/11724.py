import sys
sys.stdin = open("11724.txt", "r")

"""
n, m = 노드, 간선
무방향 인접 그래프
DFS로 탐색 끝날 때마다 cnt += 1
cnt 출력
"""

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(node)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)